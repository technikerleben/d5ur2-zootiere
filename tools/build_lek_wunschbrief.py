#!/usr/bin/env python3
"""Druckfassung der Lernerfolgskontrolle Wunschbrief (Termin 1) im Zootiere-Stil.

Quelle:  inhalt/lek_wunschbrief_termin1.json
Ausgabe: ausgabe/pruefungen/LEK_Wunschbrief_Termin1_A4.pdf  (A4, Originalgröße drucken)

Seitenfolge (3 Seiten statt 5 der Vorlage):
  1  Auftrag + Planung       (Vorlage S. 1 und 2)
  2  Schreibbogen + Reflexion (Vorlage S. 3)
  3  Das zählt + Hilfe       (Vorlage S. 4 und 5)

Satz wie Gelingensnachweis/Klassenarbeit: Andika eingebettet, Graustufen,
Schüleraufgaben mindestens 14 pt. Prüft Seitenüberlauf und Mindestschriftgröße.

Aufruf: python tools/build_lek_wunschbrief.py [inhalt/lek_wunschbrief_termin1.json]
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_material import PR_CSS, ROOT, doc, font_sizes, md, render  # noqa: E402
from playwright.sync_api import sync_playwright  # noqa: E402

QUELLE = ROOT / "inhalt" / "lek_wunschbrief_termin1.json"
MIN_PT = 12.0   # Untergrenze nach Verdichtung (Merkblatt-Niveau); Grundsatz 14 pt
MIN_ZOOM = MIN_PT / 14.0

# Verdichtet eine Seite stufenweise (CSS-Zoom auf den Inhalt), nur wenn sie sonst überläuft.
FIT_JS = """(minz) => [...document.querySelectorAll('.page')].map(p => {
  const g = p.querySelector('.grow'); let z = 1;
  const over = () => g.scrollHeight - g.clientHeight > 1;
  while (over() && z > minz + 0.001) { z = Math.max(minz, z - 0.01); g.style.zoom = z; }
  return Math.round(z * 1000) / 1000; })"""

CSS = PR_CSS + """
.page{padding:10mm 15mm 8mm 15mm}
.hs{font-weight:400;font-size:14pt}
.pfl{display:flex;gap:5mm;align-items:center}
.pfl .k1{flex:1 1 auto}
.pfl .seite{flex:0 0 50mm;margin:0;border-left:2pt solid var(--line);padding-left:3.5mm}
h2.st{font-size:16pt;margin:3mm 0 1.2mm;display:flex;align-items:baseline;gap:3mm}
h2.st .s{font-size:14pt;font-weight:400;color:var(--mid)}
.sit{font-size:14pt;line-height:1.35}
.al li{font-size:14pt;margin-bottom:1mm;line-height:1.3}
.reihe{display:flex;gap:5mm;margin-top:2.5mm;align-items:stretch}
.reihe>.zu{flex:1 1 0;padding:2mm 3.5mm;font-size:14pt;line-height:1.3}
.reihe>.zu b{display:block}
.reihe>.um{flex:1.25 1 0;padding:2mm 3.5mm;font-size:14pt;line-height:1.28}
.um .h{font-weight:700}
.um table{width:100%;border-collapse:collapse;margin-top:1mm}
.um td{border-bottom:1pt solid var(--line);padding:.3mm 1mm}
.um td.z{text-align:right;width:20mm;font-weight:700}
.um th{text-align:left;border-bottom:1.5pt solid var(--ink);padding:.3mm 1mm;font-size:14pt}
.um th.z{text-align:right}
.abl{font-size:14pt;font-weight:700;margin-top:2mm}
.trenn{border-top:2.5pt solid var(--ink);margin-top:3mm;padding-top:.5mm}
.pl{display:flex;align-items:flex-end;gap:3mm;font-size:14pt;line-height:1.2}
.pl .lab{flex:0 1 auto;max-width:118mm;padding-bottom:1mm}
.pl .ln{flex:1;min-width:40mm;border-bottom:1pt solid var(--soft);height:10mm}
.pl.frei .lab{color:var(--mid)}
.zh{font-weight:700;font-size:14pt;margin-top:2.5mm;border-bottom:1.5pt solid var(--ink)}
.klein{font-size:14pt;color:var(--mid);margin-top:1mm}
/* Seite 2 */
.sw .sb{margin-top:2mm}
.refl{padding:2.5mm 4mm;margin-top:3mm;font-size:14pt;line-height:1.35}
.refl b{font-size:15pt}
.refl .zl{display:flex;gap:2.5mm;align-items:flex-start;margin-top:1.2mm}
.refl .cb{flex:0 0 auto;margin-top:.8mm}
/* Seite 3 */
.cols3{display:flex;gap:6mm;align-items:stretch}
.cols3>div{flex:1 1 0;min-width:0}
.cols3 h2{font-size:16pt;margin:0 0 1.5mm;border-bottom:2pt solid var(--ink);padding-bottom:.5mm}
.k{display:flex;gap:2.5mm;align-items:flex-start;font-size:14pt;line-height:1.28;padding:1.1mm 0;border-bottom:1pt solid var(--line)}
.k .cb{flex:0 0 auto;margin-top:.6mm;margin-right:0}
.nb{font-size:14pt;line-height:1.28;color:var(--mid);margin:1.2mm 0 2.5mm}
.hh{font-weight:700;font-size:15pt;margin-top:2.2mm}
.ht{font-size:14pt;line-height:1.3}
.schr{list-style:none;font-size:14pt;line-height:1.25;margin-top:.8mm}
.schr li{display:flex;gap:2mm;align-items:flex-start;margin-bottom:.6mm}
.schr .n{flex:0 0 6.5mm;height:6.5mm;border:1.4pt solid var(--ink);border-radius:50%;display:inline-flex;
  align-items:center;justify-content:center;font-weight:700;font-size:14pt;line-height:1}
