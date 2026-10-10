#!/usr/bin/env python3
"""Training zwischen Probearbeit und Klassenarbeit (Elenantilope, Hirschziegenantilope).

Platzsparend: je Tier ein A4-Blatt (Vorderseite Interview zweispaltig mit Zeilennummern,
Rückseite Aufgaben mit Schreibplan), Druck A4 in Originalgröße, Schrift mindestens 12 pt.
Musterlösungen (Mindest- und Regelstandard) stehen im Kontroll-Kiosk; die Zeilenangaben
werden hier ermittelt und in ausgabe/training/zeilen_training.json abgelegt.

    python3 tools/build_training.py   -> ausgabe/training/Training_Antilopen_A4.pdf
"""
from __future__ import annotations

import html
import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_interviews import QUELLE, wort_spans  # noqa: E402
from build_material import FUSS, ROOT, b64, doc, font_sizes, md, render  # noqa: E402

AUS = ROOT / "ausgabe" / "training"

TR_CSS = """
.page{padding:11mm 13mm 9mm 13mm;font-size:12.5pt;line-height:1.32}
.kopf{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2pt solid var(--ink);padding-bottom:2mm;margin-bottom:2.5mm}
.kopf .meta{font-size:12pt;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--mid)}
.kopf h1{font-size:22pt;line-height:1.1}
.kopf .var{font-size:12pt;font-weight:700;border:1.8pt solid var(--ink);border-radius:2mm;padding:.8mm 2.5mm}
.sit{font-size:12.5pt;margin-bottom:2mm}
.fik{font-size:12pt;border:1.3pt dashed var(--ink);border-radius:2mm;padding:.8mm 2.5mm;display:inline-block;margin-bottom:2.5mm}
.foto{float:right;width:45mm;margin:0 0 2mm 4mm;font-size:12pt;color:var(--mid)}
.foto img{width:100%;border-radius:2mm;display:block}
.ivbox{column-count:2;column-gap:7mm;column-rule:1pt solid var(--line);padding-left:9mm;font-size:12.5pt;line-height:1.36}
.ivbox .par{margin-bottom:.6mm}.ivbox .par.q{margin-top:1.6mm;font-weight:700}
.ivbox .ln{position:relative;white-space:nowrap;break-inside:avoid}
.ivbox .ln .nr{position:absolute;left:-8.5mm;width:7mm;text-align:right;font-size:12pt;color:var(--mid);font-weight:400}
.wh{font-size:12pt;margin-top:3mm;padding:2mm 3mm;background:var(--fill);border-radius:2mm}
.wh b.t{text-transform:uppercase;letter-spacing:.05em;margin-right:2mm}
.auf{border:1.5pt solid var(--ink);border-radius:2.5mm;padding:2mm 3.5mm 2.5mm;margin-bottom:2.5mm}
.auf h2{font-size:14pt;display:flex;gap:2.5mm;align-items:center;margin-bottom:.8mm}
.auf h2 .n{display:inline-flex;width:7mm;height:7mm;border-radius:50%;background:var(--ink);color:#fff;font-size:12pt;align-items:center;justify-content:center}
table.plan{width:100%;border-collapse:collapse;margin-top:1.5mm;font-size:12pt}
table.plan th{font-size:12pt;text-align:left;border-bottom:1.5pt solid var(--ink);padding:.8mm 1.5mm}
table.plan td{border-bottom:1pt solid var(--soft);height:8.6mm;padding:0 1.5mm;vertical-align:bottom}
table.plan td.k{width:30mm;font-weight:700}
table.plan td.z{width:22mm;border-left:1pt solid var(--line)}
table.plan tr.neu td{border-top:1.5pt solid var(--ink)}
.checks{display:flex;flex-wrap:wrap;gap:1.5mm 5mm;margin-top:1.5mm}
.checks span{display:flex;gap:1.5mm;align-items:center}
.lin{border-bottom:1pt solid var(--soft);height:8.5mm}
.frei{border:1.5pt dashed var(--ink);border-radius:2.5mm;padding:2mm 3.5mm}
.frei b{margin-right:2mm}
.foot{font-size:12pt;color:var(--mid);border-top-width:1pt}
"""

ZEILEN_JS = r"""
() => { const out = {};
  document.querySelectorAll('.ivbox').forEach(box => { let n = 0; const st = {};
    box.querySelectorAll('.par').forEach(p => { const ws = [...p.querySelectorAll('.w')]; const z = []; let top = null, left = null;
      ws.forEach(w => { const r = w.getBoundingClientRect(); const t = Math.round(r.top), l = Math.round(r.left);
        if (top === null || Math.abs(t - top) > 4 || l < left - 2 && Math.abs(t - top) > 4) { z.push([]); top = t; }
        left = l; z[z.length - 1].push(w); });
      p.replaceChildren(...z.map(r => { n += 1; const d = document.createElement('div'); d.className = 'ln';
        if (n % 5 === 0) { const s = document.createElement('span'); s.className = 'nr'; s.textContent = n; d.appendChild(s); }
        r.forEach((w, i) => { if (i) d.appendChild(document.createTextNode(' ')); d.appendChild(w);
          if (w.dataset.s) { (st[w.dataset.s] ||= []); if (!st[w.dataset.s].includes(n)) st[w.dataset.s].push(n); } });
        return d; })); });
    out[box.dataset.id] = st; });
  return out; }
"""


