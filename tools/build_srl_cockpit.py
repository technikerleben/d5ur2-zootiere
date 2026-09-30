from pathlib import Path
import html,re,json
r=Path(__file__).resolve().parents[1]
css='''*{box-sizing:border-box}body{margin:0;background:#f4f6f8;color:#18324a;font:18px/1.55 system-ui,sans-serif}main,header,footer{max-width:1120px;margin:auto;padding:24px}header{border-bottom:6px solid #48dccb}h1,h2,h3{line-height:1.2}h1{font-size:clamp(30px,5vw,46px)}h2{margin-top:0}a{color:#245688;text-underline-offset:3px}nav{display:flex;flex-wrap:wrap;gap:18px}section,.card,details{background:white;border:1px solid #d5dee6;border-radius:10px;padding:22px;margin:22px 0}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px}.grid .card{margin:0}.status{border-left:6px solid #f0a66f;padding:16px;background:#fff}table{border-collapse:collapse;width:100%;margin:18px 0}th,td{border:1px solid #cad5df;padding:12px;text-align:left;vertical-align:top}th{background:#eef4f8}summary{cursor:pointer;font-weight:bold}a:focus-visible,summary:focus-visible{outline:3px solid #245688;outline-offset:4px}.scroll{overflow-x:auto}.small{font-size:16px}@media(max-width:600px){header,main,footer{padding:16px}td,th{padding:8px}}'''
def page(title,body):return '<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>'+title+'</title><style>'+css+'</style></head><body>'+body+'</body></html>'
def inline(s):
 s=html.escape(s);s=re.sub(r'\*\*(.+?)\*\*',r'<strong>\1</strong>',s);s=re.sub(r'\[([^]]+)\]\(([^)]+)\)',r'<a href="\2">\1</a>',s);return s
# Lean renderer for these controlled planning files. Relative plan links resolve in planung/.
def md(s):
 out=[];table=False;lst=False
 for line in s.splitlines():
  if line.startswith('|'):
   if not table:out.append('<div class="scroll"><table>');table=True
   cells=line.strip('|').split('|')
   if all(re.fullmatch(r'\s*:?-+:?\s*',c) for c in cells):continue
   out.append('<tr>'+''.join('<td>'+inline(c.strip())+'</td>' for c in cells)+'</tr>');continue
  if table:out.append('</table></div>');table=False
  if re.match(r'^(- |\d+\. )',line):
   if not lst:out.append('<ul>');lst=True
   out.append('<li>'+inline(re.sub(r'^(- |\d+\. )','',line))+'</li>');continue
  if lst:out.append('</ul>');lst=False
  if line.startswith('#'):
   n=len(line)-len(line.lstrip('#'));out.append(f'<h{n}>'+inline(line[n:].strip())+f'</h{n}>')
  elif line.strip():out.append('<p>'+inline(line)+'</p>')
 if lst:out.append('</ul>')
 if table:out.append('</table></div>')
 return ''.join(out)
for name in ['SRL_Standard','Etappen_Gelingensnachweise','Reihenplanung_8_Doppelstunden','Projekte_und_Terminwahl','Materialmatrix']:
 body='<header><a href="../index.html">Zum Lehrkraft-Cockpit</a></header><main>'+md((r/'planung'/f'{name}.md').read_text())+'</main>'
 # Link to HTML companions for the four planning documents.
 for target in ['SRL_Standard','Etappen_Gelingensnachweise','Reihenplanung_8_Doppelstunden','Projekte_und_Terminwahl','Materialmatrix']:body=body.replace(target+'.md',target+'.html')
 (r/'planung'/f'{name}.html').write_text(page('Zootiere · '+name.replace('_',' '),body))
