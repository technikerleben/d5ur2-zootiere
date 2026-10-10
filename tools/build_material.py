#!/usr/bin/env python3
"""Erzeugt alle Materialien einer Etappe aus inhalt/etappeN.json.

Ausgabe in ausgabe/etappeN/:
  Input_EtappeN.html            HTML-Präsentation (eine Datei, offline)
  Merkblatt_N_A4.pdf            A4, Originalgröße drucken
  Uebungsblaetter_EtappeN_A4.pdf  A4 gesetzt, auf A5 verkleinert drucken (mind. 14 pt)
  GN{N}_A_A4.pdf / GN{N}_B_A4.pdf  A4 mit Rückmeldeseite

Aufruf: python tools/build_material.py 1
Prüft dabei: Seitenüberlauf, Mindestschriftgrößen, 1:1-Gleichheit Input/Merkblatt.
"""
import base64
import html
import json
import re
import sys
from pathlib import Path

import pymupdf as fitz
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "assets" / "fonts"
FUSS = "Deutsch · Jahrgang 5 · Zootiere"

# Mindestschriftgrößen (pt) je Ausgabe; Rückmeldeseite der Nachweise ist Lehrkraftteil.
MIN_PT = {"merkblatt": 12.0, "uebung": 14.0, "nachweis_aufgaben": 14.0}


# ---------------------------------------------------------------- Hilfen
def b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()


def font_css() -> str:
    out = []
    for weight, style in [(400, "normal"), (700, "normal"), (400, "italic"), (700, "italic")]:
        f = FONTS / f"andika-latin-{weight}-{style}.woff2"
        out.append(
            "@font-face{font-family:'Andika';font-weight:%d;font-style:%s;"
            "src:url(data:font/woff2;base64,%s) format('woff2');}" % (weight, style, b64(f))
        )
    return "\n".join(out)


def svg_uri(rel: str) -> str:
    return "data:image/svg+xml;base64," + b64(ROOT / rel)


def md(text: str) -> str:
    """Minimales Markup: **fett**, *kursiv*, Zeilenumbruch."""
    t = html.escape(text, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"\*(.+?)\*", r"<em>\1</em>", t)
    return t.replace("\n", "<br>")


def plain(text: str) -> str:
    t = re.sub(r"<[^>]+>", " ", text)
    t = html.unescape(t).replace("*", "")
    return re.sub(r"\s+", " ", t).strip()


BASE_CSS = """
:root{--ink:#111;--mid:#444;--soft:#777;--line:#999;--fill:#ededed;}
*{box-sizing:border-box;margin:0;padding:0}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font-family:'Andika',sans-serif;color:var(--ink);background:#fff}
em{font-style:italic}
strong{font-weight:700}
.page{width:210mm;height:297mm;overflow:hidden;page-break-after:always;break-after:page;
  display:flex;flex-direction:column;position:relative}
.page:last-child{page-break-after:auto;break-after:auto}
.grow{flex:1 1 auto;min-height:0}
.foot{display:flex;justify-content:space-between;align-items:flex-end;border-top:1.5pt solid var(--ink);
  padding-top:2.5mm;flex:0 0 auto}
.box{border:1.5pt solid var(--ink);border-radius:3mm}
.dashed{border:1.5pt dashed var(--ink);border-radius:3mm}
.lines{display:flex;flex-direction:column}
.line{border-bottom:1pt solid var(--soft);height:11mm}
.cb{display:inline-block;width:5.5mm;height:5.5mm;border:1.4pt solid var(--ink);border-radius:1mm;
  vertical-align:-1mm;margin-right:2mm}
"""


def doc(body: str, css: str, title: str) -> str:
    return (
        "<!doctype html><html lang='de'><head><meta charset='utf-8'><title>%s</title>"
        "<style>%s\n@page{size:A4;margin:0}%s%s</style></head><body>%s</body></html>"
        % (html.escape(title), font_css(), BASE_CSS, css, body)
    )


# ---------------------------------------------------------------- Merkblatt A4
MB_CSS = """
.page{padding:13mm 15mm 10mm 15mm;font-size:13.5pt;line-height:1.36}
.kopf{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2.5pt solid var(--ink);padding-bottom:3mm;margin-bottom:4mm}
.kopf .mb{font-size:12.5pt;font-weight:700;letter-spacing:.06em;text-transform:uppercase}
.kopf h1{font-size:23pt;line-height:1.1;margin-top:1mm}
.kopf .ziel{max-width:75mm;font-size:12.5pt;text-align:right;color:var(--mid)}
.kopf .ziel b{display:block;color:var(--ink);text-transform:uppercase;letter-spacing:.05em;font-size:12pt}
.cols{column-count:2;column-gap:8mm;column-fill:auto}
.sec{margin-bottom:4mm}
.sec h2{break-after:avoid;font-size:16.5pt;display:flex;gap:2.5mm;align-items:center;margin-bottom:2mm}
.sec h2 .n{display:inline-flex;width:8mm;height:8mm;border-radius:50%;background:var(--ink);color:#fff;
  font-size:12.5pt;align-items:center;justify-content:center;flex:0 0 auto}
.blk{margin-bottom:2mm;break-inside:avoid}
.foto,.cred{break-after:avoid;break-inside:avoid}
.blk .lab{font-weight:700}
.blk.ans{border-left:3pt solid var(--ink);background:var(--fill);padding:1.5mm 2.5mm;border-radius:0 2mm 2mm 0}
.page.eng{font-size:12.4pt;line-height:1.3}.eng .sec{margin-bottom:3.5mm}.eng .sec h2{font-size:15pt}.eng .foto{max-height:62mm;object-fit:contain}
.blk.frage{break-after:avoid}
.blk.frage .lab::before{content:"? ";}
.foto{width:100%;max-height:50mm;object-fit:contain;object-position:left;border-radius:2mm;display:block;margin-bottom:1mm}
.cred{font-size:12pt;color:var(--mid);margin-bottom:2mm}
.abschluss{border:1.5pt solid var(--ink);border-radius:3mm;padding:2mm 3.5mm;margin-bottom:4mm}
.abschluss b{margin-right:2mm}
.foot{font-size:12pt;color:var(--mid);border-top-width:1pt;margin-top:3mm}
"""


def mb_section(i: int, s: dict, foto_b64: str, foto: dict) -> str:
    h = ["<section class='sec'><h2><span class='n'>%d</span>%s</h2>" % (i, md(s["titel"]))]
    if s.get("foto"):
        h.append("<img class='foto' src='data:image/jpeg;base64,%s' alt='%s'>" % (foto_b64, html.escape(foto["alt"])))
        h.append("<div class='cred'>%s</div>" % html.escape(foto["nachweis"]))
    if s.get("grafik"):
        h.append("<img class='foto' src='%s' alt='%s'>" % (svg_uri(s["grafik"]), html.escape(s.get("grafik_alt", ""))))
    for lab, txt in s["bloecke"]:
        cls = "ans" if lab.startswith("Gesicherte Antwort") else ("frage" if lab == "Frage" else "")
        h.append("<div class='blk %s'><span class='lab'>%s:</span> %s</div>" % (cls, md(lab), md(txt)))
    h.append("</section>")
    return "".join(h)


def merkblatt_html(c: dict, fs: float) -> str:
    """Fließender zweispaltiger Satz über die Seiten; Fußzeile über die Druckvorlage."""
    foto_b64 = b64(ROOT / c["foto"]["datei"])
    secs = "".join(mb_section(i + 1, s, foto_b64, c["foto"]) for i, s in enumerate(c["input"]))
    absch = "<div class='abschluss'><b>Deine Etappe:</b>%s</div>" % md(c["abschluss"])
    kopf = (
        "<div class='kopf'><div><div class='mb'>Merkblatt %d · zum Nachlesen</div><h1>%s</h1></div>"
        "<div class='ziel'><b>Dein Ziel</b>%s</div></div>" % (c["etappe"], md(c["titel"]), md(c["ziel"]))
    )
    css = MB_CSS + "\n.flow{font-size:%.1fpt;line-height:1.34}.flow .cols{height:auto}" % fs
    return doc("<div class='flow'>%s%s<div class='cols'>%s</div></div>" % (kopf, absch, secs), css, "Merkblatt %d" % c["etappe"]).replace(
        "@page{size:A4;margin:0}", "@page{size:A4;margin:13mm 15mm 17mm 15mm}")


