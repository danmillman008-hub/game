"""Build a wide Stage-1 backdrop by stitching real gameplay frames.

The plane-level VRAM decode is still unresolved (see RESEARCH_LOG), so the
environment art is recovered the other way round: from frames the original game
actually produced, aligned by *measured* scroll rather than assumed scroll.

Alignment: for each consecutive pair of frames, the horizontal shift is found by
maximising the agreement of a static band of rows (the shopfront band, which does
not animate). The shift is then accumulated. Nothing is scaled or filtered.

Outputs: reconstruction/stage1/assets/backdrop.png and backdrop.json (the frame
range, per-frame offsets, and the resulting world width).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.ppm import read_ppm   # noqa: E402

BAND_TOP, BAND_BOT = 100, 170     # shopfront band: below the awning, above the floor


def score(a, b, w, dx) -> int:
    """Agreement of image a shifted by dx against b, over the static band."""
    n = 0
    for y in range(BAND_TOP, BAND_BOT, 3):
        ra = (y * w) * 3
        for x in range(40, w - 40, 3):
            ia = ra + (x + dx) * 3
            ib = ra + x * 3
            if a[ia:ia + 3] == b[ib:ib + 3]:
                n += 1
    return n


def main() -> int:
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("capture")
    ap.add_argument("--first", type=int, default=14200)
    ap.add_argument("--step", type=int, default=10)
    ap.add_argument("--limit", type=int, default=140)
    ap.add_argument("--out", default=str(ROOT / "reconstruction" / "stage1" / "assets"))
    args = ap.parse_args()

    cap = Path(args.capture)
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)

    frames = []
    for fr in range(args.first, args.first + args.limit * args.step, args.step):
        p = cap / f"f{fr:04d}.ppm"
        if p.exists():
            frames.append((fr, read_ppm(p)))
    if len(frames) < 2:
        print("need at least two frames")
        return 1

    w, h, _ = frames[0][1]
    offsets, total = [(frames[0][0], 0)], 0
    prev = frames[0][1][2]
    for fr, (fw, fh, px) in frames[1:]:
        best, bestdx = -1, 0
        for dx in range(-24, 25):
            s = score(px, prev, w, dx)
            if s > best:
                best, bestdx = s, dx
        total += bestdx
        offsets.append((fr, total))
        prev = px

    lo = min(o for _, o in offsets)
    hi = max(o for _, o in offsets)
    world_w = w + (hi - lo)
    print(f"{len(frames)} frames, scroll span {lo}..{hi} -> world width {world_w}px")
    print("first offsets:", offsets[:8])

    # paint: widest frame sample wins; earliest sample kept for overlaps
    from PIL import Image
    canvas = Image.new("RGB", (world_w, h))
    filled = [[False] * world_w for _ in range(h)]
    for (fr, off), (fw, fh, px) in zip(offsets, [f[1] for f in frames]):
        img = Image.frombytes("RGB", (fw, fh), px)
        x0 = off - lo
        base = canvas.crop((x0, 0, x0 + fw, fh))
        bp = base.load()
        src = img.load()
        for y in range(h):
            row = filled[y]
            for x in range(fw):
                if not row[x0 + x]:
                    bp[x, y] = src[x, y]
                    row[x0 + x] = True
        canvas.paste(base, (x0, 0))

    canvas.save(out / "backdrop.png")
    covered = sum(sum(1 for v in row if v) for row in filled)
    (out / "backdrop.json").write_text(json.dumps({
        "width": world_w, "height": h,
        "scroll_min": lo, "scroll_max": hi,
        "offsets": offsets,
        "alignment": "measured by cross-correlation of a static band",
        "coverage": covered / (world_w * h),
    }, indent=1) + "\n")
    print(f"coverage {100*covered/(world_w*h):.1f}% -> {out/'backdrop.png'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