(r/'materialien/lehrkraft/Etappen_Gelingensnachweise.html').write_text(page('Zootiere · aktuelle Etappen','<main><h1>Aktuelle Etappenplanung</h1><p>Stand 30.09.2026: Pflichtübungen mit freiwilligen Vertiefungen, Wechsel ab 80 %, Abschluss der letzten Etappe durch Probearbeit und zwei Klassenarbeitstermine.</p><p><a href="../../planung/Etappen_Gelingensnachweise.html">Etappen, Indikatoren und Nachweise lesen</a></p><p><a href="../../index.html">Zum Cockpit</a></p></main>'))
body='''<header><p>OTTERKLASSE 5.3 · DEUTSCH · FÜR LEHRKRÄFTE</p><h1>Zootiere: Lernen in Etappen</h1><p>Stand: 30. September 2026 · vier Wochen · acht Doppelstunden · Fischotter als Beispieltier</p><nav><a href="#materialmatrix">Materialmatrix</a><a href="#etappen">Etappen</a><a href="#termine">Projekte und Termine</a><a href="#material">Materialstatus</a><a href="#planung">Planung</a></nav></header><main>
<p class="status"><strong>Neuer SRL-Standard verbindlich geplant.</strong> Die fachlichen Grundlagen sind vorhanden. Angepasste Schülerausgaben, Probearbeit, Projekt-PDFs und zwei Klassenarbeitsvarianten sind noch herzustellen. Alte Downloads sind ausdrücklich als Vorfassungen gekennzeichnet.</p>
<section id="materialmatrix"><h2>Schritt 1 abgeschlossen · Materialmatrix</h2><p>Pflichtumfang, integrierte Vertiefungen und Kompetenzbezug sind festgelegt. Neun Pflichtblätter: rund 200 Minuten als ungetesteter Planungswert. Alle 15 Etappenindikatoren werden vorher erklärt und verbindlich geübt.</p><p><a href="planung/Materialmatrix.html">Materialmatrix und 720-Minuten-Zeitprüfung lesen</a> · <a href="planung/Materialmatrix.md">Quelldokument</a></p><p>Schülerausgaben noch herzustellen. 45 Minuten für Probe-/Klassenarbeit dienen vorläufig der Kapazitätsprüfung; endgültige Dauer und Hilfen stehen noch aus. Nächster Produktionsschritt: Etappe 1 mit Input/Merkblatt, Pflichtblättern 1–4, Hilfen und GN1.</p></section><section id="etappen"><h2>Dein Tempo – klare Etappen</h2><p>Je Etappe: <strong>Startinput + identisches Merkblatt → Pflichtübungen mit freiwilligen Vertiefungen → Gelingensnachweis.</strong> Die letzte Etappe endet mit der Probearbeit.</p><div class="grid">
<article class="card"><h3>1 · Informationen</h3><p>Bild und Text auswerten, Merkmale und Sachinformationen ordnen.</p><p><strong>Pflicht:</strong> Blätter 1–4<br><strong>Abschluss:</strong> GN1 Tierdetektiv</p></article>
<article class="card"><h3>2 · Sachliche Sprache</h3><p>Genaue Wörter und vollständige Sätze im Präsens nutzen.</p><p><strong>Pflicht:</strong> Blätter 5–6<br><strong>Abschluss:</strong> GN2 Genaue Sätze</p></article>
<article class="card"><h3>3 · Schreiben und Prüfen</h3><p>Eine Beschreibung planen, schreiben und überarbeiten.</p><p><strong>Pflicht:</strong> Blätter 7–9<br><strong>Abschluss:</strong> Probearbeit mit Feedback</p></article></div>
<p><strong>Weiter ab 80 %:</strong> Vier von fünf vorab festgelegten Kompetenzindikatoren ermöglichen den Wechsel. Unter 80 % folgen gezielte Übung und erneuter Nachweis. Freiwillige Vertiefungen zählen nicht zur Freigabe. Individuelle Förderziele werden vorab vereinbart.</p><p><a href="planung/Etappen_Gelingensnachweise.html">Indikatoren und Etappen lesen</a></p><p>Die Lernenden arbeiten im eigenen Tempo. Zeitversetzte kurze Inputs und die identischen Papiermerkblätter ermöglichen den Einstieg. Der vorhandene Lernbuddy steuert die Arbeit; die A5-Aufgabe liegt in seiner Mitte.</p></section>
<section id="termine"><h2>Nach der Probearbeit: Feedback und Wahlzeit</h2><p>Wähle ein Projekt, wiederhole Aufgaben oder hole freiwillige Vertiefungen nach. Projekte sind für Einzelarbeit oder Kleingruppen vorgesehen.</p><div class="grid"><article class="card"><h3>Unser Tierlexikon</h3><p>Vorhandenen Text prüfen, bebildern und Merkmale beschriften.</p></article><article class="card"><h3>Welches Tier ist gemeint?</h3><p>Genaue Rätselkarten mit getrennten Lösungen und Materialbelegen herstellen.</p></article><article class="card"><h3>Tiervergleich</h3><p>Zwei bekannte Tiere anhand gleicher Merkmale vergleichen und Unterschiede erklären.</p></article></div><p><a href="planung/Projekte_und_Terminwahl.html">Projektaufträge und Organisation lesen</a> · Textgrundlagen fertig, Schüler-PDFs noch ausstehend.</p>
<div class="scroll"><table><thead><tr><th>Wahltermin</th><th>Vorgesehen</th><th>Parallel und danach</th></tr></thead><tbody><tr><td>Früh</td><td>Doppelstunde 7</td><td>Andere Kinder bereiten sich vor oder arbeiten still an Projekten. Früh geprüfte Kinder nutzen die verbleibende Zeit für Projekte.</td></tr><tr><td>Spät</td><td>Doppelstunde 8</td><td>Bereits geprüfte Kinder arbeiten still an Projekten.</td></tr></tbody></table></div><p>Jedes Kind schreibt regulär einmal. Feedback zur Probearbeit vor der Prüfung geben. Konkrete Daten, Dauer, Hilfen und Wahlfrist werden noch festgelegt; getrennte gleichwertige Prüfungsvarianten sind noch zu erstellen.</p></section>
<section id="material"><h2>Materialstatus</h2><div class="scroll"><table><thead><tr><th>Bereich</th><th>Stand</th><th>Nächster Schritt</th></tr></thead><tbody><tr><td>Tierpakete und K1–K6</td><td>Fachlich vorhanden</td><td>Für neue Aufgaben weiterverwenden</td></tr><tr><td>Input / Merkblatt</td><td>Vier alte Inputs, drei Merkblätter</td><td>Drei inhaltlich identische Paare erzeugen</td></tr><tr><td>Pflichtblätter 1–9</td><td>Fachaufgaben vorhanden</td><td>Pflichtkern und freiwillige Vertiefungen ausweisen</td></tr><tr><td>GN1 / GN2</td><td>Karten A/B vorhanden</td><td>Auswertung auf fünf Indikatoren und 4/5-Freigabe umstellen</td></tr><tr><td>Bisheriges GN3</td><td>Gesprächsleitfaden vorhanden</td><td>Als begleitendes Übungsfeedback nutzen</td></tr><tr><td>Probearbeit + Feedback</td><td>Geplant; Tiermaterial reserviert</td><td>Abschluss von Etappe 3 herstellen</td></tr><tr><td>Drei Projekte</td><td>Textaufträge geplant</td><td>A5-Schülerausgaben herstellen</td></tr><tr><td>Zwei Klassenarbeitstermine</td><td>Zeitfenster geplant</td><td>Zwei Varianten und Terminwahl vorbereiten</td></tr><tr><td>Lernweg / Schüler-Raster</td><td>Überarbeitung ausstehend</td><td>Etappen, 80 % und Wahltermine sichtbar machen</td></tr></tbody></table></div>
<h3 id="tiermaterial">Fachliche Grundlagen</h3><ul>'''
for label,href in [('Fischotter','materialien/tierpakete/fischotter_A5.pdf'),('Erdmännchen','materialien/tierpakete/erdmaennchen_A5.pdf'),('Roter Panda','materialien/tierpakete/roter-panda_A5.pdf'),('Kindercheckliste K1–K6','materialien/bewertung/Kindercheckliste_A5.pdf'),('Kompetenzraster mit vier Standards','materialien/bewertung/Kompetenzraster_4_Standards.html')]:body+=f'<li><a href="{href}">{label}</a></li>'
body+='</ul><details id="schritt4"><summary>Vorfassungen: Aufgaben, Merkblätter, Inputs und Lernweg</summary><p>Zur Überarbeitung bereitgehalten. Diese Ausgaben bilden den neuen SRL-Standard noch nicht vollständig ab. Nicht als aktualisiertes Gesamtpaket ausgeben.</p><ul>'
for label,href in [('Aufgaben 1–10','materialien/schritt4/Aufgaben_1-10_A5.pdf'),('Merkblätter 1–3','materialien/schritt4/Merkblaetter_1-3_A5.pdf'),('Tipps 1–10','materialien/schritt4/Tipps_1-10_A5.pdf'),('Lösungen 1–10','materialien/schritt4/Loesungen_1-10_A5.pdf'),('Vier bisherige Inputs','inputs/Zootiere_Inputs.html'),('Bisheriger Lernweg','materialien/lernweg/Mein_Lernweg_Zootiere_A5.pdf'),('Bisheriges Grundpaket','materialien/Schuelermaterial_Zootiere_A5.pdf')]:body+=f'<li><a href="{href}">{label} – Vorfassung</a></li>'
body+='</ul></details><details id="nachweise"><summary>Vorfassungen: Nachweiskarten und Gesprächsleitfaden</summary><p>Karten als Grundlage vorhanden. Die alte Auswertung ohne 80-%-Schwelle ist überholt. Das alte GN3-Gespräch ist nur Übungsfeedback, nicht der Abschluss von Etappe 3.</p><ul>'
for label,fn in [('GN1/GN2 A/B','GN1_GN2_Schuelerkarten_A5.pdf'),('Alte Erwartungshorizonte – zu ersetzen','GN1_GN2_Erwartungshorizonte_Lehrkraft_A4.pdf'),('Übungsfeedback – bisher als GN3 bezeichnet','GN3_Gespraechsleitfaden_Lehrkraft_A4.pdf')]:body+=f'<li><a href="materialien/gelingensnachweise/{fn}">{label}</a></li>'
body+='</ul></details></section><section id="planung"><h2>Verbindliche Planung</h2><ul>'
for label,fn in [('Materialmatrix · Schritt 1','Materialmatrix'),('SRL-Standard','SRL_Standard'),('Etappen und Gelingensnachweise','Etappen_Gelingensnachweise'),('Acht Doppelstunden','Reihenplanung_8_Doppelstunden'),('Projekte und Terminwahl','Projekte_und_Terminwahl')]:body+=f'<li><a href="planung/{fn}.html">{label}</a> · <a href="planung/{fn}.md">Quelldokument</a></li>'
body+='''</ul><p><a href="planung/Projektgrundlage.md">Projektgrundlage</a> · <a href="skill.md">Produktionsregeln</a></p></section><section id="ausblick"><h2>Nächste Produktion</h2><ol><li>Input-/Merkblatt-Paare, Pflichtblätter mit Vertiefungen und Lernweg aktualisieren.</li><li>80-%-Nachweise und individuelle Förderfassungen ausarbeiten.</li><li>Probearbeit, Feedback und Projekt-PDFs erstellen.</li><li>Zwei Klassenarbeitsvarianten, Terminwahl und Kontroll-Kiosk herstellen.</li></ol><p>Alle Schülerarbeitsblätter bleiben A5 mit mindestens 14 pt. Online-Angebote dienen Lehrkräften; Lernende arbeiten auf Papier und im Heft. Der geplante Kontroll-Kiosk am Raum-Laptop ist die einzige digitale Schüleranwendung.</p></section></main><footer>Deutsch 5.3 · Zootiere · Planung und Produktionsstand getrennt dargestellt.</footer>'''

