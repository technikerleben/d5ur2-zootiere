#!/usr/bin/env python3
"""Lehrkraft-Leitfaden: Aufbau der Reihe und Druckplan mit Links auf alle Materialien.

Aufruf: python tools/build_anleitung.py [artifact-ausgabe.html]
Ausgabe: anleitung.html (Repo-Wurzel, relative Links)
         optional: Fassung mit absoluten Links (für die Veröffentlichung außerhalb des Repos)
Prüft, dass jede verlinkte Datei existiert.
"""
import html
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_material import font_css  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/technikerleben/d5ur2-zootiere"
BRANCH = "claude/etappe1-muster"
ABS = "https://raw.githack.com/technikerleben/d5ur2-zootiere/%s/" % BRANCH

# Formate: a5 = A4 gesetzt, auf A5 verkleinert · a4 = A4 Originalgröße · lam = laminieren · dig = digital
# Anzahl: kind (Regelkinder) · f (zieldifferent) · alle · drittel · halb · tisch · fix:N · termin
M = {
    "animation": ("Ablauf-Animation", "ausgabe/lernweg/Ablauf_Animation.html", "dig", None, ""),
    "kiosk": ("Kontroll-Kiosk", "apps/kontroll-kiosk/index.html", "dig", None, "auf dem Klassenlaptop speichern"),
    "in1": ("Input Etappe 1", "ausgabe/etappe1/Input_Etappe1.html", "dig", None, "Beamer"),
    "in2": ("Input Etappe 2", "ausgabe/etappe2/Input_Etappe2.html", "dig", None, "Beamer oder Kleingruppe"),
    "in3": ("Input Etappe 3", "ausgabe/etappe3/Input_Etappe3.html", "dig", None, "Beamer oder Kleingruppe"),
    "lernweg": ("Lernweg", "ausgabe/lernweg/Lernweg_Zootiere_A4.pdf", "a4", "kind", "1 Seite"),
    "lernwegF": ("Lernweg F", "ausgabe/lernweg/Lernweg_Zootiere_F_A4.pdf", "a4", "f", "1 Seite"),
    "strategie": ("Strategiekarten", "ausgabe/strategiekarten/Strategiekarten_A4.pdf", "a4 lam", "tisch", "3 Bögen, 9 Karten; schneiden"),
    "schild": ("Haltestellen-Schild", "ausgabe/etappe3/Haltestelle_Schild_A4.pdf", "a4 lam", "fix:1", "1 Seite"),
    "mb1": ("Merkblatt 1", "ausgabe/etappe1/Merkblatt_1_A4.pdf", "a4", "kind", "2 Seiten, doppelseitig"),
    "ub1": ("Übungsblätter Etappe 1", "ausgabe/etappe1/Uebungsblaetter_Etappe1_A4.pdf", "a5", "kind", "5 Seiten: Material Fischotter, Blatt 1–4"),
    "gn1a": ("Gelingensnachweis 1 A", "ausgabe/etappe1/GN1_A_A4.pdf", "a4", "kind", "doppelseitig: Aufgaben vorn, Rückmeldung hinten"),
    "gn1b": ("Gelingensnachweis 1 B", "ausgabe/etappe1/GN1_B_A4.pdf", "a4", "drittel", "für die Wiederholung"),
    "mb2": ("Merkblatt 2", "ausgabe/etappe2/Merkblatt_2_A4.pdf", "a4", "kind", "2 Seiten, doppelseitig"),
    "ub2": ("Übungsblätter Etappe 2", "ausgabe/etappe2/Uebungsblaetter_Etappe2_A4.pdf", "a5", "kind", "2 Seiten: Blatt 5–6"),
    "woerter": ("Wörterhilfe", "ausgabe/etappe2/Woerterhilfe_A4.pdf", "a5 lam", "tisch", "1 Seite; gilt auch für Etappe 3"),
    "gn2a": ("Gelingensnachweis 2 A", "ausgabe/etappe2/GN2_A_A4.pdf", "a4", "kind", "doppelseitig"),
    "gn2b": ("Gelingensnachweis 2 B", "ausgabe/etappe2/GN2_B_A4.pdf", "a4", "drittel", "für die Wiederholung"),
    "mb3": ("Merkblatt 3", "ausgabe/etappe3/Merkblatt_3_A4.pdf", "a4", "kind", "2 Seiten, doppelseitig"),
    "ub3": ("Übungsblätter Etappe 3", "ausgabe/etappe3/Uebungsblaetter_Etappe3_A4.pdf", "a5", "kind",
            "7 Seiten: S. 1 Erdmännchen, S. 2 Roter Panda (je halber Klassensatz), S. 3–5 Blatt 7–9, S. 6–7 Checkliste"),
    "rueck": ("Rückmeldekarte", "ausgabe/etappe3/Rueckmeldekarte_A4.pdf", "a5 lam", "fix:3", "an der Haltestelle auslegen"),
    "probe": ("Probearbeit Waschbär", "ausgabe/etappe3/Probearbeit_Waschbaer_A4.pdf", "a4", "kind",
              "7 Seiten: S. 1–6 für das Kind, S. 7 Rückmeldung der Lehrkraft"),
    "wahl": ("Wahlphase und Projekte P1–P3", "ausgabe/wahlphase/Wahlphase_Projekte_A4.pdf", "a4", "halb",
             "4 Seiten: Übersicht, P1 Tiermagazin, P2 Tierrätsel, P3 Tiervergleich; zum Auslegen"),
    "tp_otter": ("Tierpaket Fischotter", "materialien/tierpakete/fischotter_A5.pdf", "a5", "fix:4", "für die Projekte"),
    "tp_erd": ("Tierpaket Erdmännchen", "materialien/tierpakete/erdmaennchen_A5.pdf", "a5", "fix:4", "für die Projekte"),
    "tp_panda": ("Tierpaket Roter Panda", "materialien/tierpakete/roter-panda_A5.pdf", "a5", "fix:4", "für die Projekte"),
    "ka1": ("Klassenarbeit Biber", "ausgabe/pruefungen/Klassenarbeit_Biber_A4.pdf", "a4", "termin",
            "7 Seiten: S. 1–6 für das Kind, S. 7 Bewertung · Foto vorläufig"),
    "ka2": ("Klassenarbeit Breitmaulnashorn", "ausgabe/pruefungen/Klassenarbeit_Breitmaulnashorn_A4.pdf", "a4", "termin",
            "7 Seiten · Foto fehlt noch (Platzhalter)"),
    "f1": ("Förder-Material Etappe 1F", "ausgabe/foerder/etappe1/Foerder_Etappe1_A4.pdf", "a5", "f", "7 Seiten: Merkkarte, Material, Blatt 1F–4F"),
    "gn1f": ("Gelingensnachweis 1F", "ausgabe/foerder/etappe1/GN1F_A4.pdf", "a4", "f", "4 Seiten, letzte Seite Rückmeldung"),
    "f2": ("Förder-Material Etappe 2F", "ausgabe/foerder/etappe2/Foerder_Etappe2_A4.pdf", "a5", "f", "5 Seiten: Merkkarte, Material, Blatt 5F–6F"),
    "gn2f": ("Gelingensnachweis 2F", "ausgabe/foerder/etappe2/GN2F_A4.pdf", "a4", "f", "4 Seiten, letzte Seite Rückmeldung"),
    "f3": ("Förder-Material Etappe 3F", "ausgabe/foerder/etappe3/Foerder_Etappe3_A4.pdf", "a5", "f", "7 Seiten: Merkkarte, Material Erdmännchen, Blatt 7F–9F"),
}

