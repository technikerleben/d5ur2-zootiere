#!/usr/bin/env python3
"""Erzeugt den QR-Zettel zur Lern-App (A4, Graustufen, Originalgröße drucken).

Seite 1: Elternzettel mit QR-Code, Handy-Regel, Elterninfo (Deutsch) und je einem
Satz in Ukrainisch, Arabisch, Türkisch, Englisch und Französisch.
Seite 2: acht QR-Schnipsel zum Ausschneiden und Einkleben ins Heft.

Zwei Fassungen: regulär und „Einfache Fassung“ (Link mit ?einfach=1).
Texte: inhalt/lernapp.json (app.adresse, start_hinweis, elterninfo, qrzettel).
Prüft: zwei Seiten, Mindestschrift 12 pt, QR-Code lesbar (Inhalt = Adresse).

Aufruf: python tools/build_qrzettel.py
"""
import base64
import html
import io
import json
import re
from pathlib import Path

import segno

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "ausgabe" / "lernapp"
FONTS = ROOT / "assets" / "fonts"
MIN_PT = 12.0


def b64(p: Path) -> str:
    return base64.b64encode(p.read_bytes()).decode("ascii")


def fonts() -> str:
    out = []
    for w in (400, 700):
        out.append("@font-face{font-family:'Andika';font-weight:%d;src:url(data:font/woff2;base64,%s) format('woff2');}" % (w, b64(FONTS / f"andika-latin-{w}-normal.woff2")))
        out.append("@font-face{font-family:'Andika';font-weight:%d;unicode-range:U+0100-024F,U+1E00-1EFF;src:url(data:font/woff2;base64,%s) format('woff2');}" % (w, b64(FONTS / f"andika-latin-ext-{w}-normal.woff2")))
        out.append("@font-face{font-family:'Andika';font-weight:%d;unicode-range:U+0400-045F,U+0490-0491;src:url(data:font/woff2;base64,%s) format('woff2');}" % (w, b64(FONTS / f"andika-cyrillic-{w}-normal.woff2")))
    out.append("@font-face{font-family:'Noto Sans Arabic';font-weight:400;src:url(data:font/woff2;base64,%s) format('woff2');}" % b64(FONTS / "noto-sans-arabic-arabic-400-normal.woff2"))
    return "\n".join(out)


def md(t: str) -> str:
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    return re.sub(r"\*(.+?)\*", r"<i>\1</i>", t)


INFO = ('<svg class="ic" viewBox="0 0 24 24" fill="none" stroke="#000" stroke-width="2.4" stroke-linecap="round">'
        '<circle cx="12" cy="12" r="9.5"/><path d="M12 11v6M12 7.5v.2"/></svg>')


def qr_svg(url: str) -> str:
    q = segno.make(url, error="m")
    buf = io.BytesIO()
    q.save(buf, kind="svg", scale=1, border=2, dark="#000", light="#fff", xmldecl=False, svgns=True, nl=False, omitsize=True)
    s = buf.getvalue().decode("utf-8")
    return s.replace("<svg ", '<svg width="100%" height="100%" shape-rendering="crispEdges" ', 1)


