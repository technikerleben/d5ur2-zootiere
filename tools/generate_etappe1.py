"""Generate Etappe 1 PDFs and teacher input from one content source."""
from pathlib import Path
import json,re,html,hashlib
import fitz
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'materialien/etappe1';DATA=json.loads((OUT/'inhalt.json').read_text())
PHOTO=ROOT/'materialien/gelingensnachweise/Fischotter_DavePape_Graustufen.jpg'
SOURCE='https://commons.wikimedia.org/wiki/File:Lutra_lutra_1_-_Otter,_Owl,_and_Wildlife_Park.jpg'
for name,font in [('Text','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf')]:pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+font))
manifest=[]
class Doc:
 def __init__(self,name,a4=False):
  self.path=OUT/name;self.w,self.h=(595.276,841.89) if a4 else (419.528,595.276);self.left=42.52;self.width=self.w-self.left-28.35;self.n=0
  self.c=canvas.Canvas(str(self.path),pagesize=(self.w,self.h));self.c.setTitle(name.replace('_',' '));self.c.setAuthor('Deutsch 5.3 - Zootiere')
 def p(self,s,size=14,bold=False,gap=9):
  p=Paragraph(s,ParagraphStyle('p',fontName='Bold' if bold else 'Text',fontSize=size,leading=size*1.28));_,height=p.wrap(self.width,2000)
  assert self.y+height<=self.h-48,(self.path.name,self.n,self.y,height,s)
  p.drawOn(self.c,self.left,self.h-self.y-height);self.y+=height+gap
 def page(self,label,title):
  if self.n:self.c.showPage()
  self.n+=1;self.c.setStrokeGray(.2);self.c.setLineWidth(1.2);self.c.line(self.left,self.h-25,self.w-28.35,self.h-25);self.y=35
  self.p(label,14,True,8);self.p(title,21,True,14)
  self.c.setFont('Text',14);self.c.drawString(self.left,22,'Deutsch 5.3 | Etappe 1');self.c.drawRightString(self.w-28.35,22,str(self.n))
 def block(self,title,s):self.p(title,15,True,4);self.p(s,14,gap=12)
 def photo(self,height=115):
  from PIL import Image
  w,h=Image.open(PHOTO).size;iw=height*w/h;self.c.drawImage(str(PHOTO),self.left+(self.width-iw)/2,self.h-self.y-height,iw,height);self.y+=height+8
  self.p('Foto: Dave Pape | Public Domain',14,gap=3);self.p('<link href="'+SOURCE+'"><u>Bildquelle</u></link> | Graustufenfassung',14,gap=10)
 def end(self):
  self.c.save();manifest.append({'path':str(self.path.relative_to(ROOT)),'pages':self.n,'student':self.w<500})
def memo():
 d=Doc('Merkblatt_1_A5.pdf')
 for n,item in enumerate(DATA['memo'],1):
  d.page('Merkblatt 1 | '+str(n)+'/4',item['title'])
  if item.get('photo'):d.photo(112)
  for title,s in item['blocks']:d.block(title,s)
 d.end()
def material():
 d=Doc('Fischotter_Material_A5.pdf');d.page('Material zu Blatt 1–4','Der Fischotter');d.photo(125);d.p(DATA['text']);d.end()
def exercises():
 d=Doc('Pflichtblaetter_1-4_A5.pdf')
 for w in DATA['worksheets']:
  d.page('Blatt '+str(w['n'])+' | Pflicht + freiwillig',w['title']);d.p('Du brauchst: '+w['material']+'.',gap=12)
  for title,s in w['blocks']:d.block(title,s)
 d.end()
 for key,label,filename in [('tips','Tipp','Tipps_1-4_A5.pdf'),('solutions','Lösung','Loesungen_1-4_A5.pdf')]:
  d=Doc(filename)
  for n,items in enumerate(DATA[key],1):
   d.page(label+' zu Blatt '+str(n),DATA['worksheets'][n-1]['title'])
   for s in items:d.p(s,gap=17)
   if key=='tips':d.p('Probiere es jetzt selbst. Nutze die Lösung erst zum Vergleichen.',gap=0)
  d.end()
