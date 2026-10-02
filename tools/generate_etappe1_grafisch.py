"""Graustufen-Neusatz, unveränderte Inhalte und Seitenfolge des Schülerpakets."""
from pathlib import Path
import json, re, hashlib
from io import BytesIO
import fitz
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/'materialien/etappe1'; OUT=BASE/'grafisch'
DATA=json.loads((BASE/'inhalt.json').read_text())
SOURCE='https://commons.wikimedia.org/wiki/File:Lutra_lutra_1_-_Otter,_Owl,_and_Wildlife_Park.jpg'
PHOTO=ROOT/'materialien/gelingensnachweise/Fischotter_DavePape_Graustufen.jpg'
MASCOT=OUT/'assets/Otter_und_Dino.png'
for name,font in [('Text','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf')]:
 pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+font))
W,H=419.528,595.276;LEFT=42.52;RIGHT=W-28.35;WIDTH=RIGHT-LEFT
FULL=OUT/'Etappe1_Schuelerpaket_A5_grafisch_graustufen.pdf'
WORK=OUT/'Pflichtblaetter_1-4_A5_grafisch_graustufen.pdf'
# Pure grayscale is a print colorspace conversion, not a change of illustration.
mascot=ImageReader(Image.open(MASCOT).convert('L'))
c=canvas.Canvas(str(FULL),pagesize=(W,H));c.setTitle('Etappe 1 · Otterklasse 5.3 und Dino-Klasse 5.5');c.setAuthor('Deutsch · Klassen 5.3 und 5.5')
y=0;n=0

def para(s,size=14,bold=False,width=WIDTH):
 p=Paragraph(s,ParagraphStyle('p',fontName='Bold' if bold else 'Text',fontSize=size,leading=size*1.22,textColor='#111111'));p.wrap(width,2000);return p

def draw(s,size=14,bold=False,gap=8):
 global y
 p=para(s,size,bold);assert y+p.height<=H-48,(n,y,p.height,s)
 p.drawOn(c,LEFT,H-y-p.height);y+=p.height+gap

def page(label,title,number):
 global n,y
 if n:c.showPage()
 n+=1
 c.drawImage(mascot,RIGHT-108,H-64,108,56.5)
 p=para(label,14,True,width=231);p.drawOn(c,LEFT,H-27-p.height)
 c.setStrokeGray(.5);c.setLineWidth(1);c.line(LEFT,H-61,RIGHT-120,H-61)
 p=para(title,20,True);top=74
 c.setFillGray(.94);c.roundRect(LEFT,H-top-p.height-8,WIDTH,p.height+16,6,stroke=0,fill=1)
 p.drawOn(c,LEFT,H-top-p.height);y=top+p.height+21
 c.setStrokeGray(.6);c.line(LEFT,43,RIGHT,43)
 c.setFillGray(.07);c.setFont('Text',14);c.drawString(LEFT,22,'Deutsch 5.3 + 5.5 | Etappe 1');c.drawRightString(RIGHT,22,str(number))

def block(title,text):
 global y
 # Section bars preserve full text width; voluntary work gets an outlined panel.
 h=para(title,15,True).height
 if title=='Freiwillige Vertiefung':
  heading=para(title,15,True,width=WIDTH-14);body=para(text,width=WIDTH-14)
  total=heading.height+5+body.height+14
  assert y+total<=H-48,(n,title)
  c.setLineWidth(1);c.setStrokeGray(.6);c.roundRect(LEFT,H-y-total+5,WIDTH,total,6,stroke=1,fill=0)
  heading.drawOn(c,LEFT+7,H-y-heading.height);y+=heading.height+5
  body.drawOn(c,LEFT+7,H-y-body.height);y+=body.height+16
  return
 c.setFillGray(.95);c.roundRect(LEFT,H-y-h-2,WIDTH,h+4,3,stroke=0,fill=1)
 draw(title,15,True,5);draw(text,gap=11)

def photo(height):
 global y
 im=Image.open(PHOTO);iw=height*im.width/im.height
 c.drawImage(ImageReader(im.convert('L')),LEFT+(WIDTH-iw)/2,H-y-height,iw,height);y+=height+8
 draw('Foto: Dave Pape | Public Domain',gap=3)
 draw('<link href="'+SOURCE+'"><u>Bildquelle</u></link> | Graustufenfassung',gap=10)

for i,item in enumerate(DATA['memo'],1):
 page('Merkblatt 1 | '+str(i)+'/4',item['title'],i)
 if item.get('photo'):photo(112)
 for title,s in item['blocks']:block(title,s)
page('Material zu Blatt 1–4','Der Fischotter',1);photo(125);draw(DATA['text'])
for w in DATA['worksheets']:
 page('Blatt '+str(w['n'])+' | Pflicht + freiwillig',w['title'],w['n'])
 draw('Du brauchst: '+w['material']+'.',gap=12)
 for title,s in w['blocks']:block(title,s)
c.save()
source=fitz.open(BASE/'Etappe1_Schuelerpaket_A5.pdf');result=fitz.open(FULL)
assert len(source)==len(result)==9
norm=lambda s:re.sub(r'\s+','',s)
checks=[]
for i,(a,b) in enumerate(zip(source,result),1):
 # Footer reflects the additional participating class; page labels and all body text remain.
 ta=a.get_text().replace('Deutsch 5.3 | Etappe 1','')
 tb=b.get_text().replace('Deutsch 5.3 + 5.5 | Etappe 1','')
 # Text objects for footers are painted before content, as in the source generator.
 assert norm(ta)==norm(tb),(i,ta,tb)
 sizes=[]
 for block_ in b.get_text('dict')['blocks']:
  for line in block_.get('lines',[]):
   for s in line['spans']:
    x0,y0,x1,y1=s['bbox'];assert s['size']>=13.99 and x0>=LEFT-1 and x1<=RIGHT+1 and y0>14 and y1<H-10,(i,s)
    color=s['color'];assert (color>>16)==((color>>8)&255)==(color&255),color;sizes.append(s['size'])
 assert abs(b.rect.width-W)<.01 and abs(b.rect.height-H)<.01
 for image in b.get_images():assert image[5]=='DeviceGray',image
 checks.append({'page':i,'sourceTextIdentical':True,'minimumFontPt':min(sizes),'a5':True,'imagesGrayscale':True})
part=fitz.open();part.insert_pdf(result,from_page=5,to_page=8);part.save(WORK,garbage=4,deflate=True)
report={'source':'materialien/etappe1/Etappe1_Schuelerpaket_A5.pdf','sourceSha256':hashlib.sha256((BASE/'Etappe1_Schuelerpaket_A5.pdf').read_bytes()).hexdigest(),'contentChanges':'Nur Fußzeile erweitert um Klasse 5.5. Fachliche Inhalte und Seitenfolge unverändert.','pages':checks,'visualReview':'pending','files':[{'path':str(p.relative_to(ROOT)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}for p in [FULL,WORK]]}
(OUT/'Pruefbericht.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'pages':len(result),'files':[str(FULL),str(WORK)]}))
