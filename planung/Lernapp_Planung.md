# Lern-App „Zootiere“ fürs Smartphone · Planung

> **Stand:** 10.10.2026 · Grundversion gebaut (`lernapp/`, `python tools/build_lernapp.py`), noch nicht verteilt.
> **Zweck:** Lernbegleiter für zu Hause auf eigenen oder elterlichen Handys (hochkant). Deckt den Lernweg ab, wiederholt die Merkblatt-Inhalte, bietet Übungen, Quiz, Buchstabenrätsel und eine Anleitung, wie man ohne Schulmaterial an Tieren aus der eigenen Umgebung übt.
> **Bezug:** Alles bezieht sich auf die Reihe (WISSENSBASIS.md). Die App ersetzt keinen Unterricht, keinen Kiosk und keinen Nachweis.

## 1 · Festlegungen (10.10.2026)

| Frage | Entscheidung |
|---|---|
| Lösungen zu Blatt 1–9 (Kiosk-Tipps/-Lösungen) in der App? | **Nein.** Kiosk bleibt im Raum und Teil der Lösungsleiter. Die App hat eigene Übungen mit eigener Rückmeldung. |
| Trainingstiere in der App? | **Ja:** Elenantilope (Ü1), Hirschziegenantilope (Ü2) und die Beispielaufgabe **Angola-Giraffe** (Zikomo, mit drei Mustertexten). |
| Hosting | **Im Hauptrepo** unter `lernapp/`, Deploy über das bestehende Vercel-Projekt aus `main`. Vercel-Einstellungen bleiben unverändert. |
| Prüfungsdateien und Freigabe | Klassenarbeiten werden später extern gespeichert. Die App liegt schon in `main`; **die Lehrkraft steuert die Nutzung über den QR-Code** (Entscheidung 10.10.2026). |

## 2 · Grundsätze

- **Eine Inhaltsquelle:** Generator `tools/build_lernapp.py` liest `inhalt/*.json` (Etappen, Interviews, Strategiekarten, Training) und die neue Datei `inhalt/lernapp.json` (Quiz, Rätsel, Zuhause-Teil, App-Übungen). Merkkarten und gesicherte Antworten sind wortgleich mit Input/Merkblatt.
- **Erlaubte Tiere:** Fischotter, Erdmännchen, Roter Panda, Elenantilope, Hirschziegenantilope, Angola-Giraffe, Alltagstiere im Zuhause-Teil.
- **Gesperrt:** Waschbär (Probearbeit), Biber und Breitmaulnashorn (Klassenarbeit), Interviewauszüge der Gelingensnachweise A/B, Kiosk-Lösungen zu Blatt 1–9. Der Generator prüft das automatisch (siehe 8).
- **Musterlösungen Ü1/Ü2:** bleiben im Kiosk (Kiosk 10/11). In der App: Markieren, Plan ordnen, Sätze prüfen mit Schritt-Rückmeldung. Das vollständige Muster mit drei Standards liefert die Giraffe.
- **Datenschutz:** keine Anmeldung, keine Namen, kein Tracking, keine Analytics, keine Kamera/Fotos. Fortschritt und Notizen nur in `localStorage` (try/catch), Knopf „Alles löschen“. Keine Netzladung: Andika, Bilder, Grafik eingebettet. Elterninfo in der App und als QR-Zettel.
- **Bewertungsneutral:** keine Punkte für Tempo, keine Ranglisten, kein „Level“. Häkchen setzt das Kind selbst; sie sind Orientierung, kein Nachweis. Nichts heißt „Lernbuddy“.
- **Sprache:** Du-Form, kurze Sätze, wie auf den Blättern.

## 3 · Aufbau: fünf Tabs (Leiste unten)

| Tab | Inhalt |
|---|---|
| 🧭 **Mein Weg** | Etappe 1 → 2 → 3 → Probearbeit → Wahlzeit → Training → Klassenarbeit. Blätter selbst abhaken, „Was kommt als Nächstes?“, 4/5-Regel kindgerecht erklärt |
| 📖 **Wissen** | Merkkarten je Etappe (Merkblatt-Abschnitte, Frage → „Antwort zeigen“), Strategiekarten 1–9 zum Blättern, K1–K6 in Kinderfassung |
| ✏️ **Üben** | Übungen (2–4 Min.) und Quiz je Etappe; Abschnitt **Training** |
| 🔤 **Rätsel** | Buchstabenrätsel zu Fachbegriffen |
| 🏡 **Zuhause** | Tiere in der eigenen Umgebung beschreiben, ohne Schulmaterial |

## 4 · Übungen (Tab „Üben“)

Sofortige Rückmeldung mit Begründung und Verweis („Merkblatt 1, Abschnitt 5“). **Zeilenangaben:** Auf dem Handy bricht der Text anders um; die App verweist auf die Interviewfrage („Frage 3“), nicht auf Zeilen.

