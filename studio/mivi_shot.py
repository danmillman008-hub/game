#!/usr/bin/env python3
"""mivi_shot — run Mivi generation FROM A GITHUB RUNNER (stdlib only).

Two changes on 2026-10-30, both measured problems:

1. **Parallel.** Generation used to be one task at a time: 15 shots x ~180 s came to
   45 minutes of wall clock where the runner was idle 12 of those minutes doing
   nothing but polling. Tasks are independent on the provider side, so this file now
   keeps N tasks in flight and polls them together. Chained shots still serialise —
   only the parts of the graph that are actually dependent wait.

2. **Anchor-first jobs.** A deep chain is where identity dies (see
   studio/knowledge/workflow/CONSISTENCY_AND_SPEED.md). A job that names its own `still`
   becomes parallel-safe; a job that names `still_from_clip` joins a chain. The
   tool reports the longest chain in the batch so the plan can be judged before
   anything is spent.

Usage
  python3 studio/mivi_shot.py films/short16/gen_jobs.json --out films/short16/clips_gen
  python3 studio/mivi_shot.py films/short16/gen_jobs.json --out ... --parallel 4
  python3 studio/mivi_shot.py films/short16/gen_jobs.json --out ... --dry-run

Job file
  {"shots": [{"id": "g1", "still": "path.png", "prompt": "...", "model": "mivi-gx-720p",
              "quality": 2, "attempts": 2}]}

Every attempt is kept (`g1_a1.mp4`, `g1_a2.mp4`) — generation is free, judgement
is not. A `gen_report.json` with per-shot wall-clock lands next to the clips.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "bridge"))
import mivi_mcp as M  # noqa: E402


def log(msg):
    print(msg, flush=True)


def last_frame(video: Path, out: Path) -> Path:
    """Pull the final frame so the next link starts exactly where this one ended."""
    import imageio_ffmpeg
    ff = imageio_ffmpeg.get_ffmpeg_exe()
    out.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([ff, "-y", "-v", "error", "-sseof", "-0.4", "-i", str(video),
                    "-update", "1", "-vsync", "0", str(out)], check=True)
    return out


def clip_id(path: str) -> str | None:
    """`films/.../w01_wide_a1.mp4` -> `w01_wide` (the job that makes it)."""
    m = re.match(r"(.+?)_a\d+\.mp4$", Path(path).name)
    return m.group(1) if m else None


# --------------------------------------------------------------------- graph ---
def build_nodes(jobs: list[dict]) -> list[dict]:
    """Work out, for every job, which other job (if any) it must wait for."""
    ids = {j["id"] for j in jobs}
    nodes = []
    for j in jobs:
        node = dict(j)
        node["dep"] = None
        node["still_spec"] = j.get("still", "")
        if j.get("still_from"):
            node["dep"] = j["still_from"]
        elif j.get("still_from_clip"):
            src = ROOT / j["still_from_clip"]
            if not src.exists():                     # produced later in this batch
                cid = clip_id(j["still_from_clip"])
                if cid in ids:
                    node["dep"] = cid
            node["clip_spec"] = j["still_from_clip"]
        nodes.append(node)
    # drop deps that do not exist in the batch and whose clip is already on disk
    for n in nodes:
        if n["dep"] and n["dep"] not in ids:
            n["dep"] = None
    return nodes


def chain_depths(nodes: list[dict]) -> dict[str, int]:
    by_id = {n["id"]: n for n in nodes}
    memo: dict[str, int] = {}

    def depth(i: str, seen=()) -> int:
        if i in memo:
            return memo[i]
        d = by_id[i]["dep"]
        if not d or d in seen:
            memo[i] = 0
            return 0
        memo[i] = 1 + depth(d, seen + (i,))
        return memo[i]

    for n in nodes:
        depth(n["id"])
    return memo


# ------------------------------------------------------------------- runner ---
def resolve_still(node: dict, outdir: Path, done: dict) -> str | None:
    """Return a PNG path for this job, or None if a dependency has not finished."""
    if node["dep"]:
        d = done.get(node["dep"])
        if d is None:
            return None
        if not d.get("ok"):
            raise RuntimeError(f"dependency {node['dep']} failed")
        return d["last"]
    if node.get("clip_spec"):
        c = ROOT / node["clip_spec"]
        if c.exists():
            return str(last_frame(c, outdir / f"{node['id']}_src.png"))
        return None
    s = node.get("still_spec") or ""
    if not s:
        return None
    p = Path(s)
    return str(p if p.is_absolute() else ROOT / s)


def launch(node: dict, still: str, attempt: int, outdir: Path) -> dict:
    dst = outdir / f"{node['id']}_a{attempt}.mp4"
    body = {"image": still, "prompt": node.get("prompt", ""),
            "model": node.get("model", "mivi-gx-720p"),
            "quality": int(node.get("quality", 2))}
    # two images = first/last-frame probe (see CONSISTENCY_AND_SPEED.md §3)
    if node.get("end_still"):
        e = Path(node["end_still"])
        body["images"] = [still, str(e if e.is_absolute() else ROOT / node["end_still"])]
    created = M.t_video(body)
    return {"task": created.get("task_id"), "t0": time.time(), "attempt": attempt,
            "dst": dst, "still": still}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jobs")
    ap.add_argument("--out", required=True)
    ap.add_argument("--parallel", type=int, default=3,
                    help="how many tasks may be in flight at once")
    ap.add_argument("--poll", type=float, default=6.0)
    ap.add_argument("--timeout", type=int, default=900, help="seconds per attempt")
    ap.add_argument("--skip-existing", action="store_true",
                    help="keep clips already on disk, only make what is missing")
    ap.add_argument("--dry-run", action="store_true",
                    help="print the graph, the chain depths and the wall-clock guess")
    a = ap.parse_args()

    jobs = json.loads(Path(a.jobs).read_text(encoding="utf-8"))["shots"]
    nodes = build_nodes(jobs)
    depths = chain_depths(nodes)

    # guard: never spend a generation on a prompt that breaks the motion rules
    try:
        sys.path.insert(0, str(ROOT / "studio"))
        import motionbank
        for j in jobs:
            r = motionbank.lint(j.get("prompt", ""))
            if not r["ok"]:
                log(f"[{j['id']}] PROMPT WARN score={r['score']}: "
                    + "; ".join(i["msg"] for i in r["issues"]))
    except Exception as exc:  # noqa: BLE001
        log(f"(prompt lint skipped: {exc})")

    outdir = ROOT / a.out
    outdir.mkdir(parents=True, exist_ok=True)
    longest = max(depths.values()) if depths else 0
    heads = sum(1 for n in nodes if not n["dep"])

    if a.dry_run:
        waves = {}
        for n in nodes:
            waves.setdefault(depths[n["id"]], []).append(n["id"])
        est = 0.0
        for d in sorted(waves):
            n_at = len(waves[d])
            est += 180.0 * max(1, -(-n_at // max(a.parallel, 1)))
        log(f"{len(nodes)} jobs · {len(waves)} waves · longest chain {longest} · "
            f"parallel {a.parallel} · independent {heads}")
        for d in sorted(waves):
            log(f"  wave {d}: {', '.join(waves[d])}")
        log(f"estimated wall clock ~{est/60:.0f} min "
            f"(serial would be ~{180*len(nodes)/60:.0f} min)")
        if longest > 2:
            log(f"WARN longest chain is {longest}: identity drifts after 2-3 links. "
                "Re-anchor on a still instead of extending the chain.")
        return 0

    report = {"started": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
              "runner": os.environ.get("GITHUB_RUN_ID", "local"),
              "parallel": a.parallel, "longest_chain": longest, "shots": []}
    t_all = time.time()

    pending = [n for n in nodes]
    running: dict[str, dict] = {}
    done: dict[str, dict] = {}
    attempts_used: dict[str, int] = {}

    def record(node, res, ok, err=None):
        report["shots"].append({"id": node["id"], "still": res.get("still"),
                                "prompt": node.get("prompt", ""),
                                "chained": node["dep"] is not None,
                                "attempts": [{"attempt": res["attempt"], "task": res.get("task"),
                                              "ok": ok,
                                              "seconds": round(time.time() - res["t0"], 1),
                                              "file": str(res["dst"].relative_to(ROOT)) if ok else None,
                                              "error": err}]})

    while pending or running:
        # ---- launch whatever is ready
        for node in list(pending):
            if len(running) >= a.parallel:
                break
            try:
                still = resolve_still(node, outdir, done)
            except RuntimeError as exc:
                log(f"[{node['id']}] skipped: {exc}")
                done[node["id"]] = {"ok": False}
                pending.remove(node)
                report["shots"].append({"id": node["id"], "ok": False, "attempts": [],
                                        "error": str(exc)})
                continue
            if still is None:
                continue                     # waiting on a dependency
            if not Path(still).exists() or Path(still).is_dir():
                log(f"[{node['id']}] NO STILL ({still!r}) — skipping")
                done[node["id"]] = {"ok": False}
                pending.remove(node)
                report["shots"].append({"id": node["id"], "ok": False, "attempts": [],
                                        "error": "missing still"})
                continue
            if a.skip_existing:
                have = sorted(outdir.glob(f"{node['id']}_a*.mp4"))
                if have:
                    lf = last_frame(have[-1], outdir / f"{node['id']}_last.png")
                    done[node["id"]] = {"ok": True, "last": str(lf)}
                    pending.remove(node)
                    log(f"[{node['id']}] exists, keeping {have[-1].name}")
                    report["shots"].append({"id": node["id"], "still": still, "ok": True,
                                            "skipped": True, "attempts": []})
                    continue
            attempts_used[node["id"]] = attempts_used.get(node["id"], 0) + 1
            try:
                st = launch(node, still, attempts_used[node["id"]], outdir)
                running[node["id"]] = st
                pending.remove(node)
                log(f"[{node['id']}] started task {st['task']} "
                    f"(attempt {st['attempt']}, {len(running)} in flight)")
            except Exception as exc:  # noqa: BLE001
                log(f"[{node['id']}] create FAILED: {exc}")
                done[node["id"]] = {"ok": False}
                pending.remove(node)
                report["shots"].append({"id": node["id"], "ok": False, "attempts": [],
                                        "error": f"{type(exc).__name__}: {exc}"})

        # ---- poll everything in flight
        for jid, st in list(running.items()):
            node = next(n for n in nodes if n["id"] == jid)
            try:
                s = M.t_video_status({"task_id": st["task"]})
            except Exception as exc:  # noqa: BLE001
                log(f"[{jid}] poll error: {exc}")
                continue
            if s.get("video_url"):
                try:
                    M.download(s["video_url"], str(st["dst"]))
                    lf = last_frame(st["dst"], outdir / f"{jid}_last.png")
                    done[jid] = {"ok": True, "last": str(lf)}
                    record(node, st, True)
                    log(f"[{jid}] ok in {time.time()-st['t0']:.0f}s -> {st['dst'].name}")
                except Exception as exc:  # noqa: BLE001
                    record(node, st, False, f"download: {exc}")
                    log(f"[{jid}] download FAILED: {exc}")
                del running[jid]
            elif str(s.get("status") or "").lower() in ("fail", "failed") or \
                    time.time() - st["t0"] > a.timeout:
                why = s.get("reason") or s.get("status") or "timeout"
                log(f"[{jid}] {why}")
                record(node, st, False, str(why))
                del running[jid]
                if st["attempt"] < int(node.get("attempts", 1)):
                    pending.append(node)          # retry
                else:
                    done[jid] = {"ok": False}

        if running:
            time.sleep(a.poll)

    report["wall_s"] = round(time.time() - t_all, 1)
    report["ok_count"] = sum(1 for s in report["shots"] if s.get("ok"))
    report["total"] = len(report["shots"])
    (outdir / "gen_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    log(json.dumps({k: report[k] for k in ("wall_s", "ok_count", "total", "longest_chain")},
                   indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
