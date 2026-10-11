#!/usr/bin/env python3
"""Erzeugt das lineare Arbeitsheft (A4, Originalgröße drucken) aus inhalt/arbeitsheft.json.

Das Heft führt zwei Kinder ohne Wahlentscheidungen durch die Reihe:
Etappe 1–3 mit Merkseiten (Inhalt 1:1 aus inhalt/etappeN.json), Material (vorhandene
Material-PDFs), Blatt 1–9 in Einzelschritten mit Kiosk-Nummer, Stopp-Seiten für
Gelingensnachweise, Probearbeit und Klassenarbeit, Pflichtübungen aus der Probearbeit,
Terminwahl (offen), Projekt P3 und Zusatzaufgaben.

Aufruf: python tools/build_arbeitsheft.py
Ausgabe: ausgabe/arbeitsheft/Arbeitsheft_Zootiere_A4.pdf
Prüft: Seitenüberlauf, Mindestschrift 14 pt (Fehler unter 12 pt), Seitenverweise.
"""
import json
import re
import sys
from pathlib import Path

import pymupdf as fitz
from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_material import b64, doc, md, svg_uri  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
AUS = ROOT / "ausgabe"
OUT = AUS / "arbeitsheft" / "Arbeitsheft_Zootiere_A4.pdf"
H = json.loads((ROOT / "inhalt" / "arbeitsheft.json").read_text(encoding="utf-8"))
ET = {n: json.loads((ROOT / "inhalt" / f"etappe{n}.json").read_text(encoding="utf-8")) for n in (1, 2, 3)}
FUSS = "Deutsch · Jahrgang 5 · Zootiere · Arbeitsheft"

CSS = """
.page{padding:13mm 15mm 9mm 15mm;font-size:15pt;line-height:1.35}
.foot{font-size:14pt;color:var(--mid);margin-top:3mm}
.foot b{color:var(--ink);font-size:14pt}
.lk,.lk *{font-size:14pt !important;line-height:1.3}
h1{font-size:25pt;line-height:1.12}
.kopf{display:flex;gap:4mm;align-items:stretch;border-bottom:2.5pt solid var(--ink);padding-bottom:3mm;margin-bottom:3.5mm}
.kopf .meta{font-size:14pt;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:var(--mid)}
.nr{border:2.5pt solid var(--ink);border-radius:3mm;min-width:21mm;text-align:center;padding:1mm 2mm;line-height:1}
.nr span{font-size:14pt;font-weight:700;text-transform:uppercase;display:block;margin-top:1mm}
.nr b{font-size:30pt;display:block}
.kiosk{margin-left:auto;border:2pt dashed var(--ink);border-radius:3mm;text-align:center;padding:1mm 3mm;line-height:1.05;min-width:27mm}
.kiosk span{display:block;font-size:14pt;font-weight:700;letter-spacing:.06em}
.kiosk b{font-size:24pt;display:block}
.brauch{background:var(--fill);border-radius:2mm;padding:1.5mm 3mm;margin-bottom:3mm}
.lies{border:1.5pt solid var(--ink);border-radius:3mm;padding:2mm 3.5mm;margin-bottom:3mm}
.lies>b:first-child{display:block;margin-bottom:.5mm}
.teil{font-weight:700;font-size:15pt;margin:2.5mm 0 1.5mm;display:flex;align-items:center;gap:2.5mm}
.teil .tag{border:1.5pt solid var(--ink);border-radius:1.5mm;padding:0 2mm;font-size:14pt;letter-spacing:.06em;text-transform:uppercase}
.st{display:grid;grid-template-columns:10mm 1fr 10mm;column-gap:2.5mm;align-items:start;
  border-top:1pt solid var(--line);padding:1.6mm 0 1.8mm;break-inside:avoid}
.st .n{width:9mm;height:9mm;border-radius:50%;border:1.6pt solid var(--ink);display:flex;align-items:center;justify-content:center;font-weight:700;font-size:14pt}
.st .ok{text-align:center;font-size:14pt;color:var(--mid);line-height:1.1}
.st .ok i{display:block;width:8mm;height:8mm;border:1.6pt solid var(--ink);border-radius:1.2mm;margin:0 auto .5mm}
.st .f{grid-column:2 / 4;margin-top:1.5mm}
.line{height:10mm}
.lnr{display:flex;align-items:flex-end;gap:2mm}.lnr .line{flex:1}
.zl{display:flex;gap:4mm;align-items:flex-end}.zl .line{flex:1}.zl .z{white-space:nowrap}
.blank{display:inline-block;border-bottom:1pt solid var(--ink);min-width:28mm;height:7mm;vertical-align:bottom}
.wahl{display:flex;gap:9mm;flex-wrap:wrap}.wahl span{white-space:nowrap}
table.t{border-collapse:collapse;width:100%}
table.t th,table.t td{border:1.2pt solid var(--ink);padding:1mm 2mm;text-align:left;vertical-align:top}
table.t th{font-size:14pt;background:var(--fill)}
table.t td{height:12mm}
table.t.k td{height:auto;padding:1.5mm 2mm}
.speicher{display:flex;flex-wrap:wrap;gap:2mm;margin:1mm 0 2mm}
.speicher span{border:1.2pt solid var(--ink);border-radius:2mm;padding:.5mm 2.5mm}
.plan4{display:grid;grid-template-columns:1fr 1fr;gap:3mm;margin-top:2mm}
.plan4>div{border:1.5pt solid var(--ink);border-radius:2.5mm;padding:1mm 3mm 2mm}
.plan4 .line{height:9.5mm}
.tipp{border-left:3pt solid var(--ink);background:var(--fill);padding:1.5mm 3mm;border-radius:0 2mm 2mm 0;margin:2.5mm 0}
.tipp b{margin-right:2mm}
.endk{border:2pt dashed var(--ink);border-radius:3mm;padding:2.5mm 3.5mm;margin-top:3mm;display:flex;gap:4mm;align-items:center}
.endk .kz{font-size:30pt;font-weight:700;border:2pt solid var(--ink);border-radius:2mm;padding:0 3mm;line-height:1.15}
.foto{max-width:100%;max-height:92mm;display:block;border-radius:2mm;margin-bottom:1mm}
.cred{font-size:14pt;color:var(--mid);margin-bottom:2mm}
.fill{flex:1 1 0;min-height:0;overflow:hidden}.fill div{height:10.5mm;border-bottom:1pt solid #777}
.textf{display:flex;flex-direction:column;flex:1 1 0;min-height:0}
.grow.flex{display:flex;flex-direction:column}
/* Merkseiten */
.msec{font-size:14pt;line-height:1.32;border:1.5pt solid var(--ink);border-radius:3mm;padding:2.5mm 4mm 2mm;margin-bottom:3.5mm}
.msec h2{font-size:17pt;display:flex;gap:2.5mm;align-items:center;margin-bottom:1.5mm}
.msec h2 .n{display:inline-flex;width:9mm;height:9mm;border-radius:50%;border:1.6pt solid var(--ink);font-size:14pt;align-items:center;justify-content:center;flex:0 0 auto}
.msec .blk{margin-bottom:1.6mm}
.msec .lab{font-weight:700}
.msec .ans{border-left:3pt solid var(--ink);background:var(--fill);padding:1.2mm 2.5mm;border-radius:0 2mm 2mm 0}
.msec img{max-width:100%;max-height:70mm;display:block;margin:1mm 0}
/* Stopp */
.stopp{border:5pt solid var(--ink);border-radius:5mm;padding:5mm 6mm;margin:4mm 0 5mm;text-align:center}
.stopp .w{font-size:56pt;font-weight:700;letter-spacing:.12em;line-height:1}
.stopp .u{font-size:20pt;font-weight:700;margin-top:2mm}
ol.big{padding-left:9mm}ol.big li{margin-bottom:2.5mm}
.lkbox{border:1.5pt solid var(--ink);border-radius:3mm;padding:3mm 4mm;margin-top:4mm}
.lkbox h3{font-size:14pt;text-transform:uppercase;letter-spacing:.05em;margin-bottom:2mm}
.lkbox .row{display:flex;gap:4mm;align-items:flex-end;margin:2.5mm 0;flex-wrap:wrap}
.weiter{border:2.5pt solid var(--ink);border-radius:3mm;padding:3mm 5mm;margin-top:5mm;font-size:18pt;font-weight:700;text-align:center}
.cbx{display:inline-block;width:6.5mm;height:6.5mm;border:1.6pt solid var(--ink);border-radius:1mm;vertical-align:-1.3mm;margin-right:2mm}
/* Weg / Legende */
.leg{display:grid;grid-template-columns:38mm 1fr;gap:3mm 5mm;align-items:center;margin-bottom:3mm}
.sym{border:1.8pt solid var(--ink);border-radius:2.5mm;text-align:center;font-weight:700;padding:2mm 1mm;font-size:15pt}
.sym.d{border-style:dashed}.sym.s{border-width:4pt;letter-spacing:.1em}
.weg{width:100%;border-collapse:collapse}
.weg td{border-bottom:1pt solid var(--line);padding:.9mm 1.5mm;vertical-align:middle}
.weg td.s{text-align:right;white-space:nowrap;width:24mm}
.weg tr.e td{font-weight:700;border-bottom:1.6pt solid var(--ink);padding-top:3mm}
.weg tr.stp td{font-weight:700}
.cover{display:flex;flex-direction:column;justify-content:center;height:100%}
.cover .t{font-size:40pt;font-weight:700;line-height:1.1}
.cover .u{font-size:20pt;margin:4mm 0 14mm}
.feldz{display:flex;align-items:flex-end;gap:4mm;margin:7mm 0;font-size:17pt}
.feldz .line{flex:1;height:12mm}
.pubox{border:2pt solid var(--ink);border-radius:3mm;padding:2.5mm 4mm;margin-bottom:3mm;display:flex;gap:6mm;align-items:center;flex-wrap:wrap}
"""


