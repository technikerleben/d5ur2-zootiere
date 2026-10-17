"""Baut anleitung.html (Erklär-App für Lehrkräfte, Stil wie Logbuch/Lernbuddy erklärt).
Quellen: Kernpaket-PDF (Seitenbilder), srl5/lernbuddy.html (Schriften, Lernbuddy-Blatt),
Screenshots von Input und Kiosk (shots/), Strategiekarten-PDF aus dem Zootiere-Repo."""
import re, sys, json, base64, io, pathlib
import pymupdf
from PIL import Image
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from steps import CH, STEPS

# Aufruf: python tools/anleitung_erklaer/build.py <Kernpaket.pdf> <srl5/lernbuddy.html> <Screenshot-Ordner> [Ausgabe]
#   Screenshot-Ordner enthält in_0.png, in_3.png (Input Etappe 1, Folie 1 und 4) und k_0.png, k_2.png (Kiosk Start und Tipp Blatt 3)
ROOT = pathlib.Path(__file__).resolve().parents[2]
KP = sys.argv[1]
SK = str(ROOT / "ausgabe/pakete/lehrkraft/Strategiekarten_210x99.pdf")
LB = pathlib.Path(sys.argv[2]).read_text(encoding="utf-8")
SHOTS = pathlib.Path(sys.argv[3])
TPL = (pathlib.Path(__file__).parent / "template.html").read_text(encoding="utf-8")
OUT = pathlib.Path(sys.argv[4]) if len(sys.argv) > 4 else ROOT / "anleitung.html"

W = 1150  # Bildbreite in px

def webp(im, q=52):
    b = io.BytesIO(); im.save(b, "WEBP", quality=q, method=6); return "data:image/webp;base64," + base64.b64encode(b.getvalue()).decode()

def pdf_page(doc, n):
    pg = doc[n - 1]; z = W / pg.rect.width
    pm = pg.get_pixmap(matrix=pymupdf.Matrix(z, z), colorspace=pymupdf.csGRAY)
    return Image.frombytes("L", (pm.width, pm.height), pm.samples)

kp = pymupdf.open(KP); sk = pymupdf.open(SK)
need = sorted({s["v"] for s in STEPS})
IMGS = {}   # key -> (dataurl, ratio h/w)
for v in need:
    if v.startswith("p"):
        im = pdf_page(kp, int(v[1:]))
    elif v == "sk":
        im = pdf_page(sk, 1)
    elif v in ("in0", "in3", "k0", "k2"):
        f = {"in0": "in_0", "in3": "in_3", "k0": "k_0", "k2": "k_2"}[v]
        im = Image.open(SHOTS / f"{f}.png").convert("RGB")
    else:
        continue
    IMGS[v] = (webp(im), im.height / im.width)
# Blatt 3 für die Lernbuddy-Mitte (etwas kleiner)
b3 = pdf_page(kp, 13).resize((760, round(760 * 842 / 595)))
B3 = webp(b3, 55)

# --- Schriften (ohne Arabisch) und Lernbuddy-Blatt aus srl5/lernbuddy.html ---
style = re.search(r"<style>(.*?)</style>", LB, re.S).group(1)
faces = [f for f in re.findall(r"@font-face\s*\{[^}]*\}", style) if "Noto Sans Arabic" not in f]
FONTS = "\n".join(faces)
lbcss = style[style.index("/* ---------- Lernbuddy-Blatt"):]
m = re.search(r'<div class="sheet" data-v="r"[^>]*>(.*?)\n\s*<div class="sheet hide" data-v="l"', LB, re.S)
sheet = m.group(1).strip()
assert sheet.endswith("</div></div>")
sheet = sheet[:-len("</div>")]  # schließendes sheet-div entfernen
# Blatt 3 in die Mitte legen, Hinweistext ersetzen
sheet, n = re.subn(r'(<div class="z-abs z-drop"[^>]*>)', r'\1<img class="z-blatt" src="%s" alt="">' % B3, sheet, count=1)
assert n == 1, "z-drop nicht gefunden"
lbcss += "\n.z-lb .z-drop .z-msg{display:none}\n.z-lb .z-blatt{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);height:94%;box-shadow:0 1mm 4mm rgba(0,0,0,.25);border:.3mm solid #999;background:#fff;z-index:2}"

# --- Blätter (HTML) ---
sheets = []
for v, (src, r) in IMGS.items():
    sheets.append(f'<div class="sheet hide" data-v="{v}" data-r="{r:.5f}" style="height:{1000*r:.2f}px"><img src="{src}" alt=""></div>')
if "lb" in need:
    sheets.append(f'<div class="sheet hide" data-v="lb" data-r="{420/297:.5f}" style="height:{1000*420/297:.2f}px" aria-hidden="true">{sheet}</div>')

html = (TPL.replace("/*FONTS*/", FONTS).replace("/*LBCSS*/", lbcss)
        .replace("<!--SHEETS-->", "\n".join(sheets))
        .replace("/*DATA*/", "const CH=" + json.dumps(CH, ensure_ascii=False) + ";\nconst STEPS=" + json.dumps(STEPS, ensure_ascii=False) + ";"))
OUT.write_text(html, encoding="utf-8")
print(OUT, round(len(html) / 1e6, 2), "MB", len(STEPS), "Schritte", len(IMGS), "Bilder")