def gn(v):
 text= ('Der Fischotter hat einen lang gestreckten Körper und kurze Beine. Sein Fell ist oben dunkelbraun. Er lebt an Flüssen und Seen. Er frisst vor allem Fische, aber auch Frösche und Krebse. Kopf und Rumpf sind zusammen 60 bis 90 Zentimeter lang. Der Schwanz kommt noch dazu.' if v=='A' else 'An Flüssen und Seen lebt der Fischotter. Zu seiner Nahrung gehören Fische, Frösche und Krebse. Sein Kopf ist breit und flach. Seine Beine sind kurz. Kopf und Rumpf messen zusammen 60 bis 90 Zentimeter. Der Schwanz wird dabei nicht mitgemessen.')
 d=Doc('GN1_'+v+'_A5.pdf');d.page('Nachweis 1'+v+' | Material','Der Fischotter');d.photo(125);d.p(text);d.page('Nachweis 1'+v+' | Aufgaben','Zeige dein Können')
 d.p('Nutze die Materialseite. Schreibe „1'+v+'“ über deine Antworten im Heft.')
 d.block('1 | Merkmale und Quellen','Notiere zwei verschiedene genaue äußere Merkmale: eines aus dem Bild (B), ein anderes aus dem Text (T). Zeige beide Fundstellen.')
 d.block('2 | Das Maß','Notiere die Länge von Kopf und Rumpf mit Einheit. Schreibe dazu, ob der Schwanz mitgezählt wird.')
 d.block('3 | Informationen ordnen','Schreibe die Überschriften Lebensraum und Nahrung ins Heft. Notiere darunter je eine richtige Angabe aus dem Text.')
 d.p('Fünf Ziele: zwei Merkmale, Quellen zeigen, Maß angeben, Lebensraum/Nahrung finden, Angaben ordnen.<br/>Vier von fünf = 80 %. Dann kannst du weitergehen. Es gibt keine Note.',gap=0);d.end()
def foerder():
 d=Doc('Foerdermodule_A5.pdf')
 for n,item in enumerate(DATA['foerder'],1):
  d.page('Fördermodul '+str(n)+' | nach Vereinbarung',item['title'])
  for title,s in item['blocks']:d.block(title,s)
 d.end()
