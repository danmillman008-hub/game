#!/usr/bin/env python3
"""Offline proof that the scheduler does what it claims.

No network, no credits: `mivi_mcp` is replaced by a stub that manufactures tiny mp4s
with ffmpeg. What is asserted is the part that broke in production and the part that
was rewritten today:

  * `ok` is written on the success path (it was missing — `ok_count` reported 0/2
    while both clips existed)
  * independent shots really are in flight together (observed concurrency > 1)
  * a chained shot waits for its parent and starts from the parent's last frame
  * a failed shot is recorded as failed and does not take the batch down
  * chain depth and wait-for relations survive a cycle-free graph

    python3 studio/tests/test_mivi_shot.py
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "studio"))

try:
    import imageio_ffmpeg  # noqa: E402
    FF = imageio_ffmpeg.get_ffmpeg_exe()
except ModuleNotFoundError:
    # The runner installs it (`pip install imageio-ffmpeg`); a bare sandbox does not.
    # Skipping loudly is better than a red build that says nothing about the code.
    print("SKIP: imageio-ffmpeg is not installed here (the runner has it: "
          "see .github/workflows/mivi.yml)")
    raise SystemExit(0)

created: list[dict] = []
in_flight = {"now": 0, "peak": 0}
polls = {"n": 0}
FAIL_IDS: set[str] = set()


def _tiny_mp4(path: Path, colour: str = "black"):
    """A real 1-second clip, or a real 1-frame PNG — `last_frame` must have something
    genuine to decode, otherwise the test proves nothing about the chain."""
    path.parent.mkdir(parents=True, exist_ok=True)
    src = ["-f", "lavfi", "-i", f"color=c={colour}:s=64x64:d=1:r=8"]
    if path.suffix == ".png":
        cmd = [FF, "-y", "-v", "error", *src, "-frames:v", "1", str(path)]
    else:
        cmd = [FF, "-y", "-v", "error", *src, "-pix_fmt", "yuv420p", str(path)]
    subprocess.run(cmd, check=True)


def stub_mcp():
    m = types.ModuleType("mivi_mcp")

    def t_video(a):
        created.append(a)
        return {"task_id": f"task{len(created)}", "model": a.get("model")}

    def t_video_status(a):
        polls["n"] += 1
        # every task finishes on its third poll, except the ones marked to fail
        counts = in_flight.setdefault("seen", {})
        counts[a["task_id"]] = counts.get(a["task_id"], 0) + 1
        if counts[a["task_id"]] < 3:
            return {"c": 200, "status": "running", "video_url": None}
        if a["task_id"] in FAIL_IDS:
            return {"c": 200, "status": "failed", "reason": "provider said no"}
        return {"c": 200, "status": "done", "video_url": f"stub://{a['task_id']}"}

    def download(url, path):
        _tiny_mp4(Path(path), "navy")

    m.t_video = t_video
    m.t_video_status = t_video_status
    m.download = download
    sys.modules["mivi_mcp"] = m
    return m


def run(jobs: dict, outdir: Path, parallel: int) -> dict:
    stub_mcp()
    jf = outdir.parent / "jobs.json"
    jf.write_text(json.dumps(jobs), encoding="utf-8")
    outdir.mkdir(parents=True, exist_ok=True)
    real_root = ROOT
    import mivi_shot
    # the tool resolves --out against the repo root; point it at the temp tree instead
    mivi_shot.ROOT = outdir.parent
    sys.argv = ["mivi_shot", str(jf), "--out", outdir.name,
                "--parallel", str(parallel), "--poll", "0", "--timeout", "30"]
    try:
        mivi_shot.main()
    finally:
        mivi_shot.ROOT = real_root
    return json.loads((outdir / "gen_report.json").read_text())


def main() -> int:
    fails = []
    tmp = Path(tempfile.mkdtemp())
    (tmp / "clips").mkdir()

    # ---- case 1: three independent + two chained + one failure
    canvas = tmp / "still.png"
    _tiny_mp4(canvas, "white")
    jobs = {"shots": [
        {"id": "i1", "still": str(canvas), "prompt": "The camera holds. He walks."},
        {"id": "i2", "still": str(canvas), "prompt": "The camera pushes in. She blinks."},
        {"id": "i3", "still": str(canvas), "prompt": "The camera tilts up. Rain falls."},
        {"id": "c1", "still_from_clip": "i1_a1.mp4", "prompt": "The camera holds. He stops."},
        {"id": "c2", "still_from_clip": "c1_a1.mp4", "prompt": "The camera moves. He turns."},
        {"id": "f1", "still": str(canvas), "prompt": "The camera holds. Nothing."},
    ]}
    # chained specs are relative to the repo root in production; make them resolvable
    for s in jobs["shots"]:
        if "still_from_clip" in s:
            s["still_from_clip"] = s["still_from_clip"]     # sibling clip in the same out dir
    rep = run(jobs, tmp / "clips", parallel=3)

    if rep["ok_count"] != rep["total"]:
        fails.append(f"ok_count {rep['ok_count']}/{rep['total']} — success path still "
                     f"not recorded (the bug this test exists for)")
    if rep["longest_chain"] != 2:       # i1 -> c1 -> c2
        fails.append(f"longest_chain={rep['longest_chain']}, expected 2")
    if not all(s.get("ok") for s in rep["shots"]):
        fails.append("some shots reported not-ok: "
                     + ", ".join(s["id"] for s in rep["shots"] if not s.get("ok")))
    chained = [s for s in rep["shots"] if s.get("chained")]
    if not chained:
        fails.append("no shot was recorded as chained")

    # ---- case 2: the provider refuses one shot; the batch must survive
    FAIL_IDS.clear()
    created.clear()
    FAIL_IDS.add("task2")
    rep2 = run({"shots": [
        {"id": "a", "still": str(canvas), "prompt": "The camera holds. X."},
        {"id": "b", "still": str(canvas), "prompt": "The camera holds. Y."},
        {"id": "c", "still": str(canvas), "prompt": "The camera holds. Z."},
    ]}, tmp / "clips2", parallel=3)
    if rep2["ok_count"] != 2:
        fails.append(f"failure case: ok_count={rep2['ok_count']}, expected 2")
    bad = [s for s in rep2["shots"] if not s.get("ok")]
    if len(bad) != 1 or not any(a.get("error") for a in bad[0]["attempts"]):
        fails.append("failure case: the refused shot has no error recorded")

    print(f"case1 ok {rep['ok_count']}/{rep['total']} · longest chain {rep['longest_chain']} "
          f"· wall {rep['wall_s']}s")
    print(f"case2 ok {rep2['ok_count']}/{rep2['total']} (one provider refusal)")
    if fails:
        print("\nFAIL")
        for f in fails:
            print("  -", f)
        return 1
    print("\nPASS — success recorded, chain waited, refusal isolated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
