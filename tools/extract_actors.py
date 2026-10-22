"""Extract the Stage-1 actors from the original's sprites' own footprints.

The plate from tools/build_plate2.py is the environment at a fixed camera. An
actor's art is then simply the frame's pixels inside the rectangle the game's own
sprite table says the actor occupies, minus everything that equals the plate.

Because the rectangle comes from the SAT rather than from a guess, the crop is
exactly the character's footprint, and the plate comparison removes whatever
environment shows through gaps in the silhouette.
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.ppm import read_ppm                  # noqa: E402
from tools.sat_log import read_frames, entries  # noqa: E402
from PIL import Image                           # noqa: E402

OUT = ROOT / "reconstruction" / "stage1" / "assets"


def footprints(frames_bin: str, frame: int):
    """Cluster the sprite entries of one frame into actor-sized boxes."""
    sat = {f["frame"]: f for f in read_frames(frames_bin)}[frame]
    boxes = []
    for e in entries(sat["sat"]):
        if not e["tile"] or e["w"] > 4 or e["h"] > 4:
            continue
        x, y = e["x"] - 128, e["y"] - 128
        if not (-8 <= x < 320 and 40 <= y < 224):
            continue
        boxes.append((x, y, x + e["w"] * 8, y + e["h"] * 8))
    # merge overlapping boxes into actors
    merged = []
    for b in boxes:
        for m in merged:
            if not (b[2] < m[0] or b[0] > m[2] or b[3] < m[1] or b[1] > m[3]):
                m[0] = min(m[0], b[0]); m[1] = min(m[1], b[1])
                m[2] = max(m[2], b[2]); m[3] = max(m[3], b[3])
                break
        else:
            merged.append(list(b))
    return [tuple(m) for m in merged]


def keep_main_components(img, min_px=60):
    """Drop stray opaque specks: keep connected blobs of at least min_px.

    Background pixels that happened to differ from the plate come out as isolated
    dots; a character is one large connected blob (or a few, e.g. a fist detached
    by an outline gap).
    """
    w, h = img.size
    op = [[img.getpixel((x, y))[3] > 0 for x in range(w)] for y in range(h)]
    seen = [[False] * w for _ in range(h)]
    blobs = []
    for y in range(h):
        for x in range(w):
            if not op[y][x] or seen[y][x]:
                continue
            stack = [(x, y)]
            seen[y][x] = True
            blob = []
            while stack:
                cx, cy = stack.pop()
                blob.append((cx, cy))
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)):
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < w and 0 <= ny < h and op[ny][nx] and not seen[ny][nx]:
                        seen[ny][nx] = True
                        stack.append((nx, ny))
            blobs.append(blob)
    if not blobs:
        return None
    biggest = max(len(b) for b in blobs)
    keep = set()
    for b in blobs:
        if len(b) >= max(min_px, biggest * 0.12):
            keep.update(b)
    out = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    for (x, y) in keep:
        out.putpixel((x, y), img.getpixel((x, y)))
    return out


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--frame-ppm", required=True)
    ap.add_argument("--frames-bin", required=True)
    ap.add_argument("--frame", type=int, required=True)
    ap.add_argument("--plate", default=str(OUT / "plate.png"))
    ap.add_argument("--prefix", default="actor")
    ap.add_argument("--min-pixels", type=int, default=300)
    args = ap.parse_args()

    w, h, px = read_ppm(args.frame_ppm)
    plate = Image.open(args.plate).convert("RGB")
    pld = plate.load()

    boxes = footprints(args.frames_bin, args.frame)
    print(f"{len(boxes)} actor footprints at frame {args.frame}: {boxes}")
    made = []
    for i, (x0, y0, x1, y1) in enumerate(boxes):
        x0, y0 = max(0, x0), max(0, y0)
        x1, y1 = min(w, x1), min(h, y1)
        if x1 - x0 < 8 or y1 - y0 < 8:
            continue
        img = Image.new("RGBA", (x1 - x0, y1 - y0), (0, 0, 0, 0))
        kept = 0
        for y in range(y0, y1):
            for x in range(x0, x1):
                i2 = (y * w + x) * 3
                pc = pld[x, y]
                d = sum(abs(px[i2 + k] - pc[k]) for k in range(3))
                if d > 30:
                    img.putpixel((x - x0, y - y0), (px[i2], px[i2 + 1], px[i2 + 2], 255))
                    kept += 1
        if kept < args.min_pixels:
            print(f"  footprint {i} at {(x0, y0)} kept only {kept} px, skipped")
            continue
        img = keep_main_components(img)
        if img is None:
            print(f"  footprint {i} produced no solid component, skipped")
            continue
        bb = img.getbbox()
        if bb:
            img = img.crop(bb)
        name = f"{args.prefix}{i}"
        img.save(OUT / f"{name}.png")
        made.append((name, img.size, kept))
        print(f"  {name}: {img.size} opaque={kept} from box {(x0, y0, x1, y1)}")
    return 0 if made else 1


if __name__ == "__main__":
    raise SystemExit(main())
