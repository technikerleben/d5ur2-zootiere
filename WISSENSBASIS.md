# Wissensbasis · Deutsch 5 · Unterrichtsreihe „Zootiere“

> **Zweck:** Vollständige, verbindliche Wissensgrundlage für ein LLM, das an dieser Reihe weiterarbeitet (Material ergänzen, ändern, prüfen, Fragen beantworten).
> **Stand:** 09.10.2026. Abschnitte mit ⚙ werden aus den Inhaltsdateien `inhalt/*.json` erzeugt (`python tools/build_wissensbasis.py`) und spiegeln den aktuellen Materialstand.
> **Repo:** `technikerleben/d5ur2-zootiere`, Arbeitsbranch `claude/etappe1-muster` (noch nicht in `main`). Lehrkraft-Leitfaden: `anleitung.html`.

## 0 · Kurzfassung in zehn Sätzen

1. Deutsch, Jahrgang 5, Heinrich-Böll-Gesamtschule Dortmund; vier Wochen, acht Doppelstunden à 90 Minuten.
2. Zielkompetenz: **ein Zootier mithilfe von Bild und Sachtext sachlich und geordnet beschreiben** (Aufgabentyp 2, informierendes Schreiben, materialgestützt).
3. Die Reihe ist in **drei Etappen** gegliedert, die jedes Kind **im eigenen Tempo** durchläuft.
4. Jede Etappe: **Input (HTML-Präsentation) + inhaltsgleiches Merkblatt → Pflichtblätter mit freiwilliger Vertiefung → Abschlussnachweis**.
5. Nachweise prüfen **fünf Indikatoren**; **4 von 5 (80 %)** = Freigabe für die nächste Etappe; sonst gezielt üben und erneut nachweisen (Variante B).
6. Etappe 3 endet mit der **Probearbeit** (unbenotet, mit Feedback). Danach **Wahlzeit** (Projekte P1–P3, Wiederholung, Vertiefungen).
7. Die **Klassenarbeit** wird an **einem von zwei Wahlterminen** geschrieben (Doppelstunde 7 oder 8), zwei Varianten (Biber, Breitmaulnashorn).
8. **Fischotter** ist das durchgehende Beispieltier; Übungstiere Erdmännchen/Roter Panda; Waschbär für die Probearbeit; Biber und Breitmaulnashorn für die Klassenarbeit.
9. Der **Lernbuddy** (laminierter A4-Tischrahmen, SRL) wird genutzt, aber **nie auf Fachblättern nachgebaut**; Strategiekarten werden an ihm angelegt.
10. Gedrucktes für Kinder ist **graustufig, neutral (ohne Maskottchen), mindestens 14 pt**; HTML-Seiten dürfen **farbig** sein (HBG-SRL-Farbschema).



## Inhalt

- 1 · Rahmen und Lehrplanbezug
- 2 · Verbindlicher SRL-Standard (Ablauf)
- 3 · Lernbuddy und SRL-Elemente
- 4 · Partner- und Feedbackphasen (Ergänzungsauftrag 08.10.2026)
- 5 · Tierverteilung
- 6 · Bewertung und Kriterien
- 7 · Formate und Gestaltung (verbindlich)
- 8 · Etappen im Detail
- 9 · Probearbeit und Klassenarbeit
- 10 · Wahlphase, Strategiekarten, Kiosk, Lernweg
- 11 · Repository, Quellen und Werkzeuge
- 12 · Regeln für die Weiterarbeit (Do / Don't)
- 13 · Kompetenzraster mit vier Standards (Volltext)
- 14 · Zieldifferentes Material (Förderschwerpunkt Lernen)
- 15 · Zeitplan der acht Doppelstunden und Druckplan
- 16 · Offene Punkte (Stand 09.10.2026)
- 17 · Glossar

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
- **Kontroll-Kiosk** (Laptop im Raum) ist die einzige digitale Schüleranwendung; Kinder haben keine iPads.

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
| Übungsblätter (Pflicht + Vertiefung) inkl. Materialseiten, Checkliste | A4 hoch, je Blatt eine Seite | **auf A5 verkleinert** | **≥ 14 pt** (meist 17 pt) |
| Hilfekarten (Wörterhilfe, Rückmeldekarte) | A4 hoch | auf A5 verkleinert | ≥ 14 pt |
| Gelingensnachweis A/B | A4: S. 1 Aufgaben (Kind schreibt aufs Blatt), S. 2 Rückmeldung der Lehrkraft | A4 Originalgröße | Aufgaben ≥ 14 pt |
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


## 8 · Etappen im Detail ⚙

### Etappe 1 · Informationen finden und ordnen

**Ziel (Kind):** Ich kann ein Tier genau betrachten und Informationen aus Bild und Text ordnen.

**Input und Merkblatt 1 – Abschnitte (identisch):**

1. **Finde den Fisch**
   - _Schau genau hin:_ Im Aquarium schwimmen vier Fische: A, B, C und D.
   - _Beschreibung 1:_ *Der Fisch hat einen langen, schmalen Körper. Auf dem Körper sind dunkle Punkte.*
   - _Beschreibung 2:_ *Der Fisch ist schön und schwimmt im Wasser.*
   - _Frage:_ Welche Beschreibung passt nur zu einem Fisch? Zeige den Hinweis, der dir hilft. Mache Beschreibung 2 genauer.
   - _Gesicherte Antwort:_ Beschreibung 1 passt nur zu Fisch B: langer, schmaler Körper und dunkle Punkte. Beschreibung 2 passt zu allen Fischen. Genauer ist zum Beispiel: *Der Fisch hat einen runden Körper mit dunklen Streifen.* Das ist Fisch A.
2. **Genau statt wertend**
   - _Dein Ziel:_ Du findest genaue Angaben über ein Tier. Eine Beschreibung hilft anderen, sich das Tier vorzustellen.
   - _Vergleiche:_ A: *Der Fischotter ist toll. Sein Fell ist schön.* / B: *Der Fischotter hat einen langen Körper und kurze Beine. Sein Fell ist oben dunkelbraun.*
   - _Frage:_ Welcher Text hilft dir beim Vorstellen? Warum?
   - _Gesicherte Antwort:_ B nennt Körperform, Beinlänge und Fellfarbe. A enthält Meinungen. „schön“ und „toll“ sind keine genauen Merkmale.
3. **Das zeigt dir das Foto**
   - _Beobachte:_ Zeige zwei Körperteile. Nenne jeweils ein genaues Merkmal.
   - _Gesicherte Antwort:_ An der Schnauze sitzen lange **Tasthaare**. Die Ohren sind klein. Zeige die passenden Bildstellen.
   - _Grenze des Bildes:_ **Schwimmhäute** und die gesamte **Körperlänge** erkennst du hier nicht sicher. Erfinde keine verdeckten Merkmale.
4. **Das erfährst du im Text**
   - _So liest du:_ 1. Lies den Text einmal. Markiere Wörter, die du nicht verstehst. / 2. Lies den Satz um das Wort noch einmal. Nutze die Wörterhilfe. Frage bei Bedarf ein anderes Kind oder deine Lehrkraft. Rate keine Bedeutung. / 3. Lies mit deinem Suchauftrag weiter. Suchwörter helfen: *lebt, frisst, Zentimeter*. Markiere die passende Textstelle: **L** für Lebensraum, **N** für Nahrung, **M** für Maß. / 4. Notiere die Information als Stichwort unter der passenden Überschrift.
   - _Lies gezielt:_ *Der Fischotter lebt an Flüssen und Seen mit geschützten Ufern. Er hat einen lang gestreckten Körper und kurze Beine. Sein Fell ist oben dunkelbraun. Sein Kopf ist breit und flach. An der Schnauze sitzen lange Tasthaare. Kopf und Rumpf sind zusammen etwa 60 bis 90 Zentimeter lang. Der Schwanz kommt noch dazu. Der Fischotter frisst vor allem Fische, aber auch Frösche und Krebse.*
   - _Frage:_ Wo lebt der Fischotter? Was frisst er? Wie lang sind Kopf und Rumpf? Zählt der Schwanz dazu?
   - _Gesicherte Antwort:_ Flüsse und Seen mit geschützten Ufern; vor allem Fische; Kopf und Rumpf etwa 60–90 cm. Der Schwanz zählt nicht dazu. Zeige die Textstellen.
   - _Mit einem Partner prüfen:_ Zeige deine Textstelle. Erkläre, welche Information du gefunden hast. Vergleicht: Passt die Stelle zur Frage? Bei verschiedenen Antworten prüft ihr gemeinsam im Text.
5. **Sprachdetektiv**
   - _Vier Wortarten:_ **Nomen** benennen Tiere, Dinge und mehr: *Otter, Fell*. Du schreibst sie groß. / **Artikel** begleiten Nomen: *der Otter, das Fell, die Pfote*. / **Verben** sagen, was geschieht oder wie etwas ist: *schwimmt, ist*. / **Adjektive** beschreiben Merkmale: *braun, dicht, lang*.
   - _Wörter zerlegen:_ *der Körper + die Länge = die Körperlänge* / Das letzte Nomen bestimmt den Artikel.
   - _Frage:_ „Der Otter schwimmt.“ Welche Wortarten findest du?
   - _Gesicherte Antwort:_ *Der*: Artikel; *Otter*: Nomen; *schwimmt*: Verb.
6. **Informationen ordnen**
   - _So gehst du vor:_ Lies den Auftrag. Suche passende Angaben in Bild und Text. Notiere Stichwörter unter Überschriften.
   - _Beispiel: geordnete Sammlung:_ **Überblick:** Fischotter; Kopf und Rumpf 60–90 cm, Schwanz zusätzlich / **Aussehen:** langer Körper; kurze Beine; dunkelbraune Oberseite; lange Tasthaare / **Lebensraum:** Flüsse und Seen; geschützte Ufer / **Nahrung:** vor allem Fische
   - _Frage:_ Wohin gehört „breiter, flacher Kopf“?
   - _Gesicherte Antwort:_ Unter Aussehen. Eine genaue Angabe kann im Bild und im Text vorkommen. Zeige, welche Quelle du genutzt hast.

**Abschlusssatz:** Bearbeite Blatt 1–4. Vertiefungen sind freiwillig. Danach zeigst du dein Können im Gelingensnachweis. Vier von fünf Zielen reichen für Etappe 2.

**Materialseite „Der Fischotter“** (Foto: Foto: Dave Pape · Public Domain):
> Der Fischotter lebt an Flüssen und Seen mit geschützten Ufern. Er hat einen lang gestreckten Körper und kurze Beine. Sein Fell ist oben dunkelbraun. Sein Kopf ist breit und flach. An der Schnauze sitzen lange Tasthaare. Kopf und Rumpf sind zusammen etwa 60 bis 90 Zentimeter lang. Der Schwanz kommt noch dazu. Der Fischotter frisst vor allem Fische, aber auch Frösche und Krebse.

Wörterhilfe: Rumpf = Körper ohne Kopf, Beine und Schwanz; Tasthaare = Haare zum Ertasten; Ufer = Rand eines Flusses oder Sees

**Pflichtblätter:**

- **Blatt 1 · Welche Beschreibung hilft?** (Du brauchst: Heft · Merkblatt 1)
  - Lies: A: *Der Fischotter ist toll. Sein Fell ist schön.* / B: *Der Fischotter hat einen langen Körper und kurze Beine. Sein Fell ist oben dunkelbraun.*
  - Pflicht: Schreibe A oder B ins Heft. Welcher Text hilft dir, das Tier vorzustellen? Begründe. | Notiere zwei genaue Angaben aus Text B. Erkläre: Warum hilft „toll“ beim Beschreiben wenig?
  - Pflicht – Sprachdetektiv: Schreibe den Satz ins Heft: *„Der Fischotter hat einen langen Körper.“* Schreibe **N** über die Nomen und **A** über die Artikel.
  - Freiwillige Vertiefung: Ersetze *„Der Fischotter hat schöne Beine“* durch eine genaue Angabe aus dem Material. Erkläre den Unterschied.
  - Kiosk-Tipp: Welcher Text sagt dir, wie der Fischotter aussieht? Suche Wörter für Form, Länge und Farbe.
  - Kiosk-Lösung (Lösung und Vergleich): Aufgabe 1: Text B hilft. Er nennt Körperform, Beinlänge und Fellfarbe. Text A enthält nur Meinungen. /  / Aufgabe 2 – zwei genaue Angaben, zum Beispiel: langer Körper; kurze Beine; Fell oben dunkelbraun. / „toll“ sagt nur, wie jemand das Tier findet. Damit kannst du dir das Tier nicht vorstellen. /  / Sprachdetektiv: / A (Artikel): Der, einen / N (Nomen): Fischotter, Körper
  - Kiosk-Vertiefung: Beispiel: „Der Fischotter hat kurze Beine.“ / „schön“ ist eine Meinung. „kurz“ kannst du am Material prüfen.
- **Blatt 2 · Schau genau hin** (Du brauchst: Fischotter-Material · Heft · Bleistift)
  - Pflicht: Betrachte das Foto. Notiere im Heft zwei sichtbare Körperteile. Ergänze zu jedem ein genaues Merkmal. | Bilde daraus zwei vollständige Sätze. | Zeige einem anderen Kind oder der Lehrkraft beide Bildstellen. Prüfe: Passen deine Sätze zum Foto?
  - Pflicht – Sprachdetektiv: Markiere in einem deiner Sätze ein Adjektiv mit **Adj**. Schreibe das Nomen dazu, das es genauer beschreibt.
  - Freiwillige Vertiefung: Beschreibe zwei sichtbare Merkmale noch genauer. Prüfe am Foto: Was kannst du sicher sagen? Erfinde keine verdeckten Teile.
  - Achte darauf: Eine Farbe, Form oder Größe macht die Angabe genauer: nicht nur „Ohren“, sondern „kleine Ohren“.
  - Kiosk-Tipp: Schau auf Kopf und Gesicht. Was siehst du an der Schnauze? Wie groß sind die Ohren?
  - Kiosk-Lösung (Lösung und Vergleich): Aufgabe 1 – Beispiele: / Schnauze: lange Tasthaare / Ohren: klein / Kopf: breit und flach /  / Aufgabe 2 – Beispiele: / „An der Schnauze sitzen lange Tasthaare.“ / „Die Ohren sind klein.“ /  / Aufgabe 3: Zeige beide Stellen auf dem Foto. Andere sichtbare Merkmale sind auch richtig. /  / Sprachdetektiv – Beispiel: „lange“ (Adj) beschreibt das Nomen „Tasthaare“.
  - Kiosk-Vertiefung: Beispiel: „An der Schnauze sitzen viele lange Tasthaare. Sie stehen zur Seite ab.“ / Sicher sagen kannst du nur, was du siehst. Schwimmhäute und die ganze Körperlänge erkennst du auf dem Foto nicht.
- **Blatt 3 · Bild oder Text?** (Du brauchst: Fischotter-Material · Merkblatt 1 · Heft · Bleistift)
  - Pflicht: Lies den Text mit den Leseschritten von Merkblatt 1. Notiere: / a) Wo lebt der Fischotter? / b) Was frisst er vor allem? / c) Wie lang sind Kopf und Rumpf? Nenne die Einheit. Zählt der Schwanz mit? | Markiere die Textstellen im Material: **L** für Lebensraum, **N** für Nahrung, **M** für Maß. Schreibe „Text“ hinter deine Antworten. | Partnercheck: Zeige einem anderen Kind deine Textstellen. Erkläre, was du gefunden hast. Passt die Stelle zur Frage? Prüft Unterschiede gemeinsam im Text. | Notiere ein sichtbares Merkmal mit „Bild“. Zeige die Bildstelle. Steht es auch im Text?
  - Pflicht – Sprachdetektiv: Unterstreiche auf deiner Fischotter-Materialseite zwei Verben. Schreibe **V** darüber.
  - Freiwillige Vertiefung: *„Der Fischotter auf dem Foto ist genau 80 cm lang.“* Kannst du das belegen? Begründe mit dem Material.
  - Kiosk-Tipp: Nutze die Leseschritte. Suche im Text die Wörter „lebt“, „frisst“ und „Zentimeter“. Lies auch den Satz danach.
  - Kiosk-Lösung (Lösung und Vergleich): Aufgabe 1: / a) an Flüssen und Seen mit geschützten Ufern (Text) / b) vor allem Fische (Text) / c) etwa 60 bis 90 Zentimeter. Der Schwanz zählt nicht mit. (Text) /  / Aufgabe 2: L steht bei „lebt an Flüssen und Seen mit geschützten Ufern“. N steht bei „frisst vor allem Fische“. M steht bei „etwa 60 bis 90 Zentimeter“. /  / Aufgabe 3: Habt ihr verschiedene Stellen markiert? Lest die Frage noch einmal und prüft gemeinsam im Text. /  / Aufgabe 4 – Beispiel: „kleine Ohren (Bild)“. Kleine Ohren stehen nicht im Text. / Auch richtig: „lange Tasthaare (Bild)“. Das steht auch im Text. /  / Sprachdetektiv – Verben im Text, zum Beispiel: lebt, hat, ist, sitzen, sind, kommt, frisst.
  - Kiosk-Vertiefung: Nein, das kannst du nicht belegen. Im Text steht nur: Kopf und Rumpf sind etwa 60 bis 90 Zentimeter lang. Wie lang genau dieser Fischotter ist, zeigt das Foto nicht. Der Schwanz kommt noch dazu.
