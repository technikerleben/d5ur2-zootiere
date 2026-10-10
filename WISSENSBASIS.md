# Wissensbasis · Deutsch 5 · Unterrichtsreihe „Zootiere“

> **Zweck:** Vollständige, verbindliche Wissensgrundlage für ein LLM, das an dieser Reihe weiterarbeitet (Material ergänzen, ändern, prüfen, Fragen beantworten).
> **Stand:** 10.10.2026. Abschnitte mit ⚙ werden aus den Inhaltsdateien `inhalt/*.json` erzeugt (`python tools/build_wissensbasis.py`) und spiegeln den aktuellen Materialstand.
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
- 16 · Offene Punkte (Stand 10.10.2026)
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
- **Kontroll-Kiosk** (Laptop im Raum) ist die einzige digitale Schüleranwendung **im Unterricht**; Kinder haben keine iPads.
- **Lern-App fürs Smartphone (Grundversion gebaut, 10.10.2026):** freiwilliger Lernbegleiter für zu Hause auf eigenen oder elterlichen Handys (`lernapp/`, Planung: `planung/Lernapp_Planung.md`). Lernweg, Merkkarten, Übungen, Quiz, Buchstabenrätsel, Training, Üben an Tieren der eigenen Umgebung. **Keine Kiosk-Lösungen zu Blatt 1–9**, keine Prüfungstiere, keine GN-Auszüge, keine Kinderdaten (nur `localStorage`), bewertungsneutral. Elterninfo in sechs Sprachen (Deutsch, Ukrainisch, Hocharabisch, Türkisch, Englisch, Französisch) mit KI-Hinweis: App KI-unterstützt programmiert, Inhalte überwiegend KI-generiert, von den Lehrkräften geprüft und verantwortet. Übersetzungen tragen den Hinweis, dass sie KI-generiert sind und ungenau sein können. Bei jedem Öffnen erscheint ein Hinweis: In der Schule ist das Handy ausgeschaltet in der Schultasche; die App ist zum Lernen zu Hause und wird in der Schule nicht genutzt.

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
| Beispielaufgabe Training | Angola-Giraffe (Zikomo, Zoo Dortmund) | durchklickbare Beispielaufgabe mit drei Mustertexten (Mindest-/Regel-/Leistungsstandard) und Vorlesen; eigenständige Seite `apps/beispielaufgabe-giraffe/index.html`; in der Lern-App aus `inhalt/training_giraffe.json` (8 Schritte, Interview-Detektiv, Plan, Mustertexte). Pflegerin: Frau Brandt |
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


## 8 · Etappen im Detail ⚙

### 8.0 Interviews als Textbasis

Rahmen: Die Schülerzeitung „Zoo-Reporter“ war im Zoo und hat mit Tierpflegerinnen und Tierpflegern gesprochen. Hinweis auf jeder Seite: „Das Interview ist ausgedacht. Die Angaben über das Tier stimmen.“ Keine echte Person, kein echter Zoo. Lange Interviews 250–350 Wörter (Prüfungen etwa 265), Förder 6 Fragen. Markierung: ⟦Stelle|Kürzel⟧ wie in `inhalt/interviews.json`.

#### Beispieltier · Etappe 1–2 · „Otto taucht am liebsten“ (Frau Berger, `fischotter`)

- **Frau Berger, wie fängt Ihr Tag bei den Ottern an?** ⟦Um halb acht mache ich die Anlage sauber. Danach gibt es Frühstück.|X⟧ ⟦Unser Otto wartet dann schon am Gitter und pfeift laut.|X⟧ ⟦Ehrlich gesagt ist er der süßeste Otter der Welt!|W⟧
- **Was gibt es denn zum Frühstück?** Vor allem Fisch. ⟦Otto bekommt jeden Tag einen kleinen Eimer voll.|X⟧ In der Natur ⟦fressen Fischotter hauptsächlich Fische|N⟧. ⟦Sie fangen aber auch Frösche und Krebse.|N⟧ ⟦Gestern hat Otto einen Krebs ganz allein geknackt. Das hat richtig gekracht!|X⟧
- **Wo leben Fischotter, wenn sie nicht im Zoo sind?** ⟦An Flüssen und Seen.|L⟧ ⟦Sie brauchen Ufer, an denen sie sich verstecken können|L⟧, zum Beispiel unter Büschen und Wurzeln. ⟦Deshalb liegen in unserer Anlage auch so viele alte Wurzeln herum.|X⟧
- **Ist ein Otter eigentlich mit dem Biber verwandt?** Nein. ⟦Fischotter gehören zu den Mardern.|T⟧ Biber sind Nagetiere. Das ist etwas ganz anderes.
- **Woran erkennt man einen Fischotter?** Schauen Sie mal, wie er durchs Wasser saust! ⟦Sein Körper ist lang und schmal|A⟧, ⟦fast wie ein Torpedo|V⟧. ⟦Die Beine sind dagegen richtig kurz.|A⟧ Und ⟦der Kopf ist breit und flach|A⟧. Ich sage immer: ⟦wie ein Brett mit Nase|V⟧.
- **Und die Ohren? Ich sehe gar keine.** ⟦Die sind ganz klein.|A⟧ ⟦Beim Tauchen kann er sie sogar verschließen, damit kein Wasser hineinläuft.|Z⟧
- **Wie groß ist Otto eigentlich?** ⟦Letzte Woche haben wir ihn gemessen. Von der Nase bis zum Schwanzansatz waren es 80 Zentimeter.|X⟧ Der Schwanz kommt noch dazu. ⟦Fischotter sind meistens 60 bis 90 Zentimeter lang, wenn man den Schwanz nicht mitzählt.|M⟧
- **Darf man ihn streicheln? Das Fell sieht so weich aus.** Nein, ⟦Otto ist kein Kuscheltier. Ich fasse ihn nur an, wenn die Tierärztin kommt.|X⟧ ⟦Das Fell ist sehr dicht.|A⟧ ⟦Oben ist es dunkelbraun, am Hals ist es heller.|A⟧
- **Gibt es noch etwas Besonderes?** Ja, ⟦die langen Tasthaare an der Schnauze|A⟧! ⟦Damit spürt er Fische, auch wenn das Wasser trüb ist.|Z⟧ Und ⟦zwischen den Zehen hat er Schwimmhäute|A⟧. ⟦Deshalb ist er so ein toller Schwimmer.|W⟧
- **Vielen Dank, Frau Berger!** Gern. ⟦Und kommt Otto bald besuchen!|X⟧
- Wörterhilfe: Anlage = Gehege im Zoo; Tasthaare = Haare zum Ertasten; trüb = nicht klar, man sieht wenig; Schwanzansatz = Stelle, an der der Schwanz beginnt

#### Übungstier · Etappe 3 · „Kiki hält Wache“ (Herr Yıldız, `erdmaennchen`)

- **Herr Yıldız, wie viele Erdmännchen leben hier?** Im Moment neun. ⟦Erdmännchen leben immer in Gruppen.|Z⟧ ⟦Allein wären sie unglücklich, glaube ich.|W⟧ ⟦Unsere Chefin heißt Kiki. Sie ist die Mutigste von allen.|X⟧
- **Was macht Kiki gerade da oben auf dem Stein?** ⟦Sie hält Wache.|X⟧ ⟦Einer aus der Gruppe stellt sich immer auf die Hinterbeine und schaut sich um.|Z⟧ ⟦Der Schwanz ist lang und schmal|A⟧, ⟦die Spitze ist dunkel|A⟧. ⟦Wenn ein Greifvogel kommt, pfeift der Wächter, und alle verschwinden im Bau.|Z⟧
- **Im Bau?** Ja. In der Natur ⟦leben Erdmännchen im trockenen Gras- und Buschland im Süden von Afrika|L⟧. ⟦Dort graben sie unterirdische Gänge.|L⟧ Das können sie gut, denn ⟦an den Pfoten haben sie lange Krallen|A⟧. ⟦Letzten Sommer haben unsere einen Tunnel bis unter den Zaun gegraben. Da musste ich ganz schön rennen!|X⟧
- **Sind Erdmännchen eigentlich Mäuse?** Nein, überhaupt nicht! ⟦Sie gehören zu den Mangusten.|T⟧ Das ist eine Familie von kleinen Raubtieren.
- **Raubtiere? Was fressen die denn?** ⟦Vor allem Insekten, also Käfer, Heuschrecken und Larven.|N⟧ ⟦Aber auch Spinnen und kleine Eidechsen.|N⟧ ⟦Bei uns gibt es morgens Mehlwürmer. Die mag Kiki am allerliebsten.|X⟧
- **Wie groß werden Erdmännchen?** ⟦Kopf und Rumpf sind zusammen nur etwa 25 bis 29 Zentimeter lang. Der Schwanz kommt noch dazu.|M⟧ ⟦Kiki ist sogar ein bisschen kleiner. Sie wiegt nicht einmal ein Kilo.|X⟧
- **Und wie sehen sie sonst aus?** ⟦Ihr Körper ist schlank.|A⟧ ⟦Das Fell ist hellbraun bis graubraun|A⟧, und ⟦auf dem Rücken haben sie dunklere Streifen|A⟧. Am Kopf fällt ⟦die spitze Schnauze|A⟧ auf. Und ⟦um die Augen haben sie dunkle Flecken|A⟧. ⟦Das sieht aus wie eine Sonnenbrille.|V⟧ ⟦Total cool, oder?|W⟧
- **Wofür sind die Flecken gut?** ⟦Man vermutet, dass sie die Augen vor der grellen Sonne schützen. Ganz sicher weiß man das aber nicht.|U⟧ Übrigens: ⟦Die kleinen Ohren können sie beim Graben verschließen.|A⟧ So kommt kein Sand hinein.
- **Haben Sie noch einen Tipp für unsere Leserinnen und Leser?** ⟦Kommt am besten morgens. Dann sonnen sich alle vor dem Bau.|X⟧ ⟦Das ist der schönste Anblick im ganzen Zoo!|W⟧
- Wörterhilfe: Mangusten = eine Familie von kleinen Raubtieren; Bau = Versteck unter der Erde mit Gängen; Rumpf = Körper ohne Kopf, Beine und Schwanz; Greifvogel = Vogel, der andere Tiere jagt, zum Beispiel ein Adler

#### Übungstier · Etappe 3 · „Mei klettert, wenn es dunkel wird“ (Frau Nowak, `roter-panda`)

- **Frau Nowak, wo ist denn der Panda? Ich sehe nur Bäume.** ⟦Mei schläft oben in der Astgabel. Am Vormittag ist sie meistens faul.|X⟧ ⟦Rote Pandas sind vor allem in der Dämmerung und nachts unterwegs.|Z⟧ ⟦Da muss man Geduld haben!|W⟧
- **Ist Mei ein kleiner Großer Panda?** Das fragen viele! ⟦Der Rote Panda heißt auch Kleiner Panda.|T⟧ Mit dem großen schwarz-weißen Panda ist er aber nicht nah verwandt. Beide fressen nur gern Bambus.
- **Dann frisst Mei also Bambus?** Ja, ⟦hauptsächlich Bambus.|N⟧ ⟦Daneben fressen Rote Pandas zum Beispiel Beeren und Eier.|N⟧ ⟦Mei bekommt jeden Morgen frische Bambusstangen und ein paar Weintrauben. Letzte Woche hat sie die Trauben zuerst gefressen und den Bambus liegen lassen.|X⟧
- **Wo leben Rote Pandas in der Natur?** ⟦In Bergwäldern in Asien, in denen Bambus wächst.|L⟧ Dort ist es oft kühl und feucht. ⟦Deshalb haben wir in der Anlage so viele schattige Bäume gepflanzt.|X⟧
- **Woran erkennt man einen Roten Panda?** Zuerst an der Farbe! ⟦Am Rücken ist das Fell rötlich braun.|A⟧ ⟦Die Beine und der Bauch sind dunkel bis schwarz.|A⟧ ⟦Im Gesicht hat er helle, fast weiße Bereiche.|A⟧ ⟦Der Kopf ist rund|A⟧, und ⟦die Ohren sind groß und spitz|A⟧. ⟦Mei sieht aus wie ein Kuscheltier.|V⟧ ⟦Ich finde, sie ist das hübscheste Tier hier.|W⟧
- **Und der Schwanz? Der ist ja riesig!** Genau. ⟦Der Schwanz ist lang und buschig.|A⟧ ⟦Er hat hellere und dunklere Ringe.|A⟧ ⟦Beim Klettern helfen ihm der Schwanz und die Krallen.|Z⟧ ⟦Im Winter wickelt sich Mei beim Schlafen in ihren Schwanz ein wie in eine Decke.|X⟧
- **Wie groß ist ein Roter Panda?** ⟦Kopf und Rumpf sind zusammen etwa 60 Zentimeter lang. Der Schwanz kommt noch dazu.|M⟧ ⟦Mei ist etwas kleiner, sie ist noch jung.|X⟧
- **Haben Sie zum Schluss noch einen Tipp?** ⟦Kommt am späten Nachmittag. Dann klettert Mei herunter und sucht ihr Futter.|X⟧ ⟦Das ist jedes Mal ein Erlebnis!|W⟧
- Wörterhilfe: Dämmerung = Zeit zwischen Tageslicht und Dunkelheit; Bambus = eine Pflanze mit festen Halmen; Rumpf = Körper ohne Kopf, Beine und Schwanz; verwandt = zur gleichen Tierfamilie gehören

#### Probearbeit · „Rocky öffnet jede Dose“ (Herr Schäfer, `waschbaer`)

