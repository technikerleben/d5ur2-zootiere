#!/usr/bin/env python3
"""Zusatz-Input Etappe 3: „Vom Interview zum Tierlexikon – laut gedacht“.

Animierte HTML-Präsentation (eine Datei, offline). Am Fischotter-Interview wird
laut denkend gezeigt, wie aus dem Interview der Modelltext von Merkblatt 3 entsteht:
Sachangabe / nur Otto / Meinung unterscheiden, nach Themen ordnen, Präsens,
Text Schritt für Schritt mit fliegenden Wörtern aus dem Interview.

Ausgabe: ausgabe/etappe3/Input_Etappe3_Laut_gedacht.html
"""
import base64, html, io, json, re
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "ausgabe/etappe3/Input_Etappe3_Laut_gedacht.html"

# --------------------------------------------------------------------------
# Interview (Text 1:1 aus inhalt/interviews.json, „fischotter“)
# Segment: (id, Art, Text mit {Wort#wid}, Kurzform)
#   Arten: sach (T/M/A/L/N), otto (X), mein (W), vgl (V)
# --------------------------------------------------------------------------
S = lambda i, k, t, kurz: {"id": i, "k": k, "t": t, "kurz": kurz}
PAARE = [
    ("Frau Berger, wie fängt Ihr Tag bei den Ottern an?", [
        S("x1", "otto", "Um halb acht mache ich die Anlage sauber. Danach gibt es Frühstück.", "Anlage sauber"), " ",
        S("x2", "otto", "Unser Otto wartet dann schon am Gitter und pfeift laut.", "wartet am Gitter"), " ",
        S("w1", "mein", "Ehrlich gesagt ist er der süßeste Otter der Welt!", "süßester Otter")]),
    ("Was gibt es denn zum Frühstück?", [
        "Vor allem Fisch. ",
        S("x3", "otto", "Otto bekommt jeden Tag einen kleinen Eimer voll.", "ein Eimer am Tag"), " In der Natur ",
        S("n1", "sach", "{fressen#fressen} Fischotter hauptsächlich {Fische#fische}", "vor allem Fische"), ". ",
        S("n2", "sach", "Sie fangen {aber auch#aberauch} {Frösche und Krebse#froesche}.", "auch Frösche und Krebse"), " ",
        S("x4", "otto", "Gestern hat Otto einen Krebs ganz allein geknackt. Das hat richtig gekracht!", "Krebs geknackt")]),
    ("Wo {leben#leben} Fischotter, wenn sie nicht im Zoo sind?", [
        S("l1", "sach", "An {Flüssen und Seen#fluesse}.", "Flüsse und Seen"), " ",
        S("l2", "sach", "Sie {brauchen#brauchen} {Ufer#ufer}, an denen sie sich {verstecken#verstecken} können", "Ufer mit Verstecken"),
        ", zum Beispiel unter Büschen und Wurzeln. ",
        S("x5", "otto", "Deshalb liegen in unserer Anlage auch so viele alte Wurzeln herum.", "Wurzeln in der Anlage")]),
    ("Ist ein Otter eigentlich mit dem Biber verwandt?", [
        "Nein. ",
        S("t1", "sach", "{Fischotter#fo} {gehören#gehoeren} zu den {Mardern#mardern}.", "gehört zu den Mardern"),
        " Biber sind Nagetiere. Das ist etwas ganz anderes."]),
    ("Woran erkennt man einen Fischotter?", [
        "Schauen Sie mal, wie er durchs Wasser saust! ",
        S("a1", "sach", "Sein {Körper#koerper} ist {lang#lang1} und {schmal#schmal}", "Körper: lang und schmal"), ", ",
        S("v1", "vgl", "fast wie ein Torpedo", "Torpedo"), ". ",
        S("a2", "sach", "Die {Beine#beine} {sind#sind} dagegen richtig {kurz#kurz}.", "Beine: kurz"), " Und ",
        S("a3", "sach", "der {Kopf#kopf} {ist#ist3} {breit und flach#breitflach}", "Kopf: breit und flach"), ". Ich sage immer: ",
        S("v2", "vgl", "wie ein Brett mit Nase", "Brett mit Nase"), "."]),
    ("Und die Ohren? Ich sehe gar keine.", [
        S("a4", "sach", "Die sind ganz klein.", "Ohren: klein"),
        " Beim Tauchen kann er sie sogar verschließen, damit kein Wasser hineinläuft."]),
    ("Wie groß ist Otto eigentlich?", [
        S("x6", "otto", "Letzte Woche haben wir ihn gemessen. Von der Nase bis zum Schwanzansatz waren es 80 Zentimeter.", "80 cm gemessen"),
        " Der Schwanz kommt noch dazu. ",
        S("m1", "sach", "Fischotter sind meistens {60 bis 90 Zentimeter#zahl} {lang#lang2}, wenn man den {Schwanz#schwanz} nicht mitzählt.", "ohne Schwanz 60–90 cm")]),
    ("Darf man ihn streicheln? Das Fell sieht so weich aus.", [
        "Nein, ",
        S("x7", "otto", "Otto ist kein Kuscheltier. Ich fasse ihn nur an, wenn die Tierärztin kommt.", "kein Kuscheltier"), " ",
        S("a5", "sach", "Das {Fell#fell} {ist#ist2} sehr dicht.", "Fell: dicht"), " ",
        S("a6", "sach", "{Oben#oben} ist es {dunkelbraun#braun}, am Hals ist es heller.", "Fell: oben dunkelbraun")]),
    ("Gibt es noch etwas Besonderes?", [
        "Ja, ",
        S("a7", "sach", "die langen Tasthaare an der Schnauze", "Tasthaare an der Schnauze"),
        "! Damit spürt er Fische, auch wenn das Wasser trüb ist. Und ",
        S("a8", "sach", "zwischen den Zehen hat er Schwimmhäute", "Schwimmhäute zwischen den Zehen"), ". ",
        S("w2", "mein", "Deshalb ist er so ein toller Schwimmer.", "toller Schwimmer")]),
    ("Vielen Dank, Frau Berger!", [
        "Gern. ", S("x8", "otto", "Und kommt Otto bald besuchen!", "Otto besuchen")]),
]

def woerter(t):
    t = html.escape(t, quote=False)
    return re.sub(r"\{([^#}]+)#([a-z0-9]+)\}", r"<span class='w' data-w='\2'>\1</span>", t)

def interview_html():
    out = ["<div class='ivkopf'><b>Zoo-Reporter</b> · Interview mit Frau Berger, Tierpflegerin<br>"
           "<span>„Otto taucht am liebsten“ · Das Interview ist ausgedacht. Die Angaben über das Tier stimmen.</span></div>"]
    for n, (q, teile) in enumerate(PAARE):
        a = "".join(woerter(x) if isinstance(x, str) else
                    f"<span class='seg' data-s='{x['id']}' data-art='{x['k']}'>{woerter(x['t'])}</span>" for x in teile)
        out.append(f"<div class='paar' data-p='{n}'><p class='q'>{woerter(q)}</p><p class='a'>{a}</p></div>")
    return "<div class='iv'><div class='ivin'>" + "".join(out) + "</div></div>"

SEGS = {x["id"]: x for _, t in PAARE for x in t if isinstance(x, dict)}
PAAR_VON = {x["id"]: n for n, (_, t) in enumerate(PAARE) for x in t if isinstance(x, dict)}
WORT_PAAR = {}
for n, (q, t) in enumerate(PAARE):
    for s in [q] + [x if isinstance(x, str) else x["t"] for x in t]:
        for w in re.findall(r"#([a-z0-9]+)\}", s):
            WORT_PAAR[w] = n

