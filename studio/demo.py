"""Live demo of the studio instrument: two chained shots through filmkit verbs.

Proves the CLI's generation path (not just the library), then assembles and QCs.
Draft quality on purpose — this is a wiring test, not a beauty shot.

    python3 studio/demo.py
"""
import json
import pathlib
import subprocess
import sys
import traceback

ROOT = pathlib.Path(".").resolve()
KIT = [sys.executable, str(ROOT / "studio/filmkit.py")]
PROJ = ROOT / "films" / "studio_demo"
START = "http://algo.ufotosoft.com/original/261029/f7cdc842-426b-4423-aa90-d50f38c95b91.jpeg"
LOG = []


def flush_log():
    PROJ.mkdir(parents=True, exist_ok=True)
    (PROJ / "demo_log.txt").write_text("\n".join(LOG), encoding="utf-8")


def kit(*args):
    p = subprocess.run(KIT + [str(a) for a in args], capture_output=True, text=True, timeout=1800)
    LOG.append(f"$ filmkit {' '.join(str(a) for a in args)}  [{p.returncode}]")
    LOG.append((p.stdout or "")[-1500:])
    if p.returncode != 0:
        LOG.append("STDERR: " + (p.stderr or "")[-1500:])
    print(LOG[-2] if p.returncode == 0 else LOG[-1], flush=True)
    flush_log()
    if p.returncode != 0:
        raise RuntimeError(f"filmkit {' '.join(str(a) for a in args)} failed")
    return p.stdout


def run_all():
    kit("new", PROJ, "--force")
    data = json.loads((PROJ / "project.json").read_text())
    data["quality"] = 1
    data["shots"] = [
        {"n": 1, "motion": "the old man turns his head slowly toward the window light, "
                           "camera holds still", "narration": "test one",
         "still": None, "state": "planned", "clip": None, "takes": []},
        {"n": 2, "motion": "he lowers his eyes and the light dims across his face, "
                           "slow push in", "narration": "test two",
         "still": None, "state": "planned", "clip": None, "takes": []},
    ]
    (PROJ / "project.json").write_text(json.dumps(data, indent=2))

    kit("still", PROJ, "--shot", 1, "--from", f"url:{START}")
    kit("shot", PROJ, "--shot", 1, "--quality", 1, "--takes", 1)
    kit("chain", PROJ, "--from", 1, "--to", 2)
    kit("shot", PROJ, "--shot", 2, "--quality", 1, "--takes", 1)
    kit("assemble", PROJ, "--crossfade", 0.4)
    kit("qc", PROJ)
    kit("deliver", PROJ)


if __name__ == "__main__":
    code = 0
    try:
        run_all()
        LOG.append("DEMO OK")
        print("DEMO OK")
    except Exception as exc:
        code = 1
        LOG.append(f"FAILED: {exc}")
        LOG.append(traceback.format_exc()[-2000:])
        print(LOG[-2], flush=True)
    finally:
        flush_log()
    raise SystemExit(code)
