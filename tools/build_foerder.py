#!/usr/bin/env python3
"""Zieldifferentes Material (Förderschwerpunkt Lernen) aus inhalt/foerder_etappeN.json.

Aufgabentypen: ankreuzen, sortieren, luecke, zuordnen, bild, hinweis.
Jedes Blatt hat unten einen Lösungsstreifen (auf dem Kopf) zum Umknicken.

Aufruf: python tools/build_foerder.py 1
Ausgabe: ausgabe/foerder/etappeN/Foerder_EtappeN_A4.pdf  (auf A5 verkleinert drucken)
         ausgabe/foerder/etappeN/GN{N}F_A4.pdf           (A4 Originalgröße)
"""
import html
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_material import FUSS, GN_CSS, UB_CSS, b64, doc, font_sizes, md, render  # noqa: E402
from playwright.sync_api import sync_playwright  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

ICON = {
    "ankreuzen": "<rect x='4' y='4' width='40' height='40' rx='5' fill='none' stroke='#111' stroke-width='4'/><path d='M12 12l24 24M36 12L12 36' stroke='#111' stroke-width='5' stroke-linecap='round'/>",
    "sortieren": "<rect x='4' y='6' width='17' height='36' fill='none' stroke='#111' stroke-width='4'/><rect x='27' y='6' width='17' height='36' fill='none' stroke='#111' stroke-width='4'/><path d='M8 16h9M8 24h9M31 16h9' stroke='#111' stroke-width='3'/>",
    "luecke": "<path d='M4 30h10M18 30h14M36 30h8' stroke='#111' stroke-width='4'/><path d='M18 34h14' stroke='#111' stroke-width='3' stroke-dasharray='3 3'/><path d='M4 18h40' stroke='#888' stroke-width='3'/>",
    "zuordnen": "<circle cx='10' cy='12' r='5' fill='#111'/><circle cx='10' cy='36' r='5' fill='#111'/><rect x='30' y='4' width='14' height='14' fill='none' stroke='#111' stroke-width='3'/><rect x='30' y='30' width='14' height='14' fill='none' stroke='#111' stroke-width='3'/><path d='M15 12l15 24M15 36l15-24' stroke='#111' stroke-width='3'/>",
    "bild": "<rect x='4' y='8' width='40' height='32' rx='4' fill='none' stroke='#111' stroke-width='4'/><circle cx='17' cy='20' r='5' fill='#111'/><path d='M8 36l12-10 8 6 6-5 8 9' fill='none' stroke='#111' stroke-width='3'/>",
    "ordnen": "<rect x='3' y='14' width='13' height='12' fill='none' stroke='#111' stroke-width='3'/><rect x='18' y='14' width='13' height='12' fill='#bbb' stroke='#111' stroke-width='3'/><rect x='33' y='14' width='12' height='12' fill='none' stroke='#111' stroke-width='3'/><path d='M4 38h40' stroke='#111' stroke-width='3'/>",
    "schreiben": "<path d='M10 38l4-12 22-22 8 8-22 22z' fill='none' stroke='#111' stroke-width='4' stroke-linejoin='round'/><path d='M6 44h36' stroke='#111' stroke-width='3'/>",
    "check": "<path d='M6 10l4 4 7-8M6 24l4 4 7-8M6 38l4 4 7-8' fill='none' stroke='#111' stroke-width='3.5' stroke-linecap='round'/><path d='M22 12h20M22 26h20M22 40h20' stroke='#111' stroke-width='3'/>",
    "hinweis": "<path d='M8 8h32v26H22l-10 8v-8H8z' fill='none' stroke='#111' stroke-width='4' stroke-linejoin='round'/><path d='M24 14v10M24 28v2' stroke='#111' stroke-width='4' stroke-linecap='round'/>",
}