- **Blatt 4 · Informationen ordnen** (Du brauchst: Fischotter-Material · Heft)
  - Pflicht: Schreibe ins Heft: Überblick · Aussehen · Lebensraum · Nahrung. | Ordne diese Angaben zu: / *Fischotter · kurze Beine · Fische · Flüsse und Seen · Kopf und Rumpf: 60–90 cm · dunkelbraune Oberseite · Frösche und Krebse · geschützte Ufer* | Ergänze den Hinweis zum Schwanz und zwei weitere äußere Merkmale aus dem Text. Hast du vier verschiedene Merkmale?
  - Pflicht – Sprachdetektiv: Zerlege „Körperlänge“ im Heft in zwei Nomen. Schreibe beide mit Artikel auf. Ergänze den Artikel zu „Körperlänge“.
  - Freiwillige Vertiefung: Ordne deine Angaben zum Aussehen in einer anderen sinnvollen Reihenfolge. Erkläre deine Wahl.
  - Kiosk-Tipp: Frage bei jeder Angabe: Geht es um das Aussehen, den Wohnort oder das Futter? Tiername und Maß gehören zum Überblick.
  - Kiosk-Lösung (Lösung und Vergleich): Aufgabe 2: / Überblick: Fischotter; Kopf und Rumpf: 60–90 cm / Aussehen: kurze Beine; dunkelbraune Oberseite / Lebensraum: Flüsse und Seen; geschützte Ufer / Nahrung: Fische; Frösche und Krebse /  / Aufgabe 3: / Überblick: Der Schwanz kommt noch dazu. / Aussehen, zum Beispiel: lang gestreckter Körper; breiter, flacher Kopf; lange Tasthaare. / Dann hast du mindestens vier verschiedene Merkmale. /  / Sprachdetektiv: der Körper + die Länge = die Körperlänge
  - Kiosk-Vertiefung: Zum Beispiel von oben nach unten: Kopf, Körper, Beine, Fell. Oder vom großen zum kleinen Merkmal. / Erkläre, warum deine Reihenfolge beim Vorstellen hilft. Mehrere Reihenfolgen sind richtig.

**Gelingensnachweis 1 „Tierdetektiv“ (Varianten A, B)** – 4 von 5 Indikatoren:

| ID | Kind-Formulierung | erreicht, wenn | Übe mit |
|---|---|---|---|
| E1.1 | Ich nenne zwei verschiedene äußere Merkmale genau. | zwei verschiedene äußere Merkmale richtig und genau benannt | Blatt 2 |
| E1.2 | Ich zeige, was ich im Bild und was ich im Text gefunden habe. | ein Bildbeleg und ein Textbeleg richtig zugeordnet und gezeigt | Blatt 3 |
| E1.3 | Ich gebe die Länge von Kopf und Rumpf mit Einheit an. | Kopf-Rumpf-Länge mit Einheit und ohne mitgerechneten Schwanz richtig angegeben | Blatt 3 |
| E1.4 | Ich finde Lebensraum und Nahrung im Text. | Lebensraum und Nahrung dem Text richtig entnommen | Blatt 3 |
| E1.5 | Ich ordne Angaben unter passende Überschriften. | Angaben unter passenden Überschriften | Blatt 4 |

Aufgaben: 1) Merkmale und Quellen: Notiere zwei verschiedene genaue äußere Merkmale: eines aus dem Bild, ein anderes aus dem Text. Kreise auf dem Foto die Bildstelle ein. Unterstreiche im Text die Textstelle. · 2) Das Maß: Notiere die Länge von Kopf und Rumpf mit Einheit. Kreuze an, ob der Schwanz mitgezählt wird. · 3) Informationen ordnen: Notiere unter jeder Überschrift eine richtige Angabe aus dem Text.