def teacher():
 d=Doc('Lehrkraft_Auswertung_A4.pdf',True);d.page('Lehrkraft | Einsatz','Etappe 1 begleiten')
 for title,s in [
 ('Material ausgeben','Grundpaket: Merkblatt 1 (4 Seiten), Fischotter-Material (1), Pflichtblätter 1–4 (4). Alle Schülerseiten A5 mit mindestens 14 pt. Tipps, Lösungen und Nachweise separat halten. Keine Nachweislösungen im Kontroll-Kiosk.'),
 ('Input und Merkblatt','Die fachlichen Inhalte werden aus derselben JSON-Quelle erzeugt. Der Input ist eine Lehrkraft-Präsentation. Fachliche Aussagen, Beispiele, Fragen und gesicherte Antworten stimmen mit dem Merkblatt überein; nur Aufteilung und Bedienung unterscheiden sich.'),
 ('Pflicht und freiwillig','Pflichtkern aller vier Blätter bearbeiten. Vertiefungen sind freiwillig; keine Voraussetzung für GN1. Lernbuddy als Tischrahmen nutzen, Reflexion vor dem Abwischen ins Heft. Ein Zyklus darf mehrere Blätter umfassen.'),
 ('GN1 durchführen','Erstversuch A, nach Übung B oder passende B-Teilaufgabe. Beide Materialseiten zugänglich halten. Antworten im Heft. Rund 5–8 Minuten als Planungswert, kein Abbruch bei langsamem Schreiben. Bei der Abgabe Bild- und Textbeleg kurz zeigen lassen; alternativ die Fundstellen markieren lassen.'),
 ('Hilfen vorher vereinbaren','Auftrag vorlesen, Wörter erklären oder Schreibentlastung nach Vereinbarung. Keine Lösung nennen und keine fertige Zuordnung vorgeben. Hilfen dokumentieren; sie senken den Standard nicht automatisch. Schriftfehler sind bei GN1 kein eigener Indikator.'),
 ('Grenze und Weiterarbeit','Fünf Indikatoren, jeder erreicht = 1. Vier oder fünf = Etappenwechsel. Null bis drei = gezielte Teilübung und erneuter Nachweis. Bereits Gezeigtes anerkennen; Datum und neuen Beleg ergänzen. Eine offene Kompetenz auch bei 4/5 rückmelden. Keine Note aus dem Anteil ableiten.')]:d.block(title,s)
 d.page('Lehrkraft | Kriterien','Fünf Ziele transparent prüfen')
 for title,s in [
 ('E1.1 · Zwei Merkmale','Erreicht: zwei verschiedene äußere Merkmale richtig und genau, jeweils Körperteil mit Eigenschaft oder eindeutiger Bezug. „Ohren“ allein genügt nicht; „kleine Ohren“ genügt. Dieselbe Fellfarbe zweimal zählt einmal. Nur tatsächlich sichtbare Merkmale als Bildangabe akzeptieren.'),
 ('E1.2 · Quellen','Erreicht: ein passender Bildbeleg und ein passender Textbeleg werden richtig zugeordnet und gezeigt/markiert. Das Merkmal darf in beiden Quellen vorkommen. Die gewählte Fundstelle muss stimmen. Reines Hinschreiben von B/T ohne passenden Beleg reicht nicht.'),
 ('E1.3 · Maß','Erreicht: Kopf und Rumpf 60–90 cm bzw. Zentimeter und der Hinweis, dass der Schwanz nicht mitgezählt wird. Gleichwertige Formulierungen akzeptieren. Fehlt Einheit oder Bezug, Ziel noch offen.'),
 ('E1.4 · Sachinformationen','Erreicht: Lebensraum Flüsse/Seen und eine im jeweiligen Text genannte Nahrung richtig entnommen. Eine passende Einzelangabe zur Nahrung genügt. Inhalt unabhängig von der Zuordnung bewerten: richtige Wörter unter falscher Überschrift können E1.4 erfüllen, E1.5 nicht.'),
 ('E1.5 · Ordnung','Erreicht: eine passende Lebensraumangabe steht unter Lebensraum und eine passende Nahrungsangabe unter Nahrung. Beide Zuordnungen müssen stimmen. Keine weiteren Überschriften verlangen.'),
 ('Erneuter Beleg','Merkmale → Blatt 2; Quellen/Maß/Sachangaben → Blatt 3; Ordnung → Blatt 4. Nur offene Ziele erneut prüfen. Bei einer Teilwiederholung Gesamtstand aus alten und neuen Belegen bilden; nicht den kleineren Aufgabenumfang zur neuen Bezugsgröße machen.')]:d.block(title,s)
 d.page('Lehrkraft | Lösungen A/B','Gleichwertige Antworten')
 for title,s in [
 ('GN1 A · Aufgabe 1','B: zum Beispiel kleine Ohren, lange Tasthaare an der Schnauze oder braunes Fell. T: lang gestreckter Körper, kurze Beine oder oben dunkelbraunes Fell. Zwei verschiedene Merkmale auswählen; Bild- und Textstelle zeigen.'),
 ('GN1 B · Aufgabe 1','B: zum Beispiel kleine Ohren, lange Tasthaare an der Schnauze oder braunes Fell. T: breiter, flacher Kopf oder kurze Beine. Andere belegte Angaben gelten, sofern sie in der gewählten Quelle nachweisbar sind.'),
 ('Beide Varianten · Aufgabe 2','Kopf und Rumpf: 60 bis 90 cm. Der Schwanz zählt nicht dazu. Eine einzelne Zahl aus der Spanne ist ohne entsprechende Materialangabe keine gleichwertige Lösung.'),
 ('Beide Varianten · Aufgabe 3','Lebensraum: Flüsse und Seen. Nahrung: Fische; alternativ Frösche oder Krebse. Stichwörter reichen. Die passende Einzelangabe „Flüsse“ oder „Seen“ ist als Lebensraum ebenfalls richtig.'),
 ('Wiederholung sinnvoll nutzen','A und B prüfen dieselben Kompetenzen am vertrauten Fischotter. B ist ein erneuter Anwendungsnachweis nach Übung, kein unabhängiger Transfertest. Das Foto und einzelne Tierdaten bleiben gleich. Vergleichbare Schwierigkeit ist geplant, noch nicht erprobt.'),
 ('Rückmeldung an das Kind','„Du hast __ von 5 Zielen gezeigt. Das sind __ %. Besonders gut gelingt dir __. Als Nächstes __.“ Bei 4/5 oder 5/5 nächsten Etappeninput ermöglichen; offene Kompetenz weiter beachten. Unter 4/5 konkrete Teilübung und erneuten Beleg vereinbaren.')]:d.block(title,s)
 d.page('Lehrkraft | Kurzprotokoll','Kompetenzzuwachs festhalten')
 d.p('Kürzel: __________________  Datum: ______________<br/>Variante: A / B / Teilnachweis ____________________<br/>Vereinbarte Hilfen: ______________________________',gap=18)
 for title in ['E1.1 Zwei genaue Merkmale','E1.2 Bild- und Textbeleg','E1.3 Maß mit Einheit und Schwanzbezug','E1.4 Lebensraum und Nahrung','E1.5 Richtige Zuordnung']:
  d.p('<b>'+title+'</b><br/>Erreicht: ja / noch offen<br/>Beleg / Datum eines erneuten Belegs: __________________',gap=16)
 d.p('Gesamt: ___ / 5 = ___ %  (0 / 20 / 40 / 60 / 80 / 100)<br/>Ab 4/5: nächste Etappe. Sonst: Teilübung + erneuter Beleg.<br/>Nächster Schritt: __________________________________<br/>Erneuter Nachweis am: ______________________________',gap=14)
 d.p('Fachlichen Stand und Lernbuddy-Nutzung getrennt rückmelden. Ausgefüllte Protokolle schulisch geschützt aufbewahren; nicht ins öffentliche Cockpit hochladen.',gap=0)
 d.page('Lehrkraft | Individuelle Ziele','Fördermodule auswählen')
 for title,s in [
 ('Keine pauschale Förderfassung','Module 1–3 sind auswählbare Übungshilfen. Modul 4 bietet einen kurzen Nachweis zu vorab vereinbarten Zielen. Umfang, Antwortform und Hilfe individuell festlegen. Kein automatisches Etikett bei nicht erreichtem Mindeststandard.'),
 ('Beispiel für fünf individuelle Ziele','F1: einen Körperteil mit passender Eigenschaft benennen.<br/>F2: die Textstelle zum Lebensraum zeigen.<br/>F3: eine Lebensraumangabe richtig entnehmen.<br/>F4: eine Nahrungsangabe richtig entnehmen.<br/>F5: beide Angaben den Überschriften zuordnen.<br/>Diese Liste nur nutzen, wenn sie zu den vereinbarten Zielen passt. Modul 4 enthält passende Belegaufgaben.'),
 ('Auswertung und Lösungen','Bei fünf vereinbarten Zielen reichen vier. Bei anderer Anzahl vorab aufrunden: mindestens 0,8 × Anzahl. Beispiel: bei drei Zielen sind drei nötig. Hilfen und Eigenleistung kennzeichnen. Lösungen: Modul 1 kleine Ohren/lange Tasthaare; Modul 2 Lebensraum Flüsse und Seen, Nahrung Fische; Modul 3 60–90 cm, Schwanz nein; Modul 4 entsprechend Foto und kurzem Text.'),
 ('Erneuter Nachweis','Nach gezielter Übung nur offene Ziele erneut zeigen lassen, etwa andere sichtbare Merkmale oder eine neue Anordnung der Zuordnung. Nicht bloß die richtige Antwort vorsagen und direkt als selbstständigen Nachweis werten. Die individuelle Liste separat dokumentieren.'),
 ('Druck und Quelle','A5 in Originalgröße drucken. GN-Material und Aufgaben möglichst auf getrennten Blättern bereithalten. Foto: Dave Pape, Public Domain, Graustufenfassung aus dem bestehenden Fischotterpaket. Sachangaben aus dem vorhandenen Tiermaterial. Quellenlink im Schüler-Material. Keine neuen Schülergeräte erforderlich.')]:d.block(title,s)
 d.end()