- **Herr Schäfer, warum steht da ein Schloss an der Futterkiste?** ⟦Wegen Rocky! Er öffnet jede Dose und jede Kiste.|X⟧ ⟦Mit den Vorderpfoten kann ein Waschbär Nahrung geschickt greifen.|Z⟧ ⟦An jeder Pfote sitzen fünf Zehen.|A⟧ ⟦Ehrlich, manchmal ist er schlauer als ich.|W⟧
- **Woher kommen Waschbären eigentlich?** ⟦Ursprünglich aus Nordamerika.|L⟧ ⟦Sie leben gern in Wäldern mit Gewässern.|L⟧ ⟦Heute kommen sie aber auch in Städten vor.|L⟧
- **Gibt es auch in Deutschland Waschbären?** ⟦Ja. Ein Nachbar von mir hatte neulich einen im Garten. Der hat in der Nacht die ganze Mülltonne ausgeräumt!|X⟧ ⟦Waschbären sind vor allem nachts unterwegs.|Z⟧
- **Was frisst Rocky?** ⟦Waschbären fressen pflanzliche und tierische Nahrung.|N⟧ ⟦Zum Beispiel Früchte, Nüsse, Insekten und Frösche.|N⟧ ⟦Rocky liebt Weintrauben. Gestern hat er eine ganze Schale leer gemacht.|X⟧
- **Warum heißt er eigentlich Waschbär?** ⟦Waschbären gehören zu den Kleinbären.|T⟧ ⟦Oft tasten sie ihr Futter im Wasser ab. Das sieht aus, als würden sie es waschen.|Z⟧ ⟦Rocky taucht seine Trauben auch immer in den Wassernapf.|X⟧ ⟦Das ist so lustig!|W⟧
- **Woran erkennt man einen Waschbären?** ⟦Am Gesicht! Um die Augen liegt eine schwarze Zeichnung.|A⟧ ⟦Die sieht aus wie eine Maske von einem Räuber.|V⟧ ⟦Die Ohren sind abgerundet und haben einen hellen Rand.|A⟧ ⟦Der Körper ist kräftig und wirkt gedrungen.|A⟧ ⟦Das Fell ist meist graubraun.|A⟧
- **Und der Schwanz?** ⟦Der ist buschig und hat mehrere dunkle Ringe.|A⟧ ⟦Ich finde, das ist der schönste Schwanz im ganzen Zoo.|W⟧
- **Wie schwer ist so ein Waschbär?** ⟦Ein erwachsener Waschbär wiegt häufig etwa sechs bis sieben Kilogramm.|M⟧ ⟦Rocky wiegt im Moment acht Kilo. Er hat im Herbst zu viel genascht.|X⟧
- **Danke, Herr Schäfer!** ⟦Gern. Und passt auf eure Brotdosen auf!|X⟧
- Wörterhilfe: gedrungen = eher kurz und kräftig gebaut; Zeichnung = Muster auf dem Fell; Vorderpfoten = die beiden vorderen Pfoten; ursprünglich = zuerst, von Anfang an

#### Klassenarbeit Variante 1 · „Bruno baut die ganze Nacht“ (Frau Krause, `biber`)

- **Frau Krause, was ist denn mit dem Baumstamm passiert?** ⟦Das war Bruno heute Nacht!|X⟧ ⟦Biber sind Nagetiere.|T⟧ ⟦Ihre großen Schneidezähne sind vorne orange gefärbt.|A⟧ Damit können sie sogar dicke Äste durchnagen. ⟦Bruno ist da wirklich ein Meister.|W⟧
- **Fressen Biber Holz?** Nicht direkt. ⟦Biber ernähren sich von Pflanzen.|N⟧ ⟦Sie fressen zum Beispiel Blätter, junge Triebe und Rinde.|N⟧ ⟦Bruno bekommt jeden Abend Weidenzweige. Die Rinde nagt er ab, den Rest verbaut er.|X⟧
- **Wo leben Biber in der Natur?** ⟦An Flüssen und Seen.|L⟧ ⟦Sie bauen dort Burgen aus Ästen und Schlamm.|Z⟧
- **Wann ist Bruno denn wach?** ⟦Biber sind vor allem in der Dämmerung und nachts aktiv.|Z⟧ ⟦Tagsüber schläft Bruno in seiner Burg. Wenn ich morgens komme, finde ich nur noch Holzspäne.|X⟧
- **Wie sieht ein Biber aus?** ⟦Sein Körper ist kräftig|A⟧ und ⟦die Beine sind kurz|A⟧. ⟦Das Fell ist braun und sehr dicht.|A⟧ ⟦Am Kopf sitzen kleine Ohren und eine stumpfe Schnauze.|A⟧ ⟦Bruno sieht ein bisschen aus wie ein dicker Teddy.|V⟧ ⟦Ich finde ihn total niedlich.|W⟧ ⟦Zwischen den Zehen der Hinterfüße liegen Schwimmhäute.|A⟧
- **Und was ist das für ein komischer Schwanz?** ⟦Der Schwanz ist breit und flach. Er ist kaum behaart und mit Schuppen bedeckt.|A⟧ Dieser Schwanz heißt auch Kelle. ⟦Wenn Gefahr droht, klatscht der Biber damit aufs Wasser.|Z⟧ ⟦Letzte Woche hat Bruno mich damit ganz nass gespritzt!|X⟧
- **Kann ein Biber gut tauchen?** ⟦Ja, er kann mehrere Minuten unter Wasser bleiben.|Z⟧ ⟦Bruno taucht einmal quer durch unseren Teich. Das sind bestimmt 20 Meter.|X⟧ ⟦Das finde ich jedes Mal spannend.|W⟧
- **Wie schwer ist so ein Biber?** ⟦Ein erwachsener Biber kann etwa 13 bis 35 Kilogramm wiegen.|M⟧ ⟦Bruno wiegt gerade 25 Kilo.|X⟧
- Wörterhilfe: Triebe = junge Teile einer Pflanze; Kelle = Name für den breiten Biberschwanz; Schneidezähne = die vorderen Zähne zum Abbeißen und Nagen; Burg = Wohnhöhle des Bibers aus Ästen; Späne = kleine, dünne Holzstücke

#### Klassenarbeit Variante 2 · „Nala badet gern im Schlamm“ (Herr Mensah, `breitmaulnashorn`)

- **Herr Mensah, warum ist Nala so dreckig?** ⟦Sie hat sich gerade im Schlamm gewälzt. Das macht sie jeden Mittag.|X⟧ ⟦Der Schlamm schützt die Haut vor Sonne und Insekten.|Z⟧ ⟦Für mich ist das der lustigste Moment des Tages.|W⟧
- **Was für ein Nashorn ist Nala?** ⟦Ein Breitmaulnashorn.|T⟧ ⟦Es hat sehr breite Lippen.|A⟧ Damit rupft es das Gras ab, ⟦fast wie ein Rasenmäher|V⟧.
- **Was frisst ein Breitmaulnashorn?** ⟦Es frisst fast nur Gras.|N⟧ ⟦Nala bekommt bei uns Heu, jeden Tag einen ganzen Berg.|X⟧
- **Wo leben Breitmaulnashörner in der Natur?** ⟦In Afrika.|L⟧ ⟦Sie leben in Savannen mit kurzem Gras.|L⟧
- **Wie sieht ein Breitmaulnashorn aus?** ⟦Der Körper ist groß und massig.|A⟧ ⟦Die Haut ist grau und dick.|A⟧ ⟦Sie hat fast keine Haare.|A⟧ ⟦Im Nacken hat es einen Buckel.|A⟧ ⟦Die Beine sind kurz und kräftig.|A⟧ ⟦Nala sieht aus wie ein Panzer auf vier Beinen.|V⟧
- **Kann Nala gut sehen?** ⟦Nashörner sehen eher schlecht. Dafür können sie sehr gut hören und riechen.|Z⟧ ⟦Wenn ich mit dem Heuwagen komme, dreht Nala schon von Weitem die Ohren zu mir.|X⟧
- **Und die Hörner?** ⟦Auf der Nase trägt es zwei Hörner. Das vordere Horn ist länger als das hintere.|A⟧ ⟦Nalas vorderes Horn ist ein bisschen abgebrochen. Sie ist gegen einen Baum gerannt.|X⟧
- **Wie groß ist so ein Tier?** ⟦Kopf und Rumpf sind zusammen etwa 3,40 bis 3,80 Meter lang. Der Schwanz kommt noch dazu.|M⟧ ⟦Ein erwachsenes Männchen kann bis zu 3600 Kilogramm wiegen.|M⟧ ⟦Nala ist ein Weibchen und etwas leichter.|X⟧ ⟦Ich finde sie trotzdem riesig!|W⟧
- **Wie lange sind Sie schon Nalas Pfleger?** ⟦Seit sieben Jahren. Am Anfang hatte ich ein bisschen Angst vor ihr.|X⟧ ⟦Heute ist sie für mich das tollste Tier der Welt.|W⟧
- Wörterhilfe: Savanne = Grasland mit wenigen Bäumen; massig = sehr groß und schwer; Buckel = eine Erhöhung im Nacken; sich wälzen = sich hin und her rollen

#### Training vor der Klassenarbeit · Ü1 · „Kito springt über jeden Zaun“ (Frau Demir, `elenantilope`)

- **Frau Demir, ist das da hinten eine Kuh?** Nein, das ist Kito, unser Bulle! ⟦Viele Besucher halten ihn für eine Kuh, weil er so groß ist.|X⟧ ⟦Elenantilopen gehören zu den größten Antilopen der Welt.|T⟧
- **Wie groß ist so ein Tier?** ⟦Bei einem erwachsenen Männchen sind Kopf und Rumpf zusammen 2,50 bis 3,40 Meter lang. Der Schwanz kommt noch dazu.|M⟧ ⟦Kito wiegt im Moment 780 Kilogramm.|X⟧ ⟦Wir haben ihn letzten Monat auf eine Viehwaage gestellt. Das war ein Abenteuer!|X⟧
- **Woran erkennt man eine Elenantilope?** ⟦Der Körper ist groß und massig.|A⟧ ⟦Das Fell ist hellbraun bis grau.|A⟧ ⟦An den Seiten hat sie schmale, helle Querstreifen.|A⟧ ⟦Am Hals hängt eine große Hautfalte. Sie heißt Wamme.|A⟧ ⟦Kitos Wamme wackelt beim Laufen hin und her, wie ein Vorhang.|V⟧
- **Und die Hörner?** ⟦Beide, Männchen und Weibchen, haben Hörner.|A⟧ ⟦Die Hörner sind lang und schraubenförmig gedreht.|A⟧ ⟦Ich finde, Kito hat die schönsten Hörner im ganzen Zoo!|W⟧
- **Wo leben Elenantilopen in der Natur?** ⟦In Afrika, vor allem im Osten und im Süden.|L⟧ ⟦Sie leben in Savannen und im Buschland.|L⟧ ⟦Bei uns ist es Kito im Winter manchmal zu nass, dann bleibt er lieber im Stall.|X⟧
- **Was fressen sie?** ⟦Vor allem Blätter, Früchte und Schoten von Büschen und Bäumen.|N⟧ ⟦Gras fressen sie nur, wenn es frisch ist.|N⟧ ⟦Kito bekommt bei uns Heu, Zweige und jeden Tag ein paar Möhren.|X⟧ ⟦Die Möhren liebt er.|X⟧
- **Stimmt es, dass Elenantilopen gut springen können?** ⟦Ja, junge Tiere springen aus dem Stand über Hindernisse, die so hoch sind wie zwei Menschen.|Z⟧ ⟦Ich glaube, Kito könnte über unseren Zaun springen. Er will aber nicht.|U⟧ ⟦Darüber bin ich ehrlich gesagt sehr froh!|W⟧
- **Vielen Dank, Frau Demir!** ⟦Gern geschehen. Und besucht Kito bald einmal!|X⟧
- Wörterhilfe: Bulle = männliches Tier bei Rindern und großen Antilopen; massig = sehr groß und schwer; Wamme = Hautfalte am Hals; Schoten = Hüllen mit Samen, zum Beispiel bei Bohnen

#### Training vor der Klassenarbeit · Ü2 · „Raja ist der Schnellste“ (Herr Lindner, `hirschziegenantilope`)

- **Herr Lindner, warum sind die Tiere so unterschiedlich gefärbt?** ⟦Das schwarze Tier ist Raja, unser Männchen.|X⟧ ⟦Bei Hirschziegenantilopen sehen Männchen und Weibchen ganz verschieden aus.|Z⟧ ⟦Erwachsene Männchen sind auf dem Rücken fast schwarz.|A⟧ ⟦Die Weibchen sind auf dem Rücken hellbraun.|A⟧ ⟦Der Bauch ist bei beiden weiß.|A⟧
- **Was ist das Weiße um die Augen?** ⟦Um die Augen haben sie einen weißen Ring.|A⟧ ⟦Das sieht aus, als hätte Raja eine Brille auf.|V⟧ ⟦Total witzig, finde ich!|W⟧
- **Haben alle Tiere Hörner?** ⟦Nein, nur die Männchen.|A⟧ ⟦Die Hörner sind lang und schraubenförmig gewunden.|A⟧ ⟦Sie sind meistens etwa 50 Zentimeter lang.|A⟧ ⟦Rajas Hörner sind sogar ein bisschen länger. Darauf ist er bestimmt stolz.|U⟧
- **Wie groß ist so eine Antilope?** ⟦Kopf und Rumpf sind zusammen etwa 1,20 Meter lang. Der Schwanz kommt noch dazu.|M⟧ ⟦Sie wiegt ungefähr 40 Kilogramm.|M⟧ ⟦Raja wiegt 38 Kilo. Er ist sehr schlank.|X⟧
- **Woher kommen Hirschziegenantilopen?** ⟦Aus Indien und Nepal.|L⟧ ⟦Dort leben sie in offenen Steppen und im Grasland.|L⟧ ⟦Ich war vor zwei Jahren in Indien und habe dort eine Herde gesehen. Das war mein schönster Urlaub!|X⟧
- **Was fressen sie?** ⟦Hauptsächlich Gras.|N⟧ ⟦Manchmal fressen sie auch Blätter und Kräuter.|N⟧ ⟦Bei uns gibt es Heu und frisches Gras. Raja frisst immer zuerst die Kräuter heraus.|X⟧
- **Leben die Tiere allein?** ⟦Nein, Hirschziegenantilopen leben in Herden.|Z⟧ ⟦Bei uns wohnen Raja und vier Weibchen zusammen. Die Weibchen heißen nach Blumen.|X⟧
- **Und warum heißt das Interview „Raja ist der Schnellste“?** ⟦Hirschziegenantilopen können sehr schnell rennen, bis zu 80 Kilometer pro Stunde.|Z⟧ ⟦Raja rennt jeden Morgen einmal quer durch die Anlage.|X⟧ ⟦Für mich ist er das schnellste Tier im ganzen Zoo!|W⟧
- Wörterhilfe: Steppe = weites, trockenes Grasland ohne Wald; gewunden = in Drehungen gebogen; Rumpf = Körper ohne Kopf, Beine und Schwanz; Anlage = Gehege im Zoo