- Variante A Materialtext: Der Fischotter hat einen lang gestreckten Körper und kurze Beine. Sein Fell ist oben dunkelbraun. Er lebt an Flüssen und Seen. Er frisst vor allem Fische, aber auch Frösche und Krebse. Kopf und Rumpf sind zusammen 60 bis 90 Zentimeter lang. Der Schwanz kommt noch dazu.

- Variante B Materialtext: An Flüssen und Seen lebt der Fischotter. Zu seiner Nahrung gehören Fische, Frösche und Krebse. Sein Kopf ist breit und flach. Seine Beine sind kurz. Kopf und Rumpf messen zusammen 60 bis 90 Zentimeter. Der Schwanz wird dabei nicht mitgemessen.

### Etappe 2 · Sachlich und genau formulieren

**Ziel (Kind):** Ich kann genaue Wörter nutzen und verständliche Sätze im Präsens schreiben.

**Input und Merkblatt 2 – Abschnitte (identisch):**

1. **Genau statt wertend**
   - _Sachlich beschreiben:_ Beschreibe überprüfbare Merkmale. „schön“ und „süß“ sagen nur, wie jemand etwas findet. Nutze Angaben aus deinem Material.
   - _Genaue Wörter wählen:_ Nutze genaue Nomen, Verben und Adjektive. / *„Das Tier bewegt sich im Wasser.“* wird genauer: *„Der Fischotter schwimmt im Wasser.“* / *„Sein Fell ist oben dunkelbraun.“* ist ebenfalls genau. Du musst „ist“ nicht immer ersetzen.
   - _Wörter zusammensetzen:_ Aus *Fell* und *Farbe* wird die *Fellfarbe*. Das letzte Wort bestimmt den Artikel: *die Farbe → die Fellfarbe*. **Fachwörter** benennen etwas genau. Kläre ihre Bedeutung.
   - _Die Wörterhilfe:_ Auf der Wörterhilfe findest du genaue Wörter für Körperteile. Wähle nur Wörter, die zu deinem Tier passen. Prüfe die Angabe am Bild oder im Text.
   - _Frage:_ Was ist genauer: „schönes Fell“ oder „oben dunkelbraunes Fell“?
   - _Gesicherte Antwort:_ „oben dunkelbraunes Fell“. Die Farbe ist überprüfbar.
2. **Fische genau beschreiben**
   - _Ungenau:_ *„Der Fisch ist hübsch.“* Welcher Fisch ist gemeint? Das weiß niemand.
   - _Genau:_ *„Der Fisch hat einen kleinen Körper und eine sehr große Schwanzflosse.“* Das ist Fisch D.
   - _Rätsel mit einem Partner:_ Beschreibe einen Fisch mit zwei genauen Merkmalen. Verrate nicht, welchen du meinst. Dein Partner zeigt auf den passenden Fisch.
   - _Frage:_ Verbessere: „Der Fisch sieht cool aus.“ Nenne ein genaues Merkmal, damit man den Fisch erkennt.
   - _Gesicherte Antwort:_ Zum Beispiel: *„Der Fisch hat lange Flossen oben und unten.“* Das ist Fisch C. Andere genaue Merkmale sind auch richtig.
3. **Im Präsens beschreiben**
   - _Warum Präsens?:_ Tierbeschreibungen sagen, was allgemein für ein Tier gilt. Deshalb stehen sie meistens im **Präsens**, der Gegenwart: *Der Fischotter lebt an Gewässern.*
   - _Grundform und gebeugte Form:_ Im Wörterbuch steht die **Grundform**: *leben, fressen, sein*. / Im Satz beugst du das Verb passend: / *leben → er lebt* / *fressen → er frisst* / *sein → sein Fell ist dicht.*
   - _Subjekt und Verb:_ Das **Subjekt** ist der Satzgegenstand. Frage: Wer oder was schwimmt? / *Der Otter schwimmt. Die Otter schwimmen.*
   - _Frage:_ Was ändert sich?
   - _Gesicherte Antwort:_ Bei mehreren Ottern heißt das Verb „schwimmen“ statt „schwimmt“.
4. **Vollständige Sätze**
   - _Ein vollständiger Satz:_ Verbinde die Angaben zu einem verständlichen Satz. Achte darauf, dass Subjekt und Verb zusammenpassen: *Der Fischotter lebt. Die Fischotter leben.*
   - _Beispiel:_ Wortgruppe: *sein Fell – oben dunkelbraun – sein* / Satz: *Sein Fell ist oben dunkelbraun.* / Der Satz ist vollständig und verständlich.
   - _Frage:_ Was fehlt bei „Der Fischotter an einem See“?
   - _Gesicherte Antwort:_ Das Verb. Vollständig heißt es: *Der Fischotter lebt an einem See.*
5. **Sätze prüfen**
   - _Prüfe jeden Satz:_ Passt die Aussage zum Material? / Ist der Satz vollständig? / Steht das Verb im Präsens und passt es? / Sind die Wörter genau? / Beginnen Satz und Nomen groß? / Steht am Ende ein Punkt?
   - _Beispiel verbessern:_ *„sein fell war schön“* wird zu: *„Sein Fell ist oben dunkelbraun.“* Die Angabe stammt aus dem Material.

**Abschlusssatz:** Bearbeite die Pflichtaufgaben auf Blatt 5 und 6. Vertiefungen sind freiwillig. Im Gelingensnachweis bildest du drei Sätze und verbesserst einen Satz. Fünf Ziele: Materialtreue, vollständige Sätze, passende Verben im Präsens, genaue statt wertende Wörter, Großschreibung und Punkte. Bei vier von fünf Zielen gehst du weiter zu Etappe 3.

**Pflichtblätter:**

- **Blatt 5 · Treffende Wörter** (Du brauchst: Heft · Merkblatt 2 · Wörterhilfe)
  - Material und Wörterhilfe: Fell oben: dunkelbraun. Kopf: breit und flach. Im Wasser schwimmt der Fischotter. / **Tasthaare:** Haare zum Ertasten. / **Schwimmhäute:** Haut zwischen den Zehen.
  - Pflicht – Schreibe ins Heft: Ersetze „schönes Fell“ und „toller Kopf“ durch genaue Angaben aus dem Material. | Bilde Wörter mit Artikel: *Tast + Haare*; *Schwimm + Häute*. Erkläre beide mit der Wörterhilfe. | Verbessere mit dem Material: *„Das Tier bewegt sich im Wasser.“* Nenne das Tier genau. Nutze ein treffendes Verb.
  - Freiwillige Vertiefung – Vertiefung: Schau dir das Aquarium auf Merkblatt 2 an. Verbessere: *„Der Fisch ist lustig.“* Nenne ein genaues Merkmal, damit man den Fisch erkennt. Schreibe einen ganzen Satz im Präsens.
  - Kiosk-Tipp: Lies das Material oben auf dem Blatt. Wie ist das Fell oben? Wie ist der Kopf? Was macht der Fischotter im Wasser?
  - Kiosk-Lösung (Lösung und Vergleich): Aufgabe 1: „oben dunkelbraunes Fell“ und „breiter, flacher Kopf“ /  / Aufgabe 2: / die Tasthaare: Haare zum Ertasten / die Schwimmhäute: Haut zwischen den Zehen /  / Aufgabe 3: „Der Fischotter schwimmt im Wasser.“
  - Kiosk-Vertiefung: Zum Beispiel: „Der Fisch hat einen runden Körper mit dunklen Streifen.“ Das ist Fisch A. / Oder: „Der Fisch hat einen langen, schmalen Körper mit dunklen Punkten.“ Das ist Fisch B. / Wichtig: Das Merkmal passt nur zu einem Fisch.
- **Blatt 6 · Sachliche Sätze** (Du brauchst: Heft · Merkblatt 2)
  - Pflicht – Drei neue Sätze: Schreibe im Heft je einen vollständigen Satz im Präsens: *seine Beine – kurz – sein* | *der Fischotter – auch Krebse – fressen* | *an der Schnauze – lange Tasthaare – sitzen*
  - Pflicht – Verbessern und prüfen: Verbessere: *„der fischotter lebte an schönen ufern“*. / Material: *Er lebt an geschützten Ufern.* Prüfe alle vier Sätze mit Merkblatt 2. Achte auch auf große Satzanfänge und Nomen sowie Punkte.
  - Pflicht – Verben untersuchen: Unterstreiche im Heft die Verben in deinen vier Sätzen. Schreibe zu „frisst“ die Grundform. | Schreibe Satz 2 noch einmal für mehrere Fischotter. Passe das Verb an.
  - Freiwillige Vertiefung – Vertiefung: Verbinde zwei deiner Sätze mit „und“. Erkläre, warum das Präsens zu einer Tierbeschreibung passt.
  - Kiosk-Tipp: Stelle die Wortgruppen so um, dass ein ganzer Satz entsteht. Das Verb passt zum Subjekt: er frisst, die Beine sind.
  - Kiosk-Lösung (Lösung und Vergleich): 1. Seine Beine sind kurz. / 2. Der Fischotter frisst auch Krebse. / 3. An der Schnauze sitzen lange Tasthaare. / 4. Der Fischotter lebt an geschützten Ufern. /  / 5. Verben: sind, frisst, sitzen, lebt. Grundform von „frisst“: fressen. / 6. Die Fischotter fressen auch Krebse. /  / Andere Reihenfolgen im Satz sind richtig, wenn der Satz vollständig ist.
  - Kiosk-Vertiefung: Beispiel: „Der Fischotter lebt an geschützten Ufern und frisst auch Krebse.“ / Das Präsens passt, weil die Beschreibung sagt, was allgemein für den Fischotter gilt.
- **Hilfekarte Wörterhilfe · Genaue Wörter für dein Tier** – Hinweis: Wähle nur Wörter, die zu deinem Tier passen. Prüfe die Angabe am Bild oder im Text. Tabelle: der Kopf: breit, schmal, flach, rund; die Schnauze: lang, kurz, spitz, breit; die Ohren: klein, groß, rund, spitz; das Fell: dicht, glatt, dunkelbraun, graubraun, gestreift, gefleckt; der Körper: lang gestreckt, schlank, kräftig; der Schwanz: lang, kurz, buschig, schmal, geringelt; die Beine / die Pfoten: kurz, lang, kräftig. Fachwörter: die Tasthaare: Haare zum Ertasten / die Schwimmhäute: Haut zwischen den Zehen / die Krallen: spitze Nägel an den Zehen / der Rumpf: Körper ohne Kopf, Beine und Schwanz. Genaue Verben: er lebt · er frisst · er schwimmt · er klettert · er gräbt · er hat · er ist.