def input_html():
 slides=[]
 for item in DATA['memo']:
  if item.get('photo'):slides.append({'section':item['title'],'title':'Das Foto','photo':True,'text':'Foto: Dave Pape | Public Domain · Graustufenfassung'})
  for title,s in item['blocks']:slides.append({'section':item['title'],'title':title,'text':s})
 css='''*{box-sizing:border-box}body{margin:0;background:#eff5fa;color:#18324a;font:22px/1.45 system-ui}header,main,footer{max-width:1180px;margin:auto;padding:20px}header{border-bottom:5px solid #48dccb}h1{font-size:24px}h2{font-size:clamp(30px,4vw,46px);line-height:1.15}article{background:white;border-top:7px solid #245688;border-radius:12px;padding:28px 36px;min-height:360px}article p{font-size:clamp(24px,2.6vw,34px)}button,select{font:inherit;padding:10px 14px;min-height:48px;background:#245688;color:white;border:2px solid #245688;border-radius:8px}select{background:white;color:#18324a;max-width:100%}nav{display:flex;flex-wrap:wrap;gap:12px;align-items:center}a{color:#245688}button:focus-visible,select:focus-visible,a:focus-visible{outline:3px solid #cf6320;outline-offset:3px}img{display:block;margin:auto;max-width:100%;max-height:48vh}footer{font-size:18px}.section{font-size:20px}.controls{margin-top:20px;display:flex;gap:15px;align-items:center;flex-wrap:wrap}[hidden]{display:none!important}@media(max-width:650px){article{padding:20px}header,main{padding:14px}}'''
 options=''.join('<option value="'+str(i)+'">'+str(i+1)+'. '+html.escape(s['section']+' · '+s['title'])+'</option>' for i,s in enumerate(slides))
 payload=json.dumps(slides,ensure_ascii=False).replace('<','\\u003c')
 body='<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Etappe 1 · Informationen</title><style>'+css+'</style></head><body><header><h1>Etappe 1 · Informationen finden und ordnen</h1><nav><a href="../../index.html#etappe1">Zum Cockpit</a><a href="Merkblatt_1_A5.pdf">Identisches Merkblatt</a><label for="slide">Abschnitt</label><select id="slide">'+options+'</select></nav></header><main><article><p class="section" id="section"></p><h2 id="title"></h2><img id="photo" src="../gelingensnachweise/Fischotter_DavePape_Graustufen.jpg" alt="Fischotter mit kleinen Ohren und langen Tasthaaren an der Schnauze" hidden><p id="text"></p><p id="source" hidden><a href="'+SOURCE+'">Bildquelle: Dave Pape · Public Domain</a></p></article><nav class="controls" aria-label="Folien"><button id="prev">Zurück</button><span id="count" aria-live="polite"></span><button id="next">Weiter</button></nav></main><footer>Lehrkraftansicht · Pfeiltasten zum Blättern · Fachlicher Inhalt wie Merkblatt 1.</footer><script>const slides='+payload+';let n=0;const $=id=>document.getElementById(id);function render(){const s=slides[n];$("section").textContent=s.section;$("title").textContent=s.title;$("text").innerHTML=s.text;$("photo").hidden=!s.photo;$("source").hidden=!s.photo;$("slide").value=n;$("count").textContent=(n+1)+" / "+slides.length;$("prev").disabled=n===0;$("next").disabled=n===slides.length-1;}$("prev").onclick=()=>{if(n>0)n--;render()};$("next").onclick=()=>{if(n<slides.length-1)n++;render()};$("slide").onchange=e=>{n=Number(e.target.value);render()};document.addEventListener("keydown",e=>{if(e.target.tagName==="SELECT")return;if(e.key==="ArrowRight")$("next").click();if(e.key==="ArrowLeft")$("prev").click()});render();</script></body></html>'
 (OUT/'Input_Etappe1.html').write_text(body)
 assert [(s['title'],s['text']) for s in slides if not s.get('photo')]==[(a,b) for m in DATA['memo'] for a,b in m['blocks']]