def line(n=1, cls="line"):
    return "".join("<div class='%s' style='border-bottom:1pt solid #777'></div>" % cls for _ in range(n))


def cb():
    return "<span class='cbx'></span>"


# ---------------------------------------------------------------- Seitenverweise
R: dict = {}
MESS = [False]


def sub(t: str) -> str:
    def rep(m):
        k = m.group(1)
        if MESS[0]:
            return "99"
        if k not in R:
            raise KeyError("Unbekannte Seitenmarke: " + k)
        return str(R[k])
    return re.sub(r"\{S:([\w]+)\}", rep, t)


def M(t: str) -> str:
    t = md(sub(t))
    return t.replace("[__]", "<span class='blank'></span>")


# ---------------------------------------------------------------- Felder
def feld(f: str) -> str:
    if not f:
        return ""
    m = re.fullmatch(r"L(\d)", f)
    if m:
        return line(int(m.group(1)))
    if f == "N2":
        return "".join("<div class='lnr'><b>%d.</b>%s</div>" % (i, line()) for i in (1, 2))
    if f == "H1":
        return "<div style='height:6mm'></div>" + line()
    if f == "Z":
        return "<div class='zl'>%s<span class='z'>Zeile: Z. <span class='blank' style='min-width:20mm'></span></span></div>" % line()
    if f == "AB":
        return "<div class='wahl'><span>%sText A</span><span>%sText B</span></div>" % (cb(), cb())
    if f == "JN":
        return "<div class='wahl'><span>%sja</span><span>%snein</span></div>" % (cb(), cb())
    if f == "JNZ":
        return "<div class='wahl'><span>%sja, in Zeile Z. <span class='blank' style='min-width:20mm'></span></span><span>%snein</span></div>" % (cb(), cb())
    if f == "ZAHL":
        return "<div>Anzahl der Merkmale: <span class='blank' style='min-width:18mm'></span></div>"
    if f in ("KOFFER",):
        return ("<div class='wahl' style='align-items:flex-end;gap:3mm'><span class='blank' style='min-width:60mm'></span><b>+</b>"
                "<span class='blank' style='min-width:60mm'></span></div>")
    if f == "ARTIKEL":
        return "<div><span class='blank' style='min-width:25mm'></span> Körperlänge</div>"
    if f == "TAB_KOERPER":
        rows = "".join("<tr><td style='width:12mm'><b>%d</b></td><td></td><td></td></tr>" % i for i in (1, 2))
        return "<table class='t'><tr><th></th><th>Körperteil</th><th>genaues Merkmal</th></tr>%s</table>" % rows
    if f == "TAB_MERKMAL":
        rows = "".join("<tr><td style='width:12mm'><b>%d</b></td><td></td><td style='width:32mm'>Z.</td></tr>" % i for i in range(1, 5))
        return "<table class='t'><tr><th></th><th>äußeres Merkmal</th><th>Zeile</th></tr>%s</table>" % rows
    if f == "TAB_FEHLER":
        rows = "".join("<tr><td></td><td></td></tr>" for _ in range(4))
        return "<table class='t'><tr><th>So stand es da</th><th>So ist es richtig</th></tr>%s</table>" % rows
    if f == "PLAN4":
        box = "<div><div class='line' style='height:9mm;border-bottom:1.5pt solid #111'></div>%s</div>" % line(5)
        return "<div class='plan4'>%s</div>" % (box * 4)
    if f == "PRUEF6":
        pr = ["Passt die Aussage zum Interview? Gilt sie für alle Fischotter?", "Ist der Satz vollständig?",
              "Steht das Verb im Präsens und passt es?", "Sind die Wörter genau?",
              "Beginnen Satz und Nomen groß?", "Steht am Ende ein Punkt?"]
        rows = "".join("<tr><td>%s</td>%s</tr>" % (p, "<td style='width:15mm;height:11mm'></td>" * 4) for p in pr)
        return ("<table class='t'><tr><th>Prüffrage (Merkseiten 2)</th>%s</tr>%s</table>"
                % ("".join("<th style='text-align:center'>Satz %d</th>" % i for i in range(1, 5)), rows))
    if f == "K16":
        k = ["K1 Informationen", "K2 Aussehen", "K3 Aufbau", "K4 Sachlich", "K5 Verständlich", "K6 Schreibung"]
        return "<div class='wahl' style='gap:3mm 7mm'>%s</div>" % "".join("<span>%s%s</span>" % (cb(), x) for x in k)
    if f == "PLAN7":
        rows = [("Überblick", "Tiername"), ("Überblick", "Maß der Art (Einheit, Bezug)")] + \
               [("Aussehen", "Merkmal %d" % i) for i in range(1, 5)] + [("Lebensraum", ""), ("Nahrung", "")]
        tr = "".join("<tr><td style='width:34mm'><b>%s</b><br><span style='color:#444'>%s</span></td><td></td>"
                     "<td style='width:22mm'>Z.</td><td style='width:20mm'></td></tr>" % r for r in rows)
        return ("<table class='t plan7'><tr><th>Bereich</th><th>Stichwort</th><th>Zeile</th><th>geprüft</th></tr>%s</table>"
                % tr.replace("<td></td>", "<td style='height:20mm'></td>"))
    raise ValueError("Unbekanntes Feld: " + f)


