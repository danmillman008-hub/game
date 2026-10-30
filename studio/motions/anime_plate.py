#!/usr/bin/env python3
"""anime_plate.py — draw the probe plates for the anime test.

Why synthetic plates and not a found image: we need to know one thing and only one
thing — **does the video model keep flat, cel-shaded 2D art, or does it drift back to
photoreal?** A photoreal still would answer a different question (restyling). A plate
with five flat colours, hard edges and zero texture is the cleanest possible probe:
if the output stays flat it can do anime, if it grows skin pores it cannot.

Two plates, both 960x1280 (the pipeline's aspect):

    a1_wide.png   dusk crossing: sky band, moon, two-tone city silhouette,
                  telephone wires, wet-street reflection band, girl with umbrella
    a2_eye.png    extreme close-up of one eye: lid lines, iris ring, one highlight

No text, no gradients except the sky, no anti-aliasing tricks — cel rules.

    python3 studio/motions/anime_plate.py            # -> films/anime_test/stills/
    python3 studio/motions/anime_plate.py --check    # colour count per plate
"""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent.parent
OUT = ROOT / "films" / "anime_test" / "stills"

W, H = 960, 1280

# a deliberately tiny palette: anime backgrounds are flat fields, not gradients
SKY_TOP = (38, 48, 84)
SKY_MID = (92, 86, 122)
SKY_LOW = (196, 138, 116)
MOON = (247, 238, 205)
CITY_FAR = (58, 62, 96)
CITY_NEAR = (30, 32, 52)
WIRE = (18, 18, 28)
GROUND = (44, 46, 70)
REFLECT = (214, 176, 140)
COAT = (26, 28, 44)
SKIN = (238, 206, 176)
HAIR = (30, 26, 38)
LINE = (16, 14, 22)
IRIS = (120, 156, 176)
WHITE = (244, 242, 236)