**Gelingensnachweis 2 „Genaue Sätze“ (Varianten A, B)** – 4 von 5 Indikatoren:

| ID | Kind-Formulierung | erreicht, wenn | Übe mit |
|---|---|---|---|
| E2.1 | Meine Sätze passen zu den Angaben im Material. | alle vier Aussagen passen zu den vorgegebenen Tierinformationen | Blatt 5 |
| E2.2 | Ich schreibe vollständige, verständliche Sätze. | alle vier Aussagen als vollständige, verständliche Sätze formuliert | Blatt 6 |
| E2.3 | Meine Verben stehen im Präsens und passen zum Subjekt. | Verben im Präsens und passend zum Subjekt | Blatt 6 |
| E2.4 | Ich ersetze eine Wertung durch eine genaue Angabe. | die Wertung ist durch eine genaue passende Angabe ersetzt | Blatt 5 |
| E2.5 | Ich schreibe Satzanfänge und Nomen groß und setze Punkte. | Satzanfänge und Nomen groß sowie Satzschlusspunkte in den vier Sätzen | Blatt 6 |

Aufgaben: 1) Drei Sätze: Die Wortgruppen enthalten richtige Angaben. Schreibe daraus drei vollständige Sätze im Präsens. · 2) Einen Satz verbessern: Verbessere den Satz. Nutze die Angabe aus dem Material.

- Variante A: Wortgruppen der Fischotter – an Flüssen und Seen – leben | sein Kopf – breit und flach – sein | er – vor allem Fische – fressen; verbessern „der fischotter hatte schöne beine“ (Material: Seine Beine sind kurz.)

- Variante B: Wortgruppen der Fischotter – auch an Seen – leben | sein Körper – lang gestreckt – sein | er – auch Frösche – fressen; verbessern „der fischotter hatte einen tollen schwanz“ (Material: Sein Schwanz ist kräftig.)

### Etappe 3 · Eine Tierbeschreibung schreiben und prüfen

**Ziel (Kind):** Ich kann ein Tier mit Material sachlich, geordnet und verständlich beschreiben.

**Input und Merkblatt 3 – Abschnitte (identisch):**

1. **Vom Material zum Plan**
   - _Dein Ziel:_ Ich kann ein Tier mit Material sachlich, geordnet und verständlich beschreiben.
   - _Ein Plan in Stichwörtern:_ **Überblick:** Fischotter; Kopf und Rumpf etwa 60–90 cm, Schwanz zusätzlich / **Aussehen:** lang gestreckter Körper; kurze Beine; oben dunkelbraunes Fell; breiter, flacher Kopf / **Lebensraum:** Flüsse und Seen mit geschützten Ufern / **Nahrung:** vor allem Fische, auch Frösche und Krebse
   - _Frage:_ Was fehlt bei „60–90“?
   - _Gesicherte Antwort:_ Einheit und Bezug. Richtig: Kopf und Rumpf etwa 60–90 cm, ohne Schwanz. Prüfe alle Angaben am Material.
2. **Aus Stichwörtern wird Text**
   - _Vom Plan zum Satz:_ Stichwörter: *Kopf – breit, flach* / Satz: *Sein Kopf ist breit und flach.* / Nutze vollständige Sätze im Präsens. Schreibe sachlich und verbinde zusammengehörige Angaben.
   - _Ein vollständiges Beispiel:_ **Der Fischotter** / *Der Fischotter hat einen lang gestreckten Körper. Kopf und Rumpf sind zusammen etwa 60 bis 90 Zentimeter lang. Der Schwanz kommt noch dazu. Seine Beine sind kurz. Sein Fell ist oben dunkelbraun. Der Kopf ist breit und flach.* / *Er lebt an Flüssen und Seen mit geschützten Ufern. Er frisst vor allem Fische, aber auch Frösche und Krebse.*
3. **Mit Kriterien prüfen**
   - _K1 · Informationen:_ Tiername, Maß mit Einheit und Bezug, Lebensraum und Nahrung sind richtig im Text enthalten.
   - _K2 · Aussehen:_ Mindestens vier verschiedene äußere Merkmale sind genau beschrieben. Wiederholungen desselben Merkmals zählen nicht doppelt.
   - _K3 · Aufbau:_ Beginne mit Tiername und Überblick, etwa Körperform oder Maß. Ordne zusammengehörige Informationen. Absätze helfen.
   - _K4 und K5 · Sprache:_ Schreibe sachlich und im Präsens. Nutze genaue Wörter. Verbinde vollständige, verständliche Sätze zu einem Text. Eine Stichwortliste reicht nicht.
4. **Prüfen und überarbeiten**
   - _K6 · Schreibung:_ Prüfe Satzanfänge, Nomen und Satzschlüsse. Vergleiche schwierige Tierwörter mit dem Material. / **Zeige deine Prüfung:** Kreise einen Satzanfang ein, unterstreiche zwei Nomen und markiere einen Satzschlusspunkt.
   - _Ein Beispiel prüfen:_ *„sein kopf ist breit und flach“* wird zu: *„Sein Kopf ist breit und flach.“* / Groß: *Sein, Kopf*. Am Ende steht ein Punkt.
   - _Frage:_ Muss ein richtiger Satz verändert werden?
   - _Gesicherte Antwort:_ Nein. Zeige die Prüfung und begründe: „Mein Satz bleibt, weil …“

**Abschlusssatz:** Bearbeite die Pflichtaufgaben auf Blatt 7–9. Vertiefungen sind freiwillig. Dein Abschluss ist die Probearbeit, dein letzter Gelingensnachweis. Fünf Ziele: Informationen, vier Merkmale, Aufbau, Sprache, Schreibung mit sichtbarer Prüfung. Vier von fünf = 80 %. Danach bekommst du Feedback für deinen nächsten Schritt.

**Materialseite „Das Erdmännchen“** (Foto: Foto: Bernard DUPONT · CC BY-SA 2.0 · Wikimedia Commons · Graustufenfassung):
> Das Erdmännchen lebt im trockenen Gras- und Buschland im südlichen Afrika. Es gehört zu den Mangusten. Die Tiere leben in Gruppen und nutzen unterirdische Baue. Ein Erdmännchen hat einen schlanken Körper. Sein Fell ist hellbraun bis graubraun; auf dem Rücken liegen dunklere Streifen. Um die Augen sind dunkle Flecken zu erkennen. Kopf und Rumpf sind zusammen etwa 25 bis 29 Zentimeter lang; der Schwanz kommt noch dazu. Der Schwanz ist lang und schmal. An den Pfoten sitzen lange Krallen, die beim Graben helfen. Es frisst vor allem Insekten, aber auch Spinnen und kleine Eidechsen.

Wörterhilfe: Mangusten = eine Familie von Raubtieren; Rumpf = Körper ohne Kopf, Beine und Schwanz; Bau = unterirdisches Versteck mit Gängen

**Materialseite „Der Rote Panda“** (Foto: Foto: Brunswyk · CC BY-SA 3.0 · Wikimedia Commons · Graustufenfassung):
> Der Rote Panda wird auch Kleiner Panda genannt. Er lebt in Bergwäldern Asiens, in denen Bambus wächst. Sein Fell ist am Rücken rötlich braun. Beine und Bauch sind dunkel bis schwarz. Im Gesicht hat er helle, fast weiße Bereiche. Kopf und Rumpf sind zusammen etwa 60 Zentimeter lang; der Schwanz kommt noch dazu. Sein langer, buschiger Schwanz hat hellere und dunklere Ringe. Beim Klettern helfen ihm Krallen und der Schwanz. Er frisst hauptsächlich Bambus, daneben zum Beispiel Beeren und Eier. Der Rote Panda ist besonders in der Dämmerung und nachts aktiv.

Wörterhilfe: Rumpf = Körper ohne Kopf, Beine und Schwanz; Bambus = eine Pflanze mit festen Halmen; Dämmerung = Zeit zwischen Tageslicht und Dunkelheit

**Pflichtblätter:**

- **Blatt 7 · Dein Schreibplan** (Du brauchst: Merkblatt 3 · Material zum Erdmännchen oder Roten Panda · Heft. Wähle ein Tier. Bleibe auf Blatt 7–9 bei diesem Tier.)
  - Pflicht – Plane im Heft: Lies das Material und betrachte das Foto. | Schreibe diese Überschriften: Überblick · Aussehen · Lebensraum · Nahrung. | Ordne Stichwörter zu: Tiername, ein Maß mit Einheit und Bezug, vier verschiedene äußere Merkmale, Lebensraum und Nahrung. | Prüfe deine Angaben. Zeige eine passende Bildstelle und eine Textstelle.
  - Freiwillige Vertiefung – Vertiefung: Skizziere eine zweite sinnvolle Reihenfolge. Welche hilft dir besser beim Schreiben? Begründe kurz.
  - Kiosk-Tipp: Lies dein Tiermaterial Satz für Satz. Markiere zuerst den Tiernamen und das Maß. Suche dann vier Angaben zum Aussehen.
  - Kiosk-Lösung (Vergleichsplan): Erdmännchen / Überblick: Erdmännchen; Kopf und Rumpf etwa 25–29 cm, Schwanz zusätzlich / Aussehen: schlanker Körper; hellbraunes bis graubraunes Fell; dunkle Streifen auf dem Rücken; dunkle Flecken um die Augen; langer, schmaler Schwanz; lange Krallen / Lebensraum: trockenes Gras- und Buschland im südlichen Afrika / Nahrung: vor allem Insekten, auch Spinnen und kleine Eidechsen /  / Roter Panda / Überblick: Roter Panda; Kopf und Rumpf etwa 60 cm, Schwanz zusätzlich / Aussehen: Fell am Rücken rötlich braun; Beine und Bauch dunkel; helle Bereiche im Gesicht; langer, buschiger Schwanz mit Ringen / Lebensraum: Bergwälder Asiens mit Bambus / Nahrung: hauptsächlich Bambus, auch Beeren und Eier /  / Du brauchst nur vier Merkmale. Andere Stichwörter sind richtig, wenn sie zum Material passen.
  - Kiosk-Vertiefung: Zum Beispiel: erst Lebensraum und Nahrung, dann das Aussehen. Oder das Aussehen von oben nach unten. / Wichtig: Tiername und Überblick stehen am Anfang.