# Current release: Etappe 1. Keep older combined files labelled as drafts.
body=body.replace('Die fachlichen Grundlagen sind vorhanden. Angepasste Schülerausgaben, Probearbeit, Projekt-PDFs und zwei Klassenarbeitsvarianten sind noch herzustellen.', 'Etappe 1 ist erstellt und als A5-Paket verfügbar. Etappe 2/3, der vollständige Lernweg, Probearbeit, Projekt-PDFs und zwei Klassenarbeitsvarianten folgen noch.')
body=body.replace('Schülerausgaben noch herzustellen.', 'Schülerausgaben für Etappe 1 sind unten verfügbar; weitere Etappen folgen.')
body=body.replace('Nächster Produktionsschritt: Etappe 1 mit Input/Merkblatt, Pflichtblättern 1–4, Hilfen und GN1.', 'Nächster Produktionsschritt: Etappe 2 mit Input/Merkblatt, Pflichtblättern 5–6, Hilfen und GN2.')
body=body.replace('<a href="#materialmatrix">Materialmatrix</a>','<a href="#etappe1">Etappe 1: Downloads</a><a href="#materialmatrix">Materialmatrix</a>')
release='<section id="etappe1"><h2>Etappe 1 · erstellt und druckfertig</h2><p>Input und Merkblatt mit identischem fachlichem Inhalt. Pflichtblätter 1–4 enthalten freiwillige Vertiefungen. GN1: vier von fünf Zielen ermöglichen den Wechsel. PDF-Format, Schriftgrößen und gerenderte Seiten geprüft; Unterrichtserprobung steht aus.</p><div class="grid">'
for title,fn,desc in [('Schülerpaket','Etappe1_Schuelerpaket_A5.pdf','9 Seiten A5: Merkblatt, Tiermaterial und vier Pflichtblätter.'),('Startinput','Input_Etappe1.html','15 Folien für Lehrkräfte, gleiche Inhalte wie das Merkblatt.'),('Tipps','Tipps_1-4_A5.pdf','Vier A5-Seiten, getrennt bereitstellen.'),('Lösungen','Loesungen_1-4_A5.pdf','Vier A5-Seiten zum Vergleichen.'),('GN1 A','GN1_A_A5.pdf','Zwei A5-Seiten für den ersten Nachweis.'),('GN1 B','GN1_B_A5.pdf','Zwei A5-Seiten für erneute Belege nach Übung.'),('Auswertung und Einsatz','Lehrkraft_Auswertung_A4.pdf','Fünf Lehrkraftseiten: Kriterien, Lösungen, Kurzprotokoll, Förderhinweise.'),('Fördermodule','Foerdermodule_A5.pdf','Vier A5-Seiten, individuell auswählen und Ziele vereinbaren.')]:
 release+=f'<article class="card"><h3>{title}</h3><p>{desc}</p><a href="materialien/etappe1/{fn}">Öffnen</a></article>'
