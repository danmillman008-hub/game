#!/usr/bin/env python3
"""ten_stills.py — build the key frames for the ten-minute anime from character sheets.

The video model does not decide framing; the storyboard does. Every hard angle the
film needs — Dutch tilt, worm's eye, high angle, over-the-shoulder, silhouette — is
built HERE, in the still, and the prompt only asks for the micro-motion. That is also
the only way to test those angles honestly: if the clip from a 12-degree Dutch key
frame comes back upright, the model refused the frame, and we know.

    cutout()      pull the character off its sheet (erode+dilate kills the scan lines
                  and the stray white/red artefacts on the original PNGs)
    plates()      three flat backgrounds drawn from five colours, cel rules
    frame()       place character on plate at a scale/anchor, optional tilt and shadow

    python3 studio/motions/ten_stills.py --sheet     # contact sheet of every key frame
    python3 studio/motions/ten_stills.py             # write them
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageOps

ROOT = Path(__file__).resolve().parent.parent.parent
FILM = ROOT / "films" / "anime_ten"
OUT = FILM / "stills"
W, H = 960, 1280


# ------------------------------------------------------------------ cutout ----
def _largest_component(mask: Image.Image, scale: int = 8) -> Image.Image:
    """Keep only the biggest blob. The character sheets carry stray bars, scan lines
    and cut marks that survive erosion; the figure is always the largest thing."""
    from collections import deque
    small = mask.resize((max(1, mask.width // scale), max(1, mask.height // scale)))
    px = small.load()
    w, h = small.size
    seen = [[False] * w for _ in range(h)]
    best: list[tuple[int, int]] = []
    for y in range(h):
        for x in range(w):
            if px[x, y] and not seen[y][x]:
                q, comp = deque([(x, y)]), []
                seen[y][x] = True
                while q:
                    cx, cy = q.popleft()
                    comp.append((cx, cy))
                    for nx, ny in ((cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1)):
                        if 0 <= nx < w and 0 <= ny < h and px[nx, ny] and not seen[ny][nx]:
                            seen[ny][nx] = True
                            q.append((nx, ny))
                if len(comp) > len(best):
                    best = comp
    keep = Image.new("L", small.size, 0)
    kp = keep.load()
    for x, y in best:
        kp[x, y] = 255
    return keep.resize(mask.size, Image.NEAREST)


def erase_bands(mask: Image.Image, bands: list) -> Image.Image:
    """Some sheets carry cut marks that are attached to the figure, so blob filtering
    keeps them. A band wipe on the right half removes them without touching the body."""
    d = ImageDraw.Draw(mask)
    for y0, y1 in bands:
        d.rectangle([0, mask.height * y0, mask.width, mask.height * y1], fill=0)
    return mask


def cutout(ref: Path, dark_bg: bool = True, bands: list | None = None) -> Image.Image:
    src = Image.open(ref)
    alpha = src.convert("RGBA").getchannel("A")
    has_alpha = alpha.getextrema()[0] < 16
    im = src.convert("RGB")
    if has_alpha:                       # already cut out for us
        mask = alpha.point(lambda v: 255 if v > 40 else 0)
    else:
        g = im.convert("L")
        mask = g.point(lambda v: 255 if v > 38 else 0) if dark_bg else \
            g.point(lambda v: 255 if v < 226 else 0)
        mask = mask.filter(ImageFilter.MinFilter(5)).filter(ImageFilter.MaxFilter(5))
        mask = _largest_component(mask)
        mask = mask.filter(ImageFilter.MedianFilter(3))
        if bands:
            mask = erase_bands(mask, bands)
    rgba = im.convert("RGBA")
    rgba.putalpha(mask)
    box = mask.getbbox()
    if box:
        rgba = rgba.crop(box)
    return rgba


# ------------------------------------------------------------------ plates ----
SKY_TOP = (34, 42, 78)
SKY_LOW = (188, 132, 108)
FAR = (60, 64, 98)
NEAR = (26, 28, 44)
GROUND = (46, 48, 70)
WARM = (214, 176, 140)


def plate_storm() -> Image.Image:
    im = Image.new("RGB", (W, H), SKY_LOW)
    d = ImageDraw.Draw(im)
    hor = int(H * 0.66)
    d.rectangle([0, 0, W, int(hor * 0.5)], fill=SKY_TOP)
    d.rectangle([0, int(hor * 0.5), W, hor], fill=(120, 104, 116))
    d.rectangle([0, hor, W, H], fill=GROUND)
    # treeline: triangles only
    for i in range(0, W, 90):
        d.polygon([(i, hor), (i + 45, hor - 90 - (i % 70)), (i + 90, hor)], fill=NEAR)
    # one road, hard edges
    d.polygon([(W * 0.42, hor), (W * 0.58, hor), (W * 0.86, H), (W * 0.14, H)], fill=NEAR)
    for i in range(6):
        y = hor + 40 + i * 90
        d.rectangle([W * 0.5 - 6 - i * 3, y, W * 0.5 + 6 + i * 3, y + 26 + i * 6], fill=WARM)
    return im


def plate_room() -> Image.Image:
    im = Image.new("RGB", (W, H), (52, 46, 44))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, W, H], fill=(52, 46, 44))
    d.rectangle([W * 0.52, H * 0.10, W * 0.94, H * 0.62], fill=(226, 196, 150))  # window
    d.rectangle([W * 0.52, H * 0.10, W * 0.94, H * 0.14], fill=(38, 34, 34))
    d.line([W * 0.73, H * 0.10, W * 0.73, H * 0.62], fill=(38, 34, 34), width=8)
    d.rectangle([0, H * 0.80, W, H], fill=(38, 34, 34))                          # floor band
    d.polygon([(W * 0.55, H * 0.80), (W * 0.92, H * 0.80), (W * 0.98, H),
               (W * 0.42, H)], fill=(84, 70, 58))                                # light pool
    return im


def plate_city() -> Image.Image:
    im = Image.new("RGB", (W, H), SKY_LOW)
    d = ImageDraw.Draw(im)
    hor = int(H * 0.70)
    d.rectangle([0, 0, W, int(hor * 0.6)], fill=SKY_TOP)
    d.rectangle([0, int(hor * 0.6), W, hor], fill=(96, 96, 132))
    for x, w, h in ((-20, 180, 420), (140, 120, 560), (250, 200, 360),
                    (470, 140, 620), (620, 170, 470), (800, 180, 540)):
        d.rectangle([x, hor - h, x + w, hor], fill=FAR)
    d.rectangle([0, hor, W, H], fill=GROUND)
    return im


PLATES = {"storm": plate_storm, "room": plate_room, "city": plate_city}


# ------------------------------------------------------------------- frame ----
def frame(char: Image.Image, plate: str, scale: float, anchor: tuple[float, float],
          tilt: float = 0.0, shadow: bool = True, crop_head: float | None = None,
          darken: float = 0.0, silhouette: bool = False) -> Image.Image:
    """Place a character on a plate.

    scale   figure height as a fraction of frame height
    anchor  where the figure's feet sit (x, y) in frame fractions
    tilt    degrees of roll — this is the Dutch angle, baked into the key frame
    crop_head  take only the top N fraction of the figure (close-ups), 0-1
    darken  0-1, multiplies the plate — for night/silhouette shots
    """
    bg = PLATES[plate]().convert("RGB")
    if darken:
        bg = Image.eval(bg, lambda v: int(v * (1 - darken)))
    fig = char.copy()
    if crop_head:
        fig = fig.crop((0, 0, fig.width, int(fig.height * crop_head)))
    target_h = int(H * scale)
    target_w = max(1, int(fig.width * target_h / fig.height))
    fig = fig.resize((target_w, target_h), Image.LANCZOS)
    if silhouette:
        # keep the alpha, throw the colour away: a shape against the sky
        alpha = fig.getchannel("A")
        fig = Image.new("RGBA", fig.size, (14, 12, 20))
        fig.putalpha(alpha)
    if tilt:
        fig = fig.rotate(tilt, resample=Image.BICUBIC, expand=True)

    x = int(anchor[0] * W - fig.width / 2)
    y = int(anchor[1] * H - fig.height)

    if shadow:
        sh = Image.new("RGBA", fig.size, (0, 0, 0, 0))
        a = fig.getchannel("A").filter(ImageFilter.GaussianBlur(10))
        sh.putalpha(a.point(lambda v: int(v * 0.35)))
        bg.paste(Image.new("RGB", fig.size, (12, 10, 16)), (x, y), sh.getchannel("A"))
    bg.paste(fig, (x, y), fig)
    return bg


def build(spec: dict, chars: dict) -> Image.Image:
    ch = chars[spec["char"]]
    ref = ROOT / ch["ref"]
    char = cutout(ref, dark_bg=not ref.name.startswith(("c3", "c5")),
                  bands=ch.get("erase_bands"))
    return frame(char, spec.get("plate", "storm"), spec["scale"], tuple(spec["anchor"]),
                 spec.get("tilt", 0.0), spec.get("shadow", True),
                 spec.get("crop_head"), spec.get("darken", 0.0),
                 spec.get("silhouette", False))


def main() -> int:
    ap = argparse.ArgumentParser(prog="ten_stills", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--sheet", action="store_true", help="contact sheet instead of files")
    ap.add_argument("--specs", default=str(ROOT / "studio/motions/ten_specs.json"))
    a = ap.parse_args()

    chars = {c["id"]: c for c in json.loads((FILM / "characters.json").read_text())["characters"]}
    specs = [s for s in json.loads(Path(a.specs).read_text(encoding="utf-8"))
             if s.get("still_spec")]
    if not specs:
        raise SystemExit("no still_spec entries")

    if a.sheet:
        cols = 3
        thumbs = []
        for s in specs:
            im = build(s["still_spec"], chars).resize((320, 427))
            d = ImageDraw.Draw(im)
            d.rectangle([0, 0, 320, 22], fill=(0, 0, 0))
            d.text((6, 5), s["id"], fill=(255, 255, 255))
            thumbs.append(im)
        rows = (len(thumbs) + cols - 1) // cols
        sheet = Image.new("RGB", (cols * 320, rows * 427), (0, 0, 0))
        for i, t in enumerate(thumbs):
            sheet.paste(t, ((i % cols) * 320, (i // cols) * 427))
        out = FILM / "qc" / "contact_sheet.jpg"
        out.parent.mkdir(parents=True, exist_ok=True)
        sheet.save(out, quality=88)
        print(f"-> {out.relative_to(ROOT)}  ({len(thumbs)} frames)")
        return 0

    OUT.mkdir(parents=True, exist_ok=True)
    for s in specs:
        im = build(s["still_spec"], chars)
        p = OUT / f"{s['id']}.png"
        im.save(p)
        print(f"{s['id']}: {p.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