F_CSS = UB_CSS + """
.page.f{font-size:16.5pt;line-height:1.32;padding:12mm 15mm 8mm 15mm}
.f .ukopf{margin-bottom:4mm}.f .nr{width:26mm;height:26mm}.f .nr b{font-size:30pt}.f .ukopf h1{font-size:26pt}
.fa{border:2pt solid var(--ink);border-radius:3.5mm;padding:3mm 4mm 3.5mm;margin-bottom:4mm}
.fa .ah{display:flex;gap:3mm;align-items:flex-start;margin-bottom:2.5mm}
.fa .ah svg{flex:0 0 11mm;width:11mm;height:11mm}
.fa .an{flex:0 0 9mm;height:9mm;border-radius:50%;background:var(--ink);color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:16pt}
.fa .at{font-weight:700;padding-top:1mm}
.kx{display:grid;gap:2mm 8mm}
.kx div{display:flex;gap:3mm;align-items:center}
.kx .box{flex:0 0 8mm;height:8mm;border:2pt solid var(--ink);border-radius:1.5mm}
.ws{border:2pt dashed var(--ink);border-radius:3mm;padding:2.5mm 4mm;margin-bottom:3mm;display:flex;flex-wrap:wrap;gap:2mm 8mm}
.ws b{width:100%;font-size:14pt;text-transform:uppercase;letter-spacing:.05em}
.sp{display:grid;gap:5mm}
.sp .col .h{font-weight:700;border-bottom:2.5pt solid var(--ink);padding-bottom:1mm}
.sp .col .l{height:12mm;border-bottom:1.2pt solid var(--soft)}
.lu{line-height:2.4}
.lu .gap{display:inline-block;min-width:52mm;border-bottom:1.5pt solid var(--ink);height:1em;vertical-align:baseline}
.zo{display:grid;grid-template-columns:1fr 1fr;gap:3mm 10mm}
.zo div{display:flex;justify-content:space-between;align-items:center;border-bottom:1pt solid var(--line);padding-bottom:1.5mm}
.zo .box{width:14mm;height:12mm;border:2pt solid var(--ink);border-radius:1.5mm}
.bildwrap{position:relative;width:fit-content;max-width:100%;margin:1mm auto 0}
.bildwrap img{width:100%;display:block;border-radius:2.5mm}
.mk{position:absolute;width:11mm;height:11mm;margin:-5.5mm 0 0 -5.5mm;border-radius:50%;background:#fff;border:2pt solid #000;
  display:flex;align-items:center;justify-content:center;font-weight:700;font-size:17pt;box-shadow:0 0 0 1.2mm rgba(255,255,255,.85)}
.loes{flex:0 0 auto;transform:rotate(180deg);border-bottom:1.5pt dashed var(--ink);padding-bottom:2mm;margin-top:2mm;font-size:14pt;color:var(--mid)}
.loes b{color:var(--ink)}
.knick{flex:0 0 auto;font-size:14pt;color:var(--mid);text-align:center;margin-top:2mm}
.fmat .s{font-size:18pt;line-height:1.45}
.wk{display:flex;flex-wrap:wrap;gap:3mm;margin-bottom:2mm}
.wk span{border:2pt solid var(--ink);border-radius:2mm;padding:1.5mm 4mm;background:#fff}
.zl{height:13mm;border-bottom:1.4pt solid var(--ink)}
.sa{display:flex;align-items:flex-end;gap:3mm}.sa .zl1{flex:1;border-bottom:1.4pt solid var(--ink);height:11mm}
.bh{font-size:14pt;font-weight:700;margin-bottom:3mm}
.fmat .s div{padding:.6mm 0;border-bottom:1pt solid var(--line)}
.fmat .cred{font-size:14pt;color:var(--mid);margin:1.5mm 0 4mm}
.mkk .p{display:flex;gap:4mm;border-bottom:1.2pt solid var(--line);padding:3mm 0}
.mkk .p b{flex:0 0 40mm}
.page.f.g{font-size:16pt}
.rm table.ziele td{padding:1mm 1.5mm}.rm .ergebnis{margin-bottom:3mm}
"""


def gaps(text: str):
    return re.findall(r"\{([^}]+)\}", text)