#### Förder · Etappe 1–2 · Otto taucht gern (Frau Berger, `fischotter-f`)

- **Wo leben Fischotter?** ⟦Fischotter leben an Flüssen und Seen.|L⟧ ⟦Unser Otto wohnt im Zoo.|X⟧
- **Was fressen Fischotter?** ⟦Fischotter fressen Fische, Frösche und Krebse.|N⟧ ⟦Otto frisst am liebsten Forellen.|X⟧
- **Wie sieht ein Fischotter aus?** ⟦Der Körper ist lang.|A⟧ ⟦Das Fell ist dunkelbraun.|A⟧
- **Und die Beine und der Kopf?** ⟦Die Beine sind kurz.|A⟧ ⟦Der Kopf ist breit und flach.|A⟧
- **Wie groß ist ein Fischotter?** ⟦Ein Fischotter ist ohne Schwanz etwa 60 bis 90 Zentimeter lang.|M⟧ ⟦Otto ist 80 Zentimeter lang.|X⟧
- **Wie finden Sie Otto?** ⟦Otto ist der süßeste Otter der Welt!|W⟧
- Wörterhilfe: Forellen = eine Art von Fischen

#### Förder · Etappe 3 · Kiki hält Wache (Herr Yıldız, `erdmaennchen-f`)

- **Wo leben Erdmännchen?** ⟦Erdmännchen leben im trockenen Grasland in Afrika.|L⟧ ⟦Kiki wohnt im Zoo.|X⟧
- **Was fressen Erdmännchen?** ⟦Erdmännchen fressen Insekten und Spinnen.|N⟧ ⟦Kiki mag Mehlwürmer.|X⟧
- **Wie sieht ein Erdmännchen aus?** ⟦Das Fell ist hellbraun.|A⟧ ⟦Der Körper ist schlank.|A⟧
- **Was hat es noch?** ⟦Der Schwanz ist lang und schmal.|A⟧ ⟦Auf dem Rücken hat es dunkle Streifen.|A⟧
- **Wie groß ist ein Erdmännchen?** ⟦Ein Erdmännchen ist ohne Schwanz etwa 25 bis 29 Zentimeter lang.|M⟧ ⟦Kiki ist kleiner.|X⟧
- **Wie finden Sie Kiki?** ⟦Kiki ist das mutigste Tier im Zoo!|W⟧
- Wörterhilfe: Grasland = Land mit Gras und wenigen Bäumen

#### Förder · Probearbeit F · Rocky öffnet jede Dose (Herr Schäfer, `waschbaer-f`)

- **Wo leben Waschbären?** ⟦Waschbären leben in Wäldern mit Wasser.|L⟧ ⟦Sie leben auch in Städten.|L⟧
- **Was fressen Waschbären?** ⟦Waschbären fressen Früchte, Nüsse und Insekten.|N⟧ ⟦Rocky mag am liebsten Weintrauben.|X⟧
- **Wie sieht ein Waschbär aus?** ⟦Das Fell ist graubraun.|A⟧ ⟦Um die Augen hat er eine schwarze Maske.|A⟧
- **Was hat er noch?** ⟦Der Schwanz ist buschig.|A⟧ ⟦Der Körper ist kräftig.|A⟧
- **Wie schwer ist ein Waschbär?** ⟦Ein Waschbär wiegt etwa 6 bis 7 Kilogramm.|M⟧ ⟦Rocky wiegt 8 Kilo.|X⟧
- **Wie finden Sie Rocky?** ⟦Rocky ist der schlauste Waschbär der Welt!|W⟧
- Wörterhilfe: Maske = schwarzes Muster um die Augen

#### Förder · Klassenarbeit F · Bruno baut die ganze Nacht (Frau Krause, `biber-f`)

- **Wo leben Biber?** ⟦Biber leben an Flüssen und Seen.|L⟧ ⟦Bruno wohnt im Zoo am Teich.|X⟧
- **Was fressen Biber?** ⟦Biber fressen Blätter und Rinde.|N⟧ ⟦Bruno mag am liebsten Weidenzweige.|X⟧
- **Wie sieht ein Biber aus?** ⟦Das Fell ist braun und dicht.|A⟧ ⟦Der Körper ist kräftig.|A⟧
- **Was hat er noch?** ⟦Der Schwanz ist breit und flach.|A⟧ ⟦Die Zähne sind vorne orange.|A⟧
- **Wie schwer ist ein Biber?** ⟦Ein Biber wiegt etwa 13 bis 35 Kilogramm.|M⟧ ⟦Bruno wiegt 25 Kilo.|X⟧
- **Wie finden Sie Bruno?** ⟦Bruno ist total niedlich!|W⟧
- Wörterhilfe: Rinde = Haut von Bäumen

### Etappe 1 · Informationen finden und ordnen

**Ziel (Kind):** Ich kann ein Tier genau betrachten und Sachangaben aus Bild und Interview ordnen.

**Input und Merkblatt 1 – Abschnitte (identisch):**

1. **Finde den Fisch**
   - _Schau genau hin:_ Im Aquarium schwimmen vier Fische: A, B, C und D.
   - _Beschreibung 1:_ *Der Fisch hat einen langen, schmalen Körper. Auf dem Körper sind dunkle Punkte.*
   - _Beschreibung 2:_ *Der Fisch ist schön und schwimmt im Wasser.*
   - _Frage:_ Welche Beschreibung passt nur zu einem Fisch? Zeige den Hinweis, der dir hilft. Mache Beschreibung 2 genauer.
   - _Gesicherte Antwort:_ Beschreibung 1 passt nur zu Fisch B: langer, schmaler Körper und dunkle Punkte. Beschreibung 2 passt zu allen Fischen. Genauer ist zum Beispiel: *Der Fisch hat einen runden Körper mit dunklen Streifen.* Das ist Fisch A.
2. **Genau statt wertend**
   - _Dein Ziel:_ Genaue Angaben helfen anderen, sich das Tier vorzustellen.
   - _Vergleiche:_ A: *Der Fischotter ist toll. Sein Fell ist schön.* / B: *Der Fischotter hat einen langen Körper und kurze Beine. Sein Fell ist oben dunkelbraun.*
   - _Frage:_ Welcher Text hilft dir beim Vorstellen? Warum?
   - _Gesicherte Antwort:_ B nennt Körperform, Beine und Fellfarbe. „schön“ und „toll“ sind Meinungen, keine Merkmale.
3. **Das zeigt dir das Foto**
   - _Beobachte:_ Zeige zwei Körperteile. Nenne jeweils ein genaues Merkmal.
   - _Gesicherte Antwort:_ An der Schnauze sitzen lange **Tasthaare**. Die Ohren sind klein. Zeige die passenden Bildstellen.
   - _Grenze des Bildes:_ **Schwimmhäute** und die gesamte **Körperlänge** erkennst du hier nicht sicher. Erfinde keine verdeckten Merkmale.
4. **Das erfährst du im Interview**
   - _So liest du:_ 1. Lies das Interview einmal. Markiere Wörter, die du nicht verstehst. / 2. Kläre sie mit der Wörterhilfe oder frage nach. Rate nicht. / 3. Suche mit Suchwörtern: *leben, fressen, Zentimeter*. Markiere **L** (Lebensraum), **N** (Nahrung), **M** (Maß). / 4. Notiere ein Stichwort und die Zeile.
   - _Lies gezielt:_ **Wie groß ist Otto?** / *Von der Nase bis zum Schwanzansatz waren es 80 Zentimeter. Fischotter sind meistens 60 bis 90 Zentimeter lang, wenn man den Schwanz nicht mitzählt.*
   - _Frage:_ Wie lang sind Fischotter? Zählt der Schwanz dazu? Für wen gelten die 80 Zentimeter?
   - _Gesicherte Antwort:_ Fischotter sind ohne Schwanz etwa 60–90 cm lang. Die 80 cm gelten nur für Otto.
   - _Mit einem Partner prüfen:_ Zeige deine Stelle und nenne die Zeile. Passt sie zur Frage? Bei verschiedenen Antworten prüft ihr gemeinsam.
5. **Was gehört in die Beschreibung?**
   - _Im Interview:_ Frau Berger erzählt viel. Nicht alles passt in eine Tierbeschreibung.
   - _Drei Prüffragen:_ 1. Gilt es für **alle Fischotter**? → **Sachangabe**, passt. / 2. Geht es nur um **Otto** oder den Zoo? → **Einzelfall**, passt nicht. / 3. Sagt jemand, wie er das Tier **findet**? → **Meinung**, passt nicht.
   - _Frage:_ Ordne zu: *Fischotter fressen Fische.* · *Otto bekommt einen Eimer voll.* · *Er ist der süßeste Otter!*
   - _Gesicherte Antwort:_ Sachangabe: Fische. Einzelfall: Ottos Eimer. Meinung: „der süßeste Otter“. Nur die Sachangabe passt.
6. **Sprachdetektiv**
   - _Vier Wortarten:_ **Nomen** benennen Tiere und Dinge: *Otter, Fell*. Du schreibst sie groß. / **Artikel** begleiten Nomen: *der Otter, das Fell*. / **Verben** sagen, was geschieht oder wie etwas ist: *schwimmt, ist*. / **Adjektive** beschreiben Merkmale: *braun, dicht*.
   - _Wörter zerlegen:_ *der Körper + die Länge = die Körperlänge* / Das letzte Nomen bestimmt den Artikel.
   - _Frage:_ „Der Otter schwimmt.“ Welche Wortarten findest du?
   - _Gesicherte Antwort:_ *Der*: Artikel; *Otter*: Nomen; *schwimmt*: Verb.
7. **Informationen ordnen**
   - _Beispiel: nur Sachangaben, geordnet:_ **Überblick:** Fischotter; ohne Schwanz 60–90 cm / **Aussehen:** langer, schmaler Körper; kurze Beine; dunkelbraunes Fell oben / **Lebensraum:** Flüsse und Seen; Ufer mit Verstecken / **Nahrung:** vor allem Fische; Frösche, Krebse
   - _Frage:_ Wohin gehört „breiter, flacher Kopf“?
   - _Gesicherte Antwort:_ Unter Aussehen. Zeige, ob du die Angabe im Bild oder im Interview gefunden hast.

**Abschlusssatz:** Bearbeite Blatt 1–4 mit dem Fischotter-Interview. Vertiefungen sind freiwillig. Danach zeigst du dein Können im Gelingensnachweis. Vier von fünf Zielen reichen für Etappe 2.

**Materialbasis:** Fotoseite + Interview fischotter (Text siehe 8.0; Paket: erst Material, dann Blätter)

**Pflichtblätter:**

- **Blatt 1 · Welche Beschreibung hilft?** (Du brauchst: Heft · Merkblatt 1)
  - Lies: A: *Der Fischotter ist toll. Sein Fell ist schön.* / B: *Der Fischotter hat einen langen Körper und kurze Beine. Sein Fell ist oben dunkelbraun.*
  - Pflicht: Schreibe A oder B ins Heft. Welcher Text hilft dir, das Tier vorzustellen? Begründe. | Notiere zwei genaue Angaben aus Text B. Erkläre: Warum hilft „toll“ beim Beschreiben wenig?
  - Pflicht – Sprachdetektiv: Schreibe den Satz ins Heft: *„Der Fischotter hat einen langen Körper.“* Schreibe **N** über die Nomen und **A** über die Artikel.
  - Freiwillige Vertiefung: Ersetze *„Der Fischotter hat schöne Beine“* durch eine genaue Angabe aus dem Interview. Erkläre den Unterschied.
  - Kiosk-Tipp: Welcher Text sagt dir, wie der Fischotter aussieht? Suche Wörter für Form, Länge und Farbe.
  - Kiosk-Lösung (Lösung und Vergleich): Aufgabe 1: Text B hilft. Er nennt Körperform, Beinlänge und Fellfarbe. Text A enthält nur Meinungen. /  / Aufgabe 2 – zwei genaue Angaben, zum Beispiel: langer Körper; kurze Beine; Fell oben dunkelbraun. / „toll“ sagt nur, wie jemand das Tier findet. Damit kannst du dir das Tier nicht vorstellen. /  / Sprachdetektiv: / A (Artikel): Der, einen / N (Nomen): Fischotter, Körper
  - Kiosk-Vertiefung: Beispiel: „Der Fischotter hat kurze Beine.“ (Interview, Z. 19–20) / „schön“ ist eine Meinung. „kurz“ kannst du im Interview und am Foto prüfen.
