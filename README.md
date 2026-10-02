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

## Schritt 1 abgeschlossen · Materialmatrix

[Materialmatrix](planung/Materialmatrix.md) mit Input-/Merkblatt-Inhalten, neun Pflichtblättern, freiwilligen Vertiefungen, Hilfen und vollständiger Zuordnung der 15 Etappenindikatoren. Pflichtumfang: rund 200 Minuten als ungetesteter Planungswert. Acht Zeitfenster zu je 90 Minuten sichern Platz für Nachweise, Rückmeldung, Wahlzeit und zwei Klassenarbeitstermine. Die dort angesetzten 45 Prüfungsminuten sind noch keine endgültige Festlegung.

Alle drei Etappen einschließlich Probearbeit und Feedback sind hergestellt. Lernweg, Schüler-Kompetenzraster, Projekte und Wiederholungshilfe sind ebenfalls hergestellt. Nächster Produktionsauftrag: zwei vergleichbare Klassenarbeitsvarianten mit Bewertung und Prüfungsorganisation.

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

Planung und Cockpit sind auf den neuen Standard umgestellt. Vorhandene PDFs sind dadurch nicht automatisch neu erstellt. Tierpakete und K1–K6 bleiben fachlich nutzbar. Die alten Gesamtpakete bleiben Vorfassungen. Aktuell sind alle drei Etappen unter materialien/etappe1 bis materialien/etappe3 verfügbar. Lernweg, Schüler-Raster und Projektangebote mit Wiederholungshilfe sind ebenfalls verfügbar. Das Cockpit trennt diese Bereiche sichtbar.

Noch herzustellen: zwei vergleichbare Klassenarbeitsvarianten. Termine, Dauer, Hilfen und Wahlfrist sind vor Durchführung festzulegen. Kontroll-Kiosk und Vertretungshinweise folgen.

Schülerausgaben: A5 hoch, mindestens 14 pt einschließlich Beschriftungen, Graustufen, Lochrand, einfache Du-Form. Längere Texte ins Heft. Keine iPads; Online-Ressourcen für Lehrkräfte. Lernbuddy-Reflexion vor dem Abwischen ins Heft übertragen.

## Pflege und Erzeugung

`materialien/kompetenzen_etappen.json` enthält Kriterien und aktuelle Etappenstruktur. Die Planungs-HTML-Seiten und das Cockpit werden mit `python tools/build_srl_cockpit.py` aus den Planungsquellen erzeugt. Änderungen an fachlichen Planungen auch in den Cockpit-Zusammenfassungen nachziehen.

Die bisherigen PDF-Generatoren `generate_a5.py`, `generate_schritt4.py` und `generate_gelingensnachweise.py` sowie `generate_schritt2.py` sind für die Etappenstruktur zu überarbeiten; ihr unveränderter Aufruf erzeugt Vorfassungen. Vorhandene Prüfberichte gelten nur für die alten Ausgaben und belegen keine Freigabe nach dem neuen Standard. Schüler-PDFs erst nach technischer und visueller Prüfung ersetzen.

Das Cockpit ist statisch und benötigt keinen Build-Schritt auf Vercel. Das Deployment übernimmt der Nutzer. Es werden keine Vercel-Einstellungen verändert.

## Etappe 1 verfügbar

- [Schülerpaket A5, 9 Seiten](materialien/etappe1/Etappe1_Schuelerpaket_A5.pdf)
- [Input für Lehrkräfte](materialien/etappe1/Input_Etappe1.html)
- [Alle Einzeldateien, Tipps, Lösungen, GN1 A/B und Fördermodule](materialien/etappe1/README.md)
- [Auswertung und Einsatz](materialien/etappe1/Lehrkraft_Auswertung_A4.pdf)

Generator: `python tools/generate_etappe1.py`. Gemeinsame Inhaltsquelle: `materialien/etappe1/inhalt.json`. Technischer Inhaltsabgleich sowie technische und visuelle PDF-Prüfung abgeschlossen. Die HTML-Navigation wurde technisch geprüft; visuelle Browserprüfung steht noch aus.

## Etappe 2 verfügbar

- [Schülerpaket A5, 5 Seiten](materialien/etappe2/Etappe2_Schuelerpaket_A5.pdf)
- [Input für Lehrkräfte](materialien/etappe2/Input_Etappe2.html)
- [Einzeldateien, Tipps, Lösungen, GN2 A/B und Fördermodule](materialien/etappe2/README.md)
- [Auswertung und Einsatz](materialien/etappe2/Lehrkraft_Auswertung_A4.pdf)

Generator: `python tools/generate_etappe2.py`. Gemeinsame Inhaltsquelle: `materialien/etappe2/inhalt.json`. PDF-Prüfung und Inhaltsabgleich abgeschlossen; Navigation technisch geprüft, visuelle Browserprüfung noch offen.

## Etappe 3 verfügbar

- [Schülerpaket A5, 9 Seiten](materialien/etappe3/Etappe3_Schuelerpaket_A5.pdf)
- [Identischer Input für Lehrkräfte](materialien/etappe3/Input_Etappe3.html)
- [Probearbeit Waschbär](materialien/etappe3/Probearbeit_Waschbaer_A5.pdf) und [Feedback](materialien/etappe3/Feedback_Probearbeit_A5.pdf)
- [Alle Einzeldateien, Hilfen, Fördermodule und erneuten Belege](materialien/etappe3/README.md)
- [Lehrkraft-Auswertung mit Ankerbeispielen](materialien/etappe3/Lehrkraft_Auswertung_A4.pdf)

Generator: `python tools/generate_etappe3.py`. Inhalt und PDF-Ausgaben geprüft; HTML-Navigation technisch geprüft. Visuelle Browserprüfung und Unterrichtserprobung stehen aus. Für die Probearbeit sind 45 Minuten Arbeitsannahme; konkrete Dauer und Hilfen vor Durchführung ankündigen.

## Lernweg und Wahlphase verfügbar

[Alle Downloads, Kompetenzübersichten, drei Projekte und Wiederholungshilfe](materialien/lernweg_wahlphase/README.md). Schülerausgaben A5 mit mindestens 14 pt, technisch und visuell geprüft. Der vollständige Vier-Standards-Raster übernimmt alle 24 Beschreibungen wortgleich aus der Kompetenzquelle. Generator: `python tools/generate_lernweg_wahlphase.py`.
