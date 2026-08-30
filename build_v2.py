#!/usr/bin/env python3
import os as _os
_D = _os.path.dirname(_os.path.abspath(__file__))
DATA = open(_os.path.join(_D, 'terminal_data.json')).read()

HTML = r"""<!doctype html>
<html lang="en" data-theme="light"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Jake's AI Terminal — specialist small/mid-cap intelligence</title>
<style>
:root{color-scheme:light;
 --s0:#f4f3f0;--s1:#fcfcfb;--s2:#eeedea;--s3:#e6e5e1;--line:#e2e1dc;--lines:#cfcec8;
 --t1:#0b0b0b;--t2:#52514e;--t3:#84837c;
 --good:#008300;--warn:#c98500;--bad:#e34948;--blue:#2a78d6;--pur:#8a7fd4;
 --r100:#cde2fb;--r250:#86b6ef;--r400:#3987e5;--r550:#1c5cab;--r650:#104281;
 --sh:0 1px 2px rgba(0,0,0,.05),0 8px 24px rgba(0,0,0,.06)}
:root[data-theme="dark"]{color-scheme:dark;
 --s0:#111110;--s1:#1a1a19;--s2:#232322;--s3:#2b2b2a;--line:#333331;--lines:#4a4a47;
 --t1:#fff;--t2:#c3c2b7;--t3:#8f8e85;
 --good:#3ba33b;--warn:#d99a12;--bad:#e66767;--blue:#3987e5;--pur:#9d92e0;
 --r100:#184f95;--r250:#1c5cab;--r400:#2a78d6;--r550:#5598e7;--r650:#86b6ef;
 --sh:0 1px 2px rgba(0,0,0,.4),0 8px 24px rgba(0,0,0,.35)}
*{box-sizing:border-box}
body{margin:0;background:var(--s0);color:var(--t1);font:14px/1.5 ui-sans-serif,-apple-system,"Segoe UI",Inter,Roboto,Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased}
.wrap{max-width:1560px;margin:0 auto;padding:0 18px 90px}
h1{font-size:17px;margin:0;letter-spacing:-.01em;white-space:nowrap}
h1 b{color:var(--blue)}
h2{font-size:15px;margin:0 0 3px;letter-spacing:-.01em}
h3{font-size:13px;margin:0}
.sub{font-size:11.5px;color:var(--t3);line-height:1.5}
header{position:sticky;top:0;z-index:70;background:var(--s1);border-bottom:1px solid var(--line)}
.hdr{max-width:1560px;margin:0 auto;padding:10px 18px;display:flex;align-items:center;gap:12px;flex-wrap:wrap}
.spacer{flex:1}
#cmd{background:var(--s2);border:1px solid var(--line);color:var(--t1);border-radius:8px;padding:7px 11px;font-size:12.5px;font-family:inherit;min-width:250px}
#cmd:focus{outline:none;border-color:var(--blue)}
.pill{font-size:10.5px;color:var(--t2);background:var(--s2);border:1px solid var(--line);border-radius:999px;padding:3px 9px;white-space:nowrap}
.pill.hot{border-color:var(--warn);color:var(--warn)}
.btn{background:var(--s2);border:1px solid var(--line);color:var(--t2);border-radius:8px;padding:6px 11px;font-size:12px;cursor:pointer;font-family:inherit;white-space:nowrap}
.btn:hover{border-color:var(--lines);color:var(--t1)}
.btn.on{background:var(--blue);border-color:var(--blue);color:#fff}
nav{display:flex;gap:1px;border-bottom:1px solid var(--line);overflow-x:auto;position:sticky;top:49px;background:var(--s0);z-index:60;-webkit-overflow-scrolling:touch}
nav button{background:none;border:none;border-bottom:2px solid transparent;color:var(--t2);padding:11px 14px;font-size:13px;font-weight:500;cursor:pointer;white-space:nowrap;margin-bottom:-1px;font-family:inherit}
nav button:hover{color:var(--t1)} nav button.on{color:var(--t1);border-bottom-color:var(--blue)}
section{padding-top:18px}
.card{background:var(--s1);border:1px solid var(--line);border-radius:12px;padding:17px 19px;box-shadow:var(--sh);margin-bottom:13px}
.grid{display:grid;gap:13px}.g2{grid-template-columns:1fr 1fr}.g3{grid-template-columns:repeat(3,1fr)}
.tiles{display:grid;gap:11px;grid-template-columns:repeat(auto-fit,minmax(176px,1fr))}
.tile{background:var(--s1);border:1px solid var(--line);border-radius:11px;padding:13px 15px}
.tile .lab{font-size:10.5px;color:var(--t3);letter-spacing:.03em;text-transform:uppercase}
.tile .val{font-size:23px;font-weight:600;margin-top:4px;letter-spacing:-.02em}
.tile .dlt{font-size:11.5px;color:var(--t2);margin-top:3px;line-height:1.45}
.note{font-size:12.5px;color:var(--t2);line-height:1.7}.note b{color:var(--t1);font-weight:600}
.crow{display:grid;grid-template-columns:104px 1fr 112px;align-items:center;gap:10px;padding:3px 0}
.cnm{font-size:12.5px;font-weight:600;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;cursor:pointer}
.cnm:hover{color:var(--blue)}
.ctrack{position:relative;height:17px;background:var(--s2);border-radius:3px}
.cfill{position:absolute;left:0;top:0;height:100%;border-radius:0 4px 4px 0}
.cfill.g{background:var(--good)}.cfill.w{background:var(--warn)}.cfill.b{background:var(--bad)}.cfill.n{background:var(--r400)}
.cmark{position:absolute;top:-3px;bottom:-3px;width:2px;background:var(--t1);opacity:.75}
.cmark::after{content:'';position:absolute;top:-3px;left:-3px;width:8px;height:8px;border-radius:50%;background:var(--t1)}
.cval{font-size:11.5px;text-align:right;font-variant-numeric:tabular-nums;color:var(--t2)}
.dvtrack{position:relative;height:17px;background:var(--s2);border-radius:3px;overflow:hidden}
.dvbar{position:absolute;top:0;height:100%}.dvzero{position:absolute;top:0;bottom:0;width:1px;background:var(--lines)}
.legend{display:flex;gap:14px;flex-wrap:wrap;font-size:11.5px;color:var(--t2);margin-top:12px}
.legend span{display:inline-flex;align-items:center;gap:6px}
.key{width:11px;height:11px;border-radius:3px;display:inline-block}
.axisnote{font-size:11px;color:var(--t3);margin-top:10px;line-height:1.55}
.tw{background:var(--s1);border:1px solid var(--line);border-radius:12px;overflow:auto;box-shadow:var(--sh);max-height:70vh}
table{width:100%;border-collapse:separate;border-spacing:0;font-variant-numeric:tabular-nums}
th{position:sticky;top:0;background:var(--s1);border-bottom:1px solid var(--lines);font-size:10px;font-weight:600;letter-spacing:.05em;text-transform:uppercase;color:var(--t3);padding:8px 9px;text-align:right;white-space:nowrap;cursor:pointer;user-select:none;z-index:2}
th.l{text-align:left}th:hover{color:var(--t1)}
td{padding:8px 9px;border-bottom:1px solid var(--line);text-align:right;white-space:nowrap;font-size:12.5px}
td.l{text-align:left}tr:hover td{background:var(--s2)}
.tk{font-weight:600;cursor:pointer}.tk:hover{color:var(--blue);text-decoration:underline}
.iss{color:var(--t2);max-width:230px;overflow:hidden;text-overflow:ellipsis;display:inline-block;vertical-align:bottom}
.chip{display:inline-block;font-size:9.5px;font-weight:700;letter-spacing:.05em;padding:2px 6px;border-radius:4px;border:1px solid var(--lines);color:var(--t2);background:var(--s2);text-transform:uppercase}
.chip.g{border-color:var(--good);color:var(--good)}.chip.w{border-color:var(--warn);color:var(--warn)}
.chip.b{border-color:var(--bad);color:var(--bad)}.chip.n{border-color:var(--r400);color:var(--r400)}
.chip.p{border-color:var(--pur);color:var(--pur)}
.pos{color:var(--good)}.neg{color:var(--bad)}.mut{color:var(--t3)}
.toolbar{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin-bottom:11px}
.toolbar input,.toolbar select{background:var(--s1);border:1px solid var(--line);color:var(--t1);border-radius:8px;padding:7px 10px;font-size:12.5px;font-family:inherit}
.cnt{font-size:11.5px;color:var(--t3);margin-left:auto;font-variant-numeric:tabular-nums}
/* company panel */
#ov{position:fixed;inset:0;background:rgba(0,0,0,.42);z-index:200;display:none;backdrop-filter:blur(2px)}
#ov.on{display:block}
#pan{position:fixed;top:0;right:0;bottom:0;width:min(880px,100%);background:var(--s0);z-index:201;transform:translateX(102%);transition:transform .22s ease;overflow-y:auto;box-shadow:-8px 0 40px rgba(0,0,0,.22)}
#pan.on{transform:none}
.phead{position:sticky;top:0;background:var(--s1);border-bottom:1px solid var(--line);padding:15px 20px;display:flex;align-items:flex-start;gap:14px;z-index:5;flex-wrap:wrap}
@media(max-width:560px){.phead{padding:13px 14px;gap:10px}.phead .btn{padding:5px 9px;font-size:11px}}
.pbody{padding:18px 20px 70px}
.sec{margin-bottom:18px}
.sec h4{margin:0 0 8px;font-size:10.5px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--t3)}
.prose{font-size:13px;line-height:1.7;color:var(--t2)}
.kv{display:grid;grid-template-columns:repeat(auto-fit,minmax(138px,1fr));gap:1px;background:var(--line);border:1px solid var(--line);border-radius:8px;overflow:hidden}
.kv div{background:var(--s1);padding:8px 10px}
.kv .k{font-size:10px;color:var(--t3);text-transform:uppercase;letter-spacing:.03em}
.kv .v{font-size:13.5px;font-weight:600;margin-top:2px;font-variant-numeric:tabular-nums}
.surv{background:var(--s2);border:1px solid var(--line);border-radius:10px;padding:13px 15px}
.surv .big{font-size:20px;font-weight:600;letter-spacing:-.02em}
.deriv{font-size:11.5px;color:var(--t3);line-height:1.65;margin-top:9px;padding-top:9px;border-top:1px dashed var(--lines)}
ul.bb{margin:0;padding-left:16px;font-size:12.5px;line-height:1.65;color:var(--t2)}ul.bb li{margin-bottom:7px}
.bull{border-left:3px solid var(--good);padding-left:12px}.bear{border-left:3px solid var(--bad);padding-left:12px}
.flags{background:color-mix(in srgb,var(--warn) 9%,var(--s1));border:1px solid color-mix(in srgb,var(--warn) 35%,var(--line));border-radius:9px;padding:11px 14px}
.flags.crit{background:color-mix(in srgb,var(--bad) 9%,var(--s1));border-color:color-mix(in srgb,var(--bad) 40%,var(--line))}
.flags ul{margin:0;padding-left:16px;font-size:12.5px;line-height:1.6;color:var(--t2)}.flags li{margin-bottom:5px}
.fcard{background:var(--s1);border:1px solid var(--line);border-radius:12px;padding:15px 17px;box-shadow:var(--sh)}
.mx{width:auto;border-collapse:separate;border-spacing:2px;font-size:11.5px}
.mx th,.mx td{padding:0;position:static;background:none;border:0;cursor:default}
.mx th.rh{text-align:right;padding-right:8px;color:var(--t2);font-weight:400;font-size:11.5px;text-transform:none;letter-spacing:0}
.mx th.ch{color:var(--t2);font-weight:400;font-size:10.5px;text-transform:none;letter-spacing:0;height:78px;vertical-align:bottom;padding-bottom:5px}
.mx th.ch span{display:inline-block;writing-mode:vertical-rl;transform:rotate(180deg);white-space:nowrap}
.mx td.cl{width:52px;height:30px;border-radius:4px;text-align:center;font-variant-numeric:tabular-nums}
.hide{display:none}
.cmpsel{display:grid;grid-template-columns:1fr auto 1fr;gap:9px;align-items:center}
.cmpsel select{background:var(--s2);border:1px solid var(--line);color:var(--t1);border-radius:8px;padding:9px 11px;font-size:13.5px;font-family:inherit;font-weight:600;width:100%}
.cmpsel select:focus{outline:none;border-color:var(--blue)}
.ch2{display:grid;grid-template-columns:1fr auto 1fr;gap:12px;align-items:stretch}
.chcard{background:var(--s2);border:1px solid var(--line);border-radius:10px;padding:13px 15px}
.chcard .nm{font-size:15px;font-weight:600;letter-spacing:-.01em}
.chcard .mt{font-size:11.5px;color:var(--t3);margin-top:2px}
.chvs{align-self:center;font-size:11px;color:var(--t3);font-weight:700;letter-spacing:.08em}
.crt{width:100%;border-collapse:separate;border-spacing:0}
.crt td,.crt th{padding:8px 11px;border-bottom:1px solid var(--line);font-size:12.5px;font-variant-numeric:tabular-nums}
.crt th{text-align:left;font-size:10px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--t3);background:var(--s1);position:sticky;top:0}
.crt td.lb{color:var(--t2);width:36%;text-align:center;font-weight:500}
.crt td.va{text-align:right;width:32%;font-weight:600}
.crt td.vb{text-align:left;width:32%;font-weight:600}
.crt th.hva{text-align:right}.crt th.hvb{text-align:left}
.crt .wpill{display:inline-block;background:color-mix(in srgb,var(--good) 15%,transparent);color:var(--good);border-radius:6px;padding:2px 9px;font-weight:700}
.crt .wpill *{color:inherit}
.crt .wpill::before{content:'▲ ';font-size:8px;vertical-align:1px}
.cmpwrap{max-width:860px;margin:0 auto}
.tabintro{display:flex;gap:10px;align-items:baseline;background:var(--s1);border:1px solid var(--line);border-left:3px solid var(--blue);border-radius:9px;padding:10px 14px;margin-bottom:13px;font-size:12.5px;line-height:1.5}
.tabintro b{color:var(--t1);font-weight:600;white-space:nowrap}
.tabintro span{color:var(--t2)}
/* buy-zone shortlist */
.bz{display:flex;gap:12px;align-items:center;padding:12px 4px;border-bottom:1px solid var(--line);cursor:pointer}
.bz:hover{background:var(--s2)}
.bzrank{flex:none;width:26px;height:26px;border-radius:50%;background:var(--good);color:#fff;font-weight:700;font-size:12px;display:flex;align-items:center;justify-content:center}
.bzmain{flex:1;min-width:0}
.bztk{font-weight:700;font-size:14px;color:var(--t1)}
.bznm{font-size:11.5px;color:var(--t3)}
.bzgates{display:flex;gap:6px;flex-wrap:wrap;margin-top:4px}
.bzg{font-size:10.5px;color:var(--t2);background:var(--s2);border:1px solid var(--line);border-radius:5px;padding:2px 7px;white-space:nowrap}
.bzg b{color:var(--good);font-weight:600}
.bzmini{flex:none;text-align:right}
.bzmini .v{font-size:16px;font-weight:700;color:var(--t1)}
.bzmini .l{font-size:10px;color:var(--t3);text-transform:uppercase;letter-spacing:.04em}
.bzempty{color:var(--t2);font-size:13px;padding:14px 4px}
.bz{flex-wrap:wrap}
.bzwarn{flex-basis:100%;margin-top:8px;font-size:11.5px;line-height:1.5;color:var(--bad);background:color-mix(in srgb,var(--bad) 8%,transparent);border:1px solid color-mix(in srgb,var(--bad) 35%,transparent);border-radius:8px;padding:8px 11px}
.mvlensbar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:6px 0 10px}
.mvlens{background:var(--s2);border:1px solid var(--line);color:var(--t2);border-radius:999px;padding:5px 13px;font-size:12px;cursor:pointer;font-family:inherit}
.mvlens.on{background:var(--blue);border-color:var(--blue);color:#fff;font-weight:600}
.mvlenshint{font-size:11px;color:var(--t3);flex:1;min-width:200px;line-height:1.4}
.mvgrouplab{font-size:11px;text-transform:uppercase;letter-spacing:.04em;color:var(--t3);margin:8px 0 2px;font-weight:600}
.ftag{display:inline-block;font-size:10px;font-weight:700;padding:1px 7px;border-radius:5px;letter-spacing:.02em;vertical-align:middle}
.mvstrip{display:flex;flex-wrap:wrap;gap:7px;margin:4px 0 4px}
.mvfund{display:inline-flex;align-items:center;gap:6px;font-size:11.5px;padding:5px 10px;border-radius:999px;border:1px solid var(--line);background:var(--s1)}
.mvfund .dot{width:7px;height:7px;border-radius:50%;flex:none}
.mvfund .fnew{font-size:9px;font-weight:700;color:var(--blue);border:1px solid color-mix(in srgb,var(--blue) 45%,transparent);border-radius:4px;padding:0 4px}
.mvsec{margin-top:20px}
.mvsec>h3{font-size:13px;margin:0 0 4px;display:flex;align-items:center;gap:8px}
.mvsec .msub{font-size:11.5px;color:var(--t3);margin-bottom:8px}
.mvitem{display:flex;align-items:baseline;gap:10px;padding:9px 2px;border-bottom:1px solid var(--line);font-size:12.5px;line-height:1.5}
.mvitem .mvtk{font-weight:700;min-width:58px;cursor:pointer;color:var(--t1)}
.mvchip{display:inline-block;font-size:10px;font-weight:700;padding:1px 7px;border-radius:5px;white-space:nowrap;letter-spacing:.02em}
.mvname{display:flex;flex-wrap:wrap;gap:6px;align-items:center;padding:9px 2px;border-bottom:1px solid var(--line)}
.mvname .mvtk{font-weight:700;min-width:56px;cursor:pointer}
.mvpend{font-size:11px;color:var(--t3)}
.mvdiv{font-size:11px;color:var(--warn);font-weight:600}
.bznote{font-size:11.5px;color:var(--t3);margin-top:11px;line-height:1.5}
.bzalt{display:inline-block;font-size:11px;color:var(--t2);background:var(--s2);border:1px solid var(--line);border-radius:5px;padding:2px 8px;margin:3px 4px 0 0;cursor:pointer}
.bzalt:hover{border-color:var(--lines);color:var(--t1)}
/* multi-quarter trajectory */
.traj{display:inline-flex;gap:2px;align-items:flex-end;height:20px;vertical-align:middle}
.traj i{display:block;width:7px;border-radius:1px 1px 0 0}
.trajlab{font-size:10.5px;font-weight:600;margin-left:6px;vertical-align:middle}
/* Learn mode: click-to-explain */
#learnBtn.on{background:var(--blue);border-color:var(--blue);color:#fff}
.xp{cursor:inherit}
body.learn .xp{cursor:help;border-bottom:1.5px dotted var(--blue);background:color-mix(in srgb,var(--blue) 8%,transparent);border-radius:2px;padding:0 1px}
body.learn .xp:hover{background:color-mix(in srgb,var(--blue) 18%,transparent)}
.learnhint{display:none;background:var(--s2);border:1px solid var(--blue);border-radius:9px;padding:9px 13px;margin-bottom:13px;font-size:12.5px;color:var(--t2);line-height:1.5}
body.learn .learnhint{display:block}
.learnhint b{color:var(--blue)}
#xpPop{position:fixed;z-index:200;max-width:320px;background:var(--s1);border:1px solid var(--lines);border-radius:11px;box-shadow:var(--sh);padding:14px 16px;opacity:0;transform:translateY(4px);transition:opacity .1s,transform .1s;pointer-events:none}
#xpPop.on{opacity:1;transform:none;pointer-events:auto}
#xpPop .xpt{font-size:14px;font-weight:700;color:var(--t1);margin-bottom:5px}
#xpPop .xpd{font-size:12.5px;color:var(--t2);line-height:1.55}
#xpPop .xpd b{color:var(--t1);font-weight:600}
#xpPop .xpx{position:absolute;top:9px;right:11px;color:var(--t3);cursor:pointer;font-size:15px;line-height:1}
#xpPop .xpmore{margin-top:9px;font-size:11px;color:var(--t3)}
/* survival score scale */
.sscale{display:inline-block;vertical-align:middle}
.sstrack{display:block;position:relative;width:100%;height:7px;border-radius:4px;
 background:linear-gradient(90deg,var(--bad) 0%,var(--bad) 47.8%,var(--warn) 47.8%,var(--warn) 73.9%,var(--good) 73.9%,var(--good) 100%);opacity:.85}
.ssmark{position:absolute;top:-3px;width:3px;height:13px;background:var(--t1);border-radius:2px;transform:translateX(-1.5px);box-shadow:0 0 0 2px var(--s1)}
.ssends{display:flex;justify-content:space-between;font-size:9px;color:var(--t3);margin-top:3px;text-transform:uppercase;letter-spacing:.03em}
.ssends span{flex:1}.ssends span:nth-child(2){text-align:center}.ssends span:nth-child(3){text-align:right}
.ssrow{display:flex;align-items:center;gap:9px}
.ssnum{font-size:19px;font-weight:700;line-height:1}
.sslabel{font-size:11px;font-weight:600}
.scalecard .leg{display:flex;gap:16px;flex-wrap:wrap;font-size:11.5px;color:var(--t2);margin-top:10px}
.scalecard .leg b{color:var(--t1)}
/* market / regulatory / financing */
.mrf{display:flex;flex-direction:column;gap:2px}
.mrfrow{display:grid;grid-template-columns:118px 1fr;gap:14px;padding:11px 2px;border-bottom:1px solid var(--line);align-items:baseline}
.mrfrow:last-child{border-bottom:none}
.mrfl{font-size:10.5px;text-transform:uppercase;letter-spacing:.04em;color:var(--t3);font-weight:600}
.mrfr{font-size:12.5px;color:var(--t1)}
.mrfd{font-size:12px;color:var(--t2);line-height:1.55;margin-top:4px}
.mtag{display:inline-block;font-size:10px;font-weight:700;text-transform:uppercase;letter-spacing:.03em;padding:2px 8px;border-radius:5px;background:var(--s2);border:1px solid var(--lines);color:var(--t2);margin-right:5px}
.fdatag{display:inline-block;font-size:11px;padding:2px 8px;border-radius:5px;background:color-mix(in srgb,var(--good) 12%,transparent);border:1px solid color-mix(in srgb,var(--good) 40%,transparent);color:var(--good);margin:2px 4px 2px 0}
@media(max-width:560px){.mrfrow{grid-template-columns:1fr;gap:3px}}
/* financial statements */
.fintbl{margin-top:14px}
.fintbl:first-child{margin-top:2px}
.fintname{font-size:12px;font-weight:700;color:var(--t1);text-transform:uppercase;letter-spacing:.03em;margin-bottom:6px}
.finscroll{overflow-x:auto;border:1px solid var(--line);border-radius:8px}
table.fin{border-collapse:collapse;width:100%;font-size:12.5px;min-width:440px}
table.fin th,table.fin td{padding:7px 12px;text-align:right;white-space:nowrap;border-bottom:1px solid var(--line)}
table.fin thead th{font-size:10px;text-transform:uppercase;letter-spacing:.04em;color:var(--t3);font-weight:600;background:var(--s2);position:sticky;top:0}
table.fin tbody tr:last-child td{border-bottom:none}
table.fin tbody tr:nth-child(even) td{background:color-mix(in srgb,var(--s2) 45%,transparent)}
table.fin td.finlab,table.fin th.finlab{text-align:left;color:var(--t1);font-weight:500;position:sticky;left:0;background:var(--s1)}
table.fin tbody tr:nth-child(even) td.finlab{background:color-mix(in srgb,var(--s2) 92%,var(--s1))}
table.fin td.neg{color:var(--bad)}
.gh{font-size:15px;margin:0 0 4px}
.glegend{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:11px;margin-top:12px}
.gitem{display:flex;gap:11px;align-items:flex-start}
.gsw{flex:none;width:26px;height:18px;border-radius:5px;margin-top:1px;border:1px solid var(--line)}
.gdot{flex:none;width:18px;height:18px;border-radius:50%;margin-top:1px}
.gitem .gt{font-size:12.5px;color:var(--t1);font-weight:600}
.gitem .gd{font-size:12px;color:var(--t2);line-height:1.5}
.ggroup{margin-top:16px}
.ggroup h4{font-size:11px;text-transform:uppercase;letter-spacing:.05em;color:var(--t3);margin:0 0 2px;border-bottom:1px solid var(--line);padding-bottom:6px}
.gterm{display:grid;grid-template-columns:190px 1fr;gap:14px;padding:9px 2px;border-bottom:1px solid var(--line);align-items:baseline}
.gterm .k{font-weight:600;color:var(--t1);font-size:12.5px}
.gterm .k .sub2{display:block;font-weight:400;color:var(--t3);font-size:10.5px;margin-top:1px}
.gterm .d{color:var(--t2);font-size:12.5px;line-height:1.55}
.gterm .d b{color:var(--t1);font-weight:600}
@media(max-width:640px){.gterm{grid-template-columns:1fr;gap:2px}}
.crt tr:hover td{background:var(--s2)}
.crt tr.grp td{background:var(--s2);font-size:10px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--t3);padding:7px 11px;text-align:center}
.nar{display:grid;grid-template-columns:1fr 1fr;gap:13px}
@media(max-width:820px){.ch2,.nar,.cmpsel{grid-template-columns:1fr}.chvs{display:none}}
.lad{position:relative;display:inline-block;height:12px;background:var(--s2);border-radius:2px;vertical-align:middle;max-width:100%}
.lad i{position:absolute}
.lband{top:3px;height:6px;background:var(--r250);opacity:.55;border-radius:2px}
.lzero{top:-2px;height:16px;width:1px;background:var(--t3)}
.lmark{top:-1px;height:14px;width:2px;background:var(--t1);opacity:.6}
.lnow{top:-3px;height:18px;width:3px;border-radius:1px}
.ltip{display:none;position:absolute;bottom:20px;left:50%;transform:translateX(-50%);background:var(--t1);color:var(--s1);
 font-size:10.5px;padding:4px 8px;border-radius:5px;white-space:nowrap;z-index:20;font-weight:500}
.lad:hover .ltip{display:block}
/* real price chart */
.pchart{position:relative;width:100%;margin:2px 0}
.pchart svg{display:block;width:100%;height:auto;overflow:visible;touch-action:none}
.pcline{fill:none;stroke:var(--blue);stroke-width:2;stroke-linejoin:round;stroke-linecap:round}
.pcarea{fill:url(#pcg)}
.pcband{fill:var(--blue);opacity:.09}
.pcbandln{stroke:var(--blue);stroke-width:1;opacity:.32;stroke-dasharray:3 3}
.pcgrid{stroke:var(--line);stroke-width:1}
.pcaxis{fill:var(--t3);font-size:10px}
.pcmk{fill:none;stroke:var(--t1);stroke-width:1.5}
.pcmkdot{fill:var(--s1);stroke:var(--t1);stroke-width:2}
.pcnow{stroke:var(--s1);stroke-width:2}
.pclabel{font-size:10.5px;font-weight:600;fill:var(--t1)}
.pcsub{font-size:9.5px;fill:var(--t3)}
.pccross{stroke:var(--lines);stroke-width:1;opacity:0}
.pchit{fill:transparent}
.pctip{position:absolute;pointer-events:none;background:var(--s1);border:1px solid var(--lines);border-radius:7px;
 padding:5px 8px;font-size:11px;color:var(--t1);white-space:nowrap;z-index:8;box-shadow:var(--sh);opacity:0;transition:opacity .07s;transform:translate(-50%,calc(-100% - 9px))}
.pctip b{color:var(--blue)}
.spk{display:block;width:100%;height:auto;overflow:visible;vertical-align:middle}
.spkline{fill:none;stroke-width:1.6;stroke-linejoin:round;stroke-linecap:round}
.spkband{fill:var(--blue);opacity:.10}
.spkmk{fill:var(--s1)}
.pcrange{display:inline-flex;gap:1px;background:var(--line);border-radius:7px;overflow:hidden;margin:0 0 9px}
.pcrange button{background:var(--s2);border:none;color:var(--t3);font-size:10.5px;padding:4px 9px;cursor:pointer;font-family:inherit}
.pcrange button.on{background:var(--blue);color:#fff}
.sectabs{display:flex;flex-wrap:wrap;gap:6px;margin-top:13px}
.stab{background:var(--s2);border:1px solid var(--line);color:var(--t2);border-radius:999px;padding:5px 12px;font-size:12px;cursor:pointer;font-family:inherit;white-space:nowrap}
.stab:hover{border-color:var(--lines);color:var(--t1)}
.stab.on{background:var(--blue);border-color:var(--blue);color:#fff}
.stab .scnt{opacity:.7;font-size:10.5px;margin-left:2px}
.stab.on .scnt{opacity:.85}
.pbanner{background:var(--s2);border:1px solid var(--warn);border-radius:9px;padding:9px 13px;font-size:12px;color:var(--t2);margin-bottom:13px;line-height:1.5}
.pbanner b{color:var(--warn)}
.pstrip{display:grid;grid-template-columns:repeat(auto-fit,minmax(112px,1fr));gap:1px;background:var(--line);border:1px solid var(--line);border-radius:9px;overflow:hidden}
.pstrip div{background:var(--s1);padding:9px 11px}
.pstrip .k{font-size:9.5px;color:var(--t3);text-transform:uppercase;letter-spacing:.04em}
.pstrip .v{font-size:15px;font-weight:600;margin-top:2px;font-variant-numeric:tabular-nums}
.sr{display:flex;gap:4px;align-items:center}
.srb{width:52px;height:7px;background:var(--s2);border-radius:2px;position:relative;display:inline-block}
.srb i{position:absolute;top:-3px;width:3px;height:13px;background:var(--r400);border-radius:1px}
@media(max-width:1000px){.g2,.g3{grid-template-columns:1fr}.crow{grid-template-columns:78px 1fr 84px}
 #cmd{min-width:150px;flex:1}h1{font-size:15px}.wrap{padding:0 12px 80px}.card{padding:14px}}
</style></head><body>
<header><div class="hdr">
 <h1>Jake's <b>AI Terminal</b></h1>
 <input id="cmd" placeholder="Search ticker or company…" autocomplete="off">
 <div class="spacer"></div>
 <span class="pill" id="asofPill">Financials Q2 · 30 Jun</span>
 <span class="pill hot" id="q2"></span>
 <button class="btn" id="learnBtn" title="Turn on Learn mode, then click any highlighted word for a plain-English explanation">💡 Learn</button>
 <button class="btn" id="th">Dark</button>
</div></header>
<nav id="nav">
 <button data-v="ov" class="on">Overview</button><button data-v="bz">Buy Zone</button><button data-v="moves">Q2 Moves</button><button data-v="screen">Radar</button><button data-v="news">News</button><button data-v="analysis">Analysis</button>
 <button data-v="co">Companies</button><button data-v="cmp">Compare</button><button data-v="surv">Survival</button>
 <button data-v="risk">Risk</button><button data-v="funds">Funds</button>
 <button data-v="hold">Holdings</button><button data-v="guide">Guide</button><button data-v="meth">Method</button><button data-v="aud">Audit</button>
</nav>
<div class="wrap">
<div class="learnhint">💡 <b>Learn mode is on.</b> Any word with a dotted blue underline is clickable — tap it for a plain-English explanation. Click <b>💡 Learn</b> again to turn this off.</div>
<div class="pbanner"><b>Current as of 14 August 2026.</b> Every <b>company</b> figure is Q2 — all 17 dossiers refreshed against 30 June financials, prices to 13 Aug, catalysts re-scraped. The roster is being expanded toward <b>~21 funds</b> split into two lenses: <b>Flow</b> (big active books like Adage, Point72, Millennium, Farallon — where the money moves) and <b>Conviction</b> (concentrated specialists like RA, Perceptive, RTW, Rock Springs — the quality picks). <b>7 of 21 have filed Q2</b> so far; the rest fold in as they file. The <b>Q2 Moves</b> tab shows the Q1→Q2 change and lets you filter by lens.</div>

<section id="v-bz" class="hide">
 <div class="card" id="bzCard"><h2>Start here — the buy zone</h2>
  <div class="sub">The one synthesized shortlist. A name earns a place only if it clears all three gates: <b style="color:var(--good)">funded through its next catalyst</b> (won&rsquo;t be forced to raise first), <b style="color:var(--good)">still trading at or near what the funds paid</b> (you&rsquo;re not chasing), and <b style="color:var(--good)">bought by two or more funds</b> (more than one specialist agrees). Everything else on this terminal is the detail behind these.</div>
  <div id="bzList"></div>
 </div>
</section>
<section id="v-moves" class="hide">
 <div class="card"><h2>Q2 2026 moves — what changed since Q1</h2>
  <div class="sub">The single most useful view once the quarter turns: not what the funds <i>hold</i>, but what they <i>did</i>. An <b style="color:var(--bad)">exit</b> is the loudest signal — a fund walking away. A <b style="color:var(--good)">new buy</b> or <b style="color:var(--good)">add</b> is conviction building. Where a specialist buys what a generalist is dumping, that&rsquo;s a <b>divergence</b> worth a second look. Filed funds show live Q2 moves; the rest fill in as they file today.</div>
  <div id="movesBody"></div>
 </div>
</section>
<section id="v-ov">
 <div class="card"><h2>What this terminal is</h2>
  <div class="note" style="margin-top:6px">One consolidated view of every small/mid-cap company these funds are buying, and everything known about those companies. The signal set is being expanded toward ~21 funds in two lenses: <b>Flow</b> — big active books (Adage, Point72, Millennium, Farallon, plus Viking/Coatue/Citadel/Maverick/Balyasny/Suvretta as they file) that show where money is moving; and <b>Conviction</b> — concentrated specialists (RA, Perceptive, Braidwell, RTW, Cormorant, Deep Track, Avoro, Rock Springs, plus Baker Bros/EcoR1) whose few picks are high-quality signals. Click any ticker to open its full record.</div>
  <div class="tiles" style="margin-top:15px" id="ovTiles"></div>
 </div>
 <div class="card"><h2>Where these trade now versus where the funds were buying</h2>
  <div class="sub">The line down the middle is <b>what the funds paid on average</b> last quarter. Each <b>dot is today's price</b>: <span style="color:var(--good)">green = still below what they paid</span> (you'd be buying in cheaper than they did), <span style="color:var(--bad)">red = it already moved up above their cost</span>. The pale blue bar is the price range they were actually buying in. Sorted cheapest first.</div>
  <div style="margin-top:15px" id="cEntry"></div>
  <div class="legend">
   <span><i class="key" style="background:var(--t2);width:2px;height:13px;border-radius:1px"></i>What the funds paid (their average)</span>
   <span><i class="key" style="background:var(--blue);opacity:.4"></i>Where they were buying (price range)</span>
   <span><i class="key" style="background:var(--good)"></i>Today — cheaper than they paid</span>
   <span><i class="key" style="background:var(--bad)"></i>Today — above what they paid</span>
  </div>
  <div class="axisnote">One dot per company, all on the same scale, so you can compare every name at a glance. Want the full price history and the (sometimes misleading) 31 March filing price? Click any ticker to open its chart.</div>
 </div>
 <div class="grid g2">
  <div class="card"><h2>What the survival layer changed</h2>
   <div class="sub">Conviction rank versus survival rank. Long bars mean the balance sheet disagrees with the fund flow.</div>
   <div style="margin-top:13px" id="ovShift"></div>
   <div class="axisnote" id="ovShiftNote"></div>
  </div>
  <div class="card"><h2>Fund activity last quarter</h2>
   <div class="sub">New positions, adds, trims and full exits across the eight signal funds.</div>
   <div style="margin-top:13px" id="ovAct"></div>
   <div class="legend"><span><i class="key" style="background:var(--good)"></i>New</span><span><i class="key" style="background:var(--r400)"></i>Added</span><span><i class="key" style="background:var(--r100)"></i>Trimmed</span><span><i class="key" style="background:var(--bad)"></i>Exited</span></div>
  </div>
 </div>
 <div class="card"><h2>Start here</h2>
  <div class="sub">All ten researched names ordered by survival score. Click through for the full dossier.</div>
  <div class="tw" style="margin-top:12px;max-height:none"><table id="tQuick"></table></div>
 </div>
</section>

<section id="v-screen" class="hide">
 <div class="card"><h2>Radar — every position under $10B</h2>
  <div class="sub">The full cross-section: every company under a <b>$10B</b> market cap held by the funds that have filed Q2 (<b id="radN">9</b> of 21 so far). Market cap is computed straight from SEC data — the June-30 filing price (position value ÷ shares) × SEC shares outstanding — so no third-party numbers. <b>Sorted by how many funds hold each name</b>: the more funds converging on one small-cap, the louder the signal. This grows automatically as the remaining funds file. A handful of single-fund tickers are name-matched and may need a look.</div>
  <div class="sectabs" id="radSec"></div>
  <div class="toolbar" style="margin-top:10px">
   <input id="radQ" placeholder="Search ticker or company…" autocomplete="off" style="min-width:170px">
   <select id="radF"><option value="">Any # funds</option><option value="2">2+ funds</option><option value="3">3+ funds</option><option value="4">4+ funds</option><option value="5">5+ funds</option></select>
   <select id="radS"><option value="">Any size</option><option value="0.5">Under $500M</option><option value="1">Under $1B</option><option value="2">Under $2B</option><option value="5">Under $5B</option></select>
   <label style="font-size:12px;color:var(--t2);display:inline-flex;align-items:center;gap:5px"><input type="checkbox" id="radDos"> Dossier names only</label>
   <span class="cnt" id="radCnt"></span>
  </div>
  <div class="tw"><table id="tRadar"></table></div>
 </div>
</section>

<section id="v-news" class="hide">
 <style>
 .newsbar{display:flex;gap:8px;margin:2px 0 15px}
 .newsbar input{flex:1;padding:11px 13px;border:1px solid var(--line);border-radius:9px;background:var(--s1);color:var(--t1);font-size:14px}
 .newsbar input:focus{outline:none;border-color:var(--blue)}
 .newshead{display:flex;align-items:center;gap:14px;padding:12px 15px;background:var(--s2);border:1px solid var(--line);border-radius:11px;margin-bottom:16px;flex-wrap:wrap}
 .newshead .btn{margin-left:auto}
 .newsgrp{margin-bottom:16px}.newsgrp h4{margin:0 0 9px;font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--t3)}
 .newsgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px}
 .newsitem{display:block;padding:12px 14px;border:1px solid var(--line);border-radius:10px;background:var(--s1);text-decoration:none;transition:border-color .12s,background .12s}
 .newsitem:hover{border-color:var(--blue);background:var(--s2)}
 .ni-t{font-weight:600;color:var(--t1);font-size:14px;margin-bottom:3px}.ni-d{color:var(--t3);font-size:12px;line-height:1.35}
 </style>
 <div class="card">
  <h2 style="margin-bottom:4px">News &amp; filings desk</h2>
  <div class="sub" style="margin-bottom:2px">Type any ticker to jump straight to its latest SEC filings and news — earnings (10-Q), annual report (10-K), 8-Ks and live news feeds. Each opens in a new tab.</div>
  <div class="newsbar"><input id="newsTicker" list="newsList" placeholder="Enter a ticker — e.g. TVTX, KYMR, RYTM" autocomplete="off"><datalist id="newsList"></datalist><button class="btn on" id="newsGo">Search</button></div>
  <div id="newsOut"></div>
 </div>
</section>

<section id="v-analysis" class="hide">
 <style>
 .anabar{display:flex;gap:8px;margin:2px 0 15px}
 .anabar input{flex:1;padding:11px 13px;border:1px solid var(--line);border-radius:9px;background:var(--s1);color:var(--t1);font-size:14px}
 .anabar input:focus{outline:none;border-color:var(--blue)}
 .anahow{background:var(--s2);border:1px solid var(--line);border-radius:11px;padding:14px 16px;margin-bottom:16px}
 .anahow b{color:var(--t1)} .anahow .ex{display:inline-block;background:var(--s1);border:1px solid var(--line);border-radius:6px;padding:2px 8px;margin:4px 6px 0 0;font-size:12.5px;color:var(--t2)}
 .anagrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px}
 .anacard{border:1px solid var(--line);border-radius:11px;background:var(--s1);padding:14px 15px;cursor:pointer;transition:border-color .12s,background .12s}
 .anacard:hover{border-color:var(--blue);background:var(--s2)}
 .anacard .att{font-weight:600;color:var(--t1);font-size:15px} .anacard .asub{color:var(--t3);font-size:12.5px;margin-top:2px}
 .anacard .awhat{color:var(--t2);font-size:12.5px;line-height:1.4;margin-top:9px}
 .anacard .arow{display:flex;align-items:center;gap:10px;margin-top:10px;font-size:12px;color:var(--t3)}
 .anaEmpty{border:1px dashed var(--lines);border-radius:12px;padding:34px 22px;text-align:center;color:var(--t3)}
 .anaEmpty .big{font-size:16px;color:var(--t1);font-weight:600;margin-bottom:6px}
 </style>
 <div class="card">
  <h2 style="margin-bottom:4px">Analysis desk</h2>
  <div class="sub" style="margin-bottom:12px">On-demand deep research. Name a company and a full dossier is built and collected here.</div>
  <div class="anahow"><b>How it works —</b> tell Claude the company you want researched in the chat, and it runs a deep dive (SEC filings, financials, pipeline, catalysts, live data), scores it, and adds the full dossier here. Works for any US-listed company, whether or not the funds hold it.
   <div style="margin-top:8px"><span class="ex">research VKTX</span><span class="ex">deep dive on Vaxcyte</span><span class="ex">analyze CRSP for me</span></div></div>
  <div class="anabar"><input id="anaJump" list="anaList" placeholder="Jump to an existing analysis — type a ticker" autocomplete="off"><datalist id="anaList"></datalist><button class="btn on" id="anaJumpGo">Open</button></div>
  <div id="anaOut"></div>
 </div>
</section>

<section id="v-co" class="hide">
 <div class="card" style="padding:13px 17px"><div class="note">Ten full dossiers: the business in plain English, survival arithmetic with its derivation shown, complete financials and risk, latest reported quarter, next catalyst, bull and bear case, and every material filing warning. Click a row.</div></div>
 <div id="coList"></div>
</section>

<section id="v-cmp" class="hide">
 <div class="card">
  <h2>Head to head</h2>
  <div class="sub">Pick any two names. The green ▲ pill marks the stronger side on each scored row (for entry price, volatility and burn, lower is better). Reference rows — prices, the 31 March mark, market cap — aren't scored.</div>
  <div class="cmpsel" style="margin-top:14px">
   <select id="cmpA"></select>
   <button class="btn" id="cmpSwap" title="Swap sides">⇄</button>
   <select id="cmpB"></select>
  </div>
  <div id="cmpHead" style="margin-top:15px"></div>
 </div>
 <div id="cmpBody"></div>
</section>
<section id="v-surv" class="hide">
 <div class="card scalecard"><h2>What the survival score means</h2>
  <div class="sub">It runs on a scale from about <b>−110 to +120</b>. It combines cash runway, whether that runway reaches the next catalyst, the balance sheet, any going-concern warning, fund conviction and entry price. Read it as a <b>safety gauge, not a price target</b> — it tells you who can survive, not who will win biggest.</div>
  <div id="scaleDemo" style="margin-top:14px"></div>
  <div class="leg">
   <span><b style="color:var(--bad)">Below 0 — Danger</b> · likely can't fund itself to its next event (e.g. KPTI)</span>
   <span><b style="color:var(--warn)">0–50 — Weak</b> · thin cushion, keep watching</span>
   <span><b style="color:var(--warn)">50–80 — Fair</b> · funded but not a fortress</span>
   <span><b style="color:var(--good)">80–100 — Strong</b> · comfortable cushion</span>
   <span><b style="color:var(--good)">100+ — Top tier</b> · the strongest scores here (OKUR, RLMD)</span>
  </div>
 </div>
 <div class="card"><h2>Runway versus catalyst</h2>
  <div class="sub">Bars = quarters of cash at current burn. Dot = the next value-inflecting event. <b>A dot past the end of a bar means the company must raise before its own catalyst.</b></div>
  <div style="margin-top:14px" id="cRun"></div>
  <div class="legend"><span><i class="key" style="background:var(--good)"></i>Funded — 8+ quarters or profitable</span><span><i class="key" style="background:var(--warn)"></i>Tight — 2 to 8</span><span><i class="key" style="background:var(--bad)"></i>Distressed — under 2 or going-concern doubt</span><span><i class="key" style="background:var(--t1);width:3px;height:12px;border-radius:1px"></i>Next catalyst</span></div>
  <div class="axisnote">Karyopharm is the only name whose catalyst sits beyond its cash: it plans to file for FDA approval in myelofibrosis this month, but management guides liquidity only into late Q3 2026 and lender forbearance expires in September. Allison is profitable so its bar runs full length.</div>
 </div>
 <div class="card"><h2>Where the ranking comes from</h2>
  <div class="sub">Six components shown separately so you can disagree with any one of them.</div>
  <div style="margin-top:14px" id="cScore"></div><div class="legend" id="scLeg"></div>
 </div>
 <div class="card"><h2>Balance sheet detail</h2>
  <div class="sub">Company-reported cash. Several screeners understate it by excluding marketable securities — where that happens it is flagged in the dossier.</div>
  <div class="tw" style="margin-top:12px;max-height:none"><table id="tSurv"></table></div>
 </div>
 <div class="grid g2">
  <div class="card"><h2>Net cash as a share of market cap</h2><div class="sub">How much of what you pay is just the bank balance.</div>
   <div style="margin-top:14px" id="cNet"></div>
   <div class="axisnote">Above 100% means the market values the whole pipeline below cash. Karyopharm at −446% has debt roughly five to six times its market value.</div></div>
  <div class="card"><h2>Cash against quarterly burn</h2><div class="sub">Bar = cash on hand, same scale for all. Ticks mark each quarter of burn.</div>
   <div style="margin-top:14px" id="cBurn"></div>
   <div class="axisnote">Burn is derived per company — trailing cash flow, a sequential balance-sheet bridge, or company guidance where trailing data has stopped being representative. Each derivation is written out in the dossier.</div></div>
 </div>
</section>

<section id="v-risk" class="hide">
 <div class="card"><h2>How violently these actually trade</h2>
  <div class="sub">Two-year weekly beta against the S&amp;P 500 horizontally, annualised volatility vertically, bubble size = market cap.</div>
  <div id="scatter" style="margin-top:10px"></div>
  <div class="legend"><span><i class="key" style="background:var(--good)"></i>Funded</span><span><i class="key" style="background:var(--warn)"></i>Tight</span><span><i class="key" style="background:var(--bad)"></i>Distressed</span></div>
  <div class="axisnote">Damora has no two-year history under this ticker — it began trading in March 2026 after the reverse merger — so it is left out rather than given a misleading number.</div>
 </div>
 <div class="card"><h2>Price context</h2><div class="sub">Position in the 52-week range, worst two-year drawdown, short interest and consensus.</div>
  <div class="tw" style="margin-top:12px;max-height:none"><table id="tRisk"></table></div></div>
</section>

<section id="v-funds" class="hide">
 <div class="card" style="padding:13px 17px"><div class="toolbar" style="margin-bottom:0">
  <button class="btn on" data-set="smid" id="bSmid">Signal funds (small/mid)</button>
  <button class="btn" data-set="longonly" id="bLo">Long-only cross-reference</button>
  <span class="cnt" id="fSetNote"></span></div></div>
 <div class="grid g2" id="fundCards"></div>
 <div class="card" id="ovCard"><h2>Portfolio overlap between the signal funds</h2><div class="sub" id="ovNote"></div>
  <div class="sub">Share of two books sitting in the same tickers. Low numbers mean these managers are genuinely independent, so a name two of them both bought carries more weight.</div>
  <div style="overflow:auto;margin-top:13px"><table class="mx" id="mx"></table></div>
  <div class="legend" id="mxLeg"></div>
 </div>
</section>

<section id="v-hold" class="hide">
 <div class="card"><h2>All disclosed positions</h2>
  <div class="sub">Every 13F line across all twelve managers, with quarter-over-quarter status.</div>
  <div class="toolbar" style="margin-top:12px">
   <select id="hF"><option value="-1">All managers</option></select>
   <select id="hS"><option value="">Any change</option><option>NEW</option><option>ADD</option><option>TRIM</option><option>HOLD</option></select>
   <select id="hT"><option value="0">Shares</option><option value="1">Calls</option><option value="2">Puts</option><option value="3">Notes</option><option value="-1">All types</option></select>
   <input type="search" id="hQ" placeholder="Ticker, issuer or CUSIP…">
   <span class="cnt" id="hCnt"></span>
  </div>
  <div class="tw" id="hScroll"><table id="tHold"></table></div>
 </div>
</section>

<section id="v-aud" class="hide">
 <div class="card"><h2>Accuracy audit — 12 August 2026</h2>
  <div class="sub">Everything here was checked three ways before you rely on it: the arithmetic against itself, the 13F data against the original SEC filings, and the research claims against company sources by two independent agents instructed to find errors.</div>
  <div class="tiles" style="margin-top:15px" id="audTiles"></div>
 </div>
 <div class="card"><h2>13F data versus the original SEC filings</h2>
  <div class="sub">The form13fInfoTable XML was pulled straight from EDGAR for each signal fund and re-tallied independently of the data feed used to build this terminal.</div>
  <div class="tw" style="margin-top:12px;max-height:none"><table id="tAudSec"></table></div>
  <div class="axisnote" id="audSecNote"></div>
 </div>
 <div class="card"><h2>Every correction made</h2>
  <div class="sub">The audit found 36 issues across two passes — 27 in the first, 9 more in the 12 August Q2-financials refresh. All are listed, including the ones that changed conclusions.</div>
  <div class="tw" style="margin-top:12px;max-height:none"><table id="tAudLog"></table></div>
 </div>
 <div class="card"><h2>What the audit did not cover</h2><div class="note" id="audGaps"></div></div>
</section>
<section id="v-guide" class="hide">
 <div class="card"><h2>Plain-English guide</h2>
  <div class="sub">Everything on this terminal, explained without jargon. If a word, colour or tab anywhere confuses you, it's defined here. <b style="color:var(--blue)">Tip:</b> click the <b>💡 Learn</b> button at the top right, then any highlighted word anywhere on the terminal pops its own explanation — you don't even have to come here.</div>
 </div>
 <div class="card"><h3 class="gh">What each tab shows, and what to look for</h3>
  <div class="sub" style="margin-bottom:4px">The twelve tabs across the top, in order.</div>
  <div id="gTabs"></div>
 </div>
 <div class="card"><h3 class="gh">What the colours mean</h3>
  <div class="glegend" id="gColors"></div>
 </div>
 <div class="card"><h3 class="gh">What the marks on the price charts mean</h3>
  <div class="glegend" id="gMarks"></div>
 </div>
 <div class="card"><h3 class="gh">The words — every term, in one sentence</h3>
  <div class="sub" style="margin-bottom:4px">Grouped by the question each one helps you answer.</div>
  <div id="gGloss"></div>
 </div>
 <div class="card"><h3 class="gh">How to read this terminal in 60 seconds</h3>
  <div class="note" id="gHow"></div>
 </div>
</section>
<section id="v-meth" class="hide"><div class="card"><h2>Method, sources and known limits</h2><div class="note" id="meth"></div></div></section>
</div>

<div id="ov"></div><div id="pan"><div id="panC"></div></div>
<div id="xpPop"></div>

<script id="D" type="application/json">__DATA__</script>
<script>
const D=JSON.parse(document.getElementById('D').textContent);
(function(){try{var p=document.getElementById('asofPill');
 var stamp=D.priceStamp||(D.radar&&D.radar.priceAsOf)||null;
 if(p&&stamp)p.textContent='Financials Q2 · Prices '+stamp;}catch(e){}})();
/* hosted auto-update: poll version.json, offer a non-disruptive refresh when new data deploys */
(function(){ if(location.protocol==='file:')return;
 var cur=(D&&D.lastUpdated)||null;
 function bar(){ if(document.getElementById('updBar'))return;
   var b=document.createElement('div'); b.id='updBar';
   b.style.cssText='position:fixed;bottom:16px;left:50%;transform:translateX(-50%);z-index:99999;background:#2b6cb0;color:#fff;padding:9px 16px;border-radius:20px;font:600 12.5px system-ui,sans-serif;cursor:pointer;box-shadow:0 4px 16px rgba(0,0,0,.3)';
   b.textContent='🔄 New prices available — click to refresh'; b.onclick=function(){location.reload();};
   document.body.appendChild(b); }
 function chk(){ fetch('version.json?_='+Date.now()).then(function(r){return r.ok?r.json():null;}).then(function(v){
   if(!v||!v.ts)return; if(cur&&v.ts!==cur){bar();} else if(!cur){cur=v.ts;} }).catch(function(){}); }
 setInterval(chk, 180000); setTimeout(chk, 8000);
})();
const F=D.funds,S=D.secs,R=D.rows,A=D.ana,DOS=D.dossiers,SCR=D.screen,HOLD=D.holders;
const SMID=F.filter(f=>f.set==='smid'&&!f.dropped),LO=F.filter(f=>f.set==='longonly');
const dosBy={};DOS.forEach(d=>{dosBy[d.sym]=d;if(d.alias)dosBy[d.alias]=d;});
const scrBy={};SCR.forEach(s=>scrBy[s.sym]=s);
const esc=s=>(s||'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const bcls=b=>b==='Funded'?'g':b==='Tight'?'w':b==='Distressed'?'b':'';
/* survival score → plain band + a small scale showing where it sits */
function survBand(v){return v>=100?['Top tier','var(--good)']:v>=80?['Strong','var(--good)']:v>=50?['Fair','var(--warn)']:v>=0?['Weak','var(--warn)']:['Danger','var(--bad)'];}
function survScale(v,opt){opt=opt||{};const MIN=-110,MAX=120,R=MAX-MIN;
 const pos=Math.max(0,Math.min(100,(v-MIN)/R*100));
 return '<span class="sscale" style="width:'+(opt.w||'150px')+'"><span class="sstrack"><i class="ssmark" style="left:'+pos.toFixed(1)+'%"></i></span>'+
  (opt.labels?'<span class="ssends"><span>danger</span><span>weak</span><span>strong</span></span>':'')+'</span>';}
const money=m=>m==null?'—':(Math.abs(m)>=1000?'$'+(m/1000).toFixed(2)+'B':'$'+(+m).toFixed(1)+'M');
const K=k=>{const v=k*1000;return Math.abs(v)>=1e9?'$'+(v/1e9).toFixed(2)+'B':Math.abs(v)>=1e6?'$'+(v/1e6).toFixed(0)+'M':'$'+(v/1e3).toFixed(0)+'K';};
const N=n=>n==null?'—':(+n).toLocaleString('en-US');
const pc=(x,d=1)=>x==null?'—':(x*100).toFixed(d)+'%';
const sg=(x,d=0)=>x==null?'<span class="mut">—</span>':'<span class="'+(x>0?'pos':x<0?'neg':'mut')+'">'+(x>0?'+':'')+(x*100).toFixed(d)+'%</span>';
const sgE=x=>x==null?'<span class="mut">—</span>':'<span class="'+(x<=0?'pos':x>0.15?'neg':'')+'">'+(x>0?'+':'')+(x*100).toFixed(0)+'%</span>';
const an=s=>A[s]||null,bt=s=>{const a=an(s);return a?a[0]:null},vl=s=>{const a=an(s);return a?a[2]:null},
 sq=s=>{const a=an(s);return a?a[4]:null},r1=s=>{const a=an(s);return a?a[3]:null},
 px=s=>{const a=an(s);return a?a[6]:null},mdd=s=>{const a=an(s);return a?a[5]:null},
 p52=s=>{const a=an(s);return a?a[9]:null},lo52=s=>{const a=an(s);return a?a[7]:null},hi52=s=>{const a=an(s);return a?a[8]:null};
const nh=s=>(HOLD[s]||[]).length;
const PQ=D.pxq1||{};
const q1lo=s=>PQ[s]?PQ[s][0]:null,q1hi=s=>PQ[s]?PQ[s][1]:null,q1avg=s=>PQ[s]?PQ[s][2]:null,mk31=s=>PQ[s]?PQ[s][3]:null;
const vsQ1=s=>{const a=q1avg(s),p=px(s);return(a&&p)?p/a-1:null};
const vsMk=s=>{const m=mk31(s),p=px(s);return(m&&p)?p/m-1:null};
const rowMark=r=>r[3]?r[2]*1000/r[3]:null;              /* per 13F line: value/shares */
const rowVs=r=>{const m=rowMark(r),p=px(S[r[1]][0]);return(m&&p)?p/m-1:null};
/* compact price ladder: where price sits vs the Q1 range the funds were buying in */
function ladder(sym,w){
 const lo=q1lo(sym),hi=q1hi(sym),av=q1avg(sym),mk=mk31(sym),now=px(sym);
 if(!av||!now)return '<span class="mut">—</span>';
 const L=-0.8,H=1.0,X=v=>Math.max(0,Math.min(100,(Math.max(L,Math.min(H,v))-L)/(H-L)*100));
 const bl=X(lo/av-1),bh=X(hi/av-1),z=X(0),m=mk?X(mk/av-1):null,n=X(now/av-1);
 const ww=(typeof w==='string')?w:((w||132)+'px');
 return '<span class="lad" style="width:'+ww+'">'+
  '<i class="lband" style="left:'+bl+'%;width:'+Math.max(1.5,bh-bl)+'%"></i>'+
  '<i class="lzero" style="left:'+z+'%"></i>'+
  (m!=null?'<i class="lmark" style="left:'+m+'%"></i>':'')+
  '<i class="lnow" style="left:'+n+'%;background:'+(now<=av?'var(--good)':'var(--bad)')+'"></i>'+
  '<span class="ltip">Q1 range $'+lo+'–$'+hi+' · avg $'+av+(mk?' · 31 Mar $'+mk:'')+' · now $'+now+'</span></span>';
}
const TK=s=>'<span class="tk" data-sym="'+esc(s)+'">'+esc(s||'—')+'</span>';

/* ---------- real price charts ---------- */
const SER=D.pxSeries||{};
function serOf(sym){let s=SER[sym];const d=dosBy[sym];
 if(!s&&d){s=SER[d.sym]||(d.alias?SER[d.alias]:null);}
 if(!s||!s.c||s.c.length<4)return null;
 const base=s.t0*864e5;return{x:s.o.map(o=>base+o*864e5),c:s.c.slice()};}
const MARK_MS=Date.UTC(2026,2,31);           /* 31 Mar 2026 quarter-end */
const niceTicks=(lo,hi,n)=>{const r=hi-lo||1,raw=r/n,mag=Math.pow(10,Math.floor(Math.log10(raw))),
 st=[1,2,2.5,5,10].map(m=>m*mag).find(m=>r/m<=n+1)||10*mag,
 t=[];for(let v=Math.ceil(lo/st)*st;v<=hi+1e-9;v+=st)t.push(+v.toFixed(6));return t;};
const money0=v=>v>=100?'$'+v.toFixed(0):v>=10?'$'+v.toFixed(1):'$'+v.toFixed(2);
const MONTHS=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
let PCID=0;
/* full price chart with the funds' Q1 buying band + 31-Mar mark drawn on the real line */
function priceChart(sym,opt){opt=opt||{};const s=serOf(sym);if(!s)return '<div class="axisnote">No price history available for '+esc(sym)+'.</div>';
 const win=opt.win||9999,H=opt.h||210,id='pc'+(++PCID);
 let X=s.x,C=s.c;
 if(win<9999){const cut=X[X.length-1]-win*864e5;const i0=X.findIndex(t=>t>=cut);if(i0>0){X=X.slice(i0);C=C.slice(i0);}}
 const W=720,L=44,Rp=58,T=14,B=22,pw=W-L-Rp,ph=H-T-B;
 const lo=q1lo(sym),hi=q1hi(sym),av=q1avg(sym),mk=mk31(sym);
 let pmin=Math.min(...C),pmax=Math.max(...C);
 if(lo&&lo<pmin)pmin=lo; if(hi&&hi>pmax)pmax=hi; if(av){pmin=Math.min(pmin,av);pmax=Math.max(pmax,av);}
 const pad=(pmax-pmin)*0.08||1;pmin=Math.max(0,pmin-pad);pmax=pmax+pad;
 const xs=t=>L+(t-X[0])/(X[X.length-1]-X[0]||1)*pw, ys=p=>T+ph-(p-pmin)/(pmax-pmin||1)*ph;
 const line=C.map((c,i)=>(i?'L':'M')+xs(X[i]).toFixed(1)+' '+ys(c).toFixed(1)).join(' ');
 const area=line+' L'+xs(X[X.length-1]).toFixed(1)+' '+(T+ph)+' L'+xs(X[0]).toFixed(1)+' '+(T+ph)+' Z';
 let g='';
 /* y grid + labels */
 niceTicks(pmin,pmax,4).forEach(v=>{const y=ys(v).toFixed(1);
  g+='<line class="pcgrid" x1="'+L+'" y1="'+y+'" x2="'+(L+pw)+'" y2="'+y+'"/>'+
     '<text class="pcaxis" x="'+(L-6)+'" y="'+y+'" text-anchor="end" dominant-baseline="middle">'+money0(v)+'</text>';});
 /* x labels: first of quarter months */
 let lastLab='';
 for(let i=0;i<X.length;i++){const d=new Date(X[i]),m=d.getUTCMonth();if(m%3===0){const lab=MONTHS[m]+" '"+String(d.getUTCFullYear()).slice(2);
  if(lab!==lastLab){lastLab=lab;const x=xs(X[i]).toFixed(1);
   g+='<text class="pcaxis" x="'+x+'" y="'+(H-6)+'" text-anchor="middle">'+lab+'</text>';}}}
 /* Q1 buying band */
 if(lo&&hi){const yb=ys(hi),yt=ys(lo);g+='<rect class="pcband" x="'+L+'" y="'+yb.toFixed(1)+'" width="'+pw+'" height="'+Math.max(1,(yt-yb)).toFixed(1)+'"/>'+
  '<text class="pcsub" x="'+(L+4)+'" y="'+(yb-3).toFixed(1)+'">Funds’ Q1 buying range $'+lo+'–$'+hi+'</text>';}
 if(av){const y=ys(av).toFixed(1);g+='<line class="pcbandln" x1="'+L+'" y1="'+y+'" x2="'+(L+pw)+'" y2="'+y+'"/>';}
 /* area + line */
 g='<defs><linearGradient id="'+id+'g" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="var(--blue)" stop-opacity=".16"/><stop offset="1" stop-color="var(--blue)" stop-opacity="0"/></linearGradient></defs>'+
   g+'<path d="'+area+'" fill="url(#'+id+'g)"/><path class="pcline" d="'+line+'"/>';
 /* 31-Mar mark on the line */
 if(MARK_MS>=X[0]&&MARK_MS<=X[X.length-1]){let bi=0;for(let i=0;i<X.length;i++)if(Math.abs(X[i]-MARK_MS)<Math.abs(X[bi]-MARK_MS))bi=i;
  const mx=xs(X[bi]),my=ys(C[bi]);g+='<line class="pcbandln" x1="'+mx.toFixed(1)+'" y1="'+T+'" x2="'+mx.toFixed(1)+'" y2="'+(T+ph)+'"/>'+
   '<circle class="pcmkdot" cx="'+mx.toFixed(1)+'" cy="'+my.toFixed(1)+'" r="4"/>'+
   '<text class="pcsub" x="'+mx.toFixed(1)+'" y="'+(T-3)+'" text-anchor="middle">31 Mar 13F $'+(mk?mk.toFixed(2):C[bi].toFixed(2))+'</text>';}
 /* now dot + label */
 const nx=xs(X[X.length-1]),ny=ys(C[C.length-1]),cnow=C[C.length-1];
 g+='<circle class="pcnow" cx="'+nx.toFixed(1)+'" cy="'+ny.toFixed(1)+'" r="4" fill="var(--blue)"/>'+
    '<text class="pclabel" x="'+(nx+7).toFixed(1)+'" y="'+ny.toFixed(1)+'" dominant-baseline="middle">$'+cnow.toFixed(2)+'</text>';
 /* hover layer */
 g+='<line class="pccross" id="'+id+'x" x1="0" y1="'+T+'" x2="0" y2="'+(T+ph)+'"/>'+
    '<circle id="'+id+'d" class="pcmkdot" r="3.5" style="opacity:0"/>'+
    '<rect class="pchit" x="'+L+'" y="'+T+'" width="'+pw+'" height="'+ph+'" data-pc="'+id+'" data-sym="'+esc(sym)+'"/>';
 return '<div class="pchart" id="'+id+'w" data-l="'+L+'" data-pw="'+pw+'">'+
  '<svg viewBox="0 0 '+W+' '+H+'" preserveAspectRatio="none" style="height:'+H+'px">'+g+'</svg>'+
  '<div class="pctip" id="'+id+'t"></div></div>';}
/* store live series for hover keyed by chart id via a registry populated on render */
const PCREG={};
function regChart(id,X,C,L,pw){PCREG[id]={X,C,L,pw};}
/* re-emit priceChart but also register — wrap */
const _priceChart=priceChart;
priceChart=function(sym,opt){const s=serOf(sym);const html=_priceChart(sym,opt);
 if(s){const m=html.match(/id="(pc\d+)w"/);if(m){let X=s.x,C=s.c;const win=(opt&&opt.win)||9999;
  if(win<9999){const cut=X[X.length-1]-win*864e5;const i0=X.findIndex(t=>t>=cut);if(i0>0){X=X.slice(i0);C=C.slice(i0);}}
  regChart(m[1],X,C,44,720-44-58);}}return html;};
/* global hover handler */
document.addEventListener('pointermove',e=>{const hit=e.target.closest&&e.target.closest('.pchit');
 if(!hit){return;}const id=hit.dataset.pc,reg=PCREG[id];if(!reg)return;
 const wrap=document.getElementById(id+'w'),svg=wrap.querySelector('svg'),rect=svg.getBoundingClientRect();
 const W=720,H=svg.viewBox.baseVal.height,sx=rect.width/W;
 const px_=(e.clientX-rect.left)/sx;const frac=Math.max(0,Math.min(1,(px_-reg.L)/reg.pw));
 const t0=reg.X[0],t1=reg.X[reg.X.length-1],tt=t0+frac*(t1-t0);
 let bi=0;for(let i=0;i<reg.X.length;i++)if(Math.abs(reg.X[i]-tt)<Math.abs(reg.X[bi]-tt))bi=i;
 const xs=reg.L+(reg.X[bi]-t0)/(t1-t0||1)*reg.pw;
 const cross=document.getElementById(id+'x'),dot=document.getElementById(id+'d'),tip=document.getElementById(id+'t');
 cross.setAttribute('x1',xs);cross.setAttribute('x2',xs);cross.style.opacity=.9;
 /* find y from the rendered line: recompute using same scale */
 const vb=svg.viewBox.baseVal,T=14,B=22,ph=vb.height-T-B;
 let pmin=Math.min(...reg.C),pmax=Math.max(...reg.C);const sym2=hit.dataset.sym;
 const lo=q1lo(sym2),hi=q1hi(sym2),av=q1avg(sym2);
 if(lo&&lo<pmin)pmin=lo;if(hi&&hi>pmax)pmax=hi;if(av){pmin=Math.min(pmin,av);pmax=Math.max(pmax,av);}
 const pad=(pmax-pmin)*0.08||1;pmin=Math.max(0,pmin-pad);pmax=pmax+pad;
 const ys=T+ph-(reg.C[bi]-pmin)/(pmax-pmin||1)*ph;
 dot.setAttribute('cx',xs);dot.setAttribute('cy',ys);dot.style.opacity=1;
 const d=new Date(reg.X[bi]);tip.innerHTML='<b>$'+reg.C[bi].toFixed(2)+'</b> · '+MONTHS[d.getUTCMonth()]+' '+d.getUTCDate()+" '"+String(d.getUTCFullYear()).slice(2);
 tip.style.left=(xs*sx)+'px';tip.style.top=(ys*(rect.height/H))+'px';tip.style.opacity=1;});
document.addEventListener('pointerleave',e=>{const hit=e.target.closest&&e.target.closest('.pchit');if(!hit)return;
 const id=hit.dataset.pc;const c=document.getElementById(id+'x'),dt=document.getElementById(id+'d'),tp=document.getElementById(id+'t');
 if(c)c.style.opacity=0;if(dt)dt.style.opacity=0;if(tp)tp.style.opacity=0;},true);
/* compact sparkline for table cells: real price line + faint Q1 band + mark dot */
function sparkChart(sym,w,h){const s=serOf(sym);const ww=(typeof w==='string')?w:((w||116)+'px');const H=h||30;
 if(!s)return '<span class="mut">—</span>';
 const X=s.x,C=s.c,W=116,pw=W-2,ph=H-6,x0=1,y0=3;
 const lo=q1lo(sym),hi=q1hi(sym);let pmin=Math.min(...C),pmax=Math.max(...C);
 if(lo&&lo<pmin)pmin=lo;if(hi&&hi>pmax)pmax=hi;const rng=(pmax-pmin)||1;
 const xs=t=>x0+(t-X[0])/(X[X.length-1]-X[0]||1)*pw, ys=p=>y0+ph-(p-pmin)/rng*ph;
 const line=C.map((c,i)=>(i?'L':'M')+xs(X[i]).toFixed(1)+' '+ys(c).toFixed(1)).join(' ');
 const up=C[C.length-1]>=C[0];let g='';
 if(lo&&hi)g+='<rect class="spkband" x="'+x0+'" y="'+ys(hi).toFixed(1)+'" width="'+pw+'" height="'+Math.max(1,ys(lo)-ys(hi)).toFixed(1)+'"/>';
 g+='<path class="spkline" d="'+line+'" stroke="'+(up?'var(--good)':'var(--bad)')+'"/>';
 if(MARK_MS>=X[0]&&MARK_MS<=X[X.length-1]){let bi=0;for(let i=0;i<X.length;i++)if(Math.abs(X[i]-MARK_MS)<Math.abs(X[bi]-MARK_MS))bi=i;
  g+='<circle class="spkmk" cx="'+xs(X[bi]).toFixed(1)+'" cy="'+ys(C[bi]).toFixed(1)+'" r="2.6" stroke="var(--t1)" stroke-width="1.4"/>';}
 g+='<circle cx="'+xs(X[X.length-1]).toFixed(1)+'" cy="'+ys(C[C.length-1]).toFixed(1)+'" r="2.4" fill="'+(up?'var(--good)':'var(--bad)')+'"/>';
 return '<svg class="spk" viewBox="0 0 '+W+' '+H+'" preserveAspectRatio="none" style="width:'+ww+';height:'+H+'px" title="'+esc(sym)+' 2-year price"><g>'+g+'</g></svg>';}

/* header */
(function(){const q=D.q2move;document.getElementById('q2').textContent=q?('Q2 13Fs: '+q.filedCount+' of '+q.total+' funds in'):'Q2 13Fs landing';})();
const th=document.getElementById('th');
th.onclick=()=>{const r=document.documentElement,dk=r.dataset.theme==='dark';r.dataset.theme=dk?'light':'dark';th.textContent=dk?'Dark':'Light';drawAll();};
if(matchMedia('(prefers-color-scheme:dark)').matches){document.documentElement.dataset.theme='dark';th.textContent='Light';}
const VIEWS=['ov','bz','moves','screen','news','analysis','co','cmp','surv','risk','funds','hold','guide','meth','aud'];
/* one-line "what this tab is for" banner at the top of each tab */
(function(){const INTRO={
 ov:['Overview','Your starting dashboard — the big picture of every name, where each trades versus what the funds paid, and what the funds bought and sold last quarter.'],
 bz:['Buy Zone','The payoff — the short list of names that clear all three gates at once: funded through their catalyst, still near what the funds paid, and bought by 2+ funds. Start here.'],
 moves:['Q2 Moves','What the funds DID since Q1 — exits (loudest), new buys and adds. The change between quarters is the real signal. Filed funds are live; the rest fill in as they file.'],
 screen:['Radar','The master list — every company under $10B that the funds hold, ranked by how many funds converge on each. This is where the money sits. Filter by sector, size, fund count, or search a ticker.'],
 news:['News & filings','Search any ticker to jump to its latest SEC filings — earnings (10-Q), annual report (10-K), 8-Ks and press releases — plus live news feeds. One-click launcher to the primary sources.'],
 analysis:['Analysis','Your on-demand research desk. Name any company in chat and a full deep-dive dossier is researched and added here — business, pipeline, catalysts, financials, survival math and the case for and against.'],
 co:['Companies','The seventeen fully-researched names — click any one for the business in plain English, its survival math, and the case for and against.'],
 cmp:['Compare','Put any two names head to head — every metric side by side, with a green ▲ marking the stronger one on each row.'],
 surv:['Survival','The key question, answered visually: can each company reach its next milestone without running out of cash? Runway past the catalyst = safe.'],
 risk:['Risk','How bumpy each stock is — how wildly it swings, how much it moves with the market, and its worst falls. Tells you what kind of ride you\'re taking on.'],
 funds:['Funds','Who is doing the buying — each fund\'s activity, biggest positions and style, plus how independent their bets are. This is where conviction lives.'],
 hold:['Holdings','The raw data — every single position across all twelve funds, searchable and sortable. For when you want to dig into the filings yourself.'],
 meth:['Method','How every number on this terminal was worked out, and exactly where the data came from.'],
 aud:['Audit','Every accuracy check that was run and every correction made, shown against the original SEC figures — plus an honest list of what wasn\'t covered.']
};
for(const v in INTRO){const sec=document.getElementById('v-'+v);if(!sec)continue;
 const d=document.createElement('div');d.className='tabintro';
 d.innerHTML='<b>'+INTRO[v][0]+'</b><span>'+INTRO[v][1]+'</span>';
 sec.insertBefore(d,sec.firstChild);}
})();
function go(v){[...document.querySelectorAll('#nav button')].forEach(b=>b.classList.toggle('on',b.dataset.v===v));
 VIEWS.forEach(x=>document.getElementById('v-'+x).classList.toggle('hide',x!==v));
 if(v==='risk')drawScatter(); if(v==='hold')holdT(); if(v==='cmp')drawCmp(); if(v==='aud')drawAud(); if(v==='guide')drawGuide(); if(v==='bz')buyZone(); if(v==='moves')drawMoves(); if(v==='news')drawNews(); if(v==='analysis')drawAnalysis(); window.scrollTo(0,0);}
document.getElementById('nav').onclick=e=>{const b=e.target.closest('button');if(b)go(b.dataset.v);};

/* ---------- company panel ---------- */
const ovl=document.getElementById('ov'),pan=document.getElementById('pan');
ovl.onclick=closeCo; document.addEventListener('keydown',e=>{if(e.key==='Escape')closeCo();});
function closeCo(){ovl.classList.remove('on');pan.classList.remove('on');}
/* ---------- Learn mode: click any highlighted word for a plain explanation ---------- */
const XPG={
 'runway':['Runway','How many quarters of cash the company has left before it must raise more money. <b>Higher is safer.</b> The most important survival number.'],
 'burn':['Burn','How much cash the company spends each quarter. Most of these have little or no revenue, so they live off a cash pile.'],
 'net cash':['Net cash','Cash minus debt — what\'s really the company\'s after what it owes.'],
 'net cash as % of market cap':['Net cash as % of market cap','How much of the company\'s price tag is just the cash it holds. Over 100% means the market values the actual business at less than nothing.'],
 'catalyst':['Catalyst','The next big event that could move the stock — a trial result, an FDA decision, or an earnings report. “Next catalyst in” is how many quarters away it is.'],
 'runway covers catalyst':['Runway covers catalyst','<b>YES</b> means the company has enough cash to reach its next big event without raising money first. This is the line that matters most.'],
 'survival score':['Survival score','A safety gauge on a scale of about <b>−110 to +120</b>. <b>Below 0</b> = danger (may not survive, like KPTI at −102). <b>0–60</b> = thin to adequate. <b>60–90</b> = well funded. <b>90+</b> = very strong (the best here, ~114). It combines cash, runway, catalyst timing, debt and fund conviction. Read it as who can <i>survive</i>, not who wins biggest. The Survival tab shows every name on this scale.'],
 'going concern':['Going concern','An official warning in the company\'s own filings that it may not survive the year. The worst red flag on this terminal.'],
 'funded':['Funded','Our label for a company with comfortable cash to reach its next milestone. The green, healthy bucket.'],
 'tight':['Tight','Enough cash to keep going, but not much cushion — watch it.'],
 'distressed':['Distressed','At real risk of running out of money. Treat with caution no matter who bought it.'],
 'beta':['Beta','How much the stock moves when the whole market moves. 1 = moves with the market; 2 = twice as jumpy.'],
 'volatility':['Volatility','How wildly the price swings. Higher = a bumpier ride.'],
 'annualised volatility':['Annualised volatility','How wildly the price swings over a year. Higher = a bumpier, riskier ride.'],
 'drawdown':['Drawdown','The biggest drop from a peak the stock has had — shows how bad it can get.'],
 'worst 2-year drawdown':['Worst 2-year drawdown','The biggest fall from a high point over the last two years — a gut-check on how much it can drop.'],
 'short interest':['Short interest','The share of the stock that traders have bet <i>against</i>. High = many people expect it to fall.'],
 'market cap':['Market cap','The total price tag of the whole company (share price × number of shares).'],
 'enterprise value':['Enterprise value','Market cap minus net cash — what you\'re really paying for the business itself. Can be negative when cash is worth more than the whole company.'],
 'revenue':['Revenue','Sales. Most of these early-stage names have little or none yet.'],
 'analyst target':['Analyst target','The average price Wall Street analysts expect the stock to reach. A guide, not a promise.'],
 'implied upside':['Implied upside','How far below the analyst target today\'s price sits, as a percentage — the room to the target.'],
 '13f':['13F','The report big investment funds must file every quarter listing what they own. Every buy signal here comes from these.'],
 'overlap':['Overlap','How alike two funds\' portfolios are. <b>Low overlap is good</b> — it means they decided independently, so a name they both bought carries more weight.'],
 'conviction':['Conviction','How hard the funds are really betting on a name — how many funds bought it, how much money, and how big a slice of their portfolio it is.'],
 'trajectory':['Trajectory','Whether a fund has been <b>building</b>, <b>trimming</b>, <b>holding</b>, or just <b>opened</b> a position, quarter over quarter. Quietly trimming after building is a warning.'],
 'fresh money':['Fresh money','The funds that opened or added to a name last quarter — the buyers you\'re actually following.'],
 'buy zone':['Buy zone','The shortlist of names that clear all three gates at once: funded through their catalyst, still near what the funds paid, and bought by 2+ funds.'],
 'q1 average':['Q1 average','Roughly the price the funds paid, averaged across the quarter they were buying. The honest read on “where they got in.”'],
 '31 march mark':['31 March mark','The price on the very last day of the quarter, which the filing reports. It\'s just one day\'s close and can sit at an extreme, so it often misleads.'],
 'dossier':['Dossier','The deep write-up on a company — what it does, its survival math, the case for and against, and its next catalyst.'],
 'position in 52-week range':['Position in 52-week range','Where today\'s price sits between the stock\'s lowest and highest point over the past year (0% = the low, 100% = the high).'],
 'dilution':['Dilution','When a company sells new shares to raise cash, every existing share owns a smaller slice of the company. Early biotechs dilute a lot — it\'s the price of staying alive, but it eats into your ownership.'],
 'pipe':['PIPE','“Private Investment in Public Equity” — a big block of stock sold directly to a group of investors (often the specialist funds) in one shot, usually at a set price. A large PIPE at a low price means big dilution but also a strong vote of confidence from whoever bought in.'],
 'atm':['ATM offering','“At-the-market” — the company drips new shares into the open market over time at prevailing prices. Flexible cash, but it means steady, ongoing dilution.'],
 'shelf':['Shelf registration','A pre-approved paperwork filing that lets a company sell stock quickly whenever it wants. A big shelf = the ability (and often the intent) to raise more, i.e. more dilution ahead.'],
 'fast track':['Fast Track','An FDA status that speeds up review for drugs treating serious diseases with unmet need. It shortens the path to market — a mild de-risking positive.'],
 'orphan drug':['Orphan Drug','An FDA designation for drugs treating rare diseases (under ~200,000 US patients). It brings perks (tax credits, 7 years of market exclusivity) but signals a small patient population.'],
 'breakthrough therapy':['Breakthrough Therapy','The FDA\'s strongest expedited status — given when early data looks substantially better than existing treatments. A meaningful positive signal.'],
 'accelerated approval':['Accelerated Approval','A pathway where the FDA can approve a drug on an early surrogate measure (like tumor shrinkage) before final survival data. Faster to market, but approval can be pulled if the confirmatory trial fails.'],
 'orphan':['Orphan / niche market','A small patient population (a rare disease). Upside is capped by how few patients there are, but competition is often thinner and pricing can be high.'],
 'blockbuster':['Blockbuster market','A huge disease market (like diabetes, depression, or common cancers). Massive upside if the drug works, but crowded with competition and expensive to run trials in.']
};
const XPTERMS=Object.keys(XPG).sort((a,b)=>b.length-a.length);
const XPRE=new RegExp('\\b('+XPTERMS.map(t=>t.replace(/[.*+?^${}()|[\]\\]/g,'\\$&')).join('|')+')\\b','gi');
let learnMode=false;
function wrapTerms(root){if(!root)return;
 const skip={SCRIPT:1,STYLE:1,BUTTON:1,INPUT:1,SELECT:1,TEXTAREA:1,A:1,H1:1,H2:1};
 const bad=n=>{let p=n.parentNode;while(p&&p!==root){if(p.nodeName==='svg'||skip[p.nodeName])return true;if(p.classList&&(p.classList.contains('xp')||p.classList.contains('tk')||p.classList.contains('tabintro')))return true;p=p.parentNode;}return false;};
 const w=document.createTreeWalker(root,NodeFilter.SHOW_TEXT,null),nodes=[];
 while(w.nextNode()){const n=w.currentNode;if(!n.nodeValue.trim())continue;XPRE.lastIndex=0;if(!XPRE.test(n.nodeValue))continue;if(bad(n))continue;nodes.push(n);}
 nodes.forEach(n=>{XPRE.lastIndex=0;const html=n.nodeValue.replace(XPRE,m=>{const k=m.toLowerCase();return XPG[k]?'<span class="xp" data-xp="'+k+'">'+m+'</span>':m;});
  if(html!==n.nodeValue){const s=document.createElement('span');s.innerHTML=html;n.parentNode.replaceChild(s,n);}});
}
function applyLearn(container){if(learnMode)wrapTerms(container||document.querySelector('.wrap'));}
const xpPop=document.getElementById('xpPop');
function showXP(key,x,y){const g=XPG[key];if(!g)return;
 xpPop.innerHTML='<span class="xpx" id="xpClose">×</span><div class="xpt">'+g[0]+'</div><div class="xpd">'+g[1]+'</div><div class="xpmore">Open the <b>Guide</b> tab for every term in one place.</div>';
 xpPop.classList.add('on');const w=xpPop.offsetWidth,h=xpPop.offsetHeight,vw=innerWidth,vh=innerHeight;
 let px=Math.min(Math.max(10,x-w/2),vw-w-10),py=y+14;if(py+h>vh-10)py=y-h-14;
 xpPop.style.left=px+'px';xpPop.style.top=Math.max(10,py)+'px';}
function hideXP(){xpPop.classList.remove('on');}
document.getElementById('learnBtn').onclick=()=>{learnMode=!learnMode;
 document.getElementById('learnBtn').classList.toggle('on',learnMode);
 document.body.classList.toggle('learn',learnMode);
 if(learnMode)wrapTerms(document.querySelector('.wrap'));else hideXP();};
document.addEventListener('scroll',hideXP,true);
document.body.addEventListener('click',e=>{
 const xp=e.target.closest('.xp');
 if(learnMode&&xp){e.preventDefault();e.stopPropagation();const r=xp.getBoundingClientRect();showXP(xp.dataset.xp,r.left+r.width/2,r.bottom);return;}
 if(e.target.id==='xpClose'){hideXP();return;}
 if(xpPop.classList.contains('on')&&!e.target.closest('#xpPop')){hideXP();}
 const rb=e.target.closest('.pcrange button');
 if(rb){const box=rb.closest('.pcrange'),sym=box.dataset.sym,win=+rb.dataset.win;
  [...box.children].forEach(b=>b.classList.toggle('on',b===rb));
  const host=document.getElementById('coChart');if(host)host.innerHTML=priceChart(sym,{h:230,win:win});return;}
 if(e.target.closest('.pchart,.pcrange'))return;
 const t=e.target.closest('.tk,[data-sym]');if(t&&t.dataset.sym)openCo(t.dataset.sym);});
function finTables(d){
 if(!d.financials||!d.financials.statements||!d.financials.statements.length)return '';
 const fmt=(v,eps)=>{ if(v==null)return '<span class="mut">&mdash;</span>';
   if(eps)return (v<0?'-$':'$')+Math.abs(v).toFixed(2);
   return (v<0?'-$':'$')+Math.abs(v).toLocaleString('en-US'); };
 let h='<div class="sec"><h4>Financial statements</h4><div class="sub" style="margin-bottom:2px">Straight from SEC filings ('+esc(d.financials.updated)+'). Figures in $ millions unless noted; &mdash; = not separately tagged in that filing. H1 columns are six-month year-to-date.</div>';
 d.financials.statements.forEach(st=>{
   const isEpsTbl=false;
   h+='<div class="fintbl"><div class="fintname">'+esc(st.name)+' <span class="mut" style="font-weight:400;text-transform:none;letter-spacing:0">&middot; '+esc(st.unit)+'</span></div>';
   h+='<div class="finscroll"><table class="fin"><thead><tr><th class="finlab"></th>'+st.cols.map(c=>'<th>'+esc(c)+'</th>').join('')+'</tr></thead><tbody>';
   st.rows.forEach(r=>{ const eps=/\$\/sh|EPS/.test(r[0]);
     h+='<tr><td class="finlab">'+esc(r[0])+'</td>'+r[1].map(v=>'<td class="'+(v!=null&&v<0?'neg':'')+'">'+fmt(v,eps)+'</td>').join('')+'</tr>'; });
   h+='</tbody></table></div></div>';
 });
 return h+'</div>';
}
function openCo(sym){
 const d=dosBy[sym],sc=scrBy[sym]||(d&&d.alias?scrBy[d.alias]:null);
 const rws=R.filter(r=>S[r[1]][0]===sym);
 const rr=(typeof RAD!=='undefined'&&RAD)?RAD.find(x=>x[0]===sym):null;
 const nm=d?d.name:(rr?rr[1]:(rws[0]?S[rws[0][1]][1]:sym));
 const price=d?d.price:px(sym);
 const rk={beta:bt(sym),vol:vl(sym),mdd:mdd(sym),lo:lo52(sym),hi:hi52(sym),pos:p52(sym),r1:r1(sym),sq:sq(sym)};
 let h='<div class="phead"><div style="flex:1"><div style="font-size:18px;font-weight:600;letter-spacing:-.01em">'+esc(nm)+
  ' <span class="mut" style="font-size:14px;font-weight:500">'+esc(sym)+(d&&d.alias?' · was '+d.alias:'')+'</span></div>'+
  '<div class="sub" style="margin-top:3px">'+(d?esc(d.sector)+' · '+esc(d.stage)+' · $'+d.mcapB.toFixed(2)+'B':(rr?esc(rr[8])+' · $'+(rr[2]>=1?rr[2].toFixed(2)+'B':(rr[2]*1000).toFixed(0)+'M'):'13F holding'))+'</div></div>'+
  (d?'<div style="text-align:right;min-width:170px"><div class="sub">Survival score</div>'+
     '<div class="ssrow" style="justify-content:flex-end;margin-top:2px"><span class="ssnum">'+d.survScore.toFixed(0)+'</span><span class="sslabel" style="color:'+survBand(d.survScore)[1]+'">'+survBand(d.survScore)[0]+'</span></div>'+
     '<div style="margin-top:6px">'+survScale(d.survScore,{w:'170px',labels:true})+'</div>'+
     '<div class="sub" style="margin-top:4px">scale −110 to 120 · click the number in Learn mode</div></div>':'')+
  '<div style="display:flex;flex-direction:column;gap:5px"><button class="btn" onclick="closeCo()">Close</button>'+
  '<button class="btn" onclick="cmpLoad(\''+esc(sym)+'\',0)">Compare ◀</button>'+
  '<button class="btn" onclick="cmpLoad(\''+esc(sym)+'\',1)">Compare ▶</button></div></div><div class="pbody">';
 const lsym=(d&&d.alias&&PQ[d.alias])?d.alias:sym;
 const hasQ1=!!q1avg(lsym), hasSer=!!serOf(lsym);
 if(hasSer){
  h+='<div class="sec"><h4>Stock price'+(hasQ1?' — and what they bought at':'')+'</h4>';
  if(hasQ1){const v=vsQ1(lsym),m=vsMk(lsym);
   h+='<div class="pstrip">'+
   [['Q1 range they bought in','$'+q1lo(lsym)+' – $'+q1hi(lsym)],
    ['Their Q1 average','$'+q1avg(lsym).toFixed(2)],
    ['Marked at 31 Mar','$'+mk31(lsym).toFixed(2)],
    ['Price now','$'+px(lsym).toFixed(2)],
    ['vs their average',(v<=0?'<span class="pos">':'<span class="neg">')+(v>0?'+':'')+(v*100).toFixed(0)+'%</span>'],
    ['vs 31 Mar mark',(m<=0?'<span class="pos">':'<span class="neg">')+(m>0?'+':'')+(m*100).toFixed(0)+'%</span>']]
   .map(x=>'<div><div class="k">'+x[0]+'</div><div class="v">'+x[1]+'</div></div>').join('')+'</div>';}
  h+='<div class="pcrange" data-sym="'+esc(lsym)+'">'+
     '<button data-win="9999" class="on">2Y</button><button data-win="365">1Y</button><button data-win="182">6M</button><button data-win="90">3M</button></div>'+
   '<div id="coChart">'+priceChart(lsym,{h:230})+'</div>'+
   (sym==='DMRA'||lsym==='DMRA'?'<div class="axisnote">The step-change in early 2026 is the reverse merger that formed Damora — before it, the line is the predecessor Galecto (GLTO) shell.</div>':'')+
   (hasQ1?'<div class="axisnote">The blue shaded band is the stock\'s actual Q1 2026 trading range — the window the funds were buying in, so their true average cost sits inside it. The hollow dot marks the 31 March price they reported their position at. Hover the line for any week\'s close.</div>':'<div class="axisnote">Two years of weekly closes. Hover the line for any week\'s price.</div>')+'</div>';
 }
 if(d){
  h+='<div class="sec"><h4>What this company actually is</h4><div class="prose">'+esc(d.what)+
     '</div><div class="prose" style="margin-top:8px"><b style="color:var(--t1)">Lead asset:</b> '+esc(d.leadAsset)+'</div></div>';
  if(d.market||d.fda||d.financing){
   const mkt=d.market,fda=d.fda,fin=d.financing;
   h+='<div class="sec"><h4>Market, regulatory &amp; financing</h4><div class="mrf">'+
    (mkt?'<div class="mrfrow"><div class="mrfl">Market size</div><div class="mrfr"><span class="mtag">'+esc(mkt.size)+'</span> <b>'+esc(mkt.indication)+'</b><div class="mrfd">'+esc(mkt.detail)+'</div></div></div>':'')+
    (fda?'<div class="mrfrow"><div class="mrfl">FDA status</div><div class="mrfr">'+
      (fda.items&&fda.items.length?fda.items.map(x=>'<span class="fdatag">'+esc(x)+'</span>').join(' '):'<span class="mut">No special designations</span>')+
      (fda.note?'<div class="mrfd">'+esc(fda.note)+'</div>':'')+'</div></div>':'')+
    (fin?'<div class="mrfrow"><div class="mrfl">Latest financing</div><div class="mrfr"><b>'+esc(fin.last)+'</b><div class="mrfd">'+esc(fin.note)+'</div></div></div>':'')+
   '</div></div>';
  }
  h+='<div class="sec"><h4>Survival math</h4><div class="surv"><div style="display:flex;gap:22px;flex-wrap:wrap;align-items:baseline">'+
   [['Cash',money(d.cashM),''],['Debt',d.debtM?money(d.debtM):'none',d.debtM>d.cashM?'color:var(--bad)':''],
    ['Burn / quarter',d.quarterlyBurnM?money(d.quarterlyBurnM):'—',''],
    ['Runway',d.runwayQtrs==null?'profitable':d.runwayQtrs.toFixed(1)+' qtrs','color:var(--'+(d.bucket==='Funded'?'good':d.bucket==='Tight'?'warn':'bad')+')'],
    ['Catalyst in',d.catalystQtrs.toFixed(1)+' qtrs','']]
   .map(x=>'<div><div style="font-size:10px;color:var(--t3);text-transform:uppercase;letter-spacing:.04em">'+x[0]+'</div><div class="big" style="'+x[2]+'">'+x[1]+'</div></div>').join('')+
   '</div><div class="deriv"><b style="color:var(--t1)">How this was derived — </b>'+esc(d.runwayNote)+'</div></div></div>';
  const kv=[['Market cap','$'+d.mcapB.toFixed(2)+'B'],['Price','$'+d.price.toFixed(2)],['Enterprise value',money(d.evM)],
   ['Shares out',d.sharesOutM.toFixed(1)+'M'],['Revenue TTM',d.revenueTTM_M?money(d.revenueTTM_M):'none'],
   ['Net income TTM',money(d.netIncomeTTM_M)],['Op cash flow TTM',money(d.opCashFlowTTM_M)],
   ['Net cash',money(d.netCashM)],['Net cash / cap',d.netCashPctMcap.toFixed(0)+'%'],
   ['Short % float',d.shortPctFloat==null?'—':d.shortPctFloat.toFixed(1)+'%'],
   ['Analyst target',d.analystTarget?'$'+d.analystTarget.toFixed(2):'—'],
   ['Rating',(d.analystRating||'—')+(d.analystCount?' ('+d.analystCount+')':'')],
   ['Beta',rk.beta==null?'n/a':rk.beta.toFixed(2)],['Volatility',rk.vol==null?'n/a':(rk.vol*100).toFixed(0)+'%'],
   ['Max drawdown 2y',rk.mdd==null?'n/a':(rk.mdd*100).toFixed(0)+'%'],
   ['52-week range',rk.lo==null?'n/a':'$'+rk.lo+' – $'+rk.hi]];
  h+='<div class="sec"><h4>The numbers</h4><div class="kv">'+kv.map(k=>'<div><div class="k">'+k[0]+'</div><div class="v">'+k[1]+'</div></div>').join('')+'</div></div>';
  h+=finTables(d);
  h+='<div class="grid g2 sec"><div><h4>Most recent reported quarter</h4><div class="prose"><b style="color:var(--t1)">'+esc(d.latestReport.period)+(d.latestReport.date?' · '+esc(d.latestReport.date):'')+'</b><br>'+esc(d.latestReport.highlights)+'</div></div>'+
   '<div><h4>Next catalyst</h4><div class="prose"><b style="color:var(--t1)">'+esc(d.nextCatalyst.when||'timing unclear')+'</b><br>'+esc(d.nextCatalyst.what)+'</div></div></div>';
  h+='<div class="grid g2 sec"><div class="bull"><h4 style="color:var(--good)">The case for</h4><ul class="bb">'+d.bull.map(b=>'<li>'+esc(b)+'</li>').join('')+'</ul></div>'+
   '<div class="bear"><h4 style="color:var(--bad)">The case against</h4><ul class="bb">'+d.bear.map(b=>'<li>'+esc(b)+'</li>').join('')+'</ul></div></div>';
  if(d.flags&&d.flags.length)h+='<div class="sec"><h4>Material warnings from the filings</h4><div class="flags'+(d.bucket==='Distressed'?' crit':'')+'"><ul>'+d.flags.map(f=>'<li>'+esc(f)+'</li>').join('')+'</ul></div></div>';
 } else {
  const bn=(D.q2move&&D.q2move.byName&&D.q2move.byName[sym])||null;
  const held=(bn&&bn.filed)||[];
  h+='<div class="sec"><div class="flags"><b style="color:var(--t1)">Quick profile.</b> '+(rr?esc(rr[1]):esc(sym))+' has no full research dossier yet — those cover the highest-signal names. Here is what the 13F filings and market data show, including which funds hold it and how they moved this quarter.</div></div>';
  if(rr){const pct=rr[10],c=pct>0?'var(--good)':pct<0?'var(--bad)':'var(--t3)';
   h+='<div class="sec"><h4>What they hold it at — vs where it is now</h4><div class="pstrip">'+
    [['Their 30-Jun mark',rr[3]?'$'+rr[3].toFixed(2):'—'],
     ['Price now',rr[9]?'$'+rr[9].toFixed(2):'—'],
     ['Since 30 Jun',pct==null?'—':'<span style="color:'+c+'">'+(pct>0?'+':'')+pct+'%</span>'],
     ['Market cap',rr[2]>=1?'$'+rr[2].toFixed(2)+'B':'$'+(rr[2]*1000).toFixed(0)+'M'],
     ['Beta 1Y',rr[12]==null?'n/a':rr[12].toFixed(2)],
     ['Alpha 1Y',rr[13]==null?'n/a':(rr[13]>0?'+':'')+rr[13]+'%']]
    .map(x=>'<div><div class="k">'+x[0]+'</div><div class="v">'+x[1]+'</div></div>').join('')+'</div>'+
    '<div class="axisnote">The 30-Jun mark is the price implied by the 13F (reported value / shares) — the closest public proxy to the funds cost basis. &ldquo;Since 30 Jun&rdquo; is the unrealized gain or loss on that entry.</div></div>';}
  if(held.length){h+='<div class="sec"><h4>'+held.length+' fund'+(held.length>1?'s':'')+' hold this — and how they moved</h4><div class="prose">'+
    held.slice().sort((a,b)=>(b.q2||0)-(a.q2||0)).map(m=>'<span class="chip '+(m.m==='NEW'?'n':m.m==='ADD'?'g':m.m==='TRIM'?'w':'')+'" style="margin:0 6px 6px 0;display:inline-block">'+esc(m.short)+' · '+m.m+(m.q2?' · '+N(m.q2)+' sh':'')+'</span>').join('')+
    '</div><div class="axisnote">Green = a fund added, blue = opened a new position, amber = trimmed. A name with funds on both sides is the divergence worth reading.</div></div>';}
  if(rr){h+='<div class="sec"><h4>On the Radar board</h4><div class="kv">'+
    [['Sector',esc(rr[8])],['Funds holding',''+rr[4]],['Combined invested',rr[6]>=1000?'$'+(rr[6]/1000).toFixed(2)+'B':'$'+rr[6].toFixed(1)+'M'],['Ticker',esc(sym)]]
    .map(k=>'<div><div class="k">'+k[0]+'</div><div class="v">'+k[1]+'</div></div>').join('')+'</div></div>';}
  else{h+='<div class="sec"><h4>Market data</h4><div class="kv">'+
    [['Price',price?'$'+(+price).toFixed(2):'—'],['Beta',rk.beta==null?'n/a':rk.beta.toFixed(2)],['52-week range',rk.lo==null?'n/a':'$'+rk.lo+' – $'+rk.hi],['Held by',nh(sym)+' of '+SMID.length+' signal funds']]
    .map(k=>'<div><div class="k">'+k[0]+'</div><div class="v">'+k[1]+'</div></div>').join('')+'</div></div>';}
 }
 if(sc){h+='<div class="sec"><h4>Fund conviction</h4><div class="prose">'+
  (sc.funds||[]).map(f=>'<span class="chip '+(f[1]==='NEW'?'n':'')+'" style="margin-right:5px">'+esc(f[0])+' '+f[1]+' $'+f[2]+'M</span>').join('')+
  '<div style="margin-top:8px">Combined '+(sc.totValM!=null?'$'+sc.totValM+'M':'—')+' · these funds hold about <b style="color:var(--t1)">'+(sc.ownPct!=null?sc.ownPct+'%':'—')+
  '</b> of the company · largest position is '+(sc.maxBookPct!=null?sc.maxBookPct+'%':'—')+' of that manager’s book · reported value implies about '+
  (sc.mark?'$'+sc.mark:'—')+'/share (13F value ÷ shares) versus '+(price?'$'+(+price).toFixed(2):'—')+' now</div></div></div>';}
 if(rws.length){h+='<div class="sec"><h4>Every disclosed position in this name</h4>'+
  '<div class="axisnote" style="margin-bottom:8px">“Trajectory” shows each fund\'s share count last quarter versus now (Q4 → Q1) — building, trimming, or freshly opened. A third bar appears when the Q2 filings land.</div>'+
  '<div class="tw" style="max-height:none"><table><thead><tr>'+
  '<th class="l">Manager</th><th class="l">Type</th><th class="l">Change</th><th class="l">Trajectory</th><th>Value</th><th>Shares</th><th>Prev shares</th><th>% of book</th><th>Marked at</th><th>Price now</th><th>vs mark</th></tr></thead><tbody>'+
  rws.sort((a,b)=>b[2]-a[2]).map(r=>'<tr><td class="l">'+esc(F[r[0]].name)+'</td><td class="l"><span class="chip">'+['SHARES','CALL','PUT','NOTES'][r[4]]+'</span></td>'+
  '<td class="l">'+(r[5]?'<span class="chip '+(r[5]==='NEW'?'n':r[5]==='ADD'?'g':r[5]==='TRIM'?'w':'')+'">'+r[5]+'</span>':'—')+'</td>'+
  '<td class="l">'+traj(r[6],r[3],r[5])+'</td>'+
  '<td>'+K(r[2])+'</td><td>'+N(r[3])+'</td><td>'+(r[6]?N(r[6]):'—')+'</td><td>'+(r[7]?pc(r[7],2):'—')+'</td>'+
  '<td>'+(rowMark(r)?'$'+rowMark(r).toFixed(2):'—')+'</td><td>'+(px(S[r[1]][0])?'$'+px(S[r[1]][0]).toFixed(2):'—')+'</td><td>'+sgE(rowVs(r))+'</td></tr>').join('')+'</tbody></table></div></div>';}
 document.getElementById('panC').innerHTML=h;
 applyLearn(document.getElementById('panC'));
 pan.scrollTop=0;ovl.classList.add('on');pan.classList.add('on');
}
window.cmpLoad=function(sym,side){const el=document.getElementById(side?'cmpB':'cmpA');
 if([...el.options].some(o=>o.value===sym)){el.value=sym;closeCo();go('cmp');drawCmp();}
 else alert(sym+' is not in the candidate list.');};
/* command bar */
const cmd=document.getElementById('cmd');
cmd.addEventListener('keydown',e=>{if(e.key!=='Enter')return;
 const q=cmd.value.trim().toUpperCase();if(!q)return;
 if(A[q]||dosBy[q]||S.some(s=>s[0]===q)){openCo(q);cmd.value='';return;}
 const m=S.find(s=>s[1]&&s[1].toUpperCase().includes(q)&&s[0]);
 if(m){openCo(m[0]);cmd.value='';return;}
 go('hold');document.getElementById('hQ').value=q;holdT();});

/* ---------- overview ---------- */
const totLong=SMID.reduce((a,f)=>a+f.longK,0);
document.getElementById('ovTiles').innerHTML=[
 ['Signal funds',String(SMID.length),'8 specialists/generalists + RTW & Cormorant (added this quarter)'],
 ['Combined long book',K(totLong),'small/mid specialists only'],
 ['New positions last quarter',SMID.reduce((a,f)=>a+f.newBuys,0),'before filters'],
 ['Screened candidates','33','after removing SPACs, private and acquired'],
 ['Full dossiers',String(DOS.length),'deep research complete'],
 ['Funded through catalyst',DOS.filter(d=>d.bucket==='Funded').length+' of '+DOS.length,'can reach the readout without raising']
].map(t=>'<div class="tile"><div class="lab">'+t[0]+'</div><div class="val">'+t[1]+'</div><div class="dlt">'+t[2]+'</div></div>').join('');

function ovShift(){
 const byConv=[...DOS].sort((a,b)=>(b.convScore||0)-(a.convScore||0)).map(d=>d.sym);
 const rows=DOS.map((d,si)=>({sym:d.sym,surv:si+1,conv:byConv.indexOf(d.sym)+1}));
 rows.sort((a,b)=>Math.abs(b.conv-b.surv)-Math.abs(a.conv-a.surv));
 document.getElementById('ovShift').innerHTML=rows.map(r=>{
  const delta=r.conv-r.surv,w=Math.abs(delta)/Math.max(1,DOS.length-1)*46;
  const bar=delta>=0?'<i class="dvbar" style="left:50%;width:'+w+'%;background:var(--good)"></i>'
                    :'<i class="dvbar" style="left:'+(50-w)+'%;width:'+w+'%;background:var(--bad)"></i>';
  return '<div class="crow"><div class="cnm" data-sym="'+r.sym+'">'+r.sym+'</div><div class="dvtrack">'+bar+'<i class="dvzero" style="left:50%"></i></div>'+
   '<div class="cval">#'+r.conv+' → #'+r.surv+'</div></div>';}).join('');
 document.getElementById('ovShiftNote').innerHTML='Green = the balance sheet improved its standing, red = the balance sheet demoted it. <b>Karyopharm sits last on survival despite mid-pack fund conviction</b>: an explicit going-concern warning, ~$250M of debt against $65M of cash, and a September payment cliff. Its apparent deep "discount" to the funds’ mark is the collapse, not an opportunity — the clearest case of why conviction alone misleads.';
}
function ovEntry(){
 const rows=[...DOS].map(d=>({d,sym:d.alias&&PQ[d.alias]?d.alias:d.sym}))
   .filter(r=>q1avg(r.sym)&&px(r.sym)).map(r=>{
     const av=q1avg(r.sym);
     return {sym:r.d.sym,ls:r.sym,now:px(r.sym)/av-1,
       mark:mk31(r.sym)?mk31(r.sym)/av-1:null,
       lo:q1lo(r.sym)/av-1,hi:q1hi(r.sym)/av-1};})
   .sort((a,b)=>a.now-b.now);
 const W=1000,L=66,Rp=132,T=30,rowH=32,B=8,H=T+rows.length*rowH+B;
 const DMAX=0.85,DMIN=-0.85,pw=W-L-Rp;
 const clamp=v=>Math.max(DMIN,Math.min(DMAX,v));
 const X=v=>L+(clamp(v)-DMIN)/(DMAX-DMIN)*pw;
 const fmt=v=>(v>0?'+':'')+(v*100).toFixed(0)+'%';
 let g='';
 /* vertical gridlines + axis labels */
 [-0.75,-0.5,-0.25,0,0.25,0.5,0.75].forEach(t=>{const x=X(t).toFixed(1),zero=t===0;
  g+='<line x1="'+x+'" y1="'+(T-6)+'" x2="'+x+'" y2="'+(H-B)+'" stroke="var(--'+(zero?'t2':'line')+')" stroke-width="'+(zero?1.4:1)+'"'+(zero?'':' stroke-dasharray="2 3"')+'/>'+
     '<text x="'+x+'" y="'+(T-12)+'" text-anchor="middle" font-size="10.5" fill="var(--'+(zero?'t1':'t3')+')"'+(zero?' font-weight="600"':'')+'>'+(zero?'their avg cost':fmt(t))+'</text>';});
 rows.forEach((r,i)=>{const cy=T+i*rowH+rowH/2;
  /* Q1 buying-range band */
  const bx=X(r.lo),bw=Math.max(2,X(r.hi)-X(r.lo));
  g+='<rect x="'+bx.toFixed(1)+'" y="'+(cy-8).toFixed(1)+'" width="'+bw.toFixed(1)+'" height="16" rx="3" fill="var(--blue)" opacity="0.12"/>';
  /* stem from zero (their cost) to today's dot */
  const x0=X(0),xn=X(r.now),col=r.now<=0?'var(--good)':'var(--bad)';
  g+='<line x1="'+x0.toFixed(1)+'" y1="'+cy+'" x2="'+xn.toFixed(1)+'" y2="'+cy+'" stroke="'+col+'" stroke-width="3" stroke-linecap="round"/>';
  /* today's price — the single dot */
  g+='<circle cx="'+xn.toFixed(1)+'" cy="'+cy+'" r="5.5" fill="'+col+'" stroke="var(--s1)" stroke-width="1.5"/>';
  /* ticker label (clickable) */
  g+='<text class="tk" data-sym="'+esc(r.sym)+'" x="'+(L-10)+'" y="'+cy+'" text-anchor="end" dominant-baseline="middle" font-size="12.5" font-weight="600" fill="var(--t1)" style="cursor:pointer">'+esc(r.sym)+'</text>';
  /* value label */
  g+='<text x="'+(W-Rp+12)+'" y="'+cy+'" dominant-baseline="middle" font-size="12" font-weight="600" fill="'+col+'">'+fmt(r.now)+'</text>'+
     '<text x="'+(W-Rp+64)+'" y="'+cy+'" dominant-baseline="middle" font-size="11" fill="var(--t3)">vs avg</text>';});
 document.getElementById('cEntry').innerHTML='<svg viewBox="0 0 '+W+' '+H+'" style="width:100%;height:auto" font-family="inherit">'+g+'</svg>';
}
function ovAct(){
 const AF=SMID.filter(f=>f.newBuys!=null);
 const mx=Math.max(...AF.map(f=>f.newBuys+f.adds+f.trims+f.exits));
 document.getElementById('ovAct').innerHTML=AF.map(f=>{
  const seg=[[f.newBuys,'var(--good)'],[f.adds,'var(--r400)'],[f.trims,'var(--r100)'],[f.exits,'var(--bad)']];
  let x=0,h='';seg.forEach(([v,c])=>{const w=v/mx*100;h+='<i class="dvbar" style="left:'+x+'%;width:'+w+'%;background:'+c+'"></i>';x+=w;});
  return '<div class="crow"><div class="cnm">'+esc(f.name.split(' ')[0])+'</div><div class="dvtrack">'+h+'</div>'+
   '<div class="cval">'+f.newBuys+' new</div></div>';}).join('');
}
/* ---------- tables ---------- */
function tbl(el,cols,get,def,cntId){
 let sk=def,sd=-1;
 function paint(){
  const rows=[...get()].sort((a,b)=>{const x=cols[sk].v(a),y=cols[sk].v(b);
   if(x==null)return 1;if(y==null)return -1;
   return typeof x==='string'||typeof y==='string'?-sd*String(x).localeCompare(String(y)):sd*(x-y);});
  el.innerHTML='<thead><tr>'+cols.map((c,i)=>'<th class="'+(c.l?'l':'')+'" data-i="'+i+'" title="'+esc(c.tip||c.t)+'">'+c.t+(sk===i?'<span style="opacity:.5"> '+(sd<0?'▼':'▲')+'</span>':'')+'</th>').join('')+'</tr></thead><tbody>'+
   rows.slice(0,600).map(x=>'<tr>'+cols.map(c=>'<td class="'+(c.l?'l':'')+'">'+c.r(x)+'</td>').join('')+'</tr>').join('')+'</tbody>';
  if(cntId)document.getElementById(cntId).textContent=N(rows.length)+' rows'+(rows.length>600?' · showing 600':'');
 }
 el.onclick=e=>{const t=e.target.closest('th');if(!t)return;const i=+t.dataset.i;if(sk===i)sd=-sd;else{sk=i;sd=-1}paint();};
 return {paint};
}
const survRank={};[...DOS].sort((a,b)=>b.survScore-a.survScore).forEach((d,i)=>survRank[d.sym]=i+1);
const quickT=tbl(document.getElementById('tQuick'),[
 {t:'#',l:1,v:d=>d.survScore,r:d=>'<span class="mut">'+survRank[d.sym]+'</span>'},
 {t:'Ticker',l:1,v:d=>d.sym,r:d=>TK(d.sym)},
 {t:'Company',l:1,v:d=>d.name,r:d=>'<span class="iss">'+esc(d.name)+'</span>'},
 {t:'Status',l:1,v:d=>d.survScore,r:d=>'<span class="chip '+bcls(d.bucket)+'">'+d.bucket+'</span>'},
 {t:'Runway',v:d=>d.runwayQtrs==null?99:d.runwayQtrs,r:d=>d.runwayQtrs==null?'<span class="pos">profitable</span>':'<b>'+d.runwayQtrs.toFixed(1)+'</b>q'},
 {t:'Mkt cap',v:d=>d.mcapB,r:d=>'$'+d.mcapB.toFixed(2)+'B'},
 {t:'Funds own',v:d=>d.ownPct,r:d=>d.ownPct==null?'—':d.ownPct+'%'},
 {t:'Price · 2Y',l:1,v:d=>vsQ1(d.alias&&PQ[d.alias]?d.alias:d.sym),r:d=>sparkChart(d.alias&&PQ[d.alias]?d.alias:d.sym,120,32),tip:'Two-year weekly price. Shaded band = the Q1 range the funds bought in · hollow dot = 31 Mar mark · line ends at today'},
 {t:'vs Q1 avg',v:d=>vsQ1(d.alias&&PQ[d.alias]?d.alias:d.sym),r:d=>sgE(vsQ1(d.alias&&PQ[d.alias]?d.alias:d.sym)),tip:'Today versus their average cost through the quarter they were buying'},
 {t:'vs 31 Mar mark',v:d=>d.entry,r:d=>sgE(d.entry)},
 {t:'Beta',v:d=>bt(d.alias||d.sym),r:d=>{const b=bt(d.alias||d.sym);return b==null?'<span class="mut">n/a</span>':b.toFixed(2)}},
 {t:'Survival',v:d=>d.survScore,r:d=>'<b>'+d.survScore.toFixed(0)+'</b>'}
],()=>DOS,11);
/* screen */
/* ---------- Radar: full <$10B universe ---------- */
const RAD=(D.radar&&D.radar.rows)||[];          /* [sym,name,mcapB,pxJun,nf,fundsStr,totValM,dossier,sector,pxNow,pctVsJun,dayChg] */
const FTYPE={};(D.q2move&&D.q2move.fundStatus||[]).forEach(f=>{FTYPE[f.short]=f.ftype;});
let radSecSel='All';
(function(){const el=document.getElementById('radSec');if(!el)return;
 const cnt={};RAD.forEach(r=>{cnt[r[8]]=(cnt[r[8]]||0)+1;});
 const secs=['All'].concat(Object.keys(cnt).sort((a,b)=>cnt[b]-cnt[a]));
 el.innerHTML=secs.map(x=>'<button class="stab'+(x==='All'?' on':'')+'" data-sec="'+esc(x)+'">'+esc(x)+' <span class="scnt">'+(x==='All'?RAD.length:cnt[x])+'</span></button>').join('');
 el.onclick=e=>{const b=e.target.closest('.stab');if(!b)return;radSecSel=b.dataset.sec;[...el.children].forEach(c=>c.classList.toggle('on',c===b));radarT.paint();};
})();
function radarRows(){
 const q=(document.getElementById('radQ').value||'').toUpperCase().trim();
 const f=document.getElementById('radF').value, sz=document.getElementById('radS').value, dos=document.getElementById('radDos').checked;
 return RAD.filter(r=>{
  if(radSecSel!=='All'&&r[8]!==radSecSel)return false;
  if(f&&r[4]<+f)return false;
  if(sz&&r[2]>+sz)return false;
  if(dos&&!r[7])return false;
  if(q&&!(r[0].includes(q)||(r[1]||'').toUpperCase().includes(q)))return false;
  return true;});
}
const radFundChips=str=>(str||'').split('|').map(f=>{const ft=(FTYPE[f]||'conviction');return '<span class="chip" style="background:color-mix(in srgb,'+(ft==='flow'?'var(--blue)':'var(--good)')+' 13%,transparent);color:'+(ft==='flow'?'var(--blue)':'var(--good)')+'">'+esc(f)+'</span>';}).join(' ');
const fmtM=v=>v==null?'—':'$'+(v>=1000?(v/1000).toFixed(2)+'B':v.toFixed(1)+'M');
const fmtMcap=v=>v==null?'—':'$'+(v>=1?v.toFixed(2)+'B':(v*1000).toFixed(0)+'M');
const radarT=tbl(document.getElementById('tRadar'),[
 {t:'Ticker',l:1,v:r=>r[0],r:r=>TK(r[0])},
 {t:'Company',l:1,v:r=>r[1],r:r=>'<span class="iss tk" data-sym="'+esc(r[0])+'" title="'+esc(r[1])+'">'+esc(r[1])+'</span>'},
 {t:'Sector',l:1,v:r=>r[8],r:r=>'<span class="chip">'+esc(r[8])+'</span>'},
 {t:'# funds',v:r=>r[4],r:r=>'<b style="color:'+(r[4]>=4?'var(--good)':r[4]>=2?'var(--t1)':'var(--t3)')+'">'+r[4]+'</b>'},
 {t:'Invested $',v:r=>r[6],r:r=>'<span title="Combined market value across the holding funds, at each fund&#39;s 30-Jun 13F mark">'+fmtM(r[6])+'</span>'},
 {t:'Mkt cap',v:r=>r[2],r:r=>fmtMcap(r[2])},
 {t:'Cost · 30 Jun',v:r=>r[3],r:r=>'<span title="Price implied by the funds 30-Jun 13F (value / shares) — the closest public proxy to their cost basis">'+(r[3]?'$'+r[3].toFixed(2):'—')+'</span>'},
 {t:'Price now',v:r=>r[9]==null?-1:r[9],r:r=>{if(r[9]==null)return '<span class="mut">—</span>';const dc=r[11]||0;return '$'+r[9].toFixed(2)+' <span style="font-size:11px;color:'+(dc>=0?'var(--good)':'var(--bad)')+'">'+(dc>=0?'+':'')+dc.toFixed(1)+'%</span>';}},
 {t:'vs 30 Jun',v:r=>r[10]==null?-9999:r[10],r:r=>{if(r[10]==null)return '<span class="mut">—</span>';const p=r[10];const c=p>0?'var(--good)':p<0?'var(--bad)':'var(--t3)';return '<b style="color:'+c+'" title="30-Jun mark $'+(r[3]||0).toFixed(2)+' → now $'+(r[9]||0).toFixed(2)+'">'+(p>0?'+':'')+p+'%</b>';}},
 {t:'Beta',v:r=>r[12]==null?-99:r[12],r:r=>{if(r[12]==null)return '<span class="mut" title="Insufficient price history (recent IPO)">n/a</span>';const b=r[12];const c=b>=1.5?'var(--bad)':b>=0.8?'var(--t1)':'var(--good)';return '<span title="1-year weekly beta vs SPY" style="color:'+c+'">'+b.toFixed(2)+'</span>';}},
 {t:'Alpha 1Y',v:r=>r[13]==null?-99999:r[13],r:r=>{if(r[13]==null)return '<span class="mut">n/a</span>';const a=r[13];const c=a>0?'var(--good)':'var(--bad)';return '<span title="Annualized 1Y alpha vs SPY (CAPM). For single-asset biotechs this is dominated by binary catalyst moves — read directionally." style="color:'+c+'">'+(a>0?'+':'')+a+'%</span>';}},
 {t:'Survival',v:r=>{const d=dosBy[r[0]];return d?d.survScore:-99999;},r:r=>{const d=dosBy[r[0]];if(!d)return '<span class="mut" title="No full dossier yet — click the ticker for the 13F quick profile">—</span>';const b=survBand(d.survScore);return '<b title="'+esc(d.bucket)+' · click ticker for the full dossier" style="color:'+b[1]+'">'+d.survScore.toFixed(0)+'</b>';}},
 {t:'Funds holding',l:1,v:r=>r[4],r:r=>radFundChips(r[5])}
],radarRows,3,'radCnt');
['radF','radS'].forEach(i=>document.getElementById(i).onchange=()=>radarT.paint());
document.getElementById('radDos').onchange=()=>radarT.paint();
document.getElementById('radQ').oninput=()=>radarT.paint();
const _rn=document.getElementById('radN');if(_rn&&D.radar)_rn.textContent=D.radar.fundsFiled;

/* companies list */
document.getElementById('coList').innerHTML=DOS.map((d,i)=>
 '<div class="card" style="padding:0;margin-bottom:10px;cursor:pointer" data-sym="'+d.sym+'">'+
 '<div style="display:grid;grid-template-columns:38px 1fr auto;gap:13px;align-items:center;padding:14px 17px">'+
 '<div style="font-size:18px;font-weight:600;color:var(--t3);text-align:center">'+(i+1)+'</div>'+
 '<div><div style="font-size:14.5px;font-weight:600">'+esc(d.name)+' <span class="mut" style="font-size:12.5px;font-weight:500">'+d.sym+'</span></div>'+
 '<div class="sub" style="margin-top:2px">'+esc(d.sector)+' · $'+d.mcapB.toFixed(2)+'B · '+esc(d.leadAsset.slice(0,88))+(d.leadAsset.length>88?'…':'')+'</div></div>'+
 '<div style="display:flex;gap:16px;align-items:center;text-align:right"><div><div class="sub">Runway</div><div style="font-size:14px;font-weight:600">'+(d.runwayQtrs==null?'profit':d.runwayQtrs.toFixed(1)+'q')+'</div></div>'+
 '<div><div class="sub">Survival</div><div style="font-size:14px;font-weight:600">'+d.survScore.toFixed(0)+'</div></div>'+
 '<span class="chip '+bcls(d.bucket)+'">'+d.bucket+'</span></div></div></div>').join('');

/* survival charts */
function drawRun(){
 const mx=Math.max(...DOS.map(d=>Math.max(d.runwayQtrs||0,d.catalystQtrs)),16);
 document.getElementById('cRun').innerHTML=[...DOS].sort((a,b)=>b.survScore-a.survScore).map(d=>{
  const prof=d.runwayQtrs==null,w=prof?100:Math.max(1.5,d.runwayQtrs/mx*100);
  return '<div class="crow"><div class="cnm" data-sym="'+d.sym+'">'+d.sym+'</div><div class="ctrack">'+
  '<i class="cfill '+bcls(d.bucket)+'" style="width:'+w.toFixed(1)+'%"></i>'+
  '<i class="cmark" style="left:'+Math.min(d.catalystQtrs/mx*100,99).toFixed(1)+'%" title="'+esc(d.catalystLabel)+'"></i></div>'+
  '<div class="cval">'+(prof?'profitable':d.runwayQtrs.toFixed(1)+' qtrs')+'</div></div>';}).join('');
}
const SC=[['runway','Runway','var(--r650)'],['catalyst','Reaches catalyst','var(--r400)'],['balance','Balance sheet','var(--r250)'],['conviction','Fund conviction','var(--r100)'],['entry','Entry vs mark','var(--pur)'],['goingConcern','Going concern','var(--bad)']];
function drawScore(){
 const p=Math.max(...DOS.map(d=>Object.values(d.sc).filter(v=>v>0).reduce((a,b)=>a+b,0)));
 const n=Math.abs(Math.min(...DOS.map(d=>Object.values(d.sc).filter(v=>v<0).reduce((a,b)=>a+b,0))));
 const T=p+n||1,z=n/T*100;
 document.getElementById('cScore').innerHTML=[...DOS].sort((a,b)=>b.survScore-a.survScore).map(d=>{
  let pos=z,neg=z,h='';
  SC.forEach(([k,,c])=>{const v=d.sc[k];if(!v)return;const w=Math.abs(v)/T*100;
   if(v>0){h+='<i class="dvbar" style="left:'+pos+'%;width:'+w+'%;background:'+c+'"></i>';pos+=w;}
   else{neg-=w;h+='<i class="dvbar" style="left:'+neg+'%;width:'+w+'%;background:var(--bad)"></i>';}});
  return '<div class="crow"><div class="cnm" data-sym="'+d.sym+'">'+d.sym+'</div><div class="dvtrack">'+h+'<i class="dvzero" style="left:'+z+'%"></i></div><div class="cval">'+d.survScore.toFixed(0)+'</div></div>';}).join('');
 document.getElementById('scLeg').innerHTML=SC.map(([,l,c])=>'<span><i class="key" style="background:'+c+'"></i>'+l+'</span>').join('');
}
function drawNet(){
 const mx=Math.max(...DOS.map(d=>Math.abs(d.netCashPctMcap))),z=50;
 document.getElementById('cNet').innerHTML=DOS.map(d=>{
  const v=d.netCashPctMcap,w=Math.abs(v)/(mx*2)*100;
  return '<div class="crow"><div class="cnm" data-sym="'+d.sym+'">'+d.sym+'</div><div class="dvtrack">'+
   (v>=0?'<i class="dvbar" style="left:'+z+'%;width:'+w+'%;background:var(--r400)"></i>':'<i class="dvbar" style="left:'+(z-w)+'%;width:'+w+'%;background:var(--bad)"></i>')+
   '<i class="dvzero" style="left:'+z+'%"></i></div><div class="cval">'+v.toFixed(0)+'%</div></div>';}).join('');
 const cm=Math.max(...DOS.map(d=>d.cashM));
 document.getElementById('cBurn').innerHTML=DOS.map(d=>{
  const w=d.cashM/cm*100,q=d.quarterlyBurnM?d.quarterlyBurnM/d.cashM*w:0;let tk='';
  if(q>1.3)for(let i=1;i*q<w;i++)tk+='<i style="position:absolute;left:'+(i*q)+'%;top:2px;bottom:2px;width:1px;background:var(--s1);opacity:.75"></i>';
  return '<div class="crow"><div class="cnm" data-sym="'+d.sym+'">'+d.sym+'</div><div class="ctrack"><i class="cfill n" style="width:'+w.toFixed(1)+'%"></i>'+tk+'</div>'+
   '<div class="cval">'+money(d.cashM)+'</div></div>';}).join('');
}
tbl(document.getElementById('tSurv'),[
 {t:'Ticker',l:1,v:d=>d.sym,r:d=>TK(d.sym)},
 {t:'Status',l:1,v:d=>d.survScore,r:d=>'<span class="chip '+bcls(d.bucket)+'">'+d.bucket+'</span>'},
 {t:'Cash',v:d=>d.cashM,r:d=>money(d.cashM)},
 {t:'Debt',v:d=>d.debtM,r:d=>d.debtM?money(d.debtM):'<span class="mut">none</span>'},
 {t:'Net cash',v:d=>d.netCashM,r:d=>'<span class="'+(d.netCashM>0?'pos':'neg')+'">'+money(d.netCashM)+'</span>'},
 {t:'% of cap',v:d=>d.netCashPctMcap,r:d=>d.netCashPctMcap.toFixed(0)+'%'},
 {t:'Burn/qtr',v:d=>d.quarterlyBurnM,r:d=>d.quarterlyBurnM?money(d.quarterlyBurnM):'<span class="pos">cash generative</span>'},
 {t:'Runway',v:d=>d.runwayQtrs==null?99:d.runwayQtrs,r:d=>d.runwayQtrs==null?'<span class="pos">profitable</span>':'<b>'+d.runwayQtrs.toFixed(1)+'</b> qtrs'},
 {t:'Catalyst in',v:d=>d.catalystQtrs,r:d=>d.catalystQtrs.toFixed(1)+' qtrs'},
 {t:'Covered?',v:d=>d.runwayCoversCatalyst?1:0,r:d=>d.runwayCoversCatalyst===false?'<span class="chip b">No</span>':'<span class="chip g">Yes</span>'},
 {t:'Rev TTM',v:d=>d.revenueTTM_M,r:d=>d.revenueTTM_M?money(d.revenueTTM_M):'<span class="mut">none</span>'},
 {t:'Survival',v:d=>d.survScore,r:d=>'<b>'+d.survScore.toFixed(0)+'</b>'}
],()=>DOS,11).paint();
tbl(document.getElementById('tRisk'),[
 {t:'Ticker',l:1,v:d=>d.sym,r:d=>TK(d.sym)},
 {t:'Price',v:d=>d.price,r:d=>'$'+d.price.toFixed(2)},
 {t:'Mkt cap',v:d=>d.mcapB,r:d=>'$'+d.mcapB.toFixed(2)+'B'},
 {t:'Beta',v:d=>bt(d.alias||d.sym),r:d=>{const b=bt(d.alias||d.sym);return b==null?'<span class="mut">n/a</span>':b.toFixed(2)}},
 {t:'Volatility',v:d=>vl(d.alias||d.sym),r:d=>{const v=vl(d.alias||d.sym);return v==null?'<span class="mut">n/a</span>':(v*100).toFixed(0)+'%'}},
 {t:'Max drawdown 2y',v:d=>mdd(d.alias||d.sym),r:d=>{const m=mdd(d.alias||d.sym);return m==null?'<span class="mut">n/a</span>':'<span class="neg">'+(m*100).toFixed(0)+'%</span>'}},
 {t:'52w low',v:d=>lo52(d.alias||d.sym),r:d=>{const x=lo52(d.alias||d.sym);return x==null?'—':'$'+x}},
 {t:'52w high',v:d=>hi52(d.alias||d.sym),r:d=>{const x=hi52(d.alias||d.sym);return x==null?'—':'$'+x}},
 {t:'In range',v:d=>p52(d.alias||d.sym),r:d=>{const p=p52(d.alias||d.sym);return p==null?'<span class="mut">n/a</span>':'<span class="sr"><span class="srb"><i style="left:'+(p*100)+'%"></i></span>'+(p*100).toFixed(0)+'%</span>'}},
 {t:'Short % float',v:d=>d.shortPctFloat,r:d=>d.shortPctFloat==null?'—':'<span class="'+(d.shortPctFloat>20?'neg':'')+'">'+d.shortPctFloat.toFixed(1)+'%</span>'},
 {t:'Q1 avg',v:d=>q1avg(d.alias&&PQ[d.alias]?d.alias:d.sym),r:d=>{const a=q1avg(d.alias&&PQ[d.alias]?d.alias:d.sym);return a?'$'+a.toFixed(2):'—'}},
 {t:'vs Q1 avg',v:d=>vsQ1(d.alias&&PQ[d.alias]?d.alias:d.sym),r:d=>sgE(vsQ1(d.alias&&PQ[d.alias]?d.alias:d.sym))},
 {t:'Target',v:d=>d.analystTarget,r:d=>d.analystTarget==null?'—':'$'+d.analystTarget.toFixed(2)+' <span class="mut">('+(d.analystCount||'?')+')</span>'},
 {t:'Implied',v:d=>d.analystTarget/d.price-1,r:d=>sg(d.analystTarget/d.price-1)}
],()=>DOS,4).paint();
function drawScatter(){
 const pts=DOS.filter(d=>bt(d.alias||d.sym)!=null).map(d=>({...d,b:bt(d.alias||d.sym),v:vl(d.alias||d.sym)}));
 const W=940,H=390,P={t:16,r:26,b:44,l:56};
 const x1=Math.ceil(Math.max(...pts.map(p=>p.b))*1.12*10)/10,y1=Math.ceil(Math.max(...pts.map(p=>p.v))*1.12*10)/10;
 const X=v=>P.l+v/x1*(W-P.l-P.r),Y=v=>H-P.b-v/y1*(H-P.t-P.b),rr=m=>Math.max(6,Math.min(26,Math.sqrt(m)*9));
 let g='';
 for(let i=0;i<=4;i++){const v=y1*i/4;g+='<line x1="'+P.l+'" y1="'+Y(v)+'" x2="'+(W-P.r)+'" y2="'+Y(v)+'" stroke="var(--line)"/><text x="'+(P.l-9)+'" y="'+(Y(v)+4)+'" text-anchor="end" font-size="10.5" fill="var(--t3)">'+(v*100).toFixed(0)+'%</text>';}
 for(let i=0;i<=4;i++){const v=x1*i/4;g+='<text x="'+X(v)+'" y="'+(H-P.b+18)+'" text-anchor="middle" font-size="10.5" fill="var(--t3)">'+v.toFixed(1)+'</text>';}
 g+='<line x1="'+X(1)+'" y1="'+P.t+'" x2="'+X(1)+'" y2="'+(H-P.b)+'" stroke="var(--t3)" stroke-dasharray="3 3" opacity=".6"/><text x="'+(X(1)+5)+'" y="'+(P.t+11)+'" font-size="10" fill="var(--t3)">beta 1.0 = moves with the market</text>';
 pts.forEach(p=>{const c=p.bucket==='Funded'?'var(--good)':p.bucket==='Tight'?'var(--warn)':'var(--bad)';
  g+='<circle cx="'+X(p.b)+'" cy="'+Y(p.v)+'" r="'+rr(p.mcapB)+'" fill="'+c+'" opacity=".22"/><circle cx="'+X(p.b)+'" cy="'+Y(p.v)+'" r="4.5" fill="'+c+'" stroke="var(--s1)" stroke-width="2"><title>'+p.sym+' — beta '+p.b.toFixed(2)+', vol '+(p.v*100).toFixed(0)+'%</title></circle>'+
  '<text x="'+(X(p.b)+rr(p.mcapB)+6)+'" y="'+(Y(p.v)+4)+'" font-size="11" font-weight="600" fill="var(--t1)">'+p.sym+'</text>';});
 g+='<text x="'+(P.l+(W-P.l-P.r)/2)+'" y="'+(H-6)+'" text-anchor="middle" font-size="11" fill="var(--t3)">Beta vs S&amp;P 500 (2y weekly)</text>';
 g+='<text transform="translate(15,'+(P.t+(H-P.t-P.b)/2)+') rotate(-90)" text-anchor="middle" font-size="11" fill="var(--t3)">Annualised volatility</text>';
 document.getElementById('scatter').innerHTML='<svg viewBox="0 0 '+W+' '+H+'" style="width:100%;height:auto">'+g+'</svg>';
}
/* ---------- compare ---------- */
const CMPLIST=(()=>{const inD=DOS.map(d=>({sym:d.sym,name:d.name,dos:1}));
 const rest=SCR.filter(x=>!dosBy[x.sym]).map(x=>({sym:x.sym==='GLTO'?'DMRA':x.sym,name:x.name,dos:0}));
 rest.sort((a,b)=>a.sym.localeCompare(b.sym));return {inD,rest};})();
function fillSel(el,def){
 el.innerHTML='<optgroup label="Full dossier">'+CMPLIST.inD.map(x=>'<option value="'+x.sym+'">'+esc(x.sym)+' — '+esc(x.name)+'</option>').join('')+'</optgroup>'+
  '<optgroup label="Screen only — no dossier yet">'+CMPLIST.rest.map(x=>'<option value="'+x.sym+'">'+esc(x.sym)+' — '+esc(x.name)+'</option>').join('')+'</optgroup>';
 el.value=def;}
fillSel(document.getElementById('cmpA'),DOS[0].sym);
fillSel(document.getElementById('cmpB'),DOS[1].sym);
document.getElementById('cmpA').onchange=drawCmp;document.getElementById('cmpB').onchange=drawCmp;
document.getElementById('cmpSwap').onclick=()=>{const a=document.getElementById('cmpA'),b=document.getElementById('cmpB');
 const t=a.value;a.value=b.value;b.value=t;drawCmp();};
function coDat(sym){const d=dosBy[sym]||DOS.find(x=>x.alias===sym);
 const sc=scrBy[sym]||(d&&d.alias?scrBy[d.alias]:null);
 const ls=(PQ[sym]?sym:(d&&d.alias&&PQ[d.alias]?d.alias:sym));
 return {sym,d,sc,ls};}
function drawCmp(){
 const A=coDat(document.getElementById('cmpA').value),B=coDat(document.getElementById('cmpB').value);
 const nm=x=>x.d?x.d.name:(x.sc?x.sc.name:x.sym);
 if(A.sym===B.sym){document.getElementById('cmpHead').innerHTML='<div class="axisnote">Same company selected on both sides — pick two different names.</div>';
  document.getElementById('cmpBody').innerHTML='';return;}
 document.getElementById('cmpHead').innerHTML='<div class="ch2">'+
  [A,B].map((x,i)=>'<div class="chcard'+(i?'':'')+'"><div class="nm" data-sym="'+x.sym+'" style="cursor:pointer">'+esc(nm(x))+' <span class="mut" style="font-size:12.5px">'+x.sym+'</span></div>'+
   '<div class="mt">'+(x.d?esc(x.d.sector)+' · '+esc(x.d.stage)+' · $'+x.d.mcapB.toFixed(2)+'B':(x.sc?'$'+x.sc.mcapB.toFixed(2)+'B · screen only':'—'))+'</div>'+
   (x.d?'<div style="margin-top:9px;display:flex;gap:9px;align-items:center"><span class="chip '+bcls(x.d.bucket)+'">'+x.d.bucket+'</span>'+
   '<span class="mut" style="font-size:11.5px">survival '+x.d.survScore.toFixed(0)+'</span></div>':'<div style="margin-top:9px"><span class="chip">no dossier</span></div>')+
   '<div style="margin-top:10px">'+priceChart(x.ls,{h:172})+'</div></div>').join('<div class="chvs">VS</div>')+'</div>';
 let wa=0,wb=0;
 const rows=[];
 const G=t=>rows.push({g:t});
 const N_=(lab,va,vb,dir,fmt,tip,guard)=>{
  const f=fmt||(v=>v==null?'<span class="mut">—</span>':v);
  let cw='';
  const ok=guard?guard(va,vb):true;
  if(dir&&ok&&va!=null&&vb!=null&&va!==vb){const aWin=dir>0?va>vb:va<vb;cw=aWin?'a':'b';aWin?wa++:wb++;}
  rows.push({lab,a:f(va),b:f(vb),cw,tip});};
 /* a fall steeper than 40% is a collapse, not a discount — never score it as a better entry */
 const entryGuard=(x,y)=>x!=null&&y!=null&&x>-0.40&&y>-0.40;
 const M=v=>v==null?'<span class="mut">—</span>':money(v);
 const P$=v=>v==null?'<span class="mut">—</span>':'$'+(+v).toFixed(2);
 const PC=(v,d=0)=>v==null?'<span class="mut">—</span>':(v*100).toFixed(d)+'%';
 const SGE=v=>sgE(v), SG=v=>sg(v);
 const dA=A.d,dB=B.d;
 G('Survival and balance sheet');
 N_('Status',dA&&dA.bucket,dB&&dB.bucket,0,v=>v?'<span class="chip '+bcls(v)+'">'+v+'</span>':'<span class="mut">—</span>');
 N_('Runway (quarters)',dA?(dA.runwayQtrs==null?99:dA.runwayQtrs):null,dB?(dB.runwayQtrs==null?99:dB.runwayQtrs):null,1,
    v=>v==null?'<span class="mut">—</span>':(v===99?'<span class="pos">profitable</span>':v.toFixed(1)));
 N_('Next catalyst in (quarters)',dA&&dA.catalystQtrs,dB&&dB.catalystQtrs,0,v=>v==null?'<span class="mut">—</span>':v.toFixed(1));
 N_('Runway covers catalyst',dA?(dA.runwayCoversCatalyst?1:0):null,dB?(dB.runwayCoversCatalyst?1:0):null,1,
    v=>v==null?'<span class="mut">—</span>':(v?'<span class="chip g">Yes</span>':'<span class="chip b">No</span>'));
 N_('Cash',dA&&dA.cashM,dB&&dB.cashM,1,M);
 N_('Debt',dA&&dA.debtM,dB&&dB.debtM,-1,v=>v==null?'<span class="mut">—</span>':(v?money(v):'<span class="pos">none</span>'));
 N_('Net cash',dA&&dA.netCashM,dB&&dB.netCashM,1,M);
 N_('Net cash as % of market cap',dA&&dA.netCashPctMcap,dB&&dB.netCashPctMcap,1,v=>v==null?'<span class="mut">—</span>':v.toFixed(0)+'%');
 N_('Burn per quarter',dA&&dA.quarterlyBurnM,dB&&dB.quarterlyBurnM,0,v=>v==null?'<span class="pos">cash generative</span>':money(v),'Not scored on its own — burn only means something against cash, which the runway row already captures');
 N_('Survival score',dA&&dA.survScore,dB&&dB.survScore,1,v=>v==null?'<span class="mut">—</span>':'<b>'+v.toFixed(0)+'</b>');
 G('What they bought at, versus now');
 N_('Q1 range they bought in',q1lo(A.ls)&&('$'+q1lo(A.ls)+' – $'+q1hi(A.ls)),q1lo(B.ls)&&('$'+q1lo(B.ls)+' – $'+q1hi(B.ls)),0);
 N_('Their Q1 average',q1avg(A.ls),q1avg(B.ls),0,P$);
 N_('Marked at 31 March',mk31(A.ls),mk31(B.ls),0,P$);
 N_('Price now',px(A.ls),px(B.ls),0,P$);
 N_('Versus their Q1 average',vsQ1(A.ls),vsQ1(B.ls),-1,SGE,'Lower is better — you are buying closer to their cost. Not scored where either has fallen more than 40%, because that is a collapse rather than a discount.',entryGuard);
 N_('Versus the 31 March mark',A.sc&&A.sc.entry,B.sc&&B.sc.entry,0,SGE,'Shown for reference, not scored — the 31 March mark is just the quarter-end close and often sits at a range extreme, so a big discount to it can be an illusion. The Q1-average row above is the honest entry comparison.');
 G('Business and valuation');
 N_('Market cap',dA?dA.mcapB*1000:(A.sc&&A.sc.mcapB*1000),dB?dB.mcapB*1000:(B.sc&&B.sc.mcapB*1000),0,M);
 N_('Enterprise value',dA&&dA.evM,dB&&dB.evM,0,M);
 N_('Revenue TTM',dA&&dA.revenueTTM_M,dB&&dB.revenueTTM_M,1,v=>v==null?'<span class="mut">—</span>':(v?money(v):'<span class="mut">none</span>'));
 N_('Net income TTM',dA&&dA.netIncomeTTM_M,dB&&dB.netIncomeTTM_M,1,M);
 N_('Operating cash flow TTM',dA&&dA.opCashFlowTTM_M,dB&&dB.opCashFlowTTM_M,1,M);
 N_('Shares outstanding',dA&&dA.sharesOutM,dB&&dB.sharesOutM,0,v=>v==null?'<span class="mut">—</span>':v.toFixed(1)+'M');
 G('Risk and market');
 N_('Beta vs S&P 500',bt(A.ls),bt(B.ls),0,v=>v==null?'<span class="mut">n/a</span>':v.toFixed(2));
 N_('Annualised volatility',vl(A.ls),vl(B.ls),-1,v=>v==null?'<span class="mut">n/a</span>':(v*100).toFixed(0)+'%');
 N_('Worst 2-year drawdown',mdd(A.ls),mdd(B.ls),1,v=>v==null?'<span class="mut">n/a</span>':'<span class="neg">'+(v*100).toFixed(0)+'%</span>');
 N_('Position in 52-week range',p52(A.ls),p52(B.ls),0,v=>v==null?'<span class="mut">n/a</span>':(v*100).toFixed(0)+'%');
 N_('Short interest % of float',dA&&dA.shortPctFloat,dB&&dB.shortPctFloat,-1,v=>v==null?'<span class="mut">—</span>':v.toFixed(1)+'%');
 N_('Analyst target',dA&&dA.analystTarget,dB&&dB.analystTarget,0,P$);
 N_('Implied upside to target',dA&&dA.analystTarget?dA.analystTarget/dA.price-1:null,dB&&dB.analystTarget?dB.analystTarget/dB.price-1:null,1,SG);
 N_('Return since 31 March',sq(A.ls),sq(B.ls),1,SG);
 G('Fund conviction');
 N_('Funds with fresh money',A.sc&&A.sc.nf,B.sc&&B.sc.nf,1,v=>v==null?'<span class="mut">—</span>':v);
 N_('Combined position value',A.sc&&A.sc.totValM,B.sc&&B.sc.totValM,1,v=>v==null?'<span class="mut">—</span>':'$'+v+'M');
 N_('Share of company owned',A.sc&&A.sc.ownPct,B.sc&&B.sc.ownPct,1,v=>v==null?'<span class="mut">—</span>':'<b>'+v+'%</b>');
 N_('Largest position as % of that fund',A.sc&&A.sc.maxBookPct,B.sc&&B.sc.maxBookPct,1,v=>v==null?'<span class="mut">—</span>':v+'%');
 N_('Who bought',A.sc&&A.sc.funds,B.sc&&B.sc.funds,0,v=>v?v.map(f=>'<span class="chip '+(f[1]==='NEW'?'n':'')+'">'+esc(f[0].split(' ')[0])+' '+f[1]+'</span>').join(' '):'<span class="mut">—</span>');
 let h='<div class="card cmpwrap" style="padding:0;overflow:hidden"><div style="overflow:auto;max-height:none"><table class="crt">'+
  '<thead><tr><th class="hva">'+esc(A.sym)+'</th><th></th><th class="hvb">'+esc(B.sym)+'</th></tr></thead><tbody>'+
  rows.map(r=>r.g?'<tr class="grp"><td colspan="3">'+r.g+'</td></tr>':
   '<tr><td class="va">'+(r.cw==='a'?'<span class="wpill">'+r.a+'</span>':r.a)+'</td>'+
   '<td class="lb"'+(r.tip?' title="'+esc(r.tip)+'"':'')+'>'+r.lab+'</td>'+
   '<td class="vb">'+(r.cw==='b'?'<span class="wpill">'+r.b+'</span>':r.b)+'</td></tr>').join('')+
  '</tbody></table></div></div>';
 const sect=(t,fa,fb)=>{if(!fa&&!fb)return '';
  return '<div class="card"><h2>'+t+'</h2><div class="nar" style="margin-top:11px">'+
   '<div><div class="sub" style="font-weight:600;color:var(--t2);margin-bottom:5px">'+esc(A.sym)+'</div>'+(fa||'<span class="mut">—</span>')+'</div>'+
   '<div><div class="sub" style="font-weight:600;color:var(--t2);margin-bottom:5px">'+esc(B.sym)+'</div>'+(fb||'<span class="mut">—</span>')+'</div></div></div>';};
 const prose=d=>d?'<div class="prose">'+esc(d.what)+'<div style="margin-top:7px"><b style="color:var(--t1)">Lead asset:</b> '+esc(d.leadAsset)+'</div></div>':null;
 const surv=d=>d?'<div class="surv"><div style="display:flex;gap:16px;flex-wrap:wrap"><div><div style="font-size:10px;color:var(--t3);text-transform:uppercase">Runway</div><div class="big">'+(d.runwayQtrs==null?'profitable':d.runwayQtrs.toFixed(1)+'q')+'</div></div>'+
   '<div><div style="font-size:10px;color:var(--t3);text-transform:uppercase">Catalyst</div><div class="big">'+d.catalystQtrs.toFixed(1)+'q</div></div></div>'+
   '<div class="deriv">'+esc(d.runwayNote)+'</div></div>':null;
 const lq=d=>d?'<div class="prose"><b style="color:var(--t1)">'+esc(d.latestReport.period)+'</b><br>'+esc(d.latestReport.highlights)+'</div>':null;
 const nc=d=>d?'<div class="prose"><b style="color:var(--t1)">'+esc(d.nextCatalyst.when||'timing unclear')+'</b><br>'+esc(d.nextCatalyst.what)+'</div>':null;
 const bl=d=>d?'<div class="bull"><ul class="bb">'+d.bull.map(x=>'<li>'+esc(x)+'</li>').join('')+'</ul></div>':null;
 const br=d=>d?'<div class="bear"><ul class="bb">'+d.bear.map(x=>'<li>'+esc(x)+'</li>').join('')+'</ul></div>':null;
 const fl=d=>d&&d.flags&&d.flags.length?'<div class="flags'+(d.bucket==='Distressed'?' crit':'')+'"><ul>'+d.flags.map(x=>'<li>'+esc(x)+'</li>').join('')+'</ul></div>':null;
 h+=sect('What each company is',prose(dA),prose(dB));
 h+=sect('How the runway was derived',surv(dA),surv(dB));
 h+=sect('Most recent reported quarter',lq(dA),lq(dB));
 h+=sect('Next catalyst',nc(dA),nc(dB));
 h+=sect('The case for',bl(dA),bl(dB));
 h+=sect('The case against',br(dA),br(dB));
 h+=sect('Material warnings from the filings',fl(dA),fl(dB));
 if(!dA||!dB)h+='<div class="card"><div class="axisnote">'+(!dA?A.sym:B.sym)+' has screen data only — full dossiers currently cover the top ten. Rows above will fill in once it is researched.</div></div>';
 document.getElementById('cmpBody').innerHTML=h;
 applyLearn(document.getElementById('cmpBody'));
 const dist=[A,B].filter(x=>x.d&&x.d.bucket==='Distressed');
 if(dist.length)document.getElementById('cmpHead').insertAdjacentHTML('beforeend',
  '<div class="flags crit" style="margin-top:12px"><b style="color:var(--t1)">'+dist.map(x=>esc(x.sym)).join(' and ')+
  ' carries an explicit going-concern warning.</b> Treat every favourable-looking row against it with suspicion: a low burn figure and a deep discount to the funds\' cost are both symptoms of the same distress, not advantages. Those rows are deliberately left unscored.</div>');
 const tot=wa+wb;
 if(tot)document.getElementById('cmpHead').insertAdjacentHTML('beforeend',
  '<div class="axisnote" style="margin-top:11px">On the '+tot+' directly comparable metrics below, <b style="color:var(--t1)">'+esc(A.sym)+'</b> is better on '+wa+' and <b style="color:var(--t1)">'+esc(B.sym)+'</b> on '+wb+'. This is a tally, not a verdict — the metrics are not equally important, and a single going-concern warning outweighs a dozen favourable ratios.</div>');
}
/* funds */
let fset='smid';
document.getElementById('bSmid').onclick=()=>{fset='smid';setF()};
document.getElementById('bLo').onclick=()=>{fset='longonly';setF()};
function setF(){
 document.getElementById('bSmid').classList.toggle('on',fset==='smid');
 document.getElementById('bLo').classList.toggle('on',fset==='longonly');
 document.getElementById('ovCard').classList.toggle('hide',fset!=='smid');
 document.getElementById('fSetNote').textContent=fset==='smid'?'These eight generate the signal':'Kept for cross-reference — mostly large-cap, not the hunting ground';
 drawFunds();
}
function drawFunds(){
 const set=F.filter(f=>f.set===fset&&!f.dropped);
 document.getElementById('fundCards').innerHTML=set.map(f=>{
  const ev=(f.edgar&&f.edgar.events)||[];
  return '<div class="fcard"><div style="display:flex;justify-content:space-between;align-items:flex-start;gap:12px">'+
  '<div><h3>'+esc(f.name)+(f.newFund?' <span class="chip" style="background:color-mix(in srgb,var(--blue) 16%,transparent);color:var(--blue)">new · '+(f.q2status==='filed'?'Q2 filed':'Q2 pending')+'</span>':'')+'</h3><div class="sub" style="margin-top:2px">'+esc(f.strategy)+' · CIK '+f.cik+(f.ftype?' · <span class="ftag" style="background:color-mix(in srgb,'+(f.ftype==='flow'?'var(--blue)':'var(--good)')+' 16%,transparent);color:'+(f.ftype==='flow'?'var(--blue)':'var(--good)')+'">'+(f.ftype==='flow'?'FLOW':'CONVICTION')+'</span>':'')+'</div></div>'+
  '<div style="text-align:right"><div class="sub">Long book</div><div style="font-size:16px;font-weight:600">'+(f.longK?K(f.longK):'—')+'</div></div></div>'+
  (f.newFund?'<div class="sub" style="margin-top:8px;color:var(--t3)">Added to the roster this quarter'+(f.q2status==='filed'?' — Q2 book shown; counts are Q1→Q2.':' — Q1 book shown; Q2 lands as it files.')+' Full overlap &amp; held-by integration completes at the Q2 fill-in.</div>':'')+
  '<div class="kv" style="margin-top:12px">'+
   [['Positions',N(f.longPositions)],['New buys',f.newBuys==null?'—':f.newBuys],['Added',f.adds==null?'—':f.adds],['Trimmed',f.trims==null?'—':f.trims],['Exited',f.exits==null?'—':f.exits],
    ['Top 10 weight',f.top10==null?'—':pc(f.top10)],['Weighted beta',f.wBeta==null?'—':f.wBeta.toFixed(2)],
    ['Book since 31 Mar',f.wSinceQ==null?'—':sg(f.wSinceQ)]]
   .map(k=>'<div><div class="k">'+k[0]+'</div><div class="v">'+k[1]+'</div></div>').join('')+'</div>'+
  (f.ww?'<div class="sub" style="margin-top:10px">WhaleWisdom: turnover '+f.ww.turnoverPct+'%, average holding period '+(f.ww.heldAllQ/4).toFixed(1)+' years'+(f.ww.advAum?', Form ADV AUM '+money(f.ww.advAum/1e6):'')+'</div>':'')+
  (f.topPos&&f.topPos.length?'<div class="sec" style="margin-top:13px;margin-bottom:0"><h4>Largest positions</h4>'+
   f.topPos.slice(0,8).map(p=>'<div class="crow" style="grid-template-columns:66px 1fr 74px"><div class="cnm" data-sym="'+esc(p[0])+'" title="'+esc(p[1]||'')+'">'+esc(p[0]|| (p[1]?p[1].replace(/ (INC|CORP|CORPORATION|LTD|PLC|LLC|CO|N V|NV|SA|S A|HLDGS|HOLDINGS)\b.*$/i,'').slice(0,10):'—'))+'</div>'+
   '<div class="ctrack"><i class="cfill n" style="width:'+((p[3]||0)/(f.topPos[0][3]||1)*100).toFixed(1)+'%"></i></div><div class="cval">'+(p[3]!=null?pc(p[3]):'')+'</div></div>').join('')+'</div>':'')+
  (ev.length?'<div class="sec" style="margin-top:13px;margin-bottom:0"><h4>Recent SEC disclosures</h4><div class="prose" style="font-size:12px">'+
   ev.slice(0,5).map(e=>'<div style="margin-bottom:3px"><span class="chip '+(/13D/.test(e.form)?'b':/13G/.test(e.form)?'p':'')+'">'+esc(e.form)+'</span> '+esc(e.filed)+' · '+esc(e.issuer||'—')+'</div>').join('')+'</div></div>':'')+
  '<div style="margin-top:12px"><a class="btn" style="text-decoration:none;display:inline-block" target="_blank" href="https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK='+f.cik+'&type=13F&dateb=&owner=include&count=20">EDGAR filings</a></div>'+
  '</div>';}).join('');
 if(fset==='smid')drawMx();
}
function drawMx(){
 const OV=SMID.filter(f=>!f.newFund);   /* overlap matrix covers only the fully-integrated funds */
 const ov=document.getElementById('ovNote');if(ov)ov.textContent=(D.overlapNote||'')+' RTW and Cormorant join the overlap grid at the Q2 fill-in.';
 const O=D.overlap,n=Math.min(OV.length,O.length),off=[];
 for(let i=0;i<n;i++)for(let j=0;j<n;j++)if(i!==j)off.push(O[i][j]);
 const mx=Math.max(...off),RAMP=['var(--r100)','var(--r250)','var(--r400)','var(--r550)','var(--r650)'];
 const st=v=>Math.min(4,Math.floor(v/mx*5));
 const sh=s=>s.replace(/ (Capital|Advisors|Partners)$/,'');
 let h='<thead><tr><th class="rh"></th>'+OV.slice(0,n).map(f=>'<th class="ch"><span>'+esc(sh(f.name))+'</span></th>').join('')+'</tr></thead><tbody>';
 for(let i=0;i<n;i++){h+='<tr><th class="rh">'+esc(sh(OV[i].name))+'</th>';
  for(let j=0;j<n;j++){h+= i===j?'<td class="cl" style="background:var(--s2);color:var(--t3)">—</td>':
   '<td class="cl" title="'+esc(OV[i].name)+' ↔ '+esc(OV[j].name)+'" style="background:'+RAMP[st(O[i][j])]+';color:'+(st(O[i][j])>=3?'#fff':'var(--t1)')+'">'+(O[i][j]*100).toFixed(0)+'%</td>';}
  h+='</tr>';}
 document.getElementById('mx').innerHTML=h+'</tbody>';
 document.getElementById('mxLeg').innerHTML='<span>Overlap</span>'+RAMP.map((c,k)=>'<span><i class="key" style="background:'+c+'"></i>'+(k*mx/5*100).toFixed(0)+'–'+((k+1)*mx/5*100).toFixed(0)+'%</span>').join('');
}
/* holdings */
document.getElementById('hF').innerHTML+=F.filter(f=>!f.dropped).map(f=>'<option value="'+f.id+'">'+esc(f.name)+'</option>').join('');
let holdTbl=null;
function holdT(){
 if(!holdTbl){holdTbl=tbl(document.getElementById('tHold'),[
  {t:'Manager',l:1,v:r=>F[r[0]].name,r:r=>'<span class="mut">'+esc(F[r[0]].name)+'</span>'},
  {t:'Ticker',l:1,v:r=>S[r[1]][0]||'zzz',r:r=>TK(S[r[1]][0])},
  {t:'Issuer',l:1,v:r=>S[r[1]][1],r:r=>'<span class="iss" title="'+esc(S[r[1]][1])+'">'+esc(S[r[1]][1])+'</span>'},
  {t:'Type',l:1,v:r=>r[4],r:r=>'<span class="chip">'+['SHARES','CALL','PUT','NOTES'][r[4]]+'</span>'},
  {t:'Change',l:1,v:r=>({NEW:4,ADD:3,HOLD:2,TRIM:1}[r[5]]||0),r:r=>r[5]?'<span class="chip '+(r[5]==='NEW'?'n':r[5]==='ADD'?'g':r[5]==='TRIM'?'w':'')+'">'+r[5]+'</span>':'—'},
  {t:'Value',v:r=>r[2],r:r=>K(r[2])},
  {t:'% of book',v:r=>r[7],r:r=>r[7]?pc(r[7],2):'—'},
  {t:'Shares',v:r=>r[3],r:r=>N(r[3])},
  {t:'Prev shares',v:r=>r[6],r:r=>r[6]?N(r[6]):'—'},
  {t:'Marked at',v:rowMark,r:r=>{const m=rowMark(r);return m?'$'+m.toFixed(2):'—'},tip:'This position\'s reported value divided by its shares — the price it was carried at on 31 March'},
  {t:'Price now',v:r=>px(S[r[1]][0]),r:r=>{const p=px(S[r[1]][0]);return p?'$'+p.toFixed(2):'<span class="mut">—</span>'}},
  {t:'vs mark',v:rowVs,r:r=>sgE(rowVs(r)),tip:'Today versus the 31 March carrying price. Green = still buyable below it.'},
  {t:'Price · 2Y',l:1,v:r=>vsQ1(S[r[1]][0]),r:r=>sparkChart(S[r[1]][0],104,30)},
  {t:'Beta',v:r=>bt(S[r[1]][0]),r:r=>{const b=bt(S[r[1]][0]);return b==null?'<span class="mut">—</span>':b.toFixed(2)}},
  {t:'Since 31 Mar',v:r=>sq(S[r[1]][0]),r:r=>sg(sq(S[r[1]][0]))},
  {t:'Held by',v:r=>nh(S[r[1]][0]),r:r=>{const n=nh(S[r[1]][0]);return n?n+' / '+SMID.length:'<span class="mut">—</span>'}},
  {t:'CUSIP',l:1,v:r=>S[r[1]][3],r:r=>'<span class="mut">'+esc(S[r[1]][3])+'</span>'}
 ],()=>{
  const fid=+document.getElementById('hF').value,st=document.getElementById('hS').value,
   ty=document.getElementById('hT').value,q=document.getElementById('hQ').value.trim().toUpperCase();
  return R.filter(r=>(fid<0||r[0]===fid)&&(ty==='-1'||r[4]===+ty)&&(!st||r[5]===st)&&
   (!q||(S[r[1]][0]||'').includes(q)||S[r[1]][1].toUpperCase().includes(q)||S[r[1]][3].includes(q)));
 },5,'hCnt');
 ['hF','hS','hT'].forEach(i=>document.getElementById(i).onchange=()=>holdTbl.paint());
 document.getElementById('hQ').oninput=()=>holdTbl.paint();}
 holdTbl.paint();
}
document.getElementById('meth').innerHTML=`
<p><b>Universe.</b> Eight managers generate the signal: Adage Capital, RA Capital, Perceptive Advisors, Senvest, Stockbridge, Point72, Millennium and Braidwell. The first five were the original set; Point72 (multi-manager, tech &amp; healthcare), Millennium (multi-strategy, all sectors) and Braidwell (healthcare crossover) were added to widen sector coverage and cross-fund correlation. Four long-only managers — TCI, Select Equity, Fundsmith and Ruane Cunniff — are kept under Funds for cross-reference but are not the hunting ground, since they buy large caps almost exclusively.</p>
<p><b>Screen.</b> Every position opened new between 31 December 2025 and 31 March 2026, matched at CUSIP level. Adage needs $15M+ to qualify (it opened 213 new positions and runs a 953-name book, so most are noise); the specialists need $8M+. Removed: roughly 90 blank-check and SPAC units from Adage's arbitrage book, private holdings with no ticker, and companies acquired since the filing. 123 new positions became 33 candidates.</p>
<p><b>Survival score</b> — the primary ranking. Six components. Runway up to 40 points scaled on quarters of cash, capped at 12; profitable companies score full. Reaching the catalyst is +20, or −40 where cash runs out first. Balance sheet ranges −30 to +20 on net cash as a share of market cap, with an automatic −30 where debt exceeds cash. An explicit going-concern statement is a −70 override. Fund conviction contributes up to 25, carried from the screen. Entry versus their mark adds up to 12 for buying at or below the funds' carrying price and subtracts 6 for chasing something already up more than 40%.</p>
<p><b>Runway is derived per company, not from one formula.</b> This is the most important methodological choice here. Trailing operating cash flow is the default but it is actively misleading for several: Neumora's trailing burn funded three Phase 3 trials terminated in June, Damora's spans a pre-merger shell, Sutro's includes pre-restructuring quarters, OnKure's understates a ramp. Where trailing data misleads, the figure comes from a sequential balance-sheet bridge or company guidance — and the derivation is written out in full in each dossier so you can reject it. Cash is company-reported; several screeners understate Century, ALX Oncology and Aclaris by excluding marketable securities.</p>
<p><b>What they bought at.</b> 13F filings do not disclose cost basis, so two measures are shown side by side and neither should be read as their actual entry. The <b>31 March mark</b> is the position's reported value divided by its shares — simply the quarter-end closing price, which can sit at an extreme of the quarter and therefore mislead: Relmada's mark was its Q1 high, making it look 36% cheaper today than it really is. The <b>Q1 range and average</b> is the stock's actual trading range through the quarter the positions were built, so their true average cost sits somewhere inside that band. Measured against the Q1 average, Relmada is only 6% below rather than 36%, and OnKure is 29% <i>above</i> despite appearing 5% below on the mark. The range is the more honest read; both are shown everywhere a price comparison appears.</p>
<p><b>Price and risk.</b> Beta is the OLS slope of weekly log returns against SPY over two years; volatility is the annualised standard deviation of those returns; maximum drawdown is the worst peak-to-trough fall over the same window. "Their mark" is 13F value divided by shares at 31 March — the carrying price, a proxy for entry, not disclosed cost basis. Tickers renamed since the filing are priced under the successor listing.</p>
<p><b>Sources.</b> SEC Form 13F-HR: Q2 2026 (period 30 June, filed 14 August) for the funds that have filed, otherwise Q1 2026 (31 March, released 15 May; Perceptive restated 29 May) — cross-checked against WhaleWisdom. Company financials re-pulled from Q2 2026 (30 June) results releases and SEC 10-Q/XBRL, refreshed 14 August 2026; market caps and consensus from stockanalysis.com. Clinical and corporate events verified against company press releases and SEC filings. Prices to 13 August 2026 close.</p>
<p><b>Known gaps.</b> Twenty-three of the 33 screened names carry screen data only — full dossiers cover the top ten, scoped deliberately because the Q2 filings reshuffle the list. Damora has no two-year price history under its current ticker. Ownership percentages use current shares outstanding, so they overstate holdings where a company issued stock after 31 March.</p>
<p><b>What changes on 14 August.</b> Q2 2026 13Fs are due. They answer what this cannot: did the specialists hold these positions through Q2, add, or quietly exit? A name surviving two consecutive quarters of specialist ownership, with runway intact and still near their mark, is materially stronger than anything ranked here today. Several of these companies also report Q2 results on 13–14 August, including the first clean look at Neumora's post-restructuring burn and whether Karyopharm cleared its September forbearance cliff.</p>
<p style="color:var(--t3)">Informational only, not investment advice. Most of these are pre-revenue clinical-stage biotechs where a single trial result can move the stock 70% in a day.</p>`;
function drawAud(){
 const A_=D.audit; if(!A_)return;
 document.getElementById('audTiles').innerHTML=[
  ['Internal assertions',A_.internal.passed+' passed · '+A_.internal.failed+' failed',A_.internal.desc],
  ['SEC positions re-tallied',A_.sec.positions+' of '+A_.sec.positions+' match exactly',A_.sec.desc],
  ['Independent corrections',A_.log.length+' applied',A_.external.desc],
  ['Conclusions changed','5',"Aclaris' runway, Neumora's failure count, Damora's competitive position, Sutro's cash and balance sheet, and ALX's burn all moved."]
 ].map(t=>'<div class="tile"><div class="lab">'+t[0]+'</div><div class="val" style="font-size:19px">'+t[1]+'</div><div class="dlt">'+t[2]+'</div></div>').join('');
 document.getElementById('tAudSec').innerHTML='<thead><tr><th class="l">Fund</th><th class="l">Filing pulled from EDGAR</th><th class="l">Rows</th><th class="l">Total value</th><th class="l">Result</th></tr></thead><tbody>'+
  A_.secDetail.map(r=>'<tr><td class="l"><b>'+esc(r[0])+'</b></td><td class="l">'+esc(r[1])+'</td><td class="l">'+esc(r[2])+'</td><td class="l">'+esc(r[3])+'</td><td class="l"><span class="chip g">'+esc(r[4])+'</span></td></tr>').join('')+'</tbody>';
 document.getElementById('audSecNote').innerHTML='Twenty-one individual positions across these funds — every holding in the ten researched companies — were also compared line by line. <b style="color:var(--t1)">All 21 match the SEC filing to the dollar and to the share.</b> One row-count difference exists: RA Capital shows 86 rows at the SEC versus 85 here, because the data feed consolidates two lines carrying the same CUSIP. The dollar totals are identical.';
 const SEV={material:'b',moderate:'w',minor:''};
 document.getElementById('tAudLog').innerHTML='<thead><tr><th class="l">Severity</th><th class="l">Company</th><th class="l">Field</th><th class="l">Was</th><th class="l">Now</th><th class="l">Why</th></tr></thead><tbody>'+
  A_.log.slice().sort((a,b)=>({material:0,moderate:1,minor:2}[a.sev]-{material:0,moderate:1,minor:2}[b.sev]))
   .map(l=>'<tr><td class="l"><span class="chip '+(SEV[l.sev]||'')+'">'+esc(l.sev)+'</span></td><td class="l"><b>'+esc(l.sym)+'</b></td>'+
   '<td class="l"><span class="mut">'+esc(l.field)+'</span></td><td class="l"><span class="mut" style="text-decoration:line-through">'+esc(String(l.old)).slice(0,60)+'</span></td>'+
   '<td class="l"><b>'+esc(String(l.new)).slice(0,70)+'</b></td><td class="l" style="white-space:normal;max-width:420px;font-size:11.5px;color:var(--t2)">'+esc(l.why||'')+'</td></tr>').join('')+'</tbody>';
 document.getElementById('audGaps').innerHTML='<p>Three limits worth stating plainly.</p>'+
  '<p><b>Where the data actually stands, as of 14 August.</b> All ten companies have now filed 30 June (Q2) financials, and every balance-sheet figure here was re-pulled and checked against them. <b style="color:var(--t1)">Neumora</b> confirmed cash of $116.8M and its lead drug navacaprant is discontinued (Phase 3 failed 0-for-3). <b style="color:var(--t1)">Karyopharm</b> is the sharp problem: Q2 cash fell to $65.1M against ~$250M of debt, a going-concern doubt was reaffirmed, and a $15.8M payment due 10 September could trigger default — its survival score stays deeply negative. On the 13F side, 4 of the 10 funds have filed Q2 (see the Q2 Moves tab); the rest fold in as they file 14 August.</p>'+
  '<p><b>Q2 13Fs are landing (14 August).</b> 4 of the 10 signal funds — Adage, Senvest, Stockbridge and RTW — have filed their 30 June books; the Q2 Moves tab shows what they did since Q1. The other six (RA Capital, Perceptive, Point72, Millennium, Braidwell, Cormorant) are deadline filers and file through today; they fold in automatically as they land. Holdings shown are always the most recent filing that exists per fund, never stale.</p>'+
  '<p><b>Runway figures are estimates built on a stated derivation, not facts.</b> Where trailing cash flow misleads, the number comes from a balance-sheet bridge or from company guidance. Each dossier shows exactly which. Reasonable people would land on different numbers — Aclaris moved from 8.4 to 10.4 quarters purely because a post-quarter capital raise was found, and Sutro moved from 6.5 to 4.3 once its actual 30 June balance replaced the March one.</p>'+
  '<p><b>Twenty-three of the 33 screened names have no dossier.</b> They carry screen and price data only, and were not put through this audit. Do not treat their absence of warnings as an absence of problems.</p>'+
  '<p style="color:var(--t3)">Both audit passes ran on 12 August 2026. They do not re-verify themselves — a fresh pass is needed after the Q2 13Fs land on 14 August.</p>';
}
/* ---------- buy-zone shortlist: funded through catalyst + near the funds' cost + 2+ funds ---------- */
/* ---------- Q2 Moves tab ---------- */
let movesDrawn=false;
let movesLens='all';
function drawMoves(){renderMoves();}
function renderMoves(){
 const Q=D.q2move; const el=document.getElementById('movesBody');
 if(!Q){el.innerHTML='<div class="bzempty">No Q2 move data yet.</div>';return;}
 const NM=s=>{const d=dosBy[s]||scrBy[s];return d?(d.name||s):s;};
 const MC={EXIT:'var(--bad)',NEW:'var(--blue)',ADD:'var(--good)',TRIM:'var(--warn)',HOLD:'var(--t3)'};
 const chip=m=>'<span class="mvchip" style="background:color-mix(in srgb,'+MC[m]+' 16%,transparent);color:'+MC[m]+'">'+m+'</span>';
 const N=n=>n==null?'—':n>=1e6?(n/1e6).toFixed(n>=1e7?0:1)+'M':n>=1e3?(n/1e3).toFixed(0)+'k':(''+n);
 const lens=movesLens, okf=ft=>lens==='all'||ft===lens;
 /* lens filter */
 const lb=[['all','All funds'],['flow','Flow · active'],['conviction','Conviction · specialists']].map(x=>
   '<button class="mvlens'+(lens===x[0]?' on':'')+'" data-lens="'+x[0]+'">'+x[1]+'</button>').join('');
 const filt='<div class="mvlensbar">'+lb+'<span class="mvlenshint"><b>Flow</b> = big active books — where the money moves. <b>Conviction</b> = concentrated specialists — the quality picks.</span></div>';
 /* status strip grouped by lens */
 function stripFor(ft,label){const list=Q.fundStatus.filter(f=>f.ftype===ft);if(!list.length)return '';
   return '<div class="mvgrouplab">'+label+'</div><div class="mvstrip">'+list.map(f=>{const col=f.status==='filed'?'var(--good)':'var(--t3)';
     return '<span class="mvfund" title="'+esc(f.type)+(f.positions?' · '+f.positions+' positions':'')+'"><span class="dot" style="background:'+col+'"></span>'+esc(f.short)+
       (f.new?' <span class="fnew">NEW</span>':'')+' <span style="color:'+col+';font-size:10.5px">'+(f.status==='filed'?'Q2':'Q1')+'</span></span>';}).join('')+'</div>';}
 let strip='';
 if(lens!=='conviction') strip+=stripFor('flow','Active / flow funds');
 if(lens!=='flow') strip+=stripFor('conviction','Concentrated specialists');
 const hdr='<div style="font-size:12.5px;color:var(--t2);margin:9px 0 4px"><b style="color:var(--t1)">'+Q.filedCount+' of '+Q.total+' funds</b> have filed their 30 June book. Moves are Q1→Q2; the rest fill in as they file.</div>';
 const nt=Q.notable;
 const ex=nt.exits.filter(e=>okf(e.ftype)), nw=nt.news.filter(e=>okf(e.ftype)), ad=nt.adds.filter(e=>okf(e.ftype));
 const itemsExit=()=>ex.slice().sort((a,b)=>(b.diverge?1:0)-(a.diverge?1:0)).map(e=>
   '<div class="mvitem"><span class="mvtk" data-sym="'+esc(e.sym)+'">'+esc(e.sym)+'</span>'+chip('EXIT')+
   '<span><b>'+esc(e.fund)+'</b> sold out of '+esc(NM(e.sym))+' — held '+N(e.q1)+' sh in Q1.'+
   (e.diverge?' <span class="mvdiv">↔ but another filed fund is buying it — divergence</span>':'')+'</span></div>').join('');
 const itemsNew=()=>nw.map(e=>'<div class="mvitem"><span class="mvtk" data-sym="'+esc(e.sym)+'">'+esc(e.sym)+'</span>'+chip('NEW')+'<span><b>'+esc(e.fund)+'</b> opened a new position in '+esc(NM(e.sym))+' — '+N(e.q2)+' sh.</span></div>').join('');
 const itemsAdd=()=>ad.map(e=>'<div class="mvitem"><span class="mvtk" data-sym="'+esc(e.sym)+'">'+esc(e.sym)+'</span>'+chip('ADD')+'<span><b>'+esc(e.fund)+'</b> added to '+esc(NM(e.sym))+' — '+N(e.q1)+' → '+N(e.q2)+' sh.</span></div>').join('');
 let secs='';
 secs+='<div class="mvsec"><h3>'+chip('EXIT')+'Exits — the loudest signal</h3><div class="msub">A fund walking away from a name it held. Divergences pushed to the top.</div>'+(ex.length?itemsExit():'<div class="bznote">No exits in this lens yet.</div>')+'</div>';
 secs+='<div class="mvsec"><h3>'+chip('NEW')+'New buys</h3><div class="msub">A fresh position opened this quarter.</div>'+(nw.length?itemsNew():'<div class="bznote">No new buys in this lens yet.</div>')+'</div>';
 secs+='<div class="mvsec"><h3>'+chip('ADD')+'Adds — conviction building</h3><div class="msub">A fund increasing a position it already held.</div>'+(ad.length?itemsAdd():'<div class="bznote">No adds in this lens yet.</div>')+'</div>';
 const names=Object.keys(Q.byName).filter(s=>{const o=Q.byName[s];return o.filed.filter(m=>okf(m.ftype)).length||(lens==='all'&&o.pendQ1.length);})
   .sort((a,b)=>{const A=Q.byName[a],B=Q.byName[b];return (B.filed.length-A.filed.length)||(B.cnt.EXIT-A.cnt.EXIT);});
 let grid='<div class="mvsec"><h3>Every tracked name — move by move</h3><div class="msub">What each <b>filed</b> fund did'+(lens==='all'?', plus which pending funds held it in Q1':' in this lens')+'.</div>';
 grid+=names.map(s=>{const o=Q.byName[s];
   const fm=o.filed.filter(m=>okf(m.ftype)).map(m=>'<span title="'+esc(m.short)+': '+m.m+' ('+N(m.q1)+'→'+N(m.q2)+')">'+chip(m.m)+'<span style="font-size:10.5px;color:var(--t2)"> '+esc(m.short)+'</span></span>').join(' ');
   const pend=(lens==='all'&&o.pendQ1.length)?'<span class="mvpend">Q2 pending: '+o.pendQ1.map(esc).join(', ')+'</span>':'';
   return '<div class="mvname"><span class="mvtk" data-sym="'+esc(s)+'">'+esc(s)+'</span>'+(fm||'<span class="mvpend">—</span>')+' '+pend+'</div>';
 }).join('')+'</div>';
 el.innerHTML=filt+strip+hdr+secs+grid;
 el.querySelectorAll('.mvlens').forEach(b=>b.onclick=()=>{movesLens=b.dataset.lens;renderMoves();});
}
function buyZone(){
 const ENTRY_MAX=0.15;   /* within 15% of their average cost, or below */
 const cand=DOS.map(d=>{
   const ls=d.alias&&PQ[d.alias]?d.alias:d.sym, sc=scrBy[d.sym]||(d.alias?scrBy[d.alias]:null);
   const v=vsQ1(ls), nf=sc?sc.nf:0;
   const funded=d.bucket!=='Distressed'&&(d.runwayCoversCatalyst===true||d.runwayQtrs==null||d.bucket==='Funded');
   const nearCost=v!=null&&v<=ENTRY_MAX;
   const clustered=nf>=2;
   return {d,ls,sc,v,nf,funded,nearCost,clustered,pass:funded&&nearCost&&clustered};
 });
 const win=cand.filter(c=>c.pass).sort((a,b)=>b.d.survScore-a.d.survScore);
 const el=document.getElementById('bzList');
 if(!win.length){el.innerHTML='<div class="bzempty">No name currently clears all three gates on this quarter\'s data. The closest are listed below — check them when Q2 lands Friday.</div>';}
 else{
  el.innerHTML=win.map((c,i)=>{const d=c.d,fresh=(c.sc&&c.sc.funds||[]).filter(f=>f[1]==='NEW'||f[1]==='ADD');
   return '<div class="bz" data-sym="'+esc(d.sym)+'"><div class="bzrank">'+(i+1)+'</div>'+
    '<div class="bzmain"><span class="bztk">'+esc(d.sym)+'</span> <span class="bznm">'+esc(d.name)+' · '+esc(d.sectorBucket||'')+'</span>'+
    '<div class="bzgates">'+
     '<span class="bzg">✓ funded <b>'+(d.runwayQtrs==null?'profitable':d.runwayQtrs.toFixed(1)+'q runway')+'</b> · catalyst in '+d.catalystQtrs.toFixed(1)+'q</span>'+
     '<span class="bzg">✓ <b>'+(c.v>0?'+':'')+(c.v*100).toFixed(0)+'%</b> vs their cost</span>'+
     '<span class="bzg">✓ <b>'+c.nf+' funds</b>'+(fresh.length?' · '+fresh.map(f=>f[0].split(' ')[0]+' '+f[1]).slice(0,3).join(', '):'')+'</span>'+
    '</div></div>'+
    '<div class="bzmini"><div class="v" style="color:'+survBand(d.survScore)[1]+'">'+d.survScore.toFixed(0)+'</div><div class="l">'+survBand(d.survScore)[0]+'</div>'+
     '<div style="margin-top:4px">'+survScale(d.survScore,{w:'120px'})+'</div></div>'+
    (d.bzWarn?'<div class="bzwarn">⚠ '+esc(d.bzWarn)+'</div>':'')+'</div>';}).join('');
 }
 /* names that pass entry + conviction but aren't researched for survival yet */
 const watch=SCR.filter(s=>!dosBy[s.sym]&&s.nf>=2&&vsQ1(s.sym)!=null&&vsQ1(s.sym)<=ENTRY_MAX)
   .sort((a,b)=>b.nf-a.nf).slice(0,10);
 const nearMiss=cand.filter(c=>!c.pass&&(c.funded?1:0)+(c.nearCost?1:0)+(c.clustered?1:0)===2)
   .sort((a,b)=>b.d.survScore-a.d.survScore);
 let extra='';
 if(nearMiss.length)extra+='<div class="bznote"><b style="color:var(--t2)">Just missed (clear 2 of 3):</b> '+
   nearMiss.map(c=>'<span class="bzalt" data-sym="'+esc(c.d.sym)+'">'+esc(c.d.sym)+' <span style="color:var(--t3)">'+(c.funded?'':'not funded')+(c.nearCost?'':(c.funded?'':' · ')+'already ran')+(c.clustered?'':' · 1 fund')+'</span></span>').join('')+'</div>';
 if(watch.length)extra+='<div class="bznote"><b style="color:var(--t2)">Cheap and clustered but not yet researched</b> (no survival read — do these next): '+
   watch.map(s=>'<span class="bzalt" data-sym="'+esc(s.sym)+'">'+esc(s.sym)+'</span>').join('')+'</div>';
 el.innerHTML+=extra;
}
/* ---------- multi-quarter trajectory: Q4 -> Q1 shares (grows to 3 bars when Q2 lands) ---------- */
function traj(prev,now,status){
 const a=prev||0,b=now||0,mx=Math.max(a,b,1);
 const col=status==='NEW'?'var(--blue)':b>a*1.03?'var(--good)':b<a*0.97?'var(--warn)':'var(--t3)';
 const bar=(val)=>'<i style="height:'+Math.max(2,val/mx*18).toFixed(0)+'px;background:'+col+'"></i>';
 const lab=status==='NEW'?'opened':status==='EXIT'?'exited':b>a*1.03?'building':b<a*0.97?'trimming':'holding';
 const pct=a>0&&status!=='NEW'?(b/a-1):null;
 return '<span class="traj" title="Q4 '+N(a)+' → Q1 '+N(b)+' shares">'+bar(a)+bar(b)+'</span>'+
   '<span class="trajlab" style="color:'+col+'">'+lab+(pct!=null?' '+(pct>0?'+':'')+(pct*100).toFixed(0)+'%':'')+'</span>';
}
let guideDrawn=false;
function drawGuide(){if(guideDrawn)return;guideDrawn=true;
 const sw=(c)=>'<span class="gsw" style="background:'+c+'"></span>',dot=(c)=>'<span class="gdot" style="background:'+c+'"></span>';
 const item=(mark,t,d)=>'<div class="gitem">'+mark+'<div><div class="gt">'+t+'</div><div class="gd">'+d+'</div></div></div>';
 document.getElementById('gColors').innerHTML=[
  item(sw('var(--good)'),'Green = in your favour','A company with enough cash to reach its next milestone; a stock still trading below what the funds paid; or the stronger of two names in a head-to-head.'),
  item(sw('var(--warn)'),'Amber = tight, not broken','Enough cash to keep going, but not much cushion — or a caution flag worth reading before you act.'),
  item(sw('var(--bad)'),'Red = be careful','A company at real risk of running out of money, or a stock that has already run up past what the funds paid — the move you were following may be over.'),
  item(sw('var(--s3)'),'Grey = neutral or no data','Either a figure we simply don\'t have yet, or a number that is just information — neither good nor bad on its own.'),
  item('<span class="chip g" style="margin-top:1px">Funded</span>','“Funded”, “Tight”, “Distressed”','The three survival buckets. <b>Funded</b> = comfortable cash. <b>Tight</b> = enough but watch it. <b>Distressed</b> = may not make it — treat with real caution whoever bought it.')
 ].join('');
 document.getElementById('gMarks').innerHTML=[
  item('<span class="gsw" style="background:color-mix(in srgb,var(--blue) 14%,transparent)"></span>','Pale blue band','The price range the stock actually traded in during the quarter the funds were buying — so their true average cost sits somewhere <b>inside</b> this band. It\'s the honest picture of “where they got in.”'),
  item('<span class="gdot" style="background:var(--s1);border:2px solid var(--t1)"></span>','Open (hollow) circle','The “31 March mark” — the price on the very last day of the quarter, which is the number the filing reports. It\'s just one day\'s close and can sit at a high or low extreme, so it often <b>misleads</b>. Trust the band and the average, not this dot.'),
  item(dot('var(--good)'),'Green dot / bar = today, below their cost','Today\'s price, when it\'s still under the funds\' average cost. You\'d be buying near where they did.'),
  item(dot('var(--bad)'),'Red dot / bar = today, above their cost','Today\'s price, when it has already risen past their average cost. The gain you were following has partly happened.'),
  item('<span class="gsw" style="background:color-mix(in srgb,var(--good) 15%,transparent);color:var(--good);font-size:9px;text-align:center;line-height:18px">▲</span>','Green ▲ pill (Compare tab)','Marks the stronger of the two companies on that row. Only shown on rows that can actually be “won” — plain rows are just reference.')
 ].join('');
 const G=(title,rows)=>'<div class="ggroup"><h4>'+title+'</h4>'+rows.map(r=>'<div class="gterm"><div class="k">'+r[0]+(r[2]?'<span class="sub2">'+r[2]+'</span>':'')+'</div><div class="d">'+r[1]+'</div></div>').join('')+'</div>';
 document.getElementById('gTabs').innerHTML=[
  ['Overview','The dashboard. Headline numbers, a single chart of where every name trades versus what the funds paid, and what the funds bought and sold last quarter. <b>Look for:</b> the big picture before you dig in.'],
  ['Buy Zone','<b>The payoff.</b> One short, ranked list of the names that clear all three gates at once — funded through their next catalyst, still trading at or near the funds\' average cost, and bought by two or more funds. Below it: names that just missed (and why), and cheap-and-clustered names not yet researched. <b>Look for:</b> your starting shortlist — everything else on the terminal is the detail behind these names.'],
  ['Screen','The full list of every small company a tracked fund bought fresh last quarter — filter by sector (the chips at the top), size, entry price, or how many funds bought. <b>Look for:</b> names with several funds and a green survival chip. This is your hunting ground.'],
  ['Companies','The ten names researched in depth. Click any one for its full dossier: what the business does, the survival math, the case for and against, and its next catalyst. <b>Look for:</b> the story behind a name the screen flagged.'],
  ['Compare','Pick any two companies and see them side by side on every metric. The green ▲ pill marks the stronger one per row. <b>Look for:</b> which of two candidates is better funded, cheaper vs the funds\' cost, or less risky.'],
  ['Survival','<b>The most important tab.</b> Answers one question: can this company reach its next milestone without running out of cash? It plots each name\'s <b>runway</b> (quarters of cash left) against how far away its next <b>catalyst</b> is, breaks the survival score into its parts, and shows the balance sheet and cash-vs-burn. <b>Look for:</b> the runway bar reaching past the catalyst dot. If it doesn\'t, the company likely has to raise money — a red flag no matter who bought it.'],
  ['Risk','How bumpy each stock is. The main chart plots <b>volatility</b> (how wildly it swings, up the side) against <b>beta</b> (how much it moves with the market, along the bottom); each bubble is a company, bubble size = its market value. Below it: worst drawdowns and where each sits in its 52-week range. <b>Look for:</b> what kind of ride you\'re signing up for — top-right bubbles are the wildest.'],
  ['Funds','Who is doing the buying — this is where <b>conviction</b> lives. Each fund gets a card (what they bought and sold, their biggest positions, their style), a toggle to the long-only cross-reference funds, and an <b>overlap grid</b> showing how alike the funds are. <b>Look for:</b> a name bought by several funds whose overlap is <i>low</i> — that means they decided independently, which is a much stronger signal than one fund alone.'],
  ['Holdings','The raw data — every single position across all twelve funds, searchable and sortable by manager, change, or type. <b>Look for:</b> use it when you want to dig into the underlying filings yourself.'],
  ['Guide','This page.'],
  ['Method','How every number was calculated and exactly where the data came from. <b>Look for:</b> the reasoning behind a figure you want to trust or question.'],
  ['Audit','The record of every accuracy check run and every correction made, with the original SEC figures. <b>Look for:</b> proof the numbers were verified, and an honest list of what wasn\'t covered.']
 ].map(r=>'<div class="gterm"><div class="k">'+r[0]+'</div><div class="d">'+r[1]+'</div></div>').join('');
 document.getElementById('gGloss').innerHTML=
  G('Can this company survive? (the most important question here)',[
   ['Runway','How many quarters of cash the company has left before it must raise more money. <b>Higher is safer.</b>','in quarters'],
   ['Burn','How much cash it spends each quarter. Most of these have little or no revenue, so they live off a cash pile.','per quarter'],
   ['Cash','Money in the bank plus short-term investments — the fuel tank.',''],
   ['Net cash','Cash minus debt. What\'s actually theirs after what they owe.',''],
   ['Net cash % of market cap','How much of the company\'s price tag is just the cash it holds. <b>Over 100%</b> means the market is valuing the actual business at less than nothing.',''],
   ['Catalyst','The next big event that could move the stock — a trial result, an FDA decision, an earnings report. “Next catalyst in” is how many quarters away it is.',''],
   ['Runway covers catalyst','<b>YES</b> = it has enough cash to reach that next event without raising money first. This is the single line that matters most.',''],
   ['Survival score','Our 0–120 score combining cash, runway, debt and catalyst timing. Treat it as a <b>disqualifier, not a ranking</b> — it tells you who is likely still standing, not who will win biggest. Above ~50 the exact order isn\'t meaningful.',''],
   ['Going concern','An official warning in the company\'s own filings that it may not survive the year. The worst red flag on this whole terminal.','']
  ])+
  G('Where did the funds buy, and where is it now?',[
   ['13F','The report big investment funds must file every quarter listing what they own. Every buy signal here comes from these.',''],
   ['The 45-day lag','Funds report about six weeks after each quarter ends, so we\'re always looking at a slightly old snapshot. Known trade-off.',''],
   ['Signal funds','The eight hedge funds we track for buy signals: Adage, RA Capital, Perceptive, Senvest, Stockbridge, Point72, Millennium, Braidwell.',''],
   ['NEW / ADD / TRIM / EXIT','What a fund did last quarter: opened a brand-new position (<b>NEW</b>), bought more (<b>ADD</b>), sold some (<b>TRIM</b>), or sold all of it (<b>EXIT</b>). NEW is the strongest “they like this now.”',''],
   ['Fresh money','The funds that opened or added to a name last quarter — the buyers you\'re actually following.',''],
   ['Their Q1 average','Roughly the price the funds paid, averaged across the quarter they were buying.',''],
   ['vs their Q1 average','Where the stock trades now versus what they paid. <b>Below (green)</b> = you can still buy near their cost; <b>above (red)</b> = it already moved.',''],
   ['Combined value','Total dollars all the tracked funds hold in this one name.',''],
   ['Funds own %','What slice of the entire company these funds hold together.',''],
   ['Overlap','How alike two funds\' portfolios are. <b>Low overlap is good</b> — it means they decided independently, so a name they both bought carries more weight.',''],
   ['Conviction','How much the funds are really betting on a name — measured by how many funds bought it, how much money they put in, and how big a slice of their own portfolio it is. More independent funds + more money = higher conviction. Lives on the Funds tab and in each company\'s record.',''],
   ['Trajectory','In each company\'s record: whether a fund has been <b>building</b>, <b>trimming</b>, <b>holding</b> or just <b>opened</b> a position, shown as small bars quarter over quarter. A fund quietly trimming after building is a warning; adding is a vote of confidence.',''],
   ['Buy zone','The shortlist at the top of the Overview: the handful of names that clear all three gates at once — funded through their next catalyst, still near what the funds paid, and bought by two or more funds. The terminal\'s single “start here” list.','']
  ])+
  G('How risky is the stock?',[
   ['Beta','How much the stock moves when the whole market moves. 1 = moves with the market; 2 = twice as jumpy.',''],
   ['Volatility','How wildly the price swings. Higher = a bumpier ride.',''],
   ['Worst 2-year drawdown','The biggest fall from a peak the stock has had in two years — shows how bad it can get.',''],
   ['52-week range','Its low and high over the past year, and where today sits between them.',''],
   ['Short interest','The share of stock traders have bet against. High = many people expect it to fall.','']
  ])+
  G('What is it worth?',[
   ['Market cap','The total price tag of the whole company (share price × number of shares).',''],
   ['Enterprise value','Market cap minus net cash — what you\'re really paying for the business itself. Can be <b>negative</b> when cash exceeds the price.',''],
   ['Revenue','Sales. Most of these early-stage names have little or none yet.',''],
   ['Analyst target','The average price Wall Street analysts expect. A guide, not a promise.',''],
   ['Implied upside','How far today\'s price sits below that target, as a percentage.','']
  ]);
 document.getElementById('gHow').innerHTML=
  '<p><b>1.</b> Start on the <b>Screen</b>. Every row is a small company that a specialist fund just bought.</p>'+
  '<p><b>2.</b> Scan the <b>Fresh money</b> chips — the more funds, especially <b>NEW</b>, the stronger the interest. Use the sector tabs at the top to focus.</p>'+
  '<p><b>3.</b> Check the <b>survival colour</b>: green (Funded) can reach its next catalyst; red (Distressed) might not — skip those no matter who bought.</p>'+
  '<p><b>4.</b> Look at the <b>price dot versus the blue band</b>: green/below their cost = you\'re not chasing; red/above = the move already happened.</p>'+
  '<p><b>5.</b> Click any name for the full story, or use <b>Compare</b> to put two side by side.</p>'+
  '<p style="color:var(--t3)">Remember: a green survival score means “still alive,” not “sure thing.” This terminal is a research shortcut for narrowing the field — not investment advice. These are early-stage companies where a single trial result can move the price 70% in a day.</p>';
}
function drawScaleDemo(){const el=document.getElementById('scaleDemo');if(!el)return;
 const MIN=-110,MAX=120,R=MAX-MIN,W=1000,L=14,Rp=14,pw=W-L-Rp,barY=92,barH=11,H=124;
 const X=v=>L+(Math.max(MIN,Math.min(MAX,v))-MIN)/R*pw;
 let g='';
 const zone=(a,b,c)=>'<rect x="'+X(a).toFixed(1)+'" y="'+barY+'" width="'+(X(b)-X(a)).toFixed(1)+'" height="'+barH+'" rx="0" fill="'+c+'" opacity="0.85"/>';
 g+=zone(MIN,0,'var(--bad)')+zone(0,60,'var(--warn)')+zone(60,MAX,'var(--good)');
 [[-110,'−110'],[0,'0'],[60,'60'],[120,'120']].forEach(t=>{const x=X(t[0]).toFixed(1);
  g+='<line x1="'+x+'" y1="'+barY+'" x2="'+x+'" y2="'+(barY+barH+4)+'" stroke="var(--t3)" stroke-width="1"/>'+
     '<text x="'+x+'" y="'+(barY+barH+16)+'" text-anchor="middle" font-size="10.5" fill="var(--t3)">'+t[1]+'</text>';});
 /* two label rows so the tightly-clustered high scores don't collide */
 const arr=[...DOS].sort((a,b)=>a.survScore-b.survScore),gap=56,PAD=26;
 const declutter=list=>{const pos=list.map(d=>X(d.survScore));
  for(let i=1;i<pos.length;i++)if(pos[i]<pos[i-1]+gap)pos[i]=pos[i-1]+gap;
  const over=pos[pos.length-1]-(W-PAD);if(over>0)for(let i=0;i<pos.length;i++)pos[i]-=over;
  for(let i=pos.length-2;i>=0;i--)if(pos[i]>pos[i+1]-gap)pos[i]=pos[i+1]-gap;
  if(pos[0]<PAD)pos[0]=PAD;return pos;};
 const tiers=[arr.filter((d,i)=>i%2===0),arr.filter((d,i)=>i%2===1)];
 const tierY=[[16,30],[46,60]];
 tiers.forEach((list,ti)=>{const pos=declutter(list),ly=tierY[ti][0],sy=tierY[ti][1];
  list.forEach((d,i)=>{const dx=X(d.survScore),lx=pos[i],col=survBand(d.survScore)[1];
   g+='<path d="M'+lx.toFixed(1)+' '+(sy+4)+' L'+lx.toFixed(1)+' '+(sy+12)+' L'+dx.toFixed(1)+' '+(barY-8)+' L'+dx.toFixed(1)+' '+barY+'" fill="none" stroke="var(--lines)" stroke-width="1"/>'+
      '<circle cx="'+dx.toFixed(1)+'" cy="'+(barY+barH/2)+'" r="3.5" fill="var(--t1)" stroke="var(--s1)" stroke-width="1.5"/>'+
      '<text class="tk" data-sym="'+esc(d.sym)+'" x="'+lx.toFixed(1)+'" y="'+ly+'" text-anchor="middle" font-size="11" font-weight="700" fill="var(--t1)" style="cursor:pointer">'+esc(d.sym)+'</text>'+
      '<text x="'+lx.toFixed(1)+'" y="'+sy+'" text-anchor="middle" font-size="10" font-weight="600" fill="'+col+'">'+d.survScore.toFixed(0)+'</text>';});});
 el.innerHTML='<svg viewBox="0 0 '+W+' '+H+'" style="width:100%;height:auto" font-family="inherit">'+g+'</svg>';}
/* ---------- News & filings desk ---------- */
const NEWSU={};
(function(){
 (typeof RAD!=='undefined'?RAD:[]).forEach(r=>{NEWSU[r[0]]={name:r[1],sec:r[8],mcapB:r[2],pxNow:r[9],pct:r[10],nf:r[4],dos:!!dosBy[r[0]]};});
 DOS.forEach(d=>{if(!NEWSU[d.sym])NEWSU[d.sym]={name:d.name,sec:d.sector,mcapB:d.mcapB,pxNow:d.price,dos:true};});
 const dl=document.getElementById('newsList');
 if(dl)dl.innerHTML=Object.keys(NEWSU).sort().map(s=>'<option value="'+s+'">'+esc(NEWSU[s].name)+'</option>').join('');
})();
function newsLinks(T){
 T=(T||'').toUpperCase().trim().replace(/[^A-Z0-9.\-]/g,'');
 if(!T)return '';
 const e='https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&owner=include&count=40&CIK='+encodeURIComponent(T)+'&type=';
 const sec=[
  ['Latest 10-Q','Quarterly report — the full earnings filing with the financial statements',e+'10-Q'],
  ['Latest 10-K','Annual report — the deepest yearly disclosure',e+'10-K'],
  ['Recent 8-Ks','Material events and press releases, including earnings releases',e+'8-K'],
  ['All SEC filings','Every document this company has filed with the SEC',e]];
 const news=[
  ['Google News','Recent headlines across the web','https://news.google.com/search?q='+encodeURIComponent(T+' stock')+'&hl=en-US'],
  ['Yahoo Finance','Quote, chart and the company news feed','https://finance.yahoo.com/quote/'+encodeURIComponent(T)+'/news'],
  ['StockAnalysis','Financials, analyst estimates and news','https://stockanalysis.com/stocks/'+encodeURIComponent(T)+'/'],
  ['SEC full-text search','Search the text of every filing for this ticker','https://efts.sec.gov/LATEST/search-index?q=%22'+encodeURIComponent(T)+'%22']];
 const card=g=>g.map(x=>'<a class="newsitem" href="'+x[2]+'" target="_blank" rel="noopener noreferrer"><div class="ni-t">'+x[0]+' ↗</div><div class="ni-d">'+x[1]+'</div></a>').join('');
 const u=NEWSU[T]; let head='';
 if(u){const pc=u.pct>0?'var(--good)':u.pct<0?'var(--bad)':'var(--t3)';
  head='<div class="newshead"><div><div style="font-size:17px;font-weight:600">'+esc(u.name)+' <span class="mut" style="font-size:13px">'+esc(T)+'</span></div>'+
   '<div class="sub" style="margin-top:2px">'+esc(u.sec||'13F holding')+(u.mcapB?' · $'+(u.mcapB>=1?u.mcapB.toFixed(2)+'B':(u.mcapB*1000).toFixed(0)+'M'):'')+(u.nf?' · held by '+u.nf+' funds':'')+'</div></div>'+
   (u.pxNow?'<div style="text-align:right"><div class="sub">Price now</div><div style="font-size:16px;font-weight:600">$'+(+u.pxNow).toFixed(2)+'</div>'+(u.pct!=null?'<div style="font-size:12px;color:'+pc+'">'+(u.pct>0?'+':'')+u.pct+'% since 30 Jun</div>':'')+'</div>':'')+
   '<button class="btn" data-sym="'+esc(T)+'">'+(u.dos?'Open dossier':'Quick profile')+'</button></div>';
 } else {
  head='<div class="newshead"><div><div style="font-size:17px;font-weight:600">'+esc(T)+'</div><div class="sub" style="margin-top:2px">Not in your fund universe — the links below still work for any US-listed ticker.</div></div></div>';
 }
 return head+
  '<div class="newsgrp"><h4>SEC filings</h4><div class="newsgrid">'+card(sec)+'</div></div>'+
  '<div class="newsgrp"><h4>News &amp; research</h4><div class="newsgrid">'+card(news)+'</div></div>'+
  '<div class="axisnote">EDGAR resolves the ticker automatically. Earnings arrive two ways: the press release lands as an 8-K (exhibit 99), the full numbers as the 10-Q. The terminal does not embed these pages, but every link opens the live source in a new tab.</div>';
}
function runNews(){const T=(document.getElementById('newsTicker').value||'').toUpperCase().trim();
 document.getElementById('newsOut').innerHTML=T?newsLinks(T):'<div class="sub" style="padding:22px 2px">Enter a ticker above to pull its latest filings and news.</div>';}
(function(){const g=document.getElementById('newsGo'),i=document.getElementById('newsTicker');
 if(g)g.onclick=runNews;
 if(i){i.addEventListener('keydown',e=>{if(e.key==='Enter')runNews();});i.addEventListener('change',runNews);}})();
function drawNews(){if(!document.getElementById('newsOut').innerHTML.trim())runNews();}

/* ---------- Analysis desk (on-demand research collection) ---------- */
function drawAnalysis(){
 const AN=(D.analysis||[]);
 const dl=document.getElementById('anaList');
 if(dl)dl.innerHTML=AN.map(a=>'<option value="'+esc(a.sym)+'">'+esc((dosBy[a.sym]&&dosBy[a.sym].name)||a.sym)+'</option>').join('');
 const host=document.getElementById('anaOut');if(!host)return;
 if(!AN.length){host.innerHTML='<div class="anaEmpty"><div class="big">No analyses yet</div>Tell Claude a company in the chat — for example &ldquo;research Viking Therapeutics&rdquo; — and its full deep-dive dossier is built and appears here, ready to open anytime.</div>';return;}
 host.innerHTML='<div class="anagrid">'+AN.map(a=>{const d=dosBy[a.sym];if(!d)return '';const b=survBand(d.survScore);
   return '<div class="anacard" data-sym="'+esc(a.sym)+'"><div class="att">'+esc(a.sym)+' <span class="mut" style="font-weight:500;font-size:12.5px">'+esc(d.name)+'</span></div>'+
    '<div class="asub">'+esc(d.sector||'')+(d.mcapB?' · $'+(d.mcapB>=1?d.mcapB.toFixed(2)+'B':(d.mcapB*1000).toFixed(0)+'M'):'')+'</div>'+
    '<div class="awhat">'+esc((d.what||'').slice(0,150))+((d.what||'').length>150?'…':'')+'</div>'+
    '<div class="arow"><span>Survival <b style="color:'+b[1]+'">'+d.survScore.toFixed(0)+'</b></span><span>·</span><span>researched '+esc(a.asOf||'')+'</span><span style="margin-left:auto;color:var(--blue)">Open ↗</span></div></div>';}).join('')+'</div>';
}
(function(){const g=document.getElementById('anaJumpGo'),i=document.getElementById('anaJump');
 function jump(){const t=(i.value||'').toUpperCase().trim();if(!t)return;if(dosBy[t]){openCo(t);}else{const h=document.getElementById('anaOut');const m=document.createElement('div');m.className='sub';m.style.cssText='padding:8px 2px;color:var(--warn)';m.textContent=t+' has no analysis yet — ask Claude to research it and it will appear here.';h.prepend(m);setTimeout(()=>{m.remove();},4500);}}
 if(g)g.onclick=jump; if(i){i.addEventListener('keydown',e=>{if(e.key==='Enter')jump();});}})();

function drawAll(){drawAud();drawScaleDemo();ovEntry();ovShift();ovAct();drawRun();drawScore();drawNet();quickT.paint();radarT.paint();
 if(!document.getElementById('v-risk').classList.contains('hide'))drawScatter();
 if(!document.getElementById('v-funds').classList.contains('hide'))drawFunds();}
setF();drawAll();drawCmp();
</script></body></html>"""
open(_os.path.join(_D, 'Jakes_AI_Terminal.html'),'w').write(HTML.replace('__DATA__', DATA))
print('written', len(HTML.replace('__DATA__', DATA)))