- **Blatt 2 · Schau genau hin** (Du brauchst: Fischotter-Foto · Heft · Bleistift)
  - Pflicht: Betrachte das Foto. Notiere im Heft zwei sichtbare Körperteile. Ergänze zu jedem ein genaues Merkmal. | Bilde daraus zwei vollständige Sätze. | Zeige einem anderen Kind oder der Lehrkraft beide Bildstellen. Prüfe: Passen deine Sätze zum Foto?
  - Pflicht – Sprachdetektiv: Markiere in einem deiner Sätze ein Adjektiv mit **Adj**. Schreibe das Nomen dazu, das es genauer beschreibt.
  - Freiwillige Vertiefung: Beschreibe zwei sichtbare Merkmale noch genauer. Prüfe am Foto: Was kannst du sicher sagen? Erfinde keine verdeckten Teile.
  - Achte darauf: Eine Farbe, Form oder Größe macht die Angabe genauer: nicht nur „Ohren“, sondern „kleine Ohren“.
  - Kiosk-Tipp: Schau auf Kopf und Gesicht. Was siehst du an der Schnauze? Wie groß sind die Ohren?
  - Kiosk-Lösung (Lösung und Vergleich): Aufgabe 1 – Beispiele: / Schnauze: lange Tasthaare / Ohren: klein / Kopf: breit und flach /  / Aufgabe 2 – Beispiele: / „An der Schnauze sitzen lange Tasthaare.“ / „Die Ohren sind klein.“ /  / Aufgabe 3: Zeige beide Stellen auf dem Foto. Andere sichtbare Merkmale sind auch richtig. /  / Sprachdetektiv – Beispiel: „lange“ (Adj) beschreibt das Nomen „Tasthaare“.
  - Kiosk-Vertiefung: Beispiel: „An der Schnauze sitzen viele lange Tasthaare. Sie stehen zur Seite ab.“ / Sicher sagen kannst du nur, was du siehst. Schwimmhäute und die ganze Körperlänge erkennst du auf dem Foto nicht.
- **Blatt 3 · Im Interview suchen** (Du brauchst: Fischotter-Interview · Fischotter-Foto · Merkblatt 1 · Heft)
  - Pflicht: Lies das Interview mit den Leseschritten von Merkblatt 1. Notiere: / a) Wo leben Fischotter? / b) Was fressen sie vor allem? / c) Wie lang sind Fischotter ohne Schwanz? Nenne die Einheit. | Markiere die Stellen im Interview: **L** für Lebensraum, **N** für Nahrung, **M** für Maß. Schreibe die Zeile hinter deine Antwort, zum Beispiel „Z. 12“. | Im Interview stehen zwei Längen. Welche gilt für alle Fischotter? Welche gilt nur für Otto? Begründe. | Partnercheck: Zeige einem anderen Kind deine Stellen. Passt die Stelle zur Frage? Prüft Unterschiede gemeinsam. | Notiere ein sichtbares Merkmal mit „Bild“. Zeige die Bildstelle. Steht es auch im Interview?
  - Pflicht – Sprachdetektiv: Unterstreiche im Interview zwei Verben. Schreibe **V** darüber.
  - Freiwillige Vertiefung: Suche im Interview zwei Stellen, die nur Otto betreffen. Erkläre, warum sie nicht in eine Tierbeschreibung gehören.
  - Kiosk-Tipp: Nutze die Leseschritte. Suche im Interview die Wörter „leben“, „fressen“ und „Zentimeter“. Lies auch den Satz danach. Die Zeilennummern stehen am Rand.
  - Kiosk-Lösung (Lösung und Vergleich): Aufgabe 1: / a) an Flüssen und Seen; Ufer, an denen sie sich verstecken können (Z. 11–12) / b) vor allem Fische, auch Frösche und Krebse (Z. 7–8) / c) etwa 60 bis 90 Zentimeter ohne Schwanz (Z. 28–29) /  / Aufgabe 2: L bei Z. 11–12 · N bei Z. 7–8 · M bei Z. 28–29. /  / Aufgabe 3: „60 bis 90 Zentimeter“ gilt für alle Fischotter. „80 Zentimeter“ gilt nur für Otto (Z. 26–27). Otto wurde gemessen – das ist ein Einzelfall. /  / Aufgabe 4: Habt ihr verschiedene Stellen markiert? Lest die Frage noch einmal und prüft gemeinsam. /  / Aufgabe 5 – Beispiel: „lange Tasthaare (Bild)“. Das steht auch im Interview (Z. 35). Auch richtig: „kleine Ohren (Bild)“ – steht in Z. 23. /  / Sprachdetektiv – Verben, zum Beispiel: mache, gibt, fressen, leben, brauchen, ist, sind.
  - Kiosk-Vertiefung: Zum Beispiel: „Otto wartet am Gitter und pfeift.“ (Z. 3) und „Otto bekommt jeden Tag einen kleinen Eimer voll.“ (Z. 6) / Das gilt nur für Otto im Zoo. Eine Tierbeschreibung erklärt, wie alle Fischotter sind.
- **Blatt 4 · Informationen ordnen** (Du brauchst: Fischotter-Interview · Heft)
  - Pflicht: Schreibe ins Heft: Überblick · Aussehen · Lebensraum · Nahrung. | Ordne die Angaben zu. Drei Angaben passen nicht in eine Tierbeschreibung. Streiche sie. / *Fischotter · kurze Beine · Otto bekommt einen Eimer Fisch · Fische · Flüsse und Seen · der süßeste Otter der Welt · ohne Schwanz 60–90 cm · dunkelbraunes Fell oben · Otto ist 80 cm lang · Frösche und Krebse · Ufer mit Verstecken* | Suche im Interview drei weitere Angaben zum Aussehen. Schreibe die Zeile dazu. Hast du jetzt vier verschiedene Merkmale?
  - Pflicht – Sprachdetektiv: Zerlege „Körperlänge“ im Heft in zwei Nomen. Schreibe beide mit Artikel auf. Ergänze den Artikel zu „Körperlänge“.
  - Freiwillige Vertiefung: Ordne deine Angaben zum Aussehen in einer anderen sinnvollen Reihenfolge. Erkläre deine Wahl.
  - Kiosk-Tipp: Frage bei jeder Angabe zuerst: Gilt das für alle Fischotter? Wenn nicht: streichen. Dann: Aussehen, Wohnort oder Futter? Tiername und Maß gehören zum Überblick.
  - Kiosk-Lösung (Lösung und Vergleich): Aufgabe 2: / Überblick: Fischotter; ohne Schwanz 60–90 cm / Aussehen: kurze Beine; dunkelbraunes Fell oben / Lebensraum: Flüsse und Seen; Ufer mit Verstecken / Nahrung: Fische; Frösche und Krebse / Gestrichen: „Otto bekommt einen Eimer Fisch“ und „Otto ist 80 cm lang“ (Einzelfall), „der süßeste Otter der Welt“ (Meinung). /  / Aufgabe 3 – zum Beispiel: langer, schmaler Körper (Z. 18–19); breiter, flacher Kopf (Z. 20); kleine Ohren (Z. 23); dichtes Fell (Z. 32); lange Tasthaare (Z. 35); Schwimmhäute zwischen den Zehen (Z. 36–37). /  / Sprachdetektiv: der Körper + die Länge = die Körperlänge
  - Kiosk-Vertiefung: Zum Beispiel von oben nach unten: Kopf, Körper, Beine, Fell. Oder vom großen zum kleinen Merkmal. / Erkläre, warum deine Reihenfolge beim Vorstellen hilft. Mehrere Reihenfolgen sind richtig.

**Gelingensnachweis 1 „Tierdetektiv“ (Varianten A, B)** – 4 von 5 Indikatoren:

| ID | Kind-Formulierung | erreicht, wenn | Übe mit |
|---|---|---|---|
| E1.1 | Ich nenne zwei verschiedene äußere Merkmale genau. | zwei verschiedene äußere Merkmale richtig und genau benannt | Blatt 2 |
| E1.2 | Ich zeige, was im Bild und was im Interview steht. | je ein Beleg aus Bild und Interview (mit Zeile) | Blatt 3 |
| E1.3 | Ich gebe an, wie lang Fischotter sind – mit Einheit. | 60–90 cm ohne Schwanz, mit Einheit; Ottos 80 cm als Einzelfall erkannt | Blatt 3 |
| E1.4 | Ich finde Lebensraum und Nahrung im Interview. | beides richtig eingeordnet, mit Zeile | Blatt 3–4 |
| E1.5 | Ich erkenne Sachangabe, Einzelfall und Meinung. | 4 von 5 Aussagen richtig | Blatt 3–4 |

Aufgaben: 1) Merkmale und Quellen: Notiere zwei verschiedene äußere Merkmale: eines aus dem Bild, eines aus dem Interview. Schreibe die Zeile dazu. · 2) Das Maß: Im Interview stehen zwei Längen. Notiere, wie lang Fischotter sind. Kreuze an, für wen die 80 cm gelten. · 3) Was gehört in die Beschreibung?: Kreuze an: Gilt die Aussage für alle Fischotter (Sachangabe), nur für Otto oder ist sie eine Meinung? · 4) Lebensraum und Nahrung: Notiere unter jeder Überschrift eine Sachangabe aus dem Interview. Schreibe die Zeile dazu.

- Variante A Interviewauszug (S. 1, Zeilennummern): **Wo leben Fischotter?** [[In der Natur leben Fischotter an Flüssen und Seen. Sie brauchen Ufer mit vielen Verstecken.|L]] [[Unser Otto hat dafür eine Höhle aus alten Wurzeln.|X]] **Was frisst Otto?** [[Jeden Morgen bekommt er einen Eimer Fisch.|X]] [[Fischotter fressen vor allem Fische, aber auch Frösche und Krebse.|N]] **Wie sieht ein Fischotter aus?** [[Sein Körper ist lang und schmal, die Beine sind kurz.|A]] [[Das Fell ist oben dunkelbraun und sehr dicht.|A]] [[Ich finde, Otto hat das schönste Fell im ganzen Zoo!|W]] **Und am Kopf?** [[Der Kopf ist breit und flach.|A]] [[Die Ohren sind ganz klein.|A]] **Wie groß ist Otto?** [[Letzte Woche haben wir ihn gemessen: 80 Zentimeter ohne Schwanz.|X]] [[Fischotter sind meistens 60 bis 90 Zentimeter lang, ohne Schwanz.|M]]
  - Einordnen (Sachangabe/nur Otto/Meinung): Fischotter fressen vor allem Fische. → Sachangabe; Otto hat eine Höhle aus alten Wurzeln. → nur Otto; Otto hat das schönste Fell im ganzen Zoo. → Meinung; Die Ohren sind ganz klein. → Sachangabe; Jeden Morgen bekommt Otto einen Eimer Fisch. → nur Otto

- Variante B Interviewauszug (S. 1, Zeilennummern): **Frau Berger, was macht Otto gerade?** [[Er schwimmt seine Runden. Das macht er jeden Mittag.|X]] [[Zwischen den Zehen hat er Schwimmhäute.|A]] [[Ich finde, er ist der beste Schwimmer der Welt!|W]] **Wo leben Fischotter sonst?** [[An Flüssen und Seen.|L]] [[Am Ufer verstecken sie sich unter Büschen und Wurzeln.|L]] **Was fressen sie?** [[Hauptsächlich Fische. Frösche und Krebse fangen sie auch.|N]] [[Otto mag am liebsten Forellen.|X]] **Woran erkennt man einen Fischotter?** [[An der Schnauze hat er lange Tasthaare.|A]] [[Der Körper ist lang, die Beine sind kurz.|A]] **Wie lang ist Otto?** [[Otto ist 80 Zentimeter lang, ohne Schwanz.|X]] [[Bei Fischottern sind es meistens 60 bis 90 Zentimeter. Der Schwanz kommt noch dazu.|M]]
  - Einordnen (Sachangabe/nur Otto/Meinung): Fischotter leben an Flüssen und Seen. → Sachangabe; Otto mag am liebsten Forellen. → nur Otto; Otto ist der beste Schwimmer der Welt. → Meinung; An der Schnauze hat er lange Tasthaare. → Sachangabe; Otto schwimmt jeden Mittag seine Runden. → nur Otto

### Etappe 2 · Sachlich und genau formulieren

**Ziel (Kind):** Ich kann genaue Wörter nutzen und verständliche Sätze im Präsens schreiben.

**Input und Merkblatt 2 – Abschnitte (identisch):**

1. **Genau statt wertend**
   - _Sachlich beschreiben:_ Beschreibe überprüfbare Merkmale. „schön“ und „süß“ sagen nur, wie jemand etwas findet. Nutze Angaben aus dem Interview.
   - _Genaue Wörter wählen:_ Nutze genaue Nomen, Verben und Adjektive. / *„Das Tier bewegt sich im Wasser.“* wird genauer: *„Der Fischotter schwimmt im Wasser.“* / *„Sein Fell ist oben dunkelbraun.“* ist ebenfalls genau. Du musst „ist“ nicht immer ersetzen.
   - _Wörter zusammensetzen:_ Aus *Fell* und *Farbe* wird die *Fellfarbe*. Das letzte Wort bestimmt den Artikel: *die Farbe → die Fellfarbe*. **Fachwörter** benennen etwas genau. Kläre ihre Bedeutung.
   - _Die Wörterhilfe:_ Auf der Wörterhilfe findest du genaue Wörter für Körperteile. Wähle nur Wörter, die zu deinem Tier passen. Prüfe am Bild oder im Interview.
   - _Frage:_ Was ist genauer: „schönes Fell“ oder „oben dunkelbraunes Fell“?
   - _Gesicherte Antwort:_ „oben dunkelbraunes Fell“. Die Farbe ist überprüfbar.
