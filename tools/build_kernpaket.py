#!/usr/bin/env python3
"""Kernpaket für Lehrkräfte: alle Druckvorlagen der Reihe in einer PDF, mit Deckblatt je Abschnitt.

Jedes Deckblatt zeigt, was als Nächstes kommt: Materialien, Seiten im Paket, Druckformat,
Menge und Zeitpunkt. Vorher alle Einzel-PDFs erzeugen (siehe tools/build_pakete.py).

    python3 tools/build_kernpaket.py   -> ausgabe/pakete/lehrkraft/Kernpaket_Lehrkraft_A4.pdf (läuft auch in build_pakete.py)
"""
from __future__ import annotations

import html
import sys
from datetime import date
from pathlib import Path

import pymupdf as fitz
from playwright.sync_api import sync_playwright

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_material import FUSS, ROOT, doc, font_sizes, render  # noqa: E402

A = ROOT / "ausgabe"
OUT = A / "pakete" / "lehrkraft" / "Kernpaket_Lehrkraft_A4.pdf"

A5 = "A4 → A5 verkleinert"
A4 = "A4, 100 %"
LAM = "A4 → A5, laminieren"

# (Titel, wann, Zweck, [(Material, Datei(en), Druck, Menge, Hinweis)])
ABSCHNITTE = [
    ("Lernweg", "vor Doppelstunde 1",
     "Orientierung über die ganze Reihe. Die Kinder haken ihre Etappen ab. Die F-Fassung ist für die zieldifferent lernenden Kinder.",
     [("Lernweg", ["lernweg/Lernweg_Zootiere_A4.pdf"], A4, "je Kind", ""),
      ("Lernweg F (zieldifferent)", ["lernweg/Lernweg_Zootiere_F_A4.pdf"], A4, "je F-Kind", "")]),
    ("Etappe 1 · Informationen finden und ordnen", "ab Doppelstunde 1",
     "Beispieltier Fischotter. Erst Input, dann Merkblatt, dann Material und Blatt 1–4, danach Gelingensnachweis 1.",
     [("Merkblatt 1", ["etappe1/Merkblatt_1_A4.pdf"], A4 + ", doppelseitig", "je Kind", "gleich wie Input 1"),
      ("Material: Foto + Interview Fischotter", ["etappe1/Material_Etappe1_A4.pdf"], A5, "je Kind", "auch für Etappe 2 nutzbar"),
      ("Übungsblätter Blatt 1–4", ["etappe1/Uebungsblaetter_Etappe1_A4.pdf"], A5, "je Kind", "Kiosk 1–4"),
      ("Gelingensnachweis 1 A", ["etappe1/GN1_A_A4.pdf"], A4, "je Kind", "S. 3 = Rückmeldung der Lehrkraft"),
      ("Gelingensnachweis 1 B", ["etappe1/GN1_B_A4.pdf"], A4, "ca. ⅓ Klasse", "für die Wiederholung")]),
    ("Etappe 2 · Sachlich und genau formulieren", "ab Doppelstunde 2",
     "Aus Interview-Sprache wird Sachsprache. Merkblatt, Interview, Blatt 5–6 und Wörterhilfe, danach Gelingensnachweis 2.",
     [("Merkblatt 2", ["etappe2/Merkblatt_2_A4.pdf"], A4 + ", doppelseitig", "je Kind", "gleich wie Input 2"),
      ("Material: Interview Fischotter", ["etappe2/Material_Etappe2_A4.pdf"], A5, "je Kind", "entfällt, wenn aus Etappe 1 vorhanden"),
      ("Übungsblätter Blatt 5–6", ["etappe2/Uebungsblaetter_Etappe2_A4.pdf"], A5, "je Kind", "Kiosk 5–6"),
      ("Wörterhilfe", ["etappe2/Woerterhilfe_A4.pdf"], LAM, "je Tisch", "gilt auch für Etappe 3"),
      ("Gelingensnachweis 2 A", ["etappe2/GN2_A_A4.pdf"], A4, "je Kind", "S. 3 = Rückmeldung der Lehrkraft"),
      ("Gelingensnachweis 2 B", ["etappe2/GN2_B_A4.pdf"], A4, "ca. ⅓ Klasse", "für die Wiederholung")]),
    ("Etappe 3 · Eine Tierbeschreibung schreiben und prüfen", "ab Doppelstunde 3",
     "Übungstiere Erdmännchen oder Roter Panda (Wahl). Plan, Text, Prüfen mit Checkliste und Haltestelle. Abschluss: Probearbeit Waschbär.",
     [("Merkblatt 3", ["etappe3/Merkblatt_3_A4.pdf"], A4 + ", doppelseitig", "je Kind", "gleich wie Input 3"),
      ("Material: Interviews Erdmännchen und Roter Panda", ["etappe3/Material_Etappe3_A4.pdf"], A5, "je Kind", "je 2 Seiten; ggf. nur das gewählte Tier"),
      ("Übungsblätter Blatt 7–9 + Checkliste K1–K6", ["etappe3/Uebungsblaetter_Etappe3_A4.pdf"], A5, "je Kind", "Kiosk 7–9"),
      ("Rückmeldekarte", ["etappe3/Rueckmeldekarte_A4.pdf"], LAM, "3 Stück", "an der Haltestelle"),
      ("Haltestellen-Schild", ["etappe3/Haltestelle_Schild_A4.pdf"], A4 + ", laminieren", "1 Stück", ""),
      ("Probearbeit Waschbär", ["etappe3/Probearbeit_Waschbaer_A4.pdf"], A4, "je Kind", "S. 1–2 Interview, S. 8 Rückmeldung; keine Note")]),
    ("Zieldifferente Materialien (Förderschwerpunkt Lernen)", "parallel zu Etappe 1–3",
     "Gleiche Etappen mit „F“. Je Etappe: Foto mit Zahlen und Kurzinterview, dann die Förderblätter mit Lösungsstreifen und Merkkarte. Förderziele vorher individuell vereinbaren.",
     [("Etappe 1F: Material", ["foerder/etappe1/Material_Foerder_Etappe1_A4.pdf"], A5, "je F-Kind", "Foto mit Zahlen + Kurzinterview"),
      ("Etappe 1F: Blatt 1F–4F + Merkkarte", ["foerder/etappe1/Foerder_Etappe1_A4.pdf"], A5, "je F-Kind", "Lösungsstreifen zum Umknicken"),
      ("Gelingensnachweis 1F", ["foerder/etappe1/GN1F_A4.pdf"], A4, "je F-Kind", "letzte Seite = Rückmeldung"),
      ("Etappe 2F: Material", ["foerder/etappe2/Material_Foerder_Etappe2_A4.pdf"], A5, "je F-Kind", ""),
      ("Etappe 2F: Blatt 5F–6F + Merkkarte", ["foerder/etappe2/Foerder_Etappe2_A4.pdf"], A5, "je F-Kind", ""),
      ("Gelingensnachweis 2F", ["foerder/etappe2/GN2F_A4.pdf"], A4, "je F-Kind", "letzte Seite = Rückmeldung"),
      ("Etappe 3F: Material", ["foerder/etappe3/Material_Foerder_Etappe3_A4.pdf"], A5, "je F-Kind", "Erdmännchen"),
      ("Etappe 3F: Blatt 7F–9F + Merkkarte", ["foerder/etappe3/Foerder_Etappe3_A4.pdf"], A5, "je F-Kind", ""),
      ("Probearbeit F Waschbär", ["pruefungen/Probearbeit_F_Waschbaer_A4.pdf"], A4, "je F-Kind", "letzte Seite = Rückmeldung; keine Note")]),
    ("Training vor der Klassenarbeit", "nach der Probearbeit, Doppelstunde 6",
     "Zwei neue Tiere aus dem Zoo Dortmund. Je Tier ein Blatt: vorn Interview, hinten Aufgaben. Musterlösungen Mindest- und Regelstandard am Kontroll-Kiosk (Nummer 10 und 11).",
     [("Ü1 Elenantilope", [("training/Training_Antilopen_A4.pdf", 0, 2)], A4 + ", doppelseitig", "nach Bedarf", "Kiosk 10"),
      ("Ü2 Hirschziegenantilope", [("training/Training_Antilopen_A4.pdf", 2, 4)], A4 + ", doppelseitig", "nach Bedarf", "Kiosk 11")]),
    ("Klassenarbeit", "Doppelstunde 7 (früh) oder 8 (spät)",
     "Zwei Varianten im gleichen Aufbau, dazu die zieldifferente Fassung. Vorschlag: Biber am frühen, Breitmaulnashorn am späten Termin.",
     [("Variante 1: Biber", ["pruefungen/Klassenarbeit_Biber_A4.pdf"], A4, "Kinder am frühen Termin", "S. 1–2 Interview, S. 8 Bewertung"),
      ("Variante 2: Breitmaulnashorn", ["pruefungen/Klassenarbeit_Breitmaulnashorn_A4.pdf"], A4, "Kinder am späten Termin", "S. 1–2 Interview, S. 8 Bewertung"),
      ("Klassenarbeit F: Biber", ["pruefungen/Klassenarbeit_F_Biber_A4.pdf"], A4, "je F-Kind", "Punkte als Vorschlag; Bewertung nach Schulvorgabe")]),
    ("Projekte in der Wahlzeit", "ab Doppelstunde 6",
     "Übersicht und drei Projekte: P1 Tiermagazin, P2 Tierrätsel, P3 Tiervergleich. Zum Auslegen.",
     [("Wahlphase und Projekte P1–P3", ["wahlphase/Wahlphase_Projekte_A4.pdf"], A4, "halber Klassensatz", "4 Seiten")]),
]