def validate():
 for item in manifest:
  doc=fitz.open(ROOT/item['path']);assert len(doc)==item['pages'];sizes=[]
  for p in doc:
   if item['student']:assert abs(p.rect.width-419.528)<.05 and abs(p.rect.height-595.276)<.05
   for b in p.get_text('dict')['blocks']:
    for l in b.get('lines',[]):
     for s in l['spans']:
      sizes.append(s['size']);x0,y0,x1,y1=s['bbox'];assert s['size']>=13.99 and x0>=41.5 and x1<=p.rect.width-27 and y0>=20 and y1<p.rect.height-10,(item,s)
  item['minimumFontPt']=round(min(sizes),2);item['bytes']=(ROOT/item['path']).stat().st_size
 text=' '.join(p.get_text() for p in fitz.open(OUT/'Merkblatt_1_A5.pdf'))
 norm=lambda s:re.sub(r'\s+','',html.unescape(re.sub('<[^>]+>',' ',s)))
 for m in DATA['memo']:
  for _,s in m['blocks']:assert norm(s) in norm(text),(m['title'],s)
 report={'files':manifest,'inputMemoContentParity':True,'sourceSha256':hashlib.sha256((OUT/'inhalt.json').read_bytes()).hexdigest(),'visualReview':'pending'}
 (OUT/'Pruefbericht.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False))
if __name__=='__main__':
 memo();material();exercises();gn('A');gn('B');foerder();teacher();input_html()
 combo=fitz.open()
 for f in ['Merkblatt_1_A5.pdf','Fischotter_Material_A5.pdf','Pflichtblaetter_1-4_A5.pdf']:combo.insert_pdf(fitz.open(OUT/f))
 combo.save(OUT/'Etappe1_Schuelerpaket_A5.pdf',garbage=4,deflate=True);manifest.append({'path':'materialien/etappe1/Etappe1_Schuelerpaket_A5.pdf','pages':len(combo),'student':True});validate()
