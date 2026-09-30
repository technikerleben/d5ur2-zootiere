"""Generate Etappe 3 PDFs and teacher input from one content source."""
from pathlib import Path
import json,re,html,hashlib
import fitz
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'materialien/etappe3';DATA=json.loads((OUT/'inhalt.json').read_text())
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
  self.c.setFont('Text',14);self.c.drawString(self.left,22,'Deutsch 5.3 | Etappe 3');self.c.drawRightString(self.w-28.35,22,str(self.n))
 def block(self,title,s):self.p(title,15,True,4);self.p(s,14,gap=12)
 def photo(self,height=115):
  from PIL import Image
  w,h=Image.open(PHOTO).size;iw=height*w/h;self.c.drawImage(str(PHOTO),self.left+(self.width-iw)/2,self.h-self.y-height,iw,height);self.y+=height+8
  self.p('Foto: Dave Pape | Public Domain',14,gap=3);self.p('<link href="'+SOURCE+'"><u>Bildquelle</u></link> | Graustufenfassung',14,gap=10)
 def end(self):
  self.c.save();manifest.append({'path':str(self.path.relative_to(ROOT)),'pages':self.n,'student':self.w<500})
def pages(name,key,label,a4=False,start=1):
 d=Doc(name,a4)
 for i,page in enumerate(DATA[key],start):
  d.page(label+' | '+str(i),page['title'])
  for title,s in page['blocks']:d.block(title,s)
 d.end()
def teacher():
 d=Doc('Lehrkraft_Auswertung_A4.pdf',True)
 for page in json.loads((OUT/'lehrkraft.json').read_text()):
  d.page('Lehrkraft | Etappe 3',page['title'])
  for title,s in page['blocks']:d.block(title,s)
 d.end()
def probearbeit():
 from reportlab.lib.utils import ImageReader
 import io
 source=fitz.open(ROOT/'materialien/tierpakete/waschbaer_A5.pdf')
 pix=fitz.Pixmap(source,source[1].get_images()[0][0]);gray=fitz.Pixmap(fitz.csGRAY,pix)
 d=Doc('Probearbeit_Waschbaer_A5.pdf')
 d.page('Probearbeit | Material 1/2',DATA['pa'][0]['title'])
 for title,s in DATA['pa'][0]['blocks']:d.block(title,s)
 d.page('Probearbeit | Material 2/2','Das Foto')
 ih=250;iw=ih*gray.width/gray.height
 d.c.drawImage(ImageReader(io.BytesIO(gray.tobytes('png'))),d.left+(d.width-iw)/2,d.h-d.y-ih,iw,ih);d.y+=ih+12
 d.p('Foto: BS Thurner Hof · CC BY-SA 3.0. Graustufenfassung.',gap=8)
 d.p('<link href="https://commons.wikimedia.org/wiki/File:Procyon_lotor_7_-_am_Wasser.jpg"><u>Bildquelle: Wikimedia Commons</u></link>',gap=8)
 d.p('<link href="https://creativecommons.org/licenses/by-sa/3.0/"><u>Lizenz: CC BY-SA 3.0</u></link>',gap=8)
 d.p('Nutze nur Merkmale, die du wirklich siehst. Gewicht, Lebensraum und Nahrung findest du im Text.')
 d.page('Probearbeit | Auftrag',DATA['pa'][1]['title'])
 for title,s in DATA['pa'][1]['blocks']:d.block(title,s)
 d.end()
