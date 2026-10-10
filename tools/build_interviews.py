#!/usr/bin/env python3
"""Interviews als Textbasis (Weg B): Schülerfassung A4 mit Zeilennummern + Lehrkraft-Prüfliste.

Quelle: inhalt/interviews.json. Markierung [[Textstelle|Kürzel]] ist im Schülertext unsichtbar;
sie liefert die Zeilenbelege für Prüfliste, Lösungen und Kiosk.

    python3 tools/build_interviews.py            # Entwurf aller Interviews -> ausgabe/interviews/

render_interview() wird auch von den anderen Generatoren genutzt (Materialseiten, Prüfungen).
"""
from __future__ import annotations

import html
import json
import re
import sys
from collections import Counter
from pathlib import Path

import pymupdf as fitz
from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_material import FUSS, ROOT, b64, font_css, font_sizes  # noqa: E402

QUELLE = ROOT / "inhalt" / "interviews.json"
AUS = ROOT / "ausgabe" / "interviews"
TAG = re.compile(r"\[\[(.+?)\|(\w)\]\]")
KUERZEL = {
    "T": "Tiername / Tiergruppe", "M": "Maß der Art", "A": "Aussehen", "L": "Lebensraum", "N": "Nahrung",
    "W": "Meinung / Wertung", "X": "einzelnes Tier, Erlebnis, Zooalltag", "V": "bildhafter Vergleich",
    "Z": "Zusatz: Verhalten", "U": "Vermutung",
}
REIN = "TMALN"      # gehört in die Tierbeschreibung
RAUS = "WXVU"       # nicht übernehmen (V: höchstens sachlich umformen)
# Mindestabdeckung je Interview (lang / Förder)
MIN_LANG = {"T": 1, "M": 1, "A": 6, "L": 1, "N": 1, "W": 1, "X": 2}
MIN_FOERDER = {"M": 1, "A": 3, "L": 1, "N": 1, "W": 1, "X": 2}


def ohne_tags(s: str) -> str:
    return TAG.sub(r"\1", s)


def woerter(t: dict) -> int:
    return len(" ".join(ohne_tags(q + " " + a) for q, a in t["paare"]).split())


def tags(t: dict) -> list[tuple[str, str]]:
    return [(m.group(2), m.group(1)) for _, a in t["paare"] for m in TAG.finditer(a)]


# ---------------------------------------------------------------- Schülerfassung
def wort_spans(text: str, frage: bool, zaehler: list) -> str:
    """Jedes Wort als <span>; markierte Stellen tragen data-k und data-s (Stellen-Nr.)."""
    tok, pos = [], 0  # [wort, attribute]; Satzzeichen direkt nach einer Stelle hängen am Vorwort

    def add(roh: str, attr: str):
        for i, w in enumerate(re.split(r"(\s+)", roh)):
            if not w or w.isspace():
                continue
            if i == 0 and tok and not (tok[-1][0].endswith(" ")) and pos_glue[0]:
                tok[-1][0] += w
            else:
                tok.append([w, attr])
            pos_glue[0] = False

    pos_glue = [False]
    for m in list(TAG.finditer(text)) + [None]:
        roh = text[pos:m.start()] if m else text[pos:]
        add(roh, " q" if frage else "")
        if m:
            zaehler[0] += 1
            pos_glue[0] = False
            add(m.group(1), "' data-k='%s' data-s='%d" % (m.group(2), zaehler[0]))
            pos_glue[0] = True
            pos = m.end()
    return " ".join("<span class='w%s'>%s</span>" % (a, html.escape(w)) for w, a in tok)