def plan_tabelle() -> str:
    rows = [("Überblick", "Tiername"), ("", "Maß der Art"), ("Aussehen", "1"), ("", "2"), ("", "3"), ("", "4"),
            ("Lebensraum", ""), ("Nahrung", "")]
    h = "<table class='plan'><tr><th></th><th>Stichwörter</th><th>Zeile</th></tr>"
    for k, lab in rows:
        h += "<tr class='%s'><td class='k'>%s</td><td><span style='color:var(--mid)'>%s</span></td><td class='z'></td></tr>" % (
            "neu" if k else "", k, lab)
    return h + "</table>"


def seiten(tr: dict, u: dict, t: dict, k: int, n: int) -> str:
    kopf = ("<div class='kopf'><div><div class='meta'>Training vor der Klassenarbeit · %s</div><h1>%s</h1></div><div class='var'>%s · Kiosk %d</div></div>"
            % ("Interview" if k % 2 else "Aufgaben", md(u["tier"]), u["kurz"], u["kiosk"]))
    z = [0]
    pars = "".join("<div class='par q'>%s</div><div class='par'>%s</div>" % (wort_spans(q, True, z), wort_spans(a, False, z))
                   for q, a in t["paare"])
    foto = ""
    if t.get("foto") and (ROOT / t["foto"]).is_file():
        foto = "<div class='foto'><img src='data:image/jpeg;base64,%s' alt=''>%s</div>" % (b64(ROOT / t["foto"]), html.escape(t["foto_nachweis"]))
    wh = "<div class='wh'><b class='t'>Wörterhilfe</b>%s</div>" % " · ".join("<b>%s:</b> %s" % (html.escape(w), html.escape(e)) for w, e in t["woerter"])
    fuss = lambda s: "<div class='foot'><span>%s · Training</span><b>%s · Seite %d/%d</b></div>" % (FUSS, u["kurz"], s, n)
    kopf2 = kopf.replace("· Interview", "· Aufgaben")
    auf = []
    for i, a in enumerate(tr["aufgaben"], 1):
        body = md(a["text"].replace("{KIOSK}", str(u["kiosk"])))
        if a.get("plan"):
            body += plan_tabelle()
        if a.get("checks"):
            body += "<div class='checks'>%s</div>" % "".join("<span><span class='cb'></span>%s</span>" % md(c) for c in a["checks"])
        if a.get("linie"):
            body += "<div class='lin'></div>"
        auf.append("<div class='auf'><h2><span class='n'>%d</span>%s</h2>%s</div>" % (i, md(a["titel"]), body))
    vorn = "<div style='margin-top:3mm'>%s</div>" % auf[0]
    auf = auf[1:]
    p1 = ("<div class='page'><div class='grow'>%s%s<div class='sit'>%s %s</div><div class='fik'>%s</div>"
          "<div class='ivbox' data-id='%s'>%s</div>%s%s</div>%s</div>"
          % (kopf, foto, md(tr["situation"].split(" Das Interview")[0]), html.escape(t["einleitung"]),
             "Das Interview ist ausgedacht. Die Angaben über das Tier stimmen.", t["id"], pars, wh, vorn, fuss(k)))
    p2 = ("<div class='page'><div class='grow'>%s%s<div class='frei'><b>Freiwillig:</b>%s</div></div>%s</div>"
          % (kopf2, "".join(auf), md(tr["frei"]), fuss(k + 1)))
    return p1 + p2


def main():
    tr = json.loads((ROOT / "inhalt" / "training.json").read_text(encoding="utf-8"))
    iv = json.loads(QUELLE.read_text(encoding="utf-8"))
    T = {t["id"]: t for t in iv["tiere"]}
    AUS.mkdir(parents=True, exist_ok=True)
    n = 2 * len(tr["uebungen"])
    body = "".join(seiten(tr, u, T[u["interview"]], 2 * k + 1, n) for k, u in enumerate(tr["uebungen"]))
    pdf = AUS / ("%s.pdf" % tr["datei"])
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page()
        pg.set_content(doc(body, TR_CSS, "Training"), wait_until="load")
        pg.evaluate("document.fonts.ready")
        st = pg.evaluate(ZEILEN_JS)
        html_fertig = pg.content()
        o = render(pg, html_fertig, pdf)
        br.close()
    zeilen = {k: {s: ("Z. %d" % v[0] if len(v) == 1 else "Z. %d–%d" % (min(v), max(v))) for s, v in d.items()} for k, d in st.items()}
    (AUS / "zeilen_training.json").write_text(json.dumps(zeilen, ensure_ascii=False, indent=1), encoding="utf-8")
    mn, pages = font_sizes(pdf)
    print("%s  %d S.  kleinste Schrift %.2f pt (mind. 12, A4 Originalgröße)" % (pdf.name, pages, mn))
    fehler = []
    if o:
        fehler.append("Überlauf %s" % o)
    if pages != n:
        fehler.append("Seitenzahl %d statt %d" % (pages, n))
    if mn < 11.95:
        fehler.append("Schrift zu klein")
    for f in fehler:
        print("FEHLER:", f)
    sys.exit(1 if fehler else 0)


if __name__ == "__main__":
    main()
