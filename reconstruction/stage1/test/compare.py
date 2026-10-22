"""Compare a reconstruction render with the original game's frame.

Reports numbers only, with no rescaling or shifting to make the match look better:
the two images are compared at their native 320x224 size, aligned by the camera
position the reconstruction reports.

    python3 reconstruction/stage1/test/compare.py <original.ppm> <recon.png> [--camera N]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from tools.ppm import read_ppm   # noqa: E402
from PIL import Image            # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("original")
    ap.add_argument("recon")
    ap.add_argument("--report", default=None)
    args = ap.parse_args()

    w, h, opx = read_ppm(args.original)
    rec = Image.open(args.recon).convert("RGB")
    if rec.size != (w, h):
        print(f"size mismatch: original {w}x{h}, reconstruction {rec.size}")
        return 2
    rpx = rec.tobytes()

    total = w * h
    diff = 0
    diff_env = 0      # rows above the action area
    diff_action = 0
    rows = [0] * h
    for y in range(h):
        for x in range(w):
            i = (y * w + x) * 3
            if opx[i:i + 3] != rpx[i:i + 3]:
                diff += 1
                rows[y] += 1
                if y < 168:
                    diff_env += 1
                else:
                    diff_action += 1

    print(f"compared pixels      {total}")
    print(f"differing pixels     {diff} ({100 * diff / total:.2f}%)")
    print(f"  environment rows   {diff_env}")
    print(f"  action rows        {diff_action}")
    worst = sorted(range(h), key=lambda y: -rows[y])[:5]
    print(f"worst rows (y, differing px): {[(y, rows[y]) for y in worst]}")

    # difference image: magenta where they disagree
    out = Image.new("RGB", (w, h))
    px = out.load()
    for y in range(h):
        for x in range(w):
            i = (y * w + x) * 3
            same = opx[i:i + 3] == rpx[i:i + 3]
            px[x, y] = (0, 0, 0) if same else (255, 0, 255)
    dst = Path(args.report) if args.report else Path(args.recon).with_suffix(".diff.png")
    out.save(dst)
    print(f"difference image      {dst}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