IV_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font-family:'Andika',sans-serif;color:#111;background:#fff;width:178mm;font-size:15pt;line-height:1.45}
@page{size:A4;margin:14mm 16mm 20mm 16mm}
.meta{font-size:14pt;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:#444}
h1{font-size:30pt;line-height:1.15;margin:1mm 0 3mm}
.rahmen{font-size:16pt;margin-bottom:3mm}
.foto{float:right;width:62mm;margin:1mm 0 3mm 5mm;font-size:14pt;color:#444;line-height:1.25}
.foto img{width:auto;max-width:100%;max-height:52mm;border-radius:3mm;display:block;margin-bottom:1mm}
.fiktiv{font-size:14pt;border:1.5pt dashed #111;border-radius:2.5mm;padding:2mm 3mm;margin:0 0 4mm;display:inline-block}
.txt{padding-left:13mm;position:relative}
.par{margin-bottom:2.2mm}.par.q{margin-top:3mm}
.ln{position:relative;break-inside:avoid;white-space:nowrap}
.ln .nr{position:absolute;left:-13mm;width:9mm;text-align:right;font-size:14pt;color:#555}
.q,.w.q{font-weight:700}
.wh{clear:both;break-inside:avoid;font-size:15pt;margin-top:6mm;padding:3mm 4mm;background:#ededed;border-radius:2.5mm}
.wh>b{display:block;font-size:14pt;letter-spacing:.05em;text-transform:uppercase}
.hint{font-size:14pt;color:#444;margin-top:3mm}
.kompakt{line-height:1.4}.kompakt .foto{width:58mm;font-size:14pt;line-height:1.2}.kompakt .foto img{max-height:40mm;width:auto;max-width:100%}.kompakt h1{font-size:26pt;margin-bottom:2mm}.kompakt .fiktiv{margin-bottom:2mm}.kompakt .par.q{margin-top:1.5mm}.kompakt .par{margin-bottom:1mm}.kompakt .wh{margin-top:2mm;padding:2mm 3mm}.kompakt .hint{margin-top:1mm}.kompakt .rahmen{margin-bottom:2mm}.kompakt .meta{font-size:14pt}
"""

ZEILEN_JS = r"""
() => {
  let n = 0; const stellen = {};
  document.querySelectorAll('.par').forEach(p => {
    const ws = [...p.querySelectorAll('.w')]; const zeilen = []; let top = null;
    ws.forEach(w => { const t = Math.round(w.getBoundingClientRect().top);
      if (top === null || Math.abs(t - top) > 4) { zeilen.push([]); top = t; } zeilen[zeilen.length-1].push(w); });
    const neu = zeilen.map(z => { n += 1; const d = document.createElement('div'); d.className = 'ln';
      if (n % 5 === 0) { const s = document.createElement('span'); s.className = 'nr'; s.textContent = n; d.appendChild(s); }
      z.forEach((w, i) => { if (i) d.appendChild(document.createTextNode(' ')); d.appendChild(w);
        if (w.dataset.s) { (stellen[w.dataset.s] ||= {k: w.dataset.k, z: []}); if (!stellen[w.dataset.s].z.includes(n)) stellen[w.dataset.s].z.push(n); } });
      return d; });
    p.replaceChildren(...neu);
  });
  return {zeilen: n, stellen};
}
"""


def interview_html(t: dict, rahmen: str, fiktiv: str, kopf: str, kompakt: bool = False) -> str:
    z = [0]
    pars = []
    for q, a in t["paare"]:
        pars.append("<div class='par q'>%s</div>" % wort_spans(q, True, z))
        pars.append("<div class='par'>%s</div>" % wort_spans(a, False, z))
    wh = ""
    if t.get("woerter"):
        wh = "<div class='wh'><b>Wörterhilfe</b>%s</div>" % "".join(
            "<div><b>%s:</b> %s</div>" % (html.escape(w), html.escape(e)) for w, e in t["woerter"])
    foto = ""
    if (ROOT / t["foto"]).exists():
        foto = "<div class='foto'><img src='data:image/jpeg;base64,%s' alt=''>%s</div>" % (
            b64(ROOT / t["foto"]), html.escape(t["foto_nachweis"]))
    return (
        "<!doctype html><html lang='de'><head><meta charset='utf-8'><style>%s%s</style></head><body class='%s'>"
        "<div class='meta'>%s</div><h1>%s</h1>%s<div class='rahmen'>%s %s</div><div class='fiktiv'>%s</div>"
        "<div class='txt'>%s</div>%s<div class='hint'>Auf diesen Seiten darfst du markieren und unterstreichen.</div>"
        "</body></html>"
        % (font_css(), IV_CSS, "kompakt" if kompakt else "", html.escape(kopf), html.escape(t["titel"]), foto, html.escape(rahmen),
           html.escape(t["einleitung"]), html.escape(fiktiv), "".join(pars), wh)
    )


def render_interview(pg, t: dict, rahmen: str, fiktiv: str, kopf: str, pdf: Path, fuss_rechts: str = "Material", kompakt: bool = False) -> dict:
    """Rendert ein Interview (mehrseitig möglich) und liefert Zeilenzahl + Zeilenbelege je markierter Stelle."""
    pg.set_viewport_size({"width": 900, "height": 1200})
    pg.set_content(interview_html(t, rahmen, fiktiv, kopf, kompakt), wait_until="load")
    pg.evaluate("document.fonts.ready")
    pg.emulate_media(media="print")
    info = pg.evaluate(ZEILEN_JS)
    fuss = ("<div style='font-size:14pt;width:100%%;padding:0 16mm;display:flex;justify-content:space-between;"
            "font-family:DejaVu Sans,sans-serif;color:#444'><span>%s</span>"
            "<span>%s · Seite <span class=pageNumber></span>/<span class=totalPages></span></span></div>"
            % (FUSS, html.escape(fuss_rechts)))
    pg.pdf(path=str(pdf), prefer_css_page_size=True, print_background=True, display_header_footer=True,
           header_template="<span></span>", footer_template=fuss)
    pg.emulate_media(media="screen")
    stellen = [(v["k"], sorted(v["z"])) for _, v in sorted(info["stellen"].items(), key=lambda x: int(x[0]))]
    return {"zeilen": info["zeilen"], "stellen": stellen, "seiten": len(fitz.open(pdf))}


def zeilen_text(z: list[int]) -> str:
    return "Z. %d" % z[0] if len(z) == 1 else "Z. %d–%d" % (z[0], z[-1])


# ---------------------------------------------------------------- Lehrkraft-Prüfliste
PL_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Andika',sans-serif;color:#111;font-size:11pt;line-height:1.35}
@page{size:A4;margin:14mm 15mm 16mm 15mm}
h1{font-size:20pt;margin-bottom:2mm}h2{font-size:15pt;margin:6mm 0 2mm;break-after:avoid}
.info{margin-bottom:3mm}
.leg{display:grid;grid-template-columns:repeat(2,1fr);gap:.5mm 6mm;font-size:10.5pt;margin:2mm 0 4mm;padding:2.5mm 3mm;border:1pt solid #999;border-radius:2mm}
table{width:100%;border-collapse:collapse;font-size:10.5pt;margin-bottom:2mm}
td,th{border-bottom:.6pt solid #bbb;padding:1mm 1.5mm;text-align:left;vertical-align:top}
th{font-size:10pt;text-transform:uppercase;letter-spacing:.04em;border-bottom:1.2pt solid #111}
td.k{font-weight:700;width:9mm;text-align:center}td.z{width:20mm;white-space:nowrap}
tr.raus td{color:#555;font-style:italic}
.ok{font-weight:700}.fehlt{font-weight:700;text-decoration:underline}
.sec+.sec{break-before:page}
"""


def pruefliste_html(daten: list[tuple[dict, dict, bool]]) -> str:
    leg = "".join("<div><b>%s</b> %s%s</div>" % (k, v, " → rein" if k in REIN else (" → nicht übernehmen" if k in RAUS else ""))
                  for k, v in KUERZEL.items())
    teile = []
    for t, info, foerder in daten:
        cnt = Counter(k for k, _ in tags(t))
        soll = MIN_FOERDER if foerder else MIN_LANG
        grenze = (60, 110) if foerder else (250, 350)
        n = woerter(t)
        pruef = ["Wörter: <b>%d</b> (Ziel %d–%d) %s" % (n, *grenze, "<span class=ok>✓</span>" if grenze[0] <= n <= grenze[1] else "<span class=fehlt>prüfen</span>")]
        for k, m in soll.items():
            pruef.append("%s: %d (mind. %d) %s" % (k, cnt.get(k, 0), m, "✓" if cnt.get(k, 0) >= m else "<span class=fehlt>fehlt</span>"))
        rows = "".join(
            "<tr class='%s'><td class=k>%s</td><td class=z>%s</td><td>%s</td></tr>"
            % ("raus" if k in RAUS else "", k, zeilen_text(z), html.escape(s))
            for (k, z), (_, s) in zip(info["stellen"], tags(t)))
        teile.append(
            "<div class=sec><h2>%s · %s</h2><div class=info>%s · %s · %d Zeilen · %d Seite(n)<br>%s</div>"
            "<table><tr><th>K.</th><th>Zeile</th><th>Textstelle</th></tr>%s</table></div>"
            % (html.escape(t["rolle"]), html.escape(t["titel"]), html.escape(t["person"]), t["id"], info["zeilen"],
               info["seiten"], " · ".join(pruef), rows))
    return ("<!doctype html><html lang='de'><head><meta charset='utf-8'><style>%s%s</style></head><body>"
            "<h1>Interviews · Lehrkraft-Prüfliste</h1><div>Zeilenbelege für Lösungen, Kiosk und Bewertung. "
            "Kursiv = gehört nicht in die Tierbeschreibung. Z (Verhalten) darf übernommen werden, ist aber nicht verlangt.</div>"
            "<div class=leg>%s</div>%s</body></html>" % (font_css(), PL_CSS, leg, "".join(teile)))


def main():
    d = json.loads(QUELLE.read_text(encoding="utf-8"))
    AUS.mkdir(parents=True, exist_ok=True)
    tmp = AUS / "_tmp"
    tmp.mkdir(exist_ok=True)
    daten, pdfs, fehler = [], [], []
    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page()
        for foerder, liste in ((False, d["tiere"]), (True, d["foerder"])):
            for t in liste:
                pdf = tmp / ("%s.pdf" % t["id"])
                info = render_interview(pg, t, d["rahmen"], d["hinweis_fiktiv"], "Material · Interview · " + t["rolle"], pdf, kompakt=foerder)
                mn, _ = font_sizes(pdf)
                if mn < 13.95:
                    fehler.append("%s: Schrift %.1f pt" % (t["id"], mn))
                daten.append((t, info, foerder))
                pdfs.append(pdf)
                print("%-18s %3d Wörter  %2d Zeilen  %d S.  min %.1f pt" % (t["id"], woerter(t), info["zeilen"], info["seiten"], mn))
        pl = tmp / "pruefliste.pdf"
        pg.set_content(pruefliste_html(daten), wait_until="load")
        pg.evaluate("document.fonts.ready")
        pg.pdf(path=str(pl), prefer_css_page_size=True, print_background=True)
        br.close()
    out = fitz.open()
    for f in pdfs + [pl]:
        out.insert_pdf(fitz.open(f))
    zl = {t["id"]: [[k, zeilen_text(z), s] for (k, z), (_, s) in zip(info["stellen"], tags(t))] for t, info, _ in daten}
    (AUS / "zeilen.json").write_text(json.dumps(zl, ensure_ascii=False, indent=1), encoding="utf-8")
    ziel = AUS / "Interviews_Entwurf_A4.pdf"
    out.save(ziel)
    for f in tmp.iterdir():
        f.unlink()
    tmp.rmdir()
    print("→", ziel.relative_to(ROOT), len(out), "Seiten")
    for f in fehler:
        print("FEHLER", f)


if __name__ == "__main__":
    main()
