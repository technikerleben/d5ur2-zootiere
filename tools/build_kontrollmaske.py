#!/usr/bin/env python3
"""Kurzkontrollmaske für alle Gelingensnachweise (GN1 A/B, GN2 A/B, GN1F, GN2F).

Eine A4-Seite je Variante für die Lehrkraft: Zeilenschlüssel des Interviewauszugs,
Erwartungshorizont je Aufgabe (mit Zeilen), Indikator-Schnellcheck und Ergebnis.
Ziele/Indikatoren kommen aus inhalt/*.json; Zeilennummern entsprechen dem Satz der
gedruckten Nachweise (ausgabe/etappe*/GN*_A4.pdf, Stand 04.11.2026).

Aufruf: python tools/build_kontrollmaske.py  →  ausgabe/lehrkraft/Kurzkontrolle_Gelingensnachweise_A4.pdf
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from build_material import doc, md  # noqa: E402

INH = ROOT / "inhalt"
OUT = ROOT / "ausgabe" / "lehrkraft"


def ziele(datei):
    return json.loads((INH / datei).read_text(encoding="utf-8"))["nachweis"]["ziele"]


TAGS = {"L": "Lebensraum", "N": "Nahrung", "A": "Aussehen", "M": "Maß der Art",
        "X": "nur Otto", "W": "Meinung", "V": "Vergleich", "–": "Frage"}

BILD = ("<b>Bild</b> (Foto Fischotter): jedes sichtbare Merkmal mit genauer Angabe, z. B. "
        "<i>lange Tasthaare an der Schnauze · kleine Ohren · breiter, flacher Kopf · dunkles Fell</i>.")
BILD_NICHT = ("Schwimmhäute, Körperlänge, „weiches Fell“ (auf dem Foto nicht sicher erkennbar) · "
              "Wertungen wie „schönes Fell“ · zweimal dasselbe Merkmal")

VARIANTEN = [
    # ------------------------------------------------------------------ GN1 A
    dict(code="1A", gn=1, etappe=1, titel="Tierdetektiv", art="Erstversuch", datei="etappe1.json",
         zeilen=[("2–3", "Flüsse und Seen; Ufer mit vielen Verstecken", "L"),
                 ("3–4", "Höhle aus alten Wurzeln", "X"),
                 ("6", "jeden Morgen ein Eimer Fisch", "X"),
                 ("6–7", "vor allem Fische, auch Frösche und Krebse", "N"),
                 ("9", "Körper lang und schmal; Beine kurz", "A"),
                 ("9–10", "Fell oben dunkelbraun, sehr dicht", "A"),
                 ("10–11", "„das schönste Fell im ganzen Zoo“", "W"),
                 ("13", "Kopf breit und flach; Ohren ganz klein", "A"),
                 ("15–16", "Otto gemessen: 80 cm ohne Schwanz", "X"),
                 ("16–17", "meistens 60 bis 90 cm, ohne Schwanz", "M")],
         aufgaben=[
             dict(nr="1", titel="Merkmale und Quellen", ziel="E1.1 · E1.2",
                  ok=[BILD,
                      "<b>Interview</b>: langer, schmaler Körper (Z. 9) · kurze Beine (Z. 9) · "
                      "Fell oben dunkelbraun / dicht (Z. 9–10) · Kopf breit und flach (Z. 13) · "
                      "Ohren ganz klein (Z. 13)",
                      "Zwei <b>verschiedene</b> Merkmale (E1.1); je eins aus Bild und Interview, Zeile trifft (E1.2)."],
                  nicht=[BILD_NICHT]),
             dict(nr="2", titel="Das Maß", ziel="E1.3",
                  ok=["<b>60 bis 90 Zentimeter</b> (ohne Schwanz) – Einheit nötig (Z. 16–17)",
                      "80 cm gelten für ☒ <b>nur Otto</b> (Z. 15–16)"],
                  nicht=["„80 cm“ als Maß der Art · Zahl ohne Einheit · ☒ alle Fischotter"]),
             dict(nr="3", titel="Was gehört in die Beschreibung?", ziel="E1.5", tabelle="einordnen"),
             dict(nr="4", titel="Lebensraum und Nahrung", ziel="E1.4",
                  ok=["<b>Lebensraum</b>: Flüsse und Seen / Ufer mit Verstecken – Z. 2–3",
                      "<b>Nahrung</b>: vor allem Fische / Frösche, Krebse – Z. 6–7"],
                  nicht=["Höhle aus Wurzeln (Z. 3–4) · Eimer Fisch (Z. 6) – gilt nur für Otto"])]),
    # ------------------------------------------------------------------ GN1 B
    dict(code="1B", gn=1, etappe=1, titel="Tierdetektiv", art="Wiederholung", datei="etappe1.json",
         zeilen=[("2", "schwimmt jeden Mittag seine Runden", "X"),
                 ("2–3", "Schwimmhäute zwischen den Zehen", "A"),
                 ("3–4", "„der beste Schwimmer der Welt“", "W"),
                 ("6–7", "Flüsse und Seen; Ufer, Büsche und Wurzeln", "L"),
                 ("9", "hauptsächlich Fische; Frösche und Krebse", "N"),
                 ("9–10", "Otto mag am liebsten Forellen", "X"),
                 ("12", "lange Tasthaare an der Schnauze; Körper lang", "A"),
                 ("12–13", "Beine kurz", "A"),
                 ("15", "Otto: 80 cm ohne Schwanz", "X"),
                 ("15–17", "meistens 60 bis 90 cm, Schwanz kommt dazu", "M")],
         aufgaben=[
             dict(nr="1", titel="Merkmale und Quellen", ziel="E1.1 · E1.2",
                  ok=[BILD,
                      "<b>Interview</b>: Schwimmhäute zwischen den Zehen (Z. 2–3) · lange Tasthaare "
                      "(Z. 12) · Körper lang (Z. 12) · Beine kurz (Z. 12–13)",
                      "Zwei <b>verschiedene</b> Merkmale (E1.1); je eins aus Bild und Interview, Zeile trifft (E1.2)."],
                  nicht=[BILD_NICHT]),
             dict(nr="2", titel="Das Maß", ziel="E1.3",
                  ok=["<b>60 bis 90 Zentimeter</b> (ohne Schwanz) – Einheit nötig (Z. 15–17)",
                      "80 cm gelten für ☒ <b>nur Otto</b> (Z. 15)"],
                  nicht=["„80 cm“ als Maß der Art · Zahl ohne Einheit · ☒ alle Fischotter"]),
             dict(nr="3", titel="Was gehört in die Beschreibung?", ziel="E1.5", tabelle="einordnen"),
             dict(nr="4", titel="Lebensraum und Nahrung", ziel="E1.4",
                  ok=["<b>Lebensraum</b>: Flüsse und Seen / Ufer unter Büschen und Wurzeln – Z. 6–7",
                      "<b>Nahrung</b>: hauptsächlich Fische / Frösche, Krebse – Z. 9"],
                  nicht=["„Forellen“ (Z. 9–10) – gilt nur für Otto"])]),
    # ------------------------------------------------------------------ GN2 A
    dict(code="2A", gn=2, etappe=2, titel="Genaue Sätze", art="Erstversuch", datei="etappe2.json",
         zeilen=[("2", "gerade aus dem Wasser gekommen", "X"),
                 ("2–3", "Fell oben dunkelbraun, am Hals heller", "A"),
                 ("3–4", "Beine kurz", "A"),
                 ("4", "„die süßesten Beine der Welt“", "W"),
                 ("6", "gestern drei Fische und ein Krebs", "X"),
                 ("6–7", "in der Natur vor allem Fische", "N"),
                 ("9–10", "Flüsse und Seen; Ufer mit Verstecken", "L"),
                 ("12", "Kopf breit und flach", "A"),
                 ("12", "„fast wie ein Brett“", "V")],
         aufgaben=[
             dict(nr="1", titel="Aus dem Interview wird ein Sachsatz", ziel="E2.1 · E2.2 · E2.3 · E2.5",
                  ok=["<b>Lebensraum</b>: <i>Der Fischotter lebt an Flüssen und Seen. (Dort braucht er "
                      "Ufer mit Verstecken.)</i> – Z. 9–10",
                      "<b>Nahrung</b>: <i>Der Fischotter frisst vor allem Fische.</i> – Z. 6–7",
                      "<b>Kopf</b>: <i>Der Kopf des Fischotters ist breit und flach.</i> – Z. 12"],
                  nicht=["„drei Fische und einen Krebs“ (Ottos Mahlzeit, Z. 6) · „Otto …“ / „Er hat … "
                         "gefressen“ · Vergleich „wie ein Brett“ übernehmen (Hinweis geben)"]),
             dict(nr="2", titel="Aus einer Meinung wird ein Sachsatz", ziel="E2.4",
                  ok=["Meinung: „Ehrlich gesagt hat er die süßesten Beine der Welt!“",
                      "Genaue Angabe in <b>Zeile 3</b> (auch 3–4 gilt)",
                      "<i>Der Fischotter hat kurze Beine.</i>"],
                  nicht=["„süß“, „toll“, „schön“ bleiben im Satz · Angabe nicht aus dem Interview"])],
         nomen="Fischotter, Flüssen, Seen, Ufer, Verstecken, Fische, Kopf, Beine"),
    # ------------------------------------------------------------------ GN2 B
    dict(code="2B", gn=2, etappe=2, titel="Genaue Sätze", art="Wiederholung", datei="etappe2.json",
         zeilen=[("2", "Otto taucht nach Fischen", "X"),
                 ("2–3", "Schwimmhäute zwischen den Zehen", "A"),
                 ("3–4", "lange Tasthaare, spüren Fische im trüben Wasser", "A"),
                 ("6", "vor allem Fische, auch Frösche", "N"),
                 ("6–7", "Otto hat eine Ente erschreckt", "X"),
                 ("9", "Flüsse und Seen mit geschützten Ufern", "L"),
                 ("11", "Körper lang und schmal", "A"),
                 ("11", "„der Kopf ist total toll“", "W"),
                 ("12", "(Kopf) breit und flach", "A")],
         aufgaben=[
             dict(nr="1", titel="Aus dem Interview wird ein Sachsatz", ziel="E2.1 · E2.2 · E2.3 · E2.5",
                  ok=["<b>Nahrung</b>: <i>Der Fischotter frisst vor allem Fische, aber auch Frösche.</i> – Z. 6",
                      "<b>Lebensraum</b>: <i>Der Fischotter lebt an Flüssen und Seen mit geschützten "
                      "Ufern.</i> – Z. 9",
                      "<b>Zehen</b>: <i>Der Fischotter hat Schwimmhäute zwischen den Zehen.</i> – Z. 2–3"],
                  nicht=["„Ente erschreckt“ (Z. 6–7, nur Otto) · Vergangenheit („tauchte“, „hat … "
                         "erschreckt“) · Satz über Otto statt über die Art"]),
             dict(nr="2", titel="Aus einer Meinung wird ein Sachsatz", ziel="E2.4",
                  ok=["Meinung: „Ich finde, der Kopf ist total toll.“",
                      "Genaue Angabe in <b>Zeile 12</b> (Z. 11–12 gilt auch)",
                      "<i>Der Kopf des Fischotters ist breit und flach.</i> / <i>Der Fischotter hat "
                      "einen breiten, flachen Kopf.</i>"],
                  nicht=["„toll“ bleibt im Satz · „Er ist breit und flach.“ ohne klares Nomen "
                         "(Bezug unklar → Hinweis)"])],
         nomen="Fischotter, Fische, Frösche, Flüssen, Seen, Ufern, Schwimmhäute, Zehen, Kopf"),
    # ------------------------------------------------------------------ GN1 F
    dict(code="1F", gn=1, etappe=1, titel="Tierdetektiv", art="zieldifferent", datei="foerder_etappe1.json",
         foerder=True,
         zeilen=[("1", "Flüsse und Seen", "L"), ("1", "Otto wohnt im Zoo", "X"),
                 ("2", "Fische, Frösche und Krebse", "N"), ("2", "Otto: Forellen", "X"),
                 ("3", "Körper lang; Fell dunkelbraun", "A"), ("4", "Beine kurz; Kopf breit und flach", "A"),
                 ("5", "ohne Schwanz 60 bis 90 cm", "M"), ("5", "Otto: 80 cm", "X"),
                 ("6", "„der süßeste Otter der Welt“", "W")],
         zeilen_hinweis="Kurzinterview ohne Zeilennummern; Spalte = Frage 1–6. Fotoseite: 1 Nase · 2 Auge · 3 Ohr · 4 Tasthaare · 5 Fell.",
         aufgaben=[
             dict(nr="1", titel="Welche Sätze sind genau?", ziel="F1.1",
                  ok=["☒ <i>Der Kopf ist breit und flach.</i>", "☒ <i>Das Fell ist dunkelbraun.</i>"],
                  nicht=["„süß“, „schön“ angekreuzt"]),
             dict(nr="2", titel="Wer ist gemeint?", ziel="F1.1",
                  ok=["Otto frisst Forellen. → <b>2</b> (nur Otto)",
                      "Fischotter leben an Seen. → <b>1</b> (alle Fischotter)"]),
             dict(nr="3", titel="Zahl vom Foto", ziel="F1.2",
                  ok=["Nase <b>1</b> · Ohr <b>3</b> · Tasthaare <b>4</b> · Auge <b>2</b>",
                      "erreicht bei 3 von 4"]),
             dict(nr="4", titel="Lückentext", ziel="F1.3 · F1.4",
                  ok=["Sie leben an <b>Flüssen</b> und <b>Seen</b>. (Reihenfolge egal) → F1.3",
                      "Sie fressen <b>Fische</b>. → F1.4"],
                  nicht=["Ablenker „Bäumen“"]),
             dict(nr="5", titel="Wörter sortieren", ziel="F1.5",
                  ok=["<b>Aussehen</b>: kurze Beine, langer Körper",
                      "<b>Lebensraum</b>: Seen, Flüsse",
                      "<b>Nahrung</b>: Krebse, Frösche",
                      "erreicht bei 5 von 6"])]),
    # ------------------------------------------------------------------ GN2 F
    dict(code="2F", gn=2, etappe=2, titel="Genaue Sätze", art="zieldifferent", datei="foerder_etappe2.json",
         foerder=True,
         zeilen=[("1", "„Wie sind die Beine?“", "A"),
                 ("2", "„der süßeste Otter der Welt“", "W")],
         zeilen_hinweis="Aufgaben ohne Zeilenbezug; Material = Kurzinterview wie GN1F.",
         aufgaben=[
             dict(nr="1", titel="Genaues Wort", ziel="F2.1", ok=["☒ <b>kurz</b>"],
                  nicht=["„toll“, „schön“"]),
             dict(nr="2", titel="Info oder Meinung?", ziel="F2.1", ok=["☒ <b>Meinung</b>"]),
             dict(nr="3", titel="Satz aus Wortkarten", ziel="F2.2",
                  ok=["<i>Der Fischotter lebt an Flüssen.</i>",
                      "Andere sinnvolle Wortstellung zählt, wenn alle Karten genutzt sind."]),
             dict(nr="4", titel="Verb im Präsens", ziel="F2.3",
                  ok=["Der Fischotter <b>frisst</b> vor allem Fische."],
                  nicht=["Ablenker „fraß“"]),
             dict(nr="5", titel="Richtig geschrieben", ziel="F2.4",
                  ok=["☒ <i>Sein Kopf ist breit.</i>"]),
             dict(nr="6", titel="Fachwort", ziel="F2.5",
                  ok=["Schwimmhäute → <b>2</b> (Haut zwischen den Zehen)"])]),
]


def einordnen_tabelle(code):
    var = json.loads((INH / "etappe1.json").read_text(encoding="utf-8"))["nachweis"]["varianten"][code[1]]
    spalten = ["Sachangabe", "nur Otto", "Meinung"]
    kopf = "".join("<th>%s</th>" % s for s in spalten)
    rows = ""
    for satz, loes in var["einordnen"]:
        rows += "<tr><td>%s</td>%s</tr>" % (
            md(satz), "".join("<td class='c'>%s</td>" % ("☒" if s == loes else "") for s in spalten))
    return ("<table class='ein'><tr><th></th>%s</tr>%s</table>"
            "<p class='hint'>erreicht bei 4 von 5 richtig</p>" % (kopf, rows))


def aufgabe_html(a, code):
    body = ""
    if a.get("tabelle") == "einordnen":
        body = einordnen_tabelle(code)
    else:
        body = "<ul class='ok'>%s</ul>" % "".join("<li>%s</li>" % x for x in a["ok"])
        if a.get("nicht"):
            body += "<p class='nicht'><b>Zählt nicht:</b> %s</p>" % " · ".join(a["nicht"])
    return ("<div class='auf'><div class='ah'><span class='an'>%s</span><span class='at'>%s</span>"
            "<span class='az'>→ %s</span></div>%s</div>" % (a["nr"], a["titel"], a["ziel"], body))


def seite(v):
    zs = ziele(v["datei"])
    foerder = v.get("foerder", False)
    spalte = "Frage" if v["code"] == "1F" else ("Aufg." if v["code"] == "2F" else "Zeile")
    zrows = "".join(
        "<tr><td class='z'>%s</td><td>%s</td><td class='t'><span class='tag t%s'>%s</span></td></tr>"
        % (z, txt, t, TAGS.get(t, t)) for z, txt, t in v["zeilen"])
    zeilen_html = ("<div class='zs'><h3>Zeilenschlüssel</h3><table class='zt'><tr><th>%s</th><th>Inhalt</th>"
                   "<th>Art</th></tr>%s</table>%s"
                   "<p class='leg'><b>Nur Zeilen der Art (L, N, A, M) gelten als Beleg.</b> "
                   "X = nur das Zootier, W = Meinung, V = Vergleich.</p></div>"
                   % (spalte, zrows, "<p class='hint'>%s</p>" % v["zeilen_hinweis"] if v.get("zeilen_hinweis") else ""))
    if v["code"] == "2F":
        zeilen_html = ("<div class='zs'><h3>Hinweis</h3><p class='leg'>Alle Aufgaben sind geschlossen "
                       "(ankreuzen, einsetzen, zuordnen). Der Interviewauszug ist derselbe wie in GN1F; "
                       "für die Kontrolle wird er nicht gebraucht.</p>"
                       "<p class='leg' style='margin-top:3mm'><b>Zuordnung</b><br>F2.1 ← Aufg. 1 + 2<br>"
                       "F2.2 ← Aufg. 3<br>F2.3 ← Aufg. 4<br>F2.4 ← Aufg. 5<br>F2.5 ← Aufg. 6</p></div>")
    if v["code"] == "1F":
        zeilen_html += ("<div class='zs' style='margin-top:3mm'><p class='leg'><b>Zuordnung</b><br>"
                        "F1.1 ← Aufg. 1 + 2<br>F1.2 ← Aufg. 3<br>F1.3 ← Aufg. 4 (Flüssen, Seen)<br>"
                        "F1.4 ← Aufg. 4 (Fische)<br>F1.5 ← Aufg. 5</p></div>")
    zeilen_html = "<div class='left'>%s</div>" % zeilen_html
    auf = "".join(aufgabe_html(a, v["code"]) for a in v["aufgaben"])
    if v.get("nomen"):
        auf += ("<div class='auf'><div class='ah'><span class='an'>✓</span><span class='at'>Schreibung in allen "
                "vier Sätzen</span><span class='az'>→ E2.5</span></div><ul class='ok'><li>Satzanfang groß · "
                "Punkt am Satzende</li><li>Nomen groß, z. B. <i>%s</i></li></ul>"
                "<p class='nicht'><b>E2.3:</b> Präsens auch dort, wo das Interview Vergangenheit nutzt; "
                "Verb passt zum Subjekt (<i>der Fischotter frisst / Fischotter fressen</i>).</p></div>"
                % v["nomen"])
    zrow = ""
    for z in zs:
        zrow += ("<tr><td class='zid'>%s</td><td><b>%s</b> <span class='ew'>· %s</span></td>"
                 "<td class='c'><span class='cb'></span></td><td class='c'><span class='cb'></span></td>"
                 "<td class='ue'>%s</td></tr>"
                 % (z["id"], md(z.get("kurz") or z["kind"]), md(z["lehrkraft"]), z["ueben"]))
    if foerder:
        zrow += ("<tr><td class='zid'>eig.</td><td>Eigenes Förderziel: ____________________</td>"
                 "<td class='c'><span class='cb'></span></td><td class='c'><span class='cb'></span></td><td></td></tr>")
        ergeb = ("<div class='erg'><div class='en'>___ / ___</div><div>80 %% der <b>vereinbarten</b> Ziele "
                 "→ Etappe %d.<br>Förderziele, Antwortform und Hilfen vorab vereinbart.</div></div>"
                 % (v["etappe"] + 1))
    else:
        ergeb = ("<div class='erg'><div class='en'>___ / 5</div><div><b>4 oder 5</b> → Freigabe Etappe %d.<br>"
                 "<b>unter 4</b> → mit „Übe mit“ üben, dann Variante B oder Teilnachweis.</div></div>"
                 % (v["etappe"] + 1))
    return """
