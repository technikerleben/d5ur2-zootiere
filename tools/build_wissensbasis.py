#!/usr/bin/env python3
"""Erzeugt WISSENSBASIS.md: Gesamtübersicht der Reihe als Wissensgrundlage für LLMs.

Feste Abschnitte (Prinzipien, Entscheidungen, Regeln) stehen unten im Skript.
Inhaltliche Abschnitte (Etappen, Blätter, Nachweise, Material, Prüfungen, Projekte,
Strategiekarten, Förder-Material) werden aus inhalt/*.json erzeugt und sind damit
immer auf dem Stand der Materialien.

Aufruf: python tools/build_wissensbasis.py
"""
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def j(name):
    return json.loads((ROOT / "inhalt" / name).read_text(encoding="utf-8"))


def clean(t: str) -> str:
    """Markup der Inhaltsdateien in Markdown übersetzen (Zeilenumbrüche, *kursiv*, **fett** bleiben)."""
    return t.replace("\n", " / ")


def gaps(t):
    return re.findall(r"\{([^}]+)\}", t)


KOPF = """# Wissensbasis · Deutsch 5 · Unterrichtsreihe „Zootiere“

> **Zweck:** Vollständige, verbindliche Wissensgrundlage für ein LLM, das an dieser Reihe weiterarbeitet (Material ergänzen, ändern, prüfen, Fragen beantworten).
> **Stand:** {stand}. Abschnitte mit ⚙ werden aus den Inhaltsdateien `inhalt/*.json` erzeugt (`python tools/build_wissensbasis.py`) und spiegeln den aktuellen Materialstand.
> **Repo:** `technikerleben/d5ur2-zootiere`, Stand in `main` (am 10.10.2026 aus `claude/etappe1-muster` zusammengeführt; Deployment über Vercel). Lehrkraft-Leitfaden: `anleitung.html`.

## 0 · Kurzfassung in zehn Sätzen

1. Deutsch, Jahrgang 5, Heinrich-Böll-Gesamtschule Dortmund; vier Wochen, acht Doppelstunden à 90 Minuten.
2. Zielkompetenz: **ein Zootier mithilfe von Bild und Interview sachlich und geordnet beschreiben** (Aufgabentyp 2, informierendes Schreiben, materialgestützt). Textbasis ist immer ein **ausgedachtes Interview** mit einer Tierpflegerin/einem Tierpfleger (Schülerzeitung „Zoo-Reporter“), das die Kinder erst auswerten (Sachangaben über die Art vs. Meinung/Einzeltier/Vergleich) und dann zum Sachtext formen.
3. Die Reihe ist in **drei Etappen** gegliedert, die jedes Kind **im eigenen Tempo** durchläuft.
4. Jede Etappe: **Input (HTML-Präsentation) + inhaltsgleiches Merkblatt → Pflichtblätter mit freiwilliger Vertiefung → Abschlussnachweis**.
5. Nachweise prüfen **fünf Indikatoren**; **4 von 5 (80 %)** = Freigabe für die nächste Etappe; sonst gezielt üben und erneut nachweisen (Variante B).
6. Etappe 3 endet mit der **Probearbeit** (unbenotet, mit Feedback). Danach **Wahlzeit** (Projekte P1–P3, Wiederholung, Vertiefungen).
7. Die **Klassenarbeit** wird an **einem von zwei Wahlterminen** geschrieben (Doppelstunde 7 oder 8), zwei Varianten (Biber, Breitmaulnashorn).
8. **Fischotter** ist das durchgehende Beispieltier; Übungstiere Erdmännchen/Roter Panda; Waschbär für die Probearbeit; Biber und Breitmaulnashorn für die Klassenarbeit.
9. Der **Lernbuddy** (laminierter A4-Tischrahmen, SRL) wird genutzt, aber **nie auf Fachblättern nachgebaut**; Strategiekarten werden an ihm angelegt.
10. Gedrucktes für Kinder ist **graustufig, neutral (ohne Maskottchen), mindestens 14 pt**; HTML-Seiten dürfen **farbig** sein (HBG-SRL-Farbschema).
"""

