#!/usr/bin/env python3
"""Generate the machine-readable artifacts for the complete-extraction workspace.

Everything here is derived from already-extracted evidence (mimo-re/evidence/*,
mimo-re/data/*) plus a fresh read of the APK for baseline facts. No network, no mutation
of the APK, deterministic output.

Usage:
    python tools/build_machine_artifacts.py APK_PATH MIMO_RE_DIR OUT_DIR

Writes into OUT_DIR: baseline/, ui/, content/, analytics/, dto/, master seeds.
"""
from __future__ import annotations

import argparse
import collections
import csv
import glob
import gzip
import json
import os
import re

RES_KINDS = ("layout", "drawable", "mipmap", "font", "anim", "animator", "navigation", "menu",
             "xml", "raw", "color", "values")


def w(path: str, header: list[str], rows: list[dict]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="", encoding="utf-8") as fh:
        wr = csv.DictWriter(fh, fieldnames=header)
        wr.writeheader()
        for r in rows:
            wr.writerow({k: r.get(k, "") for k in header})
    print(f"  wrote {path} ({len(rows)} rows)")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("apk")
    ap.add_argument("mimo_re")
    ap.add_argument("out")
    args = ap.parse_args()

    from loguru import logger
    logger.remove()
    from androguard.core.apk import APK

    os.makedirs(args.out, exist_ok=True)
    for sub in ("baseline", "ui", "content", "analytics", "dto"):
        os.makedirs(os.path.join(args.out, sub), exist_ok=True)
    ev = os.path.join(args.mimo_re, "evidence")
    data = os.path.join(args.mimo_re, "data")

    # ---------------- baseline ----------------
    apk = APK(args.apk)
    base = {
        "package": apk.get_package(),
        "version_name": apk.get_androidversion_name(),
        "version_code": apk.get_androidversion_code(),
        "min_sdk": apk.get_min_sdk_version(),
        "target_sdk": apk.get_target_sdk_version(),
        "effective_target_sdk": apk.get_effective_target_sdk_version(),
        "permissions": apk.get_permissions(),
        "declared_permissions": apk.get_declared_permissions(),
        "activities": apk.get_activities(),
        "services": apk.get_services(),
        "receivers": apk.get_receivers(),
        "providers": apk.get_providers(),
        "main_activity": apk.get_main_activity(),
        "features": apk.get_features(),
        "libraries": apk.get_libraries(),
        "files": {k: v for k, v in apk.get_files().items()} if isinstance(apk.get_files(), dict) else None,
        "certificates": [str(c) for c in (apk.get_certificates() or [])],
        "signature_names": apk.get_signature_names(),
        "is_signed_v1": apk.is_signed_v1(),
        "is_signed_v2": apk.is_signed_v2(),
        "is_signed_v3": apk.is_signed_v3(),
    }
    try:
        base["certificate_details"] = [
            {"subject": str(cert.subject), "issuer": str(cert.issuer),
             "not_valid_before": str(getattr(cert, "not_valid_before", "")),
             "not_valid_after": str(getattr(cert, "not_valid_after", "")),
             "sha256": str(cert.sha256) if hasattr(cert, "sha256") else ""}
            for cert in (apk.get_certificates() or [])
        ]
    except Exception as exc:  # pragma: no cover
        base["certificate_details_error"] = str(exc)

    json.dump(base, open(os.path.join(args.out, "00_BASELINE", "APK_FACTS.json"), "w"), indent=1, ensure_ascii=False)
    print(f"  baseline: {len(base['permissions'])} permissions, {len(base['activities'])} activities")

    files = apk.get_files()
    ext = collections.Counter()
    for f in files:
        ext[os.path.splitext(f)[1] or "(none)"] += 1
    native = [f for f in files if f.endswith(".so")]
    dexes = sorted(f for f in files if re.match(r"classes\d*\.dex$", f))
    assets = [f for f in files if f.startswith("assets/")]
    json.dump({"file_extensions": dict(ext.most_common(20)), "native_libs": native, "dex_files": dexes,
               "asset_count": len(assets), "total_entries": len(files),
               "assets_tree": sorted({"/".join(a.split("/")[:3]) for a in assets})[:120]},
              open(os.path.join(args.out, "00_BASELINE", "APK_CONTENT_TREE.json"), "w"), indent=1)

    # ---------------- UI: screen inventory + state matrix ----------------
    comp = json.load(open(os.path.join(ev, "components.json")))
    screens = json.load(open(os.path.join(ev, "screens.json")))
    rows = []
    for a in comp["activities"]:
        name = a.get("name") or ""
        exported = str(a.get("exported", "")).lower() == "true"
        rows.append({
            "screen_id": name.split(".")[-1],
            "class": name,
            "kind": "activity",
            "exported": exported,
            "launch_mode": a.get("launchMode", ""),
            "intent_filters": len(a.get("intent_filters") or []),
            "app_owned": name.startswith("com.getmimo."),
            "technology": "view|compose (unresolved per screen)" if name.startswith("com.getmimo.") else "third-party",
        })
    for f in screens.get("fragments", []):
        rows.append({"screen_id": f.split(".")[-1], "class": f, "kind": "fragment", "exported": "",
                     "launch_mode": "", "intent_filters": "", "app_owned": True, "technology": "view binding"})
    for m in screens.get("modals", []):
        rows.append({"screen_id": f"ModalData${m}", "class": f"com.getmimo.ui.introduction.ModalData${m}",
                     "kind": "modal", "exported": "", "launch_mode": "", "intent_filters": "",
                     "app_owned": True, "technology": "modal overlay"})
    for s in screens.get("bottom_sheets", []):
        rows.append({"screen_id": s.split(".")[-1], "class": s, "kind": "bottom_sheet", "exported": "",
                     "launch_mode": "", "intent_filters": "", "app_owned": True, "technology": "view|compose"})
    w(os.path.join(args.out, "03_UI_UX", "SCREEN_INVENTORY.csv"),
      ["screen_id", "class", "kind", "exported", "launch_mode", "intent_filters", "app_owned", "technology"], rows)
    json.dump(rows, open(os.path.join(args.out, "03_UI_UX", "SCREEN_INVENTORY.json"), "w"), indent=1)

    # state matrix: one row per (surface family, state) with evidence string
    states = [
        ("main_navigation", "loading", "loading", "activity_offline_description? no: 'loading'"),
        ("main_navigation", "offline", "activity_offline_description", "resources-strings.xml"),
        ("main_navigation", "error_retry", "generic_error_retry", "resources-strings.xml"),
        ("main_navigation", "empty", "state_empty", "resources-strings.xml"),
        ("onboarding", "loading_plan", "onboarding_curriculum_loading", "resources-strings.xml"),
        ("onboarding", "offline_account", "delayed_account_creation_offline_error", "resources-strings.xml"),
        ("lesson_interactive", "wrong_feedback", "visible-if=\"wrong\" (13,043 modules)", "content-deep.json"),
        ("lesson_interactive", "correct_feedback", "visible-if=\"correct\" (143 modules)", "content-deep.json"),
        ("lesson_interactive", "hint", "interaction_hint_ftg", "resources-strings.xml"),
        ("lesson_interactive", "solution_revealed", "see_solution_use_solution", "resources-strings.xml"),
        ("lesson_executable", "running", "code_header_console_loading", "resources-strings.xml"),
        ("lesson_executable", "tests_failed", "Condition %d / %d/%d checks passed", "string pool"),
        ("lesson_executable", "compiler_error", "compiler_error", "analytics enum literal"),
        ("lesson_executable", "offline_blocked", "executable_lessons_connection_warning", "resources-strings.xml"),
        ("chapter_end", "loading", "chapter_finished_loading", "resources-strings.xml"),
        ("chapter_end", "offline", "chapter_finished_offline_state_description", "resources-strings.xml"),
        ("practice", "filtered_empty", "practice_filter_no_results_description", "resources-strings.xml"),
        ("ai_tutor", "offline", "ai_tutor_offline_description", "resources-strings.xml"),
        ("ai_tutor", "quota_exhausted", "ai_tutor_upgrade_message_count", "resources-strings.xml"),
        ("store", "offline", "store_offline_message", "resources-strings.xml"),
        ("leaderboard", "offline", "leaderboard_offline_message", "resources-strings.xml"),
        ("profile", "anonymous_locked", "profile_anonymous_lock_title", "resources-strings.xml"),
        ("widget", "inactive", "widget_inactive_title", "resources-strings.xml"),
        ("certificate", "not_finished", "CertificateNotFinishedYetModalData", "ModalData class"),
    ]
    w(os.path.join(args.out, "03_UI_UX", "SCREEN_STATE_MATRIX.csv"),
      ["surface", "state", "evidence_literal", "evidence_source"],
      [{"surface": a, "state": b, "evidence_literal": c, "evidence_source": d} for a, b, c, d in states])

    # ---------------- content ----------------
    tracks = list(csv.DictReader(open(os.path.join(ev, "tracks.csv"))))
    tutorials = list(csv.DictReader(open(os.path.join(ev, "tutorials.csv"))))
    lessons = list(csv.DictReader(open(os.path.join(ev, "lessons.csv"))))
    deep = json.load(open(os.path.join(ev, "content-deep.json")))

    inv_rows = []
    for t in tracks:
        inv_rows.append({"entity": "track", "id": t["trackId"], "title": t["title"],
                         "parent": "", "version": t["version"], "sections": t["sections"],
                         "tutorials": t["tutorials"], "chapters": t["chapters"], "lessons": t["lessons"]})
    for ch in sorted({r["chapterId"] for r in lessons}):
        sample = next(r for r in lessons if r["chapterId"] == ch)
        n = sum(1 for r in lessons if r["chapterId"] == ch)
        inv_rows.append({"entity": "chapter", "id": ch, "title": "", "parent": sample["tutorialId"],
                         "version": "", "sections": "", "tutorials": "", "chapters": "",
                         "lessons": n})
    w(os.path.join(args.out, "04_CONTENT_MODEL", "CONTENT_INVENTORY.csv"),
      ["entity", "id", "title", "parent", "version", "sections", "tutorials", "chapters", "lessons"], inv_rows)

    ref_edges = []
    tj = json.load(open(os.path.join("/tmp/x/assets/lessons-en/tracks", "tracks.json")))
    for t in tj["tracks"]:
        for s in t.get("sections", []):
            for tid in s.get("tutorialIds", []):
                ref_edges.append({"from": f"track:{t['id']}", "to": f"tutorial:{tid}",
                                  "section": s.get("name", ""), "startIndex": s.get("startIndex", "")})
    json.dump({"nodes": {"tracks": len(tj["tracks"]), "tutorials": len(tutorials),
                         "chapters": deep["en"]["chapters"], "lessons": deep["en"]["lessons"]},
               "edges": ref_edges}, open(os.path.join(args.out, "04_CONTENT_MODEL", "CONTENT_REFERENCE_GRAPH.json"), "w"), indent=1)

    # ---------------- analytics ----------------
    with gzip.open(os.path.join(ev, "class-strings.json.gz"), "rt", encoding="utf-8") as fh:
        cs = json.load(fh)
    ev_rows = []
    for cls, strs in cs.items():
        if ".analytics." not in cls:
            continue
        snake = [s for s in strs if re.fullmatch(r"[a-z0-9_]{3,60}", s)]
        if not snake:
            continue
        ev_rows.append({"event_or_property": sorted(snake, key=len)[0],
                        "class": cls,
                        "kind": "property" if ".properties." in cls else "event",
                        "all_literals": " | ".join(sorted(snake)[:6])})
    seen = set()
    dedup = []
    for r in sorted(ev_rows, key=lambda x: x["event_or_property"]):
        if r["event_or_property"] in seen:
            continue
        seen.add(r["event_or_property"])
        dedup.append(r)
    w(os.path.join(args.out, "14_ANALYTICS_NOTIFICATIONS", "ANALYTICS_EVENT_CATALOG.csv"),
      ["event_or_property", "class", "kind", "all_literals"], dedup)

    # notifications + deep links
    dl = [{"host": "getmimo.com", "scheme": "https|mimo", "path": "/learn/.*", "target": "MainActivity"},
          {"host": "getmimo.com", "scheme": "https|mimo", "path": "/profile", "target": "MainActivity"},
          {"host": "getmimo.com", "scheme": "https|mimo", "path": "/login", "target": "SplashActivity"},
          {"host": "getmimo.com", "scheme": "https|mimo", "path": "/register", "target": "SplashActivity"},
          {"host": "getmimo.com", "scheme": "mimo", "path": "/deeplink/continuelearning", "target": "SplashActivity"},
          {"host": "getmimo.com", "scheme": "mimo", "path": "/deeplink/support", "target": "SplashActivity"},
          {"host": "cct.com.getmimo", "scheme": "fbconnect", "path": "", "target": "facebook.CustomTabActivity"},
          {"host": "firebase.auth", "scheme": "genericidp", "path": "", "target": "firebase.auth.internal.GenericIdpActivity"},
          {"host": "firebase.auth", "scheme": "recaptcha", "path": "", "target": "firebase.auth.internal.RecaptchaActivity"}]
    w(os.path.join(args.out, "14_ANALYTICS_NOTIFICATIONS", "DEEP_LINKS.csv"),
      ["host", "scheme", "path", "target"], dl)

    # ---------------- dto ----------------
    dc = json.load(open(os.path.join(ev, "data-contracts.json")))
    dto_dir = os.path.join(args.out, "10_BACKEND_API", "DTO_SCHEMA")
    os.makedirs(dto_dir, exist_ok=True)
    made = 0
    for cls, rec in sorted(dc.items()):
        if not rec.get("fields"):
            continue
        name = cls.split(".")[-1].replace("$", "_")
        schema = {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "title": cls,
            "x-evidence": "toString() template in DEX; field list ordered as emitted",
            "x-confidence": "MEDIUM (field presence verified, JSON key casing and nesting not verified)",
            "type": "object",
            "properties": {f: {} for f in rec["fields"]},
        }
        json.dump(schema, open(os.path.join(dto_dir, f"{name}.schema.json"), "w"), indent=1)
        made += 1
    print(f"  wrote {made} DTO schema stubs")

    # ---------------- feature catalogue seed ----------------
    feats = json.load(open(os.path.join(ev, "feature-evidence.json")))
    print(f"  feature seeds available: {len(feats)}")
    print("done")


if __name__ == "__main__":
    main()