def schritt(n: int, s: dict) -> str:
    return ("<div class='st'><div class='n'>%d</div><div>%s</div><div class='ok'><i></i></div>"
            "%s</div>" % (n, M(s["t"]), ("<div class='f'>%s</div>" % feld(s["f"])) if s.get("f") else ""))


# ---------------------------------------------------------------- Seitenrahmen
def page(inner: str, nr_label: str, cls: str = "", grow_cls: str = "") -> str:
    return ("<div class='page %s'><div class='grow %s'>%s</div><div class='foot'><span>%s</span><b>Seite %s</b></div></div>"
            % (cls, grow_cls, inner, FUSS, nr_label))


def foto_html(c: dict, h: str = "") -> str:
    return ("<img class='foto' %s src='data:image/jpeg;base64,%s' alt='%s'><div class='cred'>%s</div>"
            % (h, b64(ROOT / c["foto"]["datei"]), c["foto"]["alt"], c["foto"]["nachweis"]))


def blatt_kopf(b: dict, teil: str) -> str:
    return ("<div class='kopf'><div class='nr'><span>Blatt</span><b>%d</b></div><div><div class='meta'>Etappe %d · Pflicht%s</div>"
            "<h1>%s</h1></div><div class='kiosk'><span>KIOSK</span><b>%d</b></div></div>" % (b["nr"], b["etappe"], teil, M(b["titel"]), b["nr"]))


