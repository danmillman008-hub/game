#!/usr/bin/env python3
"""motionlint — find motion that reads as "the clip was rewound".

The defect: a large object (umbrella, head, hand) drifts one way and then
snaps back, or the whole frame's motion suddenly reverses direction. Viewers
read that as a reversed frame even when every frame is unique.

Method: estimate the whole-frame translation per frame pair with phase
correlation (no GPU, no optical flow), take the dominant slow component as
"intended motion", then flag frames where the frame-to-frame vector flips sign
against it with enough magnitude — a reversal event.

Usage
  python3 studio/motionlint.py clip.mp4 [--json out.json] [--min-flip 1.5]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import cv2
import numpy as np


def _seed_template(f):
    """Find the umbrella-like mass in frame 0 and return (template, box).

    Dark + low saturation in the upper half; the biggest such blob is the
    umbrella in this film. Coordinates are returned as a box so we can crop a
    template and then follow *that object* instead of 'whatever is darkest',
    which is what made the first version jump between the coat, the bench and
    the canopy.
    """
    hsv = cv2.cvtColor(f, cv2.COLOR_BGR2HSV)
    v, s_ = hsv[:, :, 2], hsv[:, :, 1]
    mask = ((v < 62) & (s_ < 120)).astype(np.uint8)
    mask[int(f.shape[0] * 0.60):, :] = 0
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8))
    n, _, stats, _ = cv2.connectedComponentsWithStats(mask, 8)
    if n < 2:
        return None, None
    i = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
    x, y, w, h, area = stats[i]
    if area < 3000:
        return None, None
    pad = 6
    x0, y0 = max(0, x - pad), max(0, y - pad)
    x1, y1 = min(f.shape[1], x + w + pad), min(f.shape[0], y + h + pad)
    return f[y0:y1, x0:x1], (int(x0), int(y0), int(x1), int(y1))


def _smooth(a, k=7):
    a = np.asarray(a, dtype=np.float64)
    if len(a) < k:
        return a
    pad = k // 2
    return np.convolve(np.pad(a, pad, mode="edge"), np.ones(k) / k, mode="valid")


def analyze(path: Path, flip_px_per_s: float = 12.0) -> dict:
    cap = cv2.VideoCapture(str(path))
    fps = cap.get(cv2.CAP_PROP_FPS) or 32.0
    ok, first = cap.read()
    if not ok:
        cap.release()
        return {"clip": path.name, "error": "unreadable"}
    tpl, box = _seed_template(first)
    if tpl is None:
        cap.release()
        return {"clip": path.name, "error": "no trackable object", "reversals": [],
                "reversal_ratio": None}
    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
    cx, cy, conf = [], [], []
    while True:
        ok, f = cap.read()
        if not ok:
            break
        r = cv2.matchTemplate(f, tpl, cv2.TM_CCOEFF_NORMED)
        _, score, _, loc = cv2.minMaxLoc(r)
        cx.append(loc[0] + tpl.shape[1] / 2)
        cy.append(loc[1] + tpl.shape[0] / 2)
        conf.append(score)
    cap.release()
    n = len(cx)
    if n < 8:
        return {"clip": path.name, "error": "too few frames"}
    sx, sy = _smooth(cx), _smooth(cy)
    vx = np.diff(sx) * fps
    vy = np.diff(sy) * fps

    lo, hi = n // 4, 3 * n // 4
    dom = np.array([np.median(vx[lo:hi]), np.median(vy[lo:hi])])
    dn = float(np.linalg.norm(dom))
    if dn < 1.0:
        return {"clip": path.name, "frames": n, "fps": round(float(fps), 2),
                "object_speed_px_s": round(dn, 1), "verdict": "object almost still",
                "reversals": [], "reversal_ratio": 0.0,
                "track_confidence": round(float(np.mean(conf)), 3)}
    unit = dom / dn
    proj = vx * unit[0] + vy * unit[1]
    flips = []
    for i in range(1, len(proj)):
        a, b = proj[i - 1], proj[i]
        if a * b < 0 and min(abs(a), abs(b)) > flip_px_per_s:
            flips.append({"t": round((i + 1) / fps, 2), "before": round(float(a), 1),
                          "after": round(float(b), 1),
                          "severity": round(float(min(abs(a), abs(b))), 1)})
    against = float(np.clip(-proj, 0, None).sum())
    total = float(np.abs(proj).sum()) + 1e-6
    return {"clip": path.name, "frames": n, "fps": round(float(fps), 2),
            "duration_s": round(n / float(fps), 2),
            "object_speed_px_s": round(dn, 1),
            "track_confidence": round(float(np.mean(conf)), 3),
            "reversals": flips,
            "reversal_ratio": round(against / total, 3),
            "verdict": ("reads as rewound" if (len(flips) >= 2 and against / total > 0.25)
                        else "smooth")}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("clips", nargs="+")
    ap.add_argument("--json")
    ap.add_argument("--min-flip", type=float, default=12.0)
    a = ap.parse_args()
    out = [analyze(Path(c), a.min_flip) for c in a.clips]
    for r in out:
        if r.get("error"):
            print(f"{r['clip']}: {r['error']}")
            continue
        flip_txt = ", ".join(f"{f['t']}s" for f in r["reversals"][:6]) or "—"
        print(f"{r['clip'][:38]:<40} reversal_ratio={r['reversal_ratio']:<6} "
              f"verdict={r['verdict']:<18} flips: {flip_txt}")
    if a.json:
        Path(a.json).write_text(json.dumps(out, indent=2), encoding="utf-8")
    worst = max((r.get("reversal_ratio") or 0 for r in out), default=0)
    return 0 if worst < 0.25 else 1


if __name__ == "__main__":
    sys.exit(main())
