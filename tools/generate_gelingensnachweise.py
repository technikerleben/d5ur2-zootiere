"""Gelingensnachweise 1/2, Varianten A/B und Lehrkraftmaterial.

Run: python tools/generate_gelingensnachweise.py
Requires reportlab, pymupdf, Pillow and DejaVu Sans.
All student pages: A5 portrait, grayscale, >=14 pt, 15 mm left margin.
"""
from pathlib import Path
import json
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
import fitz

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'materialien'/'gelingensnachweise'
OUT.mkdir(parents=True,exist_ok=True)
for name,file in [('Text','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name,'/usr/share/fonts/truetype/dejavu/'+file))
PHOTO=OUT/'Fischotter_DavePape_Graustufen.jpg'
SOURCE='https://commons.wikimedia.org/wiki/File:Lutra_lutra_1_-_Otter,_Owl,_and_Wildlife_Park.jpg'
manifest=[]

class Doc:
    def __init__(self,name,a4=False):
        self.path=OUT/name
        self.w,self.h=(595.276,841.89) if a4 else (419.528,595.276)
        self.left=42.52; self.right=28.35
        self.width=self.w-self.left-self.right
        self.c=canvas.Canvas(str(self.path),pagesize=(self.w,self.h),pageCompression=1)
        self.c.setTitle(name.replace('_',' ').replace('.pdf',''))
        self.c.setAuthor('Deutsch 5.3 - Zootiere')
        self.n=0; self.y=0
    def p(self,text,size=14,bold=False,gap=9):
        assert size>=14
        p=Paragraph(text,ParagraphStyle('p',fontName='Bold' if bold else 'Text',fontSize=size,leading=size*1.32,textColor=Color(.08,.08,.08)))
        _,h=p.wrap(self.width,1000)
        assert self.y+h<=self.h-51,(self.path.name,self.n,self.y,h,text)
        p.drawOn(self.c,self.left,self.h-self.y-h)
        self.y+=h+gap
    def page(self,label,title,footer='Deutsch 5.3 | Zootiere'):
        if self.n:self.c.showPage()
        self.n+=1
        self.c.bookmarkPage('s'+str(self.n))
        self.c.addOutlineEntry(label+' - '+title,'s'+str(self.n))
        self.c.setStrokeGray(.2);self.c.setLineWidth(1.5)
        self.c.line(self.left,self.h-24,self.w-self.right,self.h-24)
        self.y=34
        self.p(label,15,True,7);self.p(title,22,True,15)
        self.c.setFont('Text',14);self.c.setFillGray(.2)
        self.c.drawString(self.left,24,footer)
        self.c.drawRightString(self.w-self.right,24,str(self.n))
    def block(self,title,text):
        self.p(title,15,True,5);self.p(text,gap=14)
    def end(self):
        self.c.save()
        manifest.append({'path':str(self.path.relative_to(ROOT)),'pages':self.n,'student':self.w<500})

TEXTS={
'A':'Der Fischotter lebt an Flüssen und Seen mit geschützten Ufern. Sein Körper ist lang gestreckt. Er hat kurze Beine. Sein Fell ist oben dunkelbraun. Kopf und Rumpf sind zusammen etwa 60 bis 90 Zentimeter lang. Der Schwanz kommt noch dazu. Der Fischotter frisst vor allem Fische, aber auch Frösche und Krebse.',
'B':'An Flüssen und Seen mit geschützten Ufern lebt der Fischotter. Er frisst vor allem Fische, aber auch Frösche und Krebse. Sein Kopf ist breit und flach. Sein Schwanz ist kräftig. Kopf und Rumpf messen zusammen etwa 60 bis 90 Zentimeter. Der Schwanz wird nicht mitgemessen. Der Fischotter hat kurze Beine.'
}

def gn1(v):
    d=Doc('GN1_'+v+'_Tierdetektiv_A5.pdf')
    d.page('Gelingensnachweis 1'+v+' | Material','Der Fischotter')
    from PIL import Image
    w,h=Image.open(PHOTO).size
    ih=135; iw=ih*w/h
    d.c.drawImage(str(PHOTO),d.left+(d.width-iw)/2,d.h-d.y-ih,iw,ih)
    d.y+=ih+9
    d.p('Foto: Dave Pape | Public Domain',14,gap=3)
    d.p('<link href="'+SOURCE+'"><u>Bildquelle</u></link> | Graustufenfassung',14,gap=12)
    d.p(TEXTS[v],14,gap=0)
    d.page('Gelingensnachweis 1'+v+' | Aufgaben','Tierdetektiv')
    d.p('Du brauchst die Materialseite und dein Heft. Schreibe <b>1'+v+'</b> über deine Antworten.',gap=13)
    d.block('Aufgabe 1 | Merkmale finden','Notiere zwei genaue äußere Merkmale:<br/><b>B:</b> ein Merkmal, das du auf dem Bild erkennst.<br/><b>T:</b> ein anderes Merkmal aus dem Text.')
    d.block('Aufgabe 2 | Größe finden','Wie lang sind Kopf und Rumpf zusammen? Notiere die Angabe mit Einheit. Schreibe dazu, ob der Schwanz mitgemessen wird.')
    d.block('Aufgabe 3 | Informationen ordnen','Schreibe die Überschriften <b>Lebensraum</b> und <b>Nahrung</b> ins Heft. Notiere darunter jeweils eine passende Angabe aus dem Text in Stichwörtern.')
    d.p('Zeige beim Vergleichen deine Bildstelle und die passenden Textstellen.',gap=8)
    d.p('Du bekommst keine Note. Zeige, was dir schon gelingt.',14,gap=0)
    d.end()

def gn2(v):
    d=Doc('GN2_'+v+'_Genaue_Saetze_A5.pdf')
    d.page('Gelingensnachweis 2'+v,'Genaue Sätze')
    d.p('Schreibe <b>2'+v+'</b> über deine Antworten im Heft. Nutze die Tierangaben auf dieser Seite.',gap=13)
    groups=(['der Fischotter - an Flüssen und Seen - leben','sein Kopf - breit und flach - sein','er - vor allem Fische - fressen'] if v=='A' else ['der Fischotter - an geschützten Ufern - leben','sein Körper - lang gestreckt - sein','er - auch Frösche - fressen'])
    d.block('Aufgabe 1 | Drei Sätze','Bilde aus jeder Wortgruppe einen vollständigen Satz im Präsens:<br/>'+ '<br/>'.join(chr(97+i)+') '+t for i,t in enumerate(groups)))
    bad,fact=('der fischotter hatte schöne beine','Die Beine sind kurz.') if v=='A' else ('der fischotter hatte einen schönen schwanz','Der Schwanz ist kräftig.')
    d.block('Aufgabe 2 | Einen Satz verbessern','Schreibe diesen Satz sachlich, genau und im Präsens. Prüfe auch die Schreibung und das Satzende:<br/><br/>'+bad+'<br/><br/><b>Tierangabe:</b> '+fact)
    d.p('Lies deine vier Sätze. Sind die Satzanfänge und Nomen groß? Stehen am Ende Punkte?',gap=9)
    d.p('Du bekommst keine Note. Zeige, was dir schon gelingt.',14,gap=0)
    d.end()

def solutions():
    d=Doc('GN1_GN2_Erwartungshorizonte_Lehrkraft_A4.pdf',True)
    d.page('Lehrkraft | Nachweise 1 und 2','Einsatz und Entscheidung')
    for title,body in [
    ('A und B sind gleichwertige Varianten','A ist für den ersten Versuch vorgesehen, B für einen erneuten Nachweis. B wird nicht vorher als Übung ausgegeben. Bei einem einzelnen offenen Ziel nur die zugehörige Aufgabe wiederholen. Varianten prüfen dieselben Kompetenzen; gleiche Schwierigkeit ist eine Planungsabsicht, noch kein Ergebnis einer Erprobung.'),
    ('Material und Zeit','GN1: zwei A5-Seiten pro Variante (Material und Aufgaben). Beide Seiten zugänglich halten; die Aufgabenkarte liegt in der Mitte des vorhandenen Lernbuddys. GN2: eine A5-Seite pro Variante. Antworten im Heft. Richtwert jeweils 5-8 Minuten nach Klärung des Auftrags; kein Abbruch wegen langsamen Schreibens.'),
    ('Hilfen vorab vereinbaren','Auftrag vorlesen, Wörter erklären oder eine vereinbarte Wortbank zulassen und dokumentieren. Die fachliche Antwort nicht vorsagen. Bei GN2 beim Vorlesen keine Lösungen durch richtige Verbformen vorwegnehmen. Keine Musterlösung, Partnerlösung oder Kiosk-Lösung während des Nachweises.'),
    ('Weiterarbeit festlegen','Kernziele je Nachweis auf den folgenden Seiten prüfen. Dokumentieren: gezeigt / noch offen / nicht beobachtet. Kein Punkteschnitt und keine pauschale Prozentgrenze. Offene Ziele führen zu einer passenden Teilübung und einem kurzen erneuten Nachweis. Bei Überforderung Ziel oder Unterstützung gemeinsam anpassen; kein unbegrenztes Warten.'),
    ('Förderstandard und Lernbuddy','Die vorliegenden Karten prüfen das gemeinsame Etappenziel. Sie sind keine pauschale Förderfassung. Individuelle Förderziele und Antwortformen vorab festlegen; diese werden gesondert ausgewertet. Konkrete Förderkarten folgen noch. Lernbuddy-Nutzung getrennt rückmelden und Reflexion vor dem Abwischen ins Heft übertragen.')]: d.block(title,body)
    d.end()
    # Add further pages to one output with PyMuPDF after separate generation.
    guide=fitz.open(d.path)
    for v in ['A','B']:
        t=Doc('_GN1_'+v+'_temp.pdf',True)
        t.page('Lehrkraft | Gelingensnachweis 1'+v,'Tierdetektiv: Lösungen')
        t.block('Aufgabe 1 | Bild und Text','<b>B:</b> Zum Beispiel lange Tasthaare an der Schnauze, kleine Ohren oder braunes Fell. Ein Körperteil allein ist noch kein genaues Merkmal. Nur tatsächlich sichtbare Merkmale akzeptieren.<br/><b>T:</b> '+('Zum Beispiel lang gestreckter Körper, kurze Beine oder oben dunkelbraunes Fell.' if v=='A' else 'Zum Beispiel breiter und flacher Kopf, kräftiger Schwanz oder kurze Beine.')+'<br/>Zwei unterscheidbare Merkmale müssen vorliegen. Ein Merkmal darf auch in beiden Quellen vorkommen, wenn das Kind die gewählte Fundstelle richtig zeigt. Zwei Formulierungen derselben Fellfarbe zählen nicht doppelt.')
        t.block('Aufgabe 2 | Maßangabe','Kopf und Rumpf zusammen etwa 60-90 cm (oder Zentimeter). Der Schwanz ist nicht enthalten. Gleichbedeutende Formulierungen akzeptieren. Eine Angabe ohne Bezug auf Kopf und Rumpf bzw. ohne geklärten Schwanzbezug nachfragen lassen.')
        t.block('Aufgabe 3 | Zuordnung','<b>Lebensraum:</b> Flüsse und Seen, gegebenenfalls geschützte Ufer.<br/><b>Nahrung:</b> vor allem Fische; Frösche oder Krebse sind ebenfalls richtige Einzelangaben. Je eine passende Angabe unter der richtigen Überschrift genügt. Ganze Sätze sind nicht verlangt.')
        t.block('Kernziele für diese Etappe','1. Zwei genaue äußere Merkmale richtig benannt.<br/>2. Ein Bildbeleg und ein Textbeleg richtig zugeordnet und gezeigt.<br/>3. Maß mit Einheit und richtigem Bezug erfasst.<br/>4. Lebensraum und Nahrung richtig entnommen.<br/>5. Angaben unter passenden Überschriften geordnet.<br/>Schreibfehler sind hier kein eigenes Ziel; bei unlesbaren Antworten kurz mündlich klären.')
        t.block('Wenn etwas noch offen ist','Merkmale/Bildbeleg: Blatt 2. Textangaben: Blatt 3. Zuordnung: Blatt 4. Danach nur das offene Ziel erneut zeigen lassen. Die volle B-Variante ist bei breiterem Übungsbedarf verfügbar.')
        t.end();guide.insert_pdf(fitz.open(t.path));t.path.unlink();manifest.pop()
    for v in ['A','B']:
        t=Doc('_GN2_'+v+'_temp.pdf',True)
        t.page('Lehrkraft | Gelingensnachweis 2'+v,'Genaue Sätze: Lösungen')
        examples=(['Der Fischotter lebt an Flüssen und Seen.','Sein Kopf ist breit und flach.','Er frisst vor allem Fische.','Der Fischotter hat kurze Beine.'] if v=='A' else ['Der Fischotter lebt an geschützten Ufern.','Sein Körper ist lang gestreckt.','Er frisst auch Frösche.','Der Fischotter hat einen kräftigen Schwanz.'])
        t.block('Aufgabe 1 | Mögliche Sätze','<br/>'.join(chr(97+i)+') '+s for i,s in enumerate(examples[:3])))
        t.block('Aufgabe 2 | Mögliche Verbesserung',examples[3]+'<br/>Erwartet: „hat“ statt „hatte“, genaue Angabe statt „schön“, großer Satzanfang, große Nomen und Satzschlusspunkt. Gleichwertige Formulierungen wie „Die Beine des Fischotters sind kurz.“ bzw. „Der Schwanz des Fischotters ist kräftig.“ gelten ebenfalls.')
        t.block('Kernziele für diese Etappe','1. Alle vier Aussagen passen zu den bereitgestellten Tierangaben.<br/>2. Die Aussagen sind vollständige, verständliche Sätze.<br/>3. Die Verben stehen im Präsens und passen zum Subjekt.<br/>4. Die Angaben sind sachlich und genau; die Wertung wurde ersetzt.<br/>5. Satzanfänge und Satzschlusszeichen zeigen erkennbare Satzgrenzen. Nomen wurden geprüft.')
        t.block('Grenzfälle und Rückmeldung','Andere sinnvolle Wortstellungen anerkennen. Einzelne sonstige Schreibfehler verhindern das Etappenziel nicht, wenn die gezielt geprüften Grundregeln überwiegend gelingen und der Text verständlich bleibt. Einzelfehler an einer neuen kurzen Stelle nachprüfen, bevor daraus ein grundsätzlicher Bedarf abgeleitet wird. Wiederholte Satzfragmente, falsche Verbformen oder fehlende Satzgrenzen zeigen gezielten Übungsbedarf.')
        t.block('Wenn etwas noch offen ist','Genaue Wörter: Blatt 5. Satzbildung, Präsens oder Satzgrenzen: Blatt 6. Für den erneuten Nachweis einen passenden B-Satz oder die B-Überarbeitungsaufgabe auswählen. Bereits gezeigte Ziele bleiben anerkannt.')
        t.end();guide.insert_pdf(fitz.open(t.path));t.path.unlink();manifest.pop()
    final=d.path.with_suffix('.new.pdf');guide.save(final,garbage=4,deflate=True);guide.close();final.replace(d.path)
    manifest[-1]['pages']=5

def conversation():
    d=Doc('GN3_Gespraechsleitfaden_Lehrkraft_A4.pdf',True)
    d.page('Lehrkraft | Gelingensnachweis 3','Mein Text zeigt es')
    d.p('Grundlage: vorhandener Übungstext zu Erdmännchen oder Rotem Panda, eigener Schreibplan und Kindercheckliste K1-K6. Kein zusätzlicher Aufsatz.',gap=14)
    for title,body in [
    ('Vor dem Gespräch','Text kurz sichten. Richtigkeit mit dem Tierpaket abgleichen. Eine gelungene Stelle und höchstens zwei offene Fragen markieren. 3-5 Minuten Gespräch pro Kind gestaffelt in den Arbeitsphasen der Doppelstunden 4-5 einplanen; im Teamteaching aufteilen.'),
    ('1 | Informationen und Aufbau zeigen','„Zeige mir den Tiernamen, deine Maßangabe, den Lebensraum und die Nahrung.“<br/>„Welche vier verschiedenen äußeren Merkmale beschreibst du?“<br/>„Wie hast du deinen Text geordnet?“<br/>Nur bei Unklarheiten nachfragen; die Textsichtung nicht vollständig mündlich wiederholen.'),
    ('2 | Sprache und Prüfung erklären','„Lies einen Satz vor, der dir gut gelungen ist. Was ist daran genau?“<br/>„Zeige mir, was du geprüft hast. Musstest du etwas ändern?“<br/>Nötige Verbesserung oder begründetes Beibehalten einer bereits richtigen Stelle akzeptieren. Rechtschreibung an der Textsichtung prüfen, nicht nur am mündlichen Erklären.'),
    ('3 | Nächsten Schritt vereinbaren','„Was gelingt dir schon? Was übst du als Nächstes?“<br/>Bei offenem Ziel passende Teilübung vereinbaren. Danach eine verbesserte Stelle zeigen lassen, nicht den gesamten Text neu schreiben lassen.'),
    ('Entscheidung','Etappenziel gezeigt, wenn der Text die Mindestanforderungen K1-K6 erfüllt und das Kind seine Prüfung an einem Beleg zeigen kann. Einzelne Fehler dürfen bleiben; Qualität kriterienbezogen beurteilen, keine Fehler zählen oder Standards zu Punkten addieren. Fehlende Kerninformationen oder weniger als vier Merkmale werden gezielt ergänzt.')]:d.block(title,body)
    d.end()
    q=Doc('_GN3_Protokoll_temp.pdf',True)
    q.page('Lehrkraft | Gelingensnachweis 3','Kurzprotokoll')
    q.p('Kürzel: __________________  Datum: ______________<br/>Tier: ____________________  Variante/Ziel: __________',gap=14)
    q.p('Vorab vereinbarte Hilfen: __________________________<br/>Individuelles Förderziel, falls zutreffend: ______________<br/>________________________________________________',gap=16)
    q.p('Markiere: G = gezeigt, O = noch offen,<br/>N = nicht beobachtet. Notiere einen kurzen Beleg.',gap=12)
    for title,body in [
    ('K1 | Informationen','Tiername, Maßangabe, Lebensraum, Nahrung richtig.'),
    ('K2 | Aussehen','Mindestens vier verschiedene Merkmale richtig.'),
    ('K3 | Aufbau','Überblick und nachvollziehbare Ordnung.'),
    ('K4/K5 | Sprache und Sätze','Sachlich, überwiegend Präsens; verständliche Sätze.'),
    ('K6 | Schreibung und Prüfung','Grundregeln überwiegend sicher; Prüfung belegt.')]:
        q.p('<b>'+title+'</b>  G / O / N<br/>'+body+'<br/>Beleg: ________________________________________',14,gap=9)
    q.p('<b>Entscheidung:</b> Etappenziel gezeigt / gezielt nacharbeiten<br/><b>Nächste Aufgabe und erneuter Beleg:</b><br/>________________________________________________',14,gap=12)
    q.p('Bei zieldifferentem Lernen nur die vorher vereinbarten Ziele beurteilen; nicht pauschal vier Merkmale oder einen Fließtext verlangen. Lernbuddy-Anwendung getrennt rückmelden. Ausgefülltes Protokoll schulisch geschützt aufbewahren.',14,gap=0)
    q.end()
    doc=fitz.open(d.path);doc.insert_pdf(fitz.open(q.path));temp=d.path.with_suffix('.new.pdf');doc.save(temp,garbage=4,deflate=True);doc.close();temp.replace(d.path);q.path.unlink();manifest.pop();manifest[-1]['pages']=2

def validate():
    for item in manifest:
        doc=fitz.open(ROOT/item['path']);sizes=[]
        assert len(doc)==item['pages']
        for p in doc:
            if item['student']:
                assert abs(p.rect.width-419.528)<.05 and abs(p.rect.height-595.276)<.05
            for block in p.get_text('dict')['blocks']:
                for line in block.get('lines',[]):
                    for span in line['spans']:
                        sizes.append(span['size']);x0,y0,x1,y1=span['bbox']
                        assert span['size']>=13.99,(item,span)
                        assert x0>=41.5 and x1<=p.rect.width-27 and y0>=20 and y1<=p.rect.height-10,(item,span)
        item['minimumFontPt']=round(min(sizes),2);item['bytes']=(ROOT/item['path']).stat().st_size
    (OUT/'Pruefbericht.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
    print(json.dumps(manifest,ensure_ascii=False))

if __name__=='__main__':
    for variant in ['A','B']:gn1(variant)
    for variant in ['A','B']:gn2(variant)
    combined=fitz.open()
    for item in manifest:combined.insert_pdf(fitz.open(ROOT/item['path']))
    path=OUT/'GN1_GN2_Schuelerkarten_A5.pdf';combined.save(path,garbage=4,deflate=True)
    manifest.append({'path':str(path.relative_to(ROOT)),'pages':len(combined),'student':True})
    solutions();conversation();validate()