def blatt_items(b: dict) -> tuple[str, list, str]:
    """Liefert Kopfzusatz der ersten Seite, Elemente (html, marke, flags) und Abschlussbox."""
    erst = ("<div class='brauch'><b>Du brauchst:</b> %s<br><b>Du steckst fest?</b> Geh zum Kiosk. Tippe %d. Wähle „Tipp“.</div>"
            % (M(b["brauchst"]), b["nr"]))
    items, n = [], 1
    for el in [e for s in b["seiten"] for e in s]:
        t, flags, marke = el["typ"], {}, None
        if t == "lies":
            x = "<div class='lies'><b>%s</b>%s</div>" % (M(el["titel"]), M(el["text"]))
        elif t == "teil":
            x = "<div class='teil'><span class='tag'>%s</span></div>" % M(el["titel"])
            flags["klebt"] = True
        elif t == "text":
            x = "<div style='margin-bottom:1.5mm'>%s</div>" % M(el["text"])
            flags["klebt"] = True
        elif t == "tipp":
            x = "<div class='tipp'><b>Achte darauf:</b>%s</div>" % M(el["text"])
        elif t == "foto":
            x = foto_html(ET[1], "style='max-height:88mm'")
        elif t == "speicher":
            x = ("<div class='lies'><b>%s</b><div class='speicher'>%s</div></div>"
                 % (el["titel"], "".join("<span>%s</span>" % w for w in el["woerter"])))
        elif t == "feld" and el["f"] == "TEXT_A":
            x = ("<div class='textf' style='margin-top:2mm;min-height:75mm'><div><b>Überschrift:</b></div>"
                 "<div class='line' style='border-bottom:1.5pt solid #111'></div><div class='fill'>" + "<div></div>" * 28 + "</div></div>")
            flags["fill"] = True
        elif t == "feld" and el["f"] == "TEXT_B":
            x = "<div class='textf'><div style='margin-bottom:1mm'><b>Dein Text geht hier weiter.</b></div><div class='fill'>" + "<div></div>" * 28 + "</div></div>"
            flags.update(fill=True, neu=True)
        elif t == "feld":
            x = "<div style='margin-top:1mm'>%s</div>" % feld(el["f"])
            if el["f"] in ("PLAN7", "PLAN4"):
                marke = el["f"].lower()
                flags["neu"] = True
        elif t == "schritt":
            x = schritt(n, el)
            n += 1
        else:
            raise ValueError(t)
        items.append((x, marke, flags))
    ende = ("<div class='endk'><span class='kz'>%d</span><div><b>Blatt %d ist fertig?</b> Geh zum Kiosk. Tippe <b>%d</b>. "
            "Wähle „Lösung“. Vergleiche und verbessere mit Bleistift.</div><div class='ok' style='text-align:center;min-width:12mm'>"
            "<i style='display:block;width:8mm;height:8mm;border:1.6pt solid #111;border-radius:1.2mm;margin:0 auto'></i></div></div>"
            % (b["nr"], b["nr"], b["nr"]))
    return erst, items, ende


# ---------------------------------------------------------------- Merkseiten (Inhalt 1:1 aus etappeN.json)
def msec(i: int, s: dict, c: dict) -> str:
    h = ["<section class='msec'><h2><span class='n'>%d</span>%s</h2>" % (i, md(s["titel"]))]
    if s.get("foto"):
        h.append("<img src='data:image/jpeg;base64,%s' alt='%s' style='max-height:60mm'><div class='cred'>%s</div>"
                 % (b64(ROOT / c["foto"]["datei"]), c["foto"]["alt"], c["foto"]["nachweis"]))
    if s.get("grafik"):
        h.append("<img src='%s' alt='%s' style='max-height:62mm'>" % (svg_uri(s["grafik"]), s.get("grafik_alt", "")))
    for lab, txt in s["bloecke"]:
        cls = "ans" if lab.startswith("Gesicherte Antwort") else ""
        h.append("<div class='blk %s'><span class='lab'>%s:</span> %s</div>" % (cls, md(lab), md(txt)))
    h.append("</section>")
    return "".join(h)


def merk_kopf(n: int, teil: int, gesamt: int) -> str:
    return ("<div class='kopf'><div class='nr'><span>Merk</span><b>%d</b></div><div><div class='meta'>Merkseiten %d · zum Nachlesen · %d von %d</div>"
            "<h1>%s</h1></div></div>" % (n, n, teil, gesamt, md(ET[n]["titel"])))


# ---------------------------------------------------------------- Sonderseiten
def cover() -> str:
    return page("<div class='cover'><div class='meta' style='font-size:15pt;font-weight:700;letter-spacing:.06em'>DEUTSCH · JAHRGANG 5</div>"
                "<div class='t'>%s</div><div class='u'>%s</div>"
                "<div class='feldz'><b>Mein Name:</b>%s</div><div class='feldz'><b>Mein Partnerkind:</b>%s</div>"
                "<div class='feldz'><b>Meine Lehrkraft:</b>%s</div>"
                "<div class='lies' style='margin-top:10mm'>In diesem Heft arbeitest du Seite für Seite. Du weißt immer, was als Nächstes kommt. "
                "Das Partnerkind trägt die Lehrkraft ein.</div></div>"
                % (H["titel"], H["untertitel"], line(), line(), line()), str(R["cover"]))


def legende() -> str:
    sym = {"schritt": "<div class='sym'><span class='cbx' style='margin:0'></span> 1</div>",
           "kiosk": "<div class='sym d'>KIOSK 3</div>", "stopp": "<div class='sym s'>STOPP</div>",
           "merk": "<div class='sym'>MERK</div>", "material": "<div class='sym'>MATERIAL</div>"}
    rows = "".join("%s<div><b>%s:</b> %s</div>" % (sym[k], t, M(x)) for k, t, x in H["so_arbeitest_du"])
    leiter = "".join("<li>%s</li>" % x for x in H["loesungsleiter"])
    regeln = "".join("<li>%s</li>" % x for x in H["regeln"])
    return page("<div class='kopf'><div><div class='meta'>Arbeitsheft</div><h1>So arbeitest du mit diesem Heft</h1></div></div>"
                "<div class='leg'>%s</div><div class='lies'><b>Die Regeln</b><ol class='big'>%s</ol></div>"
                "<div class='lies'><b>Du steckst fest? Die Lösungsleiter</b><ol class='big'>%s</ol></div>" % (rows, regeln, leiter),
                str(R["legende"]))


