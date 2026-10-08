#!/usr/bin/env python3
"""Erzeugt den Kontroll-Kiosk (apps/kontroll-kiosk/index.html) aus inhalt/kiosk.json.

Nachbau des Kiosks der Reihe Wunschbriefe: Tipp oder Lösung wählen, Blattnummer
eingeben, lesen, zurück zum Start. Eine Datei, offline, keine Kinderdaten.
Titel, Etappe und Blattnummern kommen aus inhalt/etappeN.json und werden geprüft.

Aufruf: python tools/build_kiosk.py      (erzeugt und prüft im Browser)
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_material import font_css  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "apps" / "kontroll-kiosk" / "index.html"


def daten() -> dict:
    k = json.loads((ROOT / "inhalt" / "kiosk.json").read_text(encoding="utf-8"))["blaetter"]
    data, etappen = {}, []
    for n in (1, 2, 3):
        c = json.loads((ROOT / "inhalt" / f"etappe{n}.json").read_text(encoding="utf-8"))
        etappen.append({"n": n, "titel": c["titel"], "blaetter": [[b["nr"], b["titel"]] for b in c["blaetter"]]})
        for b in c["blaetter"]:
            key = str(b["nr"])
            if key not in k:
                raise SystemExit(f"Kiosk: Blatt {key} fehlt in inhalt/kiosk.json")
            data[key] = dict(k[key], title=b["titel"], status=f"Etappe {n} · Pflicht + freiwillige Vertiefung")
    extra = set(k) - set(data)
    if extra:
        raise SystemExit(f"Kiosk: Blätter ohne Arbeitsblatt: {sorted(extra)}")
    return data, etappen


TEMPLATE = r"""<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#1a1a1a">
<title>Kontroll-Kiosk · Zootiere</title>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%231a1a1a'/%3E%3Cpath d='M18 33l9 9 19-20' fill='none' stroke='white' stroke-width='7' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E">
<style>
__FONTS__
:root{--ink:#161616;--mid:#4a4a4a;--soft:#767676;--line:#cfcfcf;--fill:#f0f0f0;--fill2:#e4e4e4;--white:#fff;--radius:clamp(16px,2vw,26px)}
*{box-sizing:border-box}
html,body{margin:0;min-height:100%;font-family:'Andika',sans-serif;color:var(--ink)}
body{min-height:100vh;display:grid;place-items:center;padding:clamp(8px,2.2vh,22px);background:#2b2b2b}
button{font:inherit}
button:focus-visible,summary:focus-visible{outline:4px solid #000;outline-offset:3px;box-shadow:0 0 0 7px #fff}
.app{position:relative;width:min(1120px,100%);height:min(780px,calc(100vh - 28px));min-height:620px;background:var(--white);
  border:3px solid var(--ink);border-radius:var(--radius);overflow:hidden;display:grid;grid-template-rows:auto minmax(0,1fr) auto}
header{padding:16px clamp(22px,3.5vw,42px);display:flex;align-items:center;justify-content:space-between;gap:18px;border-bottom:2px solid var(--ink)}
.brand{display:flex;align-items:center;gap:14px;min-width:0}
.brand-mark{width:46px;height:46px;flex:0 0 auto;border-radius:13px;background:var(--ink);display:grid;place-items:center}
.brand-mark svg{width:28px;height:28px}
header h1{margin:0;font-size:clamp(1.45rem,2.8vw,2.2rem);line-height:1}
.subtitle{margin-top:5px;color:var(--mid);font-size:clamp(.85rem,1.25vw,1rem)}
.header-actions{display:flex;gap:9px}
.header-btn{min-height:44px;border:2px solid var(--ink);background:#fff;color:var(--ink);border-radius:12px;padding:9px 14px;font-weight:700;cursor:pointer}
.header-btn:hover{background:var(--fill)}
main{min-height:0;padding:clamp(16px,2.6vw,30px) clamp(20px,3.2vw,40px);display:grid;place-items:center;overflow:auto}
.screen{width:100%;max-width:960px;animation:screenIn .2s ease-out}
@keyframes screenIn{from{opacity:.3;transform:translateY(6px)}to{opacity:1;transform:none}}
.hidden{display:none!important}
.kicker{display:inline-block;margin:0 0 .5em;padding:.25em .7em;border-radius:.5em;background:var(--fill2);font-weight:700;font-size:.95rem}
h2{margin:0;line-height:1.08;font-weight:700}
.start h2{font-size:clamp(2rem,4.2vw,3.4rem)}
.lead{font-size:clamp(1.05rem,1.8vw,1.3rem);line-height:1.45;color:var(--mid);margin:.7em 0 1.2em}
.start-layout{display:grid;grid-template-columns:1.25fr .75fr;gap:clamp(24px,4vw,48px);align-items:start}
.choice-grid{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.big-btn{min-height:150px;border-radius:18px;padding:22px 20px;text-align:left;cursor:pointer;border:3px solid var(--ink);background:#fff;color:var(--ink);transition:.15s}
.big-btn:hover,.big-btn:focus-visible{transform:translateY(-2px);background:var(--fill)}
.big-btn.tip{border-style:dashed}
.big-btn.solution{background:var(--ink);color:#fff}
.big-btn.solution:hover,.big-btn.solution:focus-visible{background:#333}
.big-btn .btn-title{display:block;font-size:clamp(1.7rem,3.2vw,2.5rem);font-weight:700;line-height:1}
.big-btn .btn-copy{display:block;margin-top:.6em;font-size:1rem;line-height:1.35}
.flow{grid-column:1/-1;display:flex;align-items:center;gap:9px;margin-top:4px;color:var(--mid);font-size:.92rem;font-weight:700}
.flow-step{flex:1;text-align:center;padding:9px 8px;border-radius:10px;background:var(--fill)}
.overview{border:2px solid var(--line);border-radius:18px;padding:16px 18px;font-size:.98rem;line-height:1.35}
.overview h3{margin:0 0 8px;font-size:1.05rem}
.overview .et{margin-top:10px}
.overview .et b{display:block;font-size:.9rem;color:var(--mid);text-transform:uppercase;letter-spacing:.04em}
.overview .bl{display:flex;gap:8px}
.overview .bl span:first-child{flex:0 0 1.6em;font-weight:700;text-align:right}
.number-wrap{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(24px,5vw,52px);align-items:center}
.number-head h2{font-size:clamp(1.8rem,3vw,2.6rem)}
.number-head .lead{margin:.35em 0 .3em}
.mode-chip{display:inline-flex;align-items:center;padding:7px 15px;border-radius:999px;font-weight:700;margin-bottom:12px;border:2px solid var(--ink)}
.mode-tip{border-style:dashed;background:#fff}
.mode-solution{background:var(--ink);color:#fff}
.number-display{font-size:clamp(3rem,7vw,5rem);font-weight:700;line-height:1;background:var(--fill);border:2px solid var(--ink);border-radius:18px;
  padding:10px;margin:14px 0;min-height:110px;display:flex;align-items:center;justify-content:center;font-variant-numeric:tabular-nums}
.keypad{display:grid;grid-template-columns:repeat(3,1fr);gap:9px}
.key{min-height:64px;border:2px solid var(--line);border-radius:14px;padding:12px;font-size:1.5rem;font-weight:700;background:#fff;color:var(--ink);cursor:pointer}
.key:hover,.key:focus-visible{border-color:var(--ink);background:var(--fill)}
.key.action{font-size:1rem;background:var(--fill)}
.key.show{grid-column:span 3;background:var(--ink);border-color:var(--ink);color:#fff;font-size:1.15rem}
.key.show:hover{background:#333}
.error{min-height:24px;margin-top:8px;font-weight:700;color:#000;text-decoration:underline}
.result-card{border:2px solid var(--ink);border-radius:22px;padding:clamp(22px,3vw,34px)}
.result-card h2{font-size:clamp(1.6rem,2.7vw,2.3rem)}
.result-type{font-size:.9rem;font-weight:700;color:var(--mid);text-transform:uppercase;letter-spacing:.05em;margin:12px 0 16px}
.result-text{font-size:clamp(1.08rem,1.7vw,1.3rem);line-height:1.55;white-space:pre-line}
details{margin-top:20px;padding:12px 16px;border:2px dashed var(--ink);border-radius:14px}
summary{cursor:pointer;font-weight:700;font-size:1.1rem}
details .result-text{margin-top:8px}
.actions{display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin-top:18px}
.primary,.secondary{min-height:48px;border-radius:12px;padding:12px 19px;font-weight:700;cursor:pointer;border:2px solid var(--ink)}
.primary{background:var(--ink);color:#fff}.primary:hover{background:#333}
.secondary{background:#fff;color:var(--ink)}.secondary:hover{background:var(--fill)}
footer{display:flex;align-items:center;justify-content:space-between;gap:18px;padding:11px clamp(22px,3.5vw,42px);border-top:2px solid var(--ink);font-size:.85rem;color:var(--mid)}
.phase{font-weight:700;color:var(--ink);white-space:nowrap}
#resultTitle:focus{outline:none}
@media(max-width:820px){
  body{padding:0;background:#fff}.app{width:100%;height:100vh;min-height:100vh;border-radius:0;border-width:0}
  .start-layout,.number-wrap{grid-template-columns:1fr}.overview.side{display:none}main{padding:22px 18px}
}
@media(max-width:560px){
  header{align-items:flex-start}.brand-mark{display:none}.header-btn{padding:8px 10px}
  .choice-grid{grid-template-columns:1fr}.big-btn{min-height:112px}.flow{display:none}
  footer{display:block;text-align:center}.phase{display:block;margin-top:3px}
}
@media(max-height:650px) and (min-width:821px){.app{min-height:0}.big-btn{min-height:116px}main{padding-top:18px;padding-bottom:18px}}
@media(prefers-reduced-motion:reduce){*,*::before,*::after{animation-duration:.01ms!important;transition-duration:.01ms!important}}
</style>
</head>
<body>
<div class="app">
  <header>
    <div class="brand">
      <div class="brand-mark" aria-hidden="true"><svg viewBox="0 0 64 64"><path d="M18 33l9 9 19-20" fill="none" stroke="white" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg></div>
      <div><h1>Kontroll-Kiosk</h1><div class="subtitle">Zootiere · Blatt 1–__MAX__ · nur beim Üben</div></div>
    </div>
    <div class="header-actions">
      <button class="header-btn" id="fullscreen">Vollbild</button>
      <button class="header-btn" id="homeHeader">Start</button>
    </div>
  </header>

  <main>
    <section class="screen start" id="startScreen">
      <div class="start-layout">
        <div>
          <p class="kicker">Selbst kontrollieren</p>
          <h2>Tipp oder Lösung?</h2>
          <p class="lead">Wähle, was du brauchst. Ein Tipp hilft dir beim Weiterdenken. Mit der Lösung vergleichst du dein Ergebnis und änderst nur, was nötig ist.</p>
          <div class="choice-grid">
            <button class="big-btn tip" data-mode="tip"><span class="btn-title">Tipp</span><span class="btn-copy">Ein Hinweis hilft dir beim Weiterdenken.</span></button>
            <button class="big-btn solution" data-mode="solution"><span class="btn-title">Lösung</span><span class="btn-copy">Vergleiche dein Ergebnis mit der Lösung.</span></button>
            <div class="flow" aria-hidden="true"><div class="flow-step">1. auswählen</div><span>→</span><div class="flow-step">2. Blattnummer</div><span>→</span><div class="flow-step">3. lesen und zurück</div></div>
          </div>
        </div>
        <div class="overview side" aria-label="Übersicht der Blätter">__OVERVIEW__</div>
      </div>
    </section>

    <section class="screen hidden" id="numberScreen">
      <div class="number-wrap">
        <div>
          <div id="modeChip" class="mode-chip"></div>
          <div class="number-head"><h2>Welche Blattnummer?</h2><p class="lead">Tippe die Nummer oder nutze die Tastatur. Dann „Anzeigen“.</p></div>
          <div class="number-display" id="display" role="status" aria-label="Blattnummer">–</div>
          <div class="error" id="error" role="alert"></div>
        </div>
        <div class="keypad">
          <button class="key">1</button><button class="key">2</button><button class="key">3</button>
          <button class="key">4</button><button class="key">5</button><button class="key">6</button>
          <button class="key">7</button><button class="key">8</button><button class="key">9</button>
          <button class="key action" data-action="clear">Löschen</button><button class="key">0</button>
          <button class="key action" data-action="backspace" aria-label="Letzte Ziffer löschen">⌫</button>
          <button class="key show" data-action="show">Anzeigen</button>
        </div>
      </div>
    </section>

    <section class="screen hidden" id="resultScreen">
      <div class="result-card">
        <div id="resultMode" class="mode-chip"></div>
        <h2 id="resultTitle" tabindex="-1"></h2>
        <div class="result-type" id="resultType"></div>
        <div class="result-text" id="resultText"></div>
        <details id="extra" class="hidden"><summary>Vertiefung · freiwillig</summary><div class="result-text" id="extraText"></div></details>
      </div>
      <div class="actions">
        <button class="secondary" id="switchMode">Lösung ansehen</button>
        <button class="secondary" id="another">Andere Blattnummer</button>
        <button class="primary" id="home">Zurück zum Start</button>
      </div>
    </section>
  </main>

  <footer>
    <span>Lies in Ruhe. Kehre danach zu deinem Papierblatt zurück. Nicht bei Gelingensnachweis, Probearbeit oder Klassenarbeit.</span>
    <span class="phase">Planung → Durchführung → Reflexion</span>
  </footer>
</div>
<script>
/* DATA_START */const DATA=__DATA__;/* DATA_END */
const MAX=__MAX__;let mode=null,number="",timer;
const screens={start:document.getElementById("startScreen"),number:document.getElementById("numberScreen"),result:document.getElementById("resultScreen")};
const display=document.getElementById("display"),error=document.getElementById("error"),modeChip=document.getElementById("modeChip");
function resetTimer(){clearTimeout(timer);if(screens.result.classList.contains("hidden"))timer=setTimeout(goHome,180000)}
["click","keydown","pointerdown"].forEach(ev=>document.addEventListener(ev,resetTimer,{passive:true}));
function showScreen(n){Object.values(screens).forEach(s=>s.classList.add("hidden"));screens[n].classList.remove("hidden");window.scrollTo(0,0);resetTimer()}
function goHome(){mode=null;number="";updateDisplay();showScreen("start");document.querySelector('[data-mode="tip"]').focus()}
function setChip(el){el.textContent=mode==="tip"?"Tipp":"Lösung";el.className="mode-chip "+(mode==="tip"?"mode-tip":"mode-solution")}
function chooseMode(m){mode=m;number="";updateDisplay();setChip(modeChip);showScreen("number");document.querySelector('[data-action="show"]').focus()}
function updateDisplay(){display.textContent=number||"–";error.textContent=""}
function addDigit(d){if(number.length<2){number+=d;updateDisplay()}}
function proceedNumber(){const n=Number(number);if(!Number.isInteger(n)||n<1||n>MAX||!DATA[n]){error.textContent="Bitte gib eine Blattnummer von 1 bis "+MAX+" ein.";return}showResult()}
function showResult(){
 const n=Number(number),item=DATA[n];
 document.getElementById("resultTitle").textContent=`Blatt ${n} – ${item.title}`;
 setChip(document.getElementById("resultMode"));
 document.getElementById("resultType").textContent=item.status+(mode==="tip"?" · Tipp":" · "+item.type);
 document.getElementById("resultText").textContent=mode==="tip"?item.tip:item.solution;
 const extra=document.getElementById("extra");extra.open=false;extra.classList.toggle("hidden",mode!=="solution"||!item.extra);document.getElementById("extraText").textContent=item.extra||"";
 document.getElementById("switchMode").textContent=mode==="tip"?"Lösung ansehen":"Tipp ansehen";
 showScreen("result");document.getElementById("resultTitle").focus();
}
document.querySelectorAll("[data-mode]").forEach(b=>b.addEventListener("click",()=>chooseMode(b.dataset.mode)));
document.querySelectorAll(".key").forEach(b=>b.addEventListener("click",()=>{const a=b.dataset.action;if(a==="clear")number="";else if(a==="backspace")number=number.slice(0,-1);else if(a==="show")return proceedNumber();else addDigit(b.textContent.trim());updateDisplay()}));
document.addEventListener("keydown",e=>{if(e.ctrlKey||e.altKey||e.metaKey)return;if(!screens.number.classList.contains("hidden")){
 if(/^[0-9]$/.test(e.key)){e.preventDefault();addDigit(e.key)}
 else if(e.key==="Backspace"){e.preventDefault();number=number.slice(0,-1);updateDisplay()}
 else if(e.key==="Delete"){e.preventDefault();number="";updateDisplay()}
 else if(e.key==="Enter"){e.preventDefault();proceedNumber()}
 else if(e.key==="Escape"){e.preventDefault();goHome()}
}else if(e.key==="Escape"){e.preventDefault();goHome()}});
document.getElementById("home").onclick=goHome;document.getElementById("homeHeader").onclick=goHome;
document.getElementById("another").onclick=()=>chooseMode(mode);
document.getElementById("switchMode").onclick=()=>{mode=mode==="tip"?"solution":"tip";showResult()};
document.getElementById("fullscreen").onclick=async()=>{try{if(!document.fullscreenElement)await document.documentElement.requestFullscreen();else await document.exitFullscreen()}catch(e){document.getElementById("fullscreen").textContent="Nutze F11"}};
const params=new URLSearchParams(location.search);
if(params.has("mode")&&params.has("blatt")&&DATA[Number(params.get("blatt"))]){mode=params.get("mode")==="solution"?"solution":"tip";number=params.get("blatt");showResult()}else goHome();
</script></body></html>"""


def overview(etappen) -> str:
    h = ["<h3>Die Blätter</h3>"]
    for e in etappen:
        h.append("<div class='et'><b>Etappe %d</b>%s</div>" % (e["n"], "".join(
            "<div class='bl'><span>%d</span><span>%s</span></div>" % (nr, t) for nr, t in e["blaetter"])))
    return "".join(h)


def check(path: Path, data: dict):
    from playwright.sync_api import sync_playwright
    fails = []
    url = path.resolve().as_uri()
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        for vw in [(1280, 800), (390, 844)]:
            pg = br.new_page(viewport={"width": vw[0], "height": vw[1]})
            ext = []
            pg.on("request", lambda r: ext.append(r.url) if not r.url.startswith(("file:", "data:")) else None)
            pg.goto(url)
            for n in data:
                for m in ("tip", "solution"):
                    pg.evaluate("goHome()")
                    pg.click(f"[data-mode='{m}']")
                    for d in n:
                        pg.keyboard.press(d)
                    pg.keyboard.press("Enter")
                    t = pg.inner_text("#resultTitle")
                    body = pg.inner_text("#resultText")
                    want = data[n]["tip" if m == "tip" else "solution"]
                    if t != f"Blatt {n} – {data[n]['title']}" or body.strip() != want.strip():
                        fails.append(f"{vw} Blatt {n} {m}: falsche Anzeige")
                    if m == "solution" and data[n].get("extra"):
                        if not pg.is_visible("#extra"):
                            fails.append(f"Blatt {n}: Vertiefung fehlt")
                        elif pg.is_visible("#extraText"):
                            fails.append(f"Blatt {n}: Vertiefung schon offen")
                    over = pg.evaluate("document.querySelector('main').scrollWidth>document.querySelector('main').clientWidth+1")
                    if over:
                        fails.append(f"{vw} Blatt {n} {m}: waagerechter Überlauf")
            # Zahlenfeld, Fehler, Wechsel
            pg.evaluate("goHome()")
            pg.click("[data-mode='tip']")
            pg.click(".key:text-is('1')")
            pg.click(".key:text-is('0')")
            pg.click("[data-action='show']")
            if "1 bis" not in pg.inner_text("#error"):
                fails.append("Fehlermeldung bei Blatt 10 fehlt")
            pg.click("[data-action='backspace']")
            pg.click("[data-action='show']")
            if not pg.inner_text("#resultTitle").startswith("Blatt 1 "):
                fails.append("Zahlenfeld/Löschen fehlerhaft")
            pg.click("#switchMode")
            if pg.inner_text("#resultMode") != "Lösung":
                fails.append("Wechsel Tipp → Lösung fehlerhaft")
            pg.keyboard.press("Escape")
            if not pg.is_visible("#startScreen"):
                fails.append("Escape führt nicht zum Start")
            if ext:
                fails.append(f"Netzzugriffe: {ext[:3]}")
            pg.close()
        br.close()
    return fails


def main():
    data, etappen = daten()
    mx = max(int(k) for k in data)
    html = (TEMPLATE.replace("__FONTS__", font_css())
            .replace("__DATA__", json.dumps(data, ensure_ascii=False))
            .replace("__OVERVIEW__", overview(etappen))
            .replace("__MAX__", str(mx)))
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(html, encoding="utf-8")
    fails = check(OUT, data)
    print(f"Kiosk: {len(data)} Blätter, {2 * len(data)} Ansichten je Bildschirmgröße geprüft")
    print("ok" if not fails else "FEHLER:\n  " + "\n  ".join(fails))
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