PRINZIPIEN = """
## 1 · Rahmen und Lehrplanbezug

- **Klasse:** Jahrgang 5 (in Materialien neutral „Deutsch · Jahrgang 5“, keine Klassenbezeichnung). Zwei Kinder lernen **zieldifferent (Förderschwerpunkt Lernen)**.
- **Zeit:** 720 Minuten. Schulinterner Lehrplan sieht 20 Stunden vor; gekürzt wurden zusätzliche Recherche, mehrfache Schreibdurchgänge, längere Präsentationen.
- **Lehrplan:** Unterrichtsvorhaben „Ein Besuch im Zoo – Auf Basis von Material berichten“; Abschlussziel „Tiere sachlich beschreiben (Aufgabentyp 2)“. Digitale Recherche/Präsentation sind **nicht** Teil dieser Reihe (an anderer Stelle der Jahresplanung).
- **Sprachspur (integriert, keine eigene Grammatik-Etappe):** Wortarten Nomen/Artikel/Verb/Adjektiv, Großschreibung von Nomen, zusammengesetzte Nomen („Wörter zerlegen“, letztes Wort bestimmt den Artikel), Präsens und Subjekt-Verb-Kongruenz, Grundform vs. gebeugte Form, vollständige Sätze, genaue Verben/Adjektive. Quelle: `planung/Sprachspur_Zootiere_Feinplanung.md`.
- **Anforderungen an den Zieltext:** Tiername und Überblick mit **richtiger Maßangabe mit Einheit und Bezug** (z. B. „Kopf und Rumpf … cm, Schwanz zusätzlich“ oder Gewicht), **mindestens vier verschiedene äußere Merkmale**, **Lebensraum**, **Nahrung**; sachlich, Präsens, vollständige Sätze, geordnet (Überblick → Aussehen → Lebensraum → Nahrung). **Keine Mindestwortzahl**; Länge ist kein Qualitätsmerkmal. Steckbrief/Stichwortliste ist Planungshilfe, nicht Zielprodukt.
- **Materialtreue:** Nur Angaben, die Bild oder Text belegen. Fotos zeigen nicht alles (z. B. Schwimmhäute, Körperlänge, „weiches Fell“). Nichts erfinden, nichts aus Fotos schätzen.

## 2 · Verbindlicher SRL-Standard (Ablauf)

```
Etappe 1 ─ Input + Merkblatt 1 → Blatt 1–4 (+ Vertiefungen) → GN1 (4/5)
Etappe 2 ─ Input + Merkblatt 2 → Blatt 5–6 (+ Vertiefungen) → GN2 (4/5)
Etappe 3 ─ Input + Merkblatt 3 → Blatt 7–9 (+ Vertiefungen) → Probearbeit (4/5) → Feedback
Wahlzeit ─ offene Ziele zuerst · P1 Tiermagazin · P2 Tierrätsel · P3 Tiervergleich · Vertiefungen nachholen
Klassenarbeit ─ früher Termin (DS 7) oder später Termin (DS 8); jedes Kind schreibt einmal
```

- **Individuelles Tempo:** Etappenwechsel individuell, nicht im Klassenverband. Material einer Etappe liegt ab ihrem frühesten Start komplett bereit (Etappe 2 ab DS 2, Etappe 3 ab DS 3).
- **Input = Merkblatt:** Aussagen, Beispiele, Reihenfolge und gesicherte Antworten 1:1 identisch; beide werden aus derselben Inhaltsdatei erzeugt. Später startende Kinder bekommen den Input in der Kleingruppe oder lesen das Merkblatt.
- **Pflicht vs. freiwillig:** Pflichtblätter werden nicht zur Auswahl gestellt (individuelle Förderfassung durch die Lehrkraft möglich). Jedes Pflichtblatt hat eine **freiwillige Vertiefung** (gestrichelter Rahmen); Vertiefungen sind nie Hürde für den Nachweis.
- **Nachweise:** fünf vorab definierte Indikatoren; **4/5 = 80 %**. Unter 80 %: gezielt mit dem genannten Blatt üben, erneut nachweisen (Variante B oder Teilnachweis). Kein zusätzlicher GN3; die **Probearbeit ist der dritte Nachweis**. Das frühere GN3-Gespräch ist Übungsfeedback (Haltestelle/Lehrkraft).
- **Probearbeit:** verpflichtend, **unbenotet**, gleicher Aufbau wie die Klassenarbeit; erste Fassung und zusätzliche Hilfen werden unterschieden; Feedback benennt nächsten Schritt; Feedback **vor** dem frühen Klassenarbeitstermin.
- **Klassenarbeit:** zwei Wahltermine innerhalb der Reihe; früher Termin nur nach Feedback und Vorbereitung; danach Projektzeit. Während einer Arbeit stille Projekt-/Vorbereitungsarbeit der anderen. **Keine Partnerhilfe, kein Kiosk** in Nachweisen, Probearbeit, Klassenarbeit.
- **Rückmeldung:** fachliche Leistung und SRL-Anwendung (Lernbuddy) **getrennt**. Tempo, Zahl erledigter Blätter, Projektteilnahme oder ausgefüllte Buddy-Felder ergeben keine Textpunkte.
- **Förderziele** werden vor Nachweisen individuell vereinbart (Antwortform, Hilfen); die 80 % beziehen sich auf die vereinbarte Liste.

## 3 · Lernbuddy und SRL-Elemente

- **Lernbuddy = laminierte A4-Tischvorlage**, kein Arbeitsblatt. Mitte: „Lege hier die Lernaufgabe hin.“ Oben **Planung** (Mein Ziel, Meine Energie/Batterie, Meine Ablenker, Was hilft dir trotzdem anzufangen?). Seitlich **Durchführung** (Auftrag und Ziel lesen, Aufgabe in Schritte teilen, Strategie nutzen, Weg prüfen) mit **Lösungsleiter** (1 Aufgabe noch einmal lesen · 2 Beispiel oder Merkblatt prüfen · 3 Mitschüler:in fragen · 4 Lehrkraft fragen), „Ich stecke fest bei …“, „So komme ich weiter“ und Kante **„Strategie-Karte hier anlegen“**. Unten **Reflexion** (So lief es – Sterne, Darauf bin ich stolz, Nächstes Mal). Rechts-/Linkshändervariante.
- **Konsequenz:** Weil der Buddy A4 ist, werden alle echten Arbeitsblätter **A4 gesetzt und auf A5 verkleinert** gedruckt und in die Mitte gelegt. Auf Fachblättern **keine** Planung/Durchführung/Reflexion-Rahmen, keine SRL-Formulare; erlaubt ist höchstens ein Verweis.
- Die SRL-Elemente werden **außerhalb des Deutschunterrichts** eingeführt (schrittweise Handreichung HBG: offener Anfang → Startklar → Lösungsleiter → Buddy Planung → Durchführung → Reflexion → Strategiefächer → Entscheidungen). In Deutsch werden sie angewendet, keine eigene Einführungssequenz.
- Ein SRL-Zyklus kann mehrere zusammenhängende Blätter umfassen. Reflexion vor dem Abwischen kurz ins Heft übertragen.
- **Begriffe trennen:** Lernweg = Orientierung über die Reihe · Lernbuddy = Tischrahmen für die aktuelle Lernphase · Schreibplan = fachliche Ordnung des Textes · Checkliste K1–K6 = Prüfung der Textqualität.
- **Kontroll-Kiosk** (Laptop im Raum) ist die einzige digitale Schüleranwendung **im Unterricht**; Kinder haben keine iPads.
- **Lern-App fürs Smartphone (Grundversion gebaut, 10.10.2026):** freiwilliger Lernbegleiter für zu Hause auf eigenen oder elterlichen Handys (`lernapp/`, Planung: `planung/Lernapp_Planung.md`). Lernweg, Merkkarten, Übungen, Quiz, Buchstabenrätsel, Training, Üben an Tieren der eigenen Umgebung. **Keine Kiosk-Lösungen zu Blatt 1–9**, keine Prüfungstiere, keine GN-Auszüge, keine Kinderdaten (nur `localStorage`), bewertungsneutral.

## 4 · Partner- und Feedbackphasen (Ergänzungsauftrag 08.10.2026)

| Baustein | Ort | Regel |
|---|---|---|
| Aquarium-Rätsel | Input/Merkblatt 1 Abschnitt 1; Input/Merkblatt 2 „Fische genau beschreiben“ | Grafik mit 4 Fischen A–D (A rund/gestreift, B lang/schmal/gepunktet, C dreieckig/lange Flossen, D klein/große Schwanzflosse); in Graustufen lösbar; ca. 5 Min.; kein Pflichtblatt |
| Leseschritte | Input/Merkblatt 1 „Das erfährst du im Text“, Strategiekarte 1 | 1 einmal lesen, Unbekanntes markieren · 2 Satz erneut lesen, Wörterhilfe, fragen, nicht raten · 3 mit Suchauftrag weiterlesen, markieren (L/N/M) · 4 Stichwort unter passender Überschrift |
| Partnercheck | Blatt 3 | Fundstellen zeigen und gemeinsam am Text prüfen; keine Übernahme ohne Textstelle; Buchstaben statt Farben (L Lebensraum, N Nahrung, M Maß, A Aussehen) |
| Wörterhilfe | eigene Karte, Etappe 2 und 3 | Körperteil + mögliche genaue Angaben, Fachwörter mit Artikel, genaue Verben; Pflichthinweis „Wähle nur Wörter, die zu deinem Tier passen. Prüfe die Angabe am Bild oder im Text.“ |
| Fischrätsel mündlich | Input 2 | zwei sichtbare Merkmale nennen, Partner zeigt den Fisch; kein Nachweis |
| Haltestelle | Blatt 9, Raumschild + Rückmeldekarte | Kind prüft erst selbst, holt sich dann an der Haltestelle eine Rückmeldung (2–3 Fragen); entscheidet selbst, was es ändert; keine Unterschriften/Protokolle |
| Tiermagazin + Kurzvortrag | Projekt P1 | Magazinseite aus vorhandenem überarbeitetem Text; Vortrag 1–2 Min. freiwillig, keine Note, ersetzt keine Prüfung |

Nicht übernommen aus der Kolleginnen-PowerPoint: Kamel/Delfin/Koala, acht verbindliche Vortragsbereiche, 52-Punkte-Bogen, Vortrag als Prüfung.

## 5 · Tierverteilung

| Rolle | Tier | Verwendung |
|---|---|---|
| Beispieltier (Modell) | Fischotter | Inputs, Merkblätter, Blatt 1–6, GN1/GN2, Modelltext in Merkblatt 3 |
| Übungstiere (Wahl, eines je Kind) | Erdmännchen, Roter Panda | Blatt 7–9 (Förder: nur Erdmännchen) |
| Probearbeit | Waschbär | Transfer, neues Tier |
| Klassenarbeit | Biber (Variante 1), Breitmaulnashorn (Variante 2) | Vorschlag: Biber früher Termin, Nashorn später Termin |
| Projekte | Fischotter, Erdmännchen, Roter Panda | Tierpakete (A5-PDFs) |
| Beispielaufgabe Training | Angola-Giraffe (Zikomo, Zoo Dortmund) | durchklickbare Beispielaufgabe mit drei Mustertexten (Mindest-/Regel-/Leistungsstandard) und Vorlesen; liegt als `apps/beispielaufgabe-giraffe/index.html` vor (noch eigenständig, nicht aus `inhalt/`); in der Lern-App vorgesehen |
| Training vor der Klassenarbeit | Elenantilope (Ü1, Kiosk 10), Hirschziegenantilope (Ü2, Kiosk 11) – beide im Zoo Dortmund; auch in der Lern-App (ohne Musterlösung) | `inhalt/training.json`, `tools/build_training.py`: platzsparend A4 Originalgröße (vorn Interview zweispaltig mit Zeilen, hinten Aufgaben/Schreibplan), ≥ 12 pt; Kiosk zeigt Plan mit Zeilen, Musterlösung Mindeststandard, aufklappbar Regelstandard |

Fachlich: Fischotter ≠ Seeotter (keine Seeotter-Bilder). Klassentier der 5er ist der Otter (dekoratives Maskottchen spielt in dieser Reihe keine Rolle).

## 6 · Bewertung und Kriterien

- **K1–K6** (Kinderfassung in Checkliste, Probearbeit „Das zählt“): K1 Informationen · K2 Aussehen (4 Merkmale) · K3 Aufbau · K4 Sachlich (Präsens, ohne Wertungen) · K5 Verständliche Sätze · K6 Schreibung prüfen (Prüfbeleg: Satzanfang einkreisen, zwei Nomen unterstreichen, Punkt markieren).
- **Probearbeit-Indikatoren E3.1–E3.5** fassen K1–K6 zu fünf Zielen: Informationen (K1) · vier Merkmale (K2) · Aufbau (K3) · Sprache (K4+K5) · Schreibung mit Prüfbeleg (K6).
- **Vier Standards** (Förder-, Mindest-, Regel-, Leistungsstandard) beschreiben Leistung je Kriterium, keine Kindergruppen und keine Etappen; keine automatische Umrechnung in Noten. Volltext siehe Abschnitt 13.
- **Klassenarbeit:** Bewertungsseite mit K1–K6 (erfüllt / teilweise / noch nicht, Punktefeld je Bereich), Gesamtpunkte, Note, genutzte Hilfen, Rückmeldung. **Punkteverteilung und Notengrenzen sind noch nicht festgelegt.**
- **Erlaubte Hilfen in Probearbeit und Klassenarbeit:** Seite „Das zählt“ und Hilfeseite (Reihenfolge, Satzanfänge, Prüffragen); Auftrag vorlesen lassen. Nicht erlaubt: Partnerhilfe, Kiosk. Individuelle Anpassungen/Nachteilsausgleich werden notiert.

## 7 · Formate und Gestaltung (verbindlich)

| Material | Satz | Druck | Schrift |
|---|---|---|---|
| Input | HTML-Präsentation, offline, eine Datei | Beamer | groß; farbig erlaubt |
| Merkblatt | A4 hoch, zweispaltig, fließend, max. 2 Seiten | A4 Originalgröße, doppelseitig | Fließtext ≥ 12 pt |
| Übungsblätter (Pflicht + Vertiefung), Checkliste | A4 hoch, je Blatt eine Seite | **auf A5 verkleinert** | **≥ 14 pt** (meist 17 pt) |
| Materialbasis: Interviews | A4, fließend über 1–2 Seiten, Zeilennummern alle 5 Zeilen, Fragen fett, Foto, Wörterhilfe, Hinweis „ausgedacht“ | auf A5 verkleinert (Prüfungen: A4) | 15 pt, nichts unter 14 pt |
| Druckpakete | `ausgabe/pakete/schueler` (je Etappe, Förder-Etappe, Probearbeit, KA V1/V2: erst Material, dann Blätter) und `ausgabe/pakete/lehrkraft` (Merkblätter + GN als Kopiervorlagen, Zeilenbelege, Strategiekarten, Lernweg, Wahlphase, Inputs) | – | – |
| Hilfekarten (Wörterhilfe, Rückmeldekarte) | A4 hoch | auf A5 verkleinert | ≥ 14 pt |
| Gelingensnachweis A/B | A4, 3 Seiten: S. 1 Interviewauszug (Foto, Zeilennummern, ggf. erste Aufgabe), S. 2 Aufgaben (Kind schreibt aufs Blatt, Belege mit Zeile), S. 3 Rückmeldung der Lehrkraft | A4 Originalgröße | Aufgaben ≥ 14 pt |
| Probearbeit, Klassenarbeit | A4, 7 Seiten (s. Abschnitt 10) | A4 Originalgröße | Kinderseiten ≥ 14 pt |
| Wahlphase/Projekte | A4 | A4 Originalgröße | ≥ 12 pt |
| Lernweg | A4, eine Seite | A4 Originalgröße | ≥ 12 pt |
| Strategiekarten | 210 × 99 mm, 3 untereinander pro A4 hoch, Querformat-Karte | Originalgröße, schneiden, laminieren | ≥ 12 pt |
| Raumschild Haltestelle | A4 | Originalgröße, laminieren | groß |
| Förder-Material (1F–9F) | A4, ein Auftrag pro Kasten, Lösungsstreifen | auf A5 verkleinert | ≥ 14 pt (Grundschrift 16,5 pt) |

- **Gedrucktes für Kinder: Graustufen**, druckfreundlich (Struktur über Linien, Rahmen, helles Grau; keine kräftigen Flächen). **Neutral: keine Maskottchen** (kein Otter/Dino), keine Deko-Bilder; fachliche Fotos erlaubt (Graustufenfassung).
- **HTML (Inputs, Kiosk, Animation, Leitfaden, Cockpit): vollfarbig** im HBG-SRL-Schema: Schieferblau `#3E5668`/`#2C3D4C` (Struktur, Navigation), Rostorange `#D97A4A`/`#9E4E22` (Fragen, Aufträge, freiwillige Vertiefung, Aktionen), Salbeigrün `#7DBB6F`/`#4D8B3F` (gesicherte Antworten, Erfolg), Hintergrund `#F5F4F1`, Text `#1E2A35`. Farbfotos in HTML (`assets/bilder/*_farbe.*`, `aquarium_farbe.svg`).
- **Schrift:** Andika (SIL, OFL), eingebettet; keine Netzladung beim Lernen.
- **Kopf-/Fußzeile:** „Deutsch · Jahrgang 5 · Zootiere · Etappe N“; Blattnummer gut sichtbar.
- **Sprache:** einfache, deutliche **Du-Form**, kurze Sätze, Arbeitsort nennen („Schreibe ins Heft“ bzw. bei Nachweisen/Förder „aufs Blatt“). Längere Texte ins Heft.
- **Kennzeichnung:** Pflicht = schwarzes Etikett „PFLICHT“, durchgezogener Rahmen; freiwillig = gestricheltes Etikett/Rahmen „FREIWILLIG“.
- **Inputs:** gesicherte Antworten erst auf Klick/Leertaste (Taste A zeigt alle), Fortschrittsleiste, F = Vollbild; lange Abschnitte über `umbruch_nach` auf zwei Folien.
"""

