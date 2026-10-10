#!/usr/bin/env python3
"""Erzeugt die Lern-App fürs Smartphone (lernapp/) aus inhalt/*.json.

Eine HTML-Datei mit allen Inhalten, Schrift und Bildern (offline nutzbar),
dazu Manifest, Service Worker und Icons für „Zum Startbildschirm“.
Merkkarten (Input/Merkblatt), Strategiekarten, Checkliste K1–K6, Wörterhilfe,
Lernweg-Blätter und Interviews kommen aus den bestehenden Inhaltsdateien;
app-eigene Texte und Übungen aus inhalt/lernapp.json.

Prüft vor dem Schreiben: Sperrliste (Probearbeit, Klassenarbeiten,
Gelingensnachweise, Kiosk-Lösungen zu Blatt 1–9 dürfen nicht vorkommen) und
Stimmigkeit der Übungen. Danach Browsertest bei 390 × 844 (Playwright):
kein seitliches Scrollen, Tippflächen, keine Netzanfragen, jede Übung lösbar,
offline nach dem ersten Laden.

Aufruf: python tools/build_lernapp.py           (erzeugen und prüfen)
        python tools/build_lernapp.py --ohne-test
"""
import base64
import hashlib
import io
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "lernapp"
VORLAGE = ROOT / "tools" / "vorlagen" / "lernapp_vorlage.html"
MARK = re.compile(r"\[\[([^|\]]+)\|([^\]]+)\]\]")
BEISPIELE = {"angola-giraffe": "training_giraffe.json"}


def j(name):
    return json.loads((ROOT / "inhalt" / name).read_text(encoding="utf-8"))


def b64(data: bytes) -> str:
    return base64.b64encode(data).decode("ascii")


def font_css() -> str:
    """Andika eingebettet (wie in build_material.py, ohne dessen PDF-Abhängigkeiten)."""
    out = []
    for weight, style in [(400, "normal"), (700, "normal"), (400, "italic")]:
        f = ROOT / "assets" / "fonts" / f"andika-latin-{weight}-{style}.woff2"
        out.append("@font-face{font-family:'Andika';font-weight:%d;font-style:%s;font-display:swap;"
                   "src:url(data:font/woff2;base64,%s) format('woff2');}" % (weight, style, b64(f.read_bytes())))
    return "\n".join(out)


# ------------------------------------------------------------------ Bilder
def bilder() -> dict:
    from PIL import Image
    im = Image.open(ROOT / "assets/bilder/fischotter_farbe.jpg").convert("RGB")
    im.thumbnail((720, 720))
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=78, optimize=True, progressive=True)
    return {
        "fischotter": {"src": "data:image/jpeg;base64," + b64(buf.getvalue()),
                       "alt": "Ein Fischotter liegt im Gras. Gut zu sehen sind Kopf, Schnauze mit langen Tasthaaren, kleine Ohren und das Fell.",
                       "cred": "Foto: Dave Pape · Public Domain"},
        "aquarium": {"src": "data:image/svg+xml;base64," + b64((ROOT / "assets/grafik/aquarium_farbe.svg").read_bytes()),
                     "alt": "Aquarium mit vier Fischen: A rund mit Streifen, B lang und schmal mit Punkten, C dreieckig mit langen Flossen oben und unten, D klein mit großer Schwanzflosse.",
                     "cred": ""},
    }