2. **Aus Interview-Sprache wird Sachsprache**
   - _Im Interview:_ Frau Berger spricht mit uns. Sie sagt *ich* und *unser Otto*, sie vergleicht und sagt ihre Meinung. Im Sachtext schreibst du über **alle Fischotter**, im **Präsens** und **ohne Meinung**.
   - _Beispiel:_ Interview: *„Sein Körper ist lang und schmal, fast wie ein Torpedo.“* / Sachtext: *Der Fischotter hat einen langen, schmalen Körper.*
   - _Frage:_ Mache sachlich: *„Und der Kopf ist breit und flach. Ich sage immer: wie ein Brett mit Nase.“*
   - _Gesicherte Antwort:_ *Der Kopf des Fischotters ist breit und flach.* Den Vergleich und „Ich sage immer“ lässt du weg.
3. **Fische genau beschreiben**
   - _Ungenau:_ *„Der Fisch ist hübsch.“* Welcher Fisch ist gemeint? Das weiß niemand.
   - _Genau:_ *„Der Fisch hat einen kleinen Körper und eine sehr große Schwanzflosse.“* Das ist Fisch D.
   - _Rätsel mit einem Partner:_ Beschreibe einen Fisch mit zwei genauen Merkmalen. Verrate nicht, welchen du meinst. Dein Partner zeigt auf den passenden Fisch.
   - _Frage:_ Verbessere: „Der Fisch sieht cool aus.“ Nenne ein genaues Merkmal, damit man den Fisch erkennt.
   - _Gesicherte Antwort:_ Zum Beispiel: *„Der Fisch hat lange Flossen oben und unten.“* Das ist Fisch C. Andere genaue Merkmale sind auch richtig.
4. **Im Präsens beschreiben**
   - _Warum Präsens?:_ Tierbeschreibungen sagen, was allgemein für ein Tier gilt. Deshalb stehen sie meistens im **Präsens**, der Gegenwart: *Der Fischotter lebt an Gewässern.*
   - _Grundform und gebeugte Form:_ Im Wörterbuch steht die **Grundform**: *leben, fressen, sein*. / Im Satz beugst du das Verb passend: / *leben → er lebt* / *fressen → er frisst* / *sein → sein Fell ist dicht.*
   - _Subjekt und Verb:_ Das **Subjekt** ist der Satzgegenstand. Frage: Wer oder was schwimmt? / *Der Otter schwimmt. Die Otter schwimmen.*
   - _Frage:_ Was ändert sich?
   - _Gesicherte Antwort:_ Bei mehreren Ottern heißt das Verb „schwimmen“ statt „schwimmt“.
5. **Vollständige Sätze**
   - _Ein vollständiger Satz:_ Verbinde die Angaben zu einem verständlichen Satz. Achte darauf, dass Subjekt und Verb zusammenpassen: *Der Fischotter lebt. Die Fischotter leben.*
   - _Beispiel:_ Wortgruppe: *sein Fell – oben dunkelbraun – sein* / Satz: *Sein Fell ist oben dunkelbraun.* / Der Satz ist vollständig und verständlich.
   - _Frage:_ Was fehlt bei „Der Fischotter an einem See“?
   - _Gesicherte Antwort:_ Das Verb. Vollständig heißt es: *Der Fischotter lebt an einem See.*
6. **Sätze prüfen**
   - _Prüfe jeden Satz:_ Passt die Aussage zum Interview? Gilt sie für alle Tiere? / Ist der Satz vollständig? / Steht das Verb im Präsens und passt es? / Sind die Wörter genau? / Beginnen Satz und Nomen groß? / Steht am Ende ein Punkt?
   - _Beispiel verbessern:_ *„sein fell war schön“* wird zu: *„Sein Fell ist oben dunkelbraun.“* Die Angabe stammt aus dem Interview.

**Abschlusssatz:** Bearbeite die Pflichtaufgaben auf Blatt 5 und 6 mit dem Fischotter-Interview. Vertiefungen sind freiwillig. Im Gelingensnachweis bildest du drei Sätze und machst aus einer Meinung einen sachlichen Satz. Bei vier von fünf Zielen gehst du weiter zu Etappe 3.

**Materialbasis:** Interview fischotter (Text siehe 8.0; Paket: erst Material, dann Blätter)

**Pflichtblätter:**

- **Blatt 5 · Treffende Wörter** (Du brauchst: Fischotter-Interview · Heft · Merkblatt 2 · Wörterhilfe)
  - Aus dem Interview: *„Sein Körper ist lang und schmal, fast wie ein Torpedo.“* / *„Deshalb ist er so ein toller Schwimmer.“* / **Tasthaare:** Haare zum Ertasten. **Schwimmhäute:** Haut zwischen den Zehen.
  - Pflicht – Schreibe ins Heft: Ersetze „schönes Fell“ und „toller Kopf“ durch genaue Angaben aus dem Interview. Schreibe die Zeile dazu. | Mache den Torpedo-Satz sachlich: Schreibe über den Körper des Fischotters ohne Vergleich. | „toller Schwimmer“ ist eine Meinung. Was hat der Fischotter zum Schwimmen? Schreibe einen sachlichen Satz. | Bilde Wörter mit Artikel: *Tast + Haare*; *Schwimm + Häute*. Erkläre beide mit der Wörterhilfe.
  - Freiwillige Vertiefung – Vertiefung: Schau dir das Aquarium auf Merkblatt 2 an. Verbessere: *„Der Fisch ist lustig.“* Nenne ein genaues Merkmal, damit man den Fisch erkennt. Schreibe einen ganzen Satz im Präsens.
  - Kiosk-Tipp: Suche im Interview die Stellen zu Fell (Z. 32–33) und Kopf (Z. 20). Was hat der Fischotter zwischen den Zehen (Z. 36–37)?
  - Kiosk-Lösung (Lösung und Vergleich): Aufgabe 1: „oben dunkelbraunes Fell“ (Z. 32–33) und „breiter, flacher Kopf“ (Z. 20) /  / Aufgabe 2: „Der Fischotter hat einen langen, schmalen Körper.“ Der Vergleich mit dem Torpedo fällt weg. /  / Aufgabe 3: „Der Fischotter hat Schwimmhäute zwischen den Zehen.“ „toll“ fällt weg. /  / Aufgabe 4: / die Tasthaare: Haare zum Ertasten / die Schwimmhäute: Haut zwischen den Zehen
  - Kiosk-Vertiefung: Zum Beispiel: „Der Fisch hat einen runden Körper mit dunklen Streifen.“ Das ist Fisch A. / Oder: „Der Fisch hat einen langen, schmalen Körper mit dunklen Punkten.“ Das ist Fisch B. / Wichtig: Das Merkmal passt nur zu einem Fisch.
- **Blatt 6 · Sachliche Sätze** (Du brauchst: Fischotter-Interview · Heft · Merkblatt 2)
  - Pflicht – Aus dem Interview wird ein Sachsatz: Schreibe aus jeder Stelle einen vollständigen, sachlichen Satz im Präsens über den Fischotter: *„Die Beine sind dagegen richtig kurz.“* | *„Sie fangen aber auch Frösche und Krebse.“* | *„Die sind ganz klein.“* (Gemeint sind die Ohren.)
  - Pflicht – Verbessern und prüfen: Verbessere: *„der fischotter lebte an schönen ufern“*. / Im Interview: *„Sie brauchen Ufer, an denen sie sich verstecken können.“* Prüfe alle vier Sätze mit Merkblatt 2. Achte auch auf große Satzanfänge und Nomen sowie Punkte.
  - Pflicht – Verben untersuchen: Unterstreiche im Heft die Verben in deinen vier Sätzen. Schreibe zu „frisst“ die Grundform. | Schreibe Satz 2 noch einmal für mehrere Fischotter. Passe das Verb an.
  - Freiwillige Vertiefung – Vertiefung: Verbinde zwei deiner Sätze mit „und“. Erkläre, warum das Präsens zu einer Tierbeschreibung passt.
  - Kiosk-Tipp: Schreibe immer „Der Fischotter …“ oder „Fischotter …“. Lass „dagegen“, „aber“ und „ganz“ weg, wenn sie nichts Genaues sagen. Das Verb passt zum Subjekt: er frisst, die Beine sind.
  - Kiosk-Lösung (Lösung und Vergleich): 1. Der Fischotter hat kurze Beine. / Seine Beine sind kurz. / 2. Der Fischotter frisst auch Frösche und Krebse. / 3. Der Fischotter hat kleine Ohren. / 4. Der Fischotter lebt an Ufern, an denen er sich verstecken kann. /  / 5. Verben, zum Beispiel: hat, frisst, lebt. Grundform von „frisst“: fressen. / 6. Die Fischotter fressen auch Frösche und Krebse. /  / Andere Reihenfolgen im Satz sind richtig, wenn der Satz vollständig und sachlich ist.
  - Kiosk-Vertiefung: Beispiel: „Der Fischotter hat kurze Beine und frisst auch Krebse.“ / Das Präsens passt, weil die Beschreibung sagt, was allgemein für den Fischotter gilt.
- **Hilfekarte Wörterhilfe · Genaue Wörter für dein Tier** – Hinweis: Wähle nur Wörter, die zu deinem Tier passen. Prüfe die Angabe am Bild oder im Text. Tabelle: der Kopf: breit, schmal, flach, rund; die Schnauze: lang, kurz, spitz, breit; die Ohren: klein, groß, rund, spitz; das Fell: dicht, glatt, dunkelbraun, graubraun, gestreift, gefleckt; der Körper: lang gestreckt, schlank, kräftig; der Schwanz: lang, kurz, buschig, schmal, geringelt; die Beine / die Pfoten: kurz, lang, kräftig. Fachwörter: die Tasthaare: Haare zum Ertasten / die Schwimmhäute: Haut zwischen den Zehen / die Krallen: spitze Nägel an den Zehen / der Rumpf: Körper ohne Kopf, Beine und Schwanz. Genaue Verben: er lebt · er frisst · er schwimmt · er klettert · er gräbt · er hat · er ist.

**Gelingensnachweis 2 „Genaue Sätze“ (Varianten A, B)** – 4 von 5 Indikatoren:

| ID | Kind-Formulierung | erreicht, wenn | Übe mit |
|---|---|---|---|
| E2.1 | Meine Sätze passen zum Interview und gelten für alle Fischotter. | alle vier Aussagen stimmen mit dem Interview überein; kein Einzelfall über Otto | Blatt 5 |
| E2.2 | Ich schreibe vollständige, verständliche Sätze. | alle vier Aussagen als vollständige, verständliche Sätze formuliert | Blatt 6 |
| E2.3 | Meine Verben stehen im Präsens und passen zum Subjekt. | Verben im Präsens und passend zum Subjekt (auch bei Vergangenheit im Interview) | Blatt 6 |
| E2.4 | Ich mache aus einer Meinung eine genaue Sachangabe. | Meinung weggelassen, genaue Angabe aus dem Interview gefunden und verwendet | Blatt 5 |
| E2.5 | Ich schreibe Satzanfänge und Nomen groß und setze Punkte. | Satzanfänge und Nomen groß sowie Satzschlusspunkte in den vier Sätzen | Blatt 6 |

Aufgaben: 1) Aus dem Interview wird ein Sachsatz: Schreibe für das Tierlexikon je einen sachlichen Satz im Präsens über **den Fischotter**. Die Angaben findest du im Interview. · 2) Aus einer Meinung wird ein Sachsatz: Das sagt Frau Berger. Suche im Interview die genaue Angabe. Schreibe daraus einen sachlichen Satz.

- Variante A Interviewauszug (S. 1, Zeilennummern): **Wie geht es Otto heute?** [[Er ist gerade aus dem Wasser gekommen.|X]] [[Sein Fell ist oben dunkelbraun und am Hals heller.|A]] [[Die Beine sind dagegen richtig kurz.|A]] [[Ehrlich gesagt hat er die süßesten Beine der Welt!|W]] **Was hat er gestern gefressen?** [[Gestern hat er drei Fische und einen Krebs gefressen.|X]] [[In der Natur fressen Fischotter vor allem Fische.|N]] **Wo leben Fischotter?** [[Sie leben an Flüssen und Seen.|L]] [[Dort brauchen sie Ufer mit Verstecken.|L]] **Und der Kopf?** [[Der Kopf ist breit und flach,|A]] [[fast wie ein Brett.|V]]
  - Sachsätze zu: zum Lebensraum, zur Nahrung, zum Kopf; Meinung umformen: „Ehrlich gesagt hat er die süßesten Beine der Welt!“

- Variante B Interviewauszug (S. 1, Zeilennummern): **Was macht Otto am liebsten?** [[Er taucht nach Fischen.|X]] [[Fischotter haben dafür Schwimmhäute zwischen den Zehen.|A]] [[Mit den langen Tasthaaren spüren sie Fische auch im trüben Wasser.|A]] **Was frisst ein Fischotter?** [[Vor allem Fische. Er frisst aber auch Frösche.|N]] [[Letzte Woche hat Otto sogar eine Ente erschreckt!|X]] **Wo wohnt er in der Natur?** [[An Flüssen und Seen mit geschützten Ufern.|L]] **Wie sieht er aus?** [[Sein Körper ist lang und schmal.|A]] [[Ich finde, der Kopf ist total toll.|W]] [[Er ist breit und flach.|A]]
  - Sachsätze zu: zur Nahrung, zum Lebensraum, zu den Zehen; Meinung umformen: „Ich finde, der Kopf ist total toll.“

### Etappe 3 · Eine Tierbeschreibung schreiben und prüfen

**Ziel (Kind):** Ich kann aus einem Interview eine sachliche, geordnete und verständliche Tierbeschreibung schreiben.

