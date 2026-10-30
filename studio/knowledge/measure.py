#!/usr/bin/env python3
"""measure.py — turn a real render into numbers the bank can hold.

Run after `voice.py render`: reads audio/vo/vo_plan.json (which the render fills in
with real_s and rtf), stats every mp3, records the model files and the machine, and
writes studio/knowledge/measurements.json.

This exists because "it sounded good" is not a measurement. The three numbers that
decide whether a TTS engine is usable for us are:

    rtf      seconds of compute per second of speech   (must be < 1 to feel usable)
    MB       what the model costs to download          (your stated constraint)
    bytes/s  what the output costs per second of audio (proxy for bitrate sanity)

    python3 studio/knowledge/measure.py [project]
"""
from __future__ import annotations

import hashlib
import json
import os
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "studio"))

import voice  # noqa: E402


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()[:16]


def main() -> int:
    name = sys.argv[1] if len(sys.argv) > 1 else "voice_probe"
    proj_dir = ROOT / "films" / name
    plan_path = proj_dir / "audio" / "vo" / "vo_plan.json"
    if not plan_path.exists():
        raise SystemExit(f"no {plan_path} — run voice.py plan/render first")
    plan = json.loads(plan_path.read_text(encoding="utf-8"))

    rows, missing = [], 0
    for r in plan["rows"]:
        mp3 = proj_dir / "audio" / "vo" / f"s{r['shot']:02d}.mp3"
        if not mp3.exists():
            missing += 1
            rows.append({**r, "rendered": False})
            continue
        b = mp3.stat().st_size
        secs = r.get("real_s") or 0.0
        rows.append({
            "shot": r["shot"], "lang": r["lang"], "engine": r["engine"], "voice": r["voice"],
            "text": r["text"], "audio_s": r.get("real_s"), "rtf": r.get("rtf"),
            "bytes": b, "bytes_per_s": round(b / r["real_s"], 1) if r.get("real_s") else None,
            "sha256_16": sha256(mp3), "rendered": True,
        })

    models = {}
    for lang, spec in voice.CATALOG.items():
        for fname, want, _ in spec["files"]:
            p = voice.CACHE / fname
            models[fname] = {"lang": lang, "expected_bytes": want,
                             "present_bytes": p.stat().st_size if p.exists() else None}
    total_mb = sum(m["present_bytes"] or 0 for m in models.values()) / 1e6

    rtfs = [r["rtf"] for r in rows if r.get("rtf")]
    out = {
        "measured_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "project": name,
        "machine": {
            "cpu_count": os.cpu_count(),
            "platform": platform.platform(),
            "python": platform.python_version(),
            "gpu": "none",
        },
        "models": models,
        "model_total_mb": round(total_mb, 1),
        "lines": rows,
        "summary": {
            "lines_rendered": len([r for r in rows if r.get("rendered")]),
            "lines_missing": missing,
            "mean_rtf": round(sum(rtfs) / len(rtfs), 3) if rtfs else None,
            "worst_rtf": round(max(rtfs), 3) if rtfs else None,
            "audio_s": round(sum(r.get("audio_s") or 0 for r in rows), 2),
        },
    }
    dst = Path(__file__).resolve().parent / "measurements.json"
    dst.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(out["summary"], ensure_ascii=False))
    print(f"models on disk: {total_mb:.1f} MB")
    print(f"-> {dst.relative_to(ROOT)}")
    return 0 if not missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