def weg() -> str:
    def z(txt, key, cls=""):
        return "<tr class='%s'><td>%s %s</td><td class='s'>Seite %d</td></tr>" % (cls, cb(), txt, R[key])
    t = []
    t.append("<tr class='e'><td colspan='2'>Etappe 1 · Informationen finden und ordnen</td></tr>")
    t += [z("Merkseiten 1 lesen", "mb1"), z("Blatt 1 · Welche Beschreibung hilft?", "b1"), z("Blatt 2 · Schau genau hin", "b2"),
          z("Blatt 3 · Im Interview suchen", "b3"), z("Blatt 4 · Informationen ordnen", "b4"), z("STOPP 1 · Gelingensnachweis 1", "gn1", "stp")]
    t.append("<tr class='e'><td colspan='2'>Etappe 2 · Sachlich und genau formulieren</td></tr>")
    t += [z("Merkseiten 2 lesen", "mb2"), z("Blatt 5 · Treffende Wörter", "b5"), z("Blatt 6 · Sachliche Sätze", "b6"),
          z("STOPP 2 · Gelingensnachweis 2", "gn2", "stp")]
    t.append("<tr class='e'><td colspan='2'>Etappe 3 · Eine Tierbeschreibung schreiben und prüfen</td></tr>")
    t += [z("Merkseiten 3 lesen", "mb3"), z("Blatt 7 · Dein Schreibplan", "b7"), z("Blatt 8 · Deine Tierbeschreibung", "b8"),
          z("Blatt 9 · Prüfen und verbessern", "b9"), z("STOPP 3 · Probearbeit", "pa", "stp")]
    t.append("<tr class='e'><td colspan='2'>Nach der Probearbeit</td></tr>")
    t += [z("Pflichtübungen aus der Probearbeit", "auswertung"), z("STOPP 4 · Pflichtübungen zeigen", "pu", "stp"),
          z("Termin für die Klassenarbeit festlegen", "termin"), z("Projekt · Zwei Tiere vergleichen", "projekt"),
          z("STOPP 5 · Klassenarbeit", "ka", "stp")]
    return page("<div class='kopf'><div><div class='meta'>Arbeitsheft · Übersicht</div><h1>Dein Weg durch das Heft</h1></div></div>"
                "<table class='weg'>%s</table>" % "".join(t), str(R["weg"]))


def etappe_start(n: int) -> str:
    c = ET[n]
    e = H["etappen"][str(n)]
    li = "".join("<li>%s</li>" % M(x) for x in e["start"])
    return page("<div class='kopf'><div class='nr'><span>Etappe</span><b>%d</b></div><div><div class='meta'>Start</div>"
                "<h1>%s</h1></div></div><div class='lies' style='font-size:17pt'><b>Dein Ziel</b>%s</div>"
                "<div class='tipp'><b>Lernbuddy:</b>%s</div><div class='teil'><span class='tag'>So geht diese Etappe</span></div>"
                "<ol class='big'>%s</ol>" % (n, md(c["titel"]), md(c["ziel"]), M(e["lernbuddy"]), li), str(R["e%d" % n]))


def stopp(key: str) -> str:
    s = H["stopps"][key]
    li = "".join("<li>%s</li>" % M(x) for x in s["text"])
    lk = ""
    if key in ("gn1", "gn2"):
        nxt = R["e2" if key == "gn1" else "e3"]
        lk = ("<div class='lkbox lk'><h3>Die Lehrkraft füllt aus</h3>"
              "<div class='row'><b>Ergebnis:</b> <span class='blank' style='min-width:16mm'></span> / 5 Ziele gezeigt</div>"
              "<div class='row'>%s<b>4 oder 5 Ziele:</b> Du machst weiter auf Seite %d.</div>"
              "<div class='row'>%s<b>Weniger als 4 Ziele:</b> Übe mit %s</div>"
              "<div class='row'>Erneut gezeigt am: <span class='blank' style='min-width:40mm'></span></div>"
              "<div class='row'>Datum: <span class='blank' style='min-width:40mm'></span> Unterschrift: <span class='blank' style='min-width:60mm'></span></div></div>"
              % (cb(), nxt, cb(), s["uebe"]))
        weiter = "Weiter geht es erst, wenn die Lehrkraft unterschrieben hat: Seite %d." % nxt
    elif key == "pa":
        lk = ("<div class='lkbox lk'><h3>Die Lehrkraft füllt aus</h3>"
              "<div class='row'>Probearbeit geschrieben am: <span class='blank' style='min-width:40mm'></span></div>"
              "<div class='row'>Rückmeldung zurückgegeben am: <span class='blank' style='min-width:40mm'></span></div></div>")
        weiter = "Wenn du die Probearbeit mit Rückmeldung zurückbekommst: Seite %d." % R["auswertung"]
    elif key == "pu":
        rows = "".join("<tr><td>%s %s</td><td></td><td></td></tr>" % (i, t) for i, t, _ in H["auswertung"]["ziele"])
        lk = ("<div class='lkbox lk'><h3>Die Lehrkraft füllt aus</h3><table class='t'><tr><th>Ziel</th><th>jetzt gezeigt</th>"
              "<th>erneut gezeigt am</th></tr>%s</table>"
              "<div class='row'>Datum: <span class='blank' style='min-width:40mm'></span> Unterschrift: <span class='blank' style='min-width:60mm'></span></div></div>" % rows)
        weiter = "Weiter geht es erst, wenn die Lehrkraft unterschrieben hat: Seite %d." % R["termin"]
    else:
        lk = ("<div class='lkbox lk'><h3>Die Lehrkraft füllt aus</h3>"
              "<div class='row'>Klassenarbeit geschrieben am: <span class='blank' style='min-width:40mm'></span></div></div>")
        weiter = "Nach der Klassenarbeit: Projekt auf Seite %d." % R["projekt"]
    return page("<div class='stopp'><div class='w'>STOPP %d</div><div class='u'>%s</div></div><ol class='big'>%s</ol>%s"
                "<div class='weiter'>%s</div>" % (s["nummer"], s["titel"], li, lk, weiter), str(R[key]))