- **Blatt 8 · Deine Tierbeschreibung** (Du brauchst: deinen Plan von Blatt 7 · das gewählte Tiermaterial · Merkblatt 3 · Heft)
  - Pflicht – Schreibe im Heft: Schreibe eine passende Überschrift. | Schreibe aus deinem Plan einen zusammenhängenden Text. Beginne mit Tiername und Überblick. | Beschreibe vier verschiedene äußere Merkmale. Ergänze Maß mit Einheit und Bezug, Lebensraum und Nahrung. | Schreibe sachlich, im Präsens und in vollständigen Sätzen. Lies deinen Text einmal leise vor.
  - Freiwillige Vertiefung – Vertiefung: Verbessere zwei Satzanfänge oder Bezüge. Zeige: Welches Wort macht jetzt klarer, was gemeint ist?
  - Kiosk-Tipp: Mache aus jeder Zeile deines Plans einen ganzen Satz. Beginne mit „Das Erdmännchen …“ oder „Der Rote Panda …“.
  - Kiosk-Lösung (Prüffragen und Teilbeispiele): Hier gibt es keine feste Lösung. Prüfe deinen Text: / Überschrift vorhanden? / Tiername und Überblick am Anfang? / Maß mit Einheit und Bezug? / Vier verschiedene äußere Merkmale? / Lebensraum und Nahrung? / Präsens und ganze Sätze? /  / Teilbeispiel Erdmännchen: „Das Erdmännchen hat einen schlanken Körper. Kopf und Rumpf sind zusammen etwa 25 bis 29 Zentimeter lang. Der Schwanz kommt noch dazu.“ /  / Teilbeispiel Roter Panda: „Der Rote Panda lebt in Bergwäldern Asiens. Dort wächst Bambus.“
  - Kiosk-Vertiefung: Unklar: „Es ist lang und schmal.“ Was ist gemeint? / Klarer: „Der Schwanz ist lang und schmal.“ / Wenn „er“, „es“ oder „sein“ unklar ist, nenne das Nomen.
- **Blatt 9 · Prüfen und verbessern** (Du brauchst: deinen Text von Blatt 8 · das Tiermaterial · Checkliste K1–K6 · Rückmeldekarte)
  - Pflicht – Arbeite am Text: Prüfe deinen Text im Heft mit K1–K6. | Geh zur Haltestelle. Such dir ein Kind für eine Rückmeldung. Es liest deinen Text und nutzt die Rückmeldekarte. Lass dir die Textstelle zeigen. | Entscheide mit Material und Checkliste, was du verbesserst. Schreibe nicht den ganzen Text neu. Ist eine Stelle schon richtig? Begründe, warum sie bleibt. | Zeige die Schreibprüfung: Kreise einen Satzanfang ein, unterstreiche zwei Nomen und markiere einen Punkt. Vergleiche Tierwörter mit dem Material.
  - Freiwillige Vertiefung – Vertiefung: Zeige eine Stelle vorher und nachher. Erkläre, was durch deine Änderung besser geworden ist.
  - Kiosk-Tipp: An der Haltestelle hilft dir die Rückmeldekarte. Prüfe danach ein Kriterium nach dem anderen. Lies für K6 jeden Satz einzeln: Beginnt er groß? Steht am Ende ein Punkt?
  - Kiosk-Lösung (Prüffragen): Deine Verbesserungen hängen von deinem Text ab. Die Rückmeldung an der Haltestelle ist ein Hinweis. Du entscheidest mit Material und Checkliste, was du änderst. /  / So prüfst du: / K1: Stimmen Tiername, Maß mit Einheit und Bezug, Lebensraum und Nahrung mit dem Material überein? / K2: Zähle vier verschiedene Merkmale. Dasselbe Merkmal zählt nur einmal. / K3: Steht der Überblick am Anfang? Stehen zusammengehörige Angaben zusammen? / K4 und K5: Präsens, sachlich, ganze Sätze? / K6: Satzanfang eingekreist, zwei Nomen unterstrichen, Punkt markiert? /  / Ein richtiger Satz bleibt. Begründe: „Mein Satz bleibt, weil …“
  - Kiosk-Vertiefung: Beispiel vorher: „der schwanz ist toll“ / Nachher: „Der Schwanz ist lang und schmal.“ / Besser, weil der Satz groß beginnt, das Nomen groß ist und ein genaues Merkmal statt einer Wertung steht.
- **Checkliste · Inhalt und Aufbau:** K1 · Informationen: Hast du das Tier benannt? Stimmen Maß, Einheit und Bezug? Stehen Lebensraum und Nahrung im Text? Vergleiche alles mit dem Material. · K2 · Aussehen: Findest du vier verschiedene genaue äußere Merkmale? Zeige sie. „schön“ ist kein genaues Merkmal. · K3 · Aufbau: Stehen Tiername und Überblick am Anfang? Sind zusammengehörige Informationen zusammen?
- **Checkliste · Sprache und Schreibung:** K4 · Sachlich schreiben: Stehen deine Verben im Präsens? Beschreibst du genau und ohne persönliche Wertungen? · K5 · Verständliche Sätze: Sind deine Sätze vollständig und verständlich? Ist klar, auf wen sich „er“, „es“ und „sein“ beziehen? · K6 · Schreibung prüfen: Prüfe große Satzanfänge und Nomen sowie Satzschlusspunkte. Vergleiche schwierige Wörter mit dem Material. Kreise einen Satzanfang ein, unterstreiche zwei Nomen und markiere einen Punkt als Prüfbeleg.
- **Hilfekarte Rückmeldekarte · Rückmeldung an der Haltestelle** – Hinweis: Du gibst einem anderen Kind eine Rückmeldung zu seinem Text. Lies den Text ruhig. Wähle zwei oder drei Fragen. So geht es: 1. Das Kind hat seinen Text schon selbst geprüft. / 2. Du liest den Text. / 3. Du prüfst mit zwei oder drei Fragen. / 4. Das Kind entscheidet selbst, was es verbessert.. Fragen zum Prüfen: Kannst du dir das Aussehen des Tieres vorstellen? Zeige eine genaue Beschreibung. / Stehen zusammengehörige Informationen zusammen? / Welche Stelle sollte noch genauer oder verständlicher werden?. So sagst du es: *Diese Stelle ist genau: …* / *Hier habe ich eine Frage: …* / *Prüfe diese Angabe noch einmal im Material: …*.
- **Raumschild:** Haltestelle – Rückmeldung zum Text


## 9 · Probearbeit und Klassenarbeit ⚙

Gemeinsamer Aufbau (A4, 7 Seiten; Vorbild: Lernerfolgskontrolle der Reihe Wunschbriefe): 1 Auftrag (Situation, Auftrags-Checkliste, Arbeitszeit-Feld, bei KA Terminwahl) · 2 Material (Foto, Sachtext, Wörterhilfe, Bildhinweis) · 3 Planung (Schreibplan Überblick/Aussehen ×4/Lebensraum/Nahrung) · 4 Schreibseite (Überschrift + Linien, Prüfhinweis) · 5 „Dein Text: Das zählt“ (K1–K6 zum Abhaken) · 6 Hilfeseite (erlaubt) · 7 Lehrkraftseite (Probearbeit: Rückmeldung E3.1–E3.5, Hilfen, x/5, nächster Schritt, Wahlzeit, Klassenarbeitstermin; Klassenarbeit: Bewertung K1–K6 mit Punkten und Note).

### Deine Probearbeit: Der Waschbär (Probearbeit) · `inhalt/probearbeit_waschbaer.json`

- Situation: Unsere Klasse gestaltet ein Tierlexikon. Es fehlt noch ein Text über den Waschbären. Schreibe diesen Lexikontext. Andere sollen sich das Tier danach gut vorstellen können.
- Sachtext: Der Waschbär stammt ursprünglich aus Nordamerika. Er lebt gern in Wäldern mit Gewässern, kommt aber auch in Städten vor. Sein Körper ist kräftig und wirkt gedrungen. Das Fell ist meist graubraun. Um seine Augen liegt eine schwarze Zeichnung, die wie eine Maske aussieht. Der buschige Schwanz hat mehrere dunkle Ringe. Ein erwachsener Waschbär wiegt häufig etwa sechs bis sieben Kilogramm. An jeder Pfote sitzen fünf Zehen. Mit den Vorderpfoten kann er Nahrung geschickt greifen. Er frisst pflanzliche und tierische Nahrung, zum Beispiel Früchte, Nüsse, Insekten und Frösche.
- Wörterhilfe: gedrungen = eher kurz und kräftig gebaut; Zeichnung = Muster auf dem Fell; Vorderpfoten = die beiden vorderen Pfoten
- Foto: Foto: BS Thurner Hof · CC BY-SA 3.0 · Wikimedia Commons · Graustufenfassung
- Indikatoren: E3.1 Informationen (K1) (erreicht, wenn Tiername, richtige Maßangabe mit Bezug, Lebensraum und Nahrung enthalten) · E3.2 Aussehen: vier Merkmale (K2) (erreicht, wenn mindestens vier verschiedene äußere Merkmale richtig beschrieben) · E3.3 Aufbau (K3) (erreicht, wenn Text beginnt mit Überblick und ordnet zusammengehörige Informationen nachvollziehbar) · E3.4 Sprache (K4, K5) (erreicht, wenn zusammenhängender, überwiegend sachlicher Text im Präsens aus überwiegend vollständigen, verständlichen Sätzen) · E3.5 Schreibung mit Prüfbeleg (K6) (erreicht, wenn Prüfung von Satzanfängen, Nomen und Satzschlüssen am Produkt belegt; geübte Schreibungen überwiegend richtig)

### Deine Klassenarbeit: Der Biber (Klassenarbeit) · `inhalt/klassenarbeit_biber.json`

- Situation: Unser Tiermagazin bekommt eine neue Seite. Es fehlt noch ein Text über den Europäischen Biber. Schreibe diesen Lexikontext. Andere sollen sich das Tier danach gut vorstellen können.
- Sachtext: Der Europäische Biber lebt an Flüssen und Seen. Er ist ein Nagetier und ernährt sich von Pflanzen. Er frisst zum Beispiel Blätter, junge Triebe und Rinde. Sein Körper ist kräftig und hat kurze Beine. Das dichte Fell ist braun. Am Kopf sitzen kleine Ohren und eine stumpfe Schnauze. Ein erwachsener Biber kann etwa 13 bis 35 Kilogramm wiegen. Sein breiter, flacher Schwanz ist kaum behaart und mit Schuppen bedeckt. Dieser Schwanz heißt auch Kelle. Zwischen den Zehen der Hinterfüße liegen Schwimmhäute. Die großen Schneidezähne sind auf der Vorderseite orange gefärbt.
- Wörterhilfe: Triebe = junge Teile einer Pflanze; Kelle = Name für den breiten Biberschwanz; Schneidezähne = die vorderen Zähne zum Abbeißen und Nagen
- Foto: Foto: Tomas Čekanavičius · CC BY-SA 3.0 · Wikimedia Commons · Graustufenfassung
- Bewertungserwartung: K1 Informationen: Tiername, Gewicht mit Einheit und Bezug, Lebensraum, Nahrung · K2 Aussehen: mindestens vier verschiedene äußere Merkmale richtig (z. B. kräftiger Körper, kurze Beine, dichtes braunes Fell, breiter flacher Schwanz) · K3 Aufbau: Überschrift, Überblick am Anfang, zusammengehörige Angaben gebündelt · K4 Sachlich: überwiegend sachlich, im Präsens, ohne Wertungen · K5 Verständlich: zusammenhängender Text aus überwiegend vollständigen, verständlichen Sätzen; klare Bezüge · K6 Schreibung: Prüfung sichtbar; Satzanfänge, Nomen, Satzschlüsse und geübte Tierwörter überwiegend richtig