REPO = """
## 11 · Repository, Quellen und Werkzeuge

```
inhalt/                 Einzige Inhaltsquellen (JSON) – hier ändern, nie in den Ausgaben
  etappe1|2|3.json        Input/Merkblatt, Material, Blätter, Nachweise, Hilfen
  probearbeit_waschbaer.json, klassenarbeit_biber.json, klassenarbeit_breitmaulnashorn.json
  interviews.json         sechs Interviews (250–350 Wörter) + zwei Förder-Kurzinterviews; [[Stelle|Kürzel]]
  foerder_etappe1|2|3.json, kiosk.json, wahlphase.json, strategiekarten.json
tools/
  build_material.py N     Input, Merkblatt, Übungsblätter, Hilfen, GN, Probearbeit (Etappe N)
  build_material.py pruefung inhalt/<datei>.json   Probe-/Klassenarbeit einzeln
  build_foerder.py N      Förder-Material NF und GN-F
  build_kiosk.py          apps/kontroll-kiosk/index.html (mit Browsertest)
  build_extras.py         Wahlphase, Strategiekarten, Lernweg (regulär + F)
  build_animation.py      ausgabe/lernweg/Ablauf_Animation.html
  build_anleitung.py      anleitung.html (Lehrkraft-Leitfaden, prüft alle Links)
  build_interviews.py     Interviews (Entwurf + Prüfliste/Zeilenbelege, zeilen.json); render_interview() für alle Materialseiten
  build_pruefung_f.py     Probearbeit F / Klassenarbeit F (zieldifferent)
  build_training.py       Training Antilopen + zeilen_training.json (vor build_kiosk.py ausführen)
  build_pakete.py         Druckpakete Schüler/Lehrkraft + ZIP (ausgabe/pakete)
  build_lernapp.py        Lern-App (lernapp/) mit Sperrlisten-Prüfung und Browsertest 390×844
  build_wissensbasis.py   diese Datei
ausgabe/                Erzeugte PDFs/HTML (etappe1–3, foerder, pruefungen, wahlphase, strategiekarten, lernweg)
apps/kontroll-kiosk/    Kiosk
lernapp/                Lern-App fürs Smartphone (index.html, manifest, sw.js, Icons); erzeugt von tools/build_lernapp.py aus inhalt/lernapp.json + Etappen/Interviews/Strategiekarten
assets/                 fonts (Andika), bilder (Graustufen + Farbe), grafik (aquarium.svg / _farbe.svg)
planung/                Planungstexte (SRL_Standard, Etappen_Gelingensnachweise, Kompetenzraster, Reihenplanung,
                        Sprachspur, Ergaenzungen_Umsetzung, Foerder_Workflow, Projekte_und_Terminwahl)
materialien/            ältere Vorfassungen (A5-Satz, Otter/Dino-Stil) – nur Tierpakete *_A5.pdf und Planungsbezüge weiter nutzen
skill.md                Produktionsregeln (verbindlich)
```

**Technik:** Python + Playwright/Chromium rendert HTML → PDF; PyMuPDF prüft Schriftgrößen. Jeder Generator prüft automatisch: Seitenüberlauf, Mindestschriftgröße, Input = Merkblatt (Textabgleich), Link-Existenz (Leitfaden), Kiosk-Ansichten. Volle Übungsblätter werden automatisch dichter gesetzt (Schrift bleibt ≥ 14 pt); Förderblätter werden automatisch auf Folgeseiten verteilt.

**Markup in Inhaltsdateien:** `*kursiv*` für Beispielsätze, `**fett**` für Begriffe, `\\n` Zeilenumbruch, `{Wort}` = Lücke (Förder-Lückentext, Wortspeicher automatisch), `[[Textstelle|Kürzel]]` = Markierung im Interview (unsichtbar für Kinder; T Tiername, M Maß der Art, A Aussehen, L Lebensraum, N Nahrung, W Meinung, X Einzeltier/Zooalltag, V Vergleich, Z Zusatz Verhalten, U Vermutung). Zeilenangaben in Blättern/Kiosk („Z. 12“) beziehen sich auf den Satz der Interviews; nach Textänderungen `ausgabe/interviews/zeilen.json` prüfen und Verweise nachziehen.

**Workflow für Änderungen:** Inhaltsdatei ändern → passenden Generator ausführen → Prüfausgabe lesen → bei Bedarf gerenderte Seiten ansehen → committen → `anleitung.html`/`WISSENSBASIS.md` neu erzeugen, wenn Dateien hinzukommen. Deployment über Vercel aus `main` (statisch, kein Build-Schritt); Vercel-Einstellungen nicht ändern.

## 12 · Regeln für die Weiterarbeit (Do / Don't)

**Do**
- Immer zuerst `skill.md` und diese Datei lesen; bei Widersprüchen gelten die Festlegungen vom 08.10.2026 (A4-Satz, neutral, Jahrgang 5) vor älteren Planungstexten.
- Inhalte nur in `inhalt/*.json` ändern; Input und Merkblatt gemeinsam.
- Fachangaben nur aus Material bzw. geprüften Quellen; Quellen und Bildnachweise angeben (Lizenz, Urheber).
- Neue Aufgaben in Du-Form, kurz, kleinschrittig, mit klarem Arbeitsort; Pflicht/freiwillig kennzeichnen.
- Kiosk-Tipps/Lösungen bei jeder Blattänderung nachziehen (`inhalt/kiosk.json`), offene Aufgaben nur mit Vergleichsbeispielen/Prüffragen, nie vollständiger Mustertext als einzige Lösung.
- Gelingensnachweise: genau fünf Indikatoren, 4/5-Regel, Rückmeldeseite „gezeigt / noch offen / Übe mit / erneut gezeigt am“, Ergebnis x/5, „Das gelingt dir schon“, „Dein nächster Schritt“ (Lehrkrafteinschätzung, KI-gestützte Vorbereitung später möglich).

**Don't**
- Keine SRL-Rahmen (Planung/Durchführung/Reflexion) auf Fachblättern; nichts als „Lernbuddy“ bezeichnen, was keiner ist.
- Keine Maskottchen, keine Farbe in Druckmaterial für Kinder, keine Schrift < 14 pt auf Kinderseiten (A5-Druck).
- Keine zusätzlichen Pflichtnachweise, keine Mindestwortzahl, keine Punkte für Tempo/SRL-Felder.
- Keine Pflichtblätter zur freien Auswahl stellen; Vertiefungen nicht zur Hürde machen.
- Keine Tiere außerhalb der Tierverteilung ohne Rücksprache; Fischotter-Musterlösungen nicht als Prüfungsaufgaben.
- Keine Netzladung in Schülermaterial; HTML-Dateien eigenständig (Schrift, Bilder eingebettet).
"""


