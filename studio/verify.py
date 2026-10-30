#!/usr/bin/env python3
"""verify.py — one command that answers "does this repo actually work".

It is deliberately boring and offline:

  1. **inventory**  every tracked .py and .yml is listed in studio/inventory.json,
                    and every listed file exists. Nothing runs unattended.
  2. **data**       every tracked .json parses; every workflow has `on:` and `jobs:`.
  3. **triggers**   every `.*-trigger` file names something that exists.
  4. **smoke**      `--help` on every CLI, `run` on every test/check, `.py` compile.
  5. **links**      every path named in a doc or a script still exists; nothing has
                    grown past the size guard (studio/links.py).
  6. **report**     writes REPO_STATUS.md from what actually happened.

Entries whose dependencies are missing here are SKIPped with the reason — the same
sweep runs again on the runner (`.github/workflows/verify.yml`) where the deps are
installed, and there they must not skip.

    python3 studio/verify.py            # human table + REPO_STATUS.md
    python3 studio/verify.py --quick    # skip the `run` entries (tests are covered by make check)
    python3 studio/verify.py --json
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import py_compile
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INV = ROOT / "studio" / "inventory.json"
REPORT = ROOT / "REPO_STATUS.md"
PY = sys.executable

OK, FAIL, SKIP, WARN = "ok", "FAIL", "skip", "warn"


def tracked(pattern: str = "*") -> list[str]:
    try:
        out = subprocess.run(["git", "ls-files", pattern], cwd=ROOT, capture_output=True,
                             text=True, check=True).stdout
        return [l for l in out.splitlines() if l.strip()]
    except Exception:  # noqa: BLE001
        return [str(p.relative_to(ROOT)) for p in ROOT.rglob(pattern) if p.is_file()]


def missing_deps(names: list[str]) -> list[str]:
    return [n for n in names if importlib.util.find_spec(n) is None]


def missing_bins(names: list[str]) -> list[str]:
    import shutil
    return [n for n in names if shutil.which(n) is None]


def gaps_for(entry: dict) -> list[str]:
    """Python modules first; an executable only counts as missing if there is no
    imageio-ffmpeg to supply it."""
    gaps = missing_deps(entry.get("needs", []))
    bins = entry.get("bins", [])
    if bins and importlib.util.find_spec("imageio_ffmpeg") is None:
        gaps += missing_bins(bins)
    return gaps


# ------------------------------------------------------------------ checks ---
def check_inventory(entries: list[dict]) -> list[tuple[str, str, str]]:
    rows = []
    listed = {e["path"] for e in entries}
    for f in tracked("*.py") + tracked("*.yml"):
        if f not in listed:
            rows.append(("inventory", FAIL, f"{f} is not in studio/inventory.json"))
    for e in entries:
        if not (ROOT / e["path"]).exists():
            rows.append(("inventory", FAIL, f"{e['path']} is listed but does not exist"))
        if e["role"] == "UNCLASSIFIED":
            rows.append(("inventory", FAIL, f"{e['path']} has no role"))
    if not rows:
        rows.append(("inventory", OK, f"{len(entries)} entries, every file accounted for"))
    return rows


def check_data() -> list[tuple[str, str, str]]:
    rows, bad = [], 0
    for f in tracked("*.json"):
        try:
            json.loads((ROOT / f).read_text(encoding="utf-8"))
        except Exception as exc:  # noqa: BLE001
            bad += 1
            rows.append(("data", FAIL, f"{f}: {type(exc).__name__} {exc}"))
    rows.append(("data", OK if not bad else FAIL, f"{len(tracked('*.json')) - bad} json files parse"))
    try:
        import yaml  # noqa: F401
        has_yaml = True
    except Exception:  # noqa: BLE001
        has_yaml = False
    wf_bad = 0
    for f in tracked(".github/workflows/*.yml"):
        text = (ROOT / f).read_text(encoding="utf-8")
        if has_yaml:
            import yaml
            try:
                d = yaml.safe_load(text)
                if not (isinstance(d, dict) and d.get("jobs")):
                    raise ValueError("no jobs:")
            except Exception as exc:  # noqa: BLE001
                wf_bad += 1
                rows.append(("data", FAIL, f"{f}: {exc}"))
        else:
            if not re.search(r"^on:", text, re.M) or not re.search(r"^jobs:", text, re.M):
                wf_bad += 1
                rows.append(("data", FAIL, f"{f}: missing on:/jobs:"))
    rows.append(("data", OK if not wf_bad else FAIL,
                 f"{len(tracked('.github/workflows/*.yml')) - wf_bad} workflows parse"
                 + ("" if has_yaml else " (structural check — pyyaml not installed here)")))
    return rows


LOCAL = {"filmkit", "motionbank", "wanprompt", "shotplan", "mivi_mcp", "imageio_ffmpeg_stub",
         "bank", "links", "voice", "lipsync", "chainkit", "cutlist", "scorer", "motionlint",
         "knowledge", "mivi_video", "render_film", "selftest", "probe", "tools", "mivi_shot", "artgen", "verify", "mivi_photo"}


def declared_imports(path: str) -> set[str]:
    """Third-party imports, read from the file rather than guessed."""
    import ast
    src = (ROOT / path).read_text(encoding="utf-8")
    tree = ast.parse(src)
    names: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names |= {a.name.split(".")[0] for a in node.names}
        elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
            names.add(node.module.split(".")[0])
    # `try: import yaml / except ImportError:` is an optional dependency on purpose,
    # not an undeclared one
    optional: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Try):
            caught = any(
                (isinstance(h.type, ast.Name) and h.type.id in ("ImportError", "ModuleNotFoundError",
                                                               "Exception")) or h.type is None
                for h in node.handlers)
            if caught:
                for sub in ast.walk(ast.Module(body=node.body, type_ignores=[])):
                    if isinstance(sub, ast.Import):
                        optional |= {a.name.split(".")[0] for a in sub.names}
                    elif isinstance(sub, ast.ImportFrom) and sub.module:
                        optional.add(sub.module.split(".")[0])
    std = set(sys.stdlib_module_names) | {"__future__"}
    return {n for n in names if n not in std and n not in LOCAL and n not in optional}


def check_deps(entries: list[dict]) -> list[tuple[str, str, str]]:
    """inventory.json declares what each script needs. This proves the list is right,
    so a missing dep shows up as a skip in the table instead of a crash later."""
    rows = []
    for e in entries:
        if not e["path"].endswith(".py"):
            continue
        try:
            real = declared_imports(e["path"])
        except SyntaxError:
            continue
        declared = set(e.get("needs", []))
        text = (ROOT / e["path"]).read_text(encoding="utf-8")
        undeclared = real - declared
        # a module imported inside a function or a try/except still counts as used
        extra = {d for d in declared - real if d not in text}
        if undeclared:
            rows.append(("deps", FAIL, f"{e['path']}: imports not declared: {', '.join(sorted(undeclared))}"))
        elif extra:
            rows.append(("deps", WARN, f"{e['path']}: declares unused {', '.join(sorted(extra))}"))
    if not rows:
        rows.append(("deps", OK, "every declared dependency matches the file's imports"))
    return rows


def check_triggers() -> list[tuple[str, str, str]]:
    rows = []
    wf_scripts = set()
    for f in tracked(".github/workflows/*.yml"):
        text = (ROOT / f).read_text(encoding="utf-8")
        wf_scripts |= set(re.findall(r"python3? (studio/[\w./-]+\.py)", text))
    for f in sorted(p.name for p in ROOT.glob(".*-trigger")):
        first = (ROOT / f).read_text(encoding="utf-8").strip().splitlines()
        first = first[0].strip() if first else ""
        if not first:
            rows.append(("triggers", FAIL, f"{f}: empty first line"))
        elif first.endswith((".json", ".py", ".txt", ".md")):
            rows.append(("triggers", OK if (ROOT / first).exists() else FAIL,
                         f"{f} -> {first}" + ("" if (ROOT / first).exists() else " (missing)")))
        else:
            rows.append(("triggers", OK, f"{f} -> mode '{first}'"))
    bad = [s for s in wf_scripts if not (ROOT / s).exists()]
    for s in bad:
        rows.append(("triggers", FAIL, f"workflow calls missing script {s}"))
    return rows


def check_links() -> list[tuple[str, str, str]]:
    """Every path mentioned in a doc or a script still exists, and nothing has
    silently grown past the size guard. This is what catches the damage after a
    restructure — stale paths, dead docs, links to files that moved."""
    import subprocess
    try:
        p = subprocess.run([PY, "studio/links.py", "--json"], cwd=ROOT, capture_output=True,
                           text=True, timeout=120)
        d = json.loads(p.stdout)
    except Exception as exc:  # noqa: BLE001
        return [("links", FAIL, f"studio/links.py could not run: {type(exc).__name__}: {exc}")]
    rows = []
    if d.get("breaks"):
        rows.append(("links", FAIL, f"{d['breaks']} broken reference(s) — run studio/links.py"))
    for f in d.get("large_files", []):
        rows.append(("links", FAIL, f"{f} is over the 40 MB guard"))
    for f in d.get("large_files_warn", []):
        rows.append(("links", WARN, f"{f} (over 20 MB, tracked in git)"))
    rows.append(("links", OK if not any(r[1] == FAIL for r in rows) else FAIL,
                 f"{d.get('tracked_files', '?')} files · {d.get('breaks', 0)} breaks"
                 f" · {len(d.get('large_files_warn', []))} size warning(s)"))
    return rows


def run_help(path: str) -> tuple[str, str, str]:
    t0 = time.time()
    try:
        p = subprocess.run([PY, path, "--help"], cwd=ROOT, capture_output=True,
                           text=True, timeout=45)
    except subprocess.TimeoutExpired:
        return ("smoke", FAIL, f"{path} --help hung")
    if p.returncode != 0:
        tail = (p.stderr or p.stdout).strip().splitlines()
        return ("smoke", FAIL, f"{path} --help rc={p.returncode}: {tail[-1][:110] if tail else ''}")
    return ("smoke", OK, f"{path} --help ({time.time() - t0:.1f}s)")


def run_script(path: str) -> tuple[str, str, str]:
    try:
        p = subprocess.run([PY, path], cwd=ROOT, capture_output=True, text=True, timeout=420)
    except subprocess.TimeoutExpired:
        return ("smoke", FAIL, f"{path} timed out")
    tail = ((p.stdout or "") + (p.stderr or "")).strip().splitlines()
    last = tail[-1][:110] if tail else ""
    if p.returncode != 0:
        return ("smoke", FAIL, f"{path} rc={p.returncode}: {last}")
    return ("smoke", OK, f"{path} -> {last}")


def check_smoke(entries: list[dict], quick: bool, ci: bool = False) -> list[tuple[str, str, str]]:
    rows = []
    for e in entries:
        if e["smoke"] == "yaml" or e["smoke"] == "none":
            continue
        lack = gaps_for(e)
        if lack:
            why = f" — {e['why']}" if e.get("why") else ""
            rows.append(("smoke", SKIP, f"{e['path']} needs {', '.join(lack)}{why}"))
            continue
        if e["smoke"] == "run" and quick:
            continue
        r = run_script(e["path"]) if e["smoke"] == "run" else run_help(e["path"])
        rows.append(r)
    if ci:
        # an entry that is supposed to run everywhere must not quietly skip
        ran = {m.split(" ")[0] for g, st, m in rows if st == OK}
        for e in entries:
            if e.get("ci") and e["smoke"] in ("help", "run") and e["path"] not in ran:
                rows.append(("smoke", FAIL,
                             f"{e['path']} did not run (ci=true): needs "
                             f"{', '.join(gaps_for(e)) or 'unknown dependency'}"))
    return rows


def check_compile() -> list[tuple[str, str, str]]:
    rows, bad = [], 0
    with tempfile.TemporaryDirectory() as td:
        for f in tracked("*.py"):
            try:
                py_compile.compile(str(ROOT / f), cfile=str(Path(td) / "x.pyc"), doraise=True)
            except py_compile.PyCompileError as exc:
                bad += 1
                rows.append(("compile", FAIL, f"{f}: {exc.msg.splitlines()[-1][:110]}"))
    rows.append(("compile", OK if not bad else FAIL, f"{len(tracked('*.py')) - bad}/{len(tracked('*.py'))} compile"))
    return rows


def write_report(rows: list[tuple[str, str, str]], meta: dict) -> None:
    by = {}
    for group, status, msg in rows:
        by.setdefault(group, []).append((status, msg))
    counts = {s: sum(1 for _, st, _ in rows if st == s) for s in (OK, FAIL, SKIP, WARN)}
    lines = ["# وضعیت ریپو — ساخته‌شده با اجرا، نه با ادعا", "",
             f"> خودکار از `python3 studio/verify.py` — {meta['when']} · "
             f"پایتون {meta['python']} · {meta['platform']}", "",
             f"| ok | FAIL | skip | warn |", "|---|---|---|---|",
             f"| {counts[OK]} | {counts[FAIL]} | {counts[SKIP]} | {counts[WARN]} |", ""]
    if meta["gaps"]:
        if meta["platform"] == "runner":
            tail = "— روی رانر هم اجرا نشدند"
        else:
            tail = "— نسخهٔ رانر (verify.yml) این‌ها را نصب می‌کند، پس آنجا باید اجرا شوند"
        lines += [f"> ⚠️ {len(meta['gaps'])} وابستگی نصب نیست؛ ردیف‌های وابسته "
                  f"`skip` شده‌اند، نه pass {tail}: " + ", ".join(sorted(meta["gaps"])), ""]
    if meta["skipped_paths"] and meta["platform"] == "runner":
        lines += ["> ⏭️ این " + str(len(meta["skipped_paths"])) + " فایل روی رانر هم اجرا نشد: "
                  + ", ".join(sorted(meta["skipped_paths"])), ""]
    for group in sorted(by):
        lines.append(f"## {group}")
        lines.append("")
        for status, msg in by[group]:
            mark = {OK: "✅", FAIL: "❌", SKIP: "⏭️", WARN: "⚠️"}[status]
            lines.append(f"- {mark} {msg}")
        lines.append("")
    REPORT.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(prog="verify", description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--quick", action="store_true", help="skip `run` entries")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-report", action="store_true")
    ap.add_argument("--ci", action="store_true",
                    help="entries marked ci=true may not skip: a missing dependency fails")
    a = ap.parse_args()

    entries = json.loads(INV.read_text(encoding="utf-8"))["entries"]
    rows: list[tuple[str, str, str]] = []
    rows += check_inventory(entries)
    rows += check_data()
    rows += check_triggers()
    rows += check_deps(entries)
    rows += check_links()
    rows += check_compile()
    rows += check_smoke(entries, a.quick, a.ci)

    gaps = {n for e in entries if e["smoke"] in ("help", "run") for n in gaps_for(e)}
    counts = {s: sum(1 for _, st, _ in rows if st == s) for s in (OK, FAIL, SKIP, WARN)}

    skipped_paths = sorted({m.split(" ")[0] for g, st, m in rows
                            if g == "smoke" and st == SKIP})
    meta = {"when": time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime()),
            "python": sys.version.split()[0],
            "platform": "runner" if os.environ.get("GITHUB_ACTIONS") else "sandbox",
            "gaps": gaps, "skipped_paths": skipped_paths}

    if a.json:
        print(json.dumps({"counts": counts, "gaps": sorted(gaps),
                          "rows": [{"group": g, "status": s, "msg": m} for g, s, m in rows]},
                         indent=2))
        if not a.no_report:
            write_report(rows, meta)
        return 1 if counts[FAIL] else 0
    else:
        for group, status, msg in rows:
            if status == OK and not a.quick:
                continue                      # keep the table readable: show problems
            mark = {OK: "ok  ", FAIL: "FAIL", SKIP: "skip", WARN: "warn"}[status]
            print(f"{mark} [{group:9s}] {msg}")
        print(f"\n{counts[OK]} ok · {counts[FAIL]} failed · {counts[SKIP]} skipped"
              f"{' · deps missing: ' + ', '.join(sorted(gaps)) if gaps else ''}")

    if not a.no_report:
        write_report(rows, meta)
        print(f"-> {REPORT.relative_to(ROOT)}")
    return 1 if counts[FAIL] else 0


if __name__ == "__main__":
    raise SystemExit(main())