def merkblatt_render(pg, c: dict, pdf: Path) -> int:
    fuss = ("<div style='font-size:12pt;width:100%%;padding:0 15mm;display:flex;justify-content:space-between;"
            "font-family:DejaVu Sans,sans-serif;color:#555'><span>%s · Etappe %d</span>"
            "<span>Merkblatt %d · Seite <span class=pageNumber></span>/<span class=totalPages></span></span></div>"
            % (FUSS, c["etappe"], c["etappe"]))
    for fs in (13.5, 13.0, 12.4, 12.0):
        pg.set_content(merkblatt_html(c, fs), wait_until="load")
        pg.evaluate("document.fonts.ready")
        pg.pdf(path=str(pdf), prefer_css_page_size=True, print_background=True, display_header_footer=True,
               header_template="<span></span>", footer_template=fuss)
        n = len(fitz.open(pdf))
        if n <= 2:
            return n
    return n


# ---------------------------------------------------------------- Übungsblätter (A4, ≥14 pt)
UB_CSS = """
.page{padding:14mm 16mm 11mm 16mm;font-size:17pt;line-height:1.38}
.ukopf{display:flex;gap:6mm;align-items:center;margin-bottom:6mm}
.nr{flex:0 0 auto;width:30mm;height:30mm;border:2.5pt solid var(--ink);border-radius:4mm;display:flex;flex-direction:column;
  align-items:center;justify-content:center;line-height:1}
.nr span{font-size:14pt;font-weight:700;letter-spacing:.06em;text-transform:uppercase}
.nr b{font-size:40pt}
.ukopf .meta{font-size:14pt;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--mid)}
.ukopf h1{font-size:31pt;line-height:1.1}
.brauch{font-size:16pt;margin-bottom:6mm;padding:2.5mm 4mm;background:var(--fill);border-radius:2.5mm}
.brauch b{margin-right:2mm}
.teil{margin-bottom:6mm;padding:4mm 5mm 4.5mm}
.teil h2{font-size:18pt;display:flex;align-items:center;gap:3mm;margin-bottom:2.5mm}
.tag{font-size:14pt;font-weight:700;letter-spacing:.05em;text-transform:uppercase;padding:1mm 3mm;border-radius:1.5mm}
.tag.p{background:var(--ink);color:#fff}
.tag.f{border:1.5pt dashed var(--ink)}
ol.auf{padding-left:9mm}
ol.auf li{margin-bottom:2.5mm;padding-left:1mm}
.lies{border-left:3pt solid var(--ink);padding:1mm 0 1mm 4mm;margin-bottom:6mm}
.lies b{display:block;font-size:14pt;letter-spacing:.05em;text-transform:uppercase;margin-bottom:1mm}
.tipp{font-size:16pt;padding:3mm 4mm;border-radius:2.5mm;background:var(--fill);margin-bottom:6mm}
.tipp b{margin-right:2mm}
.foot{font-size:14pt;color:var(--mid)}
.eng{font-size:15.5pt;line-height:1.32}
.eng .ukopf{margin-bottom:4mm}.eng .nr{width:25mm;height:25mm}.eng .nr b{font-size:34pt}.eng .ukopf h1{font-size:27pt}
.eng .brauch{margin-bottom:4mm;font-size:14pt}.eng .lies{margin-bottom:4mm}
.eng .teil{margin-bottom:4mm;padding:3mm 4.5mm 3.5mm}.eng .teil h2{font-size:16pt;margin-bottom:1.5mm}
.eng ol.auf li{margin-bottom:1.5mm}
.enger{font-size:14.5pt;line-height:1.28}.enger .teil{margin-bottom:3mm}
.mat h1{font-size:34pt;margin-bottom:5mm}
.mat .meta{font-size:14pt;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--mid);margin-bottom:1mm}
.mat img{max-width:100%;height:100mm;width:auto;object-fit:contain;border-radius:3mm;display:block;margin:0 auto}
.mat.lang img{height:73mm}
.mat.lang .txt{font-size:16pt;line-height:1.45;padding:4mm 5mm}
.mat.lang .cred{margin-bottom:4mm}
.wh{font-size:15pt;margin-top:4mm;padding:3mm 4mm;background:var(--fill);border-radius:2.5mm}.wh>b{display:block;font-size:14pt;letter-spacing:.05em;text-transform:uppercase}
.cbl{display:flex;gap:2mm;align-items:flex-start}.cbl .cb{flex:0 0 auto;margin-top:1.2mm}
.mat .cred{font-size:14pt;color:var(--mid);margin:2mm 0 6mm}
.mat img.gross{height:150mm}
.mat .txt{font-size:19pt;line-height:1.6;padding:5mm 6mm}
.mat .hint{font-size:14pt;color:var(--mid);margin-top:3mm}
"""


def blatt_page(c: dict, b: dict, dicht: int = 0) -> str:
    h = ["<div class='page%s'><div class='grow'>" % ("", " eng", " eng enger")[dicht]]
    h.append(
        "<div class='ukopf'><div class='nr'><span>Blatt</span><b>%d</b></div><div><div class='meta'>Etappe %d · Pflicht + freiwillige Vertiefung</div>"
        "<h1>%s</h1></div></div>" % (b["nr"], c["etappe"], md(b["titel"]))
    )
    h.append("<div class='brauch'><b>Du brauchst:</b>%s</div>" % md(b["brauchst"]))
    if b.get("lies"):
        h.append("<div class='lies'><b>Lies</b>%s</div>" % md(b["lies"]))
    if b.get("material"):
        h.append("<div class='lies'><b>%s</b>%s</div>" % (md(b["material"]["titel"]), md(b["material"]["text"])))
    if b.get("teile"):
        # Allgemeine Form: mehrere Pflicht- und freiwillige Teile
        for t in b["teile"]:
            frei = t["art"] == "frei"
            h.append("<div class='teil %s'><h2><span class='tag %s'>%s</span>%s</h2>"
                     % ("dashed" if frei else "box", "f" if frei else "p", "Freiwillig" if frei else "Pflicht", md(t["titel"])))
            if t.get("text"):
                h.append("<div>%s</div>" % md(t["text"]))
            if t.get("aufgaben"):
                h.append("<ol class='auf' start='%d'>" % t.get("start", 1))
                h += ["<li>%s</li>" % md(x) for x in t["aufgaben"]]
                h.append("</ol>")
            if t.get("nachtext"):
                h.append("<div>%s</div>" % md(t["nachtext"]))
            h.append("</div>")
        if b.get("tipp"):
            h.append("<div class='tipp'><b>Achte darauf:</b>%s</div>" % md(b["tipp"]))
        h.append("</div><div class='foot'><span>%s · Etappe %d</span><b>Blatt %d</b></div></div>" % (FUSS, c["etappe"], b["nr"]))
        return "".join(h)
    h.append("<div class='teil box'><h2><span class='tag p'>Pflicht</span>Schreibe ins Heft</h2><ol class='auf'>")
    h += ["<li>%s</li>" % md(x) for x in b["pflicht"]]
    h.append("</ol></div>")
    if b.get("sprachdetektiv"):
        h.append("<div class='teil box'><h2><span class='tag p'>Pflicht</span>Sprachdetektiv</h2>%s</div>" % md(b["sprachdetektiv"]))
    if b.get("tipp"):
        h.append("<div class='tipp'><b>Achte darauf:</b>%s</div>" % md(b["tipp"]))
    if b.get("vertiefung"):
        h.append("<div class='teil dashed'><h2><span class='tag f'>Freiwillig</span>Vertiefung</h2>%s</div>" % md(b["vertiefung"]))
    h.append(
        "</div><div class='foot'><span>%s · Etappe %d</span><b>Blatt %d</b></div></div>" % (FUSS, c["etappe"], b["nr"])
    )
    return "".join(h)


def materialien(c: dict) -> list:
    if c.get("materialien"):
        return c["materialien"]
    if c.get("material"):
        return [dict(c["material"], foto=c["foto"])]
    return []


