#!/usr/bin/env python3
"""Planungszettel „Mein Plan bis zur Lernerfolgskontrolle“ (Zootiere, Jahrgang 5).

A4 gesetzt, Druck auf A5 verkleinert, Graustufen, Schrift >= 14 pt.
Ausgabe: ausgabe/lernweg/Planungszettel_Lernerfolgskontrolle_A4.pdf (+ .html)
"""
import asyncio, base64
from pathlib import Path
import qrcode, qrcode.image.svg
import pymupdf
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "ausgabe/lernweg/Planungszettel_Lernerfolgskontrolle_A4"
TASKCARDS = ("https://schulendortmund.taskcards.app/#/board/86a516d4-8c24-40f8-9b4e-d3b50587ecbc"
             "?token=c62bc016-43cb-4d91-80e5-05c687e62385")

# (Tag, Datum, Stunde, Hinweis, Art)
TAGE = [("Di", "24.11.", "Einzelstunde", "Plan machen", ""),
        ("Mi", "25.11.", "Doppelstunde", "früher Termin", "termin"),
        ("Fr", "27.11.", "zu Hause", "Dienstbesprechung", "haus"),
        ("Di", "01.12.", "Doppelstunde", "mittlerer Termin", "termin"),
        ("Mi", "02.12.", "zu Hause", "Sprechtag", "haus"),
        ("Fr", "04.12.", "Sprache", "Vorbereitung", ""),
        ("Di", "08.12.", "Unterricht", "später Termin", "termin")]

GESCHAFFT = ["Etappe 1 (Blatt 1–4)", "Gelingensnachweis 1", "Etappe 2 (Blatt 5–6)", "Gelingensnachweis 2",
             "Etappe 3 (Blatt 7–9)", "Probearbeit", "Feedback zur Probearbeit"]

def font(w, st, n):
    b = base64.b64encode((ROOT / "assets/fonts" / f"{n}.woff2").read_bytes()).decode()
    return f"@font-face{{font-family:Andika;font-weight:{w};font-style:{st};src:url(data:font/woff2;base64,{b})}}"

def qr():
    return qrcode.make(TASKCARDS, image_factory=qrcode.image.svg.SvgPathImage, border=1).to_string(encoding="unicode")

def html():
    fonts = font(400, "normal", "andika-latin-400-normal") + font(700, "normal", "andika-latin-700-normal")
    zeilen = "".join(
        f"<tr class='{c}'><td class='d'><b>{w} {d}</b><br><span>{s}</span></td>"
        f"<td class='h'>{'<b>' + h + '</b>' if c == 'termin' else h}</td><td class='z'></td><td class='ok'><span class='box'></span></td></tr>"
        for w, d, s, h, c in TAGE)
    geschafft = "".join(f"<li><span class='box'></span>{g}</li>" for g in GESCHAFFT)
    return f"""<!DOCTYPE html><html lang='de'><head><meta charset='utf-8'><style>{fonts}
@page{{size:A4;margin:10mm 12mm}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Andika,sans-serif;font-size:15pt;line-height:1.25;color:#000}}
.kopf{{display:flex;justify-content:space-between;font-size:14pt;border-bottom:1.5pt solid #000;padding-bottom:3pt}}
h1{{font-size:21pt;margin:5pt 0 4pt}}
.name{{font-size:15pt;margin-bottom:8pt}} .name span{{display:inline-block;width:120mm;border-bottom:1pt solid #000}}
h2{{font-size:16pt;margin:0 0 4pt}}
.abschnitt{{border:1.5pt solid #000;border-radius:5pt;padding:5pt 9pt;margin-bottom:6pt}}
.box{{display:inline-block;width:13pt;height:13pt;border:1.5pt solid #000;border-radius:2pt;vertical-align:-1pt;margin-right:6pt}}
.termine{{display:flex;gap:8pt}}
.termine div{{flex:1;border:1pt solid #000;border-radius:4pt;padding:3pt 6pt;font-size:15pt;white-space:nowrap}}
.grid{{columns:2;column-gap:12pt;list-style:none}}
.grid li{{margin-bottom:3pt;break-inside:avoid}}
.tipp{{font-size:14pt;margin-top:3pt}}
table{{width:100%;border-collapse:collapse}}
th{{font-size:14pt;text-align:left;border-bottom:1.5pt solid #000;padding:2pt 5pt}}
td{{border-bottom:1pt solid #666;padding:3pt 5pt;vertical-align:top;font-size:14pt}}
td.d{{width:40mm}} td.d span{{font-size:14pt}}
td.h{{width:33mm}}
td.z{{height:12.5mm}}
td.ok{{width:17mm;text-align:center}}
tr.termin td{{border-top:1.5pt solid #000}}
tr.haus td{{background-color:#EDEDED}}
.zuhause{{display:flex;gap:10pt;align-items:center;border:1.5pt dashed #000;border-radius:5pt;padding:4pt 9pt;font-size:14pt}}
.zuhause svg{{width:31mm;height:31mm;display:block}}
.fuss{{display:flex;justify-content:space-between;font-size:14pt;margin-top:5pt;border-top:1pt solid #000;padding-top:2pt}}
</style></head><body>
<div class=kopf><span>Deutsch · Jahrgang 5 · Zootiere</span><span>Planungszettel</span></div>
<h1>Mein Plan bis zur Lernerfolgskontrolle</h1>
<div class=name>Name: <span></span></div>

<div class=abschnitt><h2>1 · Mein Termin <span style="font-weight:400">– kreuze an:</span></h2>
<div class=termine><div><span class=box></span><b>früher</b> · Mi 25.11.</div><div><span class=box></span><b>mittlerer</b> · Di 01.12.</div><div><span class=box></span><b>später</b> · Di 08.12.</div></div></div>

<div class=abschnitt><h2>2 · Das habe ich schon geschafft</h2>
<ul class=grid>{geschafft}</ul>
<div class=tipp><b>Tipp:</b> Plane rückwärts. Vor deinem Termin sind alle Etappen, die Probearbeit und das Feedback fertig.</div></div>

<div class=abschnitt><h2>3 · Das will ich schaffen</h2>
<table><tr><th>Wann?</th><th>Hinweis</th><th>Das will ich schaffen</th><th>geschafft</th></tr>{zeilen}</table></div>

<div class=zuhause><div>{qr()}</div><div><b>Zu Hause lernen:</b> Am <b>Fr 27.11.</b> (Dienstbesprechung) kannst du zusätzlich zu Hause lernen. Am <b>Mi 02.12.</b> (Sprechtag) findet kein Unterricht statt. Bereite dich mit deinen Unterlagen und der <b>TaskCards-Pinnwand</b> gut vor. Scanne dafür den QR-Code.</div></div>
</body></html>"""

async def pdf(src, dst):
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page()
        await pg.goto(src.as_uri()); await pg.wait_for_timeout(300)
        await pg.pdf(path=str(dst), format="A4", print_background=True, prefer_css_page_size=True)
        await b.close()

def main():
    h = OUT.with_suffix(".html"); p = OUT.with_suffix(".pdf")
    h.write_text(html(), encoding="utf-8")
    asyncio.run(pdf(h, p))
    d = pymupdf.open(p)
    klein = min(s["size"] for pg in d for bl in pg.get_text("dict")["blocks"] for l in bl.get("lines", []) for s in l["spans"])
    print(f"{p.relative_to(ROOT)}: {d.page_count} Seite(n), kleinste Schrift {klein:.1f} pt")
    assert d.page_count == 1, "Seitenüberlauf"
    assert klein >= 13.9, "Schrift unter 14 pt"

if __name__ == "__main__":
    main()