# ------------------------------------------------------------------ Daten
def daten() -> dict:
    app = j("lernapp.json")
    ivs = j("interviews.json")
    etappen = [j(f"etappe{n}.json") for n in (1, 2, 3)]
    wahl = j("wahlphase.json")
    strat = j("strategiekarten.json")

    # Merkkarten = Input/Merkblatt-Abschnitte (wortgleich)
    wissen_et = []
    for c in etappen:
        abschnitte = []
        for a in c["input"]:
            bild = None
            if a.get("grafik", "").endswith("aquarium.svg"):
                bild = "aquarium"
            elif "Foto" in a["titel"] and c["etappe"] == 1:
                bild = "fischotter"
            abschnitte.append({"titel": a["titel"], "bild": bild, "bloecke": a["bloecke"]})
        wissen_et.append({"etappe": c["etappe"], "titel": c["titel"], "ziel": c["ziel"],
                          "abschnitte": abschnitte, "abschluss": c["abschluss"]})

    # Lernweg: Etappen aus den Inhaltsdateien, danach Stationen aus lernapp.json
    weg = []
    for c in etappen:
        n = c["etappe"]
        punkte = [f"Input gehört oder Merkblatt {n} gelesen"]
        punkte += [f"Blatt {b['nr']} · {b['titel']}" for b in c["blaetter"]]
        punkte.append("Freiwillige Vertiefungen")
        if n < 3:
            punkte.append(f"Gelingensnachweis {n} · {c['nachweis']['titel']} (4 von 5)")
        else:
            punkte += ["Probearbeit geschrieben (4 von 5)", "Feedback zur Probearbeit bekommen"]
        weg.append({"id": f"e{n}", "titel": f"Etappe {n} · {c['titel']}",
                    "text": app["weg"]["etappe_text"], "punkte": punkte, "wissen": f"e{n}", "ueben": n})
    projekte = {p["id"] if "id" in p else p.get("nr"): p["titel"] for p in wahl["projekte"]}
    for s in app["weg"]["stationen"]:
        for pk in s["punkte"]:
            m = re.match(r"(P\d) · (.+)", pk)
            if m and projekte.get(m.group(1)) != m.group(2):
                raise SystemExit(f"Lernapp: Projekttitel passt nicht zu wahlphase.json: {pk}")
        weg.append(s)

    # Interviews, die Übungen brauchen
    alle = {t["id"]: t for t in ivs["tiere"] + ivs["foerder"]}
    need = {u["interview"] for u in app["uebungen"] if u["typ"] == "detektiv"}
    interviews = {}
    for i in sorted(need):
        t = alle[i]
        interviews[i] = {"titel": t["titel"], "einleitung": t["einleitung"], "paare": t["paare"], "woerter": t.get("woerter", [])}

    # Beispielaufgaben (Schritt für Schritt), z. B. Angola-Giraffe
    beispiele = {}
    for u in app["uebungen"]:
        if u["typ"] == "beispiel":
            b = j(BEISPIELE[u["quelle"]])
            beispiele[u["quelle"]] = {"id": b["id"], "zootier": b["zootier"], "hinweis": b["hinweis"], "schritte": b["schritte"]}
            interviews[b["id"]] = {"titel": b["titel"], "einleitung": b["einleitung"], "paare": b["paare"], "woerter": b["woerter"]}

    nachweise = ["Fischotter: Dave Pape · Public Domain (Wikimedia Commons).",
                 "Aquarium-Grafik: eigene Zeichnung für diese Reihe."]

    return {
        "app": app["app"], "start": app["start"], "elterninfo": app["elterninfo"],
        "stand": date.today().strftime("%d.%m.%Y"),
        "hinweis_fiktiv": ivs["hinweis_fiktiv"],
        "weg": weg,
        "wissen": {"etappen": wissen_et, "strategien": strat["karten"],
                   "checkliste": etappen[2]["zusatzseiten"], "woerter": etappen[1]["hilfen"][0]},
        "uebungen": app["uebungen"], "detektiv_rueckmeldung": app["detektiv_rueckmeldung"],
        "etappen_namen": app["etappen_namen"], "interviews": interviews, "beispiele": beispiele,
        "raetsel": app["raetsel"], "zuhause": app["zuhause"], "start_hinweis": app["start_hinweis"], "nachweise": nachweise,
    }


