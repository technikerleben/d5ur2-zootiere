"""Generate step-2 print materials. Requires reportlab; fonts from system DejaVu.
Run from any directory: python tools/generate_schritt2.py
"""
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'materialien' / 'lernweg'
OUT.mkdir(parents=True, exist_ok=True)
for name, file in [('Text','DejaVuSans.ttf'),('Bold','DejaVuSans-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name, '/usr/share/fonts/truetype/dejavu/'+file))
BLUE='#245688'; DARK='#18324A'; MINT='#48DCCB'; ORANGE='#F0A66F'
W,H=595.276,841.89

def para(c, text, x, y, width=503, size=13, color=DARK, bold=False):
    st=ParagraphStyle('p',fontName='Bold' if bold else 'Text',fontSize=size,leading=size*1.35,textColor=HexColor(color),alignment=TA_LEFT)
    p=Paragraph(text,st); _,height=p.wrap(width,1000)
    p.drawOn(c,x,H-y-height)
    return y+height

def line(c,y,x=46,width=503):
    c.setStrokeColor(HexColor('#C5D0D9'));c.setLineWidth(1);c.line(x,H-y,x+width,H-y)

def head(c,title,sub,page):
    c.setTitle(title+' | Deutsch 5.3 · Zootiere')
    c.setStrokeColor(HexColor(BLUE));c.setLineWidth(4);c.line(46,H-36,549,H-36)
    para(c,'OTTERKLASSE 5.3  /  DEUTSCH',46,48,size=10,bold=True,color=BLUE)
    para(c,title,46,70,size=25,bold=True,color=BLUE)
    para(c,sub,46,110,size=12)
    line(c,796)
    para(c,'Zootiere · Lernbuddy bewusst nutzen',46,806,size=9)
    para(c,str(page),520,806,width=30,size=9)

def box(c,x,y):
    c.setStrokeColor(HexColor(DARK));c.setLineWidth(1);c.rect(x,H-y-10,10,10)

def section(c,title,y,color=BLUE):
    c.setFillColor(HexColor(color));c.rect(46,H-y-19,5,19,fill=1,stroke=0)
    para(c,title,60,y,width=489,size=15,bold=True,color=BLUE)

def learner():
    c=canvas.Canvas(str(OUT/'Mein_Lernweg_Zootiere_A4.pdf'),pagesize=(W,H))
    head(c,'Mein Lernweg: Zootiere','Genau hinsehen, verständlich beschreiben',1)
    para(c,'Name: ____________________________________',46,140,size=13)
    section(c,'Dein Ziel',178)
    para(c,'Du beschreibst ein Zootier sachlich und geordnet. Dafür nutzt du Bilder und Sachtexte. Gemeinsam übst du am Fischotter.',46,208,size=14)
    section(c,'So gehst du vor',282)
    para(c,'Input → Übung → Vertiefung → Probearbeit → Projekte → Lernerfolgskontrolle (Arbeit)',46,312,size=13,bold=True)
    para(c,'Vertiefungen und Projekte sind freiwillig. Du musst nicht jedes Blatt bearbeiten. Vereinbare passende Übungen mit deiner Lehrkraft.',46,365,size=13)
    section(c,'Deine Übungen',432)
    para(c,'Kreise die vereinbarten Blätter ein. Hake eine Zeile ab, wenn du deine vereinbarten Übungen dazu geprüft hast.',46,462,size=13)
    rows=[('1 / 2','Du erkennst und benennst genaue Merkmale.'),('3 / 4','Du findest und ordnest Informationen.'),('5 / 6','Du nutzt genaue Wörter und sachliche Sätze.'),('7 / 8','Du planst und schreibst deine Tierbeschreibung.'),('9','Du prüfst deinen Text und verbesserst ihn.'),('10','Du übst nach der Probearbeit gezielt weiter.')]
    y=527
    for num,t in rows:
        box(c,46,y+3);para(c,'Blatt '+num,66,y,width=95,size=12,bold=True)
        para(c,t,166,y,width=383,size=12);line(c,y+33);y+=40
    c.showPage()
    head(c,'Zeige, was du kannst','Dein Ergebnis zählt, nicht die Zahl deiner Haken.',2)
    stages=[('1 · Informationen zeigen','Zeige eine Information auf dem Foto und eine im Sachtext. Erkläre, wo du sie gefunden hast.','Nach Blatt 3 / 4'),('2 · Deinen Text prüfen','Schreibe eine vollständige Tierbeschreibung. Prüfe sie. Zeige eine gelungene Stelle und deinen nächsten Lernschritt.','Nach Blatt 9'),('3 · Probearbeit nutzen','Bearbeite die Probearbeit. Du bekommst keine Note. Nutze die Rückmeldung und vereinbare deine nächste Übung.','Für alle verbindlich'),('4 · Lernerfolgskontrolle (Arbeit)','Beschreibe ein neues Tier. Die Lehrkraft erklärt dir vorher die Arbeitszeit und die erlaubten Hilfen.','Für alle verbindlich')]
    y=153
    for title,body,note in stages:
        section(c,title,y);para(c,note,60,y+26,size=10,color=BLUE)
        para(c,body,46,y+47,size=13);y+=132
    section(c,'Freiwillig weiterforschen',686,color=ORANGE)
    para(c,'Wenn du die Grundlagen sicher kannst, wähle eine Vertiefung oder ein Projekt. Besprich deine Wahl mit der Lehrkraft.',46,716,size=13)
    c.save()

def help_sheet():
    c=canvas.Canvas(str(OUT/'Lernbuddy_Zielhilfe_Zootiere_A4.pdf'),pagesize=(W,H))
    head(c,'Dein Lernbuddy in Deutsch','Nutze diese Hilfe nur, wenn du sie brauchst.',1)
    section(c,'1 · Planung',152)
    para(c,'Lies deine letzte Reflexion im Heft. Wähle ein Ziel und eine passende Aufgabe. Schreibe dein Ziel kurz auf den Lernbuddy.',46,181,size=13)
    goals=[('Blatt 1 / 2','Du benennst sichtbare Merkmale genau.'),('Blatt 3 / 4','Du findest und ordnest wichtige Informationen.'),('Blatt 5 / 6','Du schreibst genaue, sachliche Sätze.'),('Blatt 7 / 8','Du ordnest deinen Text mit einem Schreibplan.'),('Blatt 9','Du prüfst deinen Text mit den Kriterien.'),('Blatt 10','Du wählst dein Ziel aus der Rückmeldung.')]
    y=249
    for n,t in goals:
        para(c,n,46,y,width=106,size=12,bold=True);para(c,t,155,y,width=394,size=12);y+=27
    para(c,'Prüfe kurz deine Energie und mögliche Ablenker. Was hilft dir, anzufangen?',46,420,size=12)
    section(c,'2 · Durchführung',471,color=ORANGE)
    para(c,'Lege die Aufgabe an deinen Lernbuddy. Nutze eine passende Strategie. Prüfe zwischendurch: Hilft dein Weg dir, dein Ziel zu erreichen?',46,502,size=13)
    para(c,'Wenn du feststeckst: Lies den Auftrag erneut. Nutze ein Beispiel oder eine Hilfe. Frage ein anderes Kind, dann die Lehrkraft. Wenn du überfordert bist, darfst du direkt die Lehrkraft fragen.',46,564,size=12)
    section(c,'3 · Reflexion',650,color=MINT)
    para(c,'Zeige eine gelungene Stelle. Schreibe vor dem Abwischen kurz ins Heft:',46,680,size=13)
    para(c,'Das ist mir gelungen: …<br/>Als Nächstes übe ich … / Diese Hilfe nutze ich wieder: …',46,722,size=12,bold=True)
    c.save()

def observation():
    out=ROOT/'materialien'/'lehrkraft';out.mkdir(parents=True,exist_ok=True)
    c=canvas.Canvas(str(out/'Beobachtung_Lernbuddy_A4.pdf'),pagesize=(W,H))
    head(c,'Lernbuddy: Kurzbeobachtung','Lehrkraftbogen · Nur ausgewählte Kinder beobachten.',1)
    para(c,'Datum / Doppelstunde: ______________________________',46,150,size=12)
    para(c,'Z = nennt ein fachliches Ziel · W = prüft den Weg / nutzt Hilfe<br/>B = zeigt einen Beleg · N = leitet einen nächsten Schritt ab',46,183,size=12)
    para(c,'S = selbstständig · I = nach Impuls · U = mit Unterstützung<br/>– = nicht beobachtet. Keine Punkte oder Noten bilden.',46,232,size=12)
    y=296;xs=[46,142,178,214,250,286,549]
    for i,label in enumerate(['Kürzel','Z','W','B','N','Beleg / nächster Impuls']):
        para(c,label,xs[i]+4,y+6,width=xs[i+1]-xs[i]-8,size=9,bold=True)
    for row in range(9):
        yy=y+row*43
        line(c,yy)
    for x in xs:
        c.setStrokeColor(HexColor('#C5D0D9'));c.setLineWidth(1);c.line(x,H-y,x,H-(y+8*43))
    section(c,'Kurze Rückmeldung',670)
    para(c,'Beispiel: „Du hast die Wortbank nach einem Hinweis genutzt. Probiere sie beim nächsten Satz selbst aus.“',46,700,size=12)
    para(c,'Ausgefüllte Bögen nur schulisch geschützt aufbewahren.<br/>Keine Namen oder Beobachtungen ins öffentliche Repository laden.',46,753,size=10)
    c.save()

if __name__=='__main__':
    learner();help_sheet();observation()