def wide() -> Image.Image:
    im = Image.new("RGB", (W, H), SKY_MID)
    d = ImageDraw.Draw(im)
    horizon = int(H * 0.62)

    # sky: three flat bands (cel backgrounds use bands, not gaussians)
    d.rectangle([0, 0, W, int(horizon * 0.55)], fill=SKY_TOP)
    d.rectangle([0, int(horizon * 0.55), W, int(horizon * 0.85)], fill=SKY_MID)
    d.rectangle([0, int(horizon * 0.85), W, horizon], fill=SKY_LOW)

    # moon
    d.ellipse([W * 0.62, H * 0.08, W * 0.62 + 150, H * 0.08 + 150], fill=MOON)

    # far city: rectangles only
    for x, w, h in ((0, 150, 300), (130, 90, 380), (210, 170, 250), (370, 120, 420),
                    (480, 100, 330), (570, 190, 300), (750, 210, 400)):
        d.rectangle([x, horizon - h, x + w, horizon], fill=CITY_FAR)
    # near city: darker, taller, offset
    for x, w, h in ((-40, 210, 520), (150, 130, 640), (600, 170, 700), (780, 200, 560)):
        d.rectangle([x, horizon - h, x + w, horizon + 20], fill=CITY_NEAR)

    # a few windows: single pixels of the warm colour, no detail
    for yy in range(horizon - 620, horizon - 40, 46):
        for xx in range(160, 300, 38):
            d.rectangle([xx, yy, xx + 12, yy + 18], fill=REFLECT)

    # ground + reflection band
    d.rectangle([0, horizon, W, H], fill=GROUND)
    for i, (y, w) in enumerate(((horizon + 40, 220), (horizon + 130, 150), (horizon + 230, 90))):
        d.rectangle([W // 2 - w // 2, y, W // 2 + w // 2, y + 18], fill=REFLECT)

    # telephone wires: three lines with a slight sag, drawn as polygons
    for i, y0 in enumerate((int(H * 0.10), int(H * 0.14), int(H * 0.18))):
        pts = [(x, y0 + int(26 * ((x - W / 2) / (W / 2)) ** 2)) for x in range(0, W + 1, 40)]
        d.line(pts, fill=WIRE, width=5)

    # the girl: coat trapezoid, head circle, umbrella arc — all flat
    cx = int(W * 0.31)
    base = int(H * 0.80)
    d.polygon([(cx - 46, base), (cx + 46, base), (cx + 66, base - 250), (cx - 66, base - 250)],
              fill=COAT)
    d.ellipse([cx - 34, base - 330, cx + 34, base - 258], fill=HAIR)
    d.pieslice([cx - 165, base - 560, cx + 165, base - 300], 180, 360, fill=COAT)
    d.line([cx, base - 430, cx, base - 300], fill=LINE, width=6)

    # rain: short strokes only, no blur
    for i in range(260):
        x = (i * 137) % W
        y = (i * 291) % (H - 120)
        d.line([x, y, x - 7, y + 34], fill=SKY_MID, width=3)
    return im


def eye() -> Image.Image:
    """Extreme close-up, the anime unit that costs the model least and shows most."""
    im = Image.new("RGB", (W, H), SKIN)
    d = ImageDraw.Draw(im)

    # hair mass across the top, flat
    d.rectangle([0, 0, W, int(H * 0.26)], fill=HAIR)
    d.polygon([(0, int(H * 0.26)), (W, int(H * 0.20)), (W, int(H * 0.34)), (0, int(H * 0.40))],
              fill=HAIR)

    # eye socket: upper lid, lower lid as two thick arcs
    top, bot = int(H * 0.42), int(H * 0.62)
    d.pieslice([W * 0.10, top - 130, W * 0.90, bot + 60], 200, 340, fill=WHITE)
    d.pieslice([W * 0.10, top + 20, W * 0.90, bot + 150], 20, 160, fill=WHITE)

    # iris: ring + pupil + one highlight, all hard shapes
    icx, icy, r = int(W * 0.50), int(H * 0.53), 150
    d.ellipse([icx - r, icy - r, icx + r, icy + r], fill=IRIS)
    d.ellipse([icx - r, icy - r, icx + r, icy + r], outline=LINE, width=8)
    d.ellipse([icx - 62, icy - 62, icx + 62, icy + 62], fill=LINE)
    d.ellipse([icx - 96, icy - 110, icx - 22, icy - 40], fill=WHITE)

    # lashes: three thick strokes, deliberately crude
    d.line([W * 0.10, top + 10, W * 0.50, top - 90], fill=LINE, width=26)
    d.line([W * 0.50, top - 90, W * 0.90, top + 20], fill=LINE, width=26)
    d.line([W * 0.10, bot + 40, W * 0.90, bot + 10], fill=LINE, width=14)

    # one hair strand crossing the frame — the shot's only moving element
    d.line([W * 0.18, int(H * 0.24), W * 0.58, int(H * 0.96)], fill=HAIR, width=22)
    return im


def cel(src: Path, levels: int = 5) -> Image.Image:
    """Posterise a real photograph into flat bands and lay line art over it.

    This is the important probe of the three. The synthetic plates prove the model can
    keep a *flat* image flat. This one starts from a real photograph of a real scene,
    so if the output comes back cel-shaded we know the model can hold a style that is
    not the style of its input — which is exactly the "can it do anime" question.
    """
    from PIL import ImageFilter, ImageOps
    im = Image.open(src).convert("RGB")
    flat = ImageOps.posterize(im, levels)                       # 5 bits -> visible bands
    flat = flat.filter(ImageFilter.ModeFilter(size=7))          # kill texture, keep shapes
    flat = ImageOps.posterize(flat, 3)                          # hard, 3 bits: poster art
    edges = im.convert("L").filter(ImageFilter.FIND_EDGES)
    edges = ImageOps.autocontrast(edges).point(lambda v: 255 if v > 60 else 0)
    ink = Image.new("RGB", im.size, (18, 16, 24))
    out = Image.composite(ink, flat, edges)
    return out


def palette_colours(im: Image.Image) -> int:
    return len(im.convert("RGB").getcolors(maxcolors=1 << 20) or [])


def main() -> int:
    ap = argparse.ArgumentParser(prog="anime_plate", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="report palette size, write nothing")
    a = ap.parse_args()
    plates = {"a1_wide.png": wide(), "a2_eye.png": eye()}
    src = ROOT / "films" / "before_leaving" / "stills" / "s01_wide.png"
    if src.exists():
        plates["a3_cel.png"] = cel(src)
    for name, im in plates.items():
        n = palette_colours(im)
        if a.check:
            print(f"{name}: {n} colours")
            continue
        OUT.mkdir(parents=True, exist_ok=True)
        im.save(OUT / name)
        print(f"{name}: {n} colours -> {(OUT / name).relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