### Deine Klassenarbeit: Das Breitmaulnashorn (Klassenarbeit) · `inhalt/klassenarbeit_breitmaulnashorn.json`

- Situation: Unser Tiermagazin bekommt eine neue Seite. Es fehlt noch ein Text über das Breitmaulnashorn. Schreibe diesen Lexikontext. Andere sollen sich das Tier danach gut vorstellen können.
- Sachtext: Das Breitmaulnashorn lebt in Afrika. Es lebt in Savannen mit kurzem Gras. Es frisst fast nur Gras. Mit seinen sehr breiten Lippen rupft es das Gras ab. Sein Körper ist groß und massig. Die Haut ist grau, dick und fast ohne Haare. Im Nacken hat es einen Buckel. Seine Beine sind kurz und kräftig. Auf der Nase trägt es zwei Hörner. Das vordere Horn ist länger als das hintere. Kopf und Rumpf sind zusammen etwa 3,40 bis 3,80 Meter lang. Der Schwanz kommt noch dazu. Ein erwachsenes Männchen kann bis zu 3600 Kilogramm wiegen.
- Wörterhilfe: Savanne = Grasland mit wenigen Bäumen; massig = sehr groß und schwer; Buckel = eine Erhöhung im Nacken
- Foto: Foto folgt
- Bewertungserwartung: K1 Informationen: Tiername, Maß mit Einheit und Bezug (z. B. Kopf und Rumpf 3,40–3,80 m, Schwanz zusätzlich), Lebensraum, Nahrung · K2 Aussehen: mindestens vier verschiedene äußere Merkmale richtig (z. B. graue, dicke Haut, zwei Hörner, breite Lippen, kurze, kräftige Beine, Buckel) · K3 Aufbau: Überschrift, Überblick am Anfang, zusammengehörige Angaben gebündelt · K4 Sachlich: überwiegend sachlich, im Präsens, ohne Wertungen · K5 Verständlich: zusammenhängender Text aus überwiegend vollständigen, verständlichen Sätzen; klare Bezüge · K6 Schreibung: Prüfung sichtbar; Satzanfänge, Nomen, Satzschlüsse und geübte Tierwörter überwiegend richtig


## 10 · Wahlphase, Strategiekarten, Kiosk, Lernweg ⚙

### Wahlphase (nach Feedback zur Probearbeit)

Du hast deine Probearbeit geschrieben und Feedback bekommen. Jetzt entscheidest du, woran du arbeitest. Hast du weniger als vier von fünf Zielen gezeigt? Dann übst du zuerst deine offenen Ziele und zeigst sie noch einmal. Deine Rückmeldung sagt dir, mit welchem Blatt du übst. Du musst nicht alle Projekte machen. Du kannst allein, zu zweit oder zu dritt arbeiten. Während einer Klassenarbeit arbeitest du still für dich.

- **P1 Unser Tiermagazin** – Du gestaltest eine Seite für das Tiermagazin unserer Klasse. Arbeite allein oder zu zweit. Schritte: Text auswählen und prüfen: Nimm deinen überarbeiteten Übungstext. Prüfe ihn noch einmal mit K1–K6. Verbessere nur nötige Stellen. Schreibe nicht alles neu. · Die Seite gestalten: Schreibe eine Überschrift mit dem Tiernamen. Übertrage deinen Text sauber. Zeichne das Tier und beschrifte vier äußere Merkmale. Schreibe unten: „Quelle: Tierpaket …“. · Die Seite abgeben: Lege deine Seite in die Magazin-Mappe. Zu zweit: Schreibt unten auf, wer was gemacht hat. Gelingt, wenn: Die Angaben passen zum Material.; Vier Merkmale sind beschriftet.; Text und Zeichnung passen zusammen.; Die Seite ist gut lesbar.. Erweiterung (freiwillig): **Kurzvortrag (1–2 Minuten):** Stelle dein Tier mit wenigen Stichwörtern vor. Nenne genaue Merkmale und eine interessante Information aus dem Material. Sprich so, dass andere dich verstehen. Eine Karteikarte oder dein Schreibplan hilft dir.
- **P2 Welches Tier ist gemeint?** – Du erstellst eine Rätselkarte und eine getrennte Lösungskarte. Arbeite allein, zu zweit oder zu dritt. Schritte: Hinweise schreiben: Wähle eines der drei Tiere. Schreibe vier genaue äußere Merkmale auf deine Rätselkarte. Nenne den Tiernamen noch nicht. Prüfe: Passen die Hinweise zusammen nur zu deinem Tier? · Lösung getrennt sichern: Schreibe den Tiernamen auf eine zweite Karte. Notiere zu jedem Hinweis den Beleg: eine Textstelle oder ein sichtbares Merkmal auf dem Foto. · Rätsel erproben: Lies einem Kind deine Hinweise vor. Es zeigt auf das passende Tier. Frage danach: „Was hat geholfen? Was war unklar?“ · Verbessern: Verbessere ungenaue Hinweise. Passt schon alles? Erkläre, warum die Hinweise eindeutig sind. Gelingt, wenn: Vier richtige Merkmale.; Verständliche Hinweise.; Unter den drei Tieren eindeutig.; Getrennte Lösung mit vier Belegen.. Erweiterung (freiwillig): Ordne deine Hinweise vom allgemeinen zum besonders kennzeichnenden Merkmal. Das letzte Merkmal verrät das Tier sicher.
- **P3 Zwei Tiere vergleichen** – Du erstellst eine Tabelle und schreibst drei Vergleichssätze. Arbeite allein, zu zweit oder zu dritt. Schritte: Merkmale auswählen: Wähle drei Körpermerkmale, zu denen beide Pakete Angaben enthalten. Vergleiche immer dasselbe Merkmal, zum Beispiel Fell oder Schwanz. · Tabelle anlegen: Zeichne im Heft eine Tabelle mit drei Spalten: Merkmal · Tier 1 · Tier 2. Trage zu jedem Merkmal die Angaben beider Tiere ein. · Sätze schreiben: Schreibe zu jeder Zeile einen Vergleichssatz. Zum Beispiel: „Beide Tiere haben …“ oder „Beim … ist …, beim … ist …“. · Prüfen: Prüfe alle Angaben in den Paketen. Markiere einen Vergleich, der beim Erkennen besonders hilft. Gelingt, wenn: Drei gleiche Merkmale verglichen.; Angaben zu beiden Tieren richtig.; Drei verständliche Vergleichssätze.. Erweiterung (freiwillig): Erkläre, warum dein Vergleich mehr hilft als eine Wertung wie „süß“.

### Strategiekarten (am Lernbuddy anlegen; Aufbau: Wann? · 4 Schritte · Beispiel · Hat es geholfen? ja/etwas/nein)

1. **Lesen mit Suchauftrag** – Wann: Du suchst Informationen in einem Sachtext. Schritte: Lies den Text einmal. Markiere unbekannte Wörter. · Kläre die Wörter: Satz noch einmal lesen, Wörterhilfe, fragen. · Lies mit Suchauftrag weiter. Markiere die Stelle. · Notiere ein Stichwort unter der Überschrift. Beispiel: Was frisst er? / Suchwort: *frisst* / → *vor allem Fische*
2. **Markieren mit Buchstaben** – Wann: Du suchst verschiedene Informationen im selben Text. Schritte: Lege fest, was du suchst. · Schreibe einen Buchstaben an die Stelle: / **A** Aussehen · **L** Lebensraum / **N** Nahrung · **M** Maß · Markiere nur die wichtigen Wörter, nicht den ganzen Satz. · Prüfe: Passt die Stelle zur Frage? Beispiel: *Er lebt an Flüssen und Seen.* → **L**
3. **Ordnen unter Überschriften** – Wann: Du sammelst Informationen für einen Plan. Schritte: Schreibe die Überschriften: Überblick · Aussehen · Lebensraum · Nahrung. · Frage bei jeder Angabe: Wohin gehört sie? · Schreibe sie als Stichwort darunter. · Zähle: Hast du vier Merkmale beim Aussehen? Beispiel: *breiter, flacher Kopf* → Aussehen / *Fische* → Nahrung
4. **Genau statt wertend** – Wann: Du beschreibst, wie ein Tier aussieht. Schritte: Lies dein Wort: Sagt es, wie jemand das Tier findet? · Frage: Kann ich es im Bild sehen oder im Text lesen? · Ersetze die Wertung durch Form, Farbe oder Größe. · Prüfe die neue Angabe am Material. Beispiel: nicht: *schönes Fell* / sondern: *oben dunkelbraunes Fell*
5. **Die Wörterhilfe nutzen** – Wann: Dir fehlt ein genaues Wort. Schritte: Suche den Körperteil in der Wörterhilfe. · Lies die möglichen Wörter. · Wähle nur ein Wort, das zu deinem Tier passt. · Prüfe es am Bild oder im Text. Beispiel: Schwanz: *lang, kurz, buschig, schmal* / Erdmännchen: *lang und schmal*
6. **Einen Satz bauen** – Wann: Du machst aus Stichwörtern einen Satz. Schritte: Wer oder was? Nenne das Subjekt. · Was tut es oder wie ist es? Setze das Verb im Präsens. · Ergänze die Angabe aus dem Plan. · Prüfe: Großer Anfang? Punkt am Ende? Beispiel: *Kopf – breit, flach* / → *Sein Kopf ist breit und flach.*
7. **Satzanfang, Nomen, Punkt** – Wann: Du prüfst die Schreibung deines Textes. Schritte: Lies Satz für Satz. Lege ein Lineal unter die Zeile. · Kreise den Satzanfang ein. Ist er groß? · Unterstreiche die Nomen. Sind sie groß? · Markiere das Satzende. Steht ein Punkt? Beispiel: *sein kopf ist flach* / → *Sein Kopf ist flach.*
8. **Rückmeldung geben** – Wann: Du liest den Text eines anderen Kindes an der Haltestelle. Schritte: Lies den ganzen Text ruhig. · Wähle zwei Fragen von der Rückmeldekarte. · Zeige die passende Textstelle. · Sage es freundlich und genau. Beispiel: *Diese Stelle ist genau: …* / *Prüfe diese Angabe im Material: …*
9. **Meine eigene Strategie** – leere Karte für eine eigene Strategie