CSS = """
.page{padding:16mm 18mm 12mm 18mm;font-size:12.5pt;line-height:1.38}
.meta{font-size:12pt;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--mid)}
.nrbig{font-size:52pt;font-weight:700;line-height:1;margin:5mm 0 2mm}
h1{font-size:28pt;line-height:1.12;margin-bottom:4mm}
.wann{display:inline-block;border:1.8pt solid var(--ink);border-radius:2mm;padding:1mm 3mm;font-weight:700;margin-bottom:5mm}
.zweck{font-size:13pt;margin-bottom:5mm;max-width:165mm}
.next{font-size:12pt;font-weight:700;letter-spacing:.06em;text-transform:uppercase;border-bottom:2pt solid var(--ink);padding-bottom:1mm;margin-bottom:1mm}
table{width:100%;border-collapse:collapse;font-size:12pt}
th{font-size:10.5pt;text-transform:uppercase;letter-spacing:.04em;text-align:left;border-bottom:1.5pt solid var(--ink);padding:1.5mm 1.5mm}
td{border-bottom:1pt solid var(--line);padding:2mm 1.5mm;vertical-align:top}
td.n{width:9mm;font-weight:700}
td.s{width:22mm;white-space:nowrap}
td.d{width:38mm}
td .h{display:block;color:var(--mid);font-size:11pt}
.foot{font-size:11pt;color:var(--mid);border-top-width:1pt}
.inh td{padding:1.4mm 1.5mm}
.inh td.s{text-align:right}
.box{padding:2.5mm 4mm;margin-top:4mm;font-size:12pt}
.box b{display:block;margin-bottom:1mm}
"""