release+='</div><p>Alle Schülerseiten: mindestens 14 pt, Graustufen, Lochrand. Tipps, Lösungen und Nachweise sind nicht im Grundpaket.</p><p><a href="materialien/etappe1/Merkblatt_1_A5.pdf">Merkblatt einzeln</a> · <a href="materialien/etappe1/Fischotter_Material_A5.pdf">Tiermaterial einzeln</a> · <a href="materialien/etappe1/Pflichtblaetter_1-4_A5.pdf">Pflichtblätter einzeln</a> · <a href="materialien/etappe1/README.md">Einsatz und Druckhinweise</a></p></section>'
body=body.replace('<section id="etappen">',release+'<section id="etappen">')
body=body.replace('<td>Vier alte Inputs, drei Merkblätter</td><td>Drei inhaltlich identische Paare erzeugen</td>','<td>Etappe 1 als identisches Paar erstellt</td><td>Paare für Etappe 2/3 herstellen</td>')
body=body.replace('<td>Fachaufgaben vorhanden</td><td>Pflichtkern und freiwillige Vertiefungen ausweisen</td>','<td>Blätter 1–4 mit Pflicht/Vertiefung erstellt</td><td>Blätter 5–9 entsprechend überarbeiten</td>')
body=body.replace('<td>Karten A/B vorhanden</td><td>Auswertung auf fünf Indikatoren und 4/5-Freigabe umstellen</td>','<td>GN1 A/B mit 4/5-Auswertung erstellt</td><td>GN2 entsprechend überarbeiten</td>')