.mu{border-left:3pt solid var(--ink);padding:.6mm 0 .6mm 3mm;margin-top:1mm;font-size:14pt;line-height:1.32;font-style:italic}
.bew{padding:2.5mm 4mm;font-size:14pt;line-height:1.32;background:var(--fill);border-radius:2.5mm;margin-top:3mm}
.bew div+div{margin-top:1mm}
.regel{font-size:14pt;line-height:1.32;border:1.5pt dashed var(--ink);border-radius:2.5mm;padding:2mm 3.5mm;margin-top:3mm}
.zielz{font-size:14pt;margin-bottom:1.5mm}
.zu{padding:2mm 3.5mm;font-size:14pt;line-height:1.3;margin-top:2.5mm}
.zu .um{margin-top:1.5mm}
.zu table{width:100%;border-collapse:collapse;margin-top:1mm;table-layout:fixed}
.zu th{font-size:14pt;text-align:center;border:1pt solid var(--ink);padding:.6mm 1mm;background:var(--fill)}
.zu td{text-align:center;border:1pt solid var(--ink);padding:.6mm 1mm;font-weight:700}
h2.h3{font-size:16pt;margin:1.5mm 0 .8mm;border-bottom:2pt solid var(--ink);padding-bottom:.3mm}
.kk{display:grid;grid-template-columns:1fr 1fr;column-gap:6mm}
.k{border-bottom:none;padding:.5mm 0}
.k1 .k{padding:.35mm 0}
.nb{margin:.8mm 0 1.5mm}
.bew{margin-top:2.5mm}
.hilfe{padding:.5mm 4mm 2mm;margin-top:2.5mm}
.hilfe .cols3{margin-top:.5mm}
.regel{margin-top:2mm;padding:1.2mm 3mm}
.schr{display:flex;flex-wrap:wrap;gap:.8mm 3.5mm}
.schr li{margin-bottom:0}
.namen{margin-bottom:1.5mm}
"""


def build(p: dict, out: Path) -> tuple:
    meta = "Deutsch · Jahrgang 5 · %s" % md(p["art"])

    def kopf(h1: str) -> str:
        return ("<div class='gkopf'><div><div class='meta'>%s</div><h1>%s</h1></div>"
                "<div class='var'>%s</div></div>" % (meta, h1, md(p["kurz"])))

    def page(inner: str) -> str:
        return "<div class='page'><div class='grow'>%s</div>{FOOT}</div>" % inner

    namen = "<div class='namen'><div>Name:</div><div class='d'>Datum:</div></div>"
    cb = "<span class='cb'></span>"
    seiten = []

    # 1 Auftrag + Planung
    um = p["umfrage"]
    pl = p["planung"]
    s1 = (kopf(md(p["titel"])) + namen
          + "<div class='zeit'>%s</div>" % md(p["arbeitszeit"])
          + "<h2 class='st'>Deine Situation</h2><div class='sit'>%s %s</div>" % (md(p["situation"]), md(p["wunsch"]))
          + "<h2 class='st'>Dein Auftrag</h2><ul class='al'>%s</ul>"
          % "".join("<li>%s<span>%s</span></li>" % (cb, md(a)) for a in p["auftrag"])
          + "<div class='zu dashed'><div><b>Zusätze · freiwillig:</b> %s</div>" % md(p["zusaetze"])
          + "<div class='um'><b>%s</b><br>%s<table><tr>%s</tr><tr>%s</tr></table></div></div>"
          % (md(um["titel"]), md(um["text"]),
             "".join("<th>%s</th>" % md(w) for w, _ in um["zeilen"]),
             "".join("<td>%d Stimmen</td>" % n for _, n in um["zeilen"]))
          + "<div class='trenn'><h2 class='st'>Planung <span class='s'>%s</span></h2>" % md(p["ablauf"])
          + "<div class='sit'>%s</div>" % md(pl["hinweis"])
          + "".join("<div class='pl'><span class='lab'>%s</span><span class='ln'></span></div>" % md(f) for f in pl["felder"])
          + "<div class='zh'>%s</div>" % md(pl["zusatz_titel"])
          + "".join("<div class='pl frei'><span class='lab'>%s</span><span class='ln'></span></div>" % md(f) for f in pl["zusatz_felder"])
          + "<div class='klein'>%s</div></div>" % md(pl["zusatz_hinweis"]))
    seiten.append(page(s1))

    # 2 Schreibbogen + Reflexion
    s2 = ("<div class='sw'>" + kopf("Durchführung: dein Brief") + namen
          + "<div class='sit'>%s</div>" % md(p["durchfuehrung"]["hinweis"])
          + "<div class='sb'>%s</div>" % ("<div class='l'></div>" * 40)
          + "<div class='refl box'><b>Reflexion</b><div>%s</div></div></div>" % md(p["reflexion"]))
    seiten.append(page(s2))

    # 3 Das zählt + Hilfe
    z, h = p["zaehlt"], p["hilfe"]
    zaehlt = ("<h2 class='h3'>Das gehört in deinen Brief</h2><div class='pfl'><div class='k1'>"
              + "".join("<div class='k'>%s<span>%s</span></div>" % (cb, md(x)) for x in z["pflicht"])
              + "</div><div class='nb seite'>%s</div></div>" % md(z["pflicht_hinweis"])
              + "<div class='cols3'><div><h2 class='h3'>Das kannst du zusätzlich zeigen</h2><div class='k1'>"
              + "".join("<div class='k'>%s<span>%s</span></div>" % (cb, md(x)) for x in z["zusatz"])
              + "</div><div class='nb'>%s</div>" % md(z["zusatz_hinweis"])
              + "</div><div><div class='bew'><b>So wird dein Brief bewertet</b><br>%s</div></div></div>" % " ".join(md(x) for x in z["bewertung"]))
    links = ("<div class='hh'>Planung</div><div class='ht'>%s</div>" % md(h["planung"])
             + "<div class='hh'>Durchführung <span class='hs'>· Schreibe in dieser Reihenfolge:</span></div>"
             + "<ol class='schr'>%s</ol>" % "".join("<li><span class='n'>%d</span><span>%s</span></li>" % (i, md(x))
                                                 for i, x in enumerate(h["reihenfolge"], 1))
             + "<div class='hh'>Reflexion</div><div class='ht'>%s</div>" % md(h["reflexion"]))
    rechts = ("<div class='ht' style='margin-top:2.2mm'>Wenn du einen Anfang brauchst:</div><div class='mu'>%s</div>"
              % "<br>".join(md(x) for x in h["anfang"])
              + "<div class='ht' style='margin-top:2mm'>Nur wenn du einen Zusatz schreiben möchtest:</div><div class='mu'>%s</div>"
              % "<br>".join(md(x) for x in h["zusatz"]))
    s3 = (kopf("Dein Wunschbrief: Das zählt") + "<div class='namen'><div>Name:</div></div>"
          + "<div class='zielz'><b>Dein Ziel:</b> %s</div>" % md(z["ziel"])
          + zaehlt
          + "<div class='hilfe box'><h2 class='h3'>Diese Hilfe darfst du nutzen</h2><div class='ht'>%s %s</div>" % (md(h["einleitung"]), md(h["regeln"]))
          + "<div class='cols3'><div>%s</div><div>%s</div></div></div>" % (links, rechts))
    seiten.append(page(s3))

    n = len(seiten)
    fuss = "Deutsch · Jahrgang 5 · %s" % md(p["reihe"])
    body = "".join(sp.replace("{FOOT}", "<div class='foot'><span>%s</span><b>%s · Seite %d/%d</b></div>"
                              % (fuss, md(p["kurz"]), k, n)) for k, sp in enumerate(seiten, 1))
    out.mkdir(parents=True, exist_ok=True)
    pdf = out / p["datei"]
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page()
        pg.set_content(doc(body, CSS, "%s · %s · %s" % (p["art"], p["titel"], p["kurz"])), wait_until="load")
        pg.evaluate("document.fonts.ready")
        zoom = pg.evaluate(FIT_JS, MIN_ZOOM)
        over = render(pg, pg.content(), pdf)
        br.close()
    return pdf, over, font_sizes(pdf), zoom


def main(src: str | None = None):
    q = Path(src) if src else QUELLE
    p = json.loads(q.read_text(encoding="utf-8"))
    pdf, over, (mn, seiten), zoom = build(p, ROOT / "ausgabe" / "pruefungen")
    print("%s: %d Seiten, kleinste Schrift %.1f pt" % (pdf.relative_to(ROOT), seiten, mn))
    print("Grundschrift je Seite: " + ", ".join("S. %d: %.1f pt" % (i, 14 * z) for i, z in enumerate(zoom, 1)))
    fehler = []
    if over:
        fehler.append("Überlauf auf Seite %s" % ", ".join(map(str, over)))
    if mn < MIN_PT - 0.05:
        fehler.append("Schrift unter %.0f pt" % MIN_PT)
    if fehler:
        print("FEHLER: " + "; ".join(fehler))
        sys.exit(1)
    print("Prüfung ok: kein Überlauf, alle Texte ≥ %.0f pt" % MIN_PT)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else None)