### Kontroll-Kiosk

Nachbau des Wunschbrief-Kiosks: Startbildschirm „Tipp oder Lösung?“, Blattnummer 1–9 per Zahlenfeld/Tastatur, Ergebnis mit Wechsel Tipp↔Lösung, freiwillige Vertiefung aufklappbar; nach 3 Minuten Inaktivität bei der Nummerneingabe zurück zum Start; Esc = Start; Vollbild; offline; keine Kinderdaten. Direktaufruf `?mode=solution&blatt=7`. Nicht für Nachweise/Probearbeit/Klassenarbeit. Texte: `inhalt/kiosk.json` (Inhalte siehe Abschnitt 8 je Blatt).

### Lernweg (A4, je Kind)

Stationen je Etappe: Start (Input, Merkblatt) · Pflichtblätter zum Abhaken · Vertiefungen (freiwillig) · Nachweisfeld (x/5, Datum, Freigabe der Lehrkraft); Etappe 3: Probearbeit, Feedback erhalten. Danach Wahlzeit (offene Ziele, P1–P3, Vertiefung) und Klassenarbeit (früher/später Termin). F-Fassung mit Blatt 1F–9F ohne Vertiefungen.

### Ablauf-Animation

HTML-Animation (11 Szenen) für den Einstieg in DS 1: Wegekarte mit Spielstein „Du“; Input → Blätter auf dem Lernbuddy → Hilfen (Strategiekarte, Lösungsleiter, Kiosk) → Nachweis mit 5 Punkten und Schleife „noch üben“ → Etappe 2 → Etappe 3 mit Probearbeit → Feedback → Wahlzeit → Klassenarbeit → „Dein Tempo“.


## 11 · Repository, Quellen und Werkzeuge

```
inhalt/                 Einzige Inhaltsquellen (JSON) – hier ändern, nie in den Ausgaben
  etappe1|2|3.json        Input/Merkblatt, Material, Blätter, Nachweise, Hilfen
  probearbeit_waschbaer.json, klassenarbeit_biber.json, klassenarbeit_breitmaulnashorn.json
  foerder_etappe1|2|3.json, kiosk.json, wahlphase.json, strategiekarten.json
tools/
  build_material.py N     Input, Merkblatt, Übungsblätter, Hilfen, GN, Probearbeit (Etappe N)
  build_material.py pruefung inhalt/<datei>.json   Probe-/Klassenarbeit einzeln
  build_foerder.py N      Förder-Material NF und GN-F
  build_kiosk.py          apps/kontroll-kiosk/index.html (mit Browsertest)
  build_extras.py         Wahlphase, Strategiekarten, Lernweg (regulär + F)
  build_animation.py      ausgabe/lernweg/Ablauf_Animation.html
  build_anleitung.py      anleitung.html (Lehrkraft-Leitfaden, prüft alle Links)
  build_wissensbasis.py   diese Datei
ausgabe/                Erzeugte PDFs/HTML (etappe1–3, foerder, pruefungen, wahlphase, strategiekarten, lernweg)
apps/kontroll-kiosk/    Kiosk
assets/                 fonts (Andika), bilder (Graustufen + Farbe), grafik (aquarium.svg / _farbe.svg)
planung/                Planungstexte (SRL_Standard, Etappen_Gelingensnachweise, Kompetenzraster, Reihenplanung,
                        Sprachspur, Ergaenzungen_Umsetzung, Foerder_Workflow, Projekte_und_Terminwahl)
materialien/            ältere Vorfassungen (A5-Satz, Otter/Dino-Stil) – nur Tierpakete *_A5.pdf und Planungsbezüge weiter nutzen
skill.md                Produktionsregeln (verbindlich)
```

**Technik:** Python + Playwright/Chromium rendert HTML → PDF; PyMuPDF prüft Schriftgrößen. Jeder Generator prüft automatisch: Seitenüberlauf, Mindestschriftgröße, Input = Merkblatt (Textabgleich), Link-Existenz (Leitfaden), Kiosk-Ansichten. Volle Übungsblätter werden automatisch dichter gesetzt (Schrift bleibt ≥ 14 pt); Förderblätter werden automatisch auf Folgeseiten verteilt.

**Markup in Inhaltsdateien:** `*kursiv*` für Beispielsätze, `**fett**` für Begriffe, `\n` Zeilenumbruch, `{Wort}` = Lücke (Förder-Lückentext, Wortspeicher automatisch).

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


## 13 · Kompetenzraster mit vier Standards (Volltext)

| Kompetenz | Förderstandard – individuelle Ziele | Mindeststandard | Regelstandard | Leistungsstandard |
|---|---|---|---|---|
| K1 · Informationen aus Material nutzen | Ich finde in einem Bild und einem kurzen, bei Bedarf vorgelesenen Text den Tiernamen sowie Angaben zu Nahrung und Lebensraum. Ich zeige oder ordne passende Informationen zu. | Ich nenne das Tier, eine richtige Größen- oder Gewichtsangabe, den Lebensraum und die Nahrung. Ich nutze dafür das Material. | Ich wähle die geforderten Informationen passend aus und gebe sie in eigenen Worten richtig wieder. Ich kann ihre Fundstellen zeigen. | Ich führe Informationen aus Bild und Text gezielt zusammen. Ich unterscheide sichere Angaben von Vermutungen und übernehme keine unbelegten Aussagen. |
| K2 · Das Aussehen genau beschreiben | Ich benenne oder beschrifte zwei auffällige Körperteile. Ich ergänze passende Merkmale, zum Beispiel eine Farbe oder Form. | Ich beschreibe mindestens vier verschiedene äußere Merkmale richtig und verständlich. | Ich beschreibe mindestens vier kennzeichnende Merkmale genau. Ich verbinde Körperteil und passende Angaben zu Form, Farbe oder Beschaffenheit. | Ich wähle besonders kennzeichnende Merkmale aus und beschreibe sie präzise. Meine Beschreibung hilft, das Tier von ähnlichen Tieren zu unterscheiden. |
| K3 · Informationen ordnen | Ich ordne Bilder, Wörter oder Satzstreifen passenden Überschriften zu. Ich nutze eine vorgegebene Reihenfolge. | Ich beginne mit dem Tiernamen und einem Überblick. Danach ordne ich Aussehen, Lebensraum und Nahrung nachvollziehbar. | Ich nutze meinen Schreibplan. Zusammengehörige Informationen stehen zusammen; passende Absätze machen den Aufbau deutlich. | Ich führe klar vom Überblick zu Einzelheiten. Ich verbinde die Abschnitte sinnvoll und vermeide unnötige Wiederholungen und Sprünge. |
| K4 · Sachlich und treffend formulieren | Ich wähle passende Beschreibungswörter aus einer Wortbank. Ich ergänze damit sachliche Aussagen über das Tier. | Ich beschreibe überwiegend sachlich und im Präsens. Ich verwende passende Nomen und Adjektive. | Ich nutze genaue Verben, Adjektive und passende Fachwörter, deren Bedeutung ich verstehe. Ich bleibe sachlich und im Präsens. | Ich formuliere durchgehend präzise und sachlich. Ich setze Fachwörter und unterschiedliche Formulierungen gezielt ein, ohne unnötig kompliziert zu schreiben. |
| K5 · Verständliche Sätze schreiben | Ich formuliere kurze Aussagen mündlich und halte sie mit Satzanfängen, Lücken oder Satzbausteinen schriftlich fest. | Ich schreibe einen kurzen, zusammenhängenden Text aus überwiegend vollständigen und verständlichen Sätzen. | Ich verbinde meine Sätze passend. Unterschiedliche Satzanfänge und eindeutige Bezüge machen meinen Text gut lesbar. | Ich verknüpfe Informationen flüssig und abwechslungsreich. Auch ausführlichere Sätze bleiben klar und verständlich. |
| K6 · Rechtschreibung und Satzzeichen prüfen | Ich vergleiche ausgewählte Tierwörter mit einer Vorlage. Ich prüfe bei kurzen Sätzen den großen Anfang und den Punkt. | Ich prüfe Satzanfänge, Nomen und Satzschlusszeichen. Geübte Wörter schreibe ich überwiegend richtig; mein Text bleibt gut lesbar. | Ich nutze Prüfschritte gezielt und berichtige gefundene Fehler. Satzgrenzen und geübte Schreibungen sind weitgehend sicher. | Ich schreibe auch bei abwechslungsreichen Sätzen weitgehend sicher. Ich erkenne Unsicherheiten und prüfe sie mit passenden Hilfen. |


## 14 · Zieldifferentes Material (Förderschwerpunkt Lernen) ⚙

Zwei Kinder; kurze Texte möglich. Gleiche Etappen und Blattnummern mit „F“, gleicher Input, Fischotter als Beispieltier (Etappe 3F: nur Erdmännchen). Je Etappe vereinfachte **Merkkarte** und **Materialseite** (ein Satz pro Zeile, Foto mit nummerierten Bildstellen). Kleinschrittig: ein Auftrag pro Kasten mit Symbol je Format. Formate: ankreuzen · zuordnen (Zahl ins Kästchen, ggf. nummerierte Bedeutungen) · sortieren (Wortspeicher → Spalten) · Lückentext (Wortspeicher, ggf. Ablenker) · Wortkarten zu einem Satz ordnen · Satz weiterschreiben · Prüfliste · Bild betrachten · Hinweis. Jede Seite mit Lösungsstreifen auf dem Kopf zum Umknicken. Schreiben aufs Blatt. GN-F-Ziele sind Vorschläge; Förderziele individuell vereinbaren, Zeile für eigenes Förderziel.

### Etappe 1F · Informationen finden und ordnen