# --------------------------------------------------------------------------
# Schritte: Prüfen (Folie 4)
# --------------------------------------------------------------------------
PRUEFEN = [
    (["x1", "x2", "w1"], "Frau Berger erzählt von ihrem Tag und von <b>Otto</b>. Das gilt nicht für alle Fischotter. "
                         "„Ehrlich gesagt … der süßeste“ – so findet <b>sie</b> Otto. Das ist eine <b>Meinung</b>."),
    (["x3", "n1", "n2", "x4"], "„In der Natur fressen Fischotter …“ – das gilt für <b>alle</b>. Eine Sachangabe! "
                               "„<b>Gestern</b> hat Otto …“ – Vergangenheit. Das ist ein Erlebnis mit Otto."),
    (["l1", "l2", "x5"], "Flüsse, Seen, Ufer mit Verstecken – so leben alle Fischotter. "
                         "„In <b>unserer Anlage</b>“ – das ist nur der Zoo."),
    (["t1"], "Zu welcher Tierfamilie gehören Fischotter? Zu den Mardern. Das gilt für alle. Gut für den <b>Überblick</b>."),
    (["a1", "v1", "a2", "a3", "v2"], "„fast wie ein Torpedo“ ist ein <b>Vergleich</b>. Ich schneide ihn ab und nehme nur die "
                                     "Sachangabe: <b>lang und schmal</b>. Beim Brett mit Nase genauso."),
    (["a4"], "„Die sind ganz klein“ – gemeint sind die Ohren. Das stimmt für alle Fischotter."),
    (["x6", "m1"], "Zwei Zahlen! Hier muss ich genau sein. <b>80 Zentimeter</b> – das ist Otto, letzte Woche gemessen. "
                   "<b>60 bis 90 Zentimeter</b> ohne Schwanz – das gilt für alle Fischotter."),
    (["x7", "a5", "a6"], "„Otto ist kein Kuscheltier“ – das ist nur Otto. Das Fell ist dicht und oben dunkelbraun: Sachangaben."),
    (["a7", "a8", "w2"], "„so ein <b>toller</b> Schwimmer“ – das ist eine Meinung. Aber: Schwimmhäute zwischen den Zehen – "
                         "das ist eine Sachangabe. Die nehme ich!"),
    (["x8"], "Zum Schluss lädt sie uns zu Otto ein. Das gehört nicht ins Lexikon."),
    ([], "Fertig geprüft! <b>14 Sachangaben</b> bleiben übrig. Nur die kommen in mein Tierlexikon."),
]

# --------------------------------------------------------------------------
# Ordnen (Folie 5)
# --------------------------------------------------------------------------
SPALTEN = [("ueb", "Überblick", ["t1", "m1"]),
           ("aus", "Aussehen", ["a1", "a2", "a3", "a4", "a5", "a6", "a7", "a8"]),
           ("leb", "Lebensraum", ["l1", "l2"]),
           ("nah", "Nahrung", ["n1", "n2"])]
ORDNEN_DENK = [
    "Ich ordne meine Sachangaben unter vier Überschriften. Zuerst der <b>Überblick</b>: Tierfamilie und Größe.",
    "Jetzt alles zum <b>Aussehen</b>. Ich zähle mit: Habe ich mindestens vier verschiedene Merkmale?",
    "Wo lebt der Fischotter? Das kommt unter <b>Lebensraum</b>.",
    "Und was frisst er? Das kommt unter <b>Nahrung</b>.",
    "Acht Merkmale – ich brauche mindestens vier. Ich nehme <b>Körper, Beine, Fell und Kopf</b>. "
    "Damit kann man sich den Fischotter gut vorstellen.",
]
WAHL = ["a1", "a2", "a3", "a6"]

# --------------------------------------------------------------------------
# Text (Folie 7): Modelltext Merkblatt 3, Wörter (wid, Zielform) fliegen aus dem Interview
# --------------------------------------------------------------------------
TEXT = [
    ("h", ["Der ", ("fo", "Fischotter")],
     "Ein Lexikonartikel braucht eine Überschrift: den Namen der <b>Tierart</b>. Nicht „Otto“!"),
    ("s", ["Der ", ("fo", "Fischotter"), " ", ("gehoeren", "gehört"), " zu den ", ("mardern", "Mardern"), "."],
     "Ich beginne mit dem Überblick. Aus „Fischotter <b>gehören</b>“ wird „Der Fischotter <b>gehört</b>“ – "
     "es ist ja ein Tier."),
    ("s", ["Er ", (None, "hat"), " einen ", ("lang1", "langen"), ", ", ("schmal", "schmalen"), " ", ("koerper", "Körper"), "."],
     "Den Torpedo lasse ich weg. „lang“ und „schmal“ stehen jetzt vor „Körper“. Dann bekommen sie eine Endung: "
     "<b>langen, schmalen</b>."),
    ("s", ["Ohne ", ("schwanz", "Schwanz"), " ", (None, "ist"), " er etwa ", ("zahl", "60 bis 90 Zentimeter"), " ", ("lang2", "lang"), "."],
     "Jetzt das Maß – mit Einheit und Bezug. Nicht 80 Zentimeter, das ist nur Otto. "
     "Für alle gilt: 60 bis 90 Zentimeter <b>ohne Schwanz</b>."),
    ("s", ["Seine ", ("beine", "Beine"), " ", ("sind", "sind"), " ", ("kurz", "kurz"), "."],
     "„dagegen richtig“ sagt nichts Genaues. Das lasse ich weg. Übrig bleibt: Seine Beine sind kurz."),
    ("s", ["Sein ", ("fell", "Fell"), " ", ("ist2", "ist"), " ", ("oben", "oben"), " ", ("braun", "dunkelbraun"), "."],
     "Das Fell. „Oben“ steht jetzt mitten im Satz. Darum schreibe ich es <b>klein</b>."),
    ("s", ["Der ", ("kopf", "Kopf"), " ", ("ist3", "ist"), " ", ("breitflach", "breit und flach"), "."],
     "„Brett mit Nase“ ist ein Vergleich – weg damit. Jetzt habe ich <b>vier Merkmale</b>: Körper, Beine, Fell, Kopf."),
    ("p", ["Er ", ("leben", "lebt"), " an ", ("fluesse", "Flüssen und Seen"), "."],
     "Neuer Absatz: der <b>Lebensraum</b>. Das Verb hole ich aus der Frage: <b>leben</b> → er <b>lebt</b>."),
    ("s", ["Dort ", ("brauchen", "braucht"), " er ", ("ufer", "Ufer"), " mit ", ("verstecken", "Verstecken"), "."],
     "<b>brauchen</b> → er <b>braucht</b>. Aus „sich verstecken“ mache ich ein Nomen: Ufer mit <b>Verstecken</b>. "
     "Nomen schreibe ich groß."),
    ("s", ["Er ", ("fressen", "frisst"), " vor allem ", ("fische", "Fische"), ", ", ("aberauch", "aber auch"), " ",
           ("froesche", "Frösche und Krebse"), "."],
     "Zum Schluss die <b>Nahrung</b>. <b>fressen</b> → er <b>frisst</b>. Statt „hauptsächlich“ schreibe ich „vor allem“."),
]

def artikel_html(mit_ids=True, gross=False):
    teile, absatz = [], []
    titel = ""
    for n, (art, toks, _) in enumerate(TEXT):
        h = []
        for t in toks:
            if isinstance(t, str):
                h.append(f"<span class='g'>{html.escape(t)}</span>")
            elif t[0] is None:
                h.append(f"<span class='g verb'>{html.escape(t[1])}</span>")
            else:
                h.append(f"<span class='t' data-src='{t[0]}'>{html.escape(t[1])}</span>")
        satz = f"<span class='satz' data-n='{n}'>{''.join(h)}</span>"
        if art == "h":
            titel = f"<h2 class='satz' data-n='{n}'>{''.join(h)}</h2>"
        else:
            if art == "p":
                teile.append(absatz); absatz = []
            absatz.append(satz)
    teile.append(absatz)
    body = "".join("<p>" + " ".join(a) + "</p>" for a in teile if a)
    return (f"<div class='lex{' gross' if gross else ''}'><div class='lexkopf'>Unser Tierlexikon · F</div>"
            f"{titel}{body}</div>")

# --------------------------------------------------------------------------
# Hilfsfunktionen
# --------------------------------------------------------------------------
def b64(p): return base64.b64encode(Path(p).read_bytes()).decode()

def font_css():
    f = ROOT / "assets/fonts"
    out = []
    for w, st, fn in [(400, "normal", "andika-latin-400-normal"), (700, "normal", "andika-latin-700-normal"),
                      (400, "italic", "andika-latin-400-italic"), (700, "italic", "andika-latin-700-italic"),
                      (400, "normal", "andika-latin-ext-400-normal"), (700, "normal", "andika-latin-ext-700-normal")]:
        out.append(f"@font-face{{font-family:'Andika';font-weight:{w};font-style:{st};"
                   f"src:url(data:font/woff2;base64,{b64(f / (fn + '.woff2'))}) format('woff2');}}")
    return "\n".join(out)