def seitenzahl(teil) -> int:
    if isinstance(teil, tuple):
        return teil[2] - teil[1]
    return len(fitz.open(A / teil))


def plan():
    """Seitenpositionen: Titelseite (Inhalt), dann je Abschnitt Deckblatt + Materialien."""
    pos = 2  # Seite 1 = Titel/Inhalt
    out = []
    for k, (titel, wann, zweck, mats) in enumerate(ABSCHNITTE, 1):
        deck = pos
        pos += 1
        rows = []
        for name, teile, druck, menge, hinweis in mats:
            n = sum(seitenzahl(t) for t in teile)
            rows.append((name, teile, druck, menge, hinweis, pos, pos + n - 1))
            pos += n
        out.append((k, titel, wann, zweck, deck, rows, pos - 1))
    return out, pos - 1


def deckblatt(k, titel, wann, zweck, rows, gesamt) -> str:
    tr = "".join(
        "<tr><td class='n'>%d.%d</td><td><b>%s</b>%s</td><td class='s'>S. %s</td><td class='d'>%s</td><td>%s</td></tr>"
        % (k, i, html.escape(name), ("<span class='h'>%s</span>" % html.escape(h)) if h else "",
           "%d–%d" % (a, b) if b > a else str(a), html.escape(druck), html.escape(menge))
        for i, (name, _, druck, menge, h, a, b) in enumerate(rows, 1))
    return ("<div class='page'><div class='grow'><div class='meta'>Kernpaket für Lehrkräfte · Abschnitt %d von %d</div>"
            "<div class='nrbig'>%d</div><h1>%s</h1><div class='wann'>%s</div><div class='zweck'>%s</div>"
            "<div class='next'>Als Nächstes in diesem Abschnitt</div>"
            "<table><tr><th></th><th>Material</th><th>Seiten</th><th>Druck</th><th>Menge</th></tr>%s</table></div>"
            "<div class='foot'><span>%s · Kernpaket Lehrkraft</span><b>Deckblatt %d</b></div></div>"
            % (k, len(ABSCHNITTE), k, html.escape(titel), html.escape(wann), html.escape(zweck), tr, FUSS, k))


