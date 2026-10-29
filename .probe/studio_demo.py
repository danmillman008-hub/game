"""Live demo of the studio instrument: two chained shots through filmkit verbs.

Proves the CLI's generation path (not just the library), then assembles and QCs.
Draft quality on purpose — this is a wiring test, not a beauty shot.
"""
import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(".").resolve()
KIT = [sys.executable, str(ROOT / "studio/filmkit.py")]
PROJ = ROOT / "films" / "studio_demo"
LOG = []


def kit(*args, ok_codes=(0,)):
    p = subprocess.run(KIT + [str(a) for a in args], capture_output=True, text=True, timeout=1800)
    line = f"$ filmkit {' '.join(str(a) for a in args)}  [{p.returncode}]"
    print(line, flush=True); LOG.append(line)
    print((p.stdout or "")[-1200:], flush=True); LOG.append((p.stdout or "")[-1200:])
    if p.returncode not in ok_codes:
        LOG.append((p.stderr or "")[-800:])
        raise SystemExit(f"failed: {p.stderr[-600:]}")
    return p.stdout


START = "http://algo.ufotosoft.com/original/261029/f7cdc842-426b-4423-aa90-d50f38c95b91.jpeg"

kit("new", PROJ, "--force")
data = json.loads((PROJ / "project.json").read_text())
data["shots"] = [
    {"n": 1, "motion": "the old man turns his head slowly toward the window light, "
                       "camera holds still", "narration": "test one",
     "still": None, "state": "planned", "clip": None, "takes": []},
    {"n": 2, "motion": "he lowers his eyes and the light dims across his face, "
                       "slow push in", "narration": "test two",
     "still": None, "state": "planned", "clip": None, "takes": []},
]
data["quality"] = 1
(PROJ / "project.json").write_text(json.dumps(data, indent=2))

kit("still", PROJ, "--shot", 1, "--from", f"url:{START}")
kit("shot", PROJ, "--shot", 1, "--quality", 1, "--takes", 1)
kit("chain", PROJ, "--from", 1, "--to", 2)
kit("shot", PROJ, "--shot", 2, "--quality", 1, "--takes", 1)
kit("assemble", PROJ, "--crossfade", 0.4)
kit("qc", PROJ)
kit("deliver", PROJ)

(PROJ / "demo_log.txt").write_text("\n".join(LOG), encoding="utf-8")
print("DEMO OK")