def foto():
    im = Image.open(ROOT / "assets/bilder/fischotter_farbe.jpg").convert("RGB")
    im.thumbnail((760, 760))
    buf = io.BytesIO(); im.save(buf, "JPEG", quality=80)
    return base64.b64encode(buf.getvalue()).decode()

def denk(txt, k=None, cls=""):
    dk = f" data-k='{k}'" if k is not None else ""
    return f"<div class='denk {cls}'{dk}><b>💭 Ich denke:</b> {txt}</div>"

KICK = "<div class='top'><span class='ph'>Laut gedacht</span><span class='kick'>Zootiere · Etappe 3 · Zusatz zum Input</span></div>"

def slide(inhalt, cls="", attr=""):
    return f"<section class='slide {cls}' {attr}>{inhalt}</section>"

# --------------------------------------------------------------------------
# Folien
# --------------------------------------------------------------------------
TASKCARDS = "https://schulendortmund.taskcards.app/#/board/86a516d4-8c24-40f8-9b4e-d3b50587ecbc?token=c62bc016-43cb-4d91-80e5-05c687e62385"

def qr_svg():
    import qrcode, qrcode.image.svg
    img = qrcode.make(TASKCARDS, image_factory=qrcode.image.svg.SvgPathImage, border=1)
    return img.to_string(encoding="unicode")

