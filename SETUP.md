# Putting Jake's AI Terminal online (auto-updating)

This turns your terminal into a real website with its own URL that **refreshes its
own prices on a schedule** — no need to open your laptop or click "go." It's free.

**How it works, in one line:** the files live in a free GitHub repository, GitHub's
built-in scheduler (Actions) re-pulls prices every 15 minutes during market hours and
rebuilds the page, and GitHub Pages serves it at a public URL. When new prices deploy,
anyone with the page open sees a small "🔄 New prices available" button.

**What updates automatically vs. not** (worth remembering):
- **Prices, day-change, 52-week position** → every 15 min during US market hours.
- **Beta / alpha** → recomputed weekly (Sunday).
- **Holdings (which funds own what), survival scores, dossiers** → these come from 13F
  filings, which only change **once a quarter** (next: mid-November). The site *detects*
  a new filing and flags it, but the actual holdings update stays a reviewed step we do
  together — that's deliberate, so an unattended script never writes a wrong holding into
  a tool you trade on.

---

## One-time setup (about 10 minutes)

### 1. Get a GitHub account
If you don't have one, go to **github.com** and sign up (free).

### 2. Create a repository
- Click the **+** (top-right) → **New repository**.
- Name it something like **`ai-terminal`**.
- Set it to **Public** (required for free GitHub Pages).
- Click **Create repository**.

### 3. Upload the files
On the new repo's page, click **"uploading an existing file"** (or **Add file → Upload
files**). Drag in **all** of these from the bundle:
- `index.html`
- `Jakes_AI_Terminal.html`
- `build_v2.py`
- `terminal_data.json`
- `refresh_live.py`
- `version.json`

Click **Commit changes**.

> The workflow file sits in a special folder. Easiest way: click **Add file → Create new
> file**, and in the filename box type exactly:
> ```
> .github/workflows/refresh.yml
> ```
> (typing the `/`s creates the folders). Then paste the contents of the `refresh.yml`
> from the bundle and **Commit**.
>
> *Or*, if you use **GitHub Desktop** or `git`, just drop the whole bundle folder in and
> push — the `.github/workflows/refresh.yml` comes along automatically.

### 4. Let the scheduler save its updates
- Go to **Settings → Actions → General**.
- Scroll to **Workflow permissions**, choose **"Read and write permissions"**, **Save**.

(This lets the auto-refresh commit the new prices back to the repo.)

### 5. Turn on the website
- Go to **Settings → Pages**.
- Under **Source**, pick **Deploy from a branch**.
- Branch: **main**, folder: **/(root)**. **Save**.
- After a minute, your site is live at:
  **`https://<your-username>.github.io/ai-terminal/`**

### 6. Turn on the schedule (and test it)
- Go to the **Actions** tab. If it asks, click to **enable workflows**.
- Click **"Refresh terminal"** on the left → **Run workflow** → **Run workflow**.
- Watch it run (green check = success). It pulls fresh prices, rebuilds, and commits.
- From now on it runs itself every 15 minutes during market hours.

**That's it.** Bookmark your Pages URL. It stays current on its own.

---

## Good to know

- **Off-hours:** nothing moves overnight or on weekends, so the schedule only runs during
  US market hours — that keeps it fast and quiet.
- **The refresh is fail-safe.** Every price is checked against that stock's own 52-week
  range before it's written; a bad or missing quote is skipped and the last good number is
  kept. If more than ~20% of names fail to pull, the run **aborts without deploying** — so a
  half-broken update can never reach the live site.
- **Data source:** free public market data (Yahoo's chart API) for prices and history, and
  the SEC's official API for filings. No API key, no cost. If Yahoo ever gets flaky we can
  switch the price source to a free keyed API (Finnhub) by adding one repo secret.
- **Want a custom domain** (e.g. `terminal.yoursite.com`)? GitHub Pages supports it under
  **Settings → Pages → Custom domain** — say the word and I'll walk you through it.
- **Quarterly holdings update:** when the November 13Fs land, we refresh holdings together
  in a session (same as now), I push the updated `terminal_data.json`, and the live site
  picks it up on its next run.

## If something looks wrong
- **Site shows old prices:** open the Actions tab and check the latest run is green. If a run
  is red, open it — the log says exactly which step failed.
- **"Run workflow" button missing:** make sure `.github/workflows/refresh.yml` is in the repo
  and the Actions tab is enabled.
- **Prices didn't change:** outside market hours that's expected. During market hours, trigger
  a manual run to confirm.
