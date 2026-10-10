#!/usr/bin/env python3
"""Probearbeit F und Klassenarbeit F (zieldifferent, Förderschwerpunkt Lernen).

Aufbau wie Probearbeit/Klassenarbeit, Aufgabenformate wie im Förder-Material:
Kurzinterview (Material) → Auftrag → Aufgabenseiten (ohne Lösungsstreifen) → Rückmeldung bzw. Bewertung.
A4, Druck in Originalgröße.

    python3 tools/build_pruefung_f.py inhalt/probearbeit_f_waschbaer.json
    python3 tools/build_pruefung_f.py inhalt/klassenarbeit_f_biber.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pymupdf as fitz
from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_foerder import F_CSS, aufgabe_html  # noqa: E402
from build_interviews import QUELLE, render_interview  # noqa: E402
from build_material import FUSS, GN_CSS, ROOT, doc, font_sizes, md, render  # noqa: E402

PF_CSS = F_CSS + GN_CSS.replace(".page{padding:12mm 15mm 9mm 15mm;font-size:14pt;line-height:1.3}", "") + """
.page.rm{padding:12mm 15mm 9mm 15mm;font-size:14pt;line-height:1.3}
.pk .sit{font-size:16.5pt;line-height:1.4;margin-bottom:4mm}
.pk h2{font-size:18pt;margin:5mm 0 2mm}
.schr{counter-reset:s;list-style:none}
.schr li{display:flex;gap:3mm;align-items:center;margin-bottom:2.5mm}
.schr li b{flex:0 0 10mm;height:10mm;border-radius:50%;background:var(--ink);color:#fff;display:flex;align-items:center;justify-content:center}
.zeit{font-size:14pt;margin-bottom:2mm}
.hw{font-size:15pt;padding:3mm 4mm;background:var(--fill);border-radius:2.5mm;margin-top:5mm}
table.bw{width:100%;border-collapse:collapse;font-size:14pt;margin:2mm 0 4mm}
table.bw th{font-size:11pt;text-transform:uppercase;letter-spacing:.04em;text-align:left;border-bottom:2pt solid var(--ink);padding:1.5mm 2mm}
table.bw td{border-bottom:1pt solid var(--line);padding:2mm;vertical-align:top}
table.bw td.p{width:30mm;text-align:right;white-space:nowrap}
"""


def build(path: str):
    p = json.loads((ROOT / path).read_text(encoding="utf-8"))
    iv = json.loads(QUELLE.read_text(encoding="utf-8"))
    tier = {t["id"]: t for t in iv["foerder"]}[p["interview"]]
    out = ROOT / "ausgabe" / "pruefungen"
    out.mkdir(parents=True, exist_ok=True)
    pdf = out / ("%s.pdf" % p["datei"])
    ivpdf = pdf.with_name(pdf.stem + "_iv.pdf")
    kurz = p["kurz"]
    meta = "Deutsch · Jahrgang 5 · Zootiere"
    kopf = lambda h1: ("<div class='gkopf'><div><div class='meta'>%s</div><h1>%s</h1></div><div class='var'>%s</div></div>" % (meta, h1, md(kurz)))
    namen = "<div class='namen'><div>Name:</div><div class='d'>Datum:</div></div>"
    seiten = []

    # Auftrag
    termin = ""
    if p.get("termin"):
        termin = "<div class='zeit'><b>Termin:</b> %s</div>" % "".join(
            "<span style='margin-right:6mm'><span class='cb'></span>%s</span>" % md(t) for t in p["termin"])
    seiten.append(("f pk", kopf(md(p["titel"])) + namen + "<div class='zeit'>%s</div>%s" % (md(p["arbeitszeit"]), termin)
                   + "<h2>Deine Situation</h2><div class='sit'>%s</div>" % md(p["situation"])
                   + "<h2>So gehst du vor</h2><ol class='schr'>%s</ol>" % "".join(
                       "<li><b>%d</b><span>%s</span></li>" % (i, md(s)) for i, s in enumerate(p["schritte"], 1))
                   + "<div class='hw'>%s</div>" % md(p["hilfen"])))
    # Aufgaben
    for k, gruppe in enumerate(p["seiten"], 1):
        inner = kopf("Deine Aufgaben") + "".join(aufgabe_html(p["aufgaben"][i], i + 1, {}) for i in gruppe)
        seiten.append(("f", inner))
    # Rückmeldung / Bewertung
    if p.get("bewertung"):
        bw = p["bewertung"]
        rows = "".join("<tr><td><b>%s</b> %s<span class='krit'>%s</span></td><td class='p'>___ / %s</td></tr>"
                       % (md(a), md(b), md(c), md(d)) for a, b, c, d in bw["kriterien"])
        seiten.append(("rm", kopf("Deine Klassenarbeit") .replace(meta, "Bewertung der Lehrkraft")
                       + "<div class='krit' style='font-size:11pt;margin-bottom:2mm'>%s</div>" % md(bw["hinweis"])
                       + "<table class='bw'><tr><th>Aufgabe</th><th style='text-align:right'>Punkte</th></tr>%s</table>" % rows
                       + "<div class='ergebnis'><div class='sum box'>Gesamt<b>___ / %s</b>Punkte</div>"
                         "<div class='ent box'><div><b>Bewertung:</b> ______________________</div>"
                         "<div><span class='cb'></span>Förderziel erreicht &nbsp; <span class='cb'></span>teilweise &nbsp; <span class='cb'></span>noch nicht</div></div></div>" % md(bw["summe"])
                       + "<div class='fb'><div class='h'>Das ist dir gelungen:</div><div class='ln'></div></div>"
                       + "<div class='fb'><div class='h'>Daran kannst du weiterarbeiten:</div><div class='ln'></div></div>"
                       + "<div class='sig'><div>Lehrkraft:</div><div>Datum:</div></div>"))
    else:
        rows = "".join(
            "<tr><td><span class='id'>%s</span> %s<span class='krit'>Erreicht, wenn: %s</span></td>"
            "<td class='c'><span class='cb'></span></td><td class='c'><span class='cb'></span></td><td class='e'></td></tr>"
            % (z["id"], md(z["kind"]), md(z["lehrkraft"])) for z in p["ziele"])
        rows += "<tr><td>Eigenes Förderziel: ______________</td><td class='c'><span class='cb'></span></td><td class='c'><span class='cb'></span></td><td class='e'></td></tr>"
        seiten.append(("rm", kopf("So weit bist du").replace(meta, "Rückmeldung der Lehrkraft")
                       + "<div class='krit' style='font-size:11pt;margin-bottom:2mm'>%s</div>" % md(p["hinweis_lehrkraft"])
                       + "<table class='ziele'><tr><th>Ziel</th><th>gezeigt</th><th>noch offen</th><th>erneut gezeigt am</th></tr>%s</table>" % rows
                       + "<div class='ergebnis'><div class='sum box'>Ergebnis<b>___ / ___</b>Ziele gezeigt</div>"
                         "<div class='ent box'><div><span class='cb'></span><b>80 % der vereinbarten Ziele:</b> Etappe 3 ist geschafft. Du wählst in der Wahlzeit.</div>"
                         "<div><span class='cb'></span><b>Noch nicht:</b> Übe die offenen Ziele. Dann zeigst du sie noch einmal.</div></div></div>"
                       + "<div class='fb'><div class='h'>Das gelingt dir schon:</div><div class='ln'></div></div>"
                       + "<div class='fb'><div class='h'>Dein nächster Schritt:</div><div class='ln'></div></div>"
                       + "<div class='sig'><div>Lehrkraft:</div><div>Datum:</div></div>"))

    fehler = []
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page()
        info = render_interview(pg, tier, iv["rahmen"], iv["hinweis_fiktiv"], "%s · Material · Interview" % kurz, ivpdf,
                                fuss_rechts="%s · Material" % kurz, kompakt=True)
        m = info["seiten"]
        n = len(seiten) + m
        body = "".join("<div class='page %s'><div class='grow'>%s</div><div class='foot'><span>%s · %s</span><b>%s · Seite %d/%d</b></div></div>"
                       % (cls, inner, FUSS, md(p["art"]), md(kurz), k + m, n) for k, (cls, inner) in enumerate(seiten, 1))
        o = render(pg, doc(body, PF_CSS, p["titel"]), pdf)
        br.close()
    if o:
        fehler.append("Überlauf auf Seite %s" % o)
    d = fitz.open(pdf)
    d.insert_pdf(fitz.open(ivpdf), start_at=0)
    d.save(pdf.with_name(pdf.stem + "_neu.pdf"))
    d.close()
    pdf.with_name(pdf.stem + "_neu.pdf").replace(pdf)
    ivpdf.unlink()
    mn, pages = font_sizes(pdf, list(range(n - 1)))
    print("%-30s %d S.  kleinste Schrift (ohne Lehrkraftseite) %.2f pt" % (pdf.name, pages, mn))
    if mn < 13.95:
        fehler.append("Schrift zu klein")
    if m > 1:
        fehler.append("Interview länger als eine Seite")
    for f in fehler:
        print("FEHLER:", f)
    return not fehler


if __name__ == "__main__":
    ok = all(build(a) for a in sys.argv[1:])
    sys.exit(0 if ok else 1)