def aufgabe_html(a: dict, i: int, foto: dict) -> str:
    t = a["typ"]
    head = "<div class='ah'><span class='an'>%d</span><svg viewBox='0 0 48 48'>%s</svg><span class='at'>%s</span></div>" % (i, ICON[t], md(a["auftrag"]))
    body = ""
    if t == "ankreuzen":
        cols = a.get("spalten", 1)
        body = "<div class='kx' style='grid-template-columns:repeat(%d,1fr)'>%s</div>" % (cols, "".join(
            "<div><span class='box'></span><span>%s</span></div>" % md(x) for x, _ in a["items"]))
    elif t == "sortieren":
        n = max(len(w) for _, w in a["spalten"])
        body = "<div class='ws'><b>Wortspeicher</b>%s</div>" % "".join("<span>%s</span>" % md(w) for w in a["wortspeicher"])
        body += "<div class='sp' style='grid-template-columns:repeat(%d,1fr)'>%s</div>" % (len(a["spalten"]), "".join(
            "<div class='col'><div class='h'>%s</div>%s</div>" % (md(h), "<div class='l'></div>" * n) for h, _ in a["spalten"]))
    elif t == "luecke":
        ws = sorted(set(gaps(a["text"]) + a.get("extra", [])), key=str.lower)
        body = "<div class='ws'><b>Wortspeicher</b>%s</div>" % "".join("<span>%s</span>" % md(w) for w in ws)
        body += "<div class='lu'>%s</div>" % re.sub(r"\{[^}]+\}", "<span class='gap'></span>", md(a["text"]))
    elif t == "zuordnen":
        if a.get("optionen"):
            body = "<div class='ws'><b>Bedeutungen</b>%s</div>" % "".join("<span><b style='display:inline'>%d</b> %s</span>" % (k, md(o)) for k, o in enumerate(a["optionen"], 1))
        body += "<div class='zo'>%s</div>" % "".join("<div><span>%s</span><span class='box'></span></div>" % md(w) for w, _ in a["paare"])
    elif t == "ordnen":
        body = "<div class='wk'>%s</div><div class='zl'></div><div class='zl'></div>" % "".join("<span>%s</span>" % md(k) for k in a["karten"])
    elif t == "schreiben":
        body = "<div class='sa'><span>%s</span><span class='zl1'></span></div><div class='zl'></div>" % md(a.get("anfang", ""))
    elif t == "check":
        body = "<div class='kx'>%s</div>" % "".join("<div><span class='box'></span><span>%s</span></div>" % md(x) for x in a["items"])
    elif t == "bild":
        body = bild_html(foto, "70mm")
    return "<div class='fa'>%s%s</div>" % (head, body)


def bild_html(foto: dict, hoehe: str = "") -> str:
    style = " style='max-height:%s;width:auto;margin:0 auto'" % hoehe if hoehe else ""
    mk = "".join("<span class='mk' style='left:%.1f%%;top:%.1f%%'>%d</span>" % (x, y, n) for n, x, y in foto["punkte"])
    return "<div class='bildwrap'><img src='data:image/jpeg;base64,%s' alt='%s'%s>%s</div>" % (
        b64(ROOT / foto["datei"]), html.escape(foto["alt"]), style, mk)


def loesung(aufgaben: list, start: int = 1) -> str:
    parts = []
    for i, a in enumerate(aufgaben, start):
        t = a["typ"]
        if t == "ankreuzen":
            r = ", ".join(x.replace("*", "") for x, ok in a["items"] if ok)
        elif t == "sortieren":
            r = " · ".join("%s: %s" % (h, ", ".join(w)) for h, w in a["spalten"])
        elif t == "luecke":
            r = ", ".join(gaps(a["text"]))
        elif t == "zuordnen":
            r = ", ".join("%s %s" % (w, z) for w, z in a["paare"])
        elif t == "ordnen":
            r = a["loesung"]
        elif t == "schreiben":
            r = "zum Beispiel: " + a["loesung"]
        else:
            continue
        parts.append("<b>%d:</b> %s" % (i, html.escape(r)))
    return "<div class='loes'><b>Lösung</b> · " + " &nbsp; ".join(parts) + "</div>"


def blatt_page(c: dict, b: dict, gruppe: list, start: int, teil: str = "") -> str:
    """Eine Seite mit den Aufgaben 'gruppe' (Nummerierung ab 'start')."""
    h = ["<div class='page f'><div class='grow'><div class='ukopf'><div class='nr'><span>Blatt</span><b>%s</b></div>"
         "<div><div class='meta'>Etappe %d · Schritt für Schritt%s</div><h1>%s</h1></div></div>" % (md(b["nr"]), c["etappe"], teil, md(b["titel"]))]
    h += [aufgabe_html(a, i, c["foto"]) for i, a in enumerate(gruppe, start)]
    hat_loesung = any(a["typ"] not in ("bild", "hinweis", "check") for a in gruppe)
    if hat_loesung:
        h.append("</div><div class='knick'>Fertig? Knicke den Streifen unten um und vergleiche.</div>%s" % loesung(gruppe, start))
    else:
        h.append("</div>")
    h.append("<div class='foot'><span>%s · Etappe %d</span><b>Blatt %s%s</b></div></div>" % (FUSS, c["etappe"], md(b["nr"]), teil.replace(" · ", " · ")))
    return "".join(h)


