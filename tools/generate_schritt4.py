"""Schritt 4: A5-Aufgaben, Merkblätter, Tipps und Lösungen.
Benötigt ReportLab, PyMuPDF und die DejaVu-Schriften.
python tools/generate_schritt4.py
Die Inhalte liegen in materialien/schritt4_inhalte.json.
"""
from pathlib import Path
import json
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
import pymupdf as fitz
ROOT=Path(__file__).resolve().parents[1]
DATA=json.loads((ROOT/'materialien/schritt4_inhalte.json').read_text())
W,H=148*72/25.4,210*72/25.4
M=30; WIDTH=W-2*M
for name,f in [('Text','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf')]:
 pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+f))
class PDF:
 def __init__(self,name):
  self.path=ROOT/'materialien/schritt4'/name
  self.path.parent.mkdir(parents=True,exist_ok=True)
  self.c=canvas.Canvas(str(self.path),pagesize=(W,H),pageCompression=1)
  self.c.setTitle(name.replace('_',' ').replace('.pdf',''))
  self.c.setAuthor('Otterklasse 5.3 · Deutsch')
  self.page=0;self.y=0
 def p(self,text,size=14,bold=False,gap=8):
  assert size>=14
  p=Paragraph(text,ParagraphStyle('p',fontName='Bold' if bold else 'Text',fontSize=size,leading=size*1.3,textColor=HexColor('#18324A')))
  _,height=p.wrap(WIDTH,1000)
  assert self.y+height<=H-49,(self.path.name,self.page,self.y,height,text)
  p.drawOn(self.c,M,H-self.y-height);self.y+=height+gap
 def head(self,label,title):
  if self.page:self.c.showPage()
  self.page+=1;c=self.c
  c.bookmarkPage('seite-'+str(self.page));c.addOutlineEntry(label+' · '+title,'seite-'+str(self.page))
  c.setStrokeColor(HexColor('#245688'));c.setLineWidth(3);c.line(M,H-24,W-M,H-24)
  self.y=34;self.p(label,16,True,7);self.p(title,21,True,12)
  c.setFont('Text',14);c.setFillColor(HexColor('#18324A'));c.drawString(M,23,'Deutsch 5.3 · Zootiere');c.drawRightString(W-M,23,str(self.page))
 def blocks(self,blocks):
  for title,body in blocks:
   self.p(title,15,True,4);self.p(body,gap=10)
 def end(self):
  self.c.save()
  d=fitz.open(self.path);sizes=[];bounds=[]
  for p in d:
   assert abs(p.rect.width-W)<.1 and abs(p.rect.height-H)<.1
   for b in p.get_text('dict')['blocks']:
    for line in b.get('lines',[]):
     for s in line['spans']:
      sizes.append(s['size'])
      x0,y0,x1,y1=s['bbox']
      assert s['size']>=13.99
      assert x0>=M-1 and x1<=W-M+1 and y0>=0 and y1<H-8,(self.path.name,p.number,s)
  return {'path':str(self.path.relative_to(ROOT)),'pages':len(d),'minimumFontPt':min(sizes),'a5':True,'bytes':self.path.stat().st_size}
def run():
 outputs=[]
 d=PDF('Aufgaben_1-10_A5.pdf')
 for a in DATA['tasks']:
  d.head('Blatt '+str(a['n']),a['title'])
  d.p('<b>Ziel:</b> '+a['goal'],gap=6)
  d.p('<b>Du brauchst:</b> '+a['material'],gap=12)
  d.blocks(a['blocks'])
  d.p('<b>Lernbuddy:</b> '+a['buddy'],gap=0)
 outputs.append(d.end())
 d=PDF('Merkblaetter_1-3_A5.pdf')
 for m in DATA['memos']:
  d.head('Merkblatt '+str(m['n']),m['title']);d.blocks(m['blocks'])
 outputs.append(d.end())
 for field,filename,label in [('tip','Tipps_1-10_A5.pdf','Tipp'),('solution','Loesungen_1-10_A5.pdf','Lösung')]:
  d=PDF(filename)
  for a in DATA['tasks']:
   d.head(label+' zu Blatt '+str(a['n']),a['title'])
   d.p('Nutze nur so viel Hilfe, wie du brauchst.' if field=='tip' else 'Vergleiche mit deinem Ergebnis. Verbessere nur, was nötig ist.',gap=18)
   for i,t in enumerate(a[field]):
    d.p(('<b>'+str(i+1)+'.</b> ' if field=='tip' else '')+t,gap=16)
   d.p('Arbeite jetzt im Heft weiter.' if field=='tip' else 'Zeige einen Beleg, wenn du deine Lösung erklärst.',gap=0)
  outputs.append(d.end())
 (ROOT/'materialien/schritt4/Pruefbericht.json').write_text(json.dumps(outputs,ensure_ascii=False,indent=2))
 print(json.dumps(outputs,ensure_ascii=False))
if __name__=='__main__':run()
