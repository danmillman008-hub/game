#!/usr/bin/env python3
"""Stage 2 — semantic analysis of the bundled curriculum.

Mimo ships its whole curriculum as JSON inside assets/lessons-<lang>/tracks/:
    tracks.json              -> publishSetVersion + tracks[].sections[].tutorialIds[]
    tutorial-<id>.json       -> tutorial.chapters[].lessons[]
    lesson.interactiveContent  (XML-like DSL: <code>/<interaction>/<selection> ...)
    lesson.executableContent   (multi-file projects + solvedContent + hints)

This script rebuilds the content model and the curriculum map, and counts the
pedagogy-relevant vocabulary (interaction types, visibility conditions,
hard-mode variants, project lessons, languages).

Usage:
    python3 tools/analyze_content.py extracted_apk_dir out/

    # where extracted_apk_dir/assets/lessons-en/tracks exists
"""
import collections
import json
import os
import re
import statistics
import sys

TAG_RE = re.compile(r"<([a-zA-Z][\w]*)((?:\s+[\w:-]+=\"[^\"]*\")*)\s*/?>")
VISIBLE_RE = re.compile(r'visible-if="([^"]+)"')
INTERACTION_RE = re.compile(r'<interaction type="([^"]+)"')


def track_summary(tut, tracks):
    rows = []
    for tr in tracks:
        ids = [i for s in tr.get("sections", []) for i in s.get("tutorialIds", [])]
        chapters = sum(len(tut[i]["chapters"]) for i in ids if i in tut)
        lessons = sum(len(c["lessons"]) for i in ids if i in tut for c in tut[i]["chapters"])
        inter = 0
        for i in ids:
            if i not in tut:
                continue
            for ch in tut[i]["chapters"]:
                for lesson in ch["lessons"]:
                    inter += (lesson.get("interactiveContent") or "").count("<interaction ")
        rows.append({
            "id": tr["id"],
            "title": tr["title"],
            "publishVersion": tr.get("version"),
            "sections": len(tr.get("sections", [])),
            "tutorials": len(ids),
            "chapters": chapters,
            "lessons": lessons,
            "interactions": inter,
            "tutorialTypes": dict(collections.Counter(
                tut[i].get("type") for i in ids if i in tut)),
            "chapterTypes": dict(collections.Counter(
                ch.get("type") for i in ids if i in tut for ch in tut[i]["chapters"])),
            "sectionList": [{"name": s["name"], "description": s.get("description"),
                             "startIndex": s.get("startIndex"), "endIndex": s.get("endIndex"),
                             "tutorialCount": len(s.get("tutorialIds", []))}
                            for s in tr.get("sections", [])],
        })
    return rows


def main(extracted_dir: str, out_dir: str, lang: str = "en"):
    base = os.path.join(extracted_dir, "assets", f"lessons-{lang}", "tracks")
    os.makedirs(out_dir, exist_ok=True)
    tracks_json = json.load(open(os.path.join(base, "tracks.json")))
    tut = {}
    for name in os.listdir(base):
        if name.startswith("tutorial-") and name.endswith(".json"):
            t = json.load(open(os.path.join(base, name)))["tutorial"]
            tut[t["id"]] = t

    def scan(include_hard_mode: bool):
        """Count DSL vocabulary for the base lesson body or base + Hard Mode variant."""
        tags, attrs, vis, inter = (collections.Counter() for _ in range(4))
        wrong_feedback = multi_select = items = 0
        lengths = []
        for t in tut.values():
            for ch in t["chapters"]:
                for lesson in ch["lessons"]:
                    bodies = [lesson.get("interactiveContent") or ""]
                    if include_hard_mode:
                        bodies.append(lesson.get("hardModeContent") or "")
                    bodies = [b for b in bodies if b]
                    if any('visible-if="wrong"' in b for b in bodies):
                        wrong_feedback += 1
                    for c in bodies:
                        lengths.append(len(c))
                        for tag, attr_blob in TAG_RE.findall(c):
                            tags[tag] += 1
                            for a in re.findall(r'([\w:-]+)="', attr_blob):
                                attrs[a] += 1
                        for it in INTERACTION_RE.findall(c):
                            inter[it] += 1
                        for v in VISIBLE_RE.findall(c):
                            vis[v] += 1
                        multi_select += c.count("<selection")
                        items += len(re.findall(r"<item ", c))
        return {
            "interactionTypes": dict(inter),
            "assessedSteps": sum(inter.values()) + multi_select,
            "visibilityConditions": dict(vis),
            "tags": dict(tags.most_common(30)),
            "attributes": dict(attrs.most_common(30)),
            "multiSelectQuestions": multi_select,
            "multiSelectItems": items,
            "lessonsWithCorrectiveFeedback": wrong_feedback,
            "interactiveContentChars": {
                "mean": round(statistics.mean(lengths)), "median": statistics.median(lengths)},
        }

    content_types, chapter_types, tutorial_types = (collections.Counter() for _ in range(3))
    lessons = hard_mode = executable = visual = with_hints = 0
    for t in tut.values():
        tutorial_types[t.get("type")] += 1
        for ch in t["chapters"]:
            chapter_types[ch.get("type")] += 1
            for lesson in ch["lessons"]:
                lessons += 1
                content_types[lesson.get("contentType")] += 1
                if lesson.get("hardModeContent"):
                    hard_mode += 1
                e = lesson.get("executableContent")
                if e:
                    executable += 1
                    if e.get("hasVisualOutput"):
                        visual += 1
                    if e.get("hints"):
                        with_hints += 1

    base = scan(False)
    with_hard = scan(True)

    stats = {
        "language": lang,
        "publishSetVersion": tracks_json.get("publishSetVersion"),
        "tracks": len(tracks_json["tracks"]),
        "tutorials": len(tut),
        "chapters": sum(len(t["chapters"]) for t in tut.values()),
        "lessons": lessons,
        "lessonsPerChapter": {
            "mean": round(statistics.mean(len(c["lessons"]) for t in tut.values() for c in t["chapters"]), 1),
            "median": statistics.median(len(c["lessons"]) for t in tut.values() for c in t["chapters"]),
            "max": max(len(c["lessons"]) for t in tut.values() for c in t["chapters"]),
        },
        "contentTypes": dict(content_types),
        "chapterTypes": dict(chapter_types),
        "tutorialTypes": dict(tutorial_types),
        "lessonsWithHardMode": hard_mode,
        "executableLessons": executable,
        "executableWithVisualOutput": visual,
        "executableWithHints": with_hints,
        "dsl": {"baseOnly": base, "includingHardMode": with_hard},
    }
    json.dump(stats, open(os.path.join(out_dir, "content_stats.json"), "w"), indent=1)
    json.dump({"publishSetVersion": tracks_json.get("publishSetVersion"),
               "tracks": track_summary(tut, tracks_json["tracks"])},
              open(os.path.join(out_dir, "curriculum-map.json"), "w"), indent=1, ensure_ascii=False)
    print(json.dumps(stats, indent=1)[:4000])


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "out",
         sys.argv[3] if len(sys.argv) > 3 else "en")
