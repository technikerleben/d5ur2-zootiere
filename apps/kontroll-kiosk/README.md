# Kontroll-Kiosk · Zootiere

Nachbau des Kiosks aus der Reihe Wunschbriefe, neutral gestaltet (Graustufen, ohne Maskottchen).

## Im Raum

Der Kiosk läuft auf dem Klassenraum-Laptop. Kinder wählen „Tipp“ oder „Lösung“, geben Blatt 1–9 über Tastatur oder Zahlenfeld ein und wählen „Anzeigen“ (oder Enter). Am Ergebnis kann zwischen Tipp und Lösung gewechselt werden. Die freiwillige Vertiefung öffnet sich erst beim Anklicken. Danach „Zurück zum Start“.

- Beim Lesen keine Zeitbegrenzung. Bei der Nummerneingabe führt eine Pause von drei Minuten zum Start.
- Escape: Start · Backspace: Ziffer löschen · Delete: Eingabe löschen · Vollbildknopf, ersatzweise F11.
- Eine Datei, alle Inhalte und die Schrift sind eingebettet. Nach dem Speichern keine Internetverbindung nötig. Es werden keine Kinderdaten gespeichert.
- Direktaufruf für die Lehrkraft: `index.html?mode=solution&blatt=7`

## Grenzen

Geschlossene Aufgaben erhalten konkrete Antworten, offene Aufgaben Vergleichsbeispiele, Teilbeispiele und Prüffragen. Blatt 8 und 9 enthalten bewusst keinen vollständigen Mustertext. Andere Lösungen sind richtig, wenn sie zum Material passen. Die Kiosktexte sind Orientierung, keine Bewertung.

Der Kiosk gehört nicht zu Gelingensnachweisen, Probearbeit oder Klassenarbeit; dafür gibt es keine Einträge.

## Pflege

Texte: `inhalt/kiosk.json`. Titel und Blattnummern kommen aus `inhalt/etappeN.json`. Erzeugen und prüfen: `python tools/build_kiosk.py` (prüft alle Tipp- und Lösungsansichten, Zahlenfeld, Fehlermeldung, Wechsel, Escape, schmale Ansicht und Offlinebetrieb im Browser).