# ------------------------------------------------------------------ Prüfungen
def pruefe_inhalt(data: dict):
    fehler = []
    text = json.dumps(data, ensure_ascii=False)
    app = j("lernapp.json")
    # Satzvergleiche nur gegen app-eigene Texte: Material aus den Etappen (Interviews,
    # Merkblätter, Wörterhilfe) darf Sätze mit Nachweisen teilen, eigene Übungen nicht.
    eigen = json.dumps([{k: app[k] for k in ("uebungen", "raetsel", "zuhause", "start", "weg")}] + [j(f) for f in BEISPIELE.values()], ensure_ascii=False)

    # 1 Sperrliste: Namen aus Probearbeit und Klassenarbeiten
    for w in app["sperrliste"]:
        if re.search(r"(?<![\wäöüß])" + re.escape(w) + r"(?![\wäöüß])", text):
            fehler.append(f"Sperrwort in der App: {w}")

    # 2 Interviews aus Probearbeit/Klassenarbeit: keine Stelle darf vorkommen
    ivs = j("interviews.json")
    gesperrt = {"waschbaer", "biber", "breitmaulnashorn", "waschbaer-f", "biber-f"}
    for t in ivs["tiere"] + ivs["foerder"]:
        if t["id"] in gesperrt:
            for _, a in t["paare"]:
                for seg, _k in MARK.findall(a):
                    if len(seg) >= 25 and seg in eigen:
                        fehler.append(f"Prüfungsinterview ({t['id']}) in der App: {seg[:50]}")

    # 3 Gelingensnachweise: Interviewauszüge A/B
    for n in (1, 2):
        nw = j(f"etappe{n}.json")["nachweis"]
        for v in nw["varianten"].values():
            for _q, a in v["interview"]:
                for seg, _k in MARK.findall(a):
                    if len(seg) >= 25 and seg in eigen:
                        fehler.append(f"GN{n}-Auszug in der App: {seg[:50]}")

    # 4 Kiosk-Lösungen zu Blatt 1–9 und Musterlösungen Training
    kiosk = j("kiosk.json")["blaetter"]
    for nr, k in kiosk.items():
        for feld in ("solution", "extra"):
            for zeile in k.get(feld, "").split("\n"):
                z = re.sub(r"\s*\(Z\.[^)]*\)", "", zeile).strip(" /")
                if len(z) >= 30 and z in eigen:
                    fehler.append(f"Kiosk-Lösung Blatt {nr} in der App: {z[:50]}")
    for u in j("training.json")["uebungen"]:
        for feld in ("mindest", "regel"):
            for satz in re.split(r"(?<=\.)\s+|\n", u[feld]):
                if len(satz) >= 30 and satz in eigen:
                    fehler.append(f"Musterlösung Training ({u['kurz']}) in der App: {satz[:50]}")

    # 5 Stimmigkeit der Übungen
    ids = set()
    for u in data["uebungen"]:
        if u["id"] in ids:
            fehler.append(f"Übungs-ID doppelt: {u['id']}")
        ids.add(u["id"])
        if str(u["etappe"]) not in data["etappen_namen"]:
            fehler.append(f"{u['id']}: unbekannte Etappe {u['etappe']}")
        if u["typ"] == "auswahl":
            for it in u["items"]:
                if "optionen" in it:
                    if not (0 <= it["richtig"] < len(it["optionen"])):
                        fehler.append(f"{u['id']}: richtig außerhalb der Optionen: {it['text'][:40]}")
                elif it["richtig"] not in [o[0] for o in u["optionen"]]:
                    fehler.append(f"{u['id']}: unbekannte Antwort {it['richtig']}")
        elif u["typ"] in ("detektiv", "beispiel"):
            iv = data["interviews"][u["interview"] if u["typ"] == "detektiv" else data["beispiele"][u["quelle"]]["id"]]
            ks = [k for _q, a in iv["paare"] for _s, k in MARK.findall(a)]
            opt = {o[0] for o in u["optionen"]}
            for k in set(ks) & set(u["kuerzel"]):
                ziel = "weg" if k in "WXVU" else k
                if ziel not in opt:
                    fehler.append(f"{u['id']}: Kürzel {k} hat keine Option")
                if k not in data["detektiv_rueckmeldung"]:
                    fehler.append(f"{u['id']}: Rückmeldung für {k} fehlt")
            if sum(k in u["kuerzel"] for k in ks) < 8:
                fehler.append(f"{u['id']}: zu wenige Stellen")
        elif u["typ"] == "fehlerjagd":
            for it in u["items"]:
                if len(it["falsch"].split()) != len(it["richtig"].split()):
                    fehler.append(f"{u['id']}: Wortzahl falsch/richtig verschieden: {it['falsch']}")
        elif u["typ"] == "satzbau":
            for it in u["items"]:
                if len(set(it["teile"])) != len(it["teile"]):
                    fehler.append(f"{u['id']}: doppelte Wortkarte: {it['teile']}")
        elif u["typ"] != "saetze":
            fehler.append(f"{u['id']}: unbekannter Typ {u['typ']}")
    sp = data["elterninfo"]["sprachen"]
    if sp[0]["code"] != "de":
        fehler.append("Elterninfo: Deutsch muss die erste Sprache sein")
    for x in sp:
        if len(x["absaetze"]) not in (len(sp[0]["absaetze"]), len(sp[0]["absaetze"]) + 1):
            fehler.append(f"Elterninfo {x['code']}: Zahl der Absätze passt nicht zu Deutsch")
        if not any(k in x["absaetze"][-1] for k in ("KI", "AI", "IA", "ШІ", "YZ", "الذكاء الاصطناعي")):
            fehler.append(f"Elterninfo {x['code']}: KI-Hinweis fehlt am Ende")
        if (x["code"] != "de") != bool(x.get("hinweis_uebersetzung")):
            fehler.append(f"Elterninfo {x['code']}: Hinweis auf KI-Übersetzung fehlt oder ist zu viel")
    for w, _h in data["raetsel"]["woerter"]:
        if not re.fullmatch(r"[A-Za-zÄÖÜäöü]+", w):
            fehler.append(f"Rätselwort mit Sonderzeichen: {w}")
    if fehler:
        raise SystemExit("Lernapp – Inhaltsprüfung fehlgeschlagen:\n  " + "\n  ".join(fehler))
    print("ok: Inhaltsprüfung (Sperrliste, Prüfungs-/GN-Inhalte, Kiosk-Lösungen, Übungen)")


