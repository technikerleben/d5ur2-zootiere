# Deutsch 5 · Zootiere

Stand: 30.09.2026. Vier Wochen, acht Doppelstunden, Fischotter als Beispieltier.

## Verbindlicher SRL-Standard

**Etappen im eigenen Tempo: Startinput und identisches Merkblatt → Pflichtübungen mit freiwilligen Vertiefungen → Gelingensnachweis ab 80 %. Die letzte Etappe endet mit der Probearbeit → Feedback → Projekte / Wiederholung / nachgeholte Vertiefungen → Klassenarbeit an einem von zwei Wahlterminen.**

Der Standard ersetzt die frühere freie Übungsauswahl, den Verzicht auf eine Prozentgrenze und die Planung mit nur einem Klassenarbeitstermin. Der vorhandene Lernbuddy bleibt der laminierte Tischrahmen; Einführung außerhalb von Deutsch. Keine zusätzlichen SRL-Formulare auf Fachblättern.

| Etappe | Pflichtkern | Abschluss |
|---|---|---|
| 1 Informationen finden und ordnen | Blätter 1–4 mit freiwilligen Vertiefungen | GN1, mindestens 4/5 Indikatoren |
| 2 Sachlich und genau formulieren | Blätter 5–6 mit freiwilligen Vertiefungen | GN2, mindestens 4/5 Indikatoren |
| 3 Eine Tierbeschreibung schreiben und prüfen | Blätter 7–9 mit freiwilligen Vertiefungen | Probearbeit mit Feedback, mindestens 4/5 Indikatoren |

Bei unter 80 % gezielt nacharbeiten und erneut nachweisen. Förderziele vorab individuell festlegen. Das bisherige GN3-Gespräch wird als Übungsfeedback genutzt. Nach der Probearbeit stehen drei Projekte, Wiederholungen und nachgeholte Vertiefungen zur Wahl. Früher Klassenarbeitstermin in Doppelstunde 7, später in Doppelstunde 8; konkrete Daten, Dauer und Hilfen noch festzulegen. Früh geprüfte Kinder arbeiten anschließend an Projekten.

## Planung und Cockpit

- [Lehrkraft-Cockpit](index.html)
- [Verbindlicher Standard](planung/SRL_Standard.md)
- [Etappen und Kompetenzindikatoren](planung/Etappen_Gelingensnachweise.md)
- [Reihenplanung](planung/Reihenplanung_8_Doppelstunden.md)
- [Drei Projektangebote und Terminwahl](planung/Projekte_und_Terminwahl.md)
- [Projektgrundlage](planung/Projektgrundlage.md)
- [Kompetenzraster mit vier Standards](planung/Kompetenzraster_4_Standards.md)
- [Produktionsregeln](skill.md)

## Materialstatus

Planung und Cockpit sind auf den neuen Standard umgestellt. Vorhandene PDFs sind dadurch nicht automatisch neu erstellt. Tierpakete und K1–K6 bleiben fachlich nutzbar. Aufgaben, Merkblätter, Inputs, Lernweg und Nachweisauswertungen sind Vorfassungen und müssen vor erneuter Freigabe angepasst werden. Das Cockpit trennt diese Bereiche sichtbar.

Noch herzustellen: drei identische Input-/Merkblatt-Paare, Pflichtblätter mit integrierten Vertiefungen, neuer Lernweg und Schüler-Raster, 80-%-Erwartungshorizonte und Förderfassungen, Probearbeit/Feedback, Projekt-PDFs und zwei vergleichbare Klassenarbeitsvarianten. Die Projektaufträge sind bereits als Textgrundlage geplant. Kontroll-Kiosk und Vertretungshinweise folgen.

Schülerausgaben: A5 hoch, mindestens 14 pt einschließlich Beschriftungen, Graustufen, Lochrand, einfache Du-Form. Längere Texte ins Heft. Keine iPads; Online-Ressourcen für Lehrkräfte. Lernbuddy-Reflexion vor dem Abwischen ins Heft übertragen.

## Pflege und Erzeugung

`materialien/kompetenzen_etappen.json` enthält Kriterien und aktuelle Etappenstruktur. Die Planungs-HTML-Seiten und das Cockpit werden mit `python tools/build_srl_cockpit.py` aus den Planungsquellen erzeugt. Änderungen an fachlichen Planungen auch in den Cockpit-Zusammenfassungen nachziehen.

Die bisherigen PDF-Generatoren `generate_a5.py`, `generate_schritt4.py` und `generate_gelingensnachweise.py` sowie `generate_schritt2.py` sind für die Etappenstruktur zu überarbeiten; ihr unveränderter Aufruf erzeugt Vorfassungen. Vorhandene Prüfberichte gelten nur für die alten Ausgaben und belegen keine Freigabe nach dem neuen Standard. Schüler-PDFs erst nach technischer und visueller Prüfung ersetzen.

Das Cockpit ist statisch und benötigt keinen Build-Schritt auf Vercel. Das Deployment übernimmt der Nutzer. Es werden keine Vercel-Einstellungen verändert.