def paginate(pg, c: dict, b: dict, css: str) -> str:
    """Aufgaben der Reihe nach auf Seiten verteilen, bis eine Seite voll ist."""
    from build_material import render as _r
    tmp = ROOT / "ausgabe" / ".tmp_probe.pdf"
    seiten, akt = [], []
    for a in b["aufgaben"]:
        probe = akt + [a]
        start = sum(len(x) for x in seiten) + 1
        if akt and _r(pg, doc(blatt_page(c, b, probe, start, " · Seite x/x"), css, "probe"), tmp):
            seiten.append(akt)
            akt = [a]
        else:
            akt = probe
    seiten.append(akt)
    tmp.unlink(missing_ok=True)
    out, start = [], 1
    for k, g in enumerate(seiten, 1):
        teil = "" if len(seiten) == 1 else " · Seite %d/%d" % (k, len(seiten))
        out.append(blatt_page(c, b, g, start, teil))
        start += len(g)
    return "".join(out)


def material_page(c: dict) -> str:
    m = c["material"]
    wh = "<div class='wh'><b>Wörterhilfe</b>%s</div>" % "".join("<div><b>%s:</b> %s</div>" % (md(w), md(e)) for w, e in m["woerter"])
    rng = "%s–%s" % (c["blaetter"][0]["nr"], c["blaetter"][-1]["nr"])
    bh = "<div class='bh'>%s</div>" % md(m["bildhinweis"]) if m.get("bildhinweis") else ""
    return ("<div class='page f fmat'><div class='grow'><div class='ukopf'><div><div class='meta'>Material zu Blatt %s</div><h1>%s</h1></div></div>"
            "%s<div class='cred'>%s</div>%s<div class='s'>%s</div>%s</div>"
            "<div class='foot'><span>%s · Etappe %d</span><b>Material F</b></div></div>"
            % (rng, md(m["titel"]), bild_html(c["foto"], "72mm" if len(m["saetze"]) <= 10 else "44mm"), html.escape(c["foto"]["nachweis"]), bh,
               "".join("<div>%s</div>" % md(s) for s in m["saetze"]), wh, FUSS, c["etappe"]))


def merkkarte_page(c: dict) -> str:
    m = c["merkkarte"]
    return ("<div class='page f mkk'><div class='grow'><div class='ukopf'><div><div class='meta'>Merkkarte · Etappe %d</div><h1>%s</h1></div></div>%s</div>"
            "<div class='foot'><span>%s · Etappe %d</span><b>Merkkarte F</b></div></div>"
            % (c["etappe"], md(m["titel"]), "".join("<div class='p'><b>%s</b><span>%s</span></div>" % (md(a), md(b)) for a, b in m["punkte"]),
               FUSS, c["etappe"]))


GN_SEITEN = []  # wird in main() mit der Aufteilung der GN-Aufgaben gefüllt


def gn_aufgaben_seiten(c: dict, kopf) -> str:
    e = c["etappe"]
    out, start = [], 1
    for k, g in enumerate(GN_SEITEN, 2):
        out.append("<div class='page f g'><div class='grow'>%s%s</div><div class='foot'><span>%s · Etappe %d</span><b>Nachweis %dF · Seite %d</b></div></div>"
                   % (kopf("Gelingensnachweis %d · Aufgaben" % e, "Zeige dein Können"), "".join(aufgabe_html(a, i, c["foto"]) for i, a in enumerate(g, start)), FUSS, e, e, k))
        start += len(g)
    return "".join(out)


