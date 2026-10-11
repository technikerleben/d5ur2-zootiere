#!/usr/bin/env python3
"""Neutraler Lernbuddy (laminierte A4-Tischvorlage) in Rechts- und Linkshänderfassung.

Aufbau nach Lernbuddy-Definition (skill.md): oben Planung, seitlich Durchführung
(Strategie, Lösungsleiter, „Ich stecke fest – so komme ich weiter“), unten Reflexion,
freie Mitte für das A5-Arbeitsblatt (148 × 210 mm), Außenkante zum Anlegen einer Strategiekarte.
Rechtshänder: Durchführung links (die Schreibhand verdeckt sie nicht); Linkshänder: rechts.

    python3 tools/build_lernbuddy.py  -> ausgabe/lernbuddy/
"""
from __future__ import annotations

import sys
from pathlib import Path

import pymupdf as fitz
from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_material import ROOT, doc, font_sizes, render  # noqa: E402

AUS = ROOT / "ausgabe" / "lernbuddy"

# Maße in mm
M, G = 5, 3            # Außenrand, Abstand zur Mitte
MW, MH = 150, 212      # freie Mitte (A5 + 1 mm Luft je Seite)
SW = 210 - M - G - MW - 2   # Seitenspalte
TOP = 33
BOT = 297 - 2 * M - 2 * G - MH - TOP

CSS = """
.page{width:210mm;height:297mm;position:relative;overflow:hidden;font-size:12pt;line-height:1.25}
.z{position:absolute;border:1.6pt solid var(--ink);border-radius:3mm;padding:1.6mm 2.6mm;overflow:hidden}
.kopf{display:flex;align-items:center;gap:2mm;font-weight:700;font-size:13pt;margin-bottom:1.2mm}
.kopf .n{display:inline-flex;width:6.5mm;height:6.5mm;border-radius:50%;background:var(--ink);color:#fff;font-size:12pt;
  align-items:center;justify-content:center;flex:0 0 auto}
.kopf .u{font-weight:400;color:var(--mid);font-size:12pt}
.reihe{display:flex;gap:4mm;align-items:flex-end;margin-top:1.2mm}
.f{display:flex;gap:1.5mm;align-items:flex-end;flex:1}
.f .l{flex:0 0 auto;font-weight:700}
.f .ln{flex:1;border-bottom:1pt solid var(--mid);height:6mm;min-width:8mm}
.f.kurz{flex:0 0 auto}.f.kurz .ln{flex:0 0 14mm}
.opt{display:flex;gap:2.5mm;align-items:center;flex:0 0 auto}
.opt span{display:flex;gap:1mm;align-items:center}
.ring{display:inline-block;width:4.6mm;height:4.6mm;border:1.3pt solid var(--ink);border-radius:50%}
.cb{display:inline-block;width:4.2mm;height:4.2mm;border:1.3pt solid var(--ink);border-radius:.8mm}
.mitte{position:absolute;border:1.6pt dashed var(--mid);border-radius:2mm;display:flex;align-items:center;justify-content:center}
.mitte .t{color:#bbb;font-size:16pt;font-weight:700;text-align:center;line-height:1.4}
.mitte .t small{display:block;font-size:12pt;font-weight:400}
.ecke{position:absolute;width:7mm;height:7mm;border-color:var(--ink);border-style:solid;border-width:0}
.leiter{margin-top:1mm}
.stufe{display:flex;gap:2mm;align-items:center;border:1.2pt solid var(--ink);border-radius:1.6mm;padding:1.1mm 1.8mm;margin-bottom:1.3mm;background:#fff}
.stufe b{flex:0 0 5.5mm;height:5.5mm;border-radius:50%;border:1.3pt solid var(--ink);display:flex;align-items:center;justify-content:center;font-size:12pt}
.stufe span{flex:1}
.pfeil{text-align:center;font-size:12pt;color:var(--mid);margin:-.6mm 0 .4mm}
.blk{margin-top:2mm}
.blk>.h{font-weight:700}
.zl{border-bottom:1pt solid var(--mid);height:6.2mm}
.fest{border:1.2pt dashed var(--ink);border-radius:2mm;padding:1.4mm 2mm;margin-top:2mm}
.kante{position:absolute;top:0;height:297mm;width:5mm;display:flex;align-items:center;justify-content:center}
.kante span{writing-mode:vertical-rl;font-size:12pt;color:var(--mid);letter-spacing:.06em;white-space:nowrap}
.hinweis{color:var(--mid)}
.marke{position:absolute;font-size:12pt;color:var(--mid)}
"""


def planung() -> str:
    return (
        "<div class='kopf'><span class='n'>1</span>Planung<span class='u'>· bevor ich starte</span></div>"
        "<div class='reihe'><div class='f'><span class='l'>Mein Ziel heute:</span><span class='ln'></span></div>"
        "<div class='f kurz'><span class='l'>Blatt:</span><span class='ln'></span></div></div>"
        "<div class='reihe'><div class='opt'><b>Meine Energie:</b><span class='hinweis'>wenig</span>%s<span class='hinweis'>viel</span></div>"
        "<div class='f'><span class='l'>Das lenkt mich ab:</span><span class='ln'></span></div></div>"
        "<div class='reihe'><div class='opt'><b>Ich starte mit:</b><span><span class='cb'></span>Merkblatt</span>"
        "<span><span class='cb'></span>Beispiel</span><span><span class='cb'></span>Strategiekarte</span><span><span class='cb'></span>gleich los</span></div></div>"
        % "".join("<span class='ring'></span>" for _ in range(5)).replace("</span><span class='ring'>", "</span> <span class='ring'>")
    )


