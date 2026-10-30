#!/usr/bin/env python3
"""scorer — objective gates for best-of-N generation (CPU only, no GPU, no cloud).

Generation is free; judgement is the bottleneck. This measures a candidate clip
instead of "looking at it and hoping":

  identity   SSIM of frame 0 vs the reference still (whole frame + face crop)
  sharp      Laplacian variance (blur / mush detector — our old clips failed here)
  motion     how much the frame actually changes; flags frozen or runaway clips
  flicker    frame-to-frame instability (the "melting" defect)
  color      Lab shift vs reference (palette drift across shots)
  lipsync    correlation between mouth-region motion and the audio envelope
             (a PROXY with a lag search — not a trained sync detector)

Usage
  python3 studio/scorer.py score  clip.mp4 --ref still.png [--audio vo.mp3] [--json out.json]
  python3 studio/scorer.py pick   cands/*.mp4 --ref still.png [--audio vo.mp3] [--min 0.55]
"""
from __future__ import annotations

import argparse
import glob
import json
import subprocess
import sys
import tempfile
from pathlib import Path

import cv2
import numpy as np

FF = None
try:
    import imageio_ffmpeg
    FF = imageio_ffmpeg.get_ffmpeg_exe()
except Exception:
    FF = "ffmpeg"

CASCADE = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"


# ------------------------------------------------------------------ primitives
def ssim(a: np.ndarray, b: np.ndarray) -> float:
    """Plain SSIM on grayscale float images in [0,1]."""
    if a.shape != b.shape:
        b = cv2.resize(b, (a.shape[1], a.shape[0]))
    a, b = a.astype(np.float64), b.astype(np.float64)
    mu_a, mu_b = a.mean(), b.mean()
    va, vb = a.var(), b.var()
    cov = ((a - mu_a) * (b - mu_b)).mean()
    C1, C2 = 0.01 ** 2, 0.03 ** 2
    return float(((2 * mu_a * mu_b + C1) * (2 * cov + C2)) /
                 ((mu_a ** 2 + mu_b ** 2 + C1) * (va + vb + C2)))


def load_gray(path: Path, size=(360, 480)) -> np.ndarray:
    img = cv2.imread(str(path), cv2.IMREAD_GRAYSCALE)
    if img is None:
        return None
    return cv2.resize(img, size).astype(np.float32) / 255.0


_CASCADE = None


def detect_face(gray_u8) -> tuple | None:
    global _CASCADE
    if _CASCADE is None:
        _CASCADE = cv2.CascadeClassifier(CASCADE)
    for img in (gray_u8, cv2.equalizeHist(gray_u8)):
        faces = _CASCADE.detectMultiScale(img, scaleFactor=1.08, minNeighbors=4,
                                          minSize=(40, 40))
        if len(faces):
            x, y, w, h = max(faces, key=lambda f: f[2] * f[3])
            return int(x), int(y), int(w), int(h)
    return None


def audio_envelope(path: Path, fps: float, n_frames: int) -> np.ndarray | None:
    """RMS per video frame, via ffmpeg -> raw f32 mono 8 kHz."""
    if not path or not Path(path).exists():
        return None
    with tempfile.NamedTemporaryFile(suffix=".f32", delete=False) as tf:
        tmp = tf.name
    subprocess.run([FF, "-y", "-v", "error", "-i", str(path), "-ac", "1", "-ar", "8000",
                    "-f", "f32le", tmp], check=True)
    raw = np.fromfile(tmp, dtype=np.float32)
    Path(tmp).unlink(missing_ok=True)
    if raw.size == 0:
        return None
    per_frame = 8000 / max(fps, 1)
    env = np.array([raw[int(i * per_frame):int((i + 1) * per_frame)].std()
                    for i in range(n_frames)])
    if env.max() > 0:
        env = env / env.max()
    return env


def pearson_lag(sig: np.ndarray, env: np.ndarray, max_lag=6):
    best_r, best_lag = -1.0, 0
    n = min(len(sig), len(env))
    sig, env = sig[:n], env[:n]
    for lag in range(-max_lag, max_lag + 1):
        if lag >= 0:
            a, b = sig[lag:], env[:n - lag]
        else:
            a, b = sig[:n + lag], env[-lag:]
        if len(a) < 8 or a.std() < 1e-6 or b.std() < 1e-6:
            continue
        r = float(np.corrcoef(a, b)[0, 1])
        if r > best_r:
            best_r, best_lag = r, lag
    return best_r, best_lag


