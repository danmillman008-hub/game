"""Build the Stage-1 art that the browser reconstruction renders.

Two products, both derived from the original game's own output:

  plate.png   a clean background plate: the per-pixel temporal median of many
              frames at a fixed camera position. Actors, effects and HUD blinks
              are transient, so the median of the sequence is the environment.
              This is a measured composite, not an invented background.

  <name>.png  character poses, cropped from frames where that pose is on screen,
              with transparent pixels only where the pose does not cover.

Nothing is scaled, filtered or recoloured.
"""
from __future__ import annotations

import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.ppm import read_ppm   # noqa: E402
from PIL import Image            # noqa: E402

OUT = ROOT / "reconstruction" / "stage1" / "assets"


def median_plate(frames: list[str], out_name="plate.png", rows=(30, 224)) -> tuple[int, int]:
    imgs = [read_ppm(f) for f in frames]
    w, h = imgs[0][0], imgs[0][1]
    plate = Image.new("RGB", (w, h))
    px = plate.load()
    n = len(imgs)
    for y in range(h):
        for x in range(w):
            i = (y * w + x) * 3
            if y < rows[0] or y >= rows[1]:
                # HUD rows: take the most common value so blinking text vanishes
                vals = [im[2][i:i + 3] for im in imgs]
                px[x, y] = tuple(statistics.mode(vals))
            else:
                r = sorted(im[2][i] for im in imgs)[n // 2]
                g = sorted(im[2][i + 1] for im in imgs)[n // 2]
                b = sorted(im[2][i + 2] for im in imgs)[n // 2]
                px[x, y] = (r, g, b)
    plate.save(OUT / out_name)
    return w, h


def crop_pose(src: str, box, name: str, bg: str | None = None) -> dict:
    """Crop a pose; if `bg` (another frame) is given, transparent = unchanged pixels."""
    w, h, px = read_ppm(src)
    from PIL import Image as I
    img = I.frombytes("RGB", (w, h), px)
    c = img.crop(box)
    if bg:
        _, _, pb = read_ppm(bg)
        c = c.convert("RGBA")
        for y in range(c.height):
            for x in range(c.width):
                gx, gy = box[0] + x, box[1] + y
                i = (gy * w + gx) * 3
                if px[i:i + 3] == pb[i:i + 3]:
                    c.putpixel((x, y), (0, 0, 0, 0))
        bbox = c.getbbox()
        if bbox:
            c = c.crop(bbox)
    c.save(OUT / f"{name}.png")
    return {"name": name, "w": c.width, "h": c.height, "from": src, "box": list(box)}


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    frames = [f"/tmp/det1/f{fr:04d}.ppm" for fr in range(14449, 14600, 10)
              if Path(f"/tmp/det1/f{fr:04d}.ppm").exists()]
    w, h = median_plate(frames)
    print(f"plate {w}x{h} from {len(frames)} frames -> {OUT/'plate.png'}")

    # character poses, cropped by hand from inspected frames
    poses = []
    for src, box, name in [
        ("/tmp/det1/f14599.ppm", (120, 110, 205, 224), "axel_pose_a"),
        ("/tmp/det1/f14449.ppm", (120, 110, 205, 224), "axel_pose_b"),
        ("/tmp/det1/f14349.ppm", (120, 110, 205, 224), "axel_pose_c"),
    ]:
        if Path(src).exists():
            poses.append(crop_pose(src, box, name))
    print(f"{len(poses)} poses -> {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