def kompetenzraster():
    t = (ROOT / "planung" / "Kompetenzraster_4_Standards.md").read_text(encoding="utf-8")
    tab = "\n".join(l for l in t.splitlines() if l.startswith("|"))
    return "\n## 13 · Kompetenzraster mit vier Standards (Volltext)\n\n" + tab + "\n"


def interviews_text():
    import re as _re
    iv = j("interviews.json")
    out = ["### 8.0 Interviews als Textbasis\n", f"Rahmen: {iv['rahmen']} Hinweis auf jeder Seite: „{iv['hinweis_fiktiv']}“ "
           "Keine echte Person, kein echter Zoo. Lange Interviews 250–350 Wörter (Prüfungen etwa 265), Förder 6 Fragen. "
           "Markierung: ⟦Stelle|Kürzel⟧ wie in `inhalt/interviews.json`.\n"]
    for t in iv["tiere"] + iv["foerder"]:
        out.append(f"#### {t['rolle']} · {t['titel']} ({t['person']}, `{t['id']}`)\n")
        for q, a in t["paare"]:
            out.append(f"- **{q}** " + _re.sub(r"\[\[(.+?)\|(\w)\]\]", r"⟦\1|\2⟧", a))
        out.append("- Wörterhilfe: " + "; ".join(f"{w} = {e}" for w, e in t["woerter"]) + "\n")
    return "\n".join(out)