# ------------------------------------------------------------------ scoring
def score_clip(clip: Path, ref: Path | None, audio: Path | None, fps_hint=32.0) -> dict:
    cap = cv2.VideoCapture(str(clip))
    fps = cap.get(cv2.CAP_PROP_FPS) or fps_hint
    frames, grays = [], []
    while True:
        ok, fr = cap.read()
        if not ok:
            break
        g = cv2.cvtColor(fr, cv2.COLOR_BGR2GRAY)
        small = cv2.resize(g, (360, 480))
        frames.append(small.astype(np.float32) / 255.0)
        grays.append(small)
    cap.release()
    if not frames:
        return {"clip": str(clip), "error": "no frames decoded"}

    grays_u8 = np.stack(grays)
    out = {"clip": clip.name, "frames": len(frames), "fps": round(float(fps), 2),
           "duration_s": round(len(frames) / float(fps), 2)}

    # motion / frozen / flicker
    diffs = np.abs(np.diff(np.stack(frames), axis=0)).mean(axis=(1, 2))
    out["motion_mean"] = round(float(diffs.mean()), 5)
    out["frozen_ratio"] = round(float((diffs < 0.002).mean()), 3)
    if len(diffs) > 3:
        smooth = np.convolve(diffs, np.ones(5) / 5, mode="same")
        out["flicker"] = round(float(np.abs(diffs - smooth).mean()), 5)
    else:
        out["flicker"] = 0.0

    # sharpness
    lap = [cv2.Laplacian(g, cv2.CV_64F).var() for g in grays[::max(1, len(grays) // 8)]]
    out["sharpness"] = round(float(np.mean(lap)), 1)

    # identity vs reference
    if ref and Path(ref).exists():
        r = load_gray(Path(ref), (360, 480))
        if r is not None:
            out["identity_ssim"] = round(ssim(frames[0], r), 4)
            out["identity_ssim_last"] = round(ssim(frames[-1], r), 4)
            # face crop comparison when a face exists on both sides
            rf = detect_face(cv2.resize(cv2.imread(str(ref), 0), (360, 480)))
            cf = detect_face(grays[0])
            if rf and cf:
                rc = frames[0][rf[1]:rf[1] + rf[3], rf[0]:rf[0] + rf[2]]
                cc = frames[0][cf[1]:cf[1] + cf[3], cf[0]:cf[0] + cf[2]]
                if rc.size and cc.size:
                    out["face_ssim"] = round(ssim(rc, cc), 4)
            # palette drift
            lab_ref = cv2.cvtColor(cv2.resize(cv2.imread(str(ref)), (360, 480)),
                                   cv2.COLOR_BGR2LAB).reshape(-1, 3).mean(0)
            lab_now = cv2.cvtColor(cv2.resize(
                (frames[0] * 255).astype(np.uint8), (360, 480)),
                cv2.COLOR_GRAY2BGR)
            lab_now = cv2.cvtColor(lab_now, cv2.COLOR_BGR2LAB).reshape(-1, 3).mean(0)
            out["color_shift"] = round(float(np.linalg.norm(
                (lab_ref[1:] - lab_now[1:]) / 255.0)), 4)

    # lipsync proxy: mouth motion vs audio envelope
    face = detect_face(grays[0])
    if face and audio:
        x, y, w, h = face
        my = y + int(h * 0.62)
        mh = int(h * 0.34)
        mouth = [g[my:my + mh, x + int(w * 0.2): x + int(w * 0.8)] for g in grays]
        mm = np.array([np.abs(np.diff(m.astype(np.float32), axis=0)).mean()
                       for m in mouth[:-1]] + [0.0])
        env = audio_envelope(Path(audio), float(fps), len(grays))
        if env is not None:
            r, lag = pearson_lag(mm, env)
            out["lipsync_r"] = round(r, 3)
            out["lipsync_lag_frames"] = int(lag)
            out["lipsync_note"] = "proxy only (mouth-motion vs RMS envelope)"
    return out


def verdict(s: dict, mins: dict) -> tuple[bool, list[str]]:
    why = []
    if s.get("frozen_ratio", 1) > mins["frozen"]:
        why.append(f"frozen {s['frozen_ratio']*100:.0f}% of frames")
    if s.get("motion_mean", 0) < mins["motion_lo"]:
        why.append("almost no motion")
    if s.get("motion_mean", 0) > mins["motion_hi"]:
        why.append("runaway motion / melting")
    if s.get("sharpness", 0) < mins["sharp"]:
        why.append(f"soft ({s['sharpness']:.0f} lap-var)")
    if "identity_ssim" in s and s["identity_ssim"] < mins["identity"]:
        why.append(f"identity drift ({s['identity_ssim']:.2f})")
    if "lipsync_r" in s and s["lipsync_r"] < mins["lipsync"]:
        why.append(f"mouth not following audio (r={s['lipsync_r']:.2f})")
    return (len(why) == 0), why


DEFAULT_MINS = {"frozen": 0.25, "motion_lo": 0.004, "motion_hi": 0.12,
                "sharp": 40.0, "identity": 0.55, "lipsync": 0.15}


def cmd_score(a):
    s = score_clip(Path(a.clip), Path(a.ref) if a.ref else None,
                   Path(a.audio) if a.audio else None)
    ok, why = verdict(s, DEFAULT_MINS)
    s["pass"] = ok
    s["reasons"] = why
    print(json.dumps(s, indent=2, ensure_ascii=False))
    if a.json:
        Path(a.json).write_text(json.dumps(s, indent=2, ensure_ascii=False), encoding="utf-8")


def cmd_pick(a):
    files = []
    for pat in a.files:
        files.extend(sorted(glob.glob(pat)) or ([pat] if Path(pat).exists() else []))
    if not files:
        raise SystemExit("no candidates matched")
    rows = []
    for f in files:
        s = score_clip(Path(f), Path(a.ref) if a.ref else None,
                       Path(a.audio) if a.audio else None)
        ok, why = verdict(s, DEFAULT_MINS)
        s["pass"], s["reasons"] = ok, why
        rows.append(s)

    def rank(s):
        v = 0.0
        v += 2.0 * s.get("identity_ssim", 0.0) + 1.0 * s.get("face_ssim", 0.0)
        v += 0.6 * s.get("lipsync_r", 0.0)
        v += 0.5 * min(s.get("sharpness", 0) / 200.0, 1.0)
        v -= 1.5 * s.get("frozen_ratio", 1.0)
        v -= 1.0 * min(s.get("flicker", 0) / 0.01, 1.0)
        v -= 0.5 * s.get("color_shift", 0.0)
        v += 1.0 if s["pass"] else 0.0
        return v

    rows.sort(key=rank, reverse=True)
    for i, r in enumerate(rows):
        r["rank"] = i + 1
        r["score"] = round(rank(r), 3)
    print(f"{'rank':<5}{'file':<34}{'score':>7}{'id':>7}{'face':>7}{'lip':>7}"
          f"{'sharp':>7}{'froz':>6}{'pass':>6}")
    for r in rows:
        print(f"{r['rank']:<5}{r['clip'][:33]:<34}{r['score']:>7.2f}"
              f"{r.get('identity_ssim', 0):>7.2f}{r.get('face_ssim', 0):>7.2f}"
              f"{r.get('lipsync_r', 0):>7.2f}{r.get('sharpness', 0):>7.0f}"
              f"{r.get('frozen_ratio', 0):>6.2f}{'YES' if r['pass'] else 'no':>6}")
    print("\nwinner:", rows[0]["clip"], "—", "; ".join(rows[0]["reasons"]) or "all gates passed")
    if a.json:
        Path(a.json).write_text(json.dumps(rows, indent=2, ensure_ascii=False), encoding="utf-8")
    fails = [r for r in rows if not r["pass"]]
    print(f"{len(rows)-len(fails)}/{len(rows)} passed all gates")
    return 0 if rows[0]["pass"] else 1


def main():
    ap = argparse.ArgumentParser(prog="scorer")
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("score"); p.add_argument("clip")
    p.add_argument("--ref"); p.add_argument("--audio"); p.add_argument("--json")
    p.set_defaults(fn=cmd_score)
    p = sub.add_parser("pick"); p.add_argument("files", nargs="+")
    p.add_argument("--ref"); p.add_argument("--audio"); p.add_argument("--json")
    p.set_defaults(fn=cmd_pick)
    a = ap.parse_args()
    sys.exit(a.fn(a) or 0)


if __name__ == "__main__":
    main()