**Input und Merkblatt 3 – Abschnitte (identisch):**

1. **Vom Interview zum Plan**
   - _Dein Ziel:_ Ich kann aus einem Interview eine sachliche, geordnete und verständliche Tierbeschreibung schreiben.
   - _Markieren und streichen:_ Markiere im Interview Sachangaben über **die Tierart**. Streiche Meinungen, Erlebnisse und Angaben nur über **das Zootier**. Aus einem Vergleich nimmst du nur die Sachangabe.
   - _Ein Plan in Stichwörtern:_ **Überblick:** Fischotter; Marder; ohne Schwanz etwa 60–90 cm / **Aussehen:** langer, schmaler Körper; kurze Beine; oben dunkelbraunes Fell; breiter, flacher Kopf / **Lebensraum:** Flüsse und Seen; Ufer mit Verstecken / **Nahrung:** vor allem Fische, auch Frösche und Krebse
   - _Frage:_ Gehört „Otto ist 80 Zentimeter lang“ in den Plan?
   - _Gesicherte Antwort:_ Nein. Das gilt nur für Otto. In den Plan gehört das Maß der Art: ohne Schwanz etwa 60–90 cm.
2. **Aus Stichwörtern wird Text**
   - _Vom Plan zum Satz:_ Stichwörter: *Kopf – breit, flach* / Satz: *Sein Kopf ist breit und flach.* / Nutze vollständige Sätze im Präsens. Schreibe sachlich und verbinde zusammengehörige Angaben.
   - _Ein vollständiges Beispiel:_ **Der Fischotter** / *Der Fischotter gehört zu den Mardern. Er hat einen langen, schmalen Körper. Ohne Schwanz ist er etwa 60 bis 90 Zentimeter lang. Seine Beine sind kurz. Sein Fell ist oben dunkelbraun. Der Kopf ist breit und flach.* / *Er lebt an Flüssen und Seen. Dort braucht er Ufer mit Verstecken. Er frisst vor allem Fische, aber auch Frösche und Krebse.*
3. **Mit Kriterien prüfen**
   - _K1 · Informationen:_ Tiername, Maß der Art mit Einheit und Bezug, Lebensraum und Nahrung sind richtig im Text. Angaben nur über das Zootier gehören nicht hinein.
   - _K2 · Aussehen:_ Mindestens vier verschiedene äußere Merkmale sind genau beschrieben. Wiederholungen desselben Merkmals zählen nicht doppelt.
   - _K3 · Aufbau:_ Beginne mit Tiername und Überblick, etwa Körperform oder Maß. Ordne zusammengehörige Informationen. Absätze helfen.
   - _K4 und K5 · Sprache:_ Schreibe sachlich und im Präsens, ohne Meinungen aus dem Interview. Nutze genaue Wörter. Verbinde vollständige, verständliche Sätze zu einem Text.
4. **Prüfen und überarbeiten**
   - _K6 · Schreibung:_ Prüfe Satzanfänge, Nomen und Satzschlüsse. Vergleiche schwierige Tierwörter mit dem Interview. / **Zeige deine Prüfung:** Kreise einen Satzanfang ein, unterstreiche zwei Nomen und markiere einen Satzschlusspunkt.
   - _Ein Beispiel prüfen:_ *„sein kopf ist breit und flach“* wird zu: *„Sein Kopf ist breit und flach.“* / Groß: *Sein, Kopf*. Am Ende steht ein Punkt.
   - _Frage:_ Muss ein richtiger Satz verändert werden?
   - _Gesicherte Antwort:_ Nein. Zeige die Prüfung und begründe: „Mein Satz bleibt, weil …“

**Abschlusssatz:** Bearbeite die Pflichtaufgaben auf Blatt 7–9 mit einem Interview. Vertiefungen sind freiwillig. Dein Abschluss ist die Probearbeit, dein letzter Gelingensnachweis. Vier von fünf Zielen = 80 %. Danach bekommst du Feedback für deinen nächsten Schritt.

**Materialbasis:** Interview erdmaennchen, Interview roter-panda (Text siehe 8.0; Paket: erst Material, dann Blätter)

**Pflichtblätter:**

- **Blatt 7 · Dein Schreibplan** (Du brauchst: Merkblatt 3 · Interview zum Erdmännchen oder Roten Panda · Heft. Wähle ein Tier. Bleibe auf Blatt 7–9 bei diesem Tier.)
  - Pflicht – Plane im Heft: Lies das Interview zu deinem Tier. Markiere Sachangaben über die Tierart. Streiche Meinungen und Angaben, die nur das Zootier betreffen. | Schreibe diese Überschriften: Überblick · Aussehen · Lebensraum · Nahrung. | Ordne Stichwörter zu: Tiername, das Maß der Art mit Einheit und Bezug, vier verschiedene äußere Merkmale, Lebensraum und Nahrung. Notiere die Zeile. | Prüfe jede Angabe: Gilt sie für alle Tiere dieser Art? Zeige eine Bildstelle und eine Interviewstelle.
  - Freiwillige Vertiefung – Vertiefung: Skizziere eine zweite sinnvolle Reihenfolge. Welche hilft dir besser beim Schreiben? Begründe kurz.
  - Kiosk-Tipp: Frage bei jedem Satz im Interview: Gilt das für alle Tiere dieser Art? Dann markieren. Geht es nur um Kiki oder Mei, oder sagt jemand seine Meinung? Dann streichen.
  - Kiosk-Lösung (Vergleichsplan): Erdmännchen / Überblick: Erdmännchen; gehört zu den Mangusten (Z. 17); Kopf und Rumpf etwa 25–29 cm, Schwanz zusätzlich (Z. 24–25) / Aussehen: schlanker Körper; hellbraunes bis graubraunes Fell; dunklere Streifen auf dem Rücken (Z. 28–29); spitze Schnauze; dunkle Flecken um die Augen (Z. 29–30); langer, schmaler Schwanz (Z. 7); lange Krallen (Z. 13–14) / Lebensraum: trockenes Gras- und Buschland im Süden von Afrika; Gänge unter der Erde (Z. 11–13) / Nahrung: vor allem Insekten, auch Spinnen und kleine Eidechsen (Z. 20–21) / Gestrichen zum Beispiel: Kiki ist die Mutigste; Mehlwürmer am Morgen; „Total cool, oder?“; „wie eine Sonnenbrille“. /  / Roter Panda / Überblick: Roter Panda, auch Kleiner Panda (Z. 6); Kopf und Rumpf etwa 60 cm, Schwanz zusätzlich (Z. 30–31) / Aussehen: Fell am Rücken rötlich braun; Beine und Bauch dunkel; helle Bereiche im Gesicht (Z. 19–21); runder Kopf; große, spitze Ohren (Z. 21–22); langer, buschiger Schwanz mit Ringen (Z. 25–26) / Lebensraum: Bergwälder in Asien mit Bambus (Z. 15) / Nahrung: hauptsächlich Bambus, auch Beeren und Eier (Z. 10–11) / Gestrichen zum Beispiel: Mei schläft in der Astgabel; Weintrauben; „sieht aus wie ein Kuscheltier“; „das hübscheste Tier“. /  / Du brauchst nur vier Merkmale. Andere Stichwörter sind richtig, wenn sie für alle Tiere der Art gelten.
  - Kiosk-Vertiefung: Zum Beispiel: erst Lebensraum und Nahrung, dann das Aussehen. Oder das Aussehen von oben nach unten. / Wichtig: Tiername und Überblick stehen am Anfang.
- **Blatt 8 · Deine Tierbeschreibung** (Du brauchst: deinen Plan von Blatt 7 · das gewählte Interview · Merkblatt 3 · Heft)
  - Pflicht – Schreibe im Heft: Schreibe eine passende Überschrift. | Schreibe aus deinem Plan einen zusammenhängenden Text. Beginne mit Tiername und Überblick. | Beschreibe vier verschiedene äußere Merkmale. Ergänze Maß mit Einheit und Bezug, Lebensraum und Nahrung. | Schreibe sachlich, im Präsens und in vollständigen Sätzen. Übernimm keine Meinung und kein Erlebnis aus dem Interview. Lies deinen Text einmal leise vor.
  - Freiwillige Vertiefung – Vertiefung: Verbessere zwei Satzanfänge oder Bezüge. Zeige: Welches Wort macht jetzt klarer, was gemeint ist?
  - Kiosk-Tipp: Mache aus jeder Zeile deines Plans einen ganzen Satz. Beginne mit „Das Erdmännchen …“ oder „Der Rote Panda …“. Schreibe nicht „Kiki“ oder „Mei“.
  - Kiosk-Lösung (Prüffragen und Teilbeispiele): Hier gibt es keine feste Lösung. Prüfe deinen Text: / Überschrift vorhanden? / Tiername und Überblick am Anfang? / Maß mit Einheit und Bezug? / Vier verschiedene äußere Merkmale? / Lebensraum und Nahrung? / Keine Meinung, kein Erlebnis aus dem Interview? / Präsens und ganze Sätze? /  / Teilbeispiel Erdmännchen: „Das Erdmännchen hat einen schlanken Körper. Kopf und Rumpf sind zusammen etwa 25 bis 29 Zentimeter lang. Der Schwanz kommt noch dazu.“ /  / Teilbeispiel Roter Panda: „Der Rote Panda lebt in Bergwäldern Asiens. Dort wächst Bambus.“
  - Kiosk-Vertiefung: Unklar: „Es ist lang und schmal.“ Was ist gemeint? / Klarer: „Der Schwanz ist lang und schmal.“ / Wenn „er“, „es“ oder „sein“ unklar ist, nenne das Nomen.
- **Blatt 9 · Prüfen und verbessern** (Du brauchst: deinen Text von Blatt 8 · das Interview · Checkliste K1–K6 · Rückmeldekarte)
  - Pflicht – Arbeite am Text: Prüfe deinen Text im Heft mit K1–K6. | Geh zur Haltestelle. Such dir ein Kind für eine Rückmeldung. Es liest deinen Text und nutzt die Rückmeldekarte. Lass dir die Textstelle zeigen. | Entscheide mit Interview und Checkliste, was du verbesserst. Schreibe nicht den ganzen Text neu. Ist eine Stelle schon richtig? Begründe, warum sie bleibt. | Zeige die Schreibprüfung: Kreise einen Satzanfang ein, unterstreiche zwei Nomen und markiere einen Punkt. Vergleiche Tierwörter mit dem Interview.
  - Freiwillige Vertiefung – Vertiefung: Zeige eine Stelle vorher und nachher. Erkläre, was durch deine Änderung besser geworden ist.
  - Kiosk-Tipp: An der Haltestelle hilft dir die Rückmeldekarte. Prüfe danach ein Kriterium nach dem anderen. Lies für K6 jeden Satz einzeln: Beginnt er groß? Steht am Ende ein Punkt?
  - Kiosk-Lösung (Prüffragen): Deine Verbesserungen hängen von deinem Text ab. Die Rückmeldung an der Haltestelle ist ein Hinweis. Du entscheidest mit Interview und Checkliste, was du änderst. /  / So prüfst du: / K1: Stimmen Tiername, Maß mit Einheit und Bezug, Lebensraum und Nahrung mit dem Interview überein? Gelten sie für alle Tiere der Art? / K2: Zähle vier verschiedene Merkmale. Dasselbe Merkmal zählt nur einmal. / K3: Steht der Überblick am Anfang? Stehen zusammengehörige Angaben zusammen? / K4 und K5: Präsens, sachlich, keine Meinung aus dem Interview, ganze Sätze? / K6: Satzanfang eingekreist, zwei Nomen unterstrichen, Punkt markiert? /  / Ein richtiger Satz bleibt. Begründe: „Mein Satz bleibt, weil …“
  - Kiosk-Vertiefung: Beispiel vorher: „der schwanz ist toll“ / Nachher: „Der Schwanz ist lang und schmal.“ / Besser, weil der Satz groß beginnt, das Nomen groß ist und ein genaues Merkmal statt einer Wertung steht.
- **Checkliste · Inhalt und Aufbau:** K1 · Informationen: Hast du das Tier benannt? Stimmen Maß, Einheit und Bezug – für alle Tiere der Art, nicht nur für das Zootier? Stehen Lebensraum und Nahrung im Text? Vergleiche alles mit dem Interview. · K2 · Aussehen: Findest du vier verschiedene genaue äußere Merkmale? Zeige sie. „schön“ ist kein genaues Merkmal. · K3 · Aufbau: Stehen Tiername und Überblick am Anfang? Sind zusammengehörige Informationen zusammen?
- **Checkliste · Sprache und Schreibung:** K4 · Sachlich schreiben: Stehen deine Verben im Präsens? Beschreibst du genau? Hast du keine Meinung und kein Erlebnis aus dem Interview übernommen? · K5 · Verständliche Sätze: Sind deine Sätze vollständig und verständlich? Ist klar, auf wen sich „er“, „es“ und „sein“ beziehen? · K6 · Schreibung prüfen: Prüfe große Satzanfänge und Nomen sowie Satzschlusspunkte. Vergleiche schwierige Wörter mit dem Interview. Kreise einen Satzanfang ein, unterstreiche zwei Nomen und markiere einen Punkt als Prüfbeleg.
- **Hilfekarte Rückmeldekarte · Rückmeldung an der Haltestelle** – Hinweis: Du gibst einem anderen Kind eine Rückmeldung zu seinem Text. Lies den Text ruhig. Wähle zwei oder drei Fragen. So geht es: 1. Das Kind hat seinen Text schon selbst geprüft. / 2. Du liest den Text. / 3. Du prüfst mit zwei oder drei Fragen. / 4. Das Kind entscheidet selbst, was es verbessert.. Fragen zum Prüfen: Kannst du dir das Aussehen des Tieres vorstellen? Zeige eine genaue Beschreibung. / Stehen zusammengehörige Informationen zusammen? / Welche Stelle sollte noch genauer oder verständlicher werden?. So sagst du es: *Diese Stelle ist genau: …* / *Hier habe ich eine Frage: …* / *Prüfe diese Angabe noch einmal im Interview: …*.
- **Raumschild:** Haltestelle – Rückmeldung zum Text