def durchfuehrung() -> str:
    stufen = ["Aufgabe neu lesen", "Merkblatt, Beispiel", "Strategiekarte", "Kind fragen (leise)", "Tipp holen", "Lehrkraft fragen"]
    leiter = "".join("<div class='stufe'><b>%d</b><span>%s</span></div>%s" % (i, s, "")
                     for i, s in reversed(list(enumerate(stufen, 1))))
    return (
        "<div class='kopf'><span class='n'>2</span>Durchführung</div><div class='hinweis'>während ich arbeite</div>"
        "<div class='blk'><div class='h'>Meine Strategie:</div><div class='zl'></div>"
        "<div class='reihe'><div class='f'><span class='l'>Karte Nr.</span><span class='ln'></span></div></div></div>"
        "<div class='blk'><div class='h'>Lösungsleiter ▲</div><div class='hinweis'>unten anfangen</div><div class='leiter'>%s</div></div>"
        "<div class='fest'><div class='h'><b>Ich stecke fest bei:</b></div><div class='zl'></div>"
        "<div class='h' style='margin-top:1.5mm'><b>So komme ich weiter:</b></div><div class='zl'></div><div class='zl'></div></div>"
        "<div class='blk'><div class='h'>Zwischenstopp: Hilft mein Weg?</div>"
        "<div class='opt' style='margin-top:1mm;flex-wrap:wrap'><span><span class='cb'></span>ja</span><span><span class='cb'></span>ich ändere etwas</span></div></div>"
        % leiter
    )


def reflexion() -> str:
    return (
        "<div class='kopf'><span class='n'>3</span>Reflexion<span class='u'>· bevor ich abwische: Wichtiges ins Heft übertragen</span></div>"
        "<div class='reihe'><div class='f'><span class='l'>Das ist mir gelungen:</span><span class='ln'></span></div>"
        "<div class='opt'><b>Ziel erreicht:</b><span><span class='cb'></span>ganz</span><span><span class='cb'></span>teilweise</span>"
        "<span><span class='cb'></span>noch nicht</span></div></div>"
        "<div class='reihe'><div class='f'><span class='l'>Geholfen hat mir:</span><span class='ln'></span></div></div>"
        "<div class='reihe'><div class='f'><span class='l'>Mein nächster Schritt:</span><span class='ln'></span></div></div>"
    )


def seite(hand: str) -> str:
    rechts = hand == "rechts"
    # Rechtshänder: Seitenspalte links, Mitte rechts; Linkshänder gespiegelt
    side_x = M if rechts else 210 - M - SW
    mid_x = M + SW + G if rechts else 210 - M - SW - G - MW
    y_mid = M + TOP + G
    h = ["<div class='page'>"]
    h.append("<div class='z' style='left:%dmm;top:%dmm;width:%dmm;height:%dmm'>%s</div>" % (M, M, 210 - 2 * M, TOP, planung()))
    h.append("<div class='z' style='left:%dmm;top:%dmm;width:%dmm;height:%dmm'>%s</div>" % (side_x, y_mid, SW, MH, durchfuehrung()))
    h.append("<div class='mitte' style='left:%dmm;top:%dmm;width:%dmm;height:%dmm'><div class='t'>Hier liegt dein<br>Arbeitsblatt (A5)"
             "<small>Ich bearbeite die Aufgabe in der Mitte.</small></div></div>" % (mid_x, y_mid, MW, MH))
    h.append("<div class='z' style='left:%dmm;top:%dmm;width:%dmm;height:%dmm'>%s</div>" % (M, y_mid + MH + G, 210 - 2 * M, BOT, reflexion()))
    # Außenkante: Strategiekarte anlegen
    h.append("<div class='kante' style='%s:0'><span>%s Strategiekarte hier anlegen %s</span></div>"
             % ("left" if rechts else "right", "▲" if rechts else "▼", "▲" if rechts else "▼"))
    h.append("<div class='marke' style='bottom:1mm;%s:%dmm'>Lernbuddy · %shänder</div>" % ("right" if rechts else "left", M + 2, "Rechts" if rechts else "Links"))
    h.append("</div>")
    return "".join(h)


def main():
    AUS.mkdir(parents=True, exist_ok=True)
    fehler = []
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page()
        dateien = []
        for hand, name in (("rechts", "Lernbuddy_Rechtshaender_A4.pdf"), ("links", "Lernbuddy_Linkshaender_A4.pdf")):
            html = doc(seite(hand), CSS, "Lernbuddy")
            pg.set_content(html, wait_until="load")
            pg.evaluate("document.fonts.ready")
            over = pg.evaluate("[...document.querySelectorAll('.z')].filter(z=>z.scrollHeight>z.clientHeight+1||z.scrollWidth>z.clientWidth+1).length")
            if over:
                fehler.append("%s: %d Feld(er) laufen über" % (name, over))
            render(pg, html, AUS / name)
            mn, n = font_sizes(AUS / name)
            print("%-34s %d S.  kleinste Schrift %.1f pt" % (name, n, mn))
            if mn < 11.95:
                fehler.append("%s: Schrift zu klein" % name)
            dateien.append(AUS / name)
        br.close()
    beide = fitz.open()
    for f in dateien:
        beide.insert_pdf(fitz.open(f))
    beide.save(AUS / "Lernbuddy_beide_A4.pdf")
    print("Mitte: %d × %d mm (A5 = 148 × 210), Seitenspalte %d mm, oben %d mm, unten %d mm" % (MW, MH, SW, TOP, BOT))
    for f in fehler:
        print("FEHLER:", f)
    sys.exit(1 if fehler else 0)


if __name__ == "__main__":
    main()
