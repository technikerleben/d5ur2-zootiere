"""A5-Schülerausgaben, durchgehend >=14 pt.
python -m pip install reportlab pymupdf pillow
python tools/generate_a5.py
Quellen: materialien/schritt3_inhalte.json. Fotos werden eingebettet.
"""
from pathlib import Path
import json, urllib.request, io
from xml.sax.saxutils import escape
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from PIL import Image
import fitz
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'materialien/schritt3_inhalte.json').read_text())
W,H=148*72/25.4,210*72/25.4
M=30; CW=W-2*M
for name,file in [('Text','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf')]:
 pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+file))
BLUE='#245688'; DARK='#18324A'
manifest=[]
class Doc:
 def __init__(self,path,title):
  self.path=ROOT/path;self.path.parent.mkdir(parents=True,exist_ok=True)
  self.c=canvas.Canvas(str(self.path),pagesize=(W,H),pageCompression=1)
  self.c.setTitle(title);self.c.setAuthor('Otterklasse 5.3 · Deutsch')
  self.n=0;self.y=0
 def p(self,s,size=14.5,bold=False,gap=8,width=None,x=None):
  assert size>=14
  p=Paragraph(s,ParagraphStyle('p',fontName='Bold' if bold else 'Text',fontSize=size,leading=size*1.32,textColor=HexColor(DARK)))
  width=width or CW
  _,h=p.wrap(width,1000)
  assert self.y+h<=H-50,(self.path.name,self.n,self.y,h,s)
  p.drawOn(self.c,M if x is None else x,H-self.y-h)
  self.y+=h+gap
 def page(self,title,label):
  if self.n:self.c.showPage()
  self.n+=1
  c=self.c;c.setStrokeColor(HexColor(BLUE));c.setLineWidth(3)
  c.line(M,H-24,W-M,H-24)
  self.y=34
  self.p(label,size=14,bold=True,gap=7)
  self.p(title,size=21,bold=True,gap=14)
  c.setFont('Text',14);c.setFillColor(HexColor(DARK))
  c.drawString(M,23,'Deutsch 5.3 · Zootiere')
  c.drawRightString(W-M,23,str(self.n))
 def section(self,s):
  self.p(s,size=16,bold=True,gap=6)
 def check(self,title,body):
  self.c.setStrokeColor(HexColor(DARK));self.c.setLineWidth(1)
  self.c.rect(M,H-self.y-16,12,12,stroke=1,fill=0)
  self.p(title,size=15,bold=True,width=CW-23,x=M+23,gap=5)
  self.p(body,gap=12)
 def end(self):
  self.c.save()
  manifest.append({'path':str(self.path.relative_to(ROOT)),'pages':self.n})
def e(s):return escape(s)
def animal(a):
 d=Doc('materialien/tierpakete/'+a['id']+'_A5.pdf',a['name']+' · Tiermaterial A5')
 d.page(a['name'],'TIERMATERIAL · SACHTEXT')
 d.p('Lies den Text. Nutze die Wörterhilfe auf der nächsten Seite.',gap=14)
 d.p(' '.join(map(e,a['sentences'])),gap=16)
 d.section('Nutze das Material')
 d.p('Zeige eine Information im Text. Schau dir dann das Foto an. Zeige ein Merkmal, das du dort wirklich erkennst.')
 d.page(a['name'],'TIERMATERIAL · FOTO & WÖRTER')
 raw=urllib.request.urlopen(urllib.request.Request(a['image'],headers={'User-Agent':'Zootiere-Unterricht/1.0'}),timeout=30).read()
 im=Image.open(io.BytesIO(raw)).convert('RGB')
 im.thumbnail((1000,700))
 b=io.BytesIO();im.save(b,format='JPEG',quality=82)
 iw,ih=im.size; scale=min(CW/iw,175/ih);dw,dh=iw*scale,ih*scale
 d.c.drawImage(ImageReader(io.BytesIO(b.getvalue())),M+(CW-dw)/2,H-d.y-dh,dw,dh)
 d.y+=dh+8
 d.p('Foto: '+e(a['author'])+' · '+e(a['license'])+'.',size=14,gap=3)
 d.p('<link href="'+e(a['imagePage'])+'"><u>Bildquelle: Wikimedia Commons</u></link> · <link href="'+e(a['licenseUrl'])+'"><u>Freigabe</u></link>',size=14,gap=12)
 d.section('Wörterhilfe')
 for word,meaning in a['glossary']:
  d.p('<b>'+e(word)+':</b> '+e(meaning),size=14,gap=7)
 d.page(a['name'],'LESEHILFE · BEI BEDARF')
 d.p('Hier steht derselbe Text. Lies Satz für Satz.',size=14,gap=12)
 for sentence in a['sentences']:d.p(e(sentence),size=14,gap=5)
 d.end()

