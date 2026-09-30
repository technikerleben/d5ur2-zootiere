# Vorfassung – Anpassung erforderlich

Stand 30.09.2026: Der neue SRL-Etappenstandard ist verbindlich. Diese Ausgabe ist eine Vorfassung. Pflichtblätter mit freiwilligen Vertiefungen, identische Input-/Merkblatt-Paare und die 80-%-Auswertung werden noch angepasst. Das bisherige GN3-Gespräch dient nur als Übungsfeedback; die Probearbeit schließt Etappe 3 ab.

[Verbindlicher Standard](../../planung/SRL_Standard.md)

# Gelingensnachweise · Einsatz und Druck

Stand: 29.09.2026. Ergänzung zu den beschlossenen drei Etappen; keine zusätzliche Klassenarbeit.

| Datei | Einsatz | Umfang |
|---|---|---|
| [GN1 A](GN1_A_Tierdetektiv_A5.pdf) | Erster Nachweis nach Etappe 1 | 2 Seiten A5 |
| [GN1 B](GN1_B_Tierdetektiv_A5.pdf) | Erneuter Nachweis nach gezielter Übung | 2 Seiten A5 |
| [GN2 A](GN2_A_Genaue_Saetze_A5.pdf) | Erster Nachweis nach Etappe 2 | 1 Seite A5 |
| [GN2 B](GN2_B_Genaue_Saetze_A5.pdf) | Erneuter Nachweis nach gezielter Übung | 1 Seite A5 |
| [Schülerkarten gesamt](GN1_GN2_Schuelerkarten_A5.pdf) | Druckvorrat für Lehrkräfte; nicht alles gleichzeitig ausgeben | 6 Seiten A5 |
| [Erwartungshorizonte](GN1_GN2_Erwartungshorizonte_Lehrkraft_A4.pdf) | Lösungen, Kernziele, Hilfen und Weiterarbeit | 5 Seiten A4 |
| [Gesprächsleitfaden 3](GN3_Gespraechsleitfaden_Lehrkraft_A4.pdf) | Vorhandener Übungstext, Gespräch und Kurzprotokoll | 2 Seiten A4 |

## Durchführung

A für den ersten Versuch, B nach passender Teilübung. Bei nur einem offenen Ziel genügt die entsprechende B-Aufgabe; bereits gezeigte Ziele bleiben anerkannt. Die Varianten prüfen dieselben Kompetenzen. Ihre vergleichbare Schwierigkeit ist eine Planungsabsicht und noch nicht empirisch erprobt. GN1 B nutzt dasselbe Bild und einige gleiche Sachinformationen mit verändertem Text; es ist eine erneute Anwendung nach Übung, kein unabhängiger Transfertest.

GN1 und GN2: jeweils etwa 5–8 Minuten nach Auftragsklärung, keine harte Zeitgrenze. Antworten ins Heft. Bei GN1 beide Seiten zugänglich halten; Aufgabenblatt in die freie Mitte des vorhandenen Lernbuddys legen. Keine zusätzlichen SRL-Felder. Ein Zyklus kann mehrere Fachblätter umfassen; Reflexion vor dem Abwischen ins Heft übertragen.

Hilfen vorher vereinbaren und dokumentieren. Keine Lösung vorsagen; bei GN2 insbesondere nicht die richtigen Verbformen vorlesen. Fachliche Leistung und Lernbuddy-Nutzung getrennt rückmelden. Kein Punkteschnitt und keine pauschale Prozenthürde. Weiterarbeit anhand der Kernziele im Erwartungshorizont entscheiden.

Die Karten sind **keine individuelle Förderfassung**. Für zieldifferent lernende Kinder vorher passende Ziele, Hilfen und Antwortformen festlegen; die vereinbarten Ziele gesondert auswerten. Konkrete Förderkarten, Schüler-Raster und angepasster Lernweg sind noch zu erstellen.

GN3: vorhandenen Text zu Erdmännchen oder Rotem Panda nutzen. Vorher sichten, Gespräche während der Arbeitsphasen in Doppelstunden 4–5 staffeln. Protokolle mit Schülerdaten ausschließlich schulisch geschützt aufbewahren, nicht im Repository oder öffentlichen Cockpit.

## Druck und Prüfung

Schülerkarten: A5 hoch, mindestens 14 pt einschließlich Fußzeile, Graustufen, linker Rand 15 mm. Bei 100 % drucken; zwei A5-Seiten auf A4 nur ohne Verkleinerung. GN1-Material und Aufgaben für die gleichzeitige Nutzung vorzugsweise auf getrennte Blätter drucken. Bei Sammeldruck nur die benötigten Seiten auswählen. Lehrkraftdateien sind A4.

[Prüfbericht](Pruefbericht.json): Maße, Schriftgrößen und Textgrenzen automatisiert geprüft. Alle 13 eigenständigen Seiten der drei Sammel-/Lehrkraftdateien mit Poppler gerendert und visuell geprüft. Einzelkarten sind im Sammelpaket enthalten. Keine abgeschnittenen Texte festgestellt.

Erzeugung: `python tools/generate_gelingensnachweise.py` aus dem Repository-Stamm. Benötigt ReportLab, PyMuPDF, Pillow und DejaVu Sans. Die Bilddatei ist lokal eingebunden; zum Drucken und Bearbeiten wird kein Internet benötigt. Nachweise und Lösungen gehören nicht in den Kontroll-Kiosk.

## Bildquelle

Fischotterfoto: Dave Pape, Public Domain. [Original und Rechteangaben bei Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Lutra_lutra_1_-_Otter,_Owl,_and_Wildlife_Park.jpg). Verwendet aus dem bestehenden Fischotterpaket; für diese Karten in Graustufen umgewandelt. Lokale Datei: `Fischotter_DavePape_Graustufen.jpg`.