def auswertung() -> str:
    a = H["auswertung"]
    li = "".join("<p style='margin-bottom:2mm'>%s</p>" % M(x) for x in a["text"])
    rows = "".join("<tr><td><b>%s</b> %s</td><td style='text-align:center'>%s</td><td style='text-align:center'>%s</td><td>P%s · Seite %d</td></tr>"
                   % (i, t, cb(), cb(), i[-1], R[m]) for i, t, m in a["ziele"])
    rows += "<tr><td><b>Dein nächster Schritt</b></td><td colspan='2' style='text-align:center'>immer</td><td>P0 · Seite %d</td></tr>" % R["pu0"]
    ablauf = ("<div class='lies' style='text-align:center;font-weight:700'>Probearbeit → Rückmeldung → <u>Pflichtübungen</u> → STOPP 4: zeigen → "
              "Termin → Projekt → Klassenarbeit</div>")
    return page("<div class='kopf'><div><div class='meta'>Nach der Probearbeit</div><h1>%s</h1></div></div>%s%s"
                "<table class='t k'><tr><th>Ziel</th><th style='width:24mm'>gezeigt</th><th style='width:24mm'>noch offen</th>"
                "<th style='width:36mm'>Pflichtübung</th></tr>%s</table>"
                "<div class='lkbox lk'><h3>Die Lehrkraft füllt aus</h3><div class='row'><b>Ergebnis der Probearbeit:</b> "
                "<span class='blank' style='min-width:16mm'></span> / 5 Ziele gezeigt</div>"
                "<div class='row'>Kreuzen Sie auch auf jeder Pflichtübung „Pflicht für dich“ oder „nicht nötig“ an.</div></div>"
                "<div class='weiter'>Beginne mit der ersten Pflichtübung auf Seite %d.</div>"
                % (a["titel"], ablauf, li, rows, R["pu0"]), str(R["auswertung"]))


def pu_unit(i: int, p: dict):
    alle = H["pflichtuebungen"]
    nxt = R.get(alle[i + 1]["marke"] if i + 1 < len(alle) else "pu", 99) if not MESS[0] else 99

    def kopf(k, n):
        teil = (" · Teil %d von %d" % (k + 1, n)) if n > 1 else ""
        return ("<div class='kopf'><div class='nr'><span>Übung</span><b>P%d</b></div><div><div class='meta'>Pflichtübung · %s%s</div>"
                "<h1>%s</h1></div></div>" % (i, p["ziel"], teil, p["titel"]))
    if p.get("immer"):
        box = "<div class='pubox'><b>PFLICHT für alle.</b> Diese Übung machst du immer.</div>"
    else:
        box = ("<div class='pubox lk'><b>Lehrkraft:</b><span>%s<b>PFLICHT für dich</b></span>"
               "<span>%snicht nötig → weiter auf Seite %s</span></div>" % (cb(), cb(), nxt))
    erst = box
    if p.get("lk_feld"):
        erst += "<div class='lkbox lk' style='margin:0 0 2mm'><h3>%s</h3>%s</div>" % (p["lk_feld"], line(2))
    if p.get("blatt"):
        erst += ("<div class='brauch'><b>Du brauchst:</b> deine Probearbeit mit Rückmeldung<br>"
                 "<b>Nachlesen:</b> Blatt %s (Seite %s) und Checkliste K1–K6 (Seite %s)</div>"
                 % (p["blatt"][1:], sub("{S:%s}" % p["blatt"]), sub("{S:check}")))
    items = [(schritt(k + 1, x), None, {}) for k, x in enumerate(p["schritte"])]
    tail = "<div class='weiter' style='font-size:15pt'>Fertig? Weiter auf Seite %s.</div>" % nxt
    return kopf, erst, items, tail


def projekt_unit():
    p = H["projekt"]

    def kopf(k, n):
        return ("<div class='kopf'><div class='nr'><span>Projekt</span><b>%s</b></div><div><div class='meta'>Projekt · Teil %d von %d</div>"
                "<h1>%s</h1></div></div>" % (p["kennung"], k + 1, n, p["titel"]))
    erst = "<div class='lies'>%s</div><div class='brauch'><b>Du brauchst:</b> %s</div>" % (M(p["intro"]), M(p["material"]))
    items = [(schritt(i + 1, x), None, {}) for i, x in enumerate(p["schritte1"])]
    rows = "".join("<tr><td><b>%s</b></td><td style='height:30mm'></td><td style='height:30mm'></td><td style='width:18mm'></td></tr>" % m
                   for m in p["merkmale"])
    items.append(("<div style='margin-top:2mm'><table class='t'><tr><th style='width:26mm'>Merkmal</th><th>Fischotter (mit Zeile)</th>"
                  "<th>Erdmännchen (mit Zeile)</th><th>geprüft</th></tr>%s</table></div>" % rows, None, {}))
    items.append(("<div class='lies'><b>Satzmuster für Vergleichssätze</b><ul style='padding-left:7mm'>%s</ul></div>"
                  % "".join("<li><i>%s</i></li>" % x for x in p["muster"]), None, {"neu": True}))
    n0 = len(p["schritte1"])
    items += [(schritt(n0 + i + 1, x), None, {}) for i, x in enumerate(p["schritte2"])]
    tail = ("<div class='lies'><b>Das Projekt gelingt, wenn:</b><ul style='padding-left:7mm'>%s</ul></div>"
            % "".join("<li>%s</li>" % x for x in p["gelingt"]))
    return kopf, erst, items, tail


def zusatz_unit():
    z = H["zusatz"]

    def kopf(k, n):
        return "<div class='kopf'><div><div class='meta'>Zusatzaufgaben · %d von %d</div><h1>%s</h1></div></div>" % (k + 1, n, z["titel"])
    items = []
    for a in z["aufgaben"]:
        ki = ("Kiosk %d" % a["kiosk"]) if a["kiosk"] else "Lehrkraft zeigen"
        items.append(("<div class='st' style='grid-template-columns:14mm 1fr 32mm'><div class='n' style='width:12mm;border-radius:2mm'>Z%d</div>"
                      "<div>%s</div><div class='ok lk' style='text-align:left'>%s angekreuzt<br><span style='color:#444'>%s</span></div>"
                      "<div class='f'>%s</div></div>" % (a["nr"], M(a["text"]), cb(), ki, feld(a["f"])), None, {}))
    return kopf, "<div class='lies'>%s</div>" % M(z["text"]), items, ""


def blatt_unit(b: dict):
    erst, items, ende = blatt_items(b)

    def kopf(k, n):
        return blatt_kopf(b, (" · Teil %d von %d" % (k + 1, n)) if n > 1 else "")
    return kopf, erst, items, ende


