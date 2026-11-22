"""Entry for make.fun 'news-image-20261121' (Python 3.13, standard library only).

The image beside this file (entry.png) sums up the world news of
Saturday 21 November 2026 in one 1024x1024 picture. This program copies
it, byte for byte, to /output/entry.png, so two runs always write the
same bytes. Outside the grader's container, MAKEFUN_OUTPUT_DIR stands
in for /output:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(SRC, os.path.join(OUT_DIR, "entry.png"))