CSS = """
@page{size:A4;margin:0}
*{box-sizing:border-box}
html,body{margin:0;font-family:'Andika',sans-serif;color:#000;font-size:12pt;line-height:1.32}
.seite{width:210mm;height:297mm;padding:11mm 15mm 10mm;position:relative;page-break-after:always;overflow:hidden}
.seite:last-child{page-break-after:auto}
.kopf{display:flex;justify-content:space-between;font-size:12pt;border-bottom:1.2pt solid #000;padding-bottom:1.5mm;margin-bottom:4.5mm}
h1{font-size:21pt;line-height:1.15;margin:0 0 3.5mm}
h2{font-size:15pt;margin:0 0 2mm}
p{margin:0 0 2.4mm}
.oben{display:flex;gap:8mm;align-items:flex-start;margin-bottom:5mm}
.qr{flex:none;width:47mm;text-align:center}
.qr .code{width:47mm;height:47mm}
.url{font-size:12pt;font-weight:700;margin-top:1mm;line-height:1.2}
ol{margin:0;padding-left:6mm}
ol li{margin:0 0 1.2mm}
.einfach{display:inline-block;border:1.5pt solid #000;border-radius:2mm;padding:0.5mm 2.5mm;font-size:13pt;vertical-align:3pt}
.regel{border:2.4pt solid #000;border-radius:4mm;padding:2.5mm 5mm;margin:0 0 4mm;display:flex;gap:5mm;align-items:center}
.regel svg{flex:none;width:14mm;height:14mm}
.regel h2{margin-bottom:1mm}
.regel p{font-size:13pt;margin:0 0 0.6mm;line-height:1.28}
.regel p:last-child{margin:0}
.eltern p{margin-bottom:1.6mm}
.sprachen{margin-top:3mm;border-top:0.8pt solid #000;padding-top:2.5mm}
.sprachen p{margin:0 0 1.3mm;line-height:1.28}
.sprachen .k{font-size:12pt;color:#333}
[lang=ar]{font-family:'Noto Sans Arabic',sans-serif;direction:rtl;text-align:right}
.ic{width:4.2mm;height:4.2mm;vertical-align:-0.8mm}
.fuss{position:absolute;left:15mm;right:15mm;bottom:7mm;font-size:12pt;border-top:0.6pt solid #000;padding-top:1.2mm}
.schnipsel{padding:0}
.raster{display:grid;grid-template-columns:105mm 105mm;grid-template-rows:repeat(4,74.25mm)}
.karte{border:0.6pt dashed #555;padding:6mm 6mm;display:flex;gap:5mm;align-items:center}
.karte .code{flex:none;width:36mm;height:36mm}
.karte b{display:block;font-size:15pt;line-height:1.2;margin-bottom:1.5mm}
.karte p{font-size:12pt;margin:0 0 1.2mm;line-height:1.3}
"""

PHONE = ('<svg viewBox="0 0 48 48" fill="none" stroke="#000" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">'
         '<rect x="15" y="5" width="18" height="32" rx="3"/><path d="M22 31h4"/><path d="M6 40h36"/><path d="M10 44h28"/><path d="M38 8l-28 28"/></svg>')


def seiten(app: dict, einfach: bool) -> str:
    Z, E, H = app["qrzettel"], app["elterninfo"], app["start_hinweis"]
    url = app["app"]["adresse"] + ("?einfach=1" if einfach else "")
    qr = qr_svg(url)
    de = next(s for s in E["sprachen"] if s["code"] == "de")
    kurz = url.replace("https://", "")
    kurz_html = html.escape(kurz).replace(".vercel", "<wbr>.vercel").replace("/", "<wbr>/", 1).replace("?", "<wbr>?")
    h = ['<section class="seite"><div class="kopf"><span>Deutsch · Jahrgang 5</span><span>Lern-App „%s“</span></div>' % html.escape(app["app"]["titel"])]
    h.append("<h1>%s%s</h1>" % (html.escape(Z["titel"]), ' <span class="einfach">%s</span>' % html.escape(app["einfach"]["titel"]) if einfach else ""))
    h.append('<div class="oben"><div class="qr"><div class="code">%s</div><div class="url">%s</div></div><div>' % (qr, kurz_html))
    if einfach:
        h.append('<p><b>%s</b></p>' % md(Z["einfach_hinweis"]))
    h.append("<h2>So geht es</h2><ol>%s</ol></div></div>" % "".join("<li>%s</li>" % md(s) for s in Z["schritte"]))
    h.append('<div class="regel">%s<div><h2>%s</h2>%s</div></div>' % (PHONE, html.escape(H["titel"]), "".join("<p>%s</p>" % md(t) for t in H["absaetze"])))
    # Offline-Absatz steht schon in „So geht es“
    eltern = [t for t in de["absaetze"] if not t.startswith("**Offline") and not t.startswith("Die Interviews sind")]
    h.append('<div class="eltern"><h2>%s</h2>%s</div>' % (html.escape(Z["anrede"]), "".join("<p>%s</p>" % md(t) for t in eltern)))
    h.append('<div class="sprachen">')
    for code, text, kenn in Z["sprachen"]:
        h.append('<p lang="%s">%s <span class="k">%s</span></p>' % (code, html.escape(text).replace("{i}", INFO), html.escape(kenn)))
    h.append("</div>")
    h.append('<div class="fuss">Heinrich-Böll-Gesamtschule Dortmund · Deutsch · Jahrgang 5</div></section>')
    # Seite 2: Schnipsel
    karte = ('<div class="karte"><div class="code">%s</div><div><b>Zootiere</b><p>Lern-App für zu Hause%s</p><p>%s</p><p><b style="display:inline;font-size:12pt">In der Schule:</b> Handy aus und in der Schultasche.</p></div></div>'
             % (qr, " · " + html.escape(app["einfach"]["titel"]) if einfach else "", kurz_html))
    h.append('<section class="seite schnipsel"><div class="raster">%s</div></section>' % (karte * 8))
    return "\n".join(h)