## 9 · Probearbeit und Klassenarbeit ⚙

Gemeinsamer Aufbau (A4, 7 Seiten; Vorbild: Lernerfolgskontrolle der Reihe Wunschbriefe): Material vorn: Interview (2 Seiten, Foto, Zeilennummern, Wörterhilfe) · 1 Auftrag (Situation, Auftrags-Checkliste inkl. „Markiere Sachangaben, streiche Meinungen/Einzeltier“, Arbeitszeit-Feld, bei KA Terminwahl) · 3 Planung (Schreibplan Überblick/Aussehen ×4/Lebensraum/Nahrung) · 4 Schreibseite (Überschrift + Linien, Prüfhinweis) · 5 „Dein Text: Das zählt“ (K1–K6 zum Abhaken) · 6 Hilfeseite (erlaubt) · 7 Lehrkraftseite (Probearbeit: Rückmeldung E3.1–E3.5, Hilfen, x/5, nächster Schritt, Wahlzeit, Klassenarbeitstermin; Klassenarbeit: Bewertung K1–K6 mit Punkten und Note).

### Deine Probearbeit: Der Waschbär (Probearbeit) · `inhalt/probearbeit_waschbaer.json`

- Situation: Unsere Klasse gestaltet ein Tierlexikon. Es fehlt noch ein Text über den Waschbären. Die Schülerzeitung hat dafür ein Interview im Zoo geführt. Schreibe daraus einen Lexikontext. Andere sollen sich das Tier danach gut vorstellen können.
- Material: Interview `waschbaer` (vor dem Auftrag, mit Zeilennummern; Text siehe 8.0)
- Foto: Foto: BS Thurner Hof · CC BY-SA 3.0 · Wikimedia Commons · Graustufenfassung
- Indikatoren: E3.1 Informationen (K1) (erreicht, wenn Tiername, Maß der Art mit Bezug, Lebensraum und Nahrung; nichts nur über Rocky) · E3.2 Aussehen: vier Merkmale (K2) (erreicht, wenn mindestens vier verschiedene äußere Merkmale richtig beschrieben) · E3.3 Aufbau (K3) (erreicht, wenn Text beginnt mit Überblick und ordnet zusammengehörige Informationen nachvollziehbar) · E3.4 Sprache (K4, K5) (erreicht, wenn zusammenhängend, überwiegend sachlich, Präsens, vollständige Sätze; keine Meinung aus dem Interview) · E3.5 Schreibung mit Prüfbeleg (K6) (erreicht, wenn Prüfung von Satzanfängen, Nomen und Satzschlüssen am Produkt belegt; geübte Schreibungen überwiegend richtig)

### Deine Klassenarbeit: Der Biber (Klassenarbeit) · `inhalt/klassenarbeit_biber.json`

- Situation: Unser Tiermagazin bekommt eine neue Seite. Es fehlt noch ein Text über den Europäischen Biber. Die Schülerzeitung hat dafür ein Interview im Zoo geführt. Schreibe daraus einen Lexikontext. Andere sollen sich das Tier danach gut vorstellen können.
- Material: Interview `biber` (vor dem Auftrag, mit Zeilennummern; Text siehe 8.0)
- Foto: Foto: Tomas Čekanavičius · CC BY-SA 3.0 · Wikimedia Commons · Graustufenfassung
- Bewertungserwartung: K1 Informationen: Tiername, Gewicht mit Einheit und Bezug, Lebensraum, Nahrung; nur Angaben zur Art · K2 Aussehen: mindestens vier verschiedene äußere Merkmale richtig (z. B. kräftiger Körper, kurze Beine, dichtes braunes Fell, breiter flacher Schwanz) · K3 Aufbau: Überschrift, Überblick am Anfang, zusammengehörige Angaben gebündelt · K4 Sachlich: sachlich, Präsens; nichts Wertendes oder Erlebtes aus dem Interview · K5 Verständlich: zusammenhängender Text aus überwiegend vollständigen, verständlichen Sätzen; klare Bezüge · K6 Schreibung: Prüfung sichtbar; Satzanfänge, Nomen, Satzschlüsse und geübte Tierwörter überwiegend richtig

### Deine Klassenarbeit: Das Breitmaulnashorn (Klassenarbeit) · `inhalt/klassenarbeit_breitmaulnashorn.json`

- Situation: Unser Tiermagazin bekommt eine neue Seite. Es fehlt noch ein Text über das Breitmaulnashorn. Die Schülerzeitung hat dafür ein Interview im Zoo geführt. Schreibe daraus einen Lexikontext. Andere sollen sich das Tier danach gut vorstellen können.
- Material: Interview `breitmaulnashorn` (vor dem Auftrag, mit Zeilennummern; Text siehe 8.0)
- Foto: Foto folgt
- Bewertungserwartung: K1 Informationen: Tiername, Maß mit Einheit und Bezug (z. B. Kopf und Rumpf 3,40–3,80 m, Schwanz zusätzlich), Lebensraum, Nahrung; nur Angaben zur Art · K2 Aussehen: mindestens vier verschiedene äußere Merkmale richtig (z. B. graue, dicke Haut, zwei Hörner, breite Lippen, kurze, kräftige Beine, Buckel) · K3 Aufbau: Überschrift, Überblick am Anfang, zusammengehörige Angaben gebündelt · K4 Sachlich: sachlich, Präsens; nichts Wertendes oder Erlebtes aus dem Interview · K5 Verständlich: zusammenhängender Text aus überwiegend vollständigen, verständlichen Sätzen; klare Bezüge · K6 Schreibung: Prüfung sichtbar; Satzanfänge, Nomen, Satzschlüsse und geübte Tierwörter überwiegend richtig


## 10 · Wahlphase, Strategiekarten, Kiosk, Lernweg ⚙

### Wahlphase (nach Feedback zur Probearbeit)

Du hast deine Probearbeit geschrieben und Feedback bekommen. Jetzt entscheidest du, woran du arbeitest. Hast du weniger als vier von fünf Zielen gezeigt? Dann übst du zuerst deine offenen Ziele und zeigst sie noch einmal. Deine Rückmeldung sagt dir, mit welchem Blatt du übst. Du musst nicht alle Projekte machen. Du kannst allein, zu zweit oder zu dritt arbeiten. Während einer Klassenarbeit arbeitest du still für dich.

- **P1 Unser Tiermagazin** – Du gestaltest eine Seite für das Tiermagazin unserer Klasse. Arbeite allein oder zu zweit. Schritte: Text auswählen und prüfen: Nimm deinen überarbeiteten Übungstext. Prüfe ihn noch einmal mit K1–K6. Verbessere nur nötige Stellen. Schreibe nicht alles neu. · Die Seite gestalten: Schreibe eine Überschrift mit dem Tiernamen. Übertrage deinen Text sauber. Zeichne das Tier und beschrifte vier äußere Merkmale. Schreibe unten: „Quelle: Tierpaket …“. · Die Seite abgeben: Lege deine Seite in die Magazin-Mappe. Zu zweit: Schreibt unten auf, wer was gemacht hat. Gelingt, wenn: Die Angaben passen zum Material.; Vier Merkmale sind beschriftet.; Text und Zeichnung passen zusammen.; Die Seite ist gut lesbar.. Erweiterung (freiwillig): **Kurzvortrag (1–2 Minuten):** Stelle dein Tier mit wenigen Stichwörtern vor. Nenne genaue Merkmale und eine interessante Information aus dem Material. Sprich so, dass andere dich verstehen. Eine Karteikarte oder dein Schreibplan hilft dir.
- **P2 Welches Tier ist gemeint?** – Du erstellst eine Rätselkarte und eine getrennte Lösungskarte. Arbeite allein, zu zweit oder zu dritt. Schritte: Hinweise schreiben: Wähle eines der drei Tiere. Schreibe vier genaue äußere Merkmale auf deine Rätselkarte. Nenne den Tiernamen noch nicht. Prüfe: Passen die Hinweise zusammen nur zu deinem Tier? · Lösung getrennt sichern: Schreibe den Tiernamen auf eine zweite Karte. Notiere zu jedem Hinweis den Beleg: eine Textstelle oder ein sichtbares Merkmal auf dem Foto. · Rätsel erproben: Lies einem Kind deine Hinweise vor. Es zeigt auf das passende Tier. Frage danach: „Was hat geholfen? Was war unklar?“ · Verbessern: Verbessere ungenaue Hinweise. Passt schon alles? Erkläre, warum die Hinweise eindeutig sind. Gelingt, wenn: Vier richtige Merkmale.; Verständliche Hinweise.; Unter den drei Tieren eindeutig.; Getrennte Lösung mit vier Belegen.. Erweiterung (freiwillig): Ordne deine Hinweise vom allgemeinen zum besonders kennzeichnenden Merkmal. Das letzte Merkmal verrät das Tier sicher.
- **P3 Zwei Tiere vergleichen** – Du erstellst eine Tabelle und schreibst drei Vergleichssätze. Arbeite allein, zu zweit oder zu dritt. Schritte: Merkmale auswählen: Wähle drei Körpermerkmale, zu denen beide Pakete Angaben enthalten. Vergleiche immer dasselbe Merkmal, zum Beispiel Fell oder Schwanz. · Tabelle anlegen: Zeichne im Heft eine Tabelle mit drei Spalten: Merkmal · Tier 1 · Tier 2. Trage zu jedem Merkmal die Angaben beider Tiere ein. · Sätze schreiben: Schreibe zu jeder Zeile einen Vergleichssatz. Zum Beispiel: „Beide Tiere haben …“ oder „Beim … ist …, beim … ist …“. · Prüfen: Prüfe alle Angaben in den Paketen. Markiere einen Vergleich, der beim Erkennen besonders hilft. Gelingt, wenn: Drei gleiche Merkmale verglichen.; Angaben zu beiden Tieren richtig.; Drei verständliche Vergleichssätze.. Erweiterung (freiwillig): Erkläre, warum dein Vergleich mehr hilft als eine Wertung wie „süß“.

### Strategiekarten (am Lernbuddy anlegen; Aufbau: Wann? · 4 Schritte · Beispiel · Hat es geholfen? ja/etwas/nein)

1. **Lesen mit Suchauftrag** – Wann: Du suchst Informationen in einem Sachtext oder Interview. Schritte: Lies den Text einmal. Markiere unbekannte Wörter. · Kläre die Wörter: Satz noch einmal lesen, Wörterhilfe, fragen. · Lies mit Suchauftrag weiter. Markiere die Stelle. · Notiere ein Stichwort unter der Überschrift. Beispiel: Was fressen Fischotter? / Suchwort: *fressen* / → *hauptsächlich Fische*
2. **Markieren mit Buchstaben** – Wann: Du suchst verschiedene Informationen im selben Text. Schritte: Lege fest, was du suchst. · Schreibe einen Buchstaben an die Stelle: / **A** Aussehen · **L** Lebensraum / **N** Nahrung · **M** Maß · Markiere nur die wichtigen Wörter, nicht den ganzen Satz. · Prüfe: Passt die Stelle zur Frage? Beispiel: *Er lebt an Flüssen und Seen.* → **L**
3. **Ordnen unter Überschriften** – Wann: Du sammelst Informationen für einen Plan. Schritte: Schreibe die Überschriften: Überblick · Aussehen · Lebensraum · Nahrung. · Frage bei jeder Angabe: Wohin gehört sie? · Schreibe sie als Stichwort darunter. · Zähle: Hast du vier Merkmale beim Aussehen? Beispiel: *breiter, flacher Kopf* → Aussehen / *Fische* → Nahrung
4. **Genau statt wertend** – Wann: Du beschreibst, wie ein Tier aussieht. Schritte: Lies dein Wort: Sagt es, wie jemand das Tier findet? · Frage: Kann ich es im Bild sehen oder im Interview lesen? · Ersetze die Wertung durch Form, Farbe oder Größe. · Prüfe die neue Angabe am Interview. Beispiel: nicht: *schönes Fell* / sondern: *oben dunkelbraunes Fell*
5. **Die Wörterhilfe nutzen** – Wann: Dir fehlt ein genaues Wort. Schritte: Suche den Körperteil in der Wörterhilfe. · Lies die möglichen Wörter. · Wähle nur ein Wort, das zu deinem Tier passt. · Prüfe es am Bild oder im Text. Beispiel: Schwanz: *lang, kurz, buschig, schmal* / Erdmännchen: *lang und schmal*
6. **Einen Satz bauen** – Wann: Du machst aus Stichwörtern einen Satz. Schritte: Wer oder was? Nenne das Subjekt. · Was tut es oder wie ist es? Setze das Verb im Präsens. · Ergänze die Angabe aus dem Plan. · Prüfe: Großer Anfang? Punkt am Ende? Beispiel: *Kopf – breit, flach* / → *Sein Kopf ist breit und flach.*
7. **Satzanfang, Nomen, Punkt** – Wann: Du prüfst die Schreibung deines Textes. Schritte: Lies Satz für Satz. Lege ein Lineal unter die Zeile. · Kreise den Satzanfang ein. Ist er groß? · Unterstreiche die Nomen. Sind sie groß? · Markiere das Satzende. Steht ein Punkt? Beispiel: *sein kopf ist flach* / → *Sein Kopf ist flach.*
8. **Rückmeldung geben** – Wann: Du liest den Text eines anderen Kindes an der Haltestelle. Schritte: Lies den ganzen Text ruhig. · Wähle zwei Fragen von der Rückmeldekarte. · Zeige die passende Textstelle. · Sage es freundlich und genau. Beispiel: *Diese Stelle ist genau: …* / *Prüfe diese Angabe im Material: …*
9. **Aus dem Interview wird ein Sachtext** – Wann: Du schreibst mit einem Interview als Material. Schritte: Frage bei jeder Angabe: Gilt das für alle Tiere der Art? · Ja: markieren. Nur das Zootier oder eine Meinung: streichen. · Vergleich? Nimm nur die Sachangabe heraus. · Schreibe im Präsens über die Tierart: *Der Fischotter …* Beispiel: *„Otto ist 80 cm lang.“* → streichen / *„Fischotter sind 60 bis 90 cm lang.“* → markieren
10. **Meine eigene Strategie** – leere Karte für eine eigene Strategie

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
  training_giraffe.json   Beispielaufgabe Angola-Giraffe für die Lern-App
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

