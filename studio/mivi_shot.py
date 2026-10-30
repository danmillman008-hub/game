#!/usr/bin/env python3
"""mivi_shot — run Mivi generation FROM A GITHUB RUNNER (stdlib only).

Why this file exists: the agent sandbox blocks cpi.ufotosoft.com and
algo-v1.wiseoel.com at the egress proxy (both return 000 in ~60 ms). A GitHub
Actions runner has normal internet, so generation happens there and the clips
come back through the repo.

Usage
  python3 studio/mivi_shot.py films/short16/gen_jobs.json --out films/short16/clips_gen

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
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "bridge"))
import mivi_mcp as M  # noqa: E402


def log(msg):
    print(msg, flush=True)


def generate_one(job: dict, outdir: Path) -> list[dict]:
    results = []
    attempts = int(job.get("attempts", 1))
    for a in range(1, attempts + 1):
        dst = outdir / f"{job['id']}_a{a}.mp4"
        t0 = time.time()
        try:
            created = M.t_video({
                "image": str(ROOT / job["still"]) if not os.path.isabs(job["still"]) else job["still"],
                "prompt": job.get("prompt", ""),
                "model": job.get("model", "mivi-gx-720p"),
                "quality": int(job.get("quality", 2)),
            })
            tid = created.get("task_id")
            log(f"[{job['id']}] attempt {a} task {tid} created in {time.time()-t0:.1f}s")
            done = M.t_video_wait({"task_id": tid, "timeout_s": job.get("timeout_s", 420),
                                   "out": str(dst), "interval_s": 5})
            ok = bool(done.get("saved"))
            results.append({"attempt": a, "task": tid, "ok": ok,
                            "seconds": round(time.time() - t0, 1),
                            "file": str(dst.relative_to(ROOT)) if ok else None,
                            "error": None if ok else (done.get("reason") or done.get("status"))})
        except Exception as exc:  # noqa: BLE001
            results.append({"attempt": a, "ok": False, "seconds": round(time.time() - t0, 1),
                            "error": f"{type(exc).__name__}: {exc}"})
            log(f"[{job['id']}] attempt {a} FAILED: {exc}")
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("jobs")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    jobs = json.loads(Path(a.jobs).read_text(encoding="utf-8"))["shots"]
    outdir = ROOT / a.out
    outdir.mkdir(parents=True, exist_ok=True)

    report = {"started": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
              "runner": os.environ.get("GITHUB_RUN_ID", "local"),
              "shots": []}
    t_all = time.time()
    for job in jobs:
        log(f"--- {job['id']}  still={job['still']}")
        res = generate_one(job, outdir)
        report["shots"].append({"id": job["id"], "still": job["still"],
                                "prompt": job.get("prompt", ""), "attempts": res,
                                "ok": any(r["ok"] for r in res)})
    report["wall_s"] = round(time.time() - t_all, 1)
    report["ok_count"] = sum(1 for s in report["shots"] if s["ok"])
    report["total"] = len(report["shots"])
    (outdir / "gen_report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    log(json.dumps({k: report[k] for k in ("wall_s", "ok_count", "total")}, indent=2))
    # never fail the job on a single bad shot — the report is the truth
    return 0


if __name__ == "__main__":
    sys.exit(main())