def woerter_html(m: dict) -> str:
    if not m.get("woerter"):
        return ""
    return "<div class='wh'><b>Wörterhilfe</b>%s</div>" % "".join(
        "<div><b>%s:</b> %s</div>" % (md(w), md(e)) for w, e in m["woerter"])


def bildseite(c: dict) -> str:
    f, bs = c["foto"], c["bildseite"]
    return (
        "<div class='page mat'><div class='grow'><div class='meta'>Material · Foto · Etappe %d</div><h1>%s</h1>"
        "<img class='gross' src='data:image/jpeg;base64,%s' alt='%s'><div class='cred'>%s</div>"
        "<div class='txt box'>%s</div><div class='hint'>Auf dieser Seite darfst du markieren und einkreisen.</div></div>"
        "<div class='foot'><span>%s · Etappe %d</span><b>Material</b></div></div>"
        % (c["etappe"], md(bs["titel"]), b64(ROOT / f["datei"]), html.escape(f["alt"]), html.escape(f["nachweis"]),
           md(bs["hinweis"]), FUSS, c["etappe"]))


def build_materialbasis(pg, c: dict, pdf: Path, ueberlauf: list) -> tuple:
    """Materialbasis einer Etappe: ggf. Fotoseite, dann die Interviews (mehrseitig, Zeilennummern)."""
    from build_interviews import QUELLE, render_interview
    iv = json.loads(QUELLE.read_text(encoding="utf-8"))
    alle = {t["id"]: t for t in iv["tiere"] + iv["foerder"]}
    teile = []
    tmp = pdf.with_suffix(".tmp")
    tmp.mkdir(exist_ok=True)
    if c.get("bildseite"):
        f = tmp / "0.pdf"
        o = render(pg, doc(bildseite(c), UB_CSS, "Foto"), f)
        if o:
            ueberlauf.append("Fotoseite: Überlauf")
        teile.append(f)
    for k, i in enumerate(c["interviews"], 1):
        f = tmp / ("%d.pdf" % k)
        kopf = c.get("interview_kopf", "Material · Interview · Etappe %s" % c.get("etappe", ""))
        render_interview(pg, alle[i], iv["rahmen"], iv["hinweis_fiktiv"], kopf, f, kompakt=c.get("kompakt", False))
        teile.append(f)
    out = fitz.open()
    for f in teile:
        out.insert_pdf(fitz.open(f))
        f.unlink()
    tmp.rmdir()
    out.save(pdf)
    return font_sizes(pdf)


def material_page(c: dict, m: dict) -> str:
    nrs = [b["nr"] for b in c["blaetter"]]
    rng = "%d–%d" % (nrs[0], nrs[-1]) if len(nrs) > 1 else str(nrs[0])
    f = m["foto"]
    lang = " lang" if len(m["text"]) > 500 or m.get("woerter") else ""
    hint = m.get("bildhinweis", "")
    return (
        "<div class='page mat%s'><div class='grow'><div class='meta'>Material zu Blatt %s</div><h1>%s</h1>"
        "<img src='data:image/jpeg;base64,%s' alt='%s'><div class='cred'>%s%s</div>"
        "<div class='txt box'>%s</div>%s<div class='hint'>Auf dieser Seite darfst du markieren und unterstreichen.</div></div>"
        "<div class='foot'><span>%s · Etappe %d</span><b>Material</b></div></div>"
        % (lang, rng, md(m["titel"]), b64(ROOT / f["datei"]), html.escape(f["alt"]), html.escape(f["nachweis"]),
           ("<br>" + md(hint)) if hint else "", md(m["text"]), woerter_html(m), FUSS, c["etappe"])
    )


def zusatz_page(c: dict, z: dict, k: int, n: int) -> str:
    h = ["<div class='page'><div class='grow'><div class='ukopf'><div><div class='meta'>%s K1–K6 · Seite %d/%d</div><h1>%s</h1></div></div>"
         % (md(z["kennung"]), k, n, md(z["titel"]))]
    for t in z["teile"]:
        h.append("<div class='teil box'><h2>%s</h2><div class='cbl'><span class='cb'></span><span>%s</span></div></div>" % (md(t["titel"]), md(t["text"])))
    h.append("</div><div class='foot'><span>%s · Etappe %d</span><b>%s %d/%d</b></div></div>" % (FUSS, c["etappe"], md(z["kennung"]), k, n))
    return "".join(h)




# ---------------------------------------------------------------- Hilfekarten und Raumschild
HK_CSS = UB_CSS + """
.hk .hin{font-size:17pt;font-weight:700;padding:3mm 4mm;border:2pt solid var(--ink);border-radius:2.5mm;margin-bottom:5mm}
table.wt{width:100%;border-collapse:collapse;margin-bottom:5mm;font-size:16pt}
table.wt th{text-align:left;font-size:14pt;text-transform:uppercase;letter-spacing:.05em;border-bottom:2pt solid var(--ink);padding:1.5mm 2mm}
table.wt td{border-bottom:1pt solid var(--line);padding:2mm;vertical-align:top}
table.wt td:first-child{font-weight:700;width:38%}
.hk .liste{margin-bottom:4.5mm}
.hk .liste b{display:block;font-size:15pt;text-transform:uppercase;letter-spacing:.05em;margin-bottom:1mm}
.hk .liste div{font-size:16pt;line-height:1.4}
.hk .acht{font-size:15pt;padding:3mm 4mm;background:var(--fill);border-radius:2.5mm}
.schild{align-items:center;justify-content:center;text-align:center}
.schild .h{width:120mm;height:120mm;border-radius:50%;border:8mm solid var(--ink);display:flex;align-items:center;justify-content:center;
  font-size:150pt;font-weight:700;margin:20mm auto 12mm;line-height:1}
.schild h1{font-size:54pt;line-height:1.05}
.schild .u{font-size:30pt;margin-top:4mm}
.schild .z{font-size:22pt;line-height:1.5;margin-top:14mm}
"""