def merk_unit(n: int):
    def kopf(k, g):
        return merk_kopf(n, k + 1, g)
    items = [(msec(i + 1, s, ET[n]), None, {}) for i, s in enumerate(ET[n]["input"])]
    return kopf, "", items, ""


def termin() -> str:
    t = H["termin"]
    li = "".join("<p style='margin-bottom:2mm'>%s</p>" % M(x) for x in t["text"])
    boxes = "".join("<div class='lies' style='flex:1'><b style='font-size:17pt'>%s %s</b>%s<div class='row' style='margin-top:4mm'>"
                    "Datum: <span class='blank' style='min-width:45mm'></span></div></div>" % (cb(), a, b) for a, b in t["termine"])
    bis = "".join("<li>%s</li>" % M(x) for x in t["bis"])
    return page("<div class='kopf'><div><div class='meta'>Klassenarbeit</div><h1>%s</h1></div></div>%s"
                "<div style='display:flex;gap:5mm;margin:3mm 0'>%s</div>"
                "<div class='lkbox lk'><h3>Termin vereinbart</h3><div class='row'>Unterschrift Lehrkraft: <span class='blank' style='min-width:70mm'></span></div></div>"
                "<div class='teil'><span class='tag'>Bis zu deinem Termin</span></div><ol class='big'>%s</ol>"
                "<div class='tipp'><b>Am Termin:</b>Schlage STOPP 5 auf (Seite %d).</div><p>%s</p>"
                % (t["titel"], li, boxes, bis, R["ka"], M(t["danach"])), str(R["termin"]))


# ---------------------------------------------------------------- Ablauf
def messen(pg, htmls: list) -> list:
    body = ("<div class='page'><div class='grow' id='g'></div><div class='foot'><span>x</span><b>Seite 99</b></div></div>"
            "<div style='width:180mm;font-size:15pt;line-height:1.35' id='m'>%s</div>" % "".join("<div style='display:flow-root'>%s</div>" % h for h in htmls))
    pg.set_content(doc(body, CSS, "m"), wait_until="load")
    pg.evaluate("document.fonts.ready")
    return pg.evaluate("[document.getElementById('g').clientHeight].concat([...document.getElementById('m').children].map(e=>e.getBoundingClientRect().height))")


def packen(pg, unit) -> list:
    """Verteilt die Elemente einer Fluss-Einheit auf Seiten; gibt Index-Gruppen zurück."""
    kopf, erst, items, tail = unit
    hs = messen(pg, [kopf(0, 2), erst, tail] + [x for x, _, _ in items])
    cap, hk, he, ht, hi = hs[0] - 1, hs[1], hs[2], hs[3], hs[4:]
    seiten, cur, frei = [], [], cap - hk - he
    for i, (_, _, fl) in enumerate(items):
        h = hi[i] if not fl.get("fill") else 75 * 96 / 25.4
        if cur and (fl.get("neu") or h > frei):
            # Zwischenüberschrift nicht allein am Seitenende lassen
            weg = []
            while cur and items[cur[-1]][2].get("klebt"):
                weg.insert(0, cur.pop())
            seiten.append(cur)
            cur, frei = weg, cap - hk - sum(hi[j] for j in weg)
        cur.append(i)
        frei -= h
    if frei < ht and cur:
        # Abschluss passt nicht mehr: letztes Element auf neue Seite
        letzte = [cur.pop()]
        seiten.append(cur)
        cur = letzte
    seiten.append(cur)
    return [s for s in seiten if s] or [[]]


def flussseite(unit, gruppe, k, n, nr) -> str:
    kopf, erst, items, tail = unit
    inner = kopf(k, n) + (erst if k == 0 else "") + "".join(items[i][0] for i in gruppe) + (tail if k == n - 1 else "")
    flex = any(items[i][2].get("fill") for i in gruppe)
    return page(inner, str(nr), grow_cls="flex" if flex else "")


def andika_fett() -> bytes | None:
    """Andika Bold als TTF (aus woff2), damit der Seitenstempel zur Heftschrift passt."""
    try:
        import io
        from fontTools.ttLib import TTFont
        f = TTFont(str(ROOT / "assets" / "fonts" / "andika-latin-700-normal.woff2"))
        f.flavor = None
        b = io.BytesIO()
        f.save(b)
        return b.getvalue()
    except Exception:
        return None


FONT = [None]