def input_html():
 slides=[]
 for item in DATA['memo']:
  if item.get('photo'):slides.append({'section':item['title'],'title':'Das Foto','photo':True,'text':'Foto: Dave Pape | Public Domain · Graustufenfassung'})
  for title,s in item['blocks']:slides.append({'section':item['title'],'title':title,'text':s})
 css='''*{box-sizing:border-box}body{margin:0;background:#eff5fa;color:#18324a;font:22px/1.45 system-ui}header,main,footer{max-width:1180px;margin:auto;padding:20px}header{border-bottom:5px solid #48dccb}h1{font-size:24px}h2{font-size:clamp(30px,4vw,46px);line-height:1.15}article{background:white;border-top:7px solid #245688;border-radius:12px;padding:28px 36px;min-height:360px}article p{font-size:clamp(24px,2.6vw,34px)}button,select{font:inherit;padding:10px 14px;min-height:48px;background:#245688;color:white;border:2px solid #245688;border-radius:8px}select{background:white;color:#18324a;max-width:100%}nav{display:flex;flex-wrap:wrap;gap:12px;align-items:center}a{color:#245688}button:focus-visible,select:focus-visible,a:focus-visible{outline:3px solid #cf6320;outline-offset:3px}img{display:block;margin:auto;max-width:100%;max-height:48vh}footer{font-size:18px}.section{font-size:20px}.controls{margin-top:20px;display:flex;gap:15px;align-items:center;flex-wrap:wrap}[hidden]{display:none!important}@media(max-width:650px){article{padding:20px}header,main{padding:14px}}'''
 options=''.join('<option value="'+str(i)+'">'+str(i+1)+'. '+html.escape(s['section']+' · '+s['title'])+'</option>' for i,s in enumerate(slides))
 payload=json.dumps(slides,ensure_ascii=False).replace('<','\\u003c')
 body='<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Etappe 3 · Schreiben</title><style>'+css+'</style></head><body><header><h1>Etappe 3 · Eine Tierbeschreibung schreiben und prüfen</h1><nav><a href="../../index.html#etappe3">Zum Cockpit</a><a href="Merkblatt_3_A5.pdf">Identisches Merkblatt</a><label for="slide">Abschnitt</label><select id="slide">'+options+'</select></nav></header><main><article><p class="section" id="section"></p><h2 id="title"></h2><img id="photo" src="../gelingensnachweise/Fischotter_DavePape_Graustufen.jpg" alt="Fischotter mit kleinen Ohren und langen Tasthaaren an der Schnauze" hidden><p id="text"></p><p id="source" hidden><a href="'+SOURCE+'">Bildquelle: Dave Pape · Public Domain</a></p></article><nav class="controls" aria-label="Folien"><button id="prev">Zurück</button><span id="count" aria-live="polite"></span><button id="next">Weiter</button></nav></main><footer>Lehrkraftansicht · Pfeiltasten zum Blättern · Fachlicher Inhalt wie Merkblatt 3.</footer><script>const slides='+payload+';let n=0;const $=id=>document.getElementById(id);function render(){const s=slides[n];$("section").textContent=s.section;$("title").textContent=s.title;$("text").innerHTML=s.text;$("photo").hidden=!s.photo;$("source").hidden=!s.photo;$("slide").value=n;$("count").textContent=(n+1)+" / "+slides.length;$("prev").disabled=n===0;$("next").disabled=n===slides.length-1;}$("prev").onclick=()=>{if(n>0)n--;render()};$("next").onclick=()=>{if(n<slides.length-1)n++;render()};$("slide").onchange=e=>{n=Number(e.target.value);render()};document.addEventListener("keydown",e=>{if(e.target.tagName==="SELECT")return;if(e.key==="ArrowRight")$("next").click();if(e.key==="ArrowLeft")$("prev").click()});render();</script></body></html>'
 (OUT/'Input_Etappe3.html').write_text(body)
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
 text=' '.join(p.get_text() for p in fitz.open(OUT/'Merkblatt_3_A5.pdf'))
 norm=lambda s:re.sub(r'\s+','',html.unescape(re.sub('<[^>]+>',' ',s)))
 for m in DATA['memo']:
  for _,s in m['blocks']:assert norm(s) in norm(text),(m['title'],s)
 report={'files':manifest,'inputMemoContentParity':True,'sourceSha256':hashlib.sha256((OUT/'inhalt.json').read_bytes()).hexdigest(),'visualReview':'pending'}
 (OUT/'Pruefbericht.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False))
if __name__=='__main__':
 pages('Merkblatt_3_A5.pdf','memo','Merkblatt 3')
 pages('Pflichtblaetter_7-9_A5.pdf','worksheets','Pflichtblatt',start=7)
 pages('Tipps_7-9_A5.pdf','tips','Tipp')
 pages('Loesungen_7-9_A5.pdf','solutions','Lösungen')
 pages('Checkliste_K1-K6_A5.pdf','check','Checkliste')
 pages('Uebungstexte_A5.pdf','practice_material','Material zu Blatt 7-9')
 probearbeit()
 pages('Feedback_Probearbeit_A5.pdf','feedback','Feedback')
 pages('Erneute_Belege_A5.pdf','repeat','Erneuter Nachweis')
 pages('Foerdermodule_A5.pdf','foerder','Fördermodul')
 teacher();input_html()
 combo=fitz.open()
 for f in ['Merkblatt_3_A5.pdf','Pflichtblaetter_7-9_A5.pdf','Checkliste_K1-K6_A5.pdf']:combo.insert_pdf(fitz.open(OUT/f))
 combo.save(OUT/'Etappe3_Schuelerpaket_A5.pdf',garbage=4,deflate=True);manifest.append({'path':'materialien/etappe3/Etappe3_Schuelerpaket_A5.pdf','pages':len(combo),'student':True});validate()
