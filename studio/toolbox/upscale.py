#!/usr/bin/env python3
"""upscale.py — the missing tool: a real anime upscaler, on CPU.

Why this exists: every quality complaint in this project traces back to one number.
The character sheets are 300x499. The model is given a 300 px drawing and asked to
invent a film from it — so it invents a soft, flat world. No prompt fixes that. The
input has to be clean first.

Two engines, both verified on GitHub today:

    pyanime4k      TianZerL/pyanime4k        122*  MIT      CPU (Anime4KCPP)   fast
    realesrgan     xinntao/Real-ESRGAN    37,280*  BSD-3    CPU, slow          better on flat art

Anime4K is an edge-directed upscaler written for cel animation: it sharpens the ink
line and keeps flat fields flat instead of hallucinating texture. Real-ESRGAN's
`x4plus_anime_6B` was trained on anime illustrations and is stronger but heavier.

    python3 studio/toolbox/upscale.py refs --scale 4          # sheets -> 4x
    python3 studio/toolbox/upscale.py refs --engine realesrgan
    python3 studio/toolbox/upscale.py compare --src films/anime_ten/refs/c1.png
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import time
from pathlib import Path

from PIL import Image, ImageFilter, ImageStat

ROOT = Path(__file__).resolve().parent.parent.parent


def sharpness(p: Path) -> float:
    """Laplacian-energy proxy: higher = crisper lines. No OpenCV needed."""
    im = Image.open(p).convert("L")
    if max(im.size) > 1200:
        im = im.resize((im.width // 2, im.height // 2))
    lap = im.filter(ImageFilter.FIND_EDGES)
    return round(ImageStat.Stat(lap).var[0] ** 0.5, 2)


# ------------------------------------------------------------------ engines ---
def anime4k(src: Path, dst: Path, scale: int = 4) -> None:
    import pyanime4k
    img = pyanime4k.upscale(scale, "cpu", str(src), str(dst))
    if img is False or not dst.exists():
        # older API: run() with explicit args
        pyanime4k.run(scale, "cpu", str(src), str(dst))


def realesrgan(src: Path, dst: Path, scale: int = 4) -> None:
    import numpy as np
    import torch
    from basicsr.archs.rrdbnet_arch import RRDBNet
    from realesrgan import RealESRGANer
    from PIL import Image as I

    model = RRDBNet(num_in_ch=3, num_out_ch=3, num_feat=64, num_block=6,
                    num_grow_ch=32, scale=4)          # x4plus_anime_6B
    w = ROOT / "studio" / "toolbox" / "weights" / "RealESRGAN_x4plus_anime_6B.pth"
    up = RealESRGANer(scale=4, model_path=str(w), model=model, tile=256,
                      tile_pad=10, pre_pad=0, half=False, device=torch.device("cpu"))
    out, _ = up.enhance(np.array(I.open(src).convert("RGB")), outscale=scale)
    I.fromarray(out).save(dst)


ENGINES = {"anime4k": anime4k, "realesrgan": realesrgan}


# ------------------------------------------------------------------ commands --
def cmd_refs(a) -> int:
    srcs = sorted((ROOT / "films" / "anime_ten" / "refs").glob("*.png"))
    out = ROOT / "films" / "anime_ten" / "refs_hi"
    out.mkdir(parents=True, exist_ok=True)
    fn = ENGINES[a.engine]
    rows = []
    for s in srcs:
        dst = out / s.name
        t0 = time.time()
        before = sharpness(s)
        if dst.exists() and not a.force:
            print(f"  {s.name}: exists, skip")
        else:
            try:
                fn(s, dst, a.scale)
            except Exception as e:                    # noqa: BLE001
                print(f"  {s.name}: FAILED {type(e).__name__}: {e}")
                continue
            print(f"  {s.name}: {Image.open(s).size} -> {Image.open(dst).size} "
                  f"in {time.time() - t0:.0f}s")
        rows.append((s.name, before, sharpness(dst)))
    print(f"\n{'file':10s} {'sharp before':>13s} {'after':>8s} {'x':>6s}")
    for n, b, aft in rows:
        print(f"{n:10s} {b:>13.2f} {aft:>8.2f} {aft / max(b, 1e-6):>6.2f}")
    return 0


def cmd_compare(a) -> int:
    src = Path(a.src)
    out = ROOT / "probe_out" / "upscale"
    out.mkdir(parents=True, exist_ok=True)
    print(f"source {src} {Image.open(src).size} sharp {sharpness(src)}")
    for name, fn in ENGINES.items():
        dst = out / f"{src.stem}_{name}.png"
        t0 = time.time()
        try:
            fn(src, dst, a.scale)
        except Exception as e:                        # noqa: BLE001
            print(f"  {name:10s} FAILED {type(e).__name__}: {e}")
            continue
        print(f"  {name:10s} {Image.open(dst).size} sharp {sharpness(dst)} "
              f"in {time.time() - t0:.0f}s")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(prog="upscale", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("refs"); p.add_argument("--scale", type=int, default=4)
    p.add_argument("--engine", default="anime4k", choices=list(ENGINES))
    p.add_argument("--force", action="store_true"); p.set_defaults(fn=cmd_refs)
    p = sub.add_parser("compare"); p.add_argument("--src", required=True)
    p.add_argument("--scale", type=int, default=4); p.set_defaults(fn=cmd_compare)
    a = ap.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    raise SystemExit(main())