def etappen():
    import re as _re
    out = ["\n## 8 · Etappen im Detail ⚙\n", interviews_text()]
    kiosk = j("kiosk.json")["blaetter"]
    for n in (1, 2, 3):
        d = j(f"etappe{n}.json")
        out.append(f"### Etappe {n} · {d['titel']}\n\n**Ziel (Kind):** {d['ziel']}\n")
        out.append("**Input und Merkblatt %d – Abschnitte (identisch):**\n" % n)
        for k, s in enumerate(d["input"], 1):
            out.append(f"{k}. **{s['titel']}**")
            for lab, txt in s["bloecke"]:
                out.append(f"   - _{lab}:_ {clean(txt)}")
        out.append(f"\n**Abschlusssatz:** {d['abschluss']}\n")
        if d.get("interviews"):
            out.append("**Materialbasis:** %s%s (Text siehe 8.0; Paket: erst Material, dann Blätter)\n"
                       % ("Fotoseite + " if d.get("bildseite") else "", ", ".join("Interview " + i for i in d["interviews"])))
        mats = [] if d.get("interviews") else d.get("materialien") or ([dict(d["material"], foto=d["foto"])] if d.get("material") else [])
        for m in mats:
            out.append(f"**Materialseite „{m['titel']}“** (Foto: {m['foto']['nachweis']}):\n> {m['text']}\n")
            if m.get("woerter"):
                out.append("Wörterhilfe: " + "; ".join(f"{w} = {e}" for w, e in m["woerter"]) + "\n")
        out.append("**Pflichtblätter:**\n")
        for b in d["blaetter"]:
            out.append(f"- **Blatt {b['nr']} · {b['titel']}** (Du brauchst: {clean(b['brauchst'])})")
            if b.get("lies"):
                out.append(f"  - Lies: {clean(b['lies'])}")
            if b.get("material"):
                out.append(f"  - {b['material']['titel']}: {clean(b['material']['text'])}")
            if b.get("teile"):
                for t in b["teile"]:
                    art = "Pflicht" if t["art"] == "pflicht" else "Freiwillige Vertiefung"
                    txt = " ".join(filter(None, [t.get("text", ""), " | ".join(t.get("aufgaben", [])), t.get("nachtext", "")]))
                    out.append(f"  - {art} – {t['titel']}: {clean(txt)}")
            else:
                out.append("  - Pflicht: " + clean(" | ".join(b["pflicht"])))
                if b.get("sprachdetektiv"):
                    out.append("  - Pflicht – Sprachdetektiv: " + clean(b["sprachdetektiv"]))
                if b.get("vertiefung"):
                    out.append("  - Freiwillige Vertiefung: " + clean(b["vertiefung"]))
            if b.get("tipp"):
                out.append("  - Achte darauf: " + clean(b["tipp"]))
            ki = kiosk.get(str(b["nr"]))
            if ki:
                out.append(f"  - Kiosk-Tipp: {clean(ki['tip'])}")
                out.append(f"  - Kiosk-Lösung ({ki['type']}): {clean(ki['solution'])}")
                if ki.get("extra"):
                    out.append(f"  - Kiosk-Vertiefung: {clean(ki['extra'])}")
        for z in d.get("zusatzseiten", []):
            out.append(f"- **{z['kennung']} · {z['titel']}:** " + " · ".join(f"{t['titel']}: {t['text']}" for t in z["teile"]))
        for h in d.get("hilfen", []):
            line = f"- **Hilfekarte {h['kennung']} · {h['titel']}** – Hinweis: {h['hinweis']}"
            if h.get("tabelle"):
                line += " Tabelle: " + "; ".join(f"{a}: {b}" for a, b in h["tabelle"]["zeilen"]) + "."
            for tit, txt in h.get("listen", []):
                line += f" {tit}: {clean(txt)}."
            out.append(line)
        if d.get("schild"):
            out.append(f"- **Raumschild:** {d['schild']['titel']} – {d['schild']['untertitel']}")
        if d.get("nachweis"):
            nw = d["nachweis"]
            out.append(f"\n**Gelingensnachweis {n} „{nw['titel']}“ (Varianten {', '.join(nw['varianten'])})** – 4 von 5 Indikatoren:\n")
            out.append("| ID | Kind-Formulierung | erreicht, wenn | Übe mit |\n|---|---|---|---|")
            for z in nw["ziele"]:
                out.append(f"| {z['id']} | {z['kind']} | {z['lehrkraft']} | {z['ueben']} |")
            out.append("\nAufgaben: " + " · ".join(f"{i}) {a['titel']}: {a['text']}" for i, a in enumerate(nw["aufgaben"], 1)))
            for v, c in nw["varianten"].items():
                if c.get("interview"):
                    out.append(f"\n- Variante {v} Interviewauszug (S. 1, Zeilennummern): " + " ".join(f"**{q}** {_re.sub(r'\\[\\[(.+?)\\|(\\w)\\]\\]', r'⟦\\1|\\2⟧', a)}" for q, a in c["interview"]))
                    if c.get("einordnen"):
                        out.append(f"  - Einordnen (Sachangabe/nur Otto/Meinung): " + "; ".join(f"{t} → {k}" for t, k in c["einordnen"]))
                    if c.get("themen"):
                        out.append(f"  - Sachsätze zu: {', '.join(c['themen'])}; Meinung umformen: „{c['verbessern']['satz']}“")
                if c.get("text"):
                    out.append(f"\n- Variante {v} Materialtext: {c['text']}")
                if c.get("wortgruppen"):
                    out.append(f"\n- Variante {v}: Wortgruppen {' | '.join(c['wortgruppen'])}; verbessern „{c['verbessern']['satz']}“ (Material: {c['verbessern']['material']})")
        out.append("")
    return "\n".join(out)


