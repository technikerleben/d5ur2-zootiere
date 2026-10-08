#!/usr/bin/env python3
"""Erzeugt die Ablauf-Animation der Reihe (HTML, farbig, offline).

Vorlage: tools/vorlagen/ablauf_animation.html (Seiteninhalt ohne Dokumentgerüst)
Ausgabe: ausgabe/lernweg/Ablauf_Animation.html (vollständige, eigenständige Datei)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_material import font_css  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent


def fragment() -> str:
    return (ROOT / "tools" / "vorlagen" / "ablauf_animation.html").read_text(encoding="utf-8").replace("__FONTS__", font_css())


def main():
    out = ROOT / "ausgabe" / "lernweg" / "Ablauf_Animation.html"
    out.write_text("<!doctype html><html lang='de'><head><meta charset='utf-8'>"
                   "<meta name='viewport' content='width=device-width,initial-scale=1,viewport-fit=cover'></head><body>"
                   + fragment() + "</body></html>", encoding="utf-8")
    if len(sys.argv) > 1:
        Path(sys.argv[1]).write_text(fragment(), encoding="utf-8")
    print("ok", out)


if __name__ == "__main__":
    main()
