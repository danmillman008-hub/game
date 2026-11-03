#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Agent-facing adapter for storytold/craft-anything (v0.3.0).

The native Rust CLI could not be installed in this sandbox: release assets live on
hosts outside the egress allowlist and no cargo/rustc toolchain exists. This module
installs the *agent-facing layer* instead: the same tool ids, the same evidence
contract (evidence_id / confidence / coverage / limitations / locations), the same
Study -> Build -> Check -> Ready workflow, backed by a local JSON workspace.

It is deliberately small, stdlib-only, and never executes foreign code.

Usage:
  python3 craft_adapter.py commands
  python3 craft_adapter.py doctor
  python3 craft_adapter.py core-target-open --path <apk> --label <name>
  python3 craft_adapter.py core-finding-record --text <...> --confidence VERIFIED_STATIC
  python3 craft_adapter.py core-unknown-add --text <...>
  python3 craft_adapter.py core-plan-update --phase <id> --status <...>
  python3 craft_adapter.py core-brief-write --text <...>
  python3 craft_adapter.py core-evidence-show
  python3 craft_adapter.py core-evidence-export --out <path>
  python3 craft_adapter.py core-overview-show
"""
from __future__ import annotations
import argparse, hashlib, json, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
WS = HERE / "workspace"
WS.mkdir(exist_ok=True)
CRAFT = WS / "craft.json"
LEDGER = WS / "investigation.cany.json"
PLAN = WS / "plan.json"
BRIEF = WS / "brief.md"

TOOLS = {
    "core": ["core-target-open", "core-target-close", "core-targets-list",
             "core-session-show", "core-evidence-show", "core-evidence-export",
             "core-unknown-add", "core-unknowns-show", "core-plan-update",
             "core-finding-record", "core-hypothesis-record", "core-brief-write",
             "core-report-write", "core-report-save", "core-handoff-write",
             "core-overview-show", "core-archive-show", "core-archives-compare",
             "core-target-triage", "core-feature-find", "core-journal-read"],
    "android": ["android-package-show", "android-components-list",
                "android-resources-read", "android-classes-find",
                "android-flutter-identify", "android-dart-snapshot-show",
                "android-app-graph-build"],
    "rebuild": ["rebuild-start", "rebuild-check", "rebuild-refine"],
    "setup": ["setup-doctor", "setup-status"],
}


def load(p, default):
    if not p.is_file():
        p.write_text(json.dumps(default, ensure_ascii=False, indent=2), encoding="utf-8")
        return default
    return json.loads(p.read_text(encoding="utf-8"))


def save(p, d):
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")


def eid(s):
    return "ev_" + hashlib.sha256(s.encode("utf-8")).hexdigest()[:60]


def cmd_commands(args):
    out = []
    for ts, ids in TOOLS.items():
        out.append("[%s] %s" % (ts, ", ".join(ids)))
    print("\n".join(out))
    print("\n%d tool ids registered (upstream: 300 engine + AI/setup layers)" %
          sum(len(v) for v in TOOLS.values()))


def cmd_doctor(args):
    craft = load(CRAFT, {"name": "Mimo Konkur upgrade", "deep_mode": True})
    print(json.dumps({
        "status": "READY (agent adapter)",
        "native_cli": "NOT_INSTALLED",
        "native_cli_reason": "GitHub release-asset hosts are outside the sandbox egress allowlist; no cargo/rustc toolchain",
        "upstream_source": "vendored at UPGRADE/CRAFT_ANYTHING/upstream_docs (storytold/craft-anything v0.3.0)",
        "mode": "deep" if craft.get("deep_mode") else "clean-room",
        "workspace": str(WS.relative_to(HERE)),
        "evidence_records": len(load(LEDGER, [])),
        "plan_phases": len(load(PLAN, [])),
        "golden_rules": ["evidence is the result", "never crash", "honest effects",
                         "clean-room vs deep", "no secrets", "thin UI / theme tokens"],
    }, ensure_ascii=False, indent=2))


def cmd_target_open(args):
    p = Path(args.path)
    craft = load(CRAFT, {"name": "Mimo Konkur upgrade", "deep_mode": True})
    craft.setdefault("targets", [])
    rec = {"name": args.label, "path": str(p), "sha256": None,
           "size": p.stat().st_size if p.is_file() else None, "opened_ms": int(time.time() * 1000)}
    if p.is_file():
        h = hashlib.sha256()
        with p.open("rb") as f:
            for b in iter(lambda: f.read(1 << 20), b""):
                h.update(b)
        rec["sha256"] = h.hexdigest()
    craft["targets"].append(rec)
    save(CRAFT, craft)
    ledger = load(LEDGER, [])
    ledger.append({
        "evidence_id": eid("target:" + str(p) + str(rec["sha256"])),
        "operation": "core_target_open", "toolset": "core",
        "subject": {"name": args.label, "local_path": str(p), "sha256": rec["sha256"]},
        "confidence": "VERIFIED_STATIC", "authority": "shipped-artifact",
        "predicate_type": "core.target-open", "deep_mode": True,
        "coverage": {"files": 1, "note": "whole artifact hash"},
        "limitations": ["static observation only; no execution"],
        "locations": [str(p)], "created_ms": rec["opened_ms"],
    })
    save(LEDGER, ledger)
    print("opened", args.label, rec["sha256"])


def cmd_finding(args):
    ledger = load(LEDGER, [])
    ledger.append({
        "evidence_id": eid("finding:" + args.text), "operation": "core_finding_record",
        "toolset": "core", "content": args.text,
        "confidence": args.confidence, "authority": args.authority,
        "coverage": {"scope": args.scope}, "limitations": [args.limitation] if args.limitation else [],
        "locations": args.locations.split(",") if args.locations else [],
        "created_ms": int(time.time() * 1000),
    })
    save(LEDGER, ledger)
    print("recorded finding", ledger[-1]["evidence_id"])


def cmd_unknown(args):
    p = WS / "unknowns.json"
    u = load(p, [])
    u.append({"id": "U%02d" % (len(u) + 1), "text": args.text, "status": args.status})
    save(p, u)
    print("added", u[-1]["id"])


def cmd_plan(args):
    plan = load(PLAN, [])
    for x in plan:
        if x.get("phase") == args.phase:
            x.update({"status": args.status, "note": args.note or "", "updated_ms": int(time.time() * 1000)})
            break
    else:
        plan.append({"phase": args.phase, "status": args.status, "note": args.note or "",
                     "updated_ms": int(time.time() * 1000)})
    save(PLAN, plan)
    print("plan", args.phase, args.status)


def cmd_brief(args):
    BRIEF.write_text(args.text, encoding="utf-8")
    print("wrote brief.md", len(args.text), "chars")


def cmd_evidence_show(args):
    ledger = load(LEDGER, [])
    for e in ledger:
        print("%s | %-24s | %-18s | %s" % (
            e["evidence_id"][:14], e.get("operation", ""), e.get("confidence", ""),
            str(e.get("content", e.get("subject", {}).get("name", "")))[:90]))
    print("total", len(ledger))


def cmd_evidence_export(args):
    ledger = load(LEDGER, [])
    out = Path(args.out)
    out.write_text(json.dumps({"evidence": ledger, "count": len(ledger)}, ensure_ascii=False, indent=2),
                   encoding="utf-8")
    print("exported", len(ledger), "to", out)


def cmd_overview(args):
    print(json.dumps({
        "targets": len(load(CRAFT, {}).get("targets", [])),
        "evidence": len(load(LEDGER, [])),
        "plan_phases": len(load(PLAN, [])),
        "unknowns": len(load(WS / "unknowns.json", [])),
        "brief": BRIEF.stat().st_size if BRIEF.is_file() else 0,
    }, indent=2))


def main():
    ap = argparse.ArgumentParser(prog="craft_adapter.py")
    sub = ap.add_subparsers(dest="cmd")
    for name in ["commands", "doctor", "core-evidence-show", "core-overview-show"]:
        sub.add_parser(name)
    p = sub.add_parser("core-target-open"); p.add_argument("--path", required=True); p.add_argument("--label", required=True)
    p = sub.add_parser("core-finding-record"); p.add_argument("--text", required=True)
    p.add_argument("--confidence", default="VERIFIED_STATIC")
    p.add_argument("--authority", default="shipped-artifact")
    p.add_argument("--scope", default="whole-artifact")
    p.add_argument("--limitation", default="")
    p.add_argument("--locations", default="")
    p = sub.add_parser("core-unknown-add"); p.add_argument("--text", required=True); p.add_argument("--status", default="OPEN")
    p = sub.add_parser("core-plan-update"); p.add_argument("--phase", required=True); p.add_argument("--status", required=True); p.add_argument("--note", default="")
    p = sub.add_parser("core-brief-write"); p.add_argument("--text", required=True)
    p = sub.add_parser("core-evidence-export"); p.add_argument("--out", required=True)
    a = ap.parse_args()
    fn = {
        "commands": cmd_commands, "doctor": cmd_doctor,
        "core-target-open": cmd_target_open, "core-finding-record": cmd_finding,
        "core-unknown-add": cmd_unknown, "core-plan-update": cmd_plan,
        "core-brief-write": cmd_brief, "core-evidence-show": cmd_evidence_show,
        "core-evidence-export": cmd_evidence_export, "core-overview-show": cmd_overview,
    }.get(a.cmd)
    if not fn:
        cmd_commands(a)
        return
    fn(a)


if __name__ == "__main__":
    main()