def folien():
    F = []
    # 1 Titel
    F.append(slide(f"""{KICK}
<div class='titelbox'><div class='tlinks'>
<h1 class='gross'>Vom Interview<br>zum Tierlexikon</h1>
<div class='ziel'><b>Ich denke laut:</b> Wie wird aus dem Interview über Otto ein Lexikontext über <b>den Fischotter</b>?</div>
<div class='weg'><span>Interview</span><i>→</i><span>prüfen</span><i>→</i><span>ordnen</span><i>→</i><span>Präsens</span><i>→</i><span class='z'>Lexikontext</span></div>
</div><figure class='tfoto'><img src='data:image/jpeg;base64,{foto()}' alt='Ein Fischotter'><figcaption>Foto: Dave Pape · Public Domain</figcaption></figure></div>""", "titel"))

    # 2 Auftrag
    F.append(slide(f"""{KICK}<h1><span class='n'>1</span>Mein Auftrag</h1>
<div class='zwei'><div class='spalte'>
<div class='blk auftrag'><span class='lab'>Situation</span>Unsere Klasse gestaltet ein <b>Tierlexikon</b>. Es fehlt noch ein Text über den Fischotter.
Die Schülerzeitung „Zoo-Reporter“ hat dafür Frau Berger interviewt.</div>
<div class='blk vergleich' data-k='1'><div><span class='lab'>Im Interview</span>Frau Berger <b>erzählt</b>: von ihrem Tag, von Otto, was sie denkt.</div>
<div><span class='lab'>Im Lexikon</span>steht nur, was für <b>alle Fischotter</b> gilt – sachlich und geordnet.</div></div>
</div><div class='spalte'>
{denk("Im Interview steht viel. Aber ein Lexikon ist kein Interview. Nicht alles darf hinein.", 1)}
{denk("Heute mache ich mein Denken <b>sichtbar</b>. Ich gehe das Interview Schritt für Schritt durch und sage laut, was ich denke.", 2)}
{denk("Am Ende steht mein Lexikontext. Ihr seht, welche Wörter aus dem Interview hineinfliegen.", 3)}
</div></div>"""))

    # 3 Prüffragen
    F.append(slide(f"""{KICK}<h1><span class='n'>2</span>Drei Prüffragen</h1>
<div class='zwei'><div class='spalte'>
<div class='pf sach' data-k='1'><span class='nr'>1</span><div><b>Gilt es für alle Fischotter?</b><br>→ <b>Sachangabe</b>. Das kommt ins Lexikon.</div></div>
<div class='pf otto' data-k='2'><span class='nr'>2</span><div><b>Geht es nur um Otto oder den Zoo?</b><br>→ <b>nur Otto</b>. Das lasse ich weg.</div></div>
<div class='pf mein' data-k='3'><span class='nr'>3</span><div><b>Sagt jemand, wie er das Tier findet?</b><br>→ <b>Meinung</b>. Das lasse ich weg.</div></div>
<div class='pf vgl' data-k='4'><span class='nr'>✂</span><div><b>Ein Vergleich?</b> („wie ein …“)<br>→ Ich nehme nur die Sachangabe heraus.</div></div>
</div><div class='spalte'>
<div class='blk signal' data-k='5'><span class='lab'>Signale im Interview</span>
<div class='sz'><span class='sig'>Otto · unser · bei uns</span><br>→ oft <b>nur Otto</b></div>
<div class='sz'><span class='sig'>gestern · letzte Woche · hat … gemessen</span><br>→ <b>Vergangenheit</b>: meist ein Erlebnis mit Otto</div>
<div class='sz'><span class='sig'>ich finde · ehrlich gesagt · toll · süß</span><br>→ <b>Meinung</b></div></div>
{denk("Diese Fragen stelle ich mir bei <b>jedem</b> Satz. Die Signalwörter helfen mir beim Entscheiden.", 6)}
</div></div>"""))

    # 4 Prüfen (Werkbank)
    F.append(slide(f"""{KICK}<h1><span class='n'>3</span>Ich prüfe das Interview</h1>
<div class='werk'>{interview_html()}
<div class='rechts'><div class='denk live' id='denk-pruef'></div>
<div class='bin sach'><div class='binkopf'>✓ Sachangabe <span class='cnt' data-c='sach'>0</span></div><div class='chips' data-bin='sach'></div></div>
<div class='binreihe'>
<div class='bin otto'><div class='binkopf'>nur Otto <span class='cnt' data-c='otto'>0</span></div><div class='chips' data-bin='otto'></div></div>
<div class='bin mein'><div class='binkopf'>Meinung <span class='cnt' data-c='mein'>0</span></div><div class='chips' data-bin='mein'></div>
<div class='binkopf v'>✂ Vergleich <span class='cnt' data-c='vgl'>0</span></div><div class='chips' data-bin='vgl'></div></div>
</div></div></div>""", "engine", "data-engine='pruefen'"))

    # 5 Ordnen
    stapel = "".join(f"<span class='chip sach' data-c='{s}'>{html.escape(SEGS[s]['kurz'])}</span>"
                     for _, ids, _ in [(0, sum([x[0] for x in PRUEFEN], []), 0)] for s in ids if SEGS[s]['k'] == 'sach')
    spalten = "".join(f"<div class='plan' data-sp='{k}'><div class='plankopf'>{t}"
                      + (" <span class='zaehl'>0 Merkmale</span>" if k == 'aus' else "") +
                      "</div><div class='planchips'></div></div>" for k, t, _ in SPALTEN)
    F.append(slide(f"""{KICK}<h1><span class='n'>4</span>Ich ordne nach Themen</h1>
<div class='ordnen'><div class='oben'><div class='stapel'><div class='binkopf'>✓ Meine Sachangaben</div><div class='chips'>{stapel}</div></div>
<div class='denk live' id='denk-ordnen'></div></div>
<div class='spalten'>{spalten}</div></div>""", "engine", "data-engine='ordnen'"))

    # 6 Präsens
    reihen = [
        ("Fischotter <u>gehören</u> zu den Mardern.", "Der Fischotter <u>gehört</u> zu den Mardern.", "gehören → gehört"),
        ("In der Natur <u>fressen</u> Fischotter hauptsächlich Fische.", "Er <u>frisst</u> vor allem Fische.", "fressen → frisst"),
        ("Sie <u>brauchen</u> Ufer, an denen sie sich verstecken können.", "Dort <u>braucht</u> er Ufer mit Verstecken.", "brauchen → braucht"),
        ("Letzte Woche <u>haben</u> wir ihn <u>gemessen</u>.", None, "Vergangenheit: Erlebnis mit Otto"),
        ("Gestern <u>hat</u> Otto einen Krebs <u>geknackt</u>.", None, "Vergangenheit: Erlebnis mit Otto"),
    ]
    rh = "".join(
        f"<div class='pr' data-k='{i+1}'><div class='pi'>{a}</div><div class='pp'>{'→' if b else '✗'}</div>"
        + (f"<div class='pl'>{b}<span class='pn'>{n}</span></div></div>" if b else f"<div class='pl raus'>{n}<br><b>Kommt nicht ins Lexikon.</b></div></div>")
        for i, (a, b, n) in enumerate(reihen))
    F.append(slide(f"""{KICK}<h1><span class='n'>5</span>Ich schreibe im Präsens</h1>
<div class='zwei pr-l'><div class='spalte breit'>
<div class='prkopf'><span>Im Interview</span><span></span><span>In meinem Lexikontext</span></div>{rh}</div>
<div class='spalte schmal'>
{denk("Ein Lexikon sagt, was <b>immer</b> gilt. Darum schreibe ich im <b>Präsens</b>, in der Gegenwart.", 0)}
{denk("Ich frage nach dem <b>Wer-Paket</b>: Wer frisst? <b>Der Fischotter</b> – also: er <b>frisst</b>.", 2)}
{denk("Steht ein Satz in der <b>Vergangenheit</b>? Dann erzählt Frau Berger meist von Otto. Der Satz fällt weg.", 4)}
</div></div>"""))

    # 7 Text
    F.append(slide(f"""{KICK}<h1><span class='n'>6</span>Mein Lexikontext entsteht</h1>
<div class='werk textbau'>{interview_html()}
<div class='rechts'>{artikel_html()}<div class='denk live' id='denk-text'></div></div></div>""", "engine", "data-engine='text'"))

    # 8 Rückblick
    F.append(slide(f"""{KICK}<h1><span class='n'>7</span>Fertig! Was ist passiert?</h1>
<div class='zwei rb'><div class='spalte schmal'>
<div class='rbz sach'><b>14</b> Sachangaben<br><span>davon 11 im Text – vier Merkmale zum Aussehen</span></div>
<div class='rbz otto'><b>8</b> Sätze nur über Otto<br><span>weggelassen</span></div>
<div class='rbz mein'><b>2</b> Meinungen · <b>2</b> Vergleiche<br><span>weggelassen</span></div>
{denk("Ich habe viel weggelassen. Trotzdem kann man sich den Fischotter genau vorstellen.", 3)}
</div><div class='spalte breit'>{artikel_html(gross=True)}
<div class='legende2'><span class='lg1' data-k='1'><i></i> Wörter aus dem Interview</span>
<span class='lg2' data-k='1'><i></i> meine eigenen Wörter</span><span class='lg3' data-k='2'><i></i> Verben im Präsens</span></div>
</div></div>""", "rueck"))

    # 9 Merksatz
    F.append(slide(f"""{KICK}<h1><span class='n'>8</span>So mache ich es</h1>
<div class='zwei'><div class='spalte'>
<div class='schritt' data-k='1'><span class='nr'>1</span><div>Frage bei jeder Angabe: <b>Gilt das für alle Tiere der Art?</b></div></div>
<div class='schritt' data-k='2'><span class='nr'>2</span><div>Ja: <b>markieren</b>. Nur das Zootier oder eine Meinung: <b>streichen</b>.</div></div>
<div class='schritt' data-k='3'><span class='nr'>3</span><div>Vergleich? Nimm nur die <b>Sachangabe</b> heraus.</div></div>
<div class='schritt' data-k='4'><span class='nr'>4</span><div>Ordne unter Überschriften. Schreibe im <b>Präsens</b> über die Tierart: <i>Der Fischotter …</i></div></div>
</div><div class='spalte'>
<div class='blk karte' data-k='5'><span class='lab'>Strategiekarte 9</span>Aus dem Interview wird ein Sachtext</div>
<div class='blk jetzt' data-k='6'><span class='lab'>Jetzt du</span><b>Blatt 7:</b> Wähle das Erdmännchen oder den Roten Panda. Prüfe das Interview so wie ich.</div>
{denk("Bei deinem Tier denkst du genauso – nur leise im Kopf.", 6)}
</div></div>"""))

    # 10 Mein Plan
    tage = [("Di", "24.11.", "Einzelstunde", "Plan machen", ""),
            ("Mi", "25.11.", "Doppelstunde", "Input: Was wird verlangt?", ""),
            ("Fr", "27.11.", "Studientag nach der 4. Stunde", "Lernzeit zu Hause", "haus"),
            ("Di", "01.12.", "Doppelstunde", "früher Termin oder Lernzeit", "termin"),
            ("Mi", "02.12.", "Sprechtag", "kein Unterricht – zu Hause lernen", "haus"),
            ("Fr", "04.12.", "Doppelstunde Sprache", "Vorbereitung", ""),
            ("Di", "08.12.", "letzte Möglichkeit", "später Termin oder Arbeit an Projekten", "termin")]
    karten = "".join(f"<div class='tag {c}'><div class='wt'>{w}</div><div class='dt'>{d}</div>"
                     f"<div class='art'>{a}</div><div class='was'>{x}</div></div>" for w, d, a, x, c in tage)
    KP = "<div class='top'><span class='ph pl'>Planung</span><span class='kick'>Zootiere · Lernerfolgskontrolle</span></div>"
    F.append(slide(f"""{KP}<h1>Heute: Ich plane meinen Weg</h1>
<div class='zwei'><div class='spalte'>
<div class='blk intro' data-k='1'><span class='lab'>Darum geht es</span>Bis zur <b>Lernerfolgskontrolle</b> bleiben noch einige Stunden.
Heute planst du, <b>was du wann schaffen willst</b>.</div>
<div class='blk brauch' data-k='2'><span class='lab'>Du brauchst</span>
<ul><li>den <b>Planungszettel</b></li><li>deine <b>Mappe</b> mit dem rosa Zettel (Lernweg)</li></ul></div>
<div class='blk morgen' data-k='3'><span class='lab'>Morgen</span>Im Input klären wir gemeinsam: <b>Was wird in der Lernerfolgskontrolle verlangt?</b></div>
</div><div class='spalte'>
{denk("Ich schaue zuerst nach: Was habe ich schon geschafft? Was fehlt mir noch?", 1)}
{denk("Dann wähle ich meinen Termin und verteile die offenen Aufgaben auf die Stunden bis dahin.", 2)}
</div></div>"""))
    F.append(slide(f"""{KP}<h1>Mein Plan bis zur Lernerfolgskontrolle</h1>
<div class='leiste'>{karten}</div>
<div class='zwei plan2'><div class='spalte'>
<div class='blk soplan' data-k='1'><span class='lab'>So planst du · Planungszettel</span>
<ol><li>Wähle deinen Termin: früh oder spät.</li>
<li>Kreuze an, was du schon geschafft hast – auch die Übungen im Stil der Lernerfolgskontrolle.</li>
<li>Plane <b>rückwärts</b>: Vor deinem Termin sind alle Etappen, die Probearbeit und das Feedback fertig.</li>
<li>Trage für jede Stunde ein, was du schaffen willst.</li></ol><div class='danach'><b>Nach deiner Lernerfolgskontrolle</b> kannst du an eigenen Tierbeschreibungen arbeiten.</div></div>
</div><div class='spalte schmal'>
<div class='blk zuhause' data-k='2'><div><span class='lab'>Zu Hause lernen</span>Am <b>Fr 27.11.</b> und am <b>Mi 02.12.</b> kannst du dich zu Hause gut vorbereiten: mit deinen Unterlagen und der <b>TaskCards-Pinnwand</b>.</div>
<div class='qr'>{qr_svg()}</div></div>
{denk("Der frühe Termin ist am 1.12. Den wähle ich nur, wenn ich bis dahin die Probearbeit geschrieben und Feedback bekommen habe.", 3)}
</div></div>"""))
    return F

