#!/usr/bin/env python3
"""cutlist — audio-first assembly of a short from a JSON timeline.

The timeline is written *after* the voice track exists: every segment's length is
set by its line, not the other way round. Freeze-holds absorb the last 0.1-0.3 s
instead of re-generating a clip.

Timeline JSON
[
  {"clip": "...mp4", "in": 0, "out": 4.03, "hold": 0.2,
   "vo": "...mp3", "vo_offset": 0.15, "text": "فارسی زیرنویس"},
  ...
]

Verbs
  build <timeline.json> --out out.mp4   segments -> concat(copy) -> audio -> subs -> loudnorm
  check <out.mp4> --timeline ...        shot-to-shot continuity + timing table
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

import imageio_ffmpeg
import numpy as np

FF = imageio_ffmpeg.get_ffmpeg_exe()
ROOT = Path(__file__).resolve().parent.parent
FONTS = ROOT / "studio" / "fonts"
T0 = time.time()


def stamp(msg):
    print(f"[{time.time() - T0:6.1f}s] {msg}", flush=True)


def run(args, timeout=1200):
    p = subprocess.run([str(a) for a in args], capture_output=True, text=True, timeout=timeout)
    if p.returncode != 0:
        raise SystemExit(f"ffmpeg failed: {' '.join(map(str, args))}\n{p.stderr[-1200:]}")
    return p.stderr


def dur(path) -> float:
    p = subprocess.run([FF, "-i", str(path)], capture_output=True, text=True)
    for line in p.stderr.splitlines():
        if "Duration:" in line:
            hms = line.split("Duration:")[1].split(",")[0].strip()
            h, m, s = hms.split(":")
            return round(int(h) * 3600 + int(m) * 60 + float(s), 3)
    return 0.0


def frame(path, at: str, out: Path):
    """One frame. -ss before -i = keyframe seek (fast)."""
    run([FF, "-y", "-v", "error", "-ss", at, "-i", path, "-frames:v", "1", out])
    return out


def ssim(a: Path, b: Path) -> float:
    p = subprocess.run([FF, "-hide_banner", "-i", str(a), "-i", str(b),
                        "-lavfi", "ssim", "-f", "null", "-"], capture_output=True, text=True)
    for line in p.stderr.splitlines():
        if "SSIM" in line and "All:" in line:
            return round(float(line.split("All:")[1].split()[0]), 4)
    return -1.0


def build(timeline: Path, out: Path, work: Path, bed: bool = True):
    segs = json.loads(Path(timeline).read_text(encoding="utf-8"))
    work.mkdir(parents=True, exist_ok=True)
    pieces, placed, t = [], [], 0.0

    # ---- 1. segments (trim + optional freeze-hold), one small encode each
    for i, s in enumerate(segs, 1):
        raw = work / f"seg{i:02d}.mp4"
        length = float(s.get("out", 4.03)) - float(s.get("in", 0.0))
        vf = ["scale=960:1280:force_original_aspect_ratio=increase", "crop=960:1280",
              "setsar=1", "fps=32", "format=yuv420p"]
        if s.get("hold"):
            vf.append(f"tpad=stop_mode=clone:stop_duration={float(s['hold']):.3f}")
        run([FF, "-y", "-v", "error", "-ss", s.get("in", 0), "-i", s["clip"],
             "-t", f"{length:.3f}", "-vf", ",".join(vf),
             "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", raw])
        d = dur(raw)
        pieces.append(raw)
        row = {"n": i, "file": raw.name, "path": str(raw.resolve()), "dur": d, "start": round(t, 3), "vo": s.get("vo"),
               "vo_at": round(t + float(s.get("vo_offset", 0.0)), 3) if s.get("vo") else None,
               "text": s.get("text", "")}
        placed.append(row)
        t += d
    stamp(f"segments: {len(pieces)} pieces, total {t:.2f}s")

    # ---- 2. concat by stream copy (no re-encode)
    lst = work / "list.txt"
    lst.write_text("".join(f"file '{p.resolve()}'\n" for p in pieces), encoding="utf-8")
    silent = work / "silent.mp4"
    run([FF, "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", lst,
         "-c", "copy", silent])
    stamp(f"concat -c copy -> {dur(silent):.2f}s")

    # ---- 3. audio: VO at absolute offsets + optional rain bed
    inputs = ["-f", "lavfi", "-t", f"{t:.3f}", "-i",
              "anoisesrc=color=pink:sample_rate=48000:amplitude=0.35"]
    filters, labels = [], []
    idx = 1
    for r in placed:
        if r["vo"]:
            ms = int(r["vo_at"] * 1000)
            inputs += ["-i", str(r["vo"])]
            filters.append(f"[{idx}:a]aformat=sample_fmts=fltp:sample_rates=48000:"
                           f"channel_layouts=stereo,adelay={ms}|{ms},volume=1.35[v{idx}]")
            labels.append(f"[v{idx}]")
            idx += 1
    filters.append("[0:a]highpass=f=350,lowpass=f=6000,volume=0.10[bed]")
    mix_in = "".join(labels) + ("[bed]" if bed else "")
    n_in = len(labels) + (1 if bed else 0)
    filters.append(f"{mix_in}amix=inputs={n_in}:duration=longest:normalize=0,"
                   f"aformat=channel_layouts=stereo[mix]")
    mix = work / "audio.m4a"
    run([FF, "-y", "-v", "error", *inputs, "-filter_complex", ";".join(filters),
         "-map", "[mix]", "-c:a", "aac", "-b:a", "192k", mix])
    stamp("audio bed + VO mixed")

    # ---- 4. subtitles from the same timeline (libass, Persian-safe)
    srt = work / "short.srt"
    cues = []
    for r in placed:
        if r.get("vo"):
            end = min(r["vo_at"] + min(dur(r["vo"]), r["dur"]) + 0.25, t)
            cues.append((r["vo_at"], end, r["text"]))
    def ts(x):
        return f"{int(x//3600):02d}:{int(x%3600//60):02d}:{x%60:06.3f}".replace(".", ",")
    srt.write_text("\n".join(f"{i}\n{ts(a)} --> {ts(b)}\n{txt}\n"
                             for i, (a, b, txt) in enumerate(cues, 1)), encoding="utf-8")
    ass = work / "short.ass"
    sys.path.insert(0, str(ROOT / "studio"))
    from filmkit import _srt_to_ass
    _srt_to_ass(srt, ass, 960, 1280, font_size=40, margin_v=118)
    stamp(f"subs: {len(cues)} cues -> ASS")

    # ---- 5. one encode: burn + mux (video re-encoded once, audio copied)
    final = work / "final_raw.mp4"
    run([FF, "-y", "-v", "error", "-i", silent, "-i", mix,
         "-filter_complex", f"[0:v]ass={ass}:fontsdir={FONTS}[v]",
         "-map", "[v]", "-map", "1:a", "-c:v", "libx264", "-preset", "veryfast",
         "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "copy",
         "-movflags", "+faststart", final])
    stamp("burn + mux (single video encode)")

    # ---- 6. loudness
    out.parent.mkdir(parents=True, exist_ok=True)
    run([FF, "-y", "-v", "error", "-i", final, "-c:v", "copy",
         "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "192k",
         "-movflags", "+faststart", out])
    stamp(f"loudnorm -> {out}")
    return placed, t


def _lab(path: Path):
    import cv2
    img = cv2.imread(str(path))
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB).reshape(-1, 3).mean(0)
    return lab


def _has_face(path: Path) -> bool:
    import cv2
    img = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (360, 480))
    c = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    return len(c.detectMultiScale(img, 1.08, 4, minSize=(40, 40))) > 0


def check(placed, timeline_out: Path):
    """Shot-to-shot continuity: what actually changes across the cut."""
    tmp = Path("/tmp/cutlist_frames")
    tmp.mkdir(exist_ok=True)
    rows = []
    for a, b in zip(placed, placed[1:]):
        fa = frame(a.get("path", a["file"]), str(max(0, a["dur"] - 0.06)), tmp / f"{a['n']}_last.png")
        fb = frame(b.get("path", b["file"]), "0.02", tmp / f"{b['n']}_first.png")
        la, lb = _lab(fa), _lab(fb)
        rows.append({"cut": f"{a['n']}->{b['n']}",
                     "ssim_last_to_first": ssim(fa, fb),
                     "color_deltaE": round(float(np.linalg.norm((la - lb) / 255.0)), 3),
                     "face_before": _has_face(fa), "face_after": _has_face(fb)})
    timeline_out.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    return rows


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("build"); p.add_argument("timeline"); p.add_argument("--out", required=True)
    p.add_argument("--work", default="/tmp/cutlist_work"); p.add_argument("--no-bed", action="store_true")
    a = ap.parse_args()
    placed, total = build(Path(a.timeline), Path(a.out), Path(a.work), bed=not a.no_bed)
    rows = check(placed, Path(a.work) / "continuity.json")
    print(json.dumps({"total_s": round(total, 2), "continuity": rows,
                      "wall_s": round(time.time() - T0, 1)}, indent=2))


if __name__ == "__main__":
    main()
