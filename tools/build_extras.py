#!/usr/bin/env python3
"""Erzeugt Wahlphase (Projekte A4, Originalgröße) und Strategiekarten (210 × 99 mm).

Aufruf: python tools/build_extras.py
Ausgabe: ausgabe/wahlphase/Wahlphase_Projekte_A4.pdf
         ausgabe/strategiekarten/Strategiekarten_A4.pdf
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_material import FUSS, UB_CSS, doc, font_sizes, md, render  # noqa: E402
from playwright.sync_api import sync_playwright  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

# ---------------------------------------------------------------- Wahlphase
WP_CSS = UB_CSS + """
.page.wp{font-size:14pt;line-height:1.3;padding:12mm 15mm 9mm 15mm}
.wp .ukopf{margin-bottom:3mm}.wp .nr{width:24mm;height:24mm}.wp .nr span{font-size:12pt}.wp .nr b{font-size:26pt}.wp .ukopf h1{font-size:26pt}
.wp .brauch{font-size:14pt;margin-bottom:3mm;padding:2mm 3.5mm}
.erg{font-size:14.5pt;border-left:3pt solid var(--ink);padding:1mm 0 1mm 4mm;margin-bottom:4mm}
.wp .teil{margin-bottom:3mm;padding:2.5mm 4mm 3mm}
.wp .teil h2{font-size:15pt;margin-bottom:1mm}
.sch{display:flex;gap:3mm;margin-bottom:1.6mm}
.sch .sn{flex:0 0 8mm;height:8mm;border-radius:50%;background:var(--ink);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:14pt}
.sch b{display:block}
.gl{display:grid;grid-template-columns:1fr 1fr;gap:1.5mm 6mm}
.gl div{display:flex;gap:2mm;align-items:flex-start}.gl .cb{flex:0 0 auto;margin-top:1mm}
.still{font-size:14pt;color:var(--mid);margin-top:2mm}
.an{border:1.5pt solid var(--ink);border-radius:3mm;padding:2.5mm 4mm;margin-bottom:2.5mm}
.an b{font-size:15pt}
.zuerst{font-size:14pt;font-weight:700;padding:3mm 4.5mm;border:2.5pt solid var(--ink);border-radius:3mm;margin-bottom:5mm}
"""


def wahl_uebersicht(u: dict) -> str:
    h = ["<div class='page wp'><div class='grow'><div class='ukopf'><div><div class='meta'>Wahlphase · nach dem Feedback</div><h1>%s</h1></div></div>" % md(u["titel"])]
    h.append("<div class='erg'>%s</div><div class='zuerst'>%s</div>" % (md(u["einleitung"]), md(u["zuerst"])))
    h += ["<div class='an'><b>%s</b><div>%s</div></div>" % (md(a), md(b)) for a, b in u["angebote"]]
    h.append("<div class='tipp'>%s</div>" % md(u["regeln"]))
    h.append("</div><div class='foot'><span>%s · Wahlphase</span><b>Übersicht · A4 Originalgröße</b></div></div>" % FUSS)
    return "".join(h)


def projekt_page(p: dict) -> str:
    h = ["<div class='page wp'><div class='grow'>"
         "<div class='ukopf'><div class='nr'><span>Projekt</span><b>%s</b></div><div><div class='meta'>Wahlprojekt · freiwillig</div><h1>%s</h1></div></div>"
         % (md(p["nr"]), md(p["titel"]))]
    h.append("<div class='erg'><b>Dein Ergebnis:</b> %s</div>" % md(p["ergebnis"]))
    h.append("<div class='brauch'><b>Du brauchst:</b>%s</div>" % md(p["brauchst"]))
    h.append("<div class='teil box'><h2>So gehst du vor</h2>%s</div>" % "".join(
        "<div class='sch'><span class='sn'>%d</span><div><b>%s</b>%s</div></div>" % (i, md(t), md(x)) for i, (t, x) in enumerate(p["schritte"], 1)))
    h.append("<div class='teil box'><h2>So gelingt dein Ergebnis</h2><div class='gl'>%s</div></div>" % "".join(
        "<div><span class='cb'></span><span>%s</span></div>" % md(g) for g in p["gelingt"]))
    h.append("<div class='teil dashed'><h2><span class='tag f'>Freiwillig</span>Erweiterung</h2>%s</div>" % md(p["erweiterung"]))
    h.append("<div class='still'>%s</div>" % md(p["still"]))
    h.append("</div><div class='foot'><span>%s · Wahlphase</span><b>%s · A4 Originalgröße</b></div></div>" % (FUSS, md(p["nr"])))
    return "".join(h)


# ---------------------------------------------------------------- Strategiekarten
ICONS = {
    "lesen": "<path d='M6 10h16v30H6zM26 10h16v30H26z' fill='none' stroke='#111' stroke-width='3'/><path d='M10 18h8M10 24h8M10 30h8M30 18h8M30 24h8' stroke='#111' stroke-width='2.5'/>",
    "markieren": "<rect x='14' y='9' width='30' height='9' fill='#bbb'/><path d='M14 13.5h30M14 26h30M14 38h24' stroke='#111' stroke-width='3'/><text x='2' y='18' font-size='14' font-weight='700' font-family='sans-serif'>L</text><text x='2' y='43' font-size='14' font-weight='700' font-family='sans-serif'>N</text><rect x='14' y='34' width='24' height='9' fill='#bbb' opacity='.8'/>",
    "ordnen": "<rect x='6' y='6' width='36' height='8' fill='#111'/><path d='M8 22h20M8 30h26M8 38h16' stroke='#111' stroke-width='3'/>",
    "lupe": "<circle cx='20' cy='20' r='12' fill='none' stroke='#111' stroke-width='4'/><path d='M29 29l12 12' stroke='#111' stroke-width='5' stroke-linecap='round'/>",
    "liste": "<rect x='8' y='6' width='32' height='38' rx='3' fill='none' stroke='#111' stroke-width='3'/><path d='M14 16h20M14 24h20M14 32h14' stroke='#111' stroke-width='2.5'/>",
    "satz": "<rect x='4' y='16' width='12' height='14' fill='#fff' stroke='#111' stroke-width='3'/><rect x='18' y='16' width='12' height='14' fill='#bbb' stroke='#111' stroke-width='3'/><rect x='32' y='16' width='12' height='14' fill='#fff' stroke='#111' stroke-width='3'/><circle cx='46' cy='36' r='2.5' fill='#111'/>",
    "pruefen": "<circle cx='14' cy='22' r='8' fill='none' stroke='#111' stroke-width='3'/><path d='M26 30h16' stroke='#111' stroke-width='3'/><circle cx='42' cy='16' r='3' fill='#111'/><path d='M8 40l6 5 12-12' fill='none' stroke='#111' stroke-width='3' stroke-linecap='round'/>",
    "sprechen": "<path d='M6 8h28v18H18l-8 7v-7H6z' fill='#fff' stroke='#111' stroke-width='3' stroke-linejoin='round'/><path d='M22 22h20v16h-4v6l-7-6h-9z' fill='#bbb' stroke='#111' stroke-width='3' stroke-linejoin='round'/>",
    "stern": "<path d='M24 5l5.6 12 13 1.4-9.7 8.8 2.7 12.8L24 33.4 12.4 40l2.7-12.8L5.4 18.4l13-1.4z' fill='#fff' stroke='#111' stroke-width='3' stroke-linejoin='round'/>",
}

SK_CSS = """
@page{size:A4;margin:0}
.bogen{width:210mm;height:297mm;display:flex;flex-direction:column;page-break-after:always;break-after:page}
.bogen:last-child{page-break-after:auto}
.karte{width:210mm;height:99mm;padding:7mm 8mm 6mm;display:grid;grid-template-columns:52mm 1fr 52mm;gap:6mm;
  border-bottom:0.6pt dashed #888;font-size:13.5pt;line-height:1.27;overflow:hidden}
.karte:last-child{border-bottom:none}
.karte .l,.karte .m,.karte .r{display:flex;flex-direction:column;min-height:0}
.karte .kk{display:flex;gap:2.5mm;align-items:center;font-size:12pt;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--mid)}
.karte .kn{width:9mm;height:9mm;border-radius:50%;background:var(--ink);color:#fff;display:flex;align-items:center;justify-content:center;font-size:13pt}
.karte svg{flex:0 0 auto;width:15mm;height:15mm;margin:3mm 0 2mm}
.karte h2{font-size:19pt;line-height:1.1;margin-bottom:2mm}
.karte .lab{font-size:12pt;font-weight:700;letter-spacing:.05em;text-transform:uppercase;margin:0 0 1.5mm;color:var(--mid)}
.karte .wann{padding:2mm 2.5mm;background:var(--fill);border-radius:2mm;font-size:13pt}
.karte .m{border-left:1.5pt solid var(--ink);border-right:1.5pt solid var(--ink);padding:0 5mm}
.karte ol{list-style:none;counter-reset:s}
.karte ol li{counter-increment:s;display:flex;gap:2.5mm;margin-bottom:2.4mm}
.karte ol li::before{content:counter(s);flex:0 0 7mm;height:7mm;border-radius:50%;border:1.5pt solid var(--ink);display:flex;align-items:center;justify-content:center;font-size:12pt;font-weight:700}
.karte ol.leer li{border-bottom:1pt solid var(--soft);min-height:12mm;margin-bottom:1mm}
.karte .bsp{border-left:3pt solid var(--ink);padding:1mm 0 1mm 3mm;font-size:13pt}
.karte .rest{flex:1}
.karte .ref{border-top:1.5pt solid var(--ink);padding-top:2mm;font-size:12.5pt}
.karte .ref .cbs{display:flex;gap:3mm;margin-top:1.5mm}
.karte .cb{width:5mm;height:5mm;margin-right:1mm}
.karte .fuss{font-size:12pt;color:var(--mid);margin-top:1.5mm}
"""


def karte(k: dict, abschluss: str) -> str:
    leer = k.get("leer")
    steps = "".join("<li><span>%s</span></li>" % md(st) for st in k["schritte"])
    bsp = "<div class='lab'>Beispiel</div><div class='bsp'>%s</div>" % md(k["beispiel"]) if k["beispiel"] else "<div class='lab'>Beispiel</div><div class='bsp' style='min-height:18mm'></div>"
    return ("<div class='karte'>"
            "<div class='l'><div class='kk'><span class='kn'>%d</span><span>Strategiekarte</span></div><svg viewBox='0 0 48 48'>%s</svg>"
            "<h2>%s</h2><div class='rest'></div><div class='lab'>Wann?</div><div class='wann'>%s</div></div>"
            "<div class='m'><div class='lab'>So gehst du vor</div><ol class='%s'>%s</ol></div>"
            "<div class='r'>%s<div class='rest'></div><div class='ref'>%s<div class='cbs'><span><span class='cb'></span>ja</span>"
            "<span><span class='cb'></span>etwas</span><span><span class='cb'></span>nein</span></div></div>"
            "<div class='fuss'>Zootiere · Lernbuddy</div></div></div>"
            % (k["nr"], ICONS[k["symbol"]], md(k["titel"]), md(k["wann"]), "leer" if leer else "", steps, bsp, md(abschluss)))


# ---------------------------------------------------------------- Lernweg (A4, Originalgröße)
LW_CSS = UB_CSS + """
.page.lw{font-size:13.5pt;line-height:1.3;padding:11mm 14mm 8mm 14mm}
.lw .ukopf{margin-bottom:3mm}.lw .ukopf h1{font-size:26pt}
.lw .kopfz{display:flex;gap:6mm;margin-bottom:4mm;font-size:13.5pt}
.lw .kopfz div{flex:1;border-bottom:1pt solid var(--ink);padding-bottom:1mm}
.lw .ziel{border-left:3pt solid var(--ink);padding:1mm 0 1mm 3.5mm;margin-bottom:4mm;font-size:14pt}
.weg{position:relative;padding-left:15mm}
.weg::before{content:"";position:absolute;left:5.5mm;top:4mm;bottom:4mm;border-left:2.5pt dashed var(--ink)}
.st{position:relative;border:1.5pt solid var(--ink);border-radius:3mm;padding:2.2mm 4mm 2.6mm;margin-bottom:2.8mm;background:#fff}
.st .sn{position:absolute;left:-15mm;top:2mm;width:11mm;height:11mm;border-radius:50%;background:var(--ink);color:#fff;
  display:flex;align-items:center;justify-content:center;font-weight:700;font-size:15pt}
.st .sn.o{background:#fff;color:var(--ink);border:2pt solid var(--ink)}
.st h2{font-size:15pt;margin-bottom:1.5mm}
.st .z{display:flex;flex-wrap:wrap;align-items:center;gap:1.5mm 4mm;margin-top:1mm}
.st .z b{min-width:31mm}
.st .z span{display:inline-flex;align-items:center;gap:1mm}
.st .cb{width:5mm;height:5mm;margin:0 .5mm 0 0}
.st .fr{color:var(--mid)}
.st .nw{display:flex;gap:4mm;margin-top:2mm;padding-top:2mm;border-top:1pt solid var(--line)}
.st .nw div{flex:1;border-bottom:1pt solid var(--soft);padding-bottom:.5mm;font-size:13pt}.st .nw div:first-child{flex:1.7}
.lw .fuss{font-size:13pt;color:var(--mid);margin-top:1mm}
"""


def lernweg_page(etappen: list, f: bool) -> str:
    suf = "F" if f else ""
    h = ["<div class='page lw'><div class='grow'><div class='ukopf'><div><div class='meta'>Zootiere · Lernweg%s</div><h1>Mein Lernweg: Zootiere</h1></div></div>" % (" · Schritt für Schritt" if f else ""),
         "<div class='kopfz'><div>Name:</div><div>Klasse:</div></div>",
         "<div class='ziel'><b>Mein Ziel:</b> Ich beschreibe ein Tier genau und sachlich.</div><div class='weg'>"]
    for e in etappen:
        n = e["etappe"]
        nrs = [str(b["nr"]) + suf for b in e["blaetter"]]
        cbs = "".join("<span><span class='cb'></span>%s</span>" % x for x in nrs)
        nachweis = ("<div class='nw'><div>Gelingensnachweis %d%s: ___ / ___</div><div>Datum:</div><div>Freigabe:</div></div>" % (n, suf)
                    if n < 3 else "<div class='nw'><div>Probearbeit: ___ / ___</div><div><span class='cb'></span>Feedback erhalten</div><div>Datum:</div></div>")
        vert = "" if f else "<div class='z fr'><b>Vertiefung · freiwillig</b>%s</div>" % cbs
        h.append("<div class='st'><span class='sn'>%d</span><h2>Etappe %d · %s</h2>"
                 "<div class='z'><b>Start</b><span><span class='cb'></span>Input</span><span><span class='cb'></span>Merkblatt%s</span></div>"
                 "<div class='z'><b>Pflichtblätter</b>%s</div>%s%s</div>"
                 % (n, n, md(e["titel"]), " / Merkkarte" if f else " " + str(n), cbs, vert, nachweis))
    h.append("<div class='st'><span class='sn o'>★</span><h2>Wahlzeit nach dem Feedback</h2>"
             "<div class='z'><span><span class='cb'></span>offene Ziele üben</span><span><span class='cb'></span>P1 Tiermagazin</span>"
             "<span><span class='cb'></span>P2 Tierrätsel</span><span><span class='cb'></span>P3 Tiervergleich</span>"
             "<span><span class='cb'></span>Vertiefung nachholen</span></div></div>")
    h.append("<div class='st'><span class='sn o'>✎</span><h2>Klassenarbeit</h2>"
             "<div class='z'><span><span class='cb'></span>früher Termin: ____________</span><span><span class='cb'></span>später Termin: ____________</span></div></div>")
    h.append("</div><div class='fuss'>Vier von fünf Zielen = 80 %. Dann geht es weiter. Lege jedes Blatt in deinen Lernbuddy. Übertrage deine Reflexion vor dem Abwischen ins Heft.</div>")
    h.append("</div><div class='foot'><span>%s</span><b>Lernweg%s · A4 Originalgröße</b></div></div>" % (FUSS, " F" if f else ""))
    return "".join(h)


def main():
    out_w = ROOT / "ausgabe" / "wahlphase"
    out_s = ROOT / "ausgabe" / "strategiekarten"
    out_w.mkdir(parents=True, exist_ok=True)
    out_s.mkdir(parents=True, exist_ok=True)
    w = json.loads((ROOT / "inhalt" / "wahlphase.json").read_text(encoding="utf-8"))
    s = json.loads((ROOT / "inhalt" / "strategiekarten.json").read_text(encoding="utf-8"))
    fail = []
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page()
        wp = out_w / "Wahlphase_Projekte_A4.pdf"
        o = render(pg, doc(wahl_uebersicht(w["uebersicht"]) + "".join(projekt_page(p) for p in w["projekte"]), WP_CSS, "Wahlphase"), wp)
        if o:
            fail.append("Wahlphase: Überlauf %s" % o)
        mn, n = font_sizes(wp)
        print(f"Wahlphase/Projekte   {n} S.  kleinste Schrift {mn:5.2f} pt (mind. 12, Originalgröße)")
        if mn < 11.95:
            fail.append("Wahlphase: Schrift zu klein")

        ks = s["karten"]
        boegen = "".join("<div class='bogen'>%s</div>" % "".join(karte(k, s["abschluss"]) for k in ks[i:i + 3]) for i in range(0, len(ks), 3))
        sp = out_s / "Strategiekarten_A4.pdf"
        pg.set_content(doc(boegen, SK_CSS, "Strategiekarten"), wait_until="load")
        pg.evaluate("document.fonts.ready")
        over = pg.evaluate("[...document.querySelectorAll('.karte')].map((k,i)=>k.scrollHeight>k.clientHeight+1?i+1:0).filter(x=>x)")
        if over:
            fail.append("Strategiekarten: Überlauf auf Karte %s" % over)
        pg.pdf(path=str(sp), prefer_css_page_size=True, print_background=True)
        mn, n = font_sizes(sp)
        print(f"Strategiekarten      {n} S.  kleinste Schrift {mn:5.2f} pt (mind. 12, Originalgröße)")
        if mn < 11.95:
            fail.append("Strategiekarten: Schrift zu klein")
        out_l = ROOT / "ausgabe" / "lernweg"
        out_l.mkdir(parents=True, exist_ok=True)
        et = [json.loads((ROOT / "inhalt" / f"etappe{k}.json").read_text(encoding="utf-8")) for k in (1, 2, 3)]
        etf = [json.loads((ROOT / "inhalt" / f"foerder_etappe{k}.json").read_text(encoding="utf-8")) for k in (1, 2, 3)]
        for name, ets, f in (("Lernweg_Zootiere_A4.pdf", et, False), ("Lernweg_Zootiere_F_A4.pdf", etf, True)):
            if f:
                for e in ets:
                    e["blaetter"] = [dict(b, nr=str(b["nr"]).rstrip("F")) for b in e["blaetter"]]
            lp = out_l / name
            o = render(pg, doc(lernweg_page(ets, f), LW_CSS, "Lernweg"), lp)
            if o:
                fail.append("%s: Überlauf %s" % (name, o))
            mn, n = font_sizes(lp)
            print(f"{name:28s} {n} S.  kleinste Schrift {mn:5.2f} pt (mind. 12, Originalgröße)")
            if mn < 11.95:
                fail.append("%s: Schrift zu klein" % name)
        br.close()
    print("ok" if not fail else "FEHLER:\n  " + "\n  ".join(fail))
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main()