SCHRITTE = [
    {"id": "vorher", "n": "0", "kurz": "Vorbereitung", "titel": "Vor der Reihe",
     "wann": "spätestens eine Woche vor Doppelstunde 1",
     "tun": [
         "Den Lernbuddy (laminierter Tischrahmen) gibt es schon. Er wird nicht neu gedruckt.",
         "Kontroll-Kiosk auf dem Klassenlaptop speichern und einmal ausprobieren: Tipp, Lösung, Vollbild.",
         "Förderziele für die zieldifferent lernenden Kinder vereinbaren.",
         "Termine festlegen: früher Klassenarbeitstermin in Doppelstunde 7, später in Doppelstunde 8. Arbeitszeit und Punkteverteilung festlegen.",
     ],
     "druck": ["lernweg", "lernwegF", "strategie", "schild"],
     "digital": ["kiosk", "animation"]},
    {"id": "ds1", "n": "1", "kurz": "Doppelstunde 1", "titel": "Start und Etappe 1",
     "wann": "Doppelstunde 1",
     "tun": [
         "Ablauf-Animation zeigen (etwa 5 Minuten). Danach bekommt jedes Kind seinen Lernweg.",
         "Input 1 am Beamer. Merkblatt 1 und Übungsblätter austeilen.",
         "Die Kinder legen jedes Blatt in die Mitte ihres Lernbuddys. Vertiefungen sind freiwillig.",
         "Strategiekarten 1 bis 3 vorstellen (Lesen mit Suchauftrag, Markieren, Ordnen).",
     ],
     "druck": ["mb1", "ub1", "f1"],
     "digital": ["animation", "in1", "kiosk"]},
    {"id": "ds2", "n": "2", "kurz": "Doppelstunde 2", "titel": "Gelingensnachweis 1, Start Etappe 2",
     "wann": "Doppelstunde 2",
     "tun": [
         "Wer Blatt 1 bis 4 fertig hat, schreibt Nachweis 1 A. Rückmeldung auf der Rückseite ausfüllen.",
         "Vier von fünf Zielen: Freigabe auf dem Lernweg eintragen. Weniger: üben mit dem genannten Blatt, dann Nachweis 1 B.",
         "Für Freigegebene Input 2 als Kleingruppe. Alles für Etappe 2 muss ab jetzt bereitliegen.",
     ],
     "druck": ["gn1a", "gn1b", "gn1f", "mb2", "ub2", "woerter", "f2"],
     "digital": ["in2"]},
    {"id": "ds3", "n": "3", "kurz": "Doppelstunde 3", "titel": "Gelingensnachweis 2, Start Etappe 3",
     "wann": "Doppelstunde 3",
     "tun": [
         "Nachweis 2 A für alle, die Blatt 5 und 6 fertig haben. Wiederholung mit 2 B.",
         "Für Freigegebene Input 3 als Kleingruppe. Jedes Kind wählt Erdmännchen oder Roten Panda und bleibt bei Blatt 7 bis 9 bei diesem Tier.",
         "Etappe 1 bei Bedarf mit gezielter Hilfe abschließen.",
     ],
     "druck": ["gn2a", "gn2b", "gn2f", "mb3", "ub3", "f3"],
     "digital": ["in3"]},
    {"id": "ds4", "n": "4", "kurz": "Doppelstunde 4", "titel": "Schreiben und Haltestelle",
     "wann": "Doppelstunde 4",
     "tun": [
         "Haltestellen-Schild aufhängen, Rückmeldekarten dort auslegen.",
         "Blatt 8 und 9: Wer den Text selbst geprüft hat, holt sich an der Haltestelle eine Rückmeldung. Das schreibende Kind entscheidet selbst, was es verbessert.",
         "Spätestens jetzt Unterstützung und Förderziele prüfen, wenn Kinder deutlich hinterherhängen.",
     ],
     "druck": ["rueck"],
     "digital": ["in3", "kiosk"]},
    {"id": "ds5", "n": "5", "kurz": "Doppelstunde 5", "titel": "Probearbeit, erstes Fenster",
     "wann": "Doppelstunde 5",
     "tun": [
         "Wer Blatt 7 bis 9 abgeschlossen hat, schreibt die Probearbeit. Die anderen arbeiten leise weiter.",
         "Arbeitszeit vorher auf Seite 1 eintragen. Hilfeseite und „Das zählt“ sind erlaubt, Partnerhilfe und Kiosk nicht.",
         "Seite 7 (Rückmeldung) bis Doppelstunde 6 ausfüllen.",
     ],
     "druck": ["probe"],
     "digital": []},
    {"id": "ds6", "n": "6", "kurz": "Doppelstunde 6", "titel": "Zweites Probefenster, Feedback, Wahlzeit",
     "wann": "Doppelstunde 6",
     "tun": [
         "Zweites Fenster für die Probearbeit. Feedback an die Kinder aus Doppelstunde 5 geben.",
         "Auf der Rückmeldung den Klassenarbeitstermin ankreuzen: früh nur nach Feedback und Vorbereitung.",
         "Wahlzeit beginnt: Projekte, Wiederholung oder Vertiefung nachholen. Unter 4 von 5 zuerst die offenen Ziele üben.",
     ],
     "druck": ["wahl", "tp_otter", "tp_erd", "tp_panda"],
     "digital": ["kiosk"]},
    {"id": "ds7", "n": "7", "kurz": "Doppelstunde 7", "titel": "Klassenarbeit, früher Termin",
     "wann": "Doppelstunde 7",
     "tun": [
         "Kinder mit frühem Termin schreiben die Klassenarbeit in einem festgelegten Teil der Doppelstunde.",
         "Alle anderen arbeiten still an Projekten oder bereiten sich vor. Danach Projektzeit für alle.",
     ],
     "druck": ["ka1"],
     "digital": []},
    {"id": "ds8", "n": "8", "kurz": "Doppelstunde 8", "titel": "Klassenarbeit, später Termin, Abschluss",
     "wann": "Doppelstunde 8",
     "tun": [
         "Kinder mit spätem Termin schreiben die zweite Variante.",
         "Bereits geprüfte Kinder arbeiten an Projekten. Am Ende: Tiermagazin vorstellen, freiwillige Kurzvorträge, Rückblick auf die Reihe.",
     ],
     "druck": ["ka2"],
     "digital": []},
]

