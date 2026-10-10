#!/usr/bin/env python3
"""Druckpakete: je eine PDF pro Schülerpaket (immer erst Materialbasis, dann Arbeitsblätter)
und Lehrkräfte-Material getrennt.

Vorher die Einzel-PDFs erzeugen:
    python3 tools/build_interviews.py
    python3 tools/build_material.py 1|2|3
    python3 tools/build_material.py pruefung inhalt/klassenarbeit_*.json
    python3 tools/build_foerder.py 1|2|3
    python3 tools/build_extras.py
Dann:
    python3 tools/build_pakete.py      -> ausgabe/pakete/
"""
from __future__ import annotations

import shutil
import sys
import zipfile
from pathlib import Path

import pymupdf as fitz

ROOT = Path(__file__).resolve().parent.parent
A = ROOT / "ausgabe"
OUT = A / "pakete"

SCHUELER = {
    "Schuelerpaket_Etappe1_A4.pdf": ["etappe1/Material_Etappe1_A4.pdf", "etappe1/Uebungsblaetter_Etappe1_A4.pdf"],
    "Schuelerpaket_Etappe2_A4.pdf": ["etappe2/Material_Etappe2_A4.pdf", "etappe2/Uebungsblaetter_Etappe2_A4.pdf"],
    "Schuelerpaket_Etappe3_A4.pdf": ["etappe3/Material_Etappe3_A4.pdf", "etappe3/Uebungsblaetter_Etappe3_A4.pdf"],
    "Schuelerpaket_Foerder_Etappe1_A4.pdf": ["foerder/etappe1/Material_Foerder_Etappe1_A4.pdf", "foerder/etappe1/Foerder_Etappe1_A4.pdf"],
    "Schuelerpaket_Foerder_Etappe2_A4.pdf": ["foerder/etappe2/Material_Foerder_Etappe2_A4.pdf", "foerder/etappe2/Foerder_Etappe2_A4.pdf"],
    "Schuelerpaket_Foerder_Etappe3_A4.pdf": ["foerder/etappe3/Material_Foerder_Etappe3_A4.pdf", "foerder/etappe3/Foerder_Etappe3_A4.pdf"],
    "Probearbeit_Waschbaer_A4.pdf": ["etappe3/Probearbeit_Waschbaer_A4.pdf"],
    "Klassenarbeit_V1_Biber_A4.pdf": ["pruefungen/Klassenarbeit_Biber_A4.pdf"],
    "Klassenarbeit_V2_Breitmaulnashorn_A4.pdf": ["pruefungen/Klassenarbeit_Breitmaulnashorn_A4.pdf"],
}

LEHRKRAFT = {
    "Kopiervorlagen_Etappe1_A4.pdf": ["etappe1/Merkblatt_1_A4.pdf", "etappe1/GN1_A_A4.pdf", "etappe1/GN1_B_A4.pdf"],
    "Kopiervorlagen_Etappe2_A4.pdf": ["etappe2/Merkblatt_2_A4.pdf", "etappe2/GN2_A_A4.pdf", "etappe2/GN2_B_A4.pdf"],
    "Kopiervorlagen_Etappe3_A4.pdf": ["etappe3/Merkblatt_3_A4.pdf", "etappe3/Haltestelle_Schild_A4.pdf"],
    "Kopiervorlagen_Foerder_A4.pdf": ["foerder/etappe1/GN1F_A4.pdf", "foerder/etappe2/GN2F_A4.pdf"],
    "Hilfekarten_laminieren_A4.pdf": ["etappe2/Woerterhilfe_A4.pdf", "etappe3/Rueckmeldekarte_A4.pdf"],
    "Interviews_Zeilenbelege_A4.pdf": ["interviews/Interviews_Pruefliste_A4.pdf"],
    "Strategiekarten_210x99.pdf": ["strategiekarten/Strategiekarten_A4.pdf"],
    "Lernweg_A4.pdf": ["lernweg/Lernweg_Zootiere_A4.pdf", "lernweg/Lernweg_Zootiere_F_A4.pdf"],
    "Wahlphase_Projekte_A4.pdf": ["wahlphase/Wahlphase_Projekte_A4.pdf"],
}
HTML = ["etappe1/Input_Etappe1.html", "etappe2/Input_Etappe2.html", "etappe3/Input_Etappe3.html", "lernweg/Ablauf_Animation.html"]

# Druckhinweis je Paket (für die Übersicht)
DRUCK = {
    "Schuelerpaket": "A4-Satz, auf A5 verkleinert drucken (Lernbuddy-Mitte)",
    "Probearbeit": "A4, Originalgröße",
    "Klassenarbeit": "A4, Originalgröße",
}


def zusammen(name: str, teile: list[str], ziel: Path) -> tuple[int, list[str]]:
    fehlt = [t for t in teile if not (A / t).exists()]
    if fehlt:
        return 0, fehlt
    d = fitz.open()
    for t in teile:
        d.insert_pdf(fitz.open(A / t))
    d.set_metadata({"title": name.replace("_", " ").replace(".pdf", ""), "author": "Deutsch · Jahrgang 5 · Zootiere"})
    d.save(ziel / name, garbage=3, deflate=True)
    return len(d), []


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    sch, lk = OUT / "schueler", OUT / "lehrkraft"
    sch.mkdir(parents=True)
    lk.mkdir()
    fehler = []
    zeilen = ["# Druckpakete Zootiere", "", "Schülerpakete: immer erst Materialbasis (Foto/Interview), dann Arbeitsblätter.", "",
              "| Datei | Seiten | Druck |", "|---|---|---|"]
    for ziel, plan in ((sch, SCHUELER), (lk, LEHRKRAFT)):
        for name, teile in plan.items():
            n, f = zusammen(name, teile, ziel)
            fehler += f
            druck = next((v for k, v in DRUCK.items() if name.startswith(k)), "siehe Lehrkraft-Leitfaden")
            zeilen.append("| %s/%s | %d | %s |" % (ziel.name, name, n, druck))
            print("%-45s %3d S." % (ziel.name + "/" + name, n))
    for h in HTML:
        if (A / h).exists():
            shutil.copy(A / h, lk / Path(h).name)
    (OUT / "README.md").write_text("\n".join(zeilen) + "\n", encoding="utf-8")
    with zipfile.ZipFile(OUT / "Zootiere_Druckpakete.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(OUT.rglob("*")):
            if f.is_file() and f.suffix != ".zip":
                z.write(f, f.relative_to(OUT))
    if fehler:
        print("FEHLT:", *fehler, sep="\n  ")
        sys.exit(1)


if __name__ == "__main__":
    main()
