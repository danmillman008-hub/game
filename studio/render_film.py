#!/usr/bin/env python3
"""Batch renderer for a filmkit project — the unattended loop.

Every still is built on Mivi (no local image generation):
    crop:<file>,l,t,r,b     crop, then 2x super resolution     (~15 s)
    compose:<a>,<b>         two-image composer + prompt         (~2-4 min)
    file:<path>             use as-is
    darken:<path>           exposure pull for a fade beat

Then each shot is rendered from its still, 720P by default, one take.
Resumable: project.json records what exists, so a re-run only does the gaps.

    python3 studio/render_film.py films/before_leaving --budget-min 95
    python3 studio/render_film.py films/before_leaving --stills-only
    python3 studio/render_film.py films/before_leaving --finish     # assemble+srt+qc
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "studio"))
sys.path.insert(0, str(ROOT / "bridge"))
import filmkit as K          # noqa: E402
import mivi_mcp as M         # noqa: E402


LOGPATH = None


def log(*a):
    line = f"[{time.strftime('%H:%M:%S')}] " + " ".join(str(x) for x in a)
    print(line, flush=True)
    if LOGPATH:
        with open(LOGPATH, "a", encoding="utf-8") as f:
            f.write(line + "\n")


def build_still(d: Path, proj: dict, s: dict, force=False) -> Path | None:
    key = s.get("still_key")
    spec = (proj.get("stills") or {}).get(key) or {}
    src = spec.get("source")
    if not src:
        raise SystemExit(f"shot {s['n']}: no still spec for key {key!r}")
    kind, _, val = src.partition(":")
    (d / "stills").mkdir(parents=True, exist_ok=True)
    (d / "clips").mkdir(parents=True, exist_ok=True)
    out = d / "stills" / f"s{int(s['n']):02d}_{key}.png"
    if out.exists() and not force:
        s["still"] = str(out.relative_to(d)); return out

    if kind == "file":
        shutil.copyfile(d / val, out)
    elif kind == "crop":
        parts = val.split(",")
        rel, box = parts[0], tuple(int(x) for x in parts[1:5])
        from PIL import Image
        im = Image.open(d / rel).crop(box)
        tmp = d / "stills" / f"_crop{s['n']}.png"
        im.save(tmp)
        up = upscale_url(tmp)
        M.download(up, str(out))
        tmp.unlink(missing_ok=True)
    elif kind == "compose":
        a, b = [x.strip() for x in val.split(",")]
        r = M.t_compose({"images": [str(d / a), str(d / b)],
                         "prompt": spec.get("prompt") or s.get("motion") or "",
                         "out": str(out), "timeout_s": 480})
        if not r.get("saved"):
            raise RuntimeError(f"compose failed: {r}")
    elif kind == "darken":
        tmp = d / "stills" / f"_dk{s['n']}.png"
        K.run([K.FF, "-y", "-v", "error", "-i", str(d / val), "-vf",
               "eq=brightness=-0.22:saturation=0.55", str(tmp)])
        shutil.move(str(tmp), str(out))
    else:
        raise SystemExit(f"unknown still source {kind}")

    s["still"] = str(out.relative_to(d))
    s["state"] = "still_ready"
    return out


def upscale_url(path: Path) -> str:
    r = M.t_upscale({"image": str(path)})
    d = r.get("result")
    if isinstance(d, str):
        return d
    if isinstance(d, list) and d:
        return d[0] if isinstance(d[0], str) else d[0].get("url")
    if isinstance(d, dict):
        for k in ("url", "urlList", "imageUrl"):
            v = d.get(k)
            if isinstance(v, str):
                return v
            if isinstance(v, list) and v:
                return v[0] if isinstance(v[0], str) else v[0].get("url")
    raise RuntimeError(f"superres returned {r}")


def render_shot(d: Path, proj: dict, s: dict, quality: int, takes: int) -> bool:
    still = d / s["still"]
    prompt = s.get("motion") or ""
    for t in range(1, takes + 1):
        created = M.t_video({"image": str(still), "prompt": prompt,
                             "model": proj.get("model") or "mivi-gx-720p",
                             "quality": quality})
        out = d / "clips" / f"s{int(s['n']):02d}_t{t}.mp4"
        res = M.t_video_wait({"task_id": created["task_id"], "out": str(out),
                              "timeout_s": 480})
        if not res.get("video_url"):
            s.setdefault("takes", []).append({"take": t, "task": created["task_id"],
                                              "ok": False, "reason": res.get("reason")})
            log(f"  shot {s['n']} take {t}: FAILED {res.get('reason')}")
            continue
        meta = K.probe(out)
        s.setdefault("takes", []).append({"take": t, "task": created["task_id"],
                                          "ok": True, "file": str(out.relative_to(d)),
                                          "bytes": meta["bytes"],
                                          "duration_s": meta["duration_s"],
                                          "size": f"{meta['width']}x{meta['height']}"})
        s["clip"] = str(out.relative_to(d))
        s["state"] = "rendered"
        log(f"  shot {s['n']} take {t}: ok {meta['width']}x{meta['height']} "
            f"{meta['duration_s']}s {meta['bytes']//1024}KB")
        return True
    return False


def finish(d: Path, proj: dict):
    log("assemble")
    K.cmd_assemble(argparse.Namespace(name=str(d), crossfade=None, subs=None,
                                     vo=None, music=None, duck=False))
    log("subtitles from narration")
    K.cmd_srt(argparse.Namespace(name=str(d), crossfade=None, cps=None))
    log("re-assemble with subs")
    K.cmd_assemble(argparse.Namespace(name=str(d), crossfade=None,
                                      subs=str(d / "subs" / "final.srt"),
                                      vo=None, music=None, duck=False))
    log("qc")
    K.cmd_qc(argparse.Namespace(name=str(d)))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project")
    ap.add_argument("--budget-min", type=float, default=95)
    ap.add_argument("--quality", type=int, choices=[1, 2])
    ap.add_argument("--takes", type=int, default=1)
    ap.add_argument("--stills-only", action="store_true")
    ap.add_argument("--finish", action="store_true")
    ap.add_argument("--force-stills", action="store_true")
    a = ap.parse_args()

    K.FF, K.FP = K.ffmpeg_bin(), K.ffprobe_bin()
    M.FFMPEG, M.FFPROBE = K.FF, K.FP or "ffprobe"

    global LOGPATH
    (Path(a.project) / "render.log").write_text("", encoding="utf-8")
    LOGPATH = str(Path(a.project) / "render.log")
    proj = json.loads((Path(a.project) / "project.json").read_text(encoding="utf-8"))
    d = Path(a.project).resolve()
    quality = int(a.quality or proj.get("quality") or 2)
    t0 = time.time()
    deadline = t0 + a.budget_min * 60

    todo = [s for s in proj["shots"]]
    done = sum(1 for s in todo if s.get("clip"))
    log(f"{proj.get('title') or proj['name']}: {len(todo)} shots, {done} already rendered, "
        f"quality {quality}, budget {a.budget_min:.0f} min")

    if a.finish:
        finish(d, proj)
        return

    for s in todo:
        if time.time() > deadline:
            log("budget exhausted — re-run to continue"); break
        try:
            if not s.get("clip") or a.force_stills:
                build_still(d, proj, s, force=a.force_stills)
                K.save(d, proj)
            if not a.stills_only and not s.get("clip"):
                render_shot(d, proj, s, quality, a.takes)
                K.save(d, proj)
        except Exception as exc:
            log(f"  shot {s['n']}: ERROR {type(exc).__name__}: {exc}")
            K.save(d, proj)

    left = [s["n"] for s in proj["shots"] if not s.get("clip")]
    log(f"rendered {len(proj['shots']) - len(left)}/{len(proj['shots'])}; "
        f"missing: {left[:12]}{'…' if len(left) > 12 else ''}")
    if not left:
        finish(d, proj)


if __name__ == "__main__":
    import traceback
    try:
        main()
    except BaseException:
        log("FATAL\n" + traceback.format_exc()[-3000:])
        raise
