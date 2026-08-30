#!/usr/bin/env python3
"""
Jake's AI Terminal — headless auto-refresh (no browser required).

Runs on a server (e.g. GitHub Actions). Pulls fresh prices (and, in --full
mode, weekly beta/alpha) from Yahoo's public chart API, updates
terminal_data.json, writes version.json, and rebuilds the site.

Design rules (this drives real investment decisions — fail safe, never lie):
  * A price is only written if it is a positive number inside a sane band of
    the stock's own 52-week range. Anything else is skipped and the previous
    good value is kept.
  * If too few tickers refresh successfully (network/API trouble), the run
    ABORTS without writing, so a half-broken pull can never deploy.
  * Holdings (13F) are NOT auto-reparsed here — they change quarterly and a
    bad unattended parse is dangerous. --full only *detects* new filings and
    prints a NOTICE so a reviewed holdings update can follow.

Usage:
  python3 refresh_live.py           # prices only (fast; market-hours cron)
  python3 refresh_live.py --full    # prices + beta/alpha + 13F filing check
"""
import json, os, sys, time, math, urllib.request, urllib.error
from datetime import datetime, timezone

FULL = '--full' in sys.argv
UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
      '(KHTML, like Gecko) Chrome/124.0 Safari/537.36')
CHART = 'https://query1.finance.yahoo.com/v8/finance/chart/{sym}?range={rng}&interval={iv}'
MIN_SUCCESS = 0.80   # abort the whole run if fewer than 80% of tickers refresh

def get_json(url, tries=2):
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': 'application/json'})
            with urllib.request.urlopen(req, timeout=15) as r:
                return json.loads(r.read().decode())
        except Exception as e:
            if i == tries - 1:
                return {'__err': str(e)}
            time.sleep(0.8)
    return None

def chart(sym, rng='5d', iv='1d'):
    # Yahoo uses '-' for class shares etc.; most US tickers pass straight through
    j = get_json(CHART.format(sym=sym.replace('.', '-'), rng=rng, iv=iv))
    try:
        res = j['chart']['result'][0]
        return res
    except Exception:
        return None

def quote(sym):
    """Return (price, dayChgPct, lo52, hi52) or None."""
    res = chart(sym, '5d', '1d')
    if not res:
        return None
    m = res.get('meta', {})
    p = m.get('regularMarketPrice')
    prev = m.get('chartPreviousClose') or m.get('previousClose')
    lo = m.get('fiftyTwoWeekLow'); hi = m.get('fiftyTwoWeekHigh')
    if not isinstance(p, (int, float)) or p <= 0:
        return None
    chg = round((p / prev - 1) * 100, 2) if isinstance(prev, (int, float)) and prev else 0.0
    return (float(p), chg, lo, hi)

def weekly_returns(sym):
    """1Y weekly % returns from adjusted closes, or None if too short."""
    res = chart(sym, '1y', '1wk')
    if not res:
        return None
    try:
        ts = res['timestamp']
        adj = res['indicators']['adjclose'][0]['adjclose']
    except Exception:
        try:
            ts = res['timestamp']; adj = res['indicators']['quote'][0]['close']
        except Exception:
            return None
    series = [(t, c) for t, c in zip(ts, adj) if isinstance(c, (int, float)) and c > 0]
    if len(series) < 21:
        return None
    series.sort()
    rets = {}
    for i in range(1, len(series)):
        t = series[i][0]; prev = series[i - 1][1]; cur = series[i][1]
        wk = datetime.fromtimestamp(t, tz=timezone.utc).strftime('%Y-%U')
        rets[wk] = (cur / prev - 1) * 100
    return rets

def beta_alpha(sym_rets, spy_rets):
    keys = sorted(set(sym_rets) & set(spy_rets))
    if len(keys) < 20:
        return (None, None)
    s = [sym_rets[k] for k in keys]; m = [spy_rets[k] for k in keys]
    n = len(keys)
    ms = sum(s) / n; mm = sum(m) / n
    cov = sum((s[i] - ms) * (m[i] - mm) for i in range(n)) / n
    var = sum((m[i] - mm) ** 2 for i in range(n)) / n
    if var == 0:
        return (None, None)
    beta = cov / var
    alpha = (ms - beta * mm) * 52
    return (round(beta, 2), round(alpha, 1))

def sane(p, lo, hi):
    """Reject an obviously-wrong quote using the stock's own 52wk range."""
    if not isinstance(p, (int, float)) or p <= 0:
        return False
    if isinstance(lo, (int, float)) and isinstance(hi, (int, float)) and hi > 0:
        return (lo * 0.5) <= p <= (hi * 1.5)
    return True  # no range available -> accept a positive number