def hilfe_page(c: dict, h: dict) -> str:
    out = ["<div class='page hk'><div class='grow'><div class='ukopf'><div><div class='meta'>%s · Etappe %d</div><h1>%s</h1></div></div>"
           % (md(h["kennung"]), c["etappe"], md(h["titel"]))]
    out.append("<div class='hin'>%s</div>" % md(h["hinweis"]))
    if h.get("tabelle"):
        t = h["tabelle"]
        out.append("<table class='wt'><tr>%s</tr>%s</table>" % ("".join("<th>%s</th>" % md(x) for x in t["kopf"]),
                   "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % md(x) for x in r) for r in t["zeilen"])))
    for tit, txt in h.get("listen", []):
        out.append("<div class='liste'><b>%s</b><div>%s</div></div>" % (md(tit), md(txt)))
    if h.get("achtung"):
        out.append("<div class='acht'>%s</div>" % md(h["achtung"]))
    out.append("</div><div class='foot'><span>%s · Etappe %d</span><b>%s</b></div></div>" % (FUSS, c["etappe"], md(h["kennung"])))
    return "".join(out)


def schild_page(c: dict, sc: dict) -> str:
    return ("<div class='page schild'><div class='grow'><div class='h'>H</div><h1>%s</h1><div class='u'>%s</div><div class='z'>%s</div></div>"
            "<div class='foot' style='width:100%%'><span>%s · Etappe %d</span><b>Raumschild · A4 in Originalgröße</b></div></div>"
            % (md(sc["titel"]), md(sc["untertitel"]), "<br>".join(md(z) for z in sc["zeilen"]), FUSS, c["etappe"]))


# ---------------------------------------------------------------- Gelingensnachweis A4
GN_CSS = """
.page{padding:12mm 15mm 9mm 15mm;font-size:14pt;line-height:1.3}
.gkopf{display:flex;justify-content:space-between;align-items:flex-start;border-bottom:2.5pt solid var(--ink);padding-bottom:2.5mm;margin-bottom:3mm}
.gkopf .meta{font-size:14pt;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--mid)}
.gkopf h1{font-size:26pt;line-height:1.1}
.gkopf .var{font-size:14pt;font-weight:700;border:2pt solid var(--ink);border-radius:2mm;padding:1mm 3mm;white-space:nowrap}
.namen{display:flex;gap:6mm;font-size:14pt;margin-bottom:3.5mm}
.namen div{flex:1;border-bottom:1pt solid var(--ink);padding-bottom:1mm}
.namen div.d{flex:0 0 55mm}
.matbox{display:flex;gap:5mm;padding:3mm;margin-bottom:3mm}
.matbox img{width:48mm;height:40mm;object-fit:cover;border-radius:2mm;flex:0 0 auto}
.matbox .t{font-size:14pt;line-height:1.38}
.matbox .cred{font-size:14pt;color:var(--mid);margin-top:1mm}
.auf{padding:2.2mm 4mm 2.6mm;margin-bottom:2.1mm}
.auf h2{font-size:16pt;display:flex;gap:3mm;align-items:center;margin-bottom:1mm}
.auf h2 .n{display:inline-flex;width:8.5mm;height:8.5mm;border-radius:50%;background:var(--ink);color:#fff;font-size:14pt;
  align-items:center;justify-content:center}
.feld{display:flex;align-items:flex-end;gap:3mm;margin-top:1mm;font-size:14pt}
.feld .lab{flex:0 0 auto;font-weight:700}
.feld .ln{flex:1;border-bottom:1pt solid var(--soft);height:9.5mm}
.zwei{display:flex;gap:6mm}
.zwei>div{flex:1}
.zwei .h{font-weight:700;font-size:14pt;border-bottom:1.5pt solid var(--ink);margin-top:2mm}
.zwei .ln{border-bottom:1pt solid var(--soft);height:9.5mm}
.wg{margin-top:2mm;font-size:15pt}
.wn{display:inline-block;width:7mm;font-weight:700}
.zielinfo{font-size:14pt;padding:2.5mm 4mm;background:var(--fill);border-radius:2.5mm}
.foot{font-size:14pt;color:var(--mid)}
/* Rückmeldeseite (Lehrkraftteil) */
.rm h1{font-size:23pt}

table.ziele{width:100%;border-collapse:collapse;margin:1mm 0 4mm;font-size:14pt}
table.ziele th{font-size:11pt;vertical-align:bottom;text-align:left;letter-spacing:.04em;text-transform:uppercase;border-bottom:2pt solid var(--ink);padding:1.5mm 2mm}
table.ziele td{border-bottom:1pt solid var(--line);padding:1.3mm 1.5mm;vertical-align:top}
table.ziele td.c{text-align:center;width:17mm}
table.ziele td.u{width:19mm;font-size:13pt}
table.ziele td.e{width:27mm}
.krit{display:block;font-size:10.5pt;line-height:1.25;color:var(--mid);margin-top:.5mm}
.id{font-weight:700}
.ergebnis{display:flex;gap:6mm;align-items:stretch;margin-bottom:4mm}
.ergebnis .sum{flex:0 0 52mm;padding:3mm 4mm;font-size:14pt}
.ergebnis .sum b{font-size:26pt;display:block;letter-spacing:.05em}
.ergebnis .ent{flex:1;padding:2.5mm 4mm;font-size:14pt;display:flex;flex-direction:column;gap:1.5mm;justify-content:center}
.fb{margin-bottom:2.5mm}
.fb .h{font-weight:700;font-size:15pt}
.fb .ln{border-bottom:1pt solid var(--soft);height:9mm}
.sig{display:flex;gap:6mm;font-size:13pt;margin-top:3mm}
.sig div{flex:1;border-bottom:1pt solid var(--ink);padding-bottom:1mm}
"""


def gn_felder(feld: str, v: dict) -> str:
    if feld == "saetze":
        return "".join(
            "<div class='wg'><span class='wn'>%d.</span><em>%s</em></div><div class='feld'><span class='ln'></span></div>"
            "<div class='feld'><span class='ln'></span></div>" % (i, md(w)) for i, w in enumerate(v["wortgruppen"], 1)
        )
    if feld == "verbessern":
        return (
            "<div class='wg'><em>„%s“</em></div><div class='wg'><b>%s:</b> <em>%s</em></div>"
            "<div class='feld'><span class='ln'></span></div><div class='feld'><span class='ln'></span></div>"
            % (md(v["verbessern"]["satz"]), v["verbessern"].get("label", "Material"), md(v["verbessern"]["material"]))
        )
    if feld == "merkmale":
        return (
            "<div class='feld'><span class='lab'>Aus dem Bild:</span><span class='ln'></span></div>"
            "<div class='feld'><span class='lab'>Aus dem Text:</span><span class='ln'></span></div>"
        )
    if feld == "mass" and v.get("mass"):
        m = v["mass"]
        return (
            "<div class='feld'><span class='lab'>%s</span><span class='ln'></span></div>"
            "<div class='feld'><span class='lab'>%s</span>"
            "<span><span class='cb'></span>%s &nbsp; <span class='cb'></span>%s</span></div>"
            % (md(m[0]), md(m[1]), md(m[2]), md(m[3])))
    if feld == "mass":
        return (
            "<div class='feld'><span class='lab'>Kopf und Rumpf:</span><span class='ln'></span></div>"
            "<div class='feld'><span class='lab'>Der Schwanz wird mitgezählt:</span>"
            "<span><span class='cb'></span>ja &nbsp; <span class='cb'></span>nein</span></div>"
        )
    if feld == "ordnen":
        return (
            "<div class='zwei'><div><div class='h'>Lebensraum</div><div class='ln'></div></div>"
            "<div><div class='h'>Nahrung</div><div class='ln'></div></div></div>"
        )
    return "<div class='feld'><span class='ln'></span></div>"


def gn_pages(c: dict, var: str) -> str:
    n = c["nachweis"]
    e = c["etappe"]
    v = n["varianten"][var]
    kurz = ", ".join(z["kurz"] for z in n["ziele"])
    p1 = [
        "<div class='page'><div class='grow'>",
        "<div class='gkopf'><div><div class='meta'>Gelingensnachweis %d · Etappe %d</div><h1>%s</h1></div><div class='var'>Nachweis %d%s</div></div>"
        % (e, e, md(n["titel"]), e, var),
        "<div class='namen'><div>Name:</div><div class='d'>Datum:</div></div>",
    ]
    if v.get("text"):
        p1.append(
            "<div class='matbox box'><img src='data:image/jpeg;base64,%s' alt='%s'><div><div class='t'>%s</div><div class='cred'>%s</div></div></div>"
            % (b64(ROOT / c["foto"]["datei"]), html.escape(c["foto"]["alt"]), md(v["text"]), html.escape(c["foto"]["nachweis"])))
    for i, a in enumerate(n["aufgaben"], 1):
        p1.append(
            "<div class='auf box'><h2><span class='n'>%d</span>%s</h2>%s%s</div>"
            % (i, md(a["titel"]), md(a["text"]), gn_felder(a["feld"], v))
        )
    p1.append(
        "<div class='zielinfo'>%s<b>Fünf Ziele:</b> %s. Vier von fünf = 80 %%. Dann gehst du weiter. Es gibt keine Note.</div>"
        % (("<b>%s</b> " % md(n["vor_zielen"])) if n.get("vor_zielen") else "", kurz)
    )
    p1.append("</div><div class='foot'><span>%s · Etappe %d</span><b>Nachweis %d%s · Seite 1</b></div></div>" % (FUSS, e, e, var))

    rows = "".join(
        "<tr><td><span class='id'>%s</span> %s<span class='krit'>Erreicht, wenn: %s</span></td>"
        "<td class='c'><span class='cb'></span></td><td class='c'><span class='cb'></span></td>"
        "<td class='u'>%s</td><td class='e'></td></tr>"
        % (z["id"], md(z["kind"]), md(z["lehrkraft"]), md(z["ueben"]))
        for z in n["ziele"]
    )
    nxt = "Etappe %d" % (e + 1) if e < 3 else "die Wahlzeit"
    p2 = (
        "<div class='page rm'><div class='grow'>"
        "<div class='gkopf'><div><div class='meta'>Rückmeldung der Lehrkraft</div><h1>So weit bist du</h1></div><div class='var'>Nachweis %d%s</div></div>"
        "<table class='ziele'><tr><th>Ziel</th><th>gezeigt</th><th>noch offen</th><th>Übe mit</th><th>erneut gezeigt am</th></tr>%s</table>"
        "<div class='ergebnis'><div class='sum box'>Ergebnis<b>___ / 5</b>Ziele gezeigt</div>"
        "<div class='ent box'><div><span class='cb'></span><b>4 oder 5 Ziele:</b> Du gehst weiter zu %s.</div>"
        "<div><span class='cb'></span><b>Weniger als 4:</b> Übe die offenen Ziele. Dann zeigst du sie noch einmal.</div>"
        "<div class='sig'><div>Lehrkraft:</div><div>Datum:</div></div></div></div>"
        "<div class='fb'><div class='h'>Das gelingt dir schon:</div><div class='ln'></div><div class='ln'></div></div>"
        "<div class='fb'><div class='h'>Dein nächster Schritt:</div><div class='ln'></div><div class='ln'></div></div>"
        "</div><div class='foot'><span>%s · Etappe %d</span><b>Nachweis %d%s · Seite 2</b></div></div>"
        % (e, var, rows, nxt, FUSS, e, e, var)
    )
    return "".join(p1) + p2



# ---------------------------------------------------------------- Probearbeit / Klassenarbeit (A4)
# Aufbau nach der Lernerfolgskontrolle der Reihe Wunschbriefe:
# Auftrag → Material → Planung → Schreibseite → Das zählt → Hilfe → Rückmeldung
PR_CSS = GN_CSS + """
.pk h2{font-size:17pt;margin:4mm 0 1.5mm}
.pk .sit{font-size:15pt;line-height:1.4}
.al{list-style:none}
.al li{display:flex;gap:2.5mm;align-items:flex-start;margin-bottom:1.8mm;font-size:15pt}
.al li .cb{flex:0 0 auto;margin-top:1.3mm}
.hw{font-size:14pt;padding:3mm 4mm;background:var(--fill);border-radius:2.5mm;margin-top:4mm}
.hw div+div{margin-top:1.5mm}
.zeit{font-size:14pt;margin-bottom:2mm}
.pm img{display:block;margin:0 auto;height:72mm;width:auto;max-width:100%;border-radius:2mm}
.pm .cred{font-size:14pt;color:var(--mid);text-align:center;margin:1.5mm 0 3mm}
.pm .bh{font-size:14pt;font-weight:700;text-align:center;margin-bottom:3mm}
.pm .txt{font-size:15pt;line-height:1.5;padding:3.5mm 4.5mm}
.pp .fh{font-weight:700;font-size:16pt;border-bottom:2pt solid var(--ink);margin-top:5mm;padding-bottom:.5mm}
.pp .zl{display:flex;align-items:flex-end;gap:3mm;font-size:14pt}
.pp .zl .lab{flex:0 0 52mm;color:var(--mid)}
.pp .zl .ln{flex:1;border-bottom:1pt solid var(--soft);height:11.5mm}
.sb{flex:1 1 0;min-height:40mm;margin-top:1mm;overflow:hidden;display:flex;flex-direction:column}
.sb .l{flex:0 0 11mm;border-bottom:1pt solid var(--soft)}
.sw{display:flex;flex-direction:column;height:100%}
.ueb{display:flex;align-items:flex-end;gap:3mm;font-size:15pt;font-weight:700;margin-top:2mm}
.ueb .ln{flex:1;border-bottom:1.4pt solid var(--ink);height:11mm}
.pz .kr{display:flex;gap:3mm;align-items:flex-start;padding:2.4mm 0;border-bottom:1pt solid var(--line);font-size:15pt}
.pz .kr .cb{flex:0 0 auto;margin-top:1.3mm}
.ph .blk{margin-top:4mm;font-size:15pt}
.ph .blk>b{display:block;font-size:16pt;margin-bottom:1mm}
.mini{display:flex;flex-wrap:wrap;gap:1.5mm 6mm;font-size:13pt;margin:0 0 2mm}
.rm table.ziele{margin-bottom:2.5mm}
"""


def build_pruefung(pg, p: dict, out: Path, ueberlauf: list):
    kurz = p["kurz"]
    seiten = []

    def page(cls: str, inner: str) -> str:
        return "<div class='page %s'><div class='grow'>%s</div>{FOOT}</div>" % (cls, inner)

    def kopf(meta: str, h1: str) -> str:
        return "<div class='gkopf'><div><div class='meta'>%s</div><h1>%s</h1></div><div class='var'>%s</div></div>" % (meta, h1, md(kurz))

    namen = "<div class='namen'><div>Name:</div><div class='d'>Datum:</div></div>"
    meta = "Deutsch · Jahrgang 5 · Zootiere · %s" % md(p["art"])

    # 1 Auftrag
    seiten.append(page("pk", kopf(meta, md(p["titel"])) + namen
        + "<div class='zeit'>%s</div>" % md(p["arbeitszeit"])
        + ("<div class='zeit'><b>Termin:</b> %s</div>" % "".join("<span style='margin-right:6mm'><span class='cb'></span>%s</span>" % md(t) for t in p["termin"]) if p.get("termin") else "")
        + "<h2>Deine Situation</h2><div class='sit'>%s</div>" % md(p["situation"])
        + "<h2>Dein Auftrag</h2><ul class='al'>%s</ul>" % "".join("<li><span class='cb'></span><span>%s</span></li>" % md(a) for a in p["auftrag"])
        + "<div class='hw'>%s<div><b>%s</b></div></div>" % ("".join("<div>%s</div>" % md(h) for h in p["hinweise"]), md(p["ablauf"]))))
    # 2 Material (Interview: eigene, mehrseitige PDF, wird nach Seite 1 eingefügt)
    m = p["material"]
    if not p.get("interview"):
      seiten.append(page("pm", kopf(meta, "Material: %s" % md(m["titel"]))
        + "<img src='data:image/jpeg;base64,%s' alt='%s'><div class='cred'>%s</div><div class='bh'>%s</div>"
        % (b64(ROOT / m["foto"]["datei"]), html.escape(m["foto"]["alt"]), html.escape(m["foto"]["nachweis"]), md(m.get("bildhinweis", "")))
        + "<div class='txt box'><b>Sachtext</b><br>%s</div>%s" % (md(m["text"]), woerter_html(m))))
    # 3 Planung
    fl = ""
    for f in p["plan"]["felder"]:
        fl += "<div class='fh'>%s</div>" % md(f["titel"])
        for lab, n in f["zeilen"]:
            fl += "".join("<div class='zl'><span class='lab'>%s</span><span class='ln'></span></div>" % md(lab) for _ in range(n))
    seiten.append(page("pp", kopf(meta, "Planung: dein Schreibplan") + "<div class='sit'>%s</div>" % md(p["plan"]["hinweis"]) + fl))
    # 4 Schreibseite
    seiten.append(page("ps", "<div class='sw'>" + kopf(meta, "Schreiben: dein Text") + namen
        + "<div class='sit'>%s</div>" % md(p["schreiben"]["hinweis"])
        + "<div class='ueb'><span>Überschrift:</span><span class='ln'></span></div><div class='sb'>%s</div>" % ("<div class='l'></div>" * 40)
        + "<div class='hw'><b>Prüfen:</b> %s</div></div>" % md(p["schreiben"]["pruefen"])))
    # 5 Das zählt
    z = p["zaehlt"]
    seiten.append(page("pz", kopf(meta, "Dein Text: Das zählt") + "<div class='sit'><b>Dein Ziel:</b> %s</div><div style='margin-top:3mm'>" % md(z["ziel"])
        + "".join("<div class='kr'><span class='cb'></span><span><b>%s:</b> %s</span></div>" % (md(a), md(b)) for a, b in z["kriterien"])
        + "</div><div class='hw'><b>So wird deine %s ausgewertet</b><div>%s</div><div>%s</div></div>" % (md(p["art"]), md(z["auswertung"]), md(z["zusatz"]))))
    # 6 Hilfe
    hl = p["hilfe"]
    seiten.append(page("ph", kopf(meta, "Diese Hilfe darfst du nutzen") + "<div class='sit'>%s</div>" % md(hl["einleitung"])
        + "".join("<div class='blk'><b>%s</b>%s</div>" % (md(a), md(b)) for a, b in hl["bloecke"])
        + "<div class='hw'>%s</div>" % md(hl["regeln"])))
    # 7 Rückmeldung der Lehrkraft (Klassenarbeit: Bewertungsseite)
    if p.get("bewertung"):
        bw = p["bewertung"]
        cbs = lambda xs: "".join("<span><span class='cb'></span>%s</span>" % md(x) for x in xs)
        rows = "".join(
            "<tr><td><span class='id'>%s</span> %s<span class='krit'>%s</span></td>"
            "<td class='c'><span class='cb'></span></td><td class='c'><span class='cb'></span></td><td class='c'><span class='cb'></span></td>"
            "<td class='e'>___ / ___</td></tr>" % (md(k[0]), md(k[1]), md(k[2])) for k in bw["kriterien"])
        seiten.append(page("rm", kopf("Bewertung der Lehrkraft", "Deine Klassenarbeit")
            + "<table class='ziele'><tr><th>Bereich</th><th>erfüllt</th><th>teil&shy;weise</th><th>noch nicht</th><th>Punkte</th></tr>%s</table>" % rows
            + "<div class='ergebnis'><div class='sum box'>Gesamt<b style='font-size:20pt'>____ / ____</b>Punkte</div>"
              "<div class='ent box'><div><b>Note:</b> ________</div><div class='krit' style='font-size:11pt'>%s</div></div></div>" % md(bw["hinweis"])
            + "<div class='mini'><b>Genutzte Hilfen:</b>%s</div>" % cbs(bw["hilfen"])
            + "<div class='fb'><div class='h'>Das ist dir gelungen:</div><div class='ln'></div></div>"
            + "<div class='fb'><div class='h'>Daran kannst du weiterarbeiten:</div><div class='ln'></div></div>"
            + "<div class='sig'><div>Lehrkraft:</div><div>Datum:</div></div>"))
        r = None
    else:
        r = p["rueckmeldung"]
    if r is not None:
      rows = "".join(
          "<tr><td><span class='id'>%s</span> %s<span class='krit'>Erreicht, wenn: %s</span></td>"
          "<td class='c'><span class='cb'></span></td><td class='c'><span class='cb'></span></td><td class='u'>%s</td><td class='e'></td></tr>"
          % (zz["id"], md(zz["kind"]), md(zz["lehrkraft"]), md(zz["ueben"])) for zz in p["ziele"])
      cbs = lambda xs: "".join("<span><span class='cb'></span>%s</span>" % md(x) for x in xs)
      seiten.append(page("rm", kopf("Rückmeldung der Lehrkraft", "So weit bist du")
          + "<table class='ziele'><tr><th>Ziel</th><th>gezeigt</th><th>noch offen</th><th>Übe mit</th><th>erneut gezeigt am</th></tr>%s</table>" % rows
          + "<div class='mini'><b>Genutzte Hilfen:</b>%s</div>" % cbs(r["hilfen"])
          + "<div class='ergebnis'><div class='sum box'>Ergebnis<b>___ / 5</b>Ziele gezeigt</div>"
          "<div class='ent box'><div><span class='cb'></span><b>4 oder 5 Ziele:</b> %s</div><div><span class='cb'></span><b>Weniger als 4:</b> %s</div></div></div>"
          % (md(r["bestanden"]), md(r["offen"]))
          + "<div class='fb'><div class='h'>Das gelingt dir schon:</div><div class='ln'></div></div>"
          + "<div class='fb'><div class='h'>Dein nächster Schritt:</div><div class='ln'></div></div>"
          + "<div class='mini'><b>Wahlzeit:</b>%s</div><div class='mini'><b>Klassenarbeit, vereinbarter Termin:</b>%s</div>" % (cbs(r["wahl"]), cbs(r["termin"]))
          + "<div class='sig'><div>Lehrkraft:</div><div>Datum:</div></div>"))

    pdf = out / ("%s.pdf" % p["datei"])
    ivpdf, m_iv = None, 0
    if p.get("interview"):
        from build_interviews import QUELLE, render_interview
        iv = json.loads(QUELLE.read_text(encoding="utf-8"))
        t = {x["id"]: x for x in iv["tiere"]}[p["interview"]]
        ivpdf = pdf.with_name(pdf.stem + "_iv.pdf")
        render_interview(pg, t, iv["rahmen"], iv["hinweis_fiktiv"], "%s · Material · Interview" % p["art"], ivpdf,
                         fuss_rechts="%s · Material" % kurz)
        m_iv = len(fitz.open(ivpdf))
    n = len(seiten) + m_iv
    nr = lambda k: k + m_iv  # Interview (Materialbasis) steht vorn
    body = "".join(sp.replace("{FOOT}", "<div class='foot'><span>%s · %s</span><b>%s · Seite %d/%d</b></div>"
                              % (FUSS, md(p["art"]), md(kurz), nr(k), n)) for k, sp in enumerate(seiten, 1))
    o = render(pg, doc(body, PR_CSS, p["titel"]), pdf)
    if o:
        ueberlauf.append("%s: Überlauf auf Seite %s" % (p["datei"], o))
    if ivpdf:
        d = fitz.open(pdf)
        d.insert_pdf(fitz.open(ivpdf), start_at=0)
        d.save(pdf.with_name(pdf.stem + "_neu.pdf"))
        d.close()
        pdf.with_name(pdf.stem + "_neu.pdf").replace(pdf)
        ivpdf.unlink()
    return ("%s (S. 1–%d)" % (kurz, n - 1), pdf, font_sizes(pdf, list(range(n - 1))), MIN_PT["nachweis_aufgaben"])



# ---------------------------------------------------------------- Input-Präsentation
INPUT_HTML = r"""<!doctype html><html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>__TITLE__</title>
<style>
__FONTS__
:root{--slate-dark:#2C3D4C;--slate-base:#3E5668;--slate-mid:#6A8599;--slate-pale:#D0DCE6;--slate-ghost:#EEF3F7;--rust-dark:#9E4E22;--rust-base:#D97A4A;--rust-mid:#EBA882;--rust-pale:#F5DDD1;--rust-ghost:#FBF0EB;--sage-dark:#4D8B3F;--sage-base:#7DBB6F;--sage-mid:#A8D49D;--sage-pale:#DDF0D8;--sage-ghost:#F0FAF0;--text:#1E2A35;--text-muted:#5A6A78;--ink:var(--text);--mid:var(--text-muted);--soft:var(--slate-mid);--line:var(--slate-pale);--fill:var(--slate-ghost);--bg:#F5F4F1}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;background:var(--slate-dark);font-family:'Andika',sans-serif;color:var(--ink);overflow:hidden}
#stage{position:absolute;left:50%;top:50%;width:1600px;height:900px;transform-origin:center;background:var(--bg)}
.slide{position:absolute;inset:0;padding:70px 90px 90px;display:none;flex-direction:column}
.slide.on{display:flex}
.kick{font-size:26px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--rust-dark)}
h1{color:var(--slate-dark)}
h1{font-size:64px;line-height:1.08;margin:8px 0 28px}
h1 .n{display:inline-flex;width:76px;height:76px;border-radius:50%;background:var(--slate-base);color:#fff;font-size:44px;
  align-items:center;justify-content:center;margin-right:24px;vertical-align:6px}
.body{flex:1;display:flex;gap:56px;min-height:0}
.col{flex:1;display:flex;flex-direction:column;gap:22px;min-height:0}
.blk{font-size:var(--fs,33px);line-height:1.38}
.blk .lab{display:block;font-size:22px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--slate-base);margin-bottom:4px}
.blk.frage{border:3px solid var(--rust-base);background:var(--rust-ghost);border-radius:18px;padding:16px 24px}
.blk.frage .lab{color:var(--rust-dark)}
.blk.ans{border-left:10px solid var(--sage-dark);background:var(--sage-pale);border-radius:0 18px 18px 0;padding:16px 24px;transition:opacity .25s}
.blk.ans.zu{opacity:0;pointer-events:none}
.blk.lang{font-size:30px}
h1 .teil{font-size:30px;color:var(--text-muted);font-weight:400;margin-left:14px}
.fotowrap{flex:0 0 640px;display:flex;flex-direction:column}
.fotowrap img{width:640px;border-radius:18px}
.blk.ans .lab{color:var(--sage-dark)}
.fotowrap .cred{font-size:18px;color:var(--mid);margin-top:8px}
.title .ziel{font-size:40px;line-height:1.35;border-left:10px solid var(--rust-base);padding:10px 0 10px 28px;max-width:1150px}
.title h1{font-size:88px;margin-top:20px}
.weg{display:flex;gap:18px;align-items:center;margin-top:auto;font-size:30px}
.weg span{border:3px solid var(--slate-base);background:var(--slate-ghost);border-radius:14px;padding:14px 22px;white-space:nowrap}
.weg span:last-child{border-color:var(--sage-dark);background:var(--sage-ghost)}
.weg span.d{border-style:dashed;border-color:var(--rust-base);background:var(--rust-ghost)}
.weg i{font-style:normal;font-size:38px;color:var(--rust-base)}
#bar{position:absolute;left:90px;right:90px;bottom:34px;display:flex;gap:10px;align-items:center}
#bar .dot{flex:1;height:8px;border-radius:4px;background:var(--line)}
#bar .dot.on{background:var(--rust-base)}
#bar .num{font-size:20px;color:var(--mid);margin-left:14px;min-width:70px;text-align:right}
#hint{position:absolute;right:90px;top:30px;font-size:18px;color:var(--soft)}
@media print{#hint,#bar{display:none}}
</style></head><body>
<div id="stage">__SLIDES__<div id="bar"></div><div id="hint">Leertaste: weiter · ←: zurück · F: Vollbild</div></div>
<script>
const slides=[...document.querySelectorAll('.slide')];let i=0;
const bar=document.getElementById('bar');
slides.forEach(()=>{const d=document.createElement('div');d.className='dot';bar.appendChild(d)});
const num=document.createElement('div');num.className='num';bar.appendChild(num);
function fit(){const s=Math.min(innerWidth/1600,innerHeight/900);document.getElementById('stage').style.transform='translate(-50%,-50%) scale('+s+')'}
function show(n){i=Math.max(0,Math.min(slides.length-1,n));slides.forEach((s,k)=>s.classList.toggle('on',k===i));
 [...bar.querySelectorAll('.dot')].forEach((d,k)=>d.classList.toggle('on',k<=i));num.textContent=(i+1)+' / '+slides.length}
function next(){const z=slides[i].querySelector('.ans.zu');if(z){z.classList.remove('zu');return}show(i+1)}
function prev(){show(i-1)}
addEventListener('keydown',e=>{if([' ','ArrowRight','PageDown','Enter'].includes(e.key)){e.preventDefault();next()}
 else if(['ArrowLeft','PageUp','Backspace'].includes(e.key)){e.preventDefault();prev()}
 else if(e.key==='f'||e.key==='F'){document.fullscreenElement?document.exitFullscreen():document.documentElement.requestFullscreen()}
 else if(e.key==='a'||e.key==='A'){slides[i].querySelectorAll('.ans').forEach(x=>x.classList.remove('zu'))}});
addEventListener('click',e=>{if(e.target.closest('.ans.zu')){e.target.closest('.ans').classList.remove('zu');return}
 (e.clientX<innerWidth/4)?prev():next()});
// Folien mit viel Text automatisch etwas kleiner setzen (mind. 24 px)
function shrink(){const top=()=>document.getElementById('bar').getBoundingClientRect().top;
 slides.forEach((s,k)=>{show(k);let f=33;s.style.setProperty('--fs',f+'px');
  const low=()=>{let m=0;s.querySelectorAll('.blk,img').forEach(e=>{m=Math.max(m,e.getBoundingClientRect().bottom)});return m};
  while(f>24&&low()>top()-8){f--;s.style.setProperty('--fs',f+'px')}})}
addEventListener('resize',fit);fit();show(0);document.fonts.ready.then(()=>{shrink();show(0)});
</script></body></html>"""


def farbig(rel: str) -> str:
    """HTML darf farbig sein: farbige Fassung bevorzugen (…_graustufen.jpg → …_farbe.jpg, x.svg → x_farbe.svg)."""
    p = Path(rel)
    kandidaten = [p.with_name(p.name.replace("_Graustufen", "").replace("_graustufen", "") + "")]
    if p.suffix == ".svg":
        kandidaten = [p.with_name(p.stem + "_farbe.svg")]
    elif "Fischotter" in p.name or "fischotter" in p.name:
        kandidaten = [Path("assets/bilder/fischotter_farbe.jpg")]
    else:
        kandidaten = [p.with_name(p.name.replace("_graustufen", "_farbe"))]
    for k in kandidaten:
        if (ROOT / k).exists():
            return str(k)
    return rel


def input_html(c: dict) -> str:
    foto_b64 = b64(ROOT / farbig(c["foto"]["datei"]))
    e = c["etappe"]
    weg = ("<div class='weg'><span>Input + Merkblatt %d</span><i>→</i><span>Blatt %d–%d · Pflicht</span>"
           "<span class='d'>Vertiefung · freiwillig</span><i>→</i><span>%s</span></div>"
           % (e, c["blaetter"][0]["nr"], c["blaetter"][-1]["nr"], c.get("abschluss_name", "Gelingensnachweis")))
    s = [
        "<section class='slide title'><div class='kick'>Zootiere · Etappe %d · Input</div><h1>%s</h1>"
        "<div class='ziel'><b>Dein Ziel:</b> %s</div>"
        "%s</section>" % (e, md(c["titel"]), md(c["ziel"]), weg)
    ]
    for k, sec in enumerate(c["input"], 1):
        # 'umbruch_nach': Folie nach so vielen Blöcken teilen (Merkblatt bleibt unverändert)
        cuts = [0] + ([sec["umbruch_nach"]] if sec.get("umbruch_nach") else []) + [len(sec["bloecke"])]
        for part in range(len(cuts) - 1):
            teil = sec["bloecke"][cuts[part]:cuts[part + 1]]
            blks = []
            for lab, txt in teil:
                cls = "ans zu" if lab.startswith("Gesicherte Antwort") else ("frage" if lab == "Frage" else "")
                if len(txt) > 260:
                    cls += " lang"
                blks.append("<div class='blk %s'><span class='lab'>%s</span>%s</div>" % (cls, md(lab), md(txt)))
            foto = ""
            if sec.get("foto"):
                foto = "<div class='fotowrap'><img src='data:image/jpeg;base64,%s' alt='%s'><div class='cred'>%s</div></div>" % (
                    foto_b64, html.escape(c["foto"]["alt"]), html.escape(c["foto"]["nachweis"].replace(" · Graustufenfassung", "")))
            if sec.get("grafik"):
                foto = "<div class='fotowrap'><img src='%s' alt='%s'></div>" % (svg_uri(farbig(sec["grafik"])), html.escape(sec.get("grafik_alt", "")))
            if foto:
                body = foto + "<div class='col'>%s</div>" % "".join(blks)
            elif len(blks) > 2:
                # links: Information, rechts: ab der ersten Frage (Frage + gesicherte Antwort)
                labs = [lab for lab, _ in teil]
                cut = labs.index("Frage") if "Frage" in labs[1:] else (len(blks) + 1) // 2
                if cut >= 3:  # links zu voll: letzten Informationsblock nach rechts über die Frage
                    cut -= 1
                body = "<div class='col'>%s</div><div class='col'>%s</div>" % ("".join(blks[:cut]), "".join(blks[cut:]))
            else:
                body = "<div class='col'>%s</div>" % "".join(blks)
            weiter = "" if len(cuts) == 2 else " <span class='teil'>%d/%d</span>" % (part + 1, len(cuts) - 1)
            s.append(
                "<section class='slide'><div class='kick'>Etappe %d · %s</div><h1><span class='n'>%d</span>%s%s</h1><div class='body'>%s</div></section>"
                % (e, md(c["titel"]), k, md(sec["titel"]), weiter, body)
            )
    s.append(
        "<section class='slide'><div class='kick'>Etappe %d · %s</div><h1>Deine Etappe</h1><div class='body'><div class='col'>"
        "<div class='blk' style='font-size:40px'>%s</div>%s</div></div></section>" % (e, md(c["titel"]), md(c["abschluss"]), weg)
    )
    return (INPUT_HTML.replace("__TITLE__", "Etappe %d · %s" % (e, plain(c["titel"])))
            .replace("__FONTS__", font_css()).replace("__SLIDES__", "".join(s)))


# ---------------------------------------------------------------- Rendern und Prüfen
def render(page, html_str: str, pdf: Path) -> list[str]:
    page.set_content(html_str, wait_until="load")
    page.evaluate("document.fonts.ready")
    over = page.evaluate(
        "[...document.querySelectorAll('.page')].map((p,i)=>{const g=p.querySelector('.grow');"
        "const d=Math.max(g?g.scrollHeight-g.clientHeight:0,p.scrollHeight-p.clientHeight);"
        "return d>1?(i+1)+' (+'+Math.round(d*25.4/96)+' mm)':0}).filter(x=>x)"
    )
    # Spaltenüberlauf (Merkblatt): Inhalt rechts außerhalb der Seite
    over += page.evaluate(
        "[...document.querySelectorAll('.cols')].map((c,i)=>c.scrollWidth>c.clientWidth+1?i+1:0).filter(x=>x)"
    )
    page.pdf(path=str(pdf), prefer_css_page_size=True, print_background=True)
    return over


def font_sizes(pdf: Path, pages: list[int] | None = None) -> tuple[float, int]:
    d = fitz.open(pdf)
    mins = []
    for pno, p in enumerate(d):
        if pages and pno not in pages:
            continue
        for b in p.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                for s in l["spans"]:
                    if s["text"].strip():
                        mins.append(round(s["size"], 2))
    return (min(mins) if mins else 0, len(d))


def check_identity(c: dict, html_in: str, pdf_mb: Path) -> list[str]:
    mbtxt = re.sub(r"\s+", " ", "".join(p.get_text() for p in fitz.open(pdf_mb)))
    intxt = plain(html_in)
    miss = []
    for sec in c["input"]:
        for lab, txt in sec["bloecke"]:
            for line in [plain(md(x)) for x in txt.split("\n")]:
                probe = line[:60]
                if probe not in intxt:
                    miss.append("Input fehlt: " + probe)
                if probe.replace(" ", "") not in mbtxt.replace(" ", "").replace("-\n", ""):
                    miss.append("Merkblatt fehlt: " + probe)
    return miss


def main(n: int):
    c = json.loads((ROOT / "inhalt" / f"etappe{n}.json").read_text(encoding="utf-8"))
    out = ROOT / "ausgabe" / f"etappe{n}"
    out.mkdir(parents=True, exist_ok=True)
    report = []
    ueberlauf = []
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page()

        # Input
        h_in = input_html(c)
        (out / f"Input_Etappe{n}.html").write_text(h_in, encoding="utf-8")

        pg.set_viewport_size({"width": 1600, "height": 900})
        pg.set_content(h_in, wait_until="load")
        pg.evaluate("document.fonts.ready.then(()=>shrink())")
        n_sl = pg.evaluate("document.querySelectorAll('.slide').length")
        for k in range(n_sl):
            pg.evaluate("show(%d); document.querySelectorAll('.ans').forEach(x=>x.classList.remove('zu'))" % k)
            d = pg.evaluate("(()=>{const s=document.querySelector('.slide.on');const bar=document.getElementById('bar').getBoundingClientRect().top;"
                            "let m=0;s.querySelectorAll('*').forEach(e=>{m=Math.max(m,e.getBoundingClientRect().bottom)});return m-bar+8})()")
            if d > 0:
                ueberlauf.append(f"Input: Folie {k+1} läuft {round(d)} px in die Fortschrittsleiste")

        # Merkblatt: fließend zweispaltig, höchstens zwei Seiten (Vorder- und Rückseite)
        mb = out / f"Merkblatt_{n}_A4.pdf"
        if merkblatt_render(pg, c, mb) > 2:
            ueberlauf.append("Merkblatt: mehr als zwei Seiten")
        report.append(("Merkblatt", mb, font_sizes(mb), MIN_PT["merkblatt"]))

        # Übungsblätter
        ub = out / f"Uebungsblaetter_Etappe{n}_A4.pdf"
        # zu volle Blätter automatisch dichter setzen (Schrift bleibt mind. 14 pt)
        dicht = {b["nr"]: 0 for b in c["blaetter"]}
        mats = [] if c.get("interviews") else materialien(c)
        off = len(mats)
        if c.get("interviews"):
            mp = out / f"Material_Etappe{n}_A4.pdf"
            report.append(("Materialbasis", mp, build_materialbasis(pg, c, mp, ueberlauf), MIN_PT["uebung"]))
        zs = c.get("zusatzseiten", [])
        for _ in range(3):
            body = ("".join(material_page(c, m) for m in mats)
                    + "".join(blatt_page(c, b, dicht[b["nr"]]) for b in c["blaetter"])
                    + "".join(zusatz_page(c, z, k, len(zs)) for k, z in enumerate(zs, 1)))
            o = render(pg, doc(body, UB_CSS, f"Übungsblätter Etappe {n}"), ub)
            voll = [int(str(x).split()[0]) - 1 - off for x in o]
            voll = [c["blaetter"][k]["nr"] for k in voll if 0 <= k < len(c["blaetter"]) and dicht[c["blaetter"][k]["nr"]] < 2]
            if not voll:
                break
            for nr in voll:
                dicht[nr] += 1
        if o:
            ueberlauf.append(f"Übungsblätter: Überlauf auf Seite {o}")
        report.append(("Übungsblätter", ub, font_sizes(ub), MIN_PT["uebung"]))

        # Hilfekarten (auf A5 verkleinert drucken) und Raumschild (A4 Originalgröße)
        for h in c.get("hilfen", []):
            hp = out / ("%s.pdf" % h["datei"])
            o = render(pg, doc(hilfe_page(c, h), HK_CSS, h["titel"]), hp)
            if o:
                ueberlauf.append("%s: Überlauf %s" % (h["datei"], o))
            report.append((h["kennung"], hp, font_sizes(hp), MIN_PT["uebung"]))
        if c.get("schild"):
            sp = out / ("%s.pdf" % c["schild"]["datei"])
            o = render(pg, doc(schild_page(c, c["schild"]), HK_CSS, c["schild"]["titel"]), sp)
            if o:
                ueberlauf.append("Schild: Überlauf %s" % o)

        # Gelingensnachweise
        for var in (c["nachweis"]["varianten"] if c.get("nachweis") else []):
            gp = out / f"GN{n}_{var}_A4.pdf"
            o = render(pg, doc(gn_pages(c, var), GN_CSS, f"Gelingensnachweis {n}{var}"), gp)
            if o:
                ueberlauf.append(f"GN{n}{var}: Überlauf auf Seite {o}")
            report.append((f"GN{n}{var} Aufgaben", gp, font_sizes(gp, [0]), MIN_PT["nachweis_aufgaben"]))
        # Probearbeit (Abschluss der letzten Etappe)
        if c.get("pruefung"):
            pr = json.loads((ROOT / c["pruefung"]).read_text(encoding="utf-8"))
            report.append(build_pruefung(pg, pr, out, ueberlauf))
        br.close()

    fail = bool(ueberlauf)
    for u in ueberlauf:
        print("ÜBERLAUF:", u)
    for name, path, (mn, pages), need in report:
        st = "ok" if mn >= need - 0.05 else "ZU KLEIN"
        fail |= st != "ok"
        print(f"{name:22s} {pages} S.  kleinste Schrift {mn:5.2f} pt (mind. {need})  {st}")
    miss = check_identity(c, h_in, mb)
    print("Input = Merkblatt:", "ok" if not miss else "\n  " + "\n  ".join(miss))
    if fail or miss:
        sys.exit(1)


def main_pruefung(path: str):
    p = json.loads((ROOT / path).read_text(encoding="utf-8"))
    out = ROOT / "ausgabe" / "pruefungen"
    out.mkdir(parents=True, exist_ok=True)
    ueberlauf = []
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        name, pdf, (mn, pages), need = build_pruefung(br.new_page(), p, out, ueberlauf)
        br.close()
    for u in ueberlauf:
        print("ÜBERLAUF:", u)
    print(f"{name:22s} {pages} S.  kleinste Schrift {mn:5.2f} pt (mind. {need})")
    if ueberlauf or mn < need - 0.05:
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "pruefung":
        main_pruefung(sys.argv[2])
    else:
        main(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