- Merkkarte: Genau: Genaue Wörter sagen, wie das Tier aussieht: *kurz, lang, dunkelbraun, breit*. · Nicht genau: Diese Wörter sind Meinungen: *toll, schön, süß*. · Bild: Auf dem Foto siehst du: Nase, Auge, Ohr, Tasthaare, Fell. · Text: Im Text findest du: Wo lebt das Tier? Was frisst es? · Ordnen: Aussehen · Lebensraum · Nahrung
- Material „Der Fischotter“: Der Fischotter lebt am Wasser. Er lebt an Flüssen und Seen. Sein Körper ist lang. Seine Beine sind kurz. Sein Fell ist dunkelbraun. Sein Kopf ist breit und flach. An der Schnauze hat er lange Tasthaare. Er frisst vor allem Fische. Er frisst auch Frösche und Krebse. Kopf und Rumpf sind 60 bis 90 Zentimeter lang. Der Schwanz kommt noch dazu.
- Bildstellen: 1, 2, 3, 4, 5 (Ein Fischotter im Gras. Die Zahlen 1 bis 5 zeigen auf Nase, Auge, Ohr, Tasthaare und Fell.)
- **Blatt 1F · Genau oder nicht genau?:** [ankreuzen] Welche Sätze sind genau? Kreuze **2** Sätze an. Richtig: Der Fischotter hat kurze Beine., Das Fell ist dunkelbraun. | [sortieren] Schreibe jedes Wort in die richtige Spalte. Lösung: genau: kurz, dunkelbraun, lang; Meinung: toll, schön, süß | [ankreuzen] **Sprachdetektiv:** Nomen schreibst du groß. Kreuze die **3** Nomen an. Richtig: Fischotter, Beine, Fell
- **Blatt 2F · Was siehst du auf dem Foto?:** [bild] Schau dir das Foto genau an. Die Zahlen zeigen auf Körperteile. | [zuordnen] Welche Zahl gehört zu welchem Wort? Schreibe die Zahl in das Kästchen. Lösung: Nase=1, Auge=2, Ohr=3, Tasthaare=4, Fell=5 | [luecke] Fülle die Lücken. Nutze den Wortspeicher. Lösung: klein, Tasthaare
- **Blatt 3F · Was steht im Text?:** [hinweis] Lies den Text auf der Materialseite. Lies Satz für Satz. Zeige mit dem Finger mit. | [luecke] Fülle die Lücken. Nutze den Wortspeicher. Lösung: Flüssen, Seen, Fische, Zentimeter | [ankreuzen] Zählt der Schwanz bei der Länge mit? Kreuze an. Richtig: nein | [ankreuzen] **Sprachdetektiv:** Welche Wörter sind Verben? Kreuze **2** an. Richtig: lebt, frisst
- **Blatt 4F · Ordne die Informationen:** [sortieren] Schreibe jedes Wort unter die richtige Überschrift. Streiche das Wort im Wortspeicher durch. Lösung: Aussehen: kurze Beine, dunkelbraunes Fell; Lebensraum: Flüsse, Seen; Nahrung: Fische, Krebse | [ankreuzen] Wohin gehört „langer Körper“? Kreuze an. Richtig: Aussehen
- **GN1F:** F1.1 Ich erkenne genaue Wörter. (erreicht, wenn zwei genaue Sätze angekreuzt, keine Meinung) · F1.2 Ich benenne Körperteile auf dem Foto. (erreicht, wenn mindestens drei von vier Zahlen richtig zugeordnet) · F1.3 Ich finde den Lebensraum im Text. (erreicht, wenn Flüsse und Seen richtig eingesetzt) · F1.4 Ich finde die Nahrung im Text. (erreicht, wenn Fische richtig eingesetzt) · F1.5 Ich ordne Angaben unter Überschriften. (erreicht, wenn mindestens fünf von sechs Wörtern richtig sortiert)

### Etappe 2F · Sachlich und genau formulieren

- Merkkarte: Genau: Nimm Wörter, die du prüfen kannst: *dunkelbraun, kurz, breit*. Nicht: *schön, toll*. · Präsens: Eine Tierbeschreibung steht in der Gegenwart: *er lebt, er frisst, es ist*. · Ein Satz: Wer? + Verb + Rest. *Der Fischotter + frisst + Fische.* · Groß: Der Satzanfang ist groß. Nomen sind groß: *Fell, Kopf, Fische*. · Punkt: Am Ende vom Satz steht ein Punkt.
- Material „Der Fischotter“: Der Fischotter lebt an Flüssen und Seen. Sein Körper ist lang. Seine Beine sind kurz. Sein Fell ist oben dunkelbraun. Sein Kopf ist breit und flach. An der Schnauze sitzen lange Tasthaare. Zwischen den Zehen hat er Schwimmhäute. Im Wasser schwimmt er schnell. Er frisst vor allem Fische.
- Bildstellen: 1, 2, 3, 4, 5 (Ein Fischotter im Gras. Die Zahlen 1 bis 5 zeigen auf Nase, Auge, Ohr, Tasthaare und Fell.)
- **Blatt 5F · Treffende Wörter:** [ankreuzen] Wie ist das Fell oben? Kreuze das **genaue** Wort an. Richtig: dunkelbraun | [ankreuzen] Wie ist der Kopf? Kreuze die **genaue** Angabe an. Richtig: breit und flach | [luecke] Mache den Satz genauer. Nutze den Wortspeicher. Lösung: Fischotter, schwimmt | [zuordnen] Was bedeutet das Wort? Schreibe die Zahl in das Kästchen. Lösung: Tasthaare=1, Schwimmhäute=2
- **Blatt 6F · Sachliche Sätze:** [ordnen] Bilde einen Satz aus den Wortkarten. Schreibe ihn auf die Linie. Lösung: Seine Beine sind kurz. | [ordnen] Bilde einen Satz aus den Wortkarten. Schreibe ihn auf die Linie. Lösung: Der Fischotter frisst auch Krebse. | [ankreuzen] Welcher Satz steht in der Gegenwart (Präsens)? Kreuze an. Richtig: Der Fischotter lebt am Wasser. | [luecke] Setze das passende Verb ein. Lösung: frisst, fressen | [ankreuzen] Welcher Satz ist richtig geschrieben? Kreuze an. Richtig: Der Fischotter lebt am See.
- **GN2F:** F2.1 Ich wähle genaue Wörter. (erreicht, wenn genaue Angabe statt Wertung angekreuzt) · F2.2 Ich bilde einen Satz aus Wortkarten. (erreicht, wenn Satz vollständig und in sinnvoller Reihenfolge) · F2.3 Ich wähle das Verb im Präsens. (erreicht, wenn Präsensform richtig gewählt bzw. eingesetzt) · F2.4 Ich erkenne große Anfänge, Nomen und Punkt. (erreicht, wenn richtig geschriebenen Satz angekreuzt) · F2.5 Ich kenne ein Fachwort. (erreicht, wenn Fachwort richtig zugeordnet)

### Etappe 3F · Eine Tierbeschreibung schreiben und prüfen

- Merkkarte: Plan: Überblick · Aussehen · Lebensraum · Nahrung · Überblick: Name und Größe: *Das Erdmännchen ist 25 bis 29 Zentimeter lang.* · Aussehen: Vier Merkmale: Körper, Fell, Schwanz, Krallen … · Text: Erst der Name, dann das Aussehen, dann Lebensraum und Nahrung. · Prüfen: Großer Anfang? Nomen groß? Punkt am Ende?
- Material „Das Erdmännchen“: Das Erdmännchen lebt in Afrika. Es lebt im trockenen Grasland. Sein Körper ist schlank. Sein Fell ist hellbraun. Auf dem Rücken hat es dunkle Streifen. Um die Augen hat es dunkle Flecken. Sein Schwanz ist lang und schmal. An den Pfoten hat es lange Krallen. Kopf und Rumpf sind 25 bis 29 Zentimeter lang. Der Schwanz kommt noch dazu. Es frisst vor allem Insekten. Es frisst auch Spinnen.
- Bildstellen: 1, 2, 3, 4 (Ein Erdmännchen steht aufrecht. Die Zahlen zeigen auf Augenfleck, Körper, Schwanz und Pfote mit Krallen.)
- **Blatt 7F · Dein Schreibplan:** [bild] Schau dir das Foto genau an. Die Zahlen zeigen auf Körperteile. | [zuordnen] Welche Zahl gehört zu welchem Wort? Schreibe die Zahl in das Kästchen. Lösung: Fleck um das Auge=1, Körper=2, Schwanz=3, Pfote mit Krallen=4 | [sortieren] Ordne die Stichwörter. Schreibe jedes unter die richtige Überschrift. Lösung: Aussehen: schlanker Körper, hellbraunes Fell, langer Schwanz, lange Krallen; Lebensraum: Afrika, Grasland; Nahrung: Insekten, Spinnen | [luecke] Fülle den Überblick aus. Nutze die Materialseite. Lösung: Erdmännchen, Zentimeter, Schwanz
- **Blatt 8F · Deine Tierbeschreibung:** [luecke] Fülle die Lücken. So entsteht deine Tierbeschreibung. Nutze deinen Plan von Blatt 7F. Lösung: schlanken, hellbraun, Streifen, lang, Grasland, Insekten | [schreiben] Schreibe einen eigenen Satz über die Pfoten. Lies danach deinen ganzen Text leise vor. Lösung: An den Pfoten hat es lange Krallen.
- **Blatt 9F · Prüfen und verbessern:** [check] Prüfe deinen Text von Blatt 8F. Kreuze an, was du gefunden hast. Zeige den Text danach einem anderen Kind oder deiner Lehrkraft. | [ankreuzen] Welcher Satz ist richtig geschrieben? Kreuze an. Richtig: Sein Fell ist hellbraun. | [schreiben] Verbessere den Satz. Schreibe ihn richtig auf die Linie. Lösung: Es frisst vor allem Insekten.


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

## 16 · Offene Punkte (Stand 09.10.2026)

- Arbeitszeit der Probearbeit; Arbeitszeit, Punkteverteilung und Notengrenzen der Klassenarbeit.
- Foto Breitmaulnashorn fehlt (Platzhalter); Biber-Foto vorläufig (Tierpaket, CC BY-SA 3.0). Wunschbild tierdoku.de nicht ladbar und ohne freie Lizenz.
- Probearbeit F und Klassenarbeit F (Lückentext mit Wortspeicher im selben Aufbau).
- Zuordnung Variante ↔ Termin (Vorschlag Biber früh, Nashorn spät).
- Lehrkraft-Cockpit `index.html` zeigt noch Vorfassungen; Branch `claude/etappe1-muster` noch nicht in `main`.
- Gedruckte Lösungsfassung (Tipps/Lösungen wie im Kiosk) und ggf. Übungskarten-Modus im Kiosk.
- Unterrichtserprobung steht aus; Zeitbudget nach Erprobung prüfen.

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
| Sprachspur | in die Etappen integrierte Grammatik-/Rechtschreibinhalte |
| K1–K6 | Textkriterien: Informationen, Aussehen, Aufbau, Sachlich, Verständlich, Schreibung |
| F-Material | zieldifferentes Material (Förderschwerpunkt Lernen), Blätter 1F–9F |