def pruefungen():
    out = ["\n## 9 · Probearbeit und Klassenarbeit ⚙\n",
           "Gemeinsamer Aufbau (A4, 7 Seiten; Vorbild: Lernerfolgskontrolle der Reihe Wunschbriefe): "
           "Material vorn: Interview (2 Seiten, Foto, Zeilennummern, Wörterhilfe) · 1 Auftrag (Situation, Auftrags-Checkliste inkl. „Markiere Sachangaben, streiche Meinungen/Einzeltier“, Arbeitszeit-Feld, bei KA Terminwahl) · "
           "3 Planung (Schreibplan Überblick/Aussehen ×4/Lebensraum/Nahrung) · 4 Schreibseite (Überschrift + Linien, Prüfhinweis) · "
           "5 „Dein Text: Das zählt“ (K1–K6 zum Abhaken) · 6 Hilfeseite (erlaubt) · 7 Lehrkraftseite (Probearbeit: Rückmeldung E3.1–E3.5, Hilfen, x/5, nächster Schritt, Wahlzeit, Klassenarbeitstermin; Klassenarbeit: Bewertung K1–K6 mit Punkten und Note).\n"]
    for f in ("probearbeit_waschbaer.json", "klassenarbeit_biber.json", "klassenarbeit_breitmaulnashorn.json"):
        p = j(f)
        out.append(f"### {p['titel']} ({p['art']}) · `inhalt/{f}`\n")
        out.append(f"- Situation: {p['situation']}")
        if p.get("interview"):
            out.append(f"- Material: Interview `{p['interview']}` (vor dem Auftrag, mit Zeilennummern; Text siehe 8.0)")
        else:
            out.append(f"- Sachtext: {p['material']['text']}")
        out.append(f"- Foto: {p['material']['foto']['nachweis']}")
        if p.get("ziele"):
            out.append("- Indikatoren: " + " · ".join(f"{z['id']} {z['kind']} (erreicht, wenn {z['lehrkraft']})" for z in p["ziele"]))
        if p.get("bewertung"):
            out.append("- Bewertungserwartung: " + " · ".join(f"{k[0]} {k[1]}: {k[2]}" for k in p["bewertung"]["kriterien"]))
        out.append("")
    return "\n".join(out)