OFFEN = [
    "Arbeitszeit, Punkteverteilung und Notengrenzen der Klassenarbeit; Arbeitszeit der Probearbeit.",
    "Foto für die Klassenarbeit Breitmaulnashorn fehlt (Platzhalter). Biber-Foto ist vorläufig aus dem Tierpaket.",
    "Probearbeit und Klassenarbeit in der F-Fassung für die zieldifferent lernenden Kinder.",
    "Welche Variante an welchem Termin geschrieben wird. Vorschlag: Biber früh, Breitmaulnashorn spät.",
]

FORMAT = {
    "a5": ("A5 verkleinert", "A4-Seiten auf A5 verkleinert drucken. Das Blatt passt dann in die Mitte des Lernbuddys."),
    "a4": ("A4 Originalgröße", "In tatsächlicher Größe drucken (100 %), nicht verkleinern."),
    "lam": ("laminieren", "Nach dem Drucken laminieren, wird mehrfach benutzt."),
    "dig": ("digital", "Wird nicht gedruckt."),
}


def link(path: str, absolut: bool) -> str:
    return (ABS + path) if absolut else path


def anzahl_attr(a):
    return "" if not a else " data-n='%s'" % a


def item(key: str, absolut: bool) -> str:
    titel, path, fmt, anz, hinweis = M[key]
    tags = "".join("<span class='tag t-%s'>%s</span>" % (f, FORMAT[f][0]) for f in fmt.split())
    cnt = "<span class='cnt'%s></span>" % anzahl_attr(anz) if anz else ""
    cb = "<input type='checkbox' id='cb-%s' aria-label='%s erledigt'>" % (key, html.escape(titel)) if anz else ""
    return ("<li class='mat'>%s<div class='mt'><a href='%s' target='_blank' rel='noopener'>%s</a>%s<div class='mh'>%s</div></div>"
            "<div class='mr'>%s%s</div></li>"
            % (cb, html.escape(link(path, absolut)), html.escape(titel), "", html.escape(hinweis), tags, cnt))