# ------------------------------------------------------------------ Ausgabe
MANIFEST = {
    "name": "Zootiere",
    "short_name": "Zootiere",
    "description": "Lernbegleiter zur Deutsch-Reihe Zootiere, Jahrgang 5",
    "lang": "de",
    "start_url": "./",
    "scope": "./",
    "display": "standalone",
    "orientation": "portrait",
    "background_color": "#F5F4F1",
    "theme_color": "#2C3D4C",
    "icons": [
        {"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
        {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"},
        {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"},
    ],
}

SW = """/* Service Worker der Lern-App: speichert die App für die Offline-Nutzung. */
const CACHE = "zootiere-lernapp-%s";
const FILES = ["./", "./index.html", "./manifest.webmanifest", "./icon-192.png", "./icon-512.png"];
self.addEventListener("install", e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(FILES)).then(() => self.skipWaiting())); });
self.addEventListener("activate", e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener("fetch", e => {
  if (e.request.method !== "GET") return;
  const url = new URL(e.request.url);
  if (url.origin !== location.origin) return;
  if (e.request.mode === "navigate") {
    e.respondWith(fetch(e.request).then(r => { const copy = r.clone(); caches.open(CACHE).then(c => c.put("./index.html", copy)); return r; }).catch(() => caches.match("./index.html")));
    return;
  }
  e.respondWith(caches.match(e.request).then(r => r || fetch(e.request)));
});
"""

ICON_HTML = """<!doctype html><html><head><style>%s
html,body{margin:0}
.i{width:512px;height:512px;background:#2C3D4C;display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:Andika;color:#fff}
.i b{font-size:150px;line-height:1;letter-spacing:-2px}
.i span{display:block;width:220px;height:22px;border-radius:11px;background:#D97A4A;margin-top:34px}
.i em{font-style:normal;font-size:54px;margin-top:26px;color:#D0DCE6}
</style></head><body><div class="i"><b>Zoo</b><span></span><em>Deutsch 5</em></div></body></html>"""


def icons(fonts: str):
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page(viewport={"width": 512, "height": 512})
        pg.set_content(ICON_HTML % fonts)
        pg.wait_for_timeout(200)
        png = pg.screenshot()
        br.close()
    from PIL import Image
    im = Image.open(io.BytesIO(png)).convert("RGB")
    im.save(OUT / "icon-512.png", optimize=True)
    im.resize((192, 192), Image.LANCZOS).save(OUT / "icon-192.png", optimize=True)


def schreiben(data: dict):
    OUT.mkdir(exist_ok=True)
    fonts = font_css()
    html = VORLAGE.read_text(encoding="utf-8")
    payload = json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    imgs = json.dumps(bilder(), ensure_ascii=False, separators=(",", ":"))
    html = html.replace("__FONTS__", fonts).replace("__DATA__", payload).replace("__IMAGES__", imgs)
    (OUT / "index.html").write_text(html, encoding="utf-8")
    (OUT / "manifest.webmanifest").write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=2), encoding="utf-8")
    version = hashlib.sha1(html.encode("utf-8")).hexdigest()[:10]
    (OUT / "sw.js").write_text(SW % version, encoding="utf-8")
    icons(fonts)
    kb = (OUT / "index.html").stat().st_size / 1024
    print(f"ok: lernapp/index.html ({kb:.0f} KB), manifest, sw.js (Version {version}), Icons")


# ------------------------------------------------------------------ Browsertest
def browsertest(data: dict, shots: Path | None = None):
    import http.server
    import socketserver
    import threading
    from functools import partial
    from playwright.sync_api import sync_playwright

    handler = partial(http.server.SimpleHTTPRequestHandler, directory=str(OUT))
    http.server.SimpleHTTPRequestHandler.log_message = lambda *a: None
    srv = socketserver.TCPServer(("127.0.0.1", 0), handler)
    port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{port}/"
    fehler, fremd = [], []

    def shot(pg, name):
        if shots:
            pg.screenshot(path=str(shots / f"{name}.png"), full_page=True)

    def overflow(pg, wo):
        w = pg.evaluate("[document.documentElement.scrollWidth, window.innerWidth]")
        if w[0] > w[1]:
            fehler.append(f"{wo}: seitliches Scrollen ({w[0]} > {w[1]})")
        klein = pg.evaluate("""() => [...document.querySelectorAll('main button, main a, main input, nav a')]
            .filter(e => e.offsetParent && !e.classList.contains('seg'))
            .map(e => { const r = e.getBoundingClientRect(); const t = e.type === 'checkbox' ? e.closest('label').getBoundingClientRect() : r;
                        return [t.width, t.height, (e.innerText || e.getAttribute('aria-label') || e.type).slice(0, 30)]; })
            .filter(x => x[0] < 44 || x[1] < 44)""")
        for k in klein[:5]:
            fehler.append(f"{wo}: Tippfläche zu klein {k[0]:.0f}×{k[1]:.0f} ({k[2]})")

    with sync_playwright() as pw:
        br = pw.chromium.launch()
        ctx = br.new_context(viewport={"width": 390, "height": 844}, device_scale_factor=2, is_mobile=True, has_touch=True, locale="de-DE")
        ctx.on("request", lambda r: fremd.append(r.url) if not r.url.startswith(base) and not r.url.startswith("data:") else None)
        pg = ctx.new_page()
        errs = []
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto(base)
        pg.locator("#popup").wait_for(state="visible", timeout=3000)
        if "Schultasche" not in pg.inner_text("#popup"):
            fehler.append("Hinweis beim Öffnen: Text fehlt")
        shot(pg, "popup")
        pg.locator("#popOk").click()
        pg.evaluate("navigator.serviceWorker.ready")
        pg.wait_for_timeout(300)

        # Tabs
        for tab in ["weg", "wissen/e1", "wissen/e2", "wissen/e3", "wissen/strategien", "wissen/pruefen", "wissen/woerter", "ueben", "raetsel", "zuhause", "info"]:
            pg.goto(base + "#/" + tab)
            pg.wait_for_timeout(120)
            overflow(pg, tab)
            shot(pg, "tab_" + tab.replace("/", "_"))
        # Merkkarte: Antwort aufdecken
        pg.goto(base + "#/wissen/e1")
        n = pg.locator("[data-reveal]").count()
        if n != sum(1 for a in data["wissen"]["etappen"][0]["abschnitte"] for b in a["bloecke"] if b[0] == "Gesicherte Antwort"):
            fehler.append("Wissen: Zahl der Antwort-Knöpfe stimmt nicht")
        pg.locator("[data-reveal]").first.click()
        # Lernweg: Haken setzen und behalten
        pg.goto(base + "#/weg")
        pg.locator("input[data-k]").first.check()
        pg.reload()
        weg_mit_hinweis(pg)
        pg.wait_for_timeout(200)
        if not pg.locator("input[data-k]").first.is_checked():
            fehler.append("Mein Weg: Haken wird nicht gespeichert")

        # Jede Übung durchspielen
        for u in data["uebungen"]:
            pg.goto(base + "#/ueben/" + u["id"])
            pg.wait_for_timeout(100)
            overflow(pg, u["id"])
            shot(pg, "ex_" + u["id"] + "_start")
            try:
                spiele(pg, u, data)
            except Exception as e:  # noqa: BLE001
                fehler.append(f"{u['id']}: nicht lösbar ({e})")
                continue
            if not pg.locator(".done-card").count():
                fehler.append(f"{u['id']}: Abschluss erscheint nicht")
            shot(pg, "ex_" + u["id"] + "_ende")

        # Rätsel lösen
        pg.goto(base + "#/raetsel")
        for _ in range(2):
            hinweis = pg.locator(".card .label + div").first.inner_text()
            wort = next(w for w, h in data["raetsel"]["woerter"] if h.replace("*", "") == hinweis)
            for ch in wort.upper():
                pg.locator(f".letter:not([disabled]):text-is('{ch}')").first.click()
            if not pg.locator(".fb.ok").count():
                fehler.append(f"Rätsel {wort}: nicht lösbar")
            shot(pg, "raetsel_geloest")
            pg.locator("#next").click()

        # Elterninfo: alle Sprachen, Arabisch von rechts nach links, KI-Hinweis
        pg.goto(base + "#/info")
        for sp in data["elterninfo"]["sprachen"]:
            pg.locator(f"[data-lang='{sp['code']}']").click()
            box = pg.locator(".elterninfo")
            if box.get_attribute("lang") != sp["code"] or len(sp["absaetze"]) + bool(sp.get("hinweis_uebersetzung")) != box.locator("p").count():
                fehler.append(f"Elterninfo {sp['code']}: Text fehlt")
            if box.get_attribute("dir") != ("rtl" if sp.get("rtl") else "ltr"):
                fehler.append(f"Elterninfo {sp['code']}: Schreibrichtung falsch")
            overflow(pg, "info_" + sp["code"])
            shot(pg, "info_" + sp["code"])
        pg.reload()
        weg_mit_hinweis(pg)
        if pg.locator(".elterninfo").get_attribute("lang") != data["elterninfo"]["sprachen"][-1]["code"]:
            fehler.append("Elterninfo: Sprachwahl wird nicht gespeichert")

        # Zuhause: Plan speichern
        pg.goto(base + "#/zuhause")
        pg.fill("[data-pf=tier]", "Amsel")
        pg.reload()
        weg_mit_hinweis(pg)
        if pg.input_value("[data-pf=tier]") != "Amsel":
            fehler.append("Zuhause: Plan wird nicht gespeichert")

        # Offline nach erstem Laden
        ctx.set_offline(True)
        pg.goto(base + "#/wissen/e2")
        pg.wait_for_timeout(300)
        if "Sachlich" not in pg.inner_text("main"):
            fehler.append("Offline: App lädt nicht")
        ctx.set_offline(False)
        if errs:
            fehler += ["JS-Fehler: " + e for e in errs[:5]]
        br.close()
    srv.shutdown()
    if fremd:
        fehler.append("Netzanfragen nach außen: " + ", ".join(sorted(set(fremd))[:5]))
    if fehler:
        raise SystemExit("Lernapp – Browsertest fehlgeschlagen:\n  " + "\n  ".join(fehler))
    print(f"ok: Browsertest 390×844 ({len(data['uebungen'])} Übungen gelöst, Tabs, Rätsel, Speichern, offline, keine Netzanfragen)")


def weg_mit_hinweis(pg):
    """Schließt den Hinweis, der bei jedem Öffnen der App erscheint."""
    pg.locator("#popup").wait_for(state="visible", timeout=3000)
    pg.locator("#popOk").click()


def loese_detektiv(pg, u, iv):
    """Ordnet alle Stellen richtig zu; bei der ersten einmal bewusst falsch."""
    ks = [k for _q, a in iv["paare"] for _s, k in MARK.findall(a) if k in u["kuerzel"]]
    if pg.locator(".seg").count() != len(ks):
        raise RuntimeError("Zahl der Stellen stimmt nicht")
    for i, sk in enumerate(ks):
        pg.locator(f".seg[data-s='{i}']").click()
        ziel = "weg" if sk in "WXVU" else sk
        if i == 0:
            falsch = next(o[0] for o in u["optionen"] if o[0] != ziel)
            pg.locator(f"#sheetBody .opt[data-o='{falsch}']").click()
            pg.locator("#sfb .fb.no").wait_for(timeout=2000)
        pg.locator(f"#sheetBody .opt[data-o='{ziel}']").click()
        if i < len(ks) - 1:
            pg.locator("#sfb [data-close]").click()
            pg.wait_for_timeout(30)


def spiele(pg, u, data):
    """Spielt eine Übung mit den richtigen Antworten durch."""
    typ = u["typ"]
    if typ == "auswahl":
        for it in u["items"]:
            if "optionen" in it:
                pg.locator(".opt").nth(it["richtig"]).click()
            else:
                pg.locator(f".opt[data-o='{it['richtig']}']").click()
            pg.locator(".fb.ok").wait_for(timeout=2000)
            pg.locator("#weiter").click()
    elif typ == "detektiv":
        loese_detektiv(pg, u, data["interviews"][u["interview"]])
    elif typ == "beispiel":
        b = data["beispiele"][u["quelle"]]
        for st in b["schritte"]:
            arten = [bl["art"] for bl in st["bloecke"]]
            pg.locator("h2", has_text=st["titel"]).wait_for(timeout=2000)
            if "detektiv" in arten:
                loese_detektiv(pg, u, data["interviews"][b["id"]])
                pg.locator("#fertig .fb.ok").wait_for(timeout=2000)
            if "plan" in arten:
                pg.locator("[data-plan]").click()
                pg.locator("[data-planall]").click()
            if "muster" in arten:
                pg.locator("#muMark").check()
                for c in range(pg.locator("[data-mu]").count()):
                    pg.locator("[data-mu]").nth(c).click()
                    if not pg.locator("#muBox mark.mt").count():
                        raise RuntimeError("Mustertext ohne Markierung")
            while pg.locator("[data-reveal]").count():
                pg.locator("[data-reveal]").first.click()
            pg.locator("#vor").click()
    elif typ == "satzbau":
        for it in u["items"]:
            for t in it["teile"]:
                pg.locator(".pool .tile", has_text=re.compile("^" + re.escape(t) + "$")).first.click()
            pg.locator("#pruefen").click()
            pg.locator(".fb.ok").wait_for(timeout=2000)
            pg.locator("#weiter").click()
    elif typ == "fehlerjagd":
        for it in u["items"]:
            f, r = it["falsch"].split(), it["richtig"].split()
            for k, (a, b) in enumerate(zip(f, r)):
                if a.rstrip(".") != b.rstrip("."):
                    pg.locator(f"[data-w='{k}']").click()
            if not it["falsch"].endswith(".") and it["richtig"].endswith("."):
                pg.locator("[data-w='end']").click()
            pg.locator("#pruefen").click()
            pg.locator(".fb.ok").wait_for(timeout=2000)
            pg.locator("#weiter").click()
    elif typ == "saetze":
        for k, s in enumerate(u["saetze"]):
            if s["ja"]:
                pg.locator(f"[data-s='{k}']").click()
        pg.locator("#pruefen").click()
        pg.locator(".fb.ok").wait_for(timeout=2000)
        pg.locator("#weiter").click()


def main():
    data = daten()
    pruefe_inhalt(data)
    schreiben(data)
    if "--ohne-test" not in sys.argv:
        shots = None
        for a in sys.argv:
            if a.startswith("--bilder="):
                shots = Path(a.split("=", 1)[1])
                shots.mkdir(parents=True, exist_ok=True)
        browsertest(data, shots)


if __name__ == "__main__":
    main()