def stempel(p, nr: int):
    """Ersetzt in eingefügten Material-Seiten die rechte Fußzeile durch die Heftseite."""
    w, h = p.rect.width, p.rect.height
    rechts = []
    for b in p.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            for sp in l["spans"]:
                r = fitz.Rect(sp["bbox"])
                if r.y0 > h - 45 and r.x0 > w / 2 and sp["text"].strip():
                    rechts.append((r, sp))
    if rechts:
        base = max(sp["origin"][1] for _, sp in rechts)
        for r, _ in rechts:
            p.add_redact_annot(r + (-1, -1, 1, 1))
        p.apply_redactions(images=fitz.PDF_REDACT_IMAGE_NONE, graphics=fitz.PDF_REDACT_LINE_ART_NONE)
    else:
        base = h - 20
    text = "Seite %d" % nr
    if FONT[0] is None:
        FONT[0] = andika_fett() or b""
    if FONT[0]:
        p.insert_font(fontname="andb", fontbuffer=FONT[0])
        font, fn = fitz.Font(fontbuffer=FONT[0]), "andb"
    else:
        font, fn = fitz.Font("hebo"), "hebo"
    x = w - 15 * 72 / 25.4 - font.text_length(text, fontsize=14)
    p.insert_text((x, base), text, fontname=fn, fontsize=14)


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    bl = {b["nr"]: b for b in H["blaetter"]}
    plan = []  # (marke, art, daten)

    def add(marke, art, daten=None):
        plan.append((marke, art, daten))

    def pdf(marke, datei, seiten):
        for i, s in enumerate(seiten):
            add(marke if i == 0 else None, "pdf", (AUS / datei, s))

    add("cover", "fix", cover); add("legende", "fix", legende); add("weg", "fix", weg)
    add("e1", "fix", lambda: etappe_start(1)); add("mb1", "fluss", lambda: merk_unit(1))
    pdf("foto1", "etappe1/Material_Etappe1_A4.pdf", [0]); pdf("iv1", "etappe1/Material_Etappe1_A4.pdf", [1, 2])
    for nr in (1, 2, 3, 4):
        add("b%d" % nr, "fluss", (lambda b: lambda: blatt_unit(b))(bl[nr]))
    add("gn1", "fix", lambda: stopp("gn1"))
    add("e2", "fix", lambda: etappe_start(2)); add("mb2", "fluss", lambda: merk_unit(2))
    pdf("wh", "etappe2/Woerterhilfe_A4.pdf", [0]); pdf("iv2", "etappe2/Material_Etappe2_A4.pdf", [0, 1])
    for nr in (5, 6):
        add("b%d" % nr, "fluss", (lambda b: lambda: blatt_unit(b))(bl[nr]))
    add("gn2", "fix", lambda: stopp("gn2"))
    add("e3", "fix", lambda: etappe_start(3)); add("mb3", "fluss", lambda: merk_unit(3))
    pdf("iv3", "etappe3/Material_Etappe3_A4.pdf", [0, 1]); pdf("check", "etappe3/Uebungsblaetter_Etappe3_A4.pdf", [3, 4])
    for nr in (7, 8, 9):
        add("b%d" % nr, "fluss", (lambda b: lambda: blatt_unit(b))(bl[nr]))
    add("pa", "fix", lambda: stopp("pa")); add("auswertung", "fix", auswertung)
    for i, pu in enumerate(H["pflichtuebungen"]):
        add(pu["marke"], "fluss", (lambda i, pu: lambda: pu_unit(i, pu))(i, pu))
    add("pu", "fix", lambda: stopp("pu")); add("termin", "fix", termin)
    add("projekt", "fluss", projekt_unit); add("ka", "fix", lambda: stopp("ka"))
    add("zusatz", "fluss", zusatz_unit)

    with sync_playwright() as p:
        br = p.chromium.launch()
        pg = br.new_page()
        # 1. Messen und verteilen (Seitenzahlen als Platzhalter)
        MESS[0] = True
        gruppen = {}
        for j, (marke, art, d) in enumerate(plan):
            if art == "fluss":
                gruppen[j] = packen(pg, d())
        # 2. Seitenzahlen vergeben (noch im Messmodus, nur Marken werden gebraucht)
        seq, nr = [], 1
        for j, (marke, art, d) in enumerate(plan):
            if art == "fluss":
                u = d()
                for k, g in enumerate(gruppen[j]):
                    seq.append(("fluss", (j, k)))
                    if k == 0:
                        R[marke] = nr
                    for i in g:
                        if u[2][i][1]:
                            R[u[2][i][1]] = nr
                    nr += 1
            else:
                if marke:
                    R[marke] = nr
                seq.append((art, d))
                nr += 1
        MESS[0] = False
        # 3. Endgültige Seiten rendern
        html_pages, nummer = [], {}
        einheiten = {}
        for i, (art, d) in enumerate(seq):
            nr = i + 1
            if art == "pdf":
                continue
            if art == "fix":
                s = d()
            else:
                j, k = d
                if j not in einheiten:
                    einheiten[j] = plan[j][2]()
                s = flussseite(einheiten[j], gruppen[j][k], k, len(gruppen[j]), nr)
            nummer[nr] = len(html_pages)
            html_pages.append(s)

        tmp = OUT.parent / "_seiten.pdf"
        pg.set_content(doc("".join(html_pages), CSS, "Arbeitsheft"), wait_until="load")
        pg.evaluate("document.fonts.ready")
        over = pg.evaluate(
            "[...document.querySelectorAll('.page')].map((p,i)=>{const g=p.querySelector('.grow');"
            "const d=Math.max(g.scrollHeight-g.clientHeight,p.scrollHeight-p.clientHeight);"
            "return d>1?[i,Math.round(d*25.4/96)]:0}).filter(x=>x)")
        pg.pdf(path=str(tmp), prefer_css_page_size=True, print_background=True)
        br.close()

    rueck = {v: k for k, v in nummer.items()}
    probleme = ["Überlauf Heftseite %d (+%d mm)" % (rueck[i], mm) for i, mm in over]

    src = fitz.open(tmp)
    out = fitz.open()
    cache = {}
    for i, (art, d) in enumerate(seq):
        nr = i + 1
        if art == "pdf":
            f, s = d
            if f not in cache:
                cache[f] = fitz.open(f)
            out.insert_pdf(cache[f], from_page=s, to_page=s)
            stempel(out[-1], nr)
        else:
            out.insert_pdf(src, from_page=nummer[nr], to_page=nummer[nr])
    out.set_metadata({"title": H["titel"], "subject": "Deutsch · Jahrgang 5 · Zootiere · lineares Arbeitsheft"})
    out.save(OUT, garbage=3, deflate=True)
    tmp.unlink()

    d = fitz.open(OUT)
    kleinste, lk_seiten = {}, []
    for i, (art, _) in enumerate(seq):
        if art == "pdf":
            continue
        for b in d[i].get_text("dict")["blocks"]:
            for l in b.get("lines", []):
                for s in l["spans"]:
                    if s["text"].strip():
                        kleinste[i + 1] = min(kleinste.get(i + 1, 99), s["size"])
    zu_klein = {k: round(v, 1) for k, v in kleinste.items() if v < 12}
    if zu_klein:
        probleme.append("Schrift unter 12 pt: %s" % zu_klein)
    print("Seiten:", d.page_count)
    print("Seiten mit Schrift unter 14 pt:", sorted(k for k, v in kleinste.items() if v < 13.9))
    print("Marken:", R)
    if probleme:
        print("PROBLEME:\n  " + "\n  ".join(probleme))
        sys.exit(1)
    print("OK:", OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