def learning_path():
 d=Doc('materialien/lernweg/Mein_Lernweg_Zootiere_A5.pdf','Mein Lernweg: Zootiere')
 d.page('Mein Lernweg','DEIN WEG DURCH DIE REIHE')
 d.p('Name: __________________________',gap=14)
 d.section('Dein Ziel')
 d.p('Du beschreibst ein Zootier sachlich und geordnet. Dafür nutzt du Bilder und Sachtexte. Gemeinsam übst du am Fischotter.')
 d.section('So gehst du vor')
 for s in ['1. Input','2. Übung','3. Vertiefung – freiwillig','4. Probearbeit – für alle, ohne Note','5. Projekte – freiwillig','6. Lernerfolgskontrolle (Arbeit)']:
  d.p(s,size=14.5,gap=4)
 d.p('Du musst nicht jedes Blatt bearbeiten. Vereinbare passende Übungen mit deiner Lehrkraft.',gap=0)
 d.page('Deine Übungen','LERNWEG · VEREINBAREN & PRÜFEN')
 d.p('Kreise die vereinbarten Blattnummern ein. Hake eine Zeile ab, wenn du deine Übungen dazu bearbeitet und geprüft hast.',gap=14)
 rows=[('Blatt 1 / 2','Du erkennst und benennst genaue Merkmale.'),('Blatt 3 / 4','Du findest und ordnest Informationen.'),('Blatt 5 / 6','Du nutzt genaue Wörter und sachliche Sätze.'),('Blatt 7 / 8','Du planst und schreibst deine Tierbeschreibung.'),('Blatt 9','Du prüfst deinen Text und verbesserst ihn.'),('Blatt 10','Du übst nach der Probearbeit gezielt weiter.')]
 for title,body in rows:d.check(title,body)
 d.page('Zeige, was du kannst','LERNWEG · DEINE PRÜFPUNKTE')
 for title,body in [
 ('Nach Blatt 3 / 4','Zeige eine Information auf dem Foto und eine im Text. Erkläre, wo du sie gefunden hast.'),
 ('Nach Blatt 9','Prüfe deine vollständige Tierbeschreibung. Zeige eine gelungene Stelle und deinen nächsten Lernschritt.'),
 ('Probearbeit – für alle','Du bekommst keine Note. Nutze die Rückmeldung. Vereinbare danach deine nächste Übung.'),
 ('Lernerfolgskontrolle (Arbeit)','Beschreibe ein neues Tier. Deine Lehrkraft erklärt dir vorher die Arbeitszeit und die erlaubten Hilfen.')]:
  d.section(title);d.p(body,gap=13)
 d.p('Wenn du die Grundlagen sicher kannst, besprich eine freiwillige Vertiefung oder ein Projekt mit deiner Lehrkraft.',size=14)
 d.end()

