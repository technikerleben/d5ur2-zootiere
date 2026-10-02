# Etappe 1 · Grafische Graustufenfassung

Für die Otterklasse 5.3 und die Dino-Klasse 5.5. Stand: 02.10.2026.

- [Schülerpaket: neun Seiten](Etappe1_Schuelerpaket_A5_grafisch_graustufen.pdf)
- [Pflichtarbeitsblätter 1–4: vier Seiten](Pflichtblaetter_1-4_A5_grafisch_graustufen.pdf)

Inhalt und Seitenfolge entsprechen der bisherigen Schülerausgabe. Das Paket enthält vier Merkblattseiten, eine Fischotter-Materialseite und vier Pflichtarbeitsblätter mit freiwilligen Vertiefungen. Lösungen, Tipps und Gelingensnachweise bleiben separat. Der fachliche Input bleibt damit 1:1 zum Merkblatt passend.

Otter und Stegosaurus sind Klassenmaskottchen im Kopfbereich jeder Seite. Sie dienen nicht als fachliche Bildquelle. Die ursprünglichen Fischotterfotos samt Quellenangabe bleiben erhalten. Die Fußzeile nennt beide Klassen.

A5 hoch, mindestens 14 pt einschließlich Fußzeile, 15 mm Lochrand, reine Graustufen. In tatsächlicher Größe drucken; bei A4 zwei A5-Seiten ohne Verkleinerung auf einen Druckbogen setzen. Bearbeitung weiterhin im Heft und mit dem vorhandenen Lernbuddy.

## Herstellung und Prüfung

`python tools/generate_etappe1_grafisch.py` erzeugt beide PDFs aus der bestehenden Inhaltsquelle `materialien/etappe1/inhalt.json`. Die ursprünglichen PDFs bleiben unverändert. Schrift: DejaVu Sans; Mascot-Illustration mit Bildgenerierung erstellt, für den Druck in Graustufen eingebettet. Das Bildasset liegt unter `assets/Otter_und_Dino.png`.

[Prüfbericht](Pruefbericht.json): seitenweiser Textvergleich gegen das Original, Format, Mindestschrift, Ränder und reine Graustufen technisch geprüft. Alle neun Seiten visuell geprüft. Die Textkontrolle erlaubt ausschließlich die Erweiterung der Klassenangabe in der Fußzeile. Nach neuer Erzeugung ist die visuelle Prüfung zu wiederholen.