# --------------------------------------------------------------------------
CSS = r"""
:root{--slate-dark:#2C3D4C;--slate-base:#3E5668;--slate-mid:#6A8599;--slate-pale:#D0DCE6;--slate-ghost:#EEF3F7;--rust-dark:#9E4E22;--rust-base:#D97A4A;--rust-mid:#EBA882;--rust-pale:#F5DDD1;--rust-ghost:#FBF0EB;--sage-dark:#4D8B3F;--sage-base:#7DBB6F;--sage-mid:#A8D49D;--sage-pale:#DDF0D8;--sage-ghost:#F0FAF0;--text:#1E2A35;--mid:#5A6A78;--grau:#8D99A4;--grau-pale:#E6E8EA;--bg:#F5F4F1}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;background:var(--slate-dark);font-family:'Andika',sans-serif;color:var(--text);overflow:hidden}
#stage{position:absolute;left:50%;top:50%;width:1600px;height:900px;transform-origin:center;background:var(--bg);overflow:hidden}
.slide{position:absolute;inset:0;padding:40px 70px 78px;display:none;flex-direction:column}
.slide.on{display:flex}
.top{display:flex;align-items:center;gap:18px;min-height:36px}
.ph{font-size:19px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:#fff;padding:5px 15px;border-radius:20px;background:var(--rust-base)}
.kick{font-size:21px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--slate-mid)}
h1{font-size:50px;line-height:1.08;margin:10px 0 20px;color:var(--slate-dark)}
h1 .n{display:inline-flex;width:62px;height:62px;border-radius:50%;background:var(--rust-base);color:#fff;font-size:36px;align-items:center;justify-content:center;margin-right:20px;vertical-align:5px}
h1.gross{font-size:92px;margin:30px 0 34px}
.slide [data-k]:not(.an){opacity:0;transform:translateY(8px)}
.slide [data-k]{transition:opacity .35s,transform .35s}
.denk{font-size:26px;line-height:1.38;background:#fff;border:3px solid var(--rust-mid);border-radius:26px 26px 26px 6px;padding:14px 22px;box-shadow:0 4px 0 var(--rust-pale)}
.denk b{color:var(--rust-dark)}
.denk.live{min-height:140px;flex:none;transition:opacity .25s}
.werk .denk.live{font-size:24px}
.denk.live.leer{opacity:0}
.blk{font-size:30px;line-height:1.4}
.lab{display:block;font-size:19px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:var(--slate-base);margin-bottom:4px}
.zwei{flex:1;display:flex;gap:50px;min-height:0}
.spalte{flex:1;display:flex;flex-direction:column;gap:22px}
.spalte.breit{flex:1.45}.spalte.schmal{flex:.85}
/* Titel */
.titelbox{flex:1;display:flex;gap:50px;align-items:center}
.tlinks{flex:1}
.ziel{font-size:36px;line-height:1.35;border-left:12px solid var(--rust-base);padding:10px 0 10px 28px}
.weg{display:flex;gap:10px;align-items:center;margin-top:48px;font-size:23px}
.weg span{border:3px solid var(--slate-base);background:var(--slate-ghost);border-radius:14px;padding:8px 13px;white-space:nowrap}
.weg span.z{border-color:var(--sage-dark);background:var(--sage-ghost);font-weight:700}
.weg i{font-style:normal;font-size:26px;color:var(--rust-base)}
.tfoto{flex:0 0 560px}.tfoto img{width:560px;border-radius:22px;display:block}
.tfoto figcaption{font-size:16px;color:var(--mid);margin-top:8px}
/* Auftrag */
.blk.auftrag{border:3px solid var(--slate-base);background:var(--slate-ghost);border-radius:18px;padding:20px 26px}
.blk.vergleich{display:flex;flex-direction:column;gap:16px}
.blk.vergleich>div{border-left:10px solid var(--slate-mid);padding:6px 0 6px 20px}
.blk.vergleich>div:last-child{border-color:var(--sage-dark)}
/* Prüffragen */
.pf{display:flex;gap:20px;align-items:flex-start;font-size:29px;line-height:1.35;border-radius:18px;padding:16px 22px;border:3px solid}
.pf .nr{flex:0 0 52px;height:52px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:28px;color:#fff}
.pf.sach{border-color:var(--sage-dark);background:var(--sage-ghost)}.pf.sach .nr{background:var(--sage-dark)}
.pf.otto{border-color:var(--grau);background:var(--grau-pale)}.pf.otto .nr{background:var(--grau)}
.pf.mein{border-color:var(--rust-base);background:var(--rust-ghost)}.pf.mein .nr{background:var(--rust-base)}
.pf.vgl{border-style:dashed;border-color:var(--rust-mid);background:#fff}.pf.vgl .nr{background:var(--rust-mid)}
.sz{margin-bottom:12px}
.blk.signal{font-size:26px;line-height:1.55;border:3px solid var(--slate-pale);background:#fff;border-radius:18px;padding:16px 22px}
.sig{background:var(--slate-ghost);border:2px solid var(--slate-pale);border-radius:10px;padding:1px 10px;font-weight:700;color:var(--slate-dark)}
/* Interview */
.werk{flex:1;display:flex;gap:34px;min-height:0}
.iv{flex:0 0 760px;position:relative;overflow:hidden;background:#fff;border:3px solid var(--slate-pale);border-radius:20px}
.ivin{position:relative;padding:18px 28px 300px}
.ivkopf{font-size:19px;color:var(--slate-base);border-bottom:2px solid var(--slate-pale);padding-bottom:10px;margin-bottom:12px}
.ivkopf span{color:var(--mid);font-size:16px}
.paar{margin-bottom:14px}
.q{font-size:23px;font-weight:700;color:var(--slate-dark);line-height:1.4}
.a{font-size:23px;line-height:1.55}
.seg{border-radius:6px;transition:background .4s,color .4s,opacity .4s;padding:1px 0;-webkit-box-decoration-break:clone;box-decoration-break:clone}
.seg.blick{background:#FFF1B8;box-shadow:0 0 0 3px #FFF1B8}
.seg.sach{background:var(--sage-pale);box-shadow:0 0 0 2px var(--sage-pale)}
.seg.otto{color:var(--grau);text-decoration:line-through;text-decoration-color:var(--grau)}
.seg.mein{color:var(--rust-dark);background:var(--rust-ghost);text-decoration:line-through}
.seg.vgl{color:var(--rust-dark);text-decoration:line-through;outline:2px dashed var(--rust-mid);outline-offset:2px}
.iv.fokus .a,.iv.fokus .q{color:#AEB7BF}
.iv.fokus .seg.sach{color:var(--text)}
.iv.fokus .seg.otto,.iv.fokus .seg.mein,.iv.fokus .seg.vgl{opacity:.55}
.w{border-radius:5px;transition:background .3s,color .3s}
.w.quelle{background:var(--sage-base);color:#fff;box-shadow:0 0 0 3px var(--sage-base)}
.w.genutzt{color:var(--sage-dark)!important;font-weight:700;text-decoration:underline 3px var(--sage-base);text-underline-offset:4px}
.rechts{flex:1;display:flex;flex-direction:column;gap:14px;min-height:0;overflow:hidden}
/* Ablagen */
.bin{border:3px solid;border-radius:18px;background:#fff;padding:10px 14px;display:flex;flex-direction:column}
.bin.sach{border-color:var(--sage-dark);flex:1;min-height:0}
.binreihe{display:flex;gap:16px;height:205px;flex:none}
.bin.otto{border-color:var(--grau);flex:1.2}
.bin.mein{border-color:var(--rust-base);flex:1}
.binkopf{font-size:19px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--slate-dark);display:flex;justify-content:space-between;margin-bottom:6px}
.bin.sach .binkopf{color:var(--sage-dark)}.bin.otto .binkopf{color:var(--mid)}.bin.mein .binkopf{color:var(--rust-dark)}
.binkopf.v{margin-top:6px;border-top:2px dashed var(--rust-mid);padding-top:6px}
.cnt{display:inline-flex;min-width:34px;height:30px;border-radius:15px;background:var(--slate-ghost);align-items:center;justify-content:center;font-size:19px}
.chips{display:flex;flex-wrap:wrap;gap:6px;align-content:flex-start}
.chip{font-size:17px;line-height:1.2;padding:4px 10px;border-radius:10px;border:2px solid;white-space:nowrap;background:#fff}
.chip.sach{border-color:var(--sage-dark);background:var(--sage-ghost)}
.chip.otto{border-color:var(--grau);color:var(--mid);background:var(--grau-pale)}
.chip.mein{border-color:var(--rust-base);color:var(--rust-dark);background:var(--rust-ghost)}
.chip.vgl{border-color:var(--rust-mid);border-style:dashed;color:var(--rust-dark)}
.chip.wart{visibility:hidden}
/* Ordnen */
.ordnen{flex:1;display:flex;flex-direction:column;gap:18px;min-height:0}
.oben{display:flex;gap:24px;height:178px;flex:none}
.stapel{flex:1.3;border:3px solid var(--sage-dark);border-radius:18px;background:#fff;padding:10px 14px}
.stapel .binkopf{color:var(--sage-dark)}
.stapel .chip{font-size:20px}
.stapel .chip.weg{visibility:hidden}
.oben .denk{flex:1;min-height:0;font-size:24px}
.spalten{flex:1;display:flex;gap:16px;min-height:0}
.plan{flex:1;border:3px solid var(--slate-base);border-radius:18px;background:#fff;padding:10px 12px}
.plan[data-sp='aus']{flex:1.5}
.plankopf{font-size:24px;font-weight:700;color:#fff;background:var(--slate-base);margin:-10px -12px 10px;padding:8px 14px;border-radius:14px 14px 0 0;display:flex;justify-content:space-between;align-items:center}
.zaehl{font-size:18px;background:#fff;color:var(--slate-dark);border-radius:12px;padding:2px 10px}
.zaehl.ok{background:var(--sage-pale);color:var(--sage-dark)}
.planchips{display:flex;flex-direction:column;gap:6px}
.planchips .chip{font-size:20px;white-space:normal;padding:3px 10px}
.planchips .chip.wahl{border-width:4px;font-weight:700;box-shadow:0 3px 0 var(--sage-mid)}
.planchips.waehlen .chip:not(.wahl){opacity:.45}
/* Präsens */
.prkopf{display:grid;grid-template-columns:1fr 50px 1fr;font-size:19px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--slate-base)}
.pr{display:grid;grid-template-columns:1fr 50px 1fr;align-items:center;font-size:25px;line-height:1.35}
.pi{background:#fff;border:2px solid var(--slate-pale);border-radius:14px;padding:10px 16px}
.pp{text-align:center;font-size:32px;color:var(--rust-base);font-weight:700}
.pl{background:var(--sage-ghost);border:2px solid var(--sage-dark);border-radius:14px;padding:10px 16px;position:relative}
.pl.raus{background:var(--grau-pale);border-color:var(--grau);color:var(--mid)}
.pr u{text-decoration:none;font-weight:700;color:var(--rust-dark);background:var(--rust-ghost);border-radius:6px;padding:0 4px}
.pl u{color:var(--sage-dark);background:var(--sage-pale)}
.pn{position:absolute;right:10px;top:-14px;font-size:16px;background:#fff;border:2px solid currentColor;border-radius:10px;padding:0 8px;color:var(--slate-base)}
.pl.raus .pn{color:var(--grau)}
.pr-l .spalte.breit{gap:16px}
/* Lexikon */
.lex{flex:1;background:#fff;border:3px solid var(--slate-base);border-radius:20px;padding:16px 28px;box-shadow:0 6px 0 var(--slate-pale);min-height:0}
.lexkopf{font-size:17px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--slate-mid);border-bottom:2px solid var(--slate-pale);padding-bottom:6px;margin-bottom:10px}
.lex h2{font-size:34px;color:var(--slate-dark);margin-bottom:8px;min-height:44px}
.lex p{font-size:24px;line-height:1.55;margin-bottom:12px}
.lex .satz .g,.lex .satz .t{opacity:0;transition:opacity .35s}
.lex .satz .an{opacity:1}
.lex .t.neu{background:var(--sage-pale);border-radius:5px}
.lex .t.form{background:var(--rust-pale);border-radius:5px}
.lex.gross{flex:none}
.lex.gross h2{font-size:42px}
.lex.gross p{font-size:30px}
.lex.gross .g,.lex.gross .t{opacity:1}
.rueck.f1 .lex .t{color:var(--sage-dark);font-weight:700}
.rueck.f2 .lex .verb{background:var(--rust-pale);color:var(--rust-dark);border-radius:6px;padding:0 3px}
.legende2{display:flex;gap:26px;font-size:21px;margin-top:16px}
.legende2 i{display:inline-block;width:22px;height:22px;border-radius:6px;vertical-align:-3px;margin-right:4px}
.lg1 i{background:var(--sage-dark)}.lg2 i{background:var(--text)}.lg3 i{background:var(--rust-pale);border:2px solid var(--rust-dark)}
.textbau .iv{flex-basis:700px}
.textbau .denk.live{min-height:128px;font-size:24px}
/* Rückblick */
.rbz{font-size:27px;line-height:1.3;border:3px solid;border-radius:18px;padding:14px 22px}
.rbz b{font-size:40px}
.rbz span{font-size:20px;color:var(--mid)}
.rbz.sach{border-color:var(--sage-dark);background:var(--sage-ghost)}
.rbz.otto{border-color:var(--grau);background:var(--grau-pale)}
.rbz.mein{border-color:var(--rust-base);background:var(--rust-ghost)}
/* Merksatz */
.schritt{display:flex;gap:18px;align-items:flex-start;font-size:30px;line-height:1.35}
.schritt .nr{flex:0 0 54px;height:54px;border-radius:50%;background:var(--slate-base);color:#fff;font-weight:700;display:flex;align-items:center;justify-content:center}
.blk.karte{border:3px solid var(--slate-base);border-radius:16px;padding:16px 22px;background:var(--slate-ghost);font-weight:700}
.blk.jetzt{border:3px solid var(--rust-base);border-radius:16px;padding:16px 22px;background:var(--rust-ghost)}
.blk.jetzt .lab{color:var(--rust-dark)}
.ph.pl{background:var(--sage-dark)}
.blk.intro{border:3px solid var(--slate-base);border-radius:16px;padding:16px 22px;background:var(--slate-ghost)}
.blk.brauch{border:3px solid var(--slate-pale);border-radius:16px;padding:14px 22px;background:#fff}
.blk.brauch ul{padding-left:30px}
.blk.morgen{border:3px solid var(--rust-base);border-radius:16px;padding:14px 22px;background:var(--rust-ghost)}
.blk.morgen .lab{color:var(--rust-dark)}
.leiste{display:flex;gap:12px;margin-bottom:14px}
.tag{flex:1;border:3px solid var(--slate-base);border-radius:16px;background:#fff;padding:10px 12px;text-align:center}
.tag .wt{font-size:20px;font-weight:700;color:var(--slate-mid);text-transform:uppercase;letter-spacing:.06em}
.tag .dt{font-size:34px;font-weight:700;color:var(--slate-dark);line-height:1.1}
.tag .art{font-size:18px;color:var(--mid);min-height:46px;line-height:1.25;margin-top:4px}
.tag .was{font-size:18px;font-weight:700;border-radius:10px;padding:4px 6px;margin-top:4px;background:var(--slate-ghost);color:var(--slate-dark)}
.tag.termin{border-color:var(--sage-dark);background:var(--sage-ghost)}
.tag.termin .was{background:var(--sage-dark);color:#fff}
.tag.haus{border-style:dashed;border-color:var(--grau);background:var(--grau-pale)}
.tag.haus .was{background:#fff;color:var(--mid)}
.plan2{gap:34px}
.plan2 .denk{font-size:23px;padding:10px 20px}
.plan2 .spalte{gap:16px}
.blk.soplan{border:3px solid var(--slate-base);border-radius:16px;padding:12px 22px;background:#fff;font-size:26px}
.blk.soplan ol{padding-left:30px}
.blk.soplan .danach{font-size:22px;margin-top:6px;color:var(--sage-dark)}
.blk.zuhause{display:flex;gap:18px;align-items:center;border:3px dashed var(--grau);border-radius:16px;padding:14px 18px;background:var(--grau-pale);font-size:24px;line-height:1.35}
.qr{flex:0 0 190px;background:#fff;border-radius:10px;padding:6px}
.qr svg{width:178px;height:178px;display:block}
.blk.termine{margin-top:auto;border:3px solid var(--sage-dark);border-radius:16px;padding:14px 22px;background:var(--sage-ghost)}
.blk.termine .lab{color:var(--sage-dark)}
.tage{display:flex;gap:14px;margin:6px 0 8px}
.tage span{flex:1;text-align:center;background:#fff;border:2px solid var(--sage-dark);border-radius:12px;padding:6px 0;font-size:30px}
.klein2{font-size:22px;color:var(--mid)}
/* Flug */
#flug{position:absolute;inset:0;pointer-events:none;z-index:20}
.fl{position:absolute;left:0;top:0;white-space:nowrap;will-change:transform}
.fl.wort{font-size:24px;font-weight:700;color:#fff;background:var(--sage-dark);border-radius:8px;padding:0 6px;box-shadow:0 6px 16px rgba(30,42,53,.3)}
.fl.chip{box-shadow:0 6px 16px rgba(30,42,53,.25)}
/* Leiste */
#bar{position:absolute;left:70px;right:250px;bottom:28px;display:flex;gap:8px;align-items:center}
#bar .dot{flex:1;height:8px;border-radius:4px;background:var(--slate-pale)}
#bar .dot.on{background:var(--rust-base)}
#bar .num{font-size:19px;color:var(--mid);margin-left:14px;min-width:70px;text-align:right}
#nav{position:fixed;right:12px;bottom:12px;display:flex;gap:10px;z-index:5;opacity:.35}
#nav:hover{opacity:1}
#nav button{width:52px;height:52px;border-radius:50%;border:2px solid var(--slate-pale);background:rgba(24,35,45,.85);color:#fff;font-size:22px;font-family:inherit;cursor:pointer}
@media print{#nav{display:none}}
"""