**Markup in Inhaltsdateien:** `*kursiv*` für Beispielsätze, `**fett**` für Begriffe, `\n` Zeilenumbruch, `{Wort}` = Lücke (Förder-Lückentext, Wortspeicher automatisch), `[[Textstelle|Kürzel]]` = Markierung im Interview (unsichtbar für Kinder; T Tiername, M Maß der Art, A Aussehen, L Lebensraum, N Nahrung, W Meinung, X Einzeltier/Zooalltag, V Vergleich, Z Zusatz Verhalten, U Vermutung). Zeilenangaben in Blättern/Kiosk („Z. 12“) beziehen sich auf den Satz der Interviews; nach Textänderungen `ausgabe/interviews/zeilen.json` prüfen und Verweise nachziehen.

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

Zwei Kinder; kurze Texte möglich. Gleiche Etappen und Blattnummern mit „F“, gleicher Input, Fischotter als Beispieltier (Etappe 3F: nur Erdmännchen). Je Etappe vereinfachte **Merkkarte**, **Fotoseite** mit nummerierten Bildstellen und **Kurzinterview** (6 Fragen, Antworten 1–2 Sätze, je eine Meinung und Angaben nur über das Zootier; Aufgaben „Info oder Meinung?“ und „Wer ist gemeint?“). Kleinschrittig: ein Auftrag pro Kasten mit Symbol je Format. Formate: ankreuzen · zuordnen (Zahl ins Kästchen, ggf. nummerierte Bedeutungen) · sortieren (Wortspeicher → Spalten) · Lückentext (Wortspeicher, ggf. Ablenker) · Wortkarten zu einem Satz ordnen · Satz weiterschreiben · Prüfliste · Bild betrachten · Hinweis. Jede Seite mit Lösungsstreifen auf dem Kopf zum Umknicken. Schreiben aufs Blatt. GN-F-Ziele sind Vorschläge; Förderziele individuell vereinbaren, Zeile für eigenes Förderziel.

### Etappe 1F · Informationen finden und ordnen

- Merkkarte: Genau: Genaue Wörter sagen, wie das Tier aussieht: *kurz, lang, dunkelbraun, breit*. · Nicht genau: Diese Wörter sind Meinungen: *toll, schön, süß*. · Bild: Auf dem Foto siehst du: Nase, Auge, Ohr, Tasthaare, Fell. · Interview: Im Interview findest du: Wo leben Fischotter? Was fressen sie? · Nur Otto?: Was nur für Otto gilt, gehört nicht in die Beschreibung. · Ordnen: Aussehen · Lebensraum · Nahrung
- Material: Fotoseite mit Zahlen + Kurzinterview `fischotter-f` (Text siehe 8.0)
- Bildstellen: 1, 2, 3, 4, 5 (Ein Fischotter im Gras. Die Zahlen 1 bis 5 zeigen auf Nase, Auge, Ohr, Tasthaare und Fell.)
- **Blatt 1F · Genau oder nicht genau?:** [ankreuzen] Welche Sätze sind genau? Kreuze **2** Sätze an. Richtig: Der Fischotter hat kurze Beine., Das Fell ist dunkelbraun. | [sortieren] Schreibe jedes Wort in die richtige Spalte. Lösung: genau: kurz, dunkelbraun, lang; Meinung: toll, schön, süß | [ankreuzen] **Info oder Meinung?** Kreuze die **Meinung** an. Richtig: Otto ist der süßeste Otter der Welt! | [ankreuzen] **Sprachdetektiv:** Nomen schreibst du groß. Kreuze die **3** Nomen an. Richtig: Fischotter, Beine, Fell
- **Blatt 2F · Was siehst du auf dem Foto?:** [bild] Schau dir das Foto genau an. Die Zahlen zeigen auf Körperteile. | [zuordnen] Welche Zahl gehört zu welchem Wort? Schreibe die Zahl in das Kästchen. Lösung: Nase=1, Auge=2, Ohr=3, Tasthaare=4, Fell=5 | [luecke] Fülle die Lücken. Nutze den Wortspeicher. Lösung: klein, Tasthaare
- **Blatt 3F · Was steht im Interview?:** [hinweis] Lies das Interview. Lies Satz für Satz. Zeige mit dem Finger mit. | [luecke] Fülle die Lücken. Nutze den Wortspeicher. Lösung: Flüssen, Seen, Fische, Zentimeter | [zuordnen] **Wer ist gemeint?** Schreibe die Zahl in das Kästchen. Lösung: Fischotter leben an Flüssen.=1, Otto wohnt im Zoo.=2, Otto ist 80 Zentimeter lang.=2, Fischotter fressen Krebse.=1 | [ankreuzen] **Sprachdetektiv:** Welche Wörter sind Verben? Kreuze **2** an. Richtig: lebt, frisst
- **Blatt 4F · Ordne die Informationen:** [sortieren] Schreibe jedes Wort unter die richtige Überschrift. Streiche das Wort im Wortspeicher durch. Lösung: Aussehen: kurze Beine, dunkelbraunes Fell; Lebensraum: Flüsse, Seen; Nahrung: Fische, Krebse | [ankreuzen] Wohin gehört „langer Körper“? Kreuze an. Richtig: Aussehen
- **GN1F:** F1.1 Ich erkenne genaue Angaben über alle Fischotter. (erreicht, wenn genaue Sätze angekreuzt; „Wer ist gemeint?“ richtig) · F1.2 Ich benenne Körperteile auf dem Foto. (erreicht, wenn 3 von 4 Zahlen richtig) · F1.3 Ich finde den Lebensraum im Interview. (erreicht, wenn Flüsse und Seen richtig eingesetzt) · F1.4 Ich finde die Nahrung im Interview. (erreicht, wenn Fische richtig eingesetzt) · F1.5 Ich ordne Angaben unter Überschriften. (erreicht, wenn 5 von 6 Wörtern richtig sortiert)

### Etappe 2F · Sachlich und genau formulieren

- Merkkarte: Genau: Nimm Wörter, die du prüfen kannst: *dunkelbraun, kurz, breit*. Nicht: *schön, toll*. · Präsens: Eine Tierbeschreibung steht in der Gegenwart: *er lebt, er frisst, es ist*. · Ein Satz: Wer? + Verb + Rest. *Der Fischotter + frisst + Fische.* · Groß: Der Satzanfang ist groß. Nomen sind groß: *Fell, Kopf, Fische*. · Punkt: Am Ende vom Satz steht ein Punkt.
- Material: Fotoseite mit Zahlen + Kurzinterview `fischotter-f` (Text siehe 8.0)
- Bildstellen: 1, 2, 3, 4, 5 (Ein Fischotter im Gras. Die Zahlen 1 bis 5 zeigen auf Nase, Auge, Ohr, Tasthaare und Fell.)
- **Blatt 5F · Treffende Wörter:** [ankreuzen] Wie ist das Fell oben? Kreuze das **genaue** Wort an. Richtig: dunkelbraun | [ankreuzen] Wie ist der Kopf? Kreuze die **genaue** Angabe an. Richtig: breit und flach | [ankreuzen] Frau Berger sagt: „Otto ist der süßeste Otter der Welt!“ **Info oder Meinung?** Richtig: Meinung | [luecke] Mache den Satz genauer. Nutze den Wortspeicher. Lösung: Fischotter, schwimmt | [zuordnen] Was bedeutet das Wort? Schreibe die Zahl in das Kästchen. Lösung: Tasthaare=1, Schwimmhäute=2
- **Blatt 6F · Sachliche Sätze:** [ordnen] Bilde einen Satz aus den Wortkarten. Schreibe ihn auf die Linie. Lösung: Seine Beine sind kurz. | [ordnen] Bilde einen Satz aus den Wortkarten. Schreibe ihn auf die Linie. Lösung: Der Fischotter frisst auch Krebse. | [ankreuzen] Welcher Satz steht in der Gegenwart (Präsens)? Kreuze an. Richtig: Der Fischotter lebt am Wasser. | [luecke] Setze das passende Verb ein. Lösung: frisst, fressen | [ankreuzen] Welcher Satz ist richtig geschrieben? Kreuze an. Richtig: Der Fischotter lebt am See.
- **GN2F:** F2.1 Ich wähle genaue Wörter und erkenne eine Meinung. (erreicht, wenn genaues Wort und Meinung richtig angekreuzt) · F2.2 Ich bilde einen Satz aus Wortkarten. (erreicht, wenn Satz vollständig und in sinnvoller Reihenfolge) · F2.3 Ich wähle das Verb im Präsens. (erreicht, wenn Präsensform richtig gewählt bzw. eingesetzt) · F2.4 Ich erkenne große Anfänge, Nomen und Punkt. (erreicht, wenn richtig geschriebenen Satz angekreuzt) · F2.5 Ich kenne ein Fachwort. (erreicht, wenn Fachwort richtig zugeordnet)

### Etappe 3F · Eine Tierbeschreibung schreiben und prüfen

- Merkkarte: Plan: Überblick · Aussehen · Lebensraum · Nahrung · Überblick: Name und Größe: *Das Erdmännchen ist ohne Schwanz 25 bis 29 Zentimeter lang.* · Aussehen: Vier Merkmale: Körper, Fell, Schwanz, Krallen … · Nur Kiki?: Was nur für Kiki gilt, gehört nicht in die Beschreibung. · Text: Erst der Name, dann das Aussehen, dann Lebensraum und Nahrung. · Prüfen: Großer Anfang? Nomen groß? Punkt am Ende?
- Material: Fotoseite mit Zahlen + Kurzinterview `erdmaennchen-f` (Text siehe 8.0)
- Bildstellen: 1, 2, 3, 4 (Ein Erdmännchen steht aufrecht. Die Zahlen zeigen auf Augenfleck, Körper, Schwanz und Pfote mit Krallen.)
- **Blatt 7F · Dein Schreibplan:** [bild] Schau dir das Foto genau an. Die Zahlen zeigen auf Körperteile. | [zuordnen] Welche Zahl gehört zu welchem Wort? Schreibe die Zahl in das Kästchen. Lösung: Fleck um das Auge=1, Körper=2, Schwanz=3, Pfote mit Krallen=4 | [zuordnen] **Wer ist gemeint?** Schreibe die Zahl in das Kästchen. Lösung: Erdmännchen fressen Insekten.=1, Kiki mag Mehlwürmer.=2, Kiki ist kleiner.=2, Erdmännchen leben in Afrika.=1 | [sortieren] Ordne die Stichwörter. Schreibe jedes unter die richtige Überschrift. Lösung: Aussehen: schlanker Körper, hellbraunes Fell, langer Schwanz, lange Krallen; Lebensraum: Afrika, Grasland; Nahrung: Insekten, Spinnen | [luecke] Fülle den Überblick aus. Nutze das Interview. Lösung: Erdmännchen, Schwanz, Zentimeter
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

## 16 · Offene Punkte (Stand 10.10.2026)

- Arbeitszeit der Probearbeit; Arbeitszeit, Punkteverteilung und Notengrenzen der Klassenarbeit.
- Foto Breitmaulnashorn fehlt (Platzhalter); Biber-Foto vorläufig (Tierpaket, CC BY-SA 3.0). Wunschbild tierdoku.de nicht ladbar und ohne freie Lizenz.
- Probearbeit F (Waschbär) und Klassenarbeit F (Biber) liegen vor (`inhalt/probearbeit_f_waschbaer.json`, `inhalt/klassenarbeit_f_biber.json`, `tools/build_pruefung_f.py`): Kurzinterview → Auftrag → Aufgaben (Info/Meinung, Wer ist gemeint, Plan sortieren, Lückentext-Beschreibung, eigener Satz, Prüfliste) → Rückmeldung F3.1–F3.5 bzw. Bewertung (22 Punkte, Vorschlag). Offen: zieldifferente Bewertung mit Schulvorgaben abstimmen; F-Fassung Nashorn bei Bedarf.
- Zuordnung Variante ↔ Termin (Vorschlag Biber früh, Nashorn spät).
- Lehrkraft-Cockpit `index.html` zeigt noch Vorfassungen.
- Gedruckte Lösungsfassung (Tipps/Lösungen wie im Kiosk) und ggf. Übungskarten-Modus im Kiosk.
- Unterrichtserprobung steht aus; Zeitbudget nach Erprobung prüfen.
- Lern-App (`planung/Lernapp_Planung.md`): Grundversion gebaut (Mein Weg, Wissen, 15 Übungen inkl. Beispielaufgabe Giraffe und Training Ü1/Ü2, Buchstabenrätsel, Zuhause); offen: Quiz je Etappe, Silbenrätsel/Suchsel, Schalter „Einfach“, QR-Zettel. Freigabe für Kinder steuert die Lehrkraft über den QR-Code. Klassenarbeiten sollen später extern gespeichert werden.

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
