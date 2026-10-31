#!/usr/bin/env python3
"""artgen.py — use the video model as the image model.

The sandbox cannot draw (the image tool returns 403) and Mivi's picture endpoint wants
a `token` that is not in the app code. But we do not need either: the video model
already proved it will *repaint* a nearly empty input. Feed it a blank canvas plus a
full-scene prompt and frame 0 comes back as a finished key frame — and frames 1-96
come back as the shot. One generation, both artefacts.

    python3 studio/artgen.py canvas                     # write the blank canvases
    python3 studio/artgen.py jobs art_prompts.json      # -> gen_jobs_art.json
    # (dispatch: printf 'films/short16/gen_jobs_art.json\\n' > .mivi-trigger)
    python3 studio/artgen.py extract                    # frame 0 of each clip -> art/

Why a blank canvas and not a photo: a blank field is the least opinionated input we
can give. The prompt then has nothing to fight. Measured earlier: a flat 11-colour
plate came back as a fully painted city in 4 s — so an empty gradient should hand the
model the whole frame.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageStat

ROOT = Path(__file__).resolve().parent.parent
FILM = ROOT / "films" / "anime_ten"
CANVAS = FILM / "canvas"
ART = FILM / "art"
CLIPS = ROOT / "films" / "short16" / "clips_gen"
W, H = 960, 1280


def ffmpeg() -> str:
    sys.path.insert(0, str(ROOT / "studio"))
    import filmkit
    return filmkit.ffmpeg_bin()


# ------------------------------------------------------------------ canvases --
def make_canvases() -> list[Path]:
    """Four neutral fields. No shapes, no text — anything drawn here becomes a prop
    the model tries to explain (the white bar on c1 became a sword once)."""
    CANVAS.mkdir(parents=True, exist_ok=True)
    out: list[Path] = []

    dusk = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(dusk)
    for y in range(H):
        t = y / H
        if t < 0.55:
            c = (28 + int(10 * t), 34 + int(14 * t), 66 + int(24 * t))
        else:
            u = (t - 0.55) / 0.45
            c = (42 + int(120 * u), 48 + int(52 * u), 90 + int(-20 * u))
        d.line([(0, y), (W, y)], fill=c)
    dusk.filter(ImageFilter.GaussianBlur(2)).save(CANVAS / "dusk.png")
    out.append(CANVAS / "dusk.png")

    night = Image.new("RGB", (W, H), (22, 26, 38))
    for i in range(120):                     # faint stars, no shapes a model can latch on
        night.putpixel(((i * 97) % W, (i * 233) % int(H * 0.5)), (120, 130, 150))
    night.save(CANVAS / "night.png")
    out.append(CANVAS / "night.png")

    # Snow at night needs its own field: `night` (22,26,38) is a summer sky, and four
    # winter anchors painted on it came back at mean luminance 24-29 — a black frame
    # that reads as "the model did nothing". snow is dark enough for lanterns to read
    # and light enough that the frame has an exposure.
    snow = Image.new("RGB", (W, H))
    ds = ImageDraw.Draw(snow)
    for y in range(H):
        t = y / H
        c = (int(64 + 26 * t), int(74 + 26 * t), int(104 + 22 * t))
        ds.line([(0, y), (W, y)], fill=c)
    snow.filter(ImageFilter.GaussianBlur(3)).save(CANVAS / "snow.png")
    out.append(CANVAS / "snow.png")

    paper = Image.new("RGB", (W, H), (238, 234, 226))
    paper.save(CANVAS / "paper.png")
    out.append(CANVAS / "paper.png")
    return out


# ---------------------------------------------------------------------- jobs --
def cmd_jobs(a) -> int:
    prompts = json.loads(Path(a.file).read_text(encoding="utf-8"))
    shots = []
    for p in prompts:
        canvas = p.get("canvas", "dusk")
        c = CANVAS / f"{canvas}.png"
        if not c.exists():
            make_canvases()
        shots.append({"id": p["id"], "still": str(c.relative_to(ROOT)), "attempts": 1,
                      "prompt": p["prompt"], "model": p.get("model", "mivi-gx-720p"),
                      "quality": p.get("quality", 2)})
    out = ROOT / "films/short16/gen_jobs_art.json"
    out.write_text(json.dumps({"shots": shots}, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"{len(shots)} art jobs -> {out.relative_to(ROOT)}")
    for s in shots:
        print(f"  {s['id']:14s} canvas={Path(s['still']).stem:7s} {s['prompt'][:60]}")
    return 0


# ------------------------------------------------------------------- extract --
def sharpness(p: Path, norm: int = 1000) -> float:
    im = Image.open(p).convert("L")
    h = max(1, int(im.height * norm / im.width))
    im = im.resize((norm, h), Image.LANCZOS)
    return round(ImageStat.Stat(im.filter(ImageFilter.FIND_EDGES)).var[0] ** 0.5, 2)


def palette(p: Path) -> int:
    im = Image.open(p).convert("RGB").resize((240, 320))
    from PIL import ImageOps
    return len(ImageOps.posterize(im, 5).getcolors(1 << 20) or [])


def cmd_frames(a) -> int:
    """Frame 0 of every clip in a batch, written next to the clips.

    The first frame is the anchor for the *next* batch — and it must be checked before
    it is trusted. On 2026-10-31 four winter anchors came back as an almost black
    field (the night canvas is dark, so mean luminance was the only thing that said
    so) and every shot built on them would have been a shot of nothing.
    """
    batch = [x.strip() for x in a.ids.split(",")] if a.ids else []
    clips = [CLIPS / f"{i}_a1.mp4" for i in batch] if batch else sorted(CLIPS.glob("art_*.mp4"))
    rows = []
    for clip in clips:
        if not clip.exists():
            print(f"missing {clip.name}")
            continue
        dst = clip.with_name(clip.stem.replace("_a1", "") + "_src.png")
        subprocess.run([ffmpeg(), "-y", "-v", "error", "-ss", "0.15", "-i", str(clip),
                        "-frames:v", "1", str(dst)], check=True)
        im = Image.open(dst).convert("L")
        mean = round(ImageStat.Stat(im).mean[0], 1)
        rows.append((dst.name, mean, sharpness(dst)))
    print(f"{'anchor':26s} {'mean':>6s} {'sharp':>7s}")
    dark = 0
    for n, m, sh in rows:
        flag = "  <-- TOO DARK, do not use" if m < a.min_mean else ""
        dark += bool(flag)
        print(f"{n:26s} {m:>6.1f} {sh:>7.2f}{flag}")
    if rows:
        print(f"\n{len(rows)} anchors · {dark} too dark (min mean {a.min_mean})")
    return 1 if dark else 0


def cmd_extract(a) -> int:
    """Frame 0 is the artwork; frame -1 is the end of the shot. Both are kept."""
    ART.mkdir(parents=True, exist_ok=True)
    rows = []
    for clip in sorted(CLIPS.glob("art_*.mp4")):
        first = ART / f"{clip.stem}_f0.png"
        last = ART / f"{clip.stem}_fN.png"
        for t, dst in ((0.15, first), (a.last_t, last)):
            subprocess.run([ffmpeg(), "-y", "-v", "error", "-ss", f"{t}",
                            "-i", str(clip), "-frames:v", "1", str(dst)], check=True)
        rows.append((clip.stem, sharpness(first), palette(first), first.name))
    print(f"{'clip':22s} {'sharp':>7s} {'palette':>8s}")
    for n, s, p, f in rows:
        print(f"{n:22s} {s:>7.2f} {p:>8d}")
    if rows:
        print(f"\nmean sharpness {sum(r[1] for r in rows) / len(rows):.1f} · "
              f"mean palette {sum(r[2] for r in rows) // len(rows)} colours")
    print(f"frames -> {(ART).relative_to(ROOT)}/")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(prog="artgen", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("canvas").set_defaults(fn=lambda a: (make_canvases(), 0)[1])
    p = sub.add_parser("jobs"); p.add_argument("file"); p.set_defaults(fn=cmd_jobs)
    pf = sub.add_parser("frames", help="frame 0 of a batch -> *_src.png anchors")
    pf.add_argument("--ids", default="", help="comma separated shot ids (default: every art_*.mp4)")
    pf.add_argument("--min-mean", dest="min_mean", type=float, default=30.0,
                    help="mean luminance below which an anchor is unusable")
    pf.set_defaults(fn=cmd_frames)
    p = sub.add_parser("extract"); p.add_argument("--last-t", type=float, default=3.6)
    p.set_defaults(fn=cmd_extract)
    a = ap.parse_args()
    return a.fn(a)


if __name__ == "__main__":
    raise SystemExit(main())