JS = r"""
const D=__DATEN__;
const stage=document.getElementById('stage'),flug=document.getElementById('flug');
const slides=[...document.querySelectorAll('.slide')];let i=0,k=0,gen=0,scale=1;
const bar=document.getElementById('bar');
slides.forEach(()=>{const d=document.createElement('div');d.className='dot';bar.appendChild(d)});
const num=document.createElement('div');num.className='num';bar.appendChild(num);
const wait=ms=>new Promise(r=>setTimeout(r,ms));
function fit(){scale=Math.min(innerWidth/1600,innerHeight/900);stage.style.transform='translate(-50%,-50%) scale('+scale+')'}
function rect(el){const r=el.getBoundingClientRect(),s=stage.getBoundingClientRect();
 return{x:(r.left-s.left)/scale,y:(r.top-s.top)/scale,w:r.width/scale,h:r.height/scale}}
// Flug von a nach b
function fly(a,b,html,cls,dauer=950){const g=gen;
 const ra=rect(a),rb=rect(b);const f=document.createElement('div');f.className='fl '+cls;f.innerHTML=html;flug.appendChild(f);
 const fw=f.offsetWidth,fh=f.offsetHeight;
 const x0=ra.x+ra.w/2-fw/2,y0=ra.y+ra.h/2-fh/2,x1=rb.x+rb.w/2-fw/2,y1=rb.y+rb.h/2-fh/2;
 const mx=(x0+x1)/2,my=Math.min(y0,y1)-90;
 const an=f.animate([{transform:`translate(${x0}px,${y0}px) scale(1)`},{transform:`translate(${mx}px,${my}px) scale(1.2)`,offset:.45},
  {transform:`translate(${x1}px,${y1}px) scale(1)`}],{duration:dauer,easing:'cubic-bezier(.45,.05,.35,1)',fill:'forwards'});
 return an.finished.then(()=>{f.remove();return g===gen})}
// Interview-Fenster weich scrollen
function scrollIv(iv,el,sofort){const ziel=Math.max(0,el.offsetTop-iv.clientHeight*.28);
 const ivin=iv.querySelector('.ivin');
 if(sofort){iv.scrollTop=ziel;return Promise.resolve()}
 const st=iv.scrollTop,t0=performance.now();
 return new Promise(r=>{function f(t){const p=Math.min(1,(t-t0)/450);iv.scrollTop=st+(ziel-st)*(1-Math.pow(1-p,3));p<1?requestAnimationFrame(f):r()}requestAnimationFrame(f)})}
function setDenk(el,html){el.innerHTML=html?'<b>💭 Ich denke:</b> '+html:'';el.classList.toggle('leer',!html)}

// ---------------- Engine: Prüfen ----------------
const E={};
E.pruefen={max:D.pruefen.length,
 reset(s){s.querySelectorAll('.seg').forEach(e=>e.className='seg');s.querySelectorAll('.chips').forEach(c=>c.innerHTML='');
  s.querySelectorAll('.cnt').forEach(c=>c.textContent='0');s.querySelector('.iv').scrollTop=0;setDenk(s.querySelector('#denk-pruef'),'')},
 chip(s,id){const sg=D.segs[id];const c=document.createElement('span');c.className='chip '+sg.k;c.textContent=sg.kurz;
  s.querySelector(`.chips[data-bin='${sg.k}']`).appendChild(c);const n=s.querySelector(`.cnt[data-c='${sg.k}']`);n.textContent=+n.textContent+1;return c},
 statisch(s,j){D.pruefen[j-1][0].forEach(id=>{s.querySelector(`.seg[data-s='${id}']`).classList.add(D.segs[id].k);this.chip(s,id)})},
 async anim(s,j){const g=gen;const [ids,txt]=D.pruefen[j-1];const iv=s.querySelector('.iv');
  setDenk(s.querySelector('#denk-pruef'),txt);
  if(!ids.length){iv.classList.add('fokus');return}
  await scrollIv(iv,s.querySelector(`.seg[data-s='${ids[0]}']`).closest('.paar'));
  for(const id of ids){if(g!==gen)return;const seg=s.querySelector(`.seg[data-s='${id}']`);seg.classList.add('blick');
   await wait(650);if(g!==gen)return;seg.classList.remove('blick');seg.classList.add(D.segs[id].k);
   const c=this.chip(s,id);c.classList.add('wart');
   const ok=await fly(seg,c,c.textContent,'chip '+D.segs[id].k,800);if(!ok)return;c.classList.remove('wart')}},
 apply(s,j,an){this.reset(s);for(let x=1;x<j;x++)this.statisch(s,x);
  if(j===0)return;if(an)return this.anim(s,j);
  this.statisch(s,j);setDenk(s.querySelector('#denk-pruef'),D.pruefen[j-1][1]);
  const ids=D.pruefen[j-1][0];const iv=s.querySelector('.iv');
  if(ids.length)scrollIv(iv,s.querySelector(`.seg[data-s='${ids[0]}']`).closest('.paar'),true);else iv.classList.add('fokus')}};
E.pruefen.reset=(r=>function(s){r.call(this,s);s.querySelector('.iv').classList.remove('fokus')})(E.pruefen.reset);

// ---------------- Engine: Ordnen ----------------
E.ordnen={max:D.spalten.length+1,
 reset(s){s.querySelectorAll('.stapel .chip').forEach(c=>c.classList.remove('weg'));s.querySelectorAll('.planchips').forEach(p=>{p.innerHTML='';p.classList.remove('waehlen')});
  const z=s.querySelector('.zaehl');z.textContent='0 Merkmale';z.classList.remove('ok');setDenk(s.querySelector('#denk-ordnen'),'')},
 neu(s,sp,id){const c=document.createElement('span');c.className='chip sach';c.dataset.c=id;c.textContent=D.segs[id].kurz;
  s.querySelector(`.plan[data-sp='${sp}'] .planchips`).appendChild(c);return c},
 zaehl(s){const n=s.querySelectorAll(".plan[data-sp='aus'] .chip:not(.wart)").length;const z=s.querySelector('.zaehl');
  z.textContent=n+' Merkmal'+(n===1?'':'e');z.classList.toggle('ok',n>=4)},
 wahl(s){const p=s.querySelector(".plan[data-sp='aus'] .planchips");p.classList.add('waehlen');
  D.wahl.forEach(id=>p.querySelector(`.chip[data-c='${id}']`).classList.add('wahl'))},
 statisch(s,j){if(j>D.spalten.length){this.wahl(s);return}const [sp,,ids]=D.spalten[j-1];
  ids.forEach(id=>{s.querySelector(`.stapel .chip[data-c='${id}']`).classList.add('weg');this.neu(s,sp,id)});this.zaehl(s)},
 async anim(s,j){const g=gen;setDenk(s.querySelector('#denk-ordnen'),D.ordnenDenk[j-1]);
  if(j>D.spalten.length){this.wahl(s);return}const [sp,,ids]=D.spalten[j-1];
  for(const id of ids){if(g!==gen)return;const q=s.querySelector(`.stapel .chip[data-c='${id}']`);const c=this.neu(s,sp,id);c.classList.add('wart');
   const p=fly(q,c,c.textContent,'chip sach',750);q.classList.add('weg');
   p.then(ok=>{if(ok){c.classList.remove('wart');this.zaehl(s)}});await wait(330)}},
 apply(s,j,an){this.reset(s);for(let x=1;x<j;x++)this.statisch(s,x);if(j===0)return;if(an)return this.anim(s,j);
  this.statisch(s,j);setDenk(s.querySelector('#denk-ordnen'),D.ordnenDenk[j-1])}};

// ---------------- Engine: Text ----------------
E.text={max:D.text.length,
 reset(s){s.querySelectorAll('.seg').forEach(e=>{e.className='seg '+D.segs[e.dataset.s].k});s.querySelector('.iv').classList.add('fokus');
  s.querySelectorAll('.w').forEach(w=>w.classList.remove('quelle','genutzt'));
  s.querySelectorAll('.lex .g,.lex .t').forEach(t=>t.classList.remove('an','neu','form'));s.querySelector('.iv').scrollTop=0;setDenk(s.querySelector('#denk-text'),'')},
 statisch(s,j){const satz=s.querySelector(`.lex .satz[data-n='${j-1}']`);
  satz.querySelectorAll('.g,.t').forEach(t=>{t.classList.add('an');if(t.classList.contains('t'))s.querySelector(`.iv .w[data-w='${t.dataset.src}']`).classList.add('genutzt')})},
 async anim(s,j){const g=gen;const satz=s.querySelector(`.lex .satz[data-n='${j-1}']`);const iv=s.querySelector('.iv');
  setDenk(s.querySelector('#denk-text'),D.text[j-1]);
  s.querySelectorAll('.lex .t.neu,.lex .t.form').forEach(t=>t.classList.remove('neu','form'));
  const toks=[...satz.querySelectorAll('.t')];
  if(toks.length)await scrollIv(iv,s.querySelector(`.iv .w[data-w='${toks[0].dataset.src}']`).closest('.paar'));
  if(g!==gen)return;
  toks.forEach(t=>s.querySelector(`.iv .w[data-w='${t.dataset.src}']`).classList.add('quelle'));
  await wait(700);if(g!==gen)return;
  satz.querySelectorAll('.g').forEach(t=>t.classList.add('an'));
  const flights=toks.map((t,n)=>wait(n*260).then(async()=>{if(g!==gen)return;const w=s.querySelector(`.iv .w[data-w='${t.dataset.src}']`);
   const ok=await fly(w,t,w.textContent,'wort',1000);if(!ok)return;w.classList.remove('quelle');w.classList.add('genutzt');
   t.classList.add('an',w.textContent===t.textContent?'neu':'form')}));
  await Promise.all(flights)},
 apply(s,j,an){this.reset(s);for(let x=1;x<j;x++)this.statisch(s,x);if(j===0)return;if(an)return this.anim(s,j);
  this.statisch(s,j);setDenk(s.querySelector('#denk-text'),D.text[j-1]);
  const t=s.querySelector(`.lex .satz[data-n='${j-1}'] .t`);if(t)scrollIv(s.querySelector('.iv'),s.querySelector(`.iv .w[data-w='${t.dataset.src}']`).closest('.paar'),true)}};

// Rückblick: Verben markieren
document.querySelectorAll('.rueck .lex .t').forEach(t=>{if(D.verben.includes(t.textContent))t.classList.add('verb')});

const maxK=s=>s.dataset.engine?E[s.dataset.engine].max:Math.max(0,...[...s.querySelectorAll('[data-k]')].map(e=>+e.dataset.k));
function zeichne(an){const s=slides[i];gen++;flug.innerHTML='';
 if(s.dataset.engine){E[s.dataset.engine].apply(s,k,an);return}
 s.querySelectorAll('[data-k]').forEach(e=>e.classList.toggle('an',+e.dataset.k<=k));
 if(s.classList.contains('rueck')){s.classList.toggle('f1',k>=1);s.classList.toggle('f2',k>=2)}}
function show(n,ende){i=Math.max(0,Math.min(slides.length-1,n));k=ende?maxK(slides[i]):0;
 slides.forEach((s,j)=>s.classList.toggle('on',j===i));
 [...bar.querySelectorAll('.dot')].forEach((d,j)=>d.classList.toggle('on',j<=i));num.textContent=(i+1)+' / '+slides.length;zeichne(false)}
function next(){if(k<maxK(slides[i])){k++;zeichne(true);return}if(i<slides.length-1)show(i+1)}
function prev(){if(k>0){k--;zeichne(false);return}if(i>0)show(i-1,true)}
function vollbild(){const d=document,el=d.documentElement;
 if(!(d.fullscreenElement||d.webkitFullscreenElement))(el.requestFullscreen||el.webkitRequestFullscreen||function(){}).call(el);
 else(d.exitFullscreen||d.webkitExitFullscreen||function(){}).call(d)}
addEventListener('keydown',e=>{if([' ','ArrowRight','PageDown','Enter'].includes(e.key)){e.preventDefault();next()}
 else if(['ArrowLeft','PageUp','Backspace'].includes(e.key)){e.preventDefault();prev()}
 else if(e.key==='f'||e.key==='F')vollbild();
 else if(e.key==='a'||e.key==='A'){k=maxK(slides[i]);zeichne(false)}});
stage.addEventListener('click',e=>{(e.clientX<innerWidth/4)?prev():next()});
let tx=null;addEventListener('touchstart',e=>{tx=e.touches[0].clientX},{passive:true});
addEventListener('touchend',e=>{if(tx===null)return;const dx=e.changedTouches[0].clientX-tx;tx=null;if(Math.abs(dx)>60){e.preventDefault();dx<0?next():prev()}},{passive:false});
document.getElementById('bz').onclick=prev;document.getElementById('bv').onclick=next;document.getElementById('bf').onclick=vollbild;
addEventListener('resize',fit);fit();
const h=location.hash.match(/^#(\d+)(?:-(\d+))?$/);show(h?+h[1]-1:0);if(h&&h[2]){k=+h[2];zeichne(false)}
"""