def wahl_strategie():
    w = j("wahlphase.json")
    s = j("strategiekarten.json")
    out = ["\n## 10 · Wahlphase, Strategiekarten, Kiosk, Lernweg ⚙\n", "### Wahlphase (nach Feedback zur Probearbeit)\n",
           f"{w['uebersicht']['einleitung']} {w['uebersicht']['zuerst']} {w['uebersicht']['regeln']}\n"]
    for p in w["projekte"]:
        out.append(f"- **{p['nr']} {p['titel']}** – {p['ergebnis']} Schritte: " + " · ".join(f"{t}: {x}" for t, x in p["schritte"])
                   + f" Gelingt, wenn: {'; '.join(p['gelingt'])}. Erweiterung (freiwillig): {clean(p['erweiterung'])}")
    out.append("\n### Strategiekarten (am Lernbuddy anlegen; Aufbau: Wann? · 4 Schritte · Beispiel · Hat es geholfen? ja/etwas/nein)\n")
    for k in s["karten"]:
        if k.get("leer"):
            out.append(f"{k['nr']}. **{k['titel']}** – leere Karte für eine eigene Strategie")
        else:
            out.append(f"{k['nr']}. **{k['titel']}** – Wann: {k['wann']} Schritte: " + " · ".join(clean(x) for x in k["schritte"]) + f" Beispiel: {clean(k['beispiel'])}")
    out.append("\n### Kontroll-Kiosk\n\nNachbau des Wunschbrief-Kiosks: Startbildschirm „Tipp oder Lösung?“, Blattnummer 1–9 per Zahlenfeld/Tastatur, Ergebnis mit Wechsel Tipp↔Lösung, freiwillige Vertiefung aufklappbar; nach 3 Minuten Inaktivität bei der Nummerneingabe zurück zum Start; Esc = Start; Vollbild; offline; keine Kinderdaten. Direktaufruf `?mode=solution&blatt=7`. Nicht für Nachweise/Probearbeit/Klassenarbeit. Texte: `inhalt/kiosk.json` (Inhalte siehe Abschnitt 8 je Blatt).\n")
    out.append("### Lernweg (A4, je Kind)\n\nStationen je Etappe: Start (Input, Merkblatt) · Pflichtblätter zum Abhaken · Vertiefungen (freiwillig) · Nachweisfeld (x/5, Datum, Freigabe der Lehrkraft); Etappe 3: Probearbeit, Feedback erhalten. Danach Wahlzeit (offene Ziele, P1–P3, Vertiefung) und Klassenarbeit (früher/später Termin). F-Fassung mit Blatt 1F–9F ohne Vertiefungen.\n")
    out.append("### Ablauf-Animation\n\nHTML-Animation (11 Szenen) für den Einstieg in DS 1: Wegekarte mit Spielstein „Du“; Input → Blätter auf dem Lernbuddy → Hilfen (Strategiekarte, Lösungsleiter, Kiosk) → Nachweis mit 5 Punkten und Schleife „noch üben“ → Etappe 2 → Etappe 3 mit Probearbeit → Feedback → Wahlzeit → Klassenarbeit → „Dein Tempo“.\n")
    return "\n".join(out)


def foerder():
    out = ["\n## 14 · Zieldifferentes Material (Förderschwerpunkt Lernen) ⚙\n",
           "Zwei Kinder; kurze Texte möglich. Gleiche Etappen und Blattnummern mit „F“, gleicher Input, Fischotter als Beispieltier (Etappe 3F: nur Erdmännchen). "
           "Je Etappe vereinfachte **Merkkarte**, **Fotoseite** mit nummerierten Bildstellen und **Kurzinterview** (6 Fragen, Antworten 1–2 Sätze, je eine Meinung und Angaben nur über das Zootier; Aufgaben „Info oder Meinung?“ und „Wer ist gemeint?“). Kleinschrittig: ein Auftrag pro Kasten mit Symbol je Format. "
           "Formate: ankreuzen · zuordnen (Zahl ins Kästchen, ggf. nummerierte Bedeutungen) · sortieren (Wortspeicher → Spalten) · Lückentext (Wortspeicher, ggf. Ablenker) · Wortkarten zu einem Satz ordnen · Satz weiterschreiben · Prüfliste · Bild betrachten · Hinweis. "
           "Jede Seite mit Lösungsstreifen auf dem Kopf zum Umknicken. Schreiben aufs Blatt. GN-F-Ziele sind Vorschläge; Förderziele individuell vereinbaren, Zeile für eigenes Förderziel.\n"]
    for n in (1, 2, 3):
        d = j(f"foerder_etappe{n}.json")
        out.append(f"### Etappe {n}F · {d['titel']}\n")
        out.append("- Merkkarte: " + " · ".join(f"{a}: {clean(b)}" for a, b in d["merkkarte"]["punkte"]))
        out.append("- Material: Fotoseite mit Zahlen + Kurzinterview `%s` (Text siehe 8.0)" % d.get("interview", "–"))
        out.append("- Bildstellen: " + ", ".join(f"{p[0]}" for p in d["foto"]["punkte"]) + f" ({d['foto']['alt']})")
        for b in d["blaetter"]:
            teile = []
            for a in b["aufgaben"]:
                t = f"[{a['typ']}] {clean(a['auftrag'])}"
                if a["typ"] == "luecke":
                    t += f" Lösung: {', '.join(gaps(a['text']))}"
                elif a["typ"] == "ankreuzen":
                    t += " Richtig: " + ", ".join(x for x, ok in a["items"] if ok)
                elif a["typ"] == "sortieren":
                    t += " Lösung: " + "; ".join(f"{h}: {', '.join(w)}" for h, w in a["spalten"])
                elif a["typ"] == "zuordnen":
                    t += " Lösung: " + ", ".join(f"{w}={z}" for w, z in a["paare"])
                elif a["typ"] in ("ordnen", "schreiben"):
                    t += f" Lösung: {a['loesung']}"
                teile.append(t)
            out.append(f"- **Blatt {b['nr']} · {b['titel']}:** " + " | ".join(teile))
        if d.get("nachweis"):
            out.append("- **GN%dF:** " % n + " · ".join(f"{z['id']} {z['kind']} (erreicht, wenn {z['lehrkraft']})" for z in d["nachweis"]["ziele"]))
        out.append("")
    return "\n".join(out)