def pruefe(pdf: Path, url: str):
    import pymupdf as fitz
    doc = fitz.open(pdf)
    if doc.page_count != 2:
        raise SystemExit(f"QR-Zettel {pdf.name}: {doc.page_count} Seiten statt 2")
    klein = set()
    for page in doc:
        for b in page.get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                for sp in l["spans"]:
                    if sp["text"].strip() and sp["size"] < MIN_PT - 0.05:
                        klein.add((round(sp["size"], 1), sp["text"][:30]))
    if klein:
        raise SystemExit(f"QR-Zettel {pdf.name}: Schrift unter {MIN_PT} pt: {sorted(klein)[:5]}")
    seite = doc[0]
    fuss_y = max(b[1] for b in seite.get_text("blocks") if "Heinrich-Böll" in b[4])
    unten = max(b[3] for b in seite.get_text("blocks") if "Heinrich-Böll" not in b[4])
    if unten > fuss_y - 2:
        raise SystemExit(f"QR-Zettel {pdf.name}: Text läuft in die Fußzeile ({unten:.0f} > {fuss_y:.0f})")
    txt = doc[0].get_text()
    for muss in ("Schultasche", "KI", "українською", "English"):
        if muss not in txt:
            raise SystemExit(f"QR-Zettel {pdf.name}: Text fehlt: {muss}")
    # QR-Code lesen (über gerenderte Seite) – nur wenn ein Decoder verfügbar ist
    try:
        import zxingcpp  # type: ignore
        from PIL import Image
        pix = doc[0].get_pixmap(dpi=200)
        img = Image.open(io.BytesIO(pix.tobytes("png")))
        res = [r.text for r in zxingcpp.read_barcodes(img)]
        if url not in res:
            raise SystemExit(f"QR-Zettel {pdf.name}: QR-Code liest {res}, erwartet {url}")
        lesbar = "QR gelesen"
    except ImportError:
        lesbar = "QR nicht maschinell gelesen (kein Decoder)"
    return lesbar


def main():
    from playwright.sync_api import sync_playwright
    app = json.loads((ROOT / "inhalt" / "lernapp.json").read_text(encoding="utf-8"))
    OUT.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page()
        for einfach, name in ((False, "QR_Lernapp_Elternzettel_A4.pdf"), (True, "QR_Lernapp_Elternzettel_Einfach_A4.pdf")):
            doc = "<!doctype html><html lang='de'><head><meta charset='utf-8'><style>%s%s</style></head><body>%s</body></html>" % (fonts(), CSS, seiten(app, einfach))
            pg.set_content(doc, wait_until="load")
            pg.evaluate("document.fonts.ready")
            pdf = OUT / name
            pg.pdf(path=str(pdf), prefer_css_page_size=True, print_background=True)
            url = app["app"]["adresse"] + ("?einfach=1" if einfach else "")
            print(f"ok: {pdf.relative_to(ROOT)} (2 Seiten, ≥ {MIN_PT:g} pt, {pruefe(pdf, url)})")
        br.close()


if __name__ == "__main__":
    main()
