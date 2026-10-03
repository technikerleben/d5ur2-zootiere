"""Pack inspected, generated page images into A5 PDFs without editing their content.
Usage: python tools/assemble_etappe1_bildfassung.py /path/to/final.json
The external manifest contains 14 ordered generated image paths.
"""
from pathlib import Path
import sys,json,hashlib
import fitz
root=Path(__file__).resolve().parents[1]; out=root/'materialien/etappe1/bildfassung'
pages=json.loads(Path(sys.argv[1]).read_text());assert len(pages)==14
names=[('Etappe1_Schuelerpaket_A5_Otter_Dino.pdf',pages[:10]),('GN1_A_A5_Otter_Dino.pdf',pages[10:12]),('GN1_B_A5_Otter_Dino.pdf',pages[12:14])]
report={'date':'2026-10-03','pdfImageEncoding':'JPEG quality 95, original resolution; no cropping or text edits','visualTextReview':'Alle 14 Bildseiten mit der jeweiligen Textquelle verglichen. Seite 1 wegen eines Kommas statt Punkt neu erzeugt; korrigierte Fassung verwendet.','minimumFontPt':'14 pt in den Textquellen technisch geprüft; in Bildfassungen nicht technisch zertifizierbar.','files':[]}
for name,items in names:
 doc=fitz.open();imgs=[]
 for item in items:
  img=Path(item['generated']);p=doc.new_page(width=419.528,height=595.276)
  # Preserve full page image, no cropping. A small right shift provides extra hole space.
  pix=fitz.Pixmap(str(img));w=419.528-17.008;h=w*pix.height/pix.width;y=(595.276-h)/2
  p.insert_image(fitz.Rect(17.008,y,419.528,y+h),stream=pix.tobytes("jpeg",jpg_quality=95))
  imgs.append({'sourcePdf':item['file'],'sourcePage':item['page'],'generatedFile':img.name,'sha256':hashlib.sha256(img.read_bytes()).hexdigest()})
 doc.set_metadata({'title':name.replace('_',' '),'author':'Deutsch 5.3 / 5.5','subject':'Sprachspur: Wortarten und Nomenzerlegung; bildgeneriert mit Otter und Dino'})
 doc.save(out/name,garbage=4,deflate=True)
 check=fitz.open(out/name);assert len(check)==len(items)
 for p in check:assert len(p.get_images())==1 and abs(p.rect.width-419.528)<.01 and abs(p.rect.height-595.276)<.01
 report['files'].append({'name':name,'pages':len(check),'bytes':(out/name).stat().st_size,'images':imgs})
(out/'Pruefbericht.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps([{'name':x['name'],'pages':x['pages'],'bytes':x['bytes']} for x in report['files']]))