def main():
    daten = {
        "segs": {k: {"k": v["k"], "kurz": v["kurz"]} for k, v in SEGS.items()},
        "pruefen": [[ids, t] for ids, t in PRUEFEN],
        "spalten": [[k, t, ids] for k, t, ids in SPALTEN],
        "ordnenDenk": ORDNEN_DENK, "wahl": WAHL,
        "text": [d for _, _, d in TEXT],
        "verben": ["gehört", "ist", "sind", "lebt", "braucht", "frisst"],
    }
    # Kontrolle: alle Quellwörter vorhanden
    alle_w = set(WORT_PAAR)
    for _, toks, _ in TEXT:
        for t in toks:
            if not isinstance(t, str) and t[0]: assert t[0] in alle_w, t
    js = JS.replace("__DATEN__", json.dumps(daten, ensure_ascii=False))
    doc = f"""<!DOCTYPE html><html lang='de'><head><meta charset='utf-8'>
<meta name='viewport' content='width=device-width,initial-scale=1'>
<title>Zootiere · Etappe 3 · Vom Interview zum Tierlexikon – laut gedacht</title>
<style>{font_css()}{CSS}</style></head><body>
<div id='stage'>{''.join(folien())}<div id='flug'></div><div id='bar'></div></div>
<div id='nav'><button id='bz' title='zurück (←)'>‹</button><button id='bv' title='weiter (→ / Leertaste)'>›</button><button id='bf' title='Vollbild (F)'>⛶</button></div>
<script>{js}</script></body></html>"""
    OUT.write_text(doc, encoding="utf-8")
    print("geschrieben:", OUT.relative_to(ROOT), f"{len(doc)//1024} KB")

if __name__ == "__main__":
    main()