**Etappe 1 · Informationen finden und ordnen**
- *Interview-Detektiv:* Fischotter-Interview als Sprechblasen; Sätze antippen → L / N / M / A / streichen. Lösung direkt aus den `[[Stelle|Kürzel]]`-Markierungen in `interviews.json`.
- *Sachangabe, nur Otto oder Meinung?* Karten in drei Felder sortieren.
- *Finde den Fisch:* `aquarium_farbe.svg`; Beschreibung lesen, Fisch antippen.
- *Was zeigt das Foto?* „sicher sichtbar“ oder „nur im Text“ (Schwimmhäute, Körperlänge).

**Etappe 2 · Sachlich und genau formulieren**
- *Genau statt wertend:* passende genaue Angabe für „schönes Fell“ wählen.
- *Interview → Sachsatz:* aus drei Umformungen die sachliche wählen; Ablenker = typische Fehler (Vergleich übernommen, Vergangenheit, „Otto“ statt Art).
- *Satzbau:* Wortkarten ordnen, dann prüfen (großer Anfang, Punkt).
- *Verb-Werkstatt:* Grundform → gebeugte Form; Singular/Plural („Der Otter schwimmt / Die Otter …“).
- *Wörter zerlegen:* Körper + Länge; Artikel des letzten Wortes hervorgehoben.

**Etappe 3 · Schreiben und prüfen** (Erdmännchen / Roter Panda)
- *Plan sortieren:* Stichwörter unter Überblick / Aussehen / Lebensraum / Nahrung.
- *Merkmale zählen (K2):* verschiedene äußere Merkmale in einem Beispieltext antippen; Doppeltes zählt nicht.
- *Fehlerjagd (K6):* kleine Satzanfänge, kleine Nomen, fehlende Punkte antippen.
- *Ist der Satz okay?* auch richtige Sätze („Mein Satz bleibt, weil …“).

**Quiz:** je Etappe 8–10 Fragen, gemischt, beliebig oft. Ende ohne Punktwert: „Das kannst du schon“ und „Schau dir noch einmal an: …“.

**Training (vor der Klassenarbeit)**
- *Angola-Giraffe:* vollständiger Durchgang (Auftrag, Interview, Markieren, Plan, Sätze, drei Mustertexte Mindest-/Regel-/Leistungsstandard, Fehler finden, Vorlesen). Quelle: `apps/beispielaufgabe-giraffe/index.html` (in `main`).10.2026); wird in `inhalt/training_giraffe.json` überführt.
- *Elenantilope (Ü1), Hirschziegenantilope (Ü2):* Interview markieren, Plan ordnen, Sätze prüfen; keine Musterlösung in der App.

## 5 · Buchstabenrätsel (Tab „Rätsel“)

**Wortliste:** Fachwörter (Tasthaare, Schwimmhäute, Krallen, Rumpf, Schwanzansatz, Mangusten, Marder, Dämmerung, Bambus, Wamme, Savanne, Steppe), Lernbegriffe (Lebensraum, Nahrung, Sachangabe, Meinung, Einzelfall, Überblick, Merkmal), Sprachspur (Nomen, Artikel, Verb, Adjektiv, Präsens, Grundform, Subjekt).

**Formate:** Buchstabensalat (Kacheln + Hinweissatz) · Silbenrätsel · Lückenwort · Suchsel 8 × 8 (nur waagerecht/senkrecht, wischen). Nach jedem Wort eine Ein-Satz-Erklärung; Großschreibung bei Nomen sichtbar.

## 6 · Zuhause üben (Tab „Zuhause“)

Gleiche Denkschritte wie in der Reihe, übertragen auf Haustiere, Amsel, Taube, Eichhörnchen, Ente, Nachbars Hund, Spinne am Fenster.

1. **Beobachten wie im Zoo:** Was siehst du sicher? Was nicht? Notiz in der App, Zeichnung im Heft.
2. **Dein eigenes Interview:** ein Familienmitglied über ein Tier befragen; danach sortieren: gilt für **alle Katzen** (Sachangabe) · nur für **Minka** (Einzelfall) · **Meinung**. Übertragung der Otto-Logik.
3. **Grenze der Beobachtung:** Lebensraum, Nahrung, Maß der Art sieht man nicht am Einzeltier → Tierlexikon, Stadtbibliothek, Erwachsene fragen; nur belegbare Angaben.
4. **Messen ist ein Einzelfall:** „Unsere Katze ist 45 cm lang“ gilt nur für eure Katze.
5. **Schreibplan + Selbstcheck:** Vorlage Überblick / Aussehen (4×) / Lebensraum / Nahrung (lokal gespeichert), Text ins Heft, dann K1–K6 abhaken.
6. **Zu zweit:** Tier mit zwei genauen Merkmalen beschreiben, jemand rät (Fischrätsel-Prinzip).
7. **Sicherheit:** fremde Tiere nicht anfassen oder füttern, Wildtiere nicht stören, Hände waschen, Haustiere nur mit Erlaubnis messen.

## 7 · Gestaltung und Technik