def main():
    d = json.load(open('terminal_data.json'))
    rows = d['radar']['rows']
    dossiers = d.get('dossiers', [])

    universe = []
    seen = set()
    for r in rows:
        if r[0] not in seen:
            universe.append(r[0]); seen.add(r[0])
    for x in dossiers:
        if x['sym'] not in seen:
            universe.append(x['sym']); seen.add(x['sym'])

    print(f"[{datetime.now(timezone.utc).isoformat()}] mode={'FULL' if FULL else 'prices'} "
          f"tickers={len(universe)}")

    # ---- prices ----
    px = {}
    ok = 0
    for i, sym in enumerate(universe):
        q = quote(sym)
        if q and sane(q[0], q[2], q[3]):
            px[sym] = q; ok += 1
        time.sleep(0.12)
        if (i + 1) % 40 == 0:
            print(f"  ...{i+1}/{len(universe)} ({ok} ok)")
    rate = ok / max(1, len(universe))
    print(f"prices: {ok}/{len(universe)} ok ({rate:.0%})")
    if rate < MIN_SUCCESS:
        print(f"ABORT: success rate {rate:.0%} below {MIN_SUCCESS:.0%} — keeping last-good data, not deploying.")
        sys.exit(1)

    # ---- beta / alpha (full mode) ----
    ba = {}
    if FULL:
        print("computing beta/alpha vs SPY (weekly, 1Y)...")
        spy = weekly_returns('SPY')
        if spy:
            for i, sym in enumerate(universe):
                sr = weekly_returns(sym)
                if sr:
                    b, a = beta_alpha(sr, spy)
                    if b is not None:
                        ba[sym] = {'beta': b, 'alpha': a}
                time.sleep(0.12)
                if (i + 1) % 40 == 0:
                    print(f"  beta ...{i+1}/{len(universe)} ({len(ba)} ok)")
            print(f"beta/alpha: {len(ba)} names")
        else:
            print("WARN: could not fetch SPY history — skipping beta/alpha this run.")

    # ---- write into the data model (mirrors refresh_prices.py) ----
    for r in rows:
        q = px.get(r[0])
        if q and r[3]:
            p = q[0]; r[9] = round(p, 4); r[10] = round((p / r[3] - 1) * 100); r[11] = q[1]
        elif q:
            r[9] = round(q[0], 4); r[11] = q[1]
        b = ba.get(r[0])
        if b:
            r[12] = b['beta']; r[13] = b['alpha']
    for x in dossiers:
        q = px.get(x['sym'])
        if q:
            x['price'] = round(q[0], 4)
            rk = x.setdefault('risk', {}); rk['last'] = round(q[0], 4)
            if isinstance(q[2], (int, float)): rk['lo52'] = round(q[2], 2)
            if isinstance(q[3], (int, float)): rk['hi52'] = round(q[3], 2)
            if isinstance(q[2], (int, float)) and isinstance(q[3], (int, float)) and q[3] > q[2]:
                rk['pos52'] = round((q[0] - q[2]) / (q[3] - q[2]), 3)
        b = ba.get(x['sym'])
        if b:
            rk = x.setdefault('risk', {}); rk['beta'] = b['beta']; rk['alpha'] = b['alpha']

    now = datetime.now(timezone.utc)
    stamp = now.strftime('%Y-%m-%d %H:%M UTC')
    d['radar']['priceAsOf'] = stamp
    d['priceStamp'] = stamp
    d['lastUpdated'] = now.strftime('%Y%m%d%H%M%S')

    # ---- 13F new-filing detector (full mode; detect only, never auto-reparse) ----
    if FULL:
        ciks = d.get('fundCIKs')  # {fundShort: "0000000000"}
        if ciks:
            newf = []
            marker = d.get('lastFilingSeen', {})
            for name, cik in ciks.items():
                sub = get_json(f'https://data.sec.gov/submissions/CIK{int(cik):010d}.json')
                try:
                    forms = sub['filings']['recent']
                    for form, dt, acc in zip(forms['form'], forms['filingDate'], forms['accessionNumber']):
                        if form.startswith('13F-HR') and dt > marker.get(name, '2026-08-15'):
                            newf.append((name, dt, acc)); break
                except Exception:
                    pass
                time.sleep(0.15)
            if newf:
                print("NOTICE: new 13F filings detected (holdings update is a reviewed step, not auto-applied):")
                for n, dt, acc in newf:
                    print(f"   - {n}: {form} filed {dt} ({acc})")
                d['pendingFilings'] = [{'fund': n, 'date': dt} for n, dt, acc in newf]
        else:
            print("13F check skipped: no fundCIKs map in terminal_data.json (holdings stay on the reviewed quarterly path).")

    json.dump(d, open('terminal_data.json', 'w'))
    json.dump({'ts': d['lastUpdated'], 'priceAsOf': stamp,
               'names': ok}, open('version.json', 'w'))
    print(f"wrote terminal_data.json + version.json (asOf {stamp})")

    # ---- rebuild ----
    import subprocess
    r = subprocess.run([sys.executable, 'build_v2.py'], capture_output=True, text=True)
    print(r.stdout.strip()[-400:])
    if r.returncode != 0:
        print("BUILD FAILED:\n" + r.stderr[-1000:]); sys.exit(1)
    import shutil
    shutil.copy('Jakes_AI_Terminal.html', 'index.html')
    print("deployed -> index.html")

if __name__ == '__main__':
    main()
