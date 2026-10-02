"""Generate paper learning path, four-level rubric and optional projects."""
from pathlib import Path
import json,re,html,hashlib
import fitz
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'materialien/lernweg_wahlphase';DATA=json.loads((OUT/'inhalt.json').read_text())
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
  self.c.setFont('Text',14);self.c.drawString(self.left,22,'Deutsch 5.3 | Zootiere');self.c.drawRightString(self.w-28.35,22,str(self.n))
 def block(self,title,s):self.p(title,15,True,4);self.p(s,14,gap=12)
 def end(self):
  self.c.save();manifest.append({'path':str(self.path.relative_to(ROOT)),'pages':self.n,'student':self.w<500})
def pages(name,key,label,a4=False):
 d=Doc(name,a4)
 for page in DATA[key]:
  d.page(label,page['title'])
  for title,s in page['blocks']:d.block(title,s)
 d.end()
def rubric():
 source=json.loads((ROOT/'materialien/kompetenzen_etappen.json').read_text())
 d=Doc('Kompetenzraster_4_Standards_A5.pdf')
 for c in source['criteria']:
  d.page(c['id']+' | Vier Standards',c['title'])
  for level in source['levels']:d.block(level,c['descriptors'][level])
 d.end()
 text=' '.join(p.get_text() for p in fitz.open(OUT/'Kompetenzraster_4_Standards_A5.pdf'))
 norm=lambda s:re.sub(r'\s+','',s)
 for c in source['criteria']:
  for v in c['descriptors'].values():assert norm(v) in norm(text)
def teacher():
 d=Doc('Lehrkraft_Einsatz_A4.pdf',True)
 for page in json.loads((OUT/'lehrkraft.json').read_text()):
  d.page('Lehrkraft | Lernweg und Wahlzeit',page['title'])
  for title,s in page['blocks']:d.block(title,s)
 d.end()
def validate():
 for item in manifest:
  doc=fitz.open(ROOT/item['path']);assert len(doc)==item['pages'];sizes=[]
  for p in doc:
   if item['student']:assert abs(p.rect.width-419.528)<.05 and abs(p.rect.height-595.276)<.05
   for b in p.get_text('dict')['blocks']:
    for l in b.get('lines',[]):
     for s in l['spans']:
      sizes.append(s['size']);x0,y0,x1,y1=s['bbox'];assert s['size']>=13.99 and x0>=41.5 and x1<=p.rect.width-27 and y0>=20 and y1<p.rect.height-10,(item,s)
      assert s['color']==0,(item,s)
  item['minimumFontPt']=round(min(sizes),2);item['bytes']=(ROOT/item['path']).stat().st_size;item['sha256']=hashlib.sha256((ROOT/item['path']).read_bytes()).hexdigest()
 report={'files':manifest,'rubricDescriptorParity':True,'visualReview':'pending','sourceSha256':hashlib.sha256((OUT/'inhalt.json').read_bytes()).hexdigest()}
 (OUT/'Pruefbericht.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False))
if __name__=='__main__':
 for fn,key,label in [('Lernweg_Zootiere_A5.pdf','lernweg','Lernweg'),('Kompetenzuebersicht_A5.pdf','kurzraster','Kompetenzübersicht'),('Individuelle_Foerderziele_A5.pdf','foerderziele','Individuelle Fachziele'),('Projekt_1_Tierlexikon_A5.pdf','p1','Wahlprojekt P1'),('Projekt_2_Tierraetsel_A5.pdf','p2','Wahlprojekt P2'),('Projekt_3_Tiervergleich_A5.pdf','p3','Wahlprojekt P3'),('Blatt_10_Wiederholung_A5.pdf','w10','Wahlhilfe nach Feedback')]:pages(fn,key,label)
 rubric();teacher()
 combo=fitz.open()
 for f in ['Projekt_1_Tierlexikon_A5.pdf','Projekt_2_Tierraetsel_A5.pdf','Projekt_3_Tiervergleich_A5.pdf']:combo.insert_pdf(fitz.open(OUT/f))
 combo.save(OUT/'Projekte_1-3_A5.pdf',garbage=4,deflate=True);manifest.append({'path':'materialien/lernweg_wahlphase/Projekte_1-3_A5.pdf','pages':len(combo),'student':True});validate()