- Hochkant, 360–430 px; Tab-Leiste unten (Daumenzone); Tippflächen ≥ 48 px; Grundschrift 18 px Andika; Kontraste WCAG AA; reduzierte Bewegung respektieren.
- HBG-SRL-Farben wie bei den Inputs: Schieferblau Navigation, Rostorange Aufträge/Aktionen, Salbeigrün gesicherte Antworten/Erfolg; Farbfotos (`assets/bilder/*_farbe.*`).
- PWA: `lernapp/index.html` (Inhalte + Logik in einer Datei), `lernapp/manifest.webmanifest`, `lernapp/sw.js` (Scope nur `/lernapp/`). „Zum Startbildschirm“, danach offline.
- Vorlesen über Web Speech API (lokal) für Interviews, Merkkarten, Aufträge.
- Optional Schalter **„Einfach“**: Förder-Kurzinterviews (`fischotter-f`, `erdmaennchen-f`) und F-Formate (ankreuzen, zuordnen, Lückentext).

## 8 · Generator und Prüfungen

`python tools/build_lernapp.py` → `lernapp/`. Automatische Prüfungen (Playwright, 390 × 844):
- kein horizontales Scrollen; Tippflächen ≥ 48 px; null Netzanfragen (auch offline neu laden)
- jede Übung lösbar; Lösungen = `interviews.json`-Markierungen; Merkkarten = Merkblatt-Text
- **Sperrliste:** Ausgabe enthält keine Wörter/Namen aus Probearbeit, Klassenarbeiten und GN-Auszügen (Waschbär, Rocky, Biber, Bruno, Breitmaulnashorn, Nala …) und keine Kiosk-Lösungstexte zu Blatt 1–9

## 9 · Deployment

- Ordner `lernapp/` im Repo `technikerleben/d5ur2-zootiere`; Adresse dann `<vercel-domain>/lernapp/`.
- Seit 10.10.2026 in `main`; Vercel liefert die App unter `/lernapp/` aus.
- Die Freigabe für Kinder steuert die Lehrkraft über den QR-Code. Klassenarbeiten werden später extern gespeichert.
- QR-Code auf Lernweg-Blatt und Elternzettel.

## 10 · Umsetzung in Schritten

1. **MVP:** Mein Weg, Wissen (Etappe 1–3, Strategiekarten), Interview-Detektiv, drei Sortier-/Auswahlübungen, Buchstabensalat, PWA.
2. **Ausbau:** Quiz je Etappe, Satzbau, Fehlerjagd, Silbenrätsel, Suchsel, Training (Giraffe, Ü1, Ü2), Zuhause mit Schreibplan und Selbstcheck.
3. **Feinschliff:** Schalter „Einfach“, Vorlesen überall, Elterninfo, QR-Zettel; Wissensbasis/Leitfaden ergänzen.

## 11 · Umsetzungsstand (10.10.2026)

**Gebaut:** Mein Weg (Etappen aus den Inhaltsdateien, Wahlzeit, Training, Klassenarbeit; Häkchen lokal) · Wissen (Merkkarten Etappe 1–3 wortgleich mit Input/Merkblatt, Antwort aufdecken; Strategiekarten 1–10; K1–K6; Wörterhilfe) · Üben: Finde den Fisch, Was zeigt das Foto?, Sachangabe/nur Otto/Meinung, Interview-Detektiv Fischotter, Sprachdetektiv, Genau statt wertend, Interview → Sachsprache, Verb-Werkstatt, Sätze bauen, Plan ordnen, Merkmale zählen, Fehlerjagd, Training Ü1/Ü2 als Interview-Detektiv · Buchstabenrätsel (24 Fachwörter) · Zuhause (Schritte, Ideen, Sicherheit, Schreibplan, Selbstcheck K1–K6) · Elterninfo mit „Alles löschen“ · Vorlesen · PWA offline.

**Prüfungen im Generator:** Sperrliste (Namen aus Probearbeit/Klassenarbeiten); app-eigene Texte dürfen keine Sätze aus Prüfungsinterviews, GN-Auszügen, Kiosk-Lösungen oder Training-Musterlösungen enthalten; Browsertest 390 × 844 (jede Übung lösbar, kein seitliches Scrollen, Tippflächen ≥ 44 px, keine Netzanfragen, offline, Speichern).

**Auslegung „keine Lösungen“:** Die App enthält keine Kiosk-Texte und keine Zeilenbelege. Übungen zum Fischotter berühren aber zwangsläufig dieselben Fakten wie Blatt 1–6 (sie stehen auch im Merkblatt). Erdmännchen und Roter Panda werden in der App nicht markiert oder geplant, damit Blatt 7 nicht vorweggenommen wird.

**Noch offen in der App:** Quiz je Etappe, Silbenrätsel und Suchsel, Giraffe als Beispielaufgabe, Schalter „Einfach“, QR-Zettel.

## 12 · Offen

- Angola-Giraffe aus `apps/beispielaufgabe-giraffe/index.html` in die Inhaltsdatei überführen. Pflegerin heißt dort „Frau Demir“ wie bei der Elenantilope → für die Giraffe neuen Namen wählen.
- Elterninfo-Text (Datenschutz, Zweck, keine Pflicht).