def seite(absolut: bool) -> str:
    for k, v in M.items():
        if not (ROOT / v[1]).exists():
            raise SystemExit("Fehlt: %s (%s)" % (v[1], k))
    nav = "".join("<a href='#%s'><b>%s</b>%s</a>" % (s["id"], s["n"], html.escape(s["kurz"])) for s in SCHRITTE)
    steps = []
    for s in SCHRITTE:
        druck = "".join(item(k, absolut) for k in s["druck"])
        dig = "".join(item(k, absolut) for k in s["digital"])
        steps.append(
            "<section class='step' id='%s'><div class='num'>%s</div><div class='sc'>"
            "<div class='when'>%s</div><h2>%s</h2>"
            "<div class='cols'><div class='tun'><h3>So läuft es</h3><ul>%s</ul></div>"
            "<div class='mats'>%s%s</div></div></div></section>"
            % (s["id"], s["n"], html.escape(s["wann"]), html.escape(s["titel"]),
               "".join("<li>%s</li>" % html.escape(t) for t in s["tun"]),
               ("<h3>Gedruckt bereitlegen</h3><ul class='ml'>%s</ul>" % druck) if druck else "",
               ("<h3>Am Beamer oder Laptop</h3><ul class='ml'>%s</ul>" % dig) if dig else ""))
    # Gesamtübersicht
    reihen = []
    for s in SCHRITTE:
        for k in s["druck"]:
            titel, path, fmt, anz, hinweis = M[k]
            reihen.append("<tr><td><a href='%s' target='_blank' rel='noopener'>%s</a></td><td>%s</td><td>%s</td><td class='num-c'><span class='cnt'%s></span></td></tr>"
                          % (html.escape(link(path, absolut)), html.escape(titel), html.escape(s["kurz"]),
                             " ".join(FORMAT[f][0] for f in fmt.split()), anzahl_attr(anz)))
    repo_hinweis = ("Die Links öffnen die Dateien im Repo <a href='%s/tree/%s' target='_blank' rel='noopener'>technikerleben/d5ur2-zootiere</a>."
                    % (REPO, BRANCH)) if absolut else "Die Links öffnen die Dateien in diesem Repo."
    return TEMPLATE.replace("__FONTS__", font_css()).replace("__NAV__", nav).replace("__STEPS__", "".join(steps)) \
        .replace("__ROWS__", "".join(reihen)).replace("__OFFEN__", "".join("<li>%s</li>" % html.escape(o) for o in OFFEN)) \
        .replace("__REPO__", repo_hinweis) \
        .replace("__ANIM__", html.escape(link(M["animation"][1], absolut))) \
        .replace("__KIOSK__", html.escape(link(M["kiosk"][1], absolut))) \
        .replace("__ERG__", REPO + "/blob/%s/planung/Ergaenzungen_Umsetzung.md" % BRANCH) \
        .replace("__FWF__", REPO + "/blob/%s/planung/Foerder_Workflow.md" % BRANCH)


