#!/usr/bin/env python3
"""Draw the site icons: a teal tile with the Devanagari letter च.

    python3 tools/make_icons.py images

Writes favicon.png (192), favicon-32.png, favicon.ico (16/32/48) and
apple-touch-icon.png (180, opaque as iOS wants). Each stays far below 50 KB.
Needs playwright (with Chromium) and Pillow.
"""
import io
import sys
from pathlib import Path

from PIL import Image
from playwright.sync_api import sync_playwright

TEAL, PARCHMENT, ACCENT = "#2f6f6a", "#fffdf8", "#e0a36b"
HTML = f"""<body style="margin:0;background:{TEAL}">
<div style="width:512px;height:512px;background:{TEAL};display:flex;
align-items:center;justify-content:center;position:relative;overflow:hidden">
<div style="font:700 400px/1 'Noto Sans Devanagari','Mukta','Nirmala UI',
'Mangal',sans-serif;color:{PARCHMENT};margin-top:-20px">च</div>
<div style="position:absolute;left:96px;right:96px;top:112px;height:22px;
border-radius:11px;background:{ACCENT}"></div></div></body>"""


def main():
    out = Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 512, "height": 512})
        pg.set_content(HTML)
        pg.wait_for_timeout(300)
        big = Image.open(io.BytesIO(pg.screenshot())).convert("RGB")
        b.close()

    def size(px):
        return big.resize((px, px), Image.LANCZOS)

    size(192).save(out / "favicon.png", optimize=True)
    size(32).save(out / "favicon-32.png", optimize=True)
    size(180).save(out / "apple-touch-icon.png", optimize=True)
    size(48).save(out / "favicon.ico", sizes=[(16, 16), (32, 32), (48, 48)])
    for f in ("favicon.png", "favicon-32.png", "apple-touch-icon.png",
              "favicon.ico"):
        print(f, (out / f).stat().st_size, "bytes")


if __name__ == "__main__":
    main()