<section class='page'><div class='in'>
 <header class='kopf'><div><div class='kl'>Kurzkontrolle · nur für die Lehrkraft</div>
  <h1>Gelingensnachweis %d · %s</h1></div>
  <div class='var'><span>Nachweis</span><b>%s</b><em>%s</em></div></header>
 <div class='grid'>%s<div class='keys%s'>%s</div></div>
 <div class='spacer'></div>
 <div class='check'><h3>Schnellcheck · Indikatoren</h3>
  <table class='ct'><tr><th></th><th>Ziel · erreicht, wenn</th><th>gezeigt</th><th>offen</th><th>Übe mit</th></tr>%s</table>
  %s
  <p class='mini'>Nur die fachliche Leistung zählt – nicht Tempo, Ordnung oder Buddy-Felder. Ergebnis auf S. %d des Nachweises übertragen.</p>
 </div>
 <footer class='foot'><span>Deutsch · Jahrgang 5 · Zootiere · Etappe %d</span><span>Kurzkontrolle %s</span></footer>
</div></section>""" % (v["gn"], v["titel"], v["code"], v["art"], zeilen_html, " two" if foerder else "", auf, zrow, ergeb,
                       4 if foerder else 3, v["etappe"], v["code"])


CSS = """
.in{padding:8.5mm 12mm 7mm;display:flex;flex-direction:column;height:100%;font-size:10.5pt;line-height:1.3}
.kopf{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2.5pt solid var(--ink);padding-bottom:2.5mm}
.kl{font-size:9.5pt;letter-spacing:.08em;text-transform:uppercase;color:var(--mid);font-weight:700}
h1{font-size:16pt;line-height:1.15}
.var{display:flex;flex-direction:column;align-items:flex-end;line-height:1.05}
.var span{font-size:9pt;text-transform:uppercase;letter-spacing:.08em;color:var(--mid)}
.var b{font-size:21pt;border:2pt solid var(--ink);border-radius:2.5mm;padding:0 3mm;margin:1mm 0}
.var em{font-style:normal;font-size:9.5pt;color:var(--mid)}
.grid{display:flex;gap:4.5mm;margin-top:3.5mm;flex:0 0 auto}
.left{width:66mm;flex:0 0 66mm}
h3{font-size:9.5pt;text-transform:uppercase;letter-spacing:.07em;margin-bottom:1.2mm}
.zt{width:100%;border-collapse:collapse;font-size:9pt;line-height:1.2}
.zt th{font-size:8pt;text-align:left;color:var(--mid);border-bottom:1pt solid var(--ink);padding:.5mm .8mm}
.zt td{border-bottom:.5pt solid var(--line);padding:.7mm .8mm;vertical-align:top}
.zt td.z{white-space:nowrap;font-weight:700}
.zt td.t{text-align:right}
.tag{display:inline-block;font-size:7.5pt;padding:0 1.1mm;border-radius:1mm;border:1pt solid var(--ink);white-space:nowrap}
.tX,.tW,.tV{border-style:dashed;color:var(--mid)}
.tL,.tN,.tA,.tM{background:var(--fill)}
.leg{font-size:8.5pt;color:var(--mid);margin-top:1.5mm;line-height:1.25}
.hint{font-size:8.5pt;color:var(--mid);margin-top:1mm;line-height:1.25}
.keys{flex:1 1 auto;display:flex;flex-direction:column;gap:2mm;min-width:0;font-size:10pt;line-height:1.25}
.keys.two{display:grid;grid-template-columns:1fr 1fr;gap:2mm;align-content:start}
.auf{border:1.2pt solid var(--ink);border-radius:2.5mm;padding:1.5mm 2.3mm 1.7mm;break-inside:avoid}
.ah{display:flex;align-items:baseline;gap:1.8mm;margin-bottom:.8mm}
.an{display:inline-flex;align-items:center;justify-content:center;width:5.5mm;height:5.5mm;border-radius:50%;
  background:var(--ink);color:#fff;font-weight:700;font-size:9pt;flex:0 0 auto;align-self:center}
.at{font-weight:700;font-size:10.5pt;flex:1 1 auto;line-height:1.15}
.az{font-size:8.5pt;color:var(--mid);white-space:nowrap}
ul.ok{list-style:none}
ul.ok li{padding-left:4mm;position:relative;margin:.3mm 0}
ul.ok li:before{content:'✓';position:absolute;left:0;font-weight:700}
.nicht{font-size:9pt;color:var(--mid);border-top:.5pt dashed var(--line);margin-top:1mm;padding-top:.8mm;line-height:1.2}
.ein{width:100%;border-collapse:collapse;font-size:9.3pt;line-height:1.15}
.ein th{font-size:8pt;color:var(--mid);font-weight:700;padding:.3mm 1mm;border-bottom:1pt solid var(--ink);width:15mm}
.ein th:first-child{width:auto}
.ein td{border-bottom:.5pt solid var(--line);padding:.35mm 1mm}
.ein td.c,.ct td.c{text-align:center;font-size:11pt}
.spacer{flex:1 1 auto;min-height:2mm}
.check{border-top:1.5pt solid var(--ink);padding-top:2mm;flex:0 0 auto}
.ct{width:100%;border-collapse:collapse;font-size:9.5pt;line-height:1.2}
.ct th{font-size:8pt;color:var(--mid);text-align:left;padding:.4mm 1.5mm;border-bottom:1pt solid var(--ink)}
.ct th:nth-child(3),.ct th:nth-child(4){text-align:center;width:14mm}
.ct td{border-bottom:.5pt solid var(--line);padding:.8mm 1.5mm;vertical-align:middle}
.ct td.zid{font-weight:700;white-space:nowrap;width:11mm}
.ct .ew{color:var(--mid);font-size:8.8pt}
.ct td.ue{font-size:8.8pt;white-space:nowrap;width:19mm}
.cb{margin:0;width:5mm;height:5mm}
.erg{display:flex;gap:4mm;align-items:center;margin-top:2mm;border:1.5pt solid var(--ink);border-radius:2.5mm;padding:1.5mm 3mm;font-size:10pt}
.en{font-size:17pt;font-weight:700;white-space:nowrap}
.mini{font-size:8.5pt;color:var(--mid);margin-top:1.2mm}
.ov th,.ov td{width:auto!important;text-align:left!important;white-space:nowrap}
.foot{font-size:9pt;color:var(--mid);border-top-width:1pt;margin-top:3mm}
"""

DECK = """
<section class='page'><div class='in'>
 <header class='kopf'><div><div class='kl'>Kurzkontrolle · nur für die Lehrkraft</div>
  <h1>Gelingensnachweise · Kontrollmasken</h1></div><div class='var'><span>Etappe</span><b>1 · 2</b></div></header>
 <div style='margin-top:5mm;display:flex;flex-direction:column;gap:3.5mm;font-size:11pt'>
  <p>Eine Seite je Variante. Neben den Nachweis legen, Aufgabe für Aufgabe abgleichen, im Schnellcheck
   ankreuzen und das Ergebnis auf die Rückmeldeseite des Nachweises übertragen.</p>
  <table class='ct ov'><tr><th>Seite</th><th>Nachweis</th><th>Variante</th><th>Material</th></tr>
   <tr><td class='zid'>2</td><td>GN1 Tierdetektiv</td><td>A · Erstversuch</td><td>Interviewauszug, 17 Zeilen, Foto</td></tr>
   <tr><td class='zid'>3</td><td>GN1 Tierdetektiv</td><td>B · Wiederholung</td><td>Interviewauszug, 17 Zeilen, Foto</td></tr>
   <tr><td class='zid'>4</td><td>GN2 Genaue Sätze</td><td>A · Erstversuch</td><td>Interviewauszug, 12 Zeilen</td></tr>
   <tr><td class='zid'>5</td><td>GN2 Genaue Sätze</td><td>B · Wiederholung</td><td>Interviewauszug, 12 Zeilen</td></tr>
   <tr><td class='zid'>6</td><td>GN1F Tierdetektiv</td><td>zieldifferent</td><td>Kurzinterview, Fotoseite 1–5</td></tr>
   <tr><td class='zid'>7</td><td>GN2F Genaue Sätze</td><td>zieldifferent</td><td>Kurzinterview</td></tr></table>
  <div class='auf'><div class='ah'><span class='an'>!</span><span class='at'>Regeln für alle Varianten</span></div>
   <ul class='ok'>
    <li><b>4 von 5 Indikatoren = 80 %</b> → Freigabe für die nächste Etappe. Unter 80 %: gezielt mit dem Blatt aus „Übe mit“ üben, dann Variante B oder Teilnachweis nur der offenen Ziele.</li>
    <li>F-Fassungen: 80 % beziehen sich auf die <b>vorab vereinbarte</b> Zielliste (ggf. eigenes Förderziel).</li>
    <li>Eigene richtige Lösungen zählen, wenn sie zum Material passen. Die Musterlösungen sind Beispiele.</li>
    <li>Eine Zeilenangabe zählt, wenn sie die Stelle trifft; bei mehrzeiligen Stellen genügt eine der Zeilen.</li>
    <li>Gilt nur für Otto (X) oder ist Meinung/Vergleich (W, V) → kein Beleg für eine Sachangabe.</li>
    <li>Keine Note, keine Punkte für Tempo, Ordnung oder ausgefüllte Buddy-Felder. Rechtschreibung zählt nur dort, wo ein Indikator sie nennt (E2.5, F2.4).</li>
    <li>Keine Partnerhilfe und kein Kiosk im Nachweis. Vereinbarte Hilfen (z. B. Vorlesen) auf der Rückmeldeseite notieren.</li>
   </ul></div>
  <div class='auf'><div class='ah'><span class='an'>?</span><span class='at'>Kürzel im Zeilenschlüssel</span></div>
   <p><span class='tag tL'>Lebensraum</span> <span class='tag tN'>Nahrung</span> <span class='tag tA'>Aussehen</span>
   <span class='tag tM'>Maß der Art</span> = Sachangabe über die Art (grau hinterlegt) ·
   <span class='tag tX'>nur Otto</span> <span class='tag tW'>Meinung</span> <span class='tag tV'>Vergleich</span> = gehört nicht in die Beschreibung (gestrichelt)</p></div>
  <p class='mini'>Zeilennummern wie in den gedruckten Nachweisen (ausgabe/etappe1–2/GN*_A4.pdf). Nach Textänderungen
   im Interviewauszug die Zeilen mit tools/build_kontrollmaske.py prüfen und anpassen.</p>
 </div>
 <div class='grow'></div>
 <footer class='foot'><span>Deutsch · Jahrgang 5 · Zootiere · Etappe 1–2</span><span>Kurzkontrolle · Übersicht</span></footer>
</div></section>"""


def main():
    from playwright.sync_api import sync_playwright
    OUT.mkdir(parents=True, exist_ok=True)
    body = DECK + "".join(seite(v) for v in VARIANTEN)
    html_doc = doc(body, CSS, "Kurzkontrolle Gelingensnachweise")
    hp = OUT / "Kurzkontrolle_Gelingensnachweise_A4.html"
    hp.write_text(html_doc, encoding="utf-8")
    pdf = OUT / "Kurzkontrolle_Gelingensnachweise_A4.pdf"
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page()
        pg.goto(hp.as_uri())
        pg.wait_for_timeout(300)
        over = pg.evaluate("""[...document.querySelectorAll('.page .in')].map((e,i)=>
            (e.scrollHeight>e.clientHeight+1||[...e.querySelectorAll('.spacer')].some(x=>x.getBoundingClientRect().height<1.5))?i+1:0).filter(Boolean)""")
        pg.pdf(path=str(pdf), format="A4", print_background=True)
        b.close()
    hp.unlink()
    print("PDF:", pdf.relative_to(ROOT), "· Seitenüberlauf:", over or "keiner")


if __name__ == "__main__":
    main()
