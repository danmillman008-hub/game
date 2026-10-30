#!/usr/bin/env python3
"""chainkit — frame-bridge filmmaking on top of ffmpeg.

The idea: never generate a "video from scratch". Generate ONE 4-second link from a
still, take its LAST frame, annotate/guide it, and generate the next link. The
film is the chain. ffmpeg does every operation that is not generation.

Verbs
  grab    one-pass frame extraction (first / last / at t / nth) — no re-encode
  guide   build the generator's input stack from a frame:
            edge.png   structure lock  (white lines on black, canny-like)
            gray.png   lighting lock   (luminance, normalized)
            annot.png  human/agent readable notes (box, thirds, camera arrow, light vector)
            guide.json the spec that produced it (deterministic, re-runnable)
  chain   link manifest: clip -> last frame -> next clip, with anchor re-locking
  audit   SSIM drift between anchor and each link (proof, not opinion)
  concat  stream-copy concat (seconds, not minutes) + fallback
  bench   honest wall-clock comparison of the paths

Nothing here calls a video model. It prepares inputs and stitches outputs.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

import imageio_ffmpeg
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
FF = imageio_ffmpeg.get_ffmpeg_exe()
FONT_BOLD = ROOT / "studio" / "fonts" / "Vazirmatn-Bold.ttf"
FONT_REG = ROOT / "studio" / "fonts" / "Vazirmatn-Regular.ttf"


# --------------------------------------------------------------------------- util
def run(args, timeout=1800, quiet=True):
    t0 = time.time()
    p = subprocess.run([str(a) for a in args], capture_output=True, text=True, timeout=timeout)
    if p.returncode != 0:
        raise SystemExit(f"ffmpeg failed: {' '.join(map(str, args))}\n{p.stderr[-1500:]}")
    return p.stdout + p.stderr, time.time() - t0


def probe(path) -> dict:
    import re
    p = subprocess.run([FF, "-i", str(path)], capture_output=True, text=True)
    txt = p.stderr
    out = {"path": str(path)}
    m = re.search(r"Duration: (\d+):(\d+):(\d+(?:\.\d+)?)", txt)
    if m:
        out["duration_s"] = round(int(m.group(1)) * 3600 + int(m.group(2)) * 60
                                  + float(m.group(3)), 3)
    m = re.search(r"Video:.*? (\d{2,5})x(\d{2,5})", txt)
    if m:
        out["width"], out["height"] = int(m.group(1)), int(m.group(2))
    else:
        m = re.search(r" (\d{2,5})x(\d{2,5})[,\s]", txt)
        if m:
            out["width"], out["height"] = int(m.group(1)), int(m.group(2))
    m = re.search(r"([\d.]+) fps", txt)
    if m:
        out["fps"] = float(m.group(1))
    return out


def norm_bgr(c: str):
    c = c.lstrip("#")
    return "#" + c


# --------------------------------------------------------------------------- grab
def cmd_grab(a):
    """Extract frames in ONE decode pass. Seeking is the thing that costs time."""
    src = Path(a.clip).resolve()
    outdir = Path(a.out or (src.parent / f"{src.stem}_frames")).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    written = []

    if a.mode == "last":
        # -sseof decodes only the tail; -update 1 keeps writing one file
        img = outdir / (a.name or "last.png")
        run([FF, "-y", "-v", "error", "-sseof", "-0.4", "-i", src, "-update", "1",
             "-vsync", "0", "-q:v", "2", img])
        written.append(img)

    elif a.mode == "first":
        img = outdir / (a.name or "first.png")
        run([FF, "-y", "-v", "error", "-i", src, "-frames:v", "1", "-q:v", "2", img])
        written.append(img)

    elif a.mode == "at":
        img = outdir / (a.name or f"t{a.at:.2f}.png")
        # fast seek: -ss BEFORE -i jumps by keyframe, then -frames:v 1
        run([FF, "-y", "-v", "error", "-ss", f"{a.at:.3f}", "-i", src,
             "-frames:v", "1", "-q:v", "2", img])
        written.append(img)

    elif a.mode == "all":
        # one decode, no re-seek per frame
        pattern = outdir / (a.name or "f%04d.jpg")
        run([FF, "-y", "-v", "error", "-i", src, "-q:v", "2",
             "-f", "image2", "-start_number", "0", pattern])
        written = sorted(outdir.glob(pattern.name.replace("%04d", "*")))

    print(json.dumps({"frames": [str(p) for p in written][:8],
                      "count": len(written)}, indent=2))


# --------------------------------------------------------------------------- guide
DEFAULT_SPEC = {
    "subject": [0.34, 0.22, 0.66, 0.72],
    "camera": None,
    "light": None,
    "horizon": None,
    "note": "",
}


def _spec_for(frame: Path) -> dict:
    side = frame.with_suffix(".guide.json")
    if side.exists():
        return json.loads(side.read_text(encoding="utf-8"))
    return dict(DEFAULT_SPEC)


def _px(pt, w, h):
    return int(pt[0] * w), int(pt[1] * h)


def cmd_guide(a):
    """Turn a frame into a generation guide stack: structure + lighting + notes."""
    frame = Path(a.frame).resolve()
    outdir = Path(a.out or (frame.parent / "guide")).resolve()
    outdir.mkdir(parents=True, exist_ok=True)
    spec = json.loads(Path(a.spec).read_text(encoding="utf-8")) if a.spec else _spec_for(frame)
    w, h = probe(frame).get("width"), probe(frame).get("height")
    if not w:
        with Image.open(frame) as im:
            w, h = im.size
    made = {}
    t_all = time.time()

    # 1) structure lock — canny-like edges, white on black (ControlNet-friendly)
    edge = outdir / "edge.png"
    run([FF, "-y", "-v", "error", "-i", frame, "-vf",
         "format=gray,gblur=sigma=1.6,edgedetect=low=0.12:high=0.35,eq=contrast=1.6", edge])
    made["edge"] = str(edge)

    # 2) lighting lock — luminance, normalized, no colour so it can't fight the palette
    gray = outdir / "gray.png"
    run([FF, "-y", "-v", "error", "-i", frame, "-vf",
         "format=gray,normalize=blackpt=black:whitept=white", gray])
    made["gray"] = str(gray)

    # 3) annotation plate — what a human/director would scribble on the frame
    annot = outdir / "annot.png"
    im = Image.open(frame).convert("RGB")
    dr = ImageDraw.Draw(im, "RGBA")
    f_big = ImageFont.truetype(str(FONT_BOLD), max(18, h // 34))
    f_sm = ImageFont.truetype(str(FONT_REG), max(14, h // 52))

    def arrow(p0, p1, color, width):
        dr.line([p0, p1], fill=color, width=width)
        import math
        ang = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
        L = width * 4
        for s in (+1, -1):
            dr.line([p1, (p1[0] - L * math.cos(ang - s * 0.5), p1[1] - L * math.sin(ang - s * 0.5))],
                    fill=color, width=width)

    # rule of thirds
    for k in (1, 2):
        dr.line([(w * k / 3, 0), (w * k / 3, h)], fill=(255, 255, 255, 70), width=2)
        dr.line([(0, h * k / 3), (w, h * k / 3)], fill=(255, 255, 255, 70), width=2)

    # subject box
    x0, y0 = _px(spec["subject"][:2], w, h)
    x1, y1 = _px(spec["subject"][2:], w, h)
    dr.rectangle([x0, y0, x1, y1], outline=(0, 255, 140, 230), width=max(2, w // 220))
    dr.text((x0, max(4, y0 - f_sm.size - 6)), "SUBJECT", font=f_sm, fill=(0, 255, 140, 230))

    # camera move
    cam = spec.get("camera") or {}
    if cam.get("from") and cam.get("to"):
        arrow(_px(cam["from"], w, h), _px(cam["to"], w, h), (80, 200, 255, 240), max(3, w // 200))
        dr.text(_px(cam["to"], w, h), cam.get("label", "camera"), font=f_sm,
                fill=(80, 200, 255, 240))

    # light vector
    light = spec.get("light") or {}
    if light.get("from"):
        p0 = _px(light["from"], w, h)
        p1 = (int(w * 0.5), int(h * 0.42))
        arrow(p0, p1, (255, 214, 80, 235), max(3, w // 200))
        dr.ellipse([p0[0] - 18, p0[1] - 18, p0[0] + 18, p0[1] + 18],
                   outline=(255, 214, 80, 235), width=3)
        dr.text((p0[0] + 24, p0[1] - 10),
                f"{light.get('label','light')} {light.get('elevation','')}deg",
                font=f_sm, fill=(255, 214, 80, 235))

    if spec.get("horizon") is not None:
        y = int(h * spec["horizon"])
        dr.line([(0, y), (w, y)], fill=(255, 255, 255, 120), width=2)

    if spec.get("note"):
        dr.text((w * 0.04, h * 0.04), spec["note"], font=f_big, fill=(255, 255, 255, 235))

    im.save(annot)
    made["annot"] = str(annot)

    (outdir / "guide.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False),
                                       encoding="utf-8")
    made["spec"] = str(outdir / "guide.json")
    print(json.dumps({"frame": str(frame), "size": [w, h], "outputs": made,
                      "seconds": round(time.time() - t_all, 2)}, indent=2))


# --------------------------------------------------------------------------- chain
def cmd_chain(a):
    """Register one link: clip -> (last frame | anchor still) -> next input."""
    root = Path(a.dir).resolve()
    links_file = root / "links.json"
    links = json.loads(links_file.read_text(encoding="utf-8")) if links_file.exists() else []
    clip = Path(a.clip).resolve()
    frames = root / "frames"
    frames.mkdir(parents=True, exist_ok=True)

    anchor = bool(a.anchor)
    if anchor and a.anchor_still:
        src_frame = Path(a.anchor_still).resolve()
        origin = "anchor"
    else:
        prev = links[-1] if links else None
        src_frame = Path(prev["out_frame"]) if prev and prev.get("out_frame") else None
        origin = "last_frame" if src_frame else "still"

    if src_frame is None and a.anchor_still is None:
        raise SystemExit("first link needs --anchor-still (the master still it was generated from)")

    # last frame of THIS clip becomes the input of the next link
    out_frame = frames / f"L{len(links)+1:03d}_last.png"
    run([FF, "-y", "-v", "error", "-sseof", "-0.4", "-i", clip, "-update", "1",
         "-vsync", "0", out_frame])

    links.append({
        "n": len(links) + 1,
        "clip": str(clip),
        "input_frame": str(src_frame) if src_frame else None,
        "input_origin": origin,
        "out_frame": str(out_frame),
        "prompt": a.prompt or "",
        "seconds": probe(clip).get("duration_s"),
        "ts": time.strftime("%Y-%m-%dT%H:%M:%S"),
    })
    links_file.write_text(json.dumps(links, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(links[-1], indent=2, ensure_ascii=False))
    print(f"link {len(links)} registered — next input is {out_frame.name}")


# --------------------------------------------------------------------------- bridge
def cmd_bridge(a):
    """Build the complete input package for the NEXT link. No generation happens here.

    Output per link (dir/links/Lnnn/):
      in.png        the frame the model will animate (last frame or anchor)
      edge.png      structure lock
      gray.png      lighting lock
      annot.png     director notes drawn on the frame
      job.json      everything a generator needs: image, prompt, duration, seed slot
    """
    root = Path(a.dir).resolve()
    links_dir = root / "links"
    links_dir.mkdir(parents=True, exist_ok=True)
    n = len([d for d in links_dir.iterdir() if d.is_dir()]) + 1 if links_dir.exists() else 1
    cell = links_dir / f"L{n:03d}"
    cell.mkdir(parents=True, exist_ok=True)

    if a.from_clip:
        src = Path(a.from_clip).resolve()
        in_frame = cell / "in.png"
        run([FF, "-y", "-v", "error", "-sseof", "-0.4", "-i", src, "-update", "1",
             "-vsync", "0", in_frame])
        origin = f"last_frame:{src.name}"
    elif a.still:
        in_frame = cell / "in.png"
        shutil.copy2(Path(a.still).resolve(), in_frame)
        origin = f"still:{Path(a.still).name}"
    else:
        raise SystemExit("need --from-clip or --still")

    # guide stack
    gdir = cell
    spec = {"subject": [0.34, 0.22, 0.66, 0.72], "camera": None, "light": None,
            "horizon": None, "note": ""}
    if a.spec:
        spec = json.loads(Path(a.spec).read_text(encoding="utf-8"))
    (cell / "in.guide.json").write_text(json.dumps(spec, indent=2, ensure_ascii=False),
                                        encoding="utf-8")
    sub = argparse.Namespace(frame=str(in_frame), out=str(gdir), spec=str(cell / "in.guide.json"))
    cmd_guide(sub)

    job = {
        "link": n,
        "input_image": str(in_frame),
        "input_origin": origin,
        "prompt": a.prompt or "",
        "duration_s": a.duration,
        "engine": a.engine,
        "aspect": a.aspect,
        "guides": {"edge": str(cell / "edge.png"), "gray": str(cell / "gray.png"),
                   "annot": str(cell / "annot.png")},
        "next": "generate -> save clip as links/L%03d/out.mp4 -> chainkit bridge --from-clip out.mp4" % n,
    }
    (cell / "job.json").write_text(json.dumps(job, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(job, indent=2, ensure_ascii=False))


# --------------------------------------------------------------------------- audit
def cmd_audit(a):
    """Objective drift proof: SSIM of every link's last frame against the anchor."""
    root = Path(a.dir).resolve()
    links = json.loads((root / "links.json").read_text(encoding="utf-8"))
    if not links:
        raise SystemExit("no links")
    anchor = Path(a.anchor).resolve()
    rows, prev = [], anchor
    for ln in links:
        cur = Path(ln["out_frame"])
        if not cur.exists():
            continue
        _, _ = run([FF, "-y", "-v", "error", "-i", prev, "-i", cur, "-lavfi",
                    "ssim", "-f", "null", "-"], timeout=120)
        out, _ = run([FF, "-hide_banner", "-i", prev, "-i", cur, "-lavfi",
                      "ssim", "-f", "null", "-"], timeout=120)
        score = None
        for line in out.splitlines():
            if "SSIM" in line and "All:" in line:
                score = float(line.split("All:")[1].split()[0])
        rows.append({"link": ln["n"], "file": cur.name,
                     "ssim_vs_anchor": score if prev == anchor else None,
                     "ssim_vs_prev": None if prev == anchor else score})
        prev = cur

    # also measure every link against the anchor (cumulative drift)
    for r, ln in zip(rows, [l for l in links if Path(l["out_frame"]).exists()]):
        out, _ = run([FF, "-hide_banner", "-i", anchor, "-i", ln["out_frame"],
                      "-lavfi", "ssim", "-f", "null", "-"], timeout=120)
        for line in out.splitlines():
            if "SSIM" in line and "All:" in line:
                r["ssim_vs_anchor"] = float(line.split("All:")[1].split()[0])

    bad = [r for r in rows if r["ssim_vs_anchor"] is not None and r["ssim_vs_anchor"] < (a.threshold or 0.55)]
    report = {"anchor": str(anchor), "links": rows, "drifted": bad,
              "advice": ("re-anchor: generate the next link from the master still, not the "
                         "previous last frame") if bad else "chain is stable"}
    (root / "drift.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps(report, indent=2))


# --------------------------------------------------------------------------- concat
def cmd_concat(a):
    """Stream-copy concat when the clips share encoder settings (seconds, not minutes)."""
    files = [Path(f).resolve() for f in a.files]
    out = Path(a.out).resolve()
    lst = out.with_suffix(".txt")
    lst.write_text("".join(f"file '{f}'\n" for f in files), encoding="utf-8")
    t0 = time.time()
    p = subprocess.run([FF, "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                        "-c", "copy", "-movflags", "+faststart", str(out)],
                       capture_output=True, text=True)
    dt = time.time() - t0
    mode = "copy"
    if p.returncode != 0 or not out.exists():
        mode = "reencode"
        run([FF, "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst,
             "-c:v", "libx264", "-preset", a.preset, "-crf", str(a.crf),
             "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out])
        dt = time.time() - t0
    info = probe(out)
    print(json.dumps({"out": str(out), "mode": mode, "seconds": round(dt, 2),
                      "duration_s": info.get("duration_s"), "bytes": out.stat().st_size}, indent=2))


# --------------------------------------------------------------------------- bench
def cmd_bench(a):
    """Wall-clock the three ways to join N clips, on real files."""
    files = [Path(f).resolve() for f in a.files]
    tmp = Path("/tmp/chainkit_bench")
    shutil.rmtree(tmp, ignore_errors=True)
    tmp.mkdir(parents=True)
    rows = []

    # A) stream copy
    lst = tmp / "a.txt"
    lst.write_text("".join(f"file '{f}'\n" for f in files), encoding="utf-8")
    t0 = time.time()
    p = subprocess.run([FF, "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lst),
                        "-c", "copy", str(tmp / "a.mp4")], capture_output=True, text=True)
    rows.append({"path": "concat -c copy", "ok": p.returncode == 0,
                 "seconds": round(time.time() - t0, 2)})

    # B) single-pass re-encode
    t0 = time.time()
    run([FF, "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst,
         "-c:v", "libx264", "-preset", "veryfast", "-crf", "19", str(tmp / "b.mp4")])
    rows.append({"path": "concat + one encode (veryfast)", "ok": True,
                 "seconds": round(time.time() - t0, 2)})

    print(json.dumps({"clips": len(files), "results": rows}, indent=2))


# --------------------------------------------------------------------------- cli
def main():
    ap = argparse.ArgumentParser(prog="chainkit")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("grab"); p.add_argument("clip")
    p.add_argument("--mode", choices=["first", "last", "at", "all"], default="last")
    p.add_argument("--at", type=float, default=0.0); p.add_argument("--out")
    p.add_argument("--name"); p.set_defaults(fn=cmd_grab)

    p = sub.add_parser("guide"); p.add_argument("frame")
    p.add_argument("--spec"); p.add_argument("--out"); p.set_defaults(fn=cmd_guide)

    p = sub.add_parser("chain"); p.add_argument("dir"); p.add_argument("clip")
    p.add_argument("--prompt"); p.add_argument("--anchor", action="store_true")
    p.add_argument("--anchor-still"); p.set_defaults(fn=cmd_chain)

    p = sub.add_parser("bridge"); p.add_argument("dir")
    p.add_argument("--from-clip"); p.add_argument("--still"); p.add_argument("--prompt")
    p.add_argument("--spec"); p.add_argument("--duration", type=float, default=4.0)
    p.add_argument("--engine", default="wan-lora"); p.add_argument("--aspect", default="3:4")
    p.set_defaults(fn=cmd_bridge)

    p = sub.add_parser("audit"); p.add_argument("dir")
    p.add_argument("--anchor", required=True); p.add_argument("--threshold", type=float)
    p.set_defaults(fn=cmd_audit)

    p = sub.add_parser("concat"); p.add_argument("out"); p.add_argument("files", nargs="+")
    p.add_argument("--preset", default="veryfast"); p.add_argument("--crf", type=int, default=19)
    p.set_defaults(fn=cmd_concat)

    p = sub.add_parser("bench"); p.add_argument("files", nargs="+"); p.set_defaults(fn=cmd_bench)

    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