def titelseite(abschn, gesamt) -> str:
    tr = "".join("<tr><td class='n'>%d</td><td><b>%s</b><span class='h'>%s</span></td><td class='s'>S. %d–%d</td></tr>"
                 % (k, html.escape(t), html.escape(w), d, e) for k, t, w, _, d, _, e in abschn)
    return ("<div class='page inh'><div class='grow'><div class='meta'>Deutsch · Jahrgang 5 · Zootiere</div>"
            "<h1 style='font-size:32pt;margin-top:4mm'>Kernpaket für Lehrkräfte</h1>"
            "<div class='zweck'>Alle Druckvorlagen der Reihe in der Reihenfolge des Unterrichts. Vor jedem Abschnitt steht ein Deckblatt: "
            "Es zeigt, welche Materialien folgen, auf welchen Seiten sie stehen, wie sie gedruckt werden und wie viele du brauchst.</div>"
            "<div class='next'>Inhalt</div><table>%s</table>"
            "<div class='box dashed'><b>So druckst du</b>Dieses Paket ist eine Kopiervorlage: einseitig ausdrucken und dann je Material "
            "nach der Angabe auf dem Deckblatt kopieren. „A4 → A5 verkleinert“ heißt: auf A5 verkleinert kopieren (71 %%). Das Blatt passt dann "
            "in die Mitte des Lernbuddys. Alles für Kinder ist in Graustufen gesetzt.</div>"
            "<div class='box dashed'><b>Nicht im Paket</b>Input-Präsentationen und Kontroll-Kiosk (digital), Strategiekarten (eigene Datei, 210 × 99 mm), "
            "Tierpakete für die Projekte (A5-Vorfassungen), Zeilenbelege der Interviews (Lehrkräfte-Material).</div></div>"
            "<div class='foot'><span>%s · Kernpaket Lehrkraft · Stand %s</span><b>%d Seiten</b></div></div>"
            % (tr, FUSS, date.today().strftime("%d.%m.%Y"), gesamt))


def main():
    abschn, gesamt = plan()
    fehlt = [t for *_, rows, _ in abschn for r in rows for t in r[1] if not (A / (t[0] if isinstance(t, tuple) else t)).exists()]
    if fehlt:
        sys.exit("Fehlende Dateien: %s" % fehlt)
    tmp = OUT.with_suffix(".deck.pdf")
    body = titelseite(abschn, gesamt) + "".join(deckblatt(k, t, w, z, rows, gesamt) for k, t, w, z, _, rows, _ in abschn)
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        o = render(br.new_page(), doc(body, CSS, "Kernpaket"), tmp)
        br.close()
    if o:
        sys.exit("Deckblatt läuft über: %s" % o)
    deck = fitz.open(tmp)
    out = fitz.open()
    out.insert_pdf(deck, from_page=0, to_page=0)
    toc = [[1, "Kernpaket – Inhalt", 1]]
    for i, (k, titel, *_r, rows, _) in enumerate(abschn, 1):
        toc.append([1, "%d · %s" % (k, titel), len(out) + 1])
        out.insert_pdf(deck, from_page=i, to_page=i)
        for name, teile, *_x, a, b in rows:
            toc.append([2, name, len(out) + 1])
            for t in teile:
                if isinstance(t, tuple):
                    out.insert_pdf(fitz.open(A / t[0]), from_page=t[1], to_page=t[2] - 1)
                else:
                    out.insert_pdf(fitz.open(A / t))
            assert len(out) == b, (name, len(out), b)
    out.set_toc(toc)
    out.set_metadata({"title": "Zootiere · Kernpaket für Lehrkräfte", "author": "Deutsch · Jahrgang 5"})
    out.save(OUT, garbage=3, deflate=True)
    mn, n = font_sizes(tmp)
    tmp.unlink()
    print("%s  %d Seiten (geplant %d), Deckblätter kleinste Schrift %.1f pt" % (OUT.relative_to(ROOT), len(out), gesamt, mn))


if __name__ == "__main__":
    main()