def gn_pages(c: dict) -> str:
    n = c["nachweis"]
    e = c["etappe"]
    kopf = lambda meta, h1: ("<div class='gkopf'><div><div class='meta'>%s</div><h1>%s</h1></div><div class='var'>Nachweis %dF</div></div>" % (meta, h1, e))
    namen = "<div class='namen'><div>Name:</div><div class='d'>Datum:</div></div>"
    p1 = ("<div class='page f fmat'><div class='grow'>%s%s%s<div class='s'>%s</div></div>"
          "<div class='foot'><span>%s · Etappe %d</span><b>Nachweis %dF · Seite 1</b></div></div>"
          % (kopf("Gelingensnachweis %d · Material" % e, md(n["titel"])), namen, bild_html(c["foto"], "88mm"),
             "".join("<div>%s</div>" % md(s) for s in c["material"]["saetze"]), FUSS, e, e))
    p2 = gn_aufgaben_seiten(c, kopf)
    rows = "".join(
        "<tr><td><span class='id'>%s</span> %s<span class='krit'>Erreicht, wenn: %s</span></td>"
        "<td class='c'><span class='cb'></span></td><td class='c'><span class='cb'></span></td><td class='u'>%s</td><td class='e'></td></tr>"
        % (z["id"], md(z["kind"]), md(z["lehrkraft"]), md(z["ueben"])) for z in n["ziele"])
    rows += "<tr><td>Eigenes Förderziel: ______________</td><td class='c'><span class='cb'></span></td><td class='c'><span class='cb'></span></td><td class='u'></td><td class='e'></td></tr>"
    p3 = ("<div class='page rm'><div class='grow'>%s<div class='krit' style='font-size:11pt;margin-bottom:2mm'>%s</div>"
          "<table class='ziele'><tr><th>Ziel</th><th>gezeigt</th><th>noch offen</th><th>Übe mit</th><th>erneut gezeigt am</th></tr>%s</table>"
          "<div class='ergebnis'><div class='sum box'>Ergebnis<b>___ / ___</b>Ziele gezeigt</div>"
          "<div class='ent box'><div><span class='cb'></span><b>80 %% der vereinbarten Ziele:</b> Du gehst weiter zu Etappe %d.</div>"
          "<div><span class='cb'></span><b>Noch nicht:</b> Übe die offenen Ziele. Dann zeigst du sie noch einmal.</div>"
          "<div class='sig'><div>Lehrkraft:</div><div>Datum:</div></div></div></div>"
          "<div class='fb'><div class='h'>Das gelingt dir schon:</div><div class='ln'></div></div>"
          "<div class='fb'><div class='h'>Dein nächster Schritt:</div><div class='ln'></div></div></div>"
          "<div class='foot'><span>%s · Etappe %d</span><b>Nachweis %dF · Rückmeldung</b></div></div>"
          % (kopf("Rückmeldung der Lehrkraft", "So weit bist du"), md(n["hinweis_lehrkraft"]), rows, e + 1, FUSS, e, e))
    return p1 + p2 + p3


def main(n: int):
    c = json.loads((ROOT / "inhalt" / f"foerder_etappe{n}.json").read_text(encoding="utf-8"))
    out = ROOT / "ausgabe" / "foerder" / f"etappe{n}"
    out.mkdir(parents=True, exist_ok=True)
    fail = []
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page()
        fp = out / f"Foerder_Etappe{n}_A4.pdf"
        body = merkkarte_page(c) + material_page(c) + "".join(paginate(pg, c, b, F_CSS) for b in c["blaetter"])
        o = render(pg, doc(body, F_CSS, f"Förder-Material Etappe {n}"), fp)
        if o:
            fail.append("Fördermaterial: Überlauf %s" % o)
        mn, pages = font_sizes(fp)
        print(f"Förder Etappe {n}      {pages} S.  kleinste Schrift {mn:5.2f} pt (mind. 14)")
        if mn < 13.95:
            fail.append("Fördermaterial: Schrift zu klein")
        if c.get("nachweis"):
            gp = out / f"GN{n}F_A4.pdf"
            GN_SEITEN.clear()
            aufs = c["nachweis"]["aufgaben"]
            GN_SEITEN.extend([aufs[:2], aufs[2:]] if len(aufs) > 2 else [aufs])
            o = render(pg, doc(gn_pages(c), F_CSS + GN_CSS.replace(".page{padding:12mm 15mm 9mm 15mm;font-size:14pt;line-height:1.3}", ""), f"GN{n}F"), gp)
            if o:
                fail.append("GN%dF: Überlauf %s" % (n, o))
            mn, pages = font_sizes(gp, list(range(len(GN_SEITEN) + 1)))
            print(f"GN{n}F (ohne Rückmeldung) {pages} S.  kleinste Schrift {mn:5.2f} pt (mind. 14)")
            if mn < 13.95:
                fail.append("GN%dF: Schrift zu klein" % n)
        br.close()
    print("ok" if not fail else "FEHLER:\n  " + "\n  ".join(fail))
    sys.exit(1 if fail else 0)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 1)