def buddy():
 d=Doc('materialien/lernweg/Lernbuddy_Zielhilfe_Zootiere_A5.pdf','Dein Lernbuddy in Deutsch')
 d.page('Dein Lernbuddy','ZIELHILFE · BEI BEDARF')
 d.section('Planung')
 d.p('Lies deine letzte Reflexion im Heft. Wähle ein Ziel und eine passende Aufgabe. Schreibe dein Ziel kurz auf deinen Lernbuddy.')
 for title,body in [
 ('Blatt 1 / 2','Du benennst sichtbare Merkmale genau.'),
 ('Blatt 3 / 4','Du findest und ordnest Informationen.'),
 ('Blatt 5 / 6','Du schreibst genaue, sachliche Sätze.'),
 ('Blatt 7 / 8','Du ordnest deinen Text mit einem Schreibplan.'),
 ('Blatt 9','Du prüfst deinen Text mit den Kriterien.'),
 ('Blatt 10','Du wählst dein Ziel aus der Rückmeldung.')]:
  d.p('<b>'+title+':</b> '+body,size=14,gap=9)
 d.p('Prüfe deine Energie und mögliche Ablenker. Was hilft dir, anzufangen?',size=14)
 d.page('Dein Lernbuddy','ARBEITEN & ZURÜCKBLICKEN')
 d.section('Durchführung')
 d.p('Lege das A5-Arbeitsblatt in die freie Mitte deines Lernbuddys. Nutze eine passende Strategie.')
 d.p('Prüfe zwischendurch: Hilft dein Weg dir, dein Ziel zu erreichen?')
 d.p('Wenn du feststeckst: Lies den Auftrag erneut. Nutze ein Beispiel oder eine Hilfe. Frage ein anderes Kind, dann die Lehrkraft.')
 d.p('Wenn du überfordert bist, darfst du direkt die Lehrkraft fragen.',gap=18)
 d.section('Reflexion')
 d.p('Zeige eine gelungene Stelle. Schreibe deine Reflexion auf den Lernbuddy. Übertrage sie vor dem Abwischen kurz ins Heft.')
 d.p('<b>Das ist mir gelungen: …<br/>Als Nächstes übe ich …<br/>Diese Hilfe nutze ich wieder: …</b>',size=14)
 d.end()

def checklist():
 d=Doc('materialien/bewertung/Kindercheckliste_A5.pdf','Deine Tierbeschreibung: Das zählt')
 d.page('Deine Tierbeschreibung','CHECKLISTE · INHALT & AUFBAU')
 d.p('Name: __________________________<br/>Tier: ___________________________',size=14)
 d.p('Prüfe deinen Text. Hake ab, was passt. Zeige eine passende Textstelle. Verbessere nur, was noch nötig ist.',gap=14)
 for c in DATA['criteria'][:3]:d.check(c['id']+' · '+c['title'],e(c['child']))
 d.page('Deine Tierbeschreibung','CHECKLISTE · SPRACHE & PRÜFEN')
 for c in DATA['criteria'][3:]:d.check(c['id']+' · '+c['title'],e(c['child']))
 d.section('Dein nächster Schritt')
 d.p('Wähle einen Punkt, den du weiterüben möchtest. Nutze ihn für die nächste Planung mit deinem Lernbuddy.')
 d.p('Die Haken ergeben keine Note. Vor der Arbeit erklärt dir die Lehrkraft die erlaubten Hilfen.',size=14)
 d.end()
def validate():
 report=[]
 for item in manifest:
  pdf=fitz.open(ROOT/item['path']); smallest=100
  for page in pdf:
   assert abs(page.rect.width-W)<.1 and abs(page.rect.height-H)<.1
   for block in page.get_text('dict')['blocks']:
    for line in block.get('lines',[]):
     for span in line['spans']:
      smallest=min(smallest,span['size'])
      assert span['size']>=13.99,(item,span)
      x0,y0,x1,y1=span['bbox']
      assert x0>=M-1 and x1<=W-M+1 and y0>=0 and y1<=H-8,(item,span)
  report.append({**item,'minimumFontPt':round(smallest,2),'a5':True,'bytes':(ROOT/item['path']).stat().st_size})
 (ROOT/'materialien/A5_Pruefbericht.json').write_text(json.dumps(report,ensure_ascii=False,indent=2))
 print(json.dumps(report,ensure_ascii=False))
if __name__=='__main__':
 learning_path();buddy();checklist()
 for a in DATA['animals']:animal(a)
 combined=fitz.open()
 for entry in manifest:
  if any(x in entry['path'] for x in ['waschbaer','biber']):continue
  source=fitz.open(ROOT/entry['path'])
  count=source.page_count
  if '/tierpakete/' in entry['path']:count=2
  combined.insert_pdf(source,to_page=count-1)
 out=ROOT/'materialien/Schuelermaterial_Zootiere_A5.pdf'
 combined.save(out,garbage=4,deflate=True)
 manifest.append({'path':str(out.relative_to(ROOT)),'pages':combined.page_count})
 validate()