TEMPLATE = r"""<title>Leitfaden Zootiere</title>
<style>
__FONTS__
/* Layout: Kopf mit Überblick und Druckrechner, darunter die Schritte 0–8 als Zeitleiste mit Seitennavigation */
:root{
  --bg:#F5F4F1; --card:#FFFFFF; --ink:#1E2A35; --muted:#5A6A78; --line:#D0DCE6; --ghost:#EEF3F7;
  --slate:#3E5668; --slate-d:#2C3D4C; --rust:#D97A4A; --rust-d:#9E4E22; --rust-g:#FBF0EB;
  --sage:#7DBB6F; --sage-d:#4D8B3F; --sage-g:#F0FAF0; --warn:#C17B00;
  --font:'Andika',"Trebuchet MS",sans-serif;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#131A20; --card:#1B242C; --ink:#E6ECF1; --muted:#A0B0BD; --line:#2F3F4D; --ghost:#202C36;
  --slate:#9DB9CE; --slate-d:#C9D9E5; --rust:#E89466; --rust-d:#F2B08B; --rust-g:#3A2A22;
  --sage:#8FCB82; --sage-d:#A8D49D; --sage-g:#1F2F24; --warn:#E3A23A; color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#131A20; --card:#1B242C; --ink:#E6ECF1; --muted:#A0B0BD; --line:#2F3F4D; --ghost:#202C36;
  --slate:#9DB9CE; --slate-d:#C9D9E5; --rust:#E89466; --rust-d:#F2B08B; --rust-g:#3A2A22;
  --sage:#8FCB82; --sage-d:#A8D49D; --sage-g:#1F2F24; --warn:#E3A23A; color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font-family:var(--font);font-size:16px;line-height:1.5;margin:0;padding-block:24px 48px;padding-inline:16px}
a{color:var(--rust-d);text-underline-offset:2px}
a:focus-visible,input:focus-visible{outline:3px solid var(--rust);outline-offset:2px}
.wrap{max-width:1180px;margin:0 auto}
header{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:28px;align-items:start;margin-bottom:28px}
.eyebrow{font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--rust-d)}
h1{font-size:clamp(30px,4vw,44px);line-height:1.08;margin:6px 0 12px;color:var(--slate-d);text-wrap:balance}
.lead{font-size:18px;max-width:60ch;margin:0 0 16px}
.flow{display:flex;flex-wrap:wrap;gap:6px;align-items:center;font-size:14px;font-weight:700;margin:0 0 14px}
.flow span{padding:6px 10px;border-radius:999px;background:var(--ghost);border:1.5px solid var(--line);color:var(--slate-d)}
.flow span.p{border-color:var(--rust);background:var(--rust-g);color:var(--rust-d)}
.flow span.s{border-color:var(--sage-d);background:var(--sage-g);color:var(--sage-d)}
.flow i{font-style:normal;color:var(--rust)}
.quick{display:flex;flex-wrap:wrap;gap:10px}
.btn{display:inline-flex;align-items:center;gap:8px;padding:10px 14px;border-radius:10px;border:2px solid var(--slate);color:var(--slate-d);text-decoration:none;font-weight:700;background:var(--card)}
.btn.main{background:var(--rust);border-color:var(--rust);color:#fff}
.panel{background:var(--card);border:1.5px solid var(--line);border-radius:16px;padding:18px 20px}
.panel h2{font-size:18px;margin:0 0 10px;color:var(--slate-d)}
.calc{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:14px}
.calc label{display:flex;flex-direction:column;gap:4px;font-size:14px;font-weight:700;color:var(--muted)}
.calc input{font:700 22px var(--font);padding:6px 10px;border:2px solid var(--line);border-radius:10px;background:var(--bg);color:var(--ink);width:100%;font-variant-numeric:tabular-nums}
.legend{display:flex;flex-direction:column;gap:8px;font-size:14px}
.legend div{display:flex;gap:10px;align-items:flex-start}
.legend .tag{flex:0 0 auto}
.tag{display:inline-block;font-size:12px;font-weight:700;padding:2px 8px;border-radius:6px;white-space:nowrap;border:1.5px solid}
.t-a5{border-color:var(--rust);color:var(--rust-d);background:var(--rust-g)}
.t-a4{border-color:var(--slate);color:var(--slate-d);background:var(--ghost)}
.t-lam{border-color:var(--sage-d);color:var(--sage-d);background:var(--sage-g)}
.t-dig{border-color:var(--line);color:var(--muted);background:transparent;border-style:dashed}
.layout{display:grid;grid-template-columns:200px minmax(0,1fr);gap:28px;align-items:start}
nav.side{position:sticky;top:calc(env(safe-area-inset-top, 0px) + 16px);display:flex;flex-direction:column;gap:2px;font-size:15px}
nav.side a{display:flex;gap:10px;align-items:center;padding:7px 10px;border-radius:8px;color:var(--ink);text-decoration:none}
nav.side a:hover{background:var(--ghost)}
nav.side a b{display:inline-flex;width:26px;height:26px;border-radius:50%;align-items:center;justify-content:center;background:var(--slate);color:var(--card);font-size:13px;flex:0 0 auto}
nav.side .sub{margin-top:10px;padding-top:10px;border-top:1.5px solid var(--line)}
.steps{display:flex;flex-direction:column;gap:18px;min-width:0;position:relative}
.steps::before{content:"";position:absolute;left:25px;top:26px;bottom:26px;width:3px;background:var(--line)}
.step{position:relative}
.step{display:grid;grid-template-columns:52px minmax(0,1fr);gap:16px;scroll-margin-top:16px}
.step .num{width:52px;height:52px;border-radius:50%;background:var(--slate);color:var(--card);display:flex;align-items:center;justify-content:center;font-size:22px;font-weight:700;position:relative}
.sc{background:var(--card);border:1.5px solid var(--line);border-radius:16px;padding:16px 20px 18px;min-width:0}
.when{font-size:13px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.sc h2{margin:2px 0 12px;font-size:24px;line-height:1.15;color:var(--slate-d);text-wrap:balance}
.cols{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);gap:22px}
h3{font-size:14px;letter-spacing:.06em;text-transform:uppercase;color:var(--rust-d);margin:0 0 8px}
.mats h3+ul+h3,.mats ul+h3{margin-top:14px}
.tun ul{margin:0;padding-left:20px;display:flex;flex-direction:column;gap:6px}
.ml{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:6px}
.mat{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:10px;align-items:start;padding:8px 10px;border:1.5px solid var(--line);border-radius:10px;background:var(--bg)}
.mat:not(:has(input)){grid-template-columns:minmax(0,1fr) auto}
.mat input{width:20px;height:20px;margin-top:2px;accent-color:var(--sage-d)}
.mat:has(input:checked){opacity:.55}
.mat:has(input:checked) a{text-decoration:line-through}
.mt a{font-weight:700}
.mh{font-size:13px;color:var(--muted);line-height:1.35}
.mr{display:flex;flex-direction:column;align-items:flex-end;gap:4px}
.cnt{font-weight:700;font-size:15px;font-variant-numeric:tabular-nums;color:var(--slate-d);white-space:nowrap}
.extra{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;margin-top:28px}
.tablewrap{overflow-x:auto;margin-top:28px}
table{width:100%;border-collapse:collapse;font-size:15px;background:var(--card);border:1.5px solid var(--line);border-radius:16px;overflow:hidden}
th,td{text-align:left;padding:8px 12px;border-bottom:1px solid var(--line);vertical-align:top}
th{font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);background:var(--ghost)}
td.num-c{text-align:right}
.offen li::marker{color:var(--warn)}
.panel ul{margin:0;padding-left:20px;display:flex;flex-direction:column;gap:6px}
.foot{margin-top:28px;font-size:13px;color:var(--muted)}
@media (max-width:900px){header{grid-template-columns:1fr}.layout{grid-template-columns:1fr}nav.side{display:none}.cols{grid-template-columns:1fr}.extra{grid-template-columns:1fr}}
@media (max-width:520px){.steps::before{display:none}.step{grid-template-columns:1fr}.step .num{width:40px;height:40px;font-size:18px}.calc{grid-template-columns:1fr}.mat{grid-template-columns:auto minmax(0,1fr)}.mr{grid-column:2;flex-direction:row;align-items:center}}
@media (prefers-reduced-motion: reduce){html{scroll-behavior:auto}}
html{scroll-behavior:smooth}
</style>

<div class="wrap">
<header>
  <div>
    <div class="eyebrow">Deutsch · Jahrgang 5 · Zootiere</div>
    <h1>So läuft die Reihe Zootiere</h1>
    <p class="lead">Acht Doppelstunden, drei Etappen im eigenen Tempo. Die Kinder lernen, ein Zootier mit Bild und Sachtext sachlich und geordnet zu beschreiben. Hier steht Schritt für Schritt, was passiert und was wann gedruckt bereitliegen muss.</p>
    <div class="flow" aria-label="Ablauf jeder Etappe">
      <span>Input + Merkblatt</span><i>→</i><span>Pflichtblätter</span><span class="p">Vertiefung freiwillig</span><i>→</i><span class="s">Nachweis: 4 von 5</span>
    </div>
    <div class="flow" aria-label="Ablauf nach Etappe 3">
      <span>Probearbeit</span><i>→</i><span class="s">Feedback</span><i>→</i><span>Wahlzeit</span><i>→</i><span class="p">Klassenarbeit, 2 Termine</span>
    </div>
    <div class="quick"><a class="btn main" href="__ANIM__" target="_blank" rel="noopener">Ablauf-Animation öffnen</a><a class="btn" href="__KIOSK__" target="_blank" rel="noopener">Kontroll-Kiosk öffnen</a></div>
  </div>
  <div class="panel">
    <h2>Druckrechner</h2>
    <div class="calc">
      <label for="n-alle">Kinder in der Klasse<input id="n-alle" type="number" min="1" max="40" value="26" inputmode="numeric"></label>
      <label for="n-f">davon zieldifferent<input id="n-f" type="number" min="0" max="10" value="2" inputmode="numeric"></label>
    </div>
    <div class="legend">
      <div><span class="tag t-a5">A5 verkleinert</span><span>A4-Seite verkleinert auf A5 drucken (Druckdialog: 2 Seiten pro Blatt, dann mittig schneiden). Passt in die Mitte des Lernbuddys.</span></div>
      <div><span class="tag t-a4">A4 Originalgröße</span><span>In tatsächlicher Größe drucken, nicht verkleinern.</span></div>
      <div><span class="tag t-lam">laminieren</span><span>Einmal herstellen, mehrfach benutzen.</span></div>
      <div><span class="tag t-a4" style="opacity:.9">Graustufen</span><span>Alles für die Kinder ist für den Graustufendruck gesetzt.</span></div>
    </div>
  </div>
</header>

<div class="layout">
  <nav class="side" aria-label="Schritte">__NAV__<div class="sub"><a href="#uebersicht"><b>≡</b>Druckübersicht</a><a href="#offen"><b>!</b>Noch offen</a></div></nav>
  <main class="steps">
    __STEPS__
  </main>
</div>

<div class="tablewrap" id="uebersicht">
  <table>
    <thead><tr><th>Material</th><th>bereit ab</th><th>Format</th><th style="text-align:right">Anzahl</th></tr></thead>
    <tbody>__ROWS__</tbody>
  </table>
</div>

<div class="extra">
  <div class="panel">
    <h2>Gut zu wissen</h2>
    <ul>
      <li>Jedes Kind arbeitet in seinem Tempo. Deshalb liegt das Material einer Etappe ab ihrem Startpunkt vollständig bereit, nicht erst, wenn die ganze Klasse so weit ist.</li>
      <li>Input und Merkblatt haben denselben Inhalt. Kinder, die später starten, bekommen den Input in der Kleingruppe oder lesen das Merkblatt.</li>
      <li>Der Kontroll-Kiosk gilt nur beim Üben. Bei Nachweisen, Probearbeit und Klassenarbeit gibt es keinen Kiosk und keine Partnerhilfe.</li>
      <li>Fachliche Leistung und Lernbuddy-Nutzung werden getrennt rückgemeldet.</li>
      <li>Hintergrund zu den Partnerphasen: <a href="__ERG__" target="_blank" rel="noopener">Ergänzungen und Hinweise</a>. Zieldifferentes Material: <a href="__FWF__" target="_blank" rel="noopener">Förder-Workflow</a>.</li>
    </ul>
  </div>
  <div class="panel offen" id="offen">
    <h2>Noch offen</h2>
    <ul>__OFFEN__</ul>
  </div>
</div>
<p class="foot">__REPO__ Die Häkchen und die Klassengröße speichert nur dein Browser.</p>
</div>

<script>
(() => {
  const st = { get(k){ try { return localStorage.getItem(k); } catch(e) { return null; } },
               set(k,v){ try { localStorage.setItem(k,v); } catch(e) {} } };
  const nA = document.getElementById("n-alle"), nF = document.getElementById("n-f");
  if (st.get("zt-alle")) nA.value = st.get("zt-alle");
  if (st.get("zt-f")) nF.value = st.get("zt-f");
  function rechne(){
    const alle = Math.max(0, parseInt(nA.value || "0", 10)), f = Math.min(alle, Math.max(0, parseInt(nF.value || "0", 10)));
    const kind = alle - f;
    const val = {kind, f, alle, drittel: Math.ceil(kind/3), halb: Math.ceil(kind/2), tisch: Math.ceil(alle/4)};
    document.querySelectorAll(".cnt[data-n]").forEach(el => {
      const a = el.dataset.n;
      let t;
      if (a.startsWith("fix:")) t = "× " + a.slice(4);
      else if (a === "termin") t = "je nach Anmeldung";
      else if (a === "tisch") t = "× " + val.tisch + " (je Tisch)";
      else t = "× " + val[a];
      el.textContent = t;
    });
    st.set("zt-alle", nA.value); st.set("zt-f", nF.value);
  }
  nA.addEventListener("input", rechne); nF.addEventListener("input", rechne); rechne();
  document.querySelectorAll(".mat input[type=checkbox]").forEach(cb => {
    if (st.get(cb.id) === "1") cb.checked = true;
    cb.addEventListener("change", () => st.set(cb.id, cb.checked ? "1" : "0"));
  });
})();
</script>
"""


def main():
    repo = seite(False)
    (ROOT / "anleitung.html").write_text(
        "<!doctype html><html lang='de'><head><meta charset='utf-8'>"
        "<meta name='viewport' content='width=device-width,initial-scale=1,viewport-fit=cover'></head><body>"
        + repo + "</body></html>", encoding="utf-8")
    if len(sys.argv) > 1:
        Path(sys.argv[1]).write_text(seite(True), encoding="utf-8")
    print("ok: anleitung.html, %d Materialien verlinkt" % len(M))


if __name__ == "__main__":
    main()