ZEIT = """
## 15 · Zeitplan der acht Doppelstunden und Druckplan

| DS | Geschehen | bereitliegen (gedruckt) |
|---|---|---|
| vorher | Kiosk auf Laptop testen, Förderziele vereinbaren, Termine/Arbeitszeit/Punkte festlegen | Lernweg (je Kind; F-Fassung), Strategiekarten (laminiert, je Tisch), Haltestellen-Schild |
| 1 | Animation, Input 1, Start Blatt 1–4, Strategiekarten 1–3 vorstellen | Merkblatt 1, Übungsblätter Etappe 1, Förder 1F |
| 2 | GN1 nach Pflichtkern, Wiederholung bei < 4/5; Input 2 für Freigegebene | GN1 A/B, GN1F, Merkblatt 2, Übungsblätter Etappe 2, Wörterhilfe, Förder 2F |
| 3 | GN2; Input 3 für Freigegebene, Tierwahl Erdmännchen/Roter Panda | GN2 A/B, GN2F, Merkblatt 3, Übungsblätter Etappe 3, Förder 3F |
| 4 | Schreiben und prüfen; Haltestelle; Unterstützung prüfen | Rückmeldekarten |
| 5 | Erstes Probearbeitsfenster; Rückmeldung bis DS 6 | Probearbeit Waschbär |
| 6 | Zweites Fenster, Feedback, Terminwahl; Wahlzeit | Wahlphase/Projekte, Tierpakete Fischotter/Erdmännchen/Roter Panda |
| 7 | Früher Klassenarbeitstermin; danach Projektzeit | Klassenarbeit Variante 1 (Biber) |
| 8 | Später Termin; Tiermagazin, Kurzvorträge, Reihenreflexion | Klassenarbeit Variante 2 (Breitmaulnashorn) |

Zeitansätze sind Planungswerte, keine individuellen Fristen. Pflichtumfang ca. 200 Minuten (ungetestet). Bei Zeitkonflikten zuerst freiwillige Ergänzungen kürzen, nicht Schreib-/Überarbeitungsprozess.

## 16 · Offene Punkte (Stand {stand})

- Arbeitszeit der Probearbeit; Arbeitszeit, Punkteverteilung und Notengrenzen der Klassenarbeit.
- Foto Breitmaulnashorn fehlt (Platzhalter); Biber-Foto vorläufig (Tierpaket, CC BY-SA 3.0). Wunschbild tierdoku.de nicht ladbar und ohne freie Lizenz.
- Probearbeit F (Waschbär) und Klassenarbeit F (Biber) liegen vor (`inhalt/probearbeit_f_waschbaer.json`, `inhalt/klassenarbeit_f_biber.json`, `tools/build_pruefung_f.py`): Kurzinterview → Auftrag → Aufgaben (Info/Meinung, Wer ist gemeint, Plan sortieren, Lückentext-Beschreibung, eigener Satz, Prüfliste) → Rückmeldung F3.1–F3.5 bzw. Bewertung (22 Punkte, Vorschlag). Offen: zieldifferente Bewertung mit Schulvorgaben abstimmen; F-Fassung Nashorn bei Bedarf.
- Zuordnung Variante ↔ Termin (Vorschlag Biber früh, Nashorn spät).
- Lehrkraft-Cockpit `index.html` zeigt noch Vorfassungen.
- Gedruckte Lösungsfassung (Tipps/Lösungen wie im Kiosk) und ggf. Übungskarten-Modus im Kiosk.
- Unterrichtserprobung steht aus; Zeitbudget nach Erprobung prüfen.
- Lern-App (`planung/Lernapp_Planung.md`): Grundversion gebaut (Mein Weg, Wissen, 14 Übungen inkl. Training Ü1/Ü2, Buchstabenrätsel, Zuhause); offen: Quiz je Etappe, Silbenrätsel/Suchsel, Giraffe, Schalter „Einfach“. Freigabe für Kinder steuert die Lehrkraft über den QR-Code. Klassenarbeiten sollen später extern gespeichert werden.
- Angola-Giraffe (`apps/beispielaufgabe-giraffe/`) in Inhaltsdatei überführen und in die Lern-App einbinden; Pflegerin heißt dort wie bei der Elenantilope „Frau Demir“ → neuen Namen wählen.

## 17 · Glossar

| Begriff | Bedeutung in dieser Reihe |
|---|---|
| Etappe | einer von drei Lernabschnitten, individuell durchlaufen |
| Input | kurze Lehrkraft-Präsentation (HTML) zu Beginn einer Etappe, auch als Kleingruppeninput wiederholbar |
| Merkblatt | gedruckte, inhaltsgleiche Fassung des Inputs zum Nachlesen |
| Pflichtblatt | Blatt 1–9, verpflichtend; enthält eine freiwillige Vertiefung |
| Vertiefung | freiwilliger Zusatz je Blatt, später nachholbar, nie Hürde |
| Gelingensnachweis (GN) | kurzer Abschlussnachweis Etappe 1/2, Variante A (Erstversuch), B (Wiederholung) |
| Indikator | eines der fünf vorab definierten Ziele eines Nachweises (E1.1–E3.5, F1.1–F2.5) |
| Probearbeit | unbenoteter Abschluss Etappe 3 im Aufbau der Klassenarbeit |
| Wahlzeit | Phase nach dem Feedback: Projekte, Wiederholung, Vertiefungen |
| Lernbuddy | laminierter A4-Tischrahmen für Planung, Durchführung, Reflexion; Blatt liegt in der Mitte |
| Lösungsleiter | feste Hilfereihenfolge: lesen → Beispiel/Merkblatt → Kind fragen → Lehrkraft fragen |
| Strategiekarte | Karte 210 × 99 mm, wird am Lernbuddy angelegt |
| Haltestelle | Ort im Raum für Partnerrückmeldung zum Übungstext (Blatt 9) |
| Kontroll-Kiosk | Laptop-Anwendung mit Tipps und Lösungen zu Blatt 1–9 |
| Lern-App | freiwilliger Smartphone-Lernbegleiter für zu Hause, ohne Blattlösungen und ohne Prüfungsinhalte |
| Sprachspur | in die Etappen integrierte Grammatik-/Rechtschreibinhalte |
| K1–K6 | Textkriterien: Informationen, Aussehen, Aufbau, Sachlich, Verständlich, Schreibung |
| F-Material | zieldifferentes Material (Förderschwerpunkt Lernen), Blätter 1F–9F |
"""


def main():
    stand = date.today().strftime("%d.%m.%Y")
    teile = [KOPF.format(stand=stand), PRINZIPIEN, etappen(), pruefungen(), wahl_strategie(), REPO, kompetenzraster(), foerder(), ZEIT.format(stand=stand)]
    text = "\n".join(teile)
    # Abschnittsreihenfolge nach Nummer
    blocks = re.split(r"(?m)^(?=## )", text)
    head, rest = blocks[0], blocks[1:]
    def key(b):
        m = re.match(r"## (\d+)", b)
        return int(m.group(1)) if m else -1
    rest.sort(key=key)
    toc = "\n## Inhalt\n\n" + "\n".join("- " + re.match(r"## (.+)", b).group(1).replace(" ⚙", "") for b in rest if key(b) > 0) + "\n\n"
    zero = [b for b in rest if key(b) == 0]
    others = [b for b in rest if key(b) != 0]
    out = head + "".join(zero) + toc + "".join(others)
    (ROOT / "WISSENSBASIS.md").write_text(out.rstrip() + "\n", encoding="utf-8")
    print("ok: WISSENSBASIS.md, %d Zeichen, %d Zeilen" % (len(out), out.count("\n")))


if __name__ == "__main__":
    main()
