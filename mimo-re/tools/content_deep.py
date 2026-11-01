#!/usr/bin/env python3
"""Stage 8 — deep, at-scale analysis of the bundled curriculum.

Covers schema conformance, referential integrity, ordering, per-entity
inventories, DSL invariants and the character-offset hypothesis that underpins
answer validation.

Usage:
    python tools/content_deep.py ASSETS_DIR OUT_DIR [--langs en,de,fr,...]

ASETS_DIR is the extracted `assets/` directory (contains lessons-<lang>/tracks).

Outputs:
    content-deep.json      summary + all issue lists
    tracks.csv             per-track inventory
    tutorials.csv          per-tutorial inventory (1,029 rows for EN)
    lessons.csv            per-lesson inventory (18,272 rows for EN)
    languages.csv          per-language parity table
"""
from __future__ import annotations

import argparse
import collections
import csv
import json
import os
import re
import statistics

TAG_RE = re.compile(r"<([a-zA-Z][\w]*)((?:\s+[\w:-]+\s*=\s*\"[^\"]*\")*)\s*/?>")
ATTR_RE = re.compile(r"([\w:-]+)\s*=\s*\"([^\"]*)\"")
TEXT_RE = re.compile(r"<text\b([^>]*)/>")
OPTION_RE = re.compile(r"<option\b([^>]*?)/?>")
CODE_BLOCK_RE = re.compile(r"<code\b([^>]*)>(.*?)</code>", re.S)

KNOWN_TAGS = {"html", "body", "p", "code", "content", "text", "interactions", "interaction",
              "options", "option", "selection", "item", "output", "table", "row", "header",
              "data", "database", "tables", "webview", "strong", "em", "br", "img", "a", "head", "style"}
KNOWN_ATTRS = {"value", "type", "visible-if", "startIndex", "endIndex", "correct", "name",
               "version", "content", "codelang", "isDefault", "multiple", "iscode",
               "bootstrapScript", "style", "src", "href", "interaction", "visible"}


