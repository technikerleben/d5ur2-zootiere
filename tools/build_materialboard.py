#!/usr/bin/env python3
"""Erzeugt Vorschaubilder und Ersatz-Dateiliste für materialboard.html.

Aufruf aus dem Repository-Stamm:  python tools/build_materialboard.py

- board/dateien.json : alle versionierten Dateien (Pfad, Größe, Git-Blob-SHA).
  Wird nur genutzt, wenn die Live-Abfrage bei GitHub scheitert.
- board/thumbs/<blob-sha>.jpg : erste Seite jeder PDF als Graustufen-Vorschau.
  Der Dateiname ist der Git-Blob-Hash. Ändert sich eine PDF, passt die alte
  Vorschau nicht mehr und das Board zeigt bis zum nächsten Lauf ein Symbol.

Benötigt PyMuPDF (pip install pymupdf). Neue Dateien vorher committen oder
mit `git add` vormerken, sonst fehlen sie in der Liste.
"""
import datetime
import json
import os
import subprocess
import sys

try:
    import pymupdf as fitz
except ImportError:
    sys.exit("PyMuPDF fehlt: pip install pymupdf")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOARD = os.path.join(ROOT, "board")
THUMBS = os.path.join(BOARD, "thumbs")
THUMB_WIDTH = 320


def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True)


def tracked_files():
    files = []
    for line in git("ls-files", "-s").splitlines():
        meta, path = line.split("\t", 1)
        sha = meta.split()[1]
        if path.startswith("board/"):
            continue
        full = os.path.join(ROOT, path)
        if os.path.isfile(full):
            files.append({"path": path, "size": os.path.getsize(full), "sha": sha})
    return files


def render_thumb(pdf_path, out_path):
    with fitz.open(pdf_path) as doc:
        page = doc[0]
        zoom = THUMB_WIDTH / page.rect.width
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), colorspace=fitz.csGRAY, alpha=False)
        pix.save(out_path, jpg_quality=72)


def main():
    os.makedirs(THUMBS, exist_ok=True)
    files = tracked_files()
    wanted = set()
    created = 0
    for f in files:
        if not f["path"].lower().endswith(".pdf"):
            continue
        name = f["sha"] + ".jpg"
        wanted.add(f["sha"])
        out = os.path.join(THUMBS, name)
        if not os.path.exists(out):
            try:
                render_thumb(os.path.join(ROOT, f["path"]), out)
                created += 1
            except Exception as exc:  # defekte PDF nicht den Lauf abbrechen lassen
                wanted.discard(f["sha"])
                print(f"Keine Vorschau für {f['path']}: {exc}")
    removed = 0
    for name in os.listdir(THUMBS):
        if name.endswith(".jpg") and name[:-4] not in wanted:
            os.remove(os.path.join(THUMBS, name))
            removed += 1
    try:
        commit = git("rev-parse", "--short", "HEAD").strip()
    except subprocess.CalledProcessError:
        commit = ""
    snapshot = {
        "erzeugt": datetime.datetime.now().astimezone().isoformat(timespec="minutes"),
        "commit": commit,
        "thumbs": sorted(wanted),
        "files": files,
    }
    with open(os.path.join(BOARD, "dateien.json"), "w", encoding="utf-8") as fh:
        json.dump(snapshot, fh, ensure_ascii=False, indent=1)
    print(f"{len(files)} Dateien, {len(wanted)} Vorschauen ({created} neu, {removed} entfernt).")


if __name__ == "__main__":
    main()