(r/'index.html').write_text(page('Zootiere · SRL-Etappen und Material-Cockpit',body))
(r/'README.md').write_text('''# Deutsch 5 · Zootiere

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

Nächster Produktionsauftrag: Etappe 1 vollständig herstellen – gemeinsamer Input-/Merkblatt-Inhalt, Pflichtblätter 1–4 mit Vertiefungen, Hilfen/Lösungen und GN1 mit 4/5-Freigabe. Neue Schüler-PDFs sind noch nicht erstellt.

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
''')



# Update generated README without advertising unfinished later stages.
p=r/'README.md';text=p.read_text()
text=text.replace('Nächster Produktionsauftrag: Etappe 1 vollständig herstellen – gemeinsamer Input-/Merkblatt-Inhalt, Pflichtblätter 1–4 mit Vertiefungen, Hilfen/Lösungen und GN1 mit 4/5-Freigabe. Neue Schüler-PDFs sind noch nicht erstellt.', 'Etappe 1 ist hergestellt. Nächster Produktionsauftrag: Etappe 2 mit identischem Input/Merkblatt, Pflichtblättern 5–6 und GN2.')
text=text.replace('Aufgaben, Merkblätter, Inputs, Lernweg und Nachweisauswertungen sind Vorfassungen und müssen vor erneuter Freigabe angepasst werden.', 'Die alten Gesamtpakete bleiben Vorfassungen. Aktuell ist Etappe 1 unter materialien/etappe1; weitere Etappen, Lernweg und Auswertungen folgen noch.')
text=text.replace('Noch herzustellen: drei identische Input-/Merkblatt-Paare, Pflichtblätter mit integrierten Vertiefungen, neuer Lernweg und Schüler-Raster, 80-%-Erwartungshorizonte und Förderfassungen, Probearbeit/Feedback, Projekt-PDFs und zwei vergleichbare Klassenarbeitsvarianten.', 'Noch herzustellen: Etappe 2/3 mit identischen Input-/Merkblatt-Paaren, Pflichtblättern mit Vertiefungen, Nachweisen und Förderangeboten, neuer Lernweg und Schüler-Raster, Probearbeit/Feedback, Projekt-PDFs und zwei vergleichbare Klassenarbeitsvarianten.')
text+='\n## Etappe 1 verfügbar\n\n- [Schülerpaket A5, 9 Seiten](materialien/etappe1/Etappe1_Schuelerpaket_A5.pdf)\n- [Input für Lehrkräfte](materialien/etappe1/Input_Etappe1.html)\n- [Alle Einzeldateien, Tipps, Lösungen, GN1 A/B und Fördermodule](materialien/etappe1/README.md)\n- [Auswertung und Einsatz](materialien/etappe1/Lehrkraft_Auswertung_A4.pdf)\n\nGenerator: `python tools/generate_etappe1.py`. Gemeinsame Inhaltsquelle: `materialien/etappe1/inhalt.json`. Technischer Inhaltsabgleich sowie technische und visuelle PDF-Prüfung abgeschlossen. Die HTML-Navigation wurde technisch geprüft; visuelle Browserprüfung steht noch aus.\n'
p.write_text(text)