def flatten_code(inner: str) -> str:
    """Rebuild the code text an editor shows: <text value> concatenated, break => newline."""
    out = []
    for m in TEXT_RE.finditer(inner):
        attrs = dict(ATTR_RE.findall(m.group(1)))
        if attrs.get("type") == "break":
            out.append("\n")
        else:
            out.append(attrs.get("value", "").replace("&lt;", "<").replace("&gt;", ">")
                       .replace("&quot;", '"').replace("&amp;", "&"))
    return "".join(out)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("assets_dir")
    ap.add_argument("out_dir")
    ap.add_argument("--langs", default="en,de,fr,es,it,pt,pl,ru,tr,id")
    args = ap.parse_args()
    os.makedirs(args.out_dir, exist_ok=True)
    langs = [l.strip() for l in args.langs.split(",") if l.strip()]

    issues = collections.defaultdict(list)
    lang_rows = []
    primary_tut: dict[int, dict] = {}
    tracks_json = None

    for lang in langs:
        base = os.path.join(args.assets_dir, f"lessons-{lang}", "tracks")
        if not os.path.isdir(base):
            issues["missing_language_pack"].append({"lang": lang, "dir": base})
            continue
        tj = json.load(open(os.path.join(base, "tracks.json")))
        files = [f for f in os.listdir(base) if f.startswith("tutorial-") and f.endswith(".json")]
        tut = {}
        for f in files:
            try:
                tut[json.load(open(os.path.join(base, f)))["tutorial"]["id"]] = f
            except Exception as exc:                       # noqa: BLE001
                issues["tutorial_parse_error"].append({"lang": lang, "file": f, "error": str(exc)})
        lessons = 0
        for f in files:
            lessons += sum(len(c["lessons"]) for c in json.load(open(os.path.join(base, f)))["tutorial"]["chapters"])
        lang_rows.append({"lang": lang, "publishSetVersion": tj.get("publishSetVersion"),
                          "tracks": len(tj.get("tracks", [])), "tutorialFiles": len(files),
                          "lessonSlots": lessons})
        if lang == "en":
            tracks_json = tj
            for f in files:
                t = json.load(open(os.path.join(base, f)))["tutorial"]
                primary_tut[t["id"]] = t

    # ---------------- EN deep analysis ----------------
    rows_t, rows_tut, rows_les = [], [], []
    lesson_ids, chapter_ids, tutorial_ids = collections.Counter(), collections.Counter(), set(primary_tut)
    referenced = set()
    gap_stats = collections.Counter()
    range_ok = range_bad = 0
    range_examples = []
    selection_stats = collections.Counter()
    exe_stats = collections.Counter()
    unknown_tags, unknown_attrs, vis_values = collections.Counter(), collections.Counter(), collections.Counter()

    for tid, t in primary_tut.items():
        key_extra = set(t) - {"id", "version", "type", "isNew", "codeLanguage", "title",
                              "descriptionContent", "shortDescriptionContent", "showInTrack",
                              "iconBanner", "chapters"}
        if key_extra:
            issues["tutorial_unexpected_keys"].append({"tutorial": tid, "keys": sorted(key_extra)})
        n_lessons = 0
        for ch in t["chapters"]:
            chapter_ids[ch["id"]] += 1
            for lesson in ch["lessons"]:
                lesson_ids[lesson["id"]] += 1
            n_lessons += len(ch["lessons"])
        rows_tut.append({"tutorialId": tid, "version": t.get("version"), "type": t.get("type"),
                         "codeLanguage": t.get("codeLanguage"), "title": t.get("title"),
                         "chapters": len(t["chapters"]), "lessons": n_lessons})

        for ch in t["chapters"]:
            for lesson in ch["lessons"]:
                c = lesson.get("interactiveContent") or ""
                e = lesson.get("executableContent")
                rec = {"tutorialId": tid, "chapterId": ch["id"], "chapterType": ch.get("type"),
                       "lessonId": lesson["id"], "title": lesson.get("title"),
                       "contentType": lesson.get("contentType"),
                       "hasHardMode": bool(lesson.get("hardModeContent")),
                       "interactions": 0, "selections": 0, "chars": len(c)}
                if c:
                    for tag, attr_blob in TAG_RE.findall(c):
                        if tag not in KNOWN_TAGS:
                            unknown_tags[tag] += 1
                        for a, _ in ATTR_RE.findall(attr_blob):
                            if a not in KNOWN_ATTRS:
                                unknown_attrs[a] += 1
                    for v in re.findall(r'visible-if="([^"]+)"', c):
                        vis_values[v] += 1
                    for m in CODE_BLOCK_RE.finditer(c):
                        flat = flatten_code(m.group(2))
                        options = OPTION_RE.findall(m.group(2))
                        ranges = []
                        for o in options:
                            a = dict(ATTR_RE.findall(o))
                            if "startIndex" in a and "endIndex" in a:
                                try:
                                    ranges.append((int(a["startIndex"]), int(a["endIndex"])))
                                except ValueError:
                                    issues["bad_range_literal"].append({"lesson": lesson["id"]})
                        for s0, e0 in ranges:
                            if 0 <= s0 <= e0 <= len(flat):
                                range_ok += 1
                            else:
                                range_bad += 1
                                if len(range_examples) < 12:
                                    range_examples.append({"lesson": lesson["id"], "range": [s0, e0],
                                                           "flatLen": len(flat)})
                        if ranges:
                            gap_stats[len(ranges)] += 1
                            if any(b[0] < a[1] for a, b in zip(sorted(ranges), sorted(ranges)[1:])):
                                issues["overlapping_ranges"].append({"lesson": lesson["id"], "ranges": ranges})
                    rec["interactions"] = c.count("<interaction ")
                    rec["selections"] = c.count("<selection")
                    for sel in re.findall(r"<selection\b([^>]*)>(.*?)</selection>", c, re.S):
                        items = re.findall(r"<item\b([^>]*)>", sel[1])
                        correct = [i for i in items if re.search(r'correct="true"', i)]
                        selection_stats["total"] += 1
                        if len(items) < 2:
                            issues["selection_too_few_items"].append({"lesson": lesson["id"]})
                        if not correct:
                            issues["selection_no_correct_item"].append({"lesson": lesson["id"]})
                        if len(correct) > 1:
                            selection_stats["multi_correct"] += 1
                        if 'multiple="multiple"' in sel[0]:
                            selection_stats["multiple"] += 1
                if e:
                    exe_stats["lessons"] += 1
                    files = e.get("files") or []
                    exe_stats["files"] += len(files)
                    if not files:
                        issues["executable_without_files"].append({"lesson": lesson["id"]})
                    if not any(f.get("solvedContent") for f in files):
                        issues["executable_without_solution"].append({"lesson": lesson["id"]})
                    idx = e.get("preselectedFileIndex", 0)
                    if not (0 <= idx < max(len(files), 1)):
                        issues["bad_preselected_index"].append({"lesson": lesson["id"], "index": idx})
                    for f in files:
                        if not f.get("content") and f.get("solvedContent"):
                            exe_stats["starter_empty"] += 1
                    if e.get("httpOptions"):
                        exe_stats["http_options"] += 1
                    if e.get("sourceDatabaseTables"):
                        exe_stats["sql_lessons"] += 1
                        try:
                            json.loads(e["sourceDatabaseTables"])
                        except Exception:
                            issues["bad_database_json"].append({"lesson": lesson["id"]})
                rows_les.append(rec)

    # duplicate / integrity
    for lid, n in lesson_ids.items():
        if n > 1:
            issues["duplicate_lesson_id"].append({"lessonId": lid, "count": n})
    for cid, n in chapter_ids.items():
        if n > 1:
            issues["duplicate_chapter_id"].append({"chapterId": cid, "count": n})

    for tr in tracks_json["tracks"]:
        sids = [i for s in tr.get("sections", []) for i in s.get("tutorialIds", [])]
        referenced.update(sids)
        missing = [i for i in sids if i not in tutorial_ids]
        if missing:
            issues["track_references_missing_tutorial"].append({"track": tr["id"], "missing": missing})
        rows_t.append({"trackId": tr["id"], "title": tr["title"],
                       "onboardingCategory": tr.get("onboardingCategory"),
                       "isNew": tr.get("isNew"), "version": tr.get("version"),
                       "sections": len(tr.get("sections", [])), "tutorials": len(sids),
                       "distinctTutorials": len(set(sids)),
                       "chapters": sum(len(primary_tut[i]["chapters"]) for i in sids if i in primary_tut),
                       "lessons": sum(len(c["lessons"]) for i in sids if i in primary_tut
                                      for c in primary_tut[i]["chapters"])})
    orphans = sorted(tutorial_ids - referenced)
    if orphans:
        issues["orphan_tutorials"].append({"count": len(orphans), "ids": orphans[:50]})

    # section ordering consistency
    for tr in tracks_json["tracks"]:
        pos = 0
        for s in tr.get("sections", []):
            if s.get("startIndex") is not None and s["startIndex"] != pos:
                issues["section_index_mismatch"].append({"track": tr["id"], "section": s["name"],
                                                          "startIndex": s["startIndex"], "expected": pos})
            pos += len(s.get("tutorialIds", []))

    for name, rows in (("tracks", rows_t), ("tutorials", rows_tut), ("lessons", rows_les)):
        with open(os.path.join(args.out_dir, f"{name}.csv"), "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
    with open(os.path.join(args.out_dir, "languages.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=list(lang_rows[0].keys()))
        w.writeheader()
        w.writerows(lang_rows)

    summary = {
        "languages": lang_rows,
        "en": {
            "tracks": len(rows_t), "tutorials": len(primary_tut), "lessons": len(rows_les),
            "chapters": sum(int(r["chapters"]) for r in rows_tut),
            "lessonsPerChapter": {
                "mean": round(statistics.mean(len(c["lessons"]) for t in primary_tut.values() for c in t["chapters"]), 2),
                "median": statistics.median(len(c["lessons"]) for t in primary_tut.values() for c in t["chapters"]),
                "max": max(len(c["lessons"]) for t in primary_tut.values() for c in t["chapters"]),
            },
        },
        "dsl": {
            "unknownTags": dict(unknown_tags), "unknownAttributes": dict(unknown_attrs),
            "visibleIfValues": dict(vis_values),
            "interactionBlocksByGapCount": dict(sorted(gap_stats.items())),
            "rangeChecks": {"inBounds": range_ok, "outOfBounds": range_bad},
            "rangeCheckExamples": range_examples,
            "selection": dict(selection_stats),
            "executable": dict(exe_stats),
        },
        "issueCounts": {k: len(v) for k, v in sorted(issues.items())},
        "issues": issues,
    }
    json.dump(summary, open(os.path.join(args.out_dir, "content-deep.json"), "w"), indent=1, ensure_ascii=False)
    print(json.dumps(summary["issueCounts"], indent=1))
    print(json.dumps(summary["dsl"]["rangeChecks"], indent=1))
    print(json.dumps(summary["en"], indent=1))


if __name__ == "__main__":
    main()
