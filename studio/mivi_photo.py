#!/usr/bin/env python3
"""mivi_photo.py — probe and use Mivi's picture endpoint (createAiPhotoTaskV2).

Why: the pilot's key frames were composited in PIL — a character cutout pasted on a
drawn background. That is a vector-poster technique, not a key frame for an image-to-
video model, and the model answered by fighting it (paper-doll edges, the Dutch angle
normalised away, a stray white bar turned into a sword). The correct input is a
*drawn frame*: a real anime illustration of the shot.

The app exposes a picture task next to the video task. This module probes its body
shape and, if it answers with an image, becomes the key-frame generator:

    upload character sheet -> prompt "the same character, wide shot, storm plain..." ->
    key frame -> image-to-video

    python3 studio/mivi_photo.py probe            # try body shapes, print verdicts
    python3 studio/mivi_photo.py make --ref c1.png --prompt "..." --out out.png

Everything here needs the Mivi host, so it runs on a GitHub runner, not the sandbox.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "bridge"))
import mivi_mcp as M  # noqa: E402

PHOTO_V2 = "/algo/v1/faceFusion/aigc/createAiPhotoTaskV2"
PHOTO_Q = "/algo/v1/faceFusion/aigc/queryAiPhotoTask"


def probe_photo(ref: str, prompt: str) -> dict:
    url = M.t_upload({"image": ref})["url"]
    variants = {
        "min": {"imageUrls": [url], "level": 1, "prompt": prompt},
        "enhance": {"imageUrls": [url], "level": 1, "prompt": prompt, "enhance": True},
        "full": {"imageUrls": [url], "level": 1, "prompt": prompt, "enhance": True,
                 "ifTest": False, "duration": 0},
        "noimg": {"level": 1, "prompt": prompt, "enhance": True},
    }
    out = {}
    for name, body in variants.items():
        try:
            r = M._post(PHOTO_V2, body, timeout=60)
        except Exception as e:                        # noqa: BLE001
            out[name] = {"error": f"{type(e).__name__}: {e}"}
            continue
        out[name] = r
        print(f"[{name}] c={r.get('c')} d={str(r.get('d'))[:200]}")
        time.sleep(2)
    return out


def wait_image(task_id: str, timeout: int = 420) -> str | None:
    t0 = time.time()
    while time.time() - t0 < timeout:
        try:
            r = M._post(PHOTO_Q, {"taskId": task_id}, timeout=60)
        except Exception:                             # noqa: BLE001
            time.sleep(6)
            continue
        d = r.get("d") or {}
        if isinstance(d, dict):
            for k in ("responseUrl", "imageUrl", "url", "resultUrl"):
                if d.get(k):
                    return d[k]
            status = d.get("status") or d.get("state")
            if status in (3, "3", "SUCCESS", "success"):
                urls = d.get("imageUrls") or d.get("urls") or []
                if urls:
                    return urls[0]
        time.sleep(6)
    return None


def main() -> int:
    ap = argparse.ArgumentParser(prog="mivi_photo", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("probe"); p.add_argument("--ref", default="films/anime_ten/refs/c1.png")
    p.add_argument("--prompt", default=(
        "anime key frame, 2D cel animation, the same character in a wide shot standing "
        "on a storm-lit plain at dusk, a road running to the horizon, flat colour fields, "
        "hard shadows, clean line art, no text"))
    p = sub.add_parser("make"); p.add_argument("--ref", required=True)
    p.add_argument("--prompt", required=True); p.add_argument("--out", required=True)
    p.add_argument("--variant", default="enhance")
    a = ap.parse_args()

    if a.cmd == "probe":
        res = probe_photo(a.ref, a.prompt)
        Path("probe_out/photo_probe.json").parent.mkdir(exist_ok=True)
        Path("probe_out/photo_probe.json").write_text(
            json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
        ok = [k for k, v in res.items() if isinstance(v, dict) and v.get("c") == 200]
        print(f"\naccepted bodies: {ok or 'none'}")
        if ok:
            tid = ((res[ok[0]].get("d") or {}) if isinstance(res[ok[0]].get("d"), dict) else {})
            tid = tid.get("taskId") or tid.get("task_id") or tid.get("id")
            print(f"task: {tid}")
            if tid:
                u = wait_image(str(tid))
                print(f"image: {u}")
                if u:
                    M.download(u, "probe_out/photo_probe.png")
        return 0

    body = {"imageUrls": [M.t_upload({"image": a.ref})["url"]], "level": 1,
            "prompt": a.prompt, "enhance": True}
    r = M._post(PHOTO_V2, body, timeout=90)
    print(json.dumps(r, ensure_ascii=False)[:400])
    d = r.get("d") or {}
    tid = (d.get("taskId") or d.get("task_id") or d.get("id")) if isinstance(d, dict) else d
    if not tid:
        raise SystemExit("no task id")
    u = wait_image(str(tid))
    if not u:
        raise SystemExit("no image")
    M.download(u, a.out)
    print(f"-> {a.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
