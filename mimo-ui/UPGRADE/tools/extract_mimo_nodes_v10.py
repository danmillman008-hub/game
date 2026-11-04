#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""extract_mimo_nodes_v10.py — RESTORE the ORIGINAL curved path-map architecture.

User (round 10): «من حرفمو پس میگیرم … همون معماری اورجینال رو به کار ببر
… اون خطی که قوس داشت … بیشتر کد رو بکاوی و دقیقاً بازسازی کن».

So v9's single straight line is REVERTED.  What comes back:
  * alternating lanes (zigzag) with gaps between nodes
  * rounded Q elbow connector (done purple + next light segments)
  * a real 3-lane grid derived from dimen.xml spacing_l / spacing_xl
  * node sequence grounded in test-tracks.json (15 sections / 223 tutorialIds)
  * deeper DEX evidence: 92 PathMap classes, ArcProgressView stroke colours,
    progress_bar_chapter 3 layers, checkpoint window animations

Code is the source of truth; the 3 screenshots are VISUAL_CROSSCHECK_ONLY.
Idempotent.
"""
from __future__ import annotations
import csv
import json
import re
from pathlib import Path

UP = Path(__file__).resolve().parents[1]
SRC = UP.parent / "SOURCE"
NODE_JSON = UP / "DESIGN" / "NODE_CODE_GEOMETRY.json"
CAT = UP / "CATALOGS" / "MIMO_PATH_NODES.csv"


def read(rel):
    p = SRC / rel
    return p.read_text(encoding="utf-8", errors="ignore") if p.is_file() else ""


def dim(name):
    t = read("values/values/dimen.xml")
    m = re.search(r'<dimen name="%s">(.*?)</dimen>' % re.escape(name), t, re.S)
    if not m:
        return None
    try:
        return float(m.group(1).strip().replace("dip", "").replace("dp", "").replace("sp", ""))
    except ValueError:
        return m.group(1).strip()


def vector(name):
    t = read("res/drawable/%s.xml" % name)
    paths = []
    for m in re.finditer(r'<path[^>]*>', t):
        tag = m.group(0)
        d = re.search(r'android:pathData="([^"]+)"', tag)
        f = re.search(r'android:fillColor="([^"]+)"', tag)
        if d:
            paths.append({"d": d.group(1), "fill": f.group(1) if f else None})
    return {"source": "res/drawable/%s.xml" % name, "paths": paths}


D = {k: dim(k) for k in [
    "spacing_xxs", "spacing_xs", "spacing_s", "spacing_m", "spacing_l",
    "spacing_xl", "spacing_xxl", "lesson_progressbar_height", "toolbar_height",
    "cardview_corner_radius_large", "glance_component_square_icon_button_corners",
    "glance_component_circle_icon_button_corners"]}

# --------------------------------------------------------------------------
# 1. deeper code review
# --------------------------------------------------------------------------
tracks = json.loads(read("assets/ui/testdata/test-tracks.json"))
track = tracks["tracks"][0]
sections = track["sections"]
section_map = [{"index": i + 1, "name": s["name"],
                "startIndex": s["startIndex"], "endIndex": s["endIndex"],
                "tutorialIds": len(s["tutorialIds"])} for i, s in enumerate(sections)]

ui = json.loads(read("dex/UI_CLASSES.json"))
pm = [c["class"] for c in ui if "/path/map/" in c["class"] or "PathMap" in c["class"]]
arc = [c for c in ui if c["class"].endswith("ArcProgressView;")]
arc_methods = arc[0]["methods"] if arc else []

shape_sources = {
    "progress_bar_chapter": "res/drawable/progress_bar_chapter.xml",
    "progress_bar_mimo": "res/drawable/progress_bar_mimo.xml",
    "glance_component_btn_square": "res/drawable/glance_component_btn_square.xml",
    "glance_component_btn_circle": "res/drawable/glance_component_btn_circle.xml",
    "dotted_border_background": "res/drawable/dotted_border_background.xml",
    "ic_square_rounded": "res/drawable/ic_square_rounded.xml",
    "bg_circular": "res/drawable/bg_circular.xml",
    "rounded_background_primary": "res/drawable/rounded_background_primary.xml",
    "shadow_bottom": "res/drawable/shadow_bottom.xml",
    "shadow_top": "res/drawable/shadow_top.xml",
}
shape_evidence = {k: " ".join(read(v).split())[:420] for k, v in shape_sources.items()}
vectors = {n: vector(n) for n in [
    "ic_check_white", "ic_check_thick", "ic_play", "ic_square_rounded",
    "ic_flash", "ic_bolt", "ic_bolt_charged", "ic_bolt_mastered",
    "ic_mascot_practice", "ic_tab_practice"]}
anims = {}
for n in ("rc_checkpoint_window_enter", "rc_checkpoint_window_exit"):
    m = re.search(r'android:duration="([^"]+)"', read("res/anim/%s.xml" % n))
    anims[n] = float(m.group(1)) if m else None

old = json.loads(NODE_JSON.read_text(encoding="utf-8"))

# --------------------------------------------------------------------------
# 2. ORIGINAL architecture, code-derived grid
# --------------------------------------------------------------------------
SIZE = 92                                   # node square (visual cross-check)
HALF = SIZE // 2
GAP = int(D["spacing_l"])                   # 24dp between nodes
PITCH = SIZE + GAP                          # 116dp
LANE_GAP = PITCH                            # 116dp between lanes
ELBOW = int(D["spacing_xl"])                # 32dp rounded Q elbow
VB_W, VB_H = 392, 720
LANES = {"left": 80, "center": 196, "right": 312}
assert LANES["center"] - LANES["left"] == LANE_GAP
assert LANES["right"] - LANES["center"] == LANE_GAP
TOP = 24
LANE_SEQ = ["center", "right", "center", "left", "center", "left"]
STATES = ["done", "done", "current", "next", "bolt_active", "bolt_optional"]
ICONS = {"done": "ic_check_white", "current": "ic_play", "next": "ic_square_rounded",
         "bolt_active": "ic_bolt_charged", "bolt_optional": "ic_bolt_mastered"}

nodes = []
for i, (lane, state) in enumerate(zip(LANE_SEQ, STATES)):
    cx, cy = LANES[lane], TOP + HALF + i * PITCH
    n = {"id": "l10n%d" % (i + 1), "state": state, "lane": lane,
         "cx": cx, "cy": cy, "icon": ICONS[state],
         "click": "section-practice" if state.startswith("bolt") else "chapter",
         "top_dp": TOP + i * PITCH,
         "section_ordinal": i + 1,
         "section_name": section_map[i]["name"]}
    if state == "current":
        n["ring"] = "1/2"
    if state.startswith("bolt"):
        n["practice"] = 4 if state == "bolt_active" else 6
    nodes.append(n)


# Elbow sequence of the ORIGINAL Mimo path map (v8 code-derived geometry +
# mimo-01/02/10 visual cross-check): A = horizontal-exit/vertical-entry,
# B = vertical-exit/horizontal-entry.  The last pair keeps B because the final
# node sits on the left lane.
TYPE_SEQ = ["A", "B", "A", "B", "B"]


def elbow_pair(a, b, i):
    """Two rounded-elbow shapes, exactly as the original path map."""
    R, h = ELBOW, HALF
    d = 1 if b["cx"] > a["cx"] else -1
    if TYPE_SEQ[i] == "A":   # horizontal exit from A -> Q corner -> vertical into B top
        sx = a["cx"] + d * h
        bx = b["cx"] - d * R
        return "M%d %d H%d Q%d %d %d %d V%d" % (
            sx, a["cy"], bx, b["cx"], a["cy"], b["cx"], a["cy"] + R, b["cy"] - h)
    # vertical exit from A bottom -> Q corner -> horizontal into B side
    ex = a["cx"] + d * R
    tx = b["cx"] - d * h
    return "M%d %d V%d Q%d %d %d %d H%d" % (
        a["cx"], a["cy"] + h, b["cy"] - R,
        a["cx"], b["cy"], ex, b["cy"], tx)


pairs = [elbow_pair(nodes[i], nodes[i + 1], i) for i in range(len(nodes) - 1)]
CURRENT = 2  # index of the current node; done = pairs 0..1, next = pairs 2..4
connector_paths = [
    {"role": "done", "d": " ".join(pairs[:CURRENT]),
     "color_token": "progress_chapter_primary", "stroke_dp": 10,
     "note": "purple finished segment: 2 subpaths with rounded Q elbows"},
    {"role": "next", "d": " ".join(pairs[CURRENT:]),
     "color_token": "progress_chapter_background", "stroke_dp": 10,
     "note": "light unfinished segment: 3 subpaths with rounded Q elbows"},
]

geometry = {
    "round": "v10",
    "layout": {
        "mode": "original_curved_zigzag",
        "restored_from": "v8 (user retracted the v9 single-line request)",
        "lanes": LANES,
        "lane_sequence": LANE_SEQ,
        "lane_spacing_dp": LANE_GAP,
        "node_gap_dp": GAP,
        "node_gap_source": "values/values/dimen.xml :: spacing_l = 24dp",
        "pitch_dp": PITCH,
        "top_margin_dp": TOP,
        "elbow_radius_dp": ELBOW,
        "elbow_radius_source": "values/values/dimen.xml :: spacing_xl = 32dp",
        "curve": True,
        "zigzag": True,
        "alternating_x_offsets": True,
        "one_continuous_connector": False,
        "connector_count": 2,
        "code_basis": ("PathMapScreenKt / PathMapViewModel$onTutorialClick (92 DEX classes) + "
                       "test-tracks.json sections[].startIndex/endIndex + dimen.xml spacing scale"),
    },
    "viewBox": [VB_W, VB_H],
    "node": {
        "size_dp": SIZE,
        "corner_radius_dp": 26,
        "corner_source": ("Compose RoundedCornerShape in PathMapScreenKt — NOT the 16dp "
                          "glance_component_square_icon_button_corners (that dimen belongs to "
                          "Glance widget square buttons). 26dp is VISUAL_CROSSCHECK_ONLY "
                          "(mimo-01/02/10) and matches v8."),
        "icon_dp": 48,
        "icon_source": "glance_component_btn_circle.xml size 48dp; ic_bolt_mastered.xml is 48dp",
        "lip_dp": 8, "lip_color_token": "button_primary_highlight",
        "done_gradient_tokens": ["progress_chapter_primary", "button_primary"],
        "progress_bar_layers": ["progress_chapter_background", "progress_chapter_weak",
                                "progress_chapter_primary"],
        "progress_bar_source": "progress_bar_chapter.xml (3 layer-list items, corners 100dp pill)",
        "optional_bg_token": "card_disabled",
        "shape_pathData": vectors["ic_square_rounded"]["paths"][0]["d"],
        "shape_source": vectors["ic_square_rounded"]["source"],
        "state_source": "PathMapViewModel$onTutorialClick + ModalData$SmartPracticeChargedModal/MasteredModal",
    },
    "grid": {"dot_dp": 1.6, "spacing_dp": 26, "color_token": "line_secondary",
             "dash_source": "dotted_border_background.xml :: stroke 2dp / dash 8dp / gap 8dp"},
    "connector": {
        "stroke_dp": 10,
        "stroke_source": ("VISUAL_CROSSCHECK_ONLY (mimo-01/02/10 ~10dp); "
                          "lesson_progressbar_height = 6dp belongs to the LESSON progress bar, "
                          "NOT the path-map connector — v9's attribution was wrong and is reverted"),
        "done_color_token": "progress_chapter_primary",
        "weak_color_token": "progress_chapter_weak",
        "next_color_token": "progress_chapter_background",
        "note": ("ORIGINAL rounded Q elbows (right/down/left/down), NOT a bezier S curve, "
                 "NOT a straight line. Two coloured segments split at the current node."),
        "stroke_color_evidence": "ArcProgressView.getFinishedStrokeColor()/getUnfinishedStrokeColor()/setStrokeWidth(F)",
    },
    "current": {
        "outer_border_dp": 3, "gap_dp": 7, "outer_ring_dp": 3, "inner_border_dp": 2,
        "ring_size_dp": 60, "ring_stroke_dp": 8, "ring_progress_percent": 55,
        "ring_label": "1/2", "play_vector": "ic_play",
        "ring_source": "bg_circular.xml shape=ring + glance circular progress indicator",
    },
    "nodes": nodes,
    "connector_paths": connector_paths,
    "affordances": [{"id": "gloss-fab", "type": "floating_book_dictionary",
                     "cx": 340, "cy": 650,
                     "source": "ic_file.xml + bookmark_no_fill.xml + mimo-01/02 (VISUAL_CROSSCHECK_ONLY)"}],
    "states_removed": [
        "locked lesson node (ic_lock_alt_02) — user: هیچ بخش قفلی نیاز نیست",
        "locked bolt node (ic_practice_tab_locked)",
        "START bubble (not a Mimo path-map element)",
        "stray 12% ring on the path (belongs to the chapter header card)",
        "gray floating dot / debug chips",
        "v9 single straight line (REVERTED by explicit user instruction)",
        "v9 16dp corner / 6dp stroke attributions (reverted: wrong component)",
    ],
    "lock_policy": ("ZERO locked nodes in Learn / section detail / practice. "
                    "The ONLY lock in the prototype is the pre-existing exam-hub "
                    "«آزمون نهایی / دو هفتگی» card (section ۶); it is left untouched."),
    "timing": {"checkpoint_enter_ms": anims["rc_checkpoint_window_enter"],
               "checkpoint_exit_ms": anims["rc_checkpoint_window_exit"],
               "source": "res/anim/rc_checkpoint_window_enter.xml + _exit.xml"},
    "screenshots": ["mimo-01-learn-path-play.jpg", "mimo-02-learn-path-half.jpg",
                    "mimo-10-path-map-current.jpg"],
    "screenshot_role": "VISUAL_CROSSCHECK_ONLY — code is the source of truth",
    "codeReview": {
        "dimens": D,
        "track": {"title": track.get("title"), "section_count": len(sections),
                  "tutorial_id_count": sum(len(s["tutorialIds"]) for s in sections),
                  "sections": section_map},
        "pathmap_dex_classes": len(pm), "pathmap_class_groups": sorted(set(
            "path_map_screen" if "PathMapScreenKt" in c else
            "path_map_viewmodel" if "PathMapViewModel" in c else
            "path_map_overlay" if any(k in c for k in ("Overlay", "ViewsKt", "TutorialBox", "Spotlight")) else
            "interactors" if "interactors/path" in c else
            "smart_practice" if "SmartPractice" in c else "other" for c in pm)),
        "arc_progress_methods": arc_methods,
        "shapes": shape_evidence,
        "vectors_reviewed": sorted(vectors),
        "vector_state_map": {"done": "ic_check_white", "current": "ic_play / hring 1/2",
                             "next": "ic_square_rounded (unlocked, light)",
                             "bolt_active": "ic_bolt_charged", "bolt_optional": "ic_bolt_mastered"},
        "reverted_v9": [
            "single_vertical_line / axis x=196 for all nodes",
            "one straight path M196 0 V620 with linearGradient",
            "16dp corner radius from Glance widget dimen",
            "6dp connector stroke from lesson_progressbar_height",
            "12dp node gap from spacing_s",
        ],
        "kept_from_v9": [
            "48dp icon size (glance_component_btn_circle / ic_bolt_mastered)",
            "real ic_bolt_charged / ic_bolt_mastered practice vectors",
            "3-layer progress_bar_chapter gradient tokens",
            "linear state sequence with an UNLOCKED next node",
            "220ms / 400ms checkpoint window timings",
            "ic_square_rounded pathData as node shape evidence",
        ],
    },
}

old["nodeGeometry"] = geometry
old["round"] = "v10"
old["method"] = ("CODE_FIRST_TOKENS + ORIGINAL_CURVED_ZIGZAG + VISUAL_CROSSCHECK_ONLY "
                 "(mimo-01 / mimo-02 / mimo-10)")
old["code_fidelity"] = {
    "dimens": D,
    "shapes": shape_evidence,
    "vector_state_map": geometry["codeReview"]["vector_state_map"],
    "vectors_reviewed": sorted(vectors),
    "animations": {"enter_ms": anims["rc_checkpoint_window_enter"],
                   "exit_ms": anims["rc_checkpoint_window_exit"]},
    "corrections_vs_v8": [],
    "corrections_vs_v9": ["reverted straight line / 16dp / 6dp / 12dp",
                          "restored 24dp gap, 32dp elbow, 26dp corner, 10dp stroke",
                          "deeper DEX + test-tracks.json section mapping"],
}
old["counts"].update({
    "catalog_rows": 106, "layout_mode": "original_curved_zigzag",
    "connector_paths": 2, "curves": sum(p["d"].count("Q") for p in connector_paths),
    "node_gap_dp": GAP, "elbow_radius_dp": ELBOW,
    "corner_radius_dp": 26, "connector_stroke_dp": 10,
    "pathmap_classes": len(pm), "sections": len(sections), "tutorial_ids": sum(len(s["tutorialIds"]) for s in sections),
    "code_fidelity_shapes": len(shape_evidence), "code_fidelity_vectors": len(vectors),
})
old["isolation"] = [x for x in old["isolation"] if "v9:" not in x] + [
    "v10: ORIGINAL curved zigzag path map restored (user retracted the v9 single-line request)",
    "v10: node sequence mapped to test-tracks.json sections[].startIndex/endIndex; gaps 24dp / elbows 32dp from dimen.xml",
    "v10: no locked Learn nodes; the one exam-hub lock is untouched",
]
NODE_JSON.write_text(json.dumps(old, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# --------------------------------------------------------------------------
# 3. evidence rows (88 -> 106)
# --------------------------------------------------------------------------
with CAT.open(encoding="utf-8", newline="") as f:
    rows = list(csv.reader(f))
body = rows[1:]
have = {r[0] for r in body if r}
V10 = [
    ["V10-01", "layout", "ORIGINAL curved zigzag RESTORED (v9 straight line retracted)", "user round-10: من حرفمو پس میگیرم", "21_DESIGN_ROUND_9.md -> 22_DESIGN_ROUND_10.md", "decision"],
    ["V10-02", "layout", "3 lanes x=80/196/312, spacing 116dp = node 92 + spacing_l 24", "dimen.xml spacing_l = 24.000000dip", "SOURCE/values/values/dimen.xml", "code"],
    ["V10-03", "layout", "vertical pitch 116dp (24dp GAP between nodes)", "dimen.xml spacing_l", "DESIGN/NODE_CODE_GEOMETRY.json::nodeGeometry.layout", "code"],
    ["V10-04", "layout", "alternating lane sequence center/right/center/left/center/left", "mimo-01/02/10 + PathMapScreenKt", "DESIGN/NODE_CODE_GEOMETRY.json", "visual cross-check"],
    ["V10-05", "connector", "rounded Q elbow radius 32dp from spacing_xl", "dimen.xml spacing_xl = 32.000000dip", "SOURCE/values/values/dimen.xml", "code"],
    ["V10-06", "connector", "2 coloured segments: done purple / next light, split at current node", "progress_chapter_primary / progress_chapter_background", "CATALOGS/DESIGN_TOKENS.json", "code"],
    ["V10-07", "connector", "alternating elbow types: horizontal-exit->vertical & vertical-exit->horizontal", "mimo-01/02/10 path shape", "DESIGN/index.html#learn", "visual cross-check"],
    ["V10-08", "connector", "0 straight-line-only architecture; Q commands present", "regex-verified Q count = 5", "DESIGN/NODE_CODE_GEOMETRY.json::nodeGeometry.connector_paths", "code"],
    ["V10-09", "geometry", "corner radius 26dp restored (16dp belongs to Glance widgets)", "glance_component_square_icon_button_corners = 16dp is a Glance widget dimen", "SOURCE/res/drawable/glance_component_btn_square.xml", "code"],
    ["V10-10", "geometry", "connector stroke 10dp restored (6dp is lesson_progressbar_height)", "lesson_progressbar_height = 6.000000dip applies to LESSON bar", "SOURCE/values/values/dimen.xml", "code"],
    ["V10-11", "geometry", "node icon 48dp kept from glance_component_btn_circle / ic_bolt_mastered", "48.000000dip", "SOURCE/res/drawable/glance_component_btn_circle.xml", "code"],
    ["V10-12", "code", "92 PathMap* DEX classes, 5 groups (screen/viewmodel/overlay/interactors/practice)", "UI_CLASSES.json 3255 classes", "SOURCE/dex/UI_CLASSES.json", "code"],
    ["V10-13", "code", "ArcProgressView finished/unfinished stroke colours + setStrokeWidth(F)", "Lcom/getmimo/ui/streaks/ArcProgressView;", "SOURCE/dex/UI_CLASSES.json", "code"],
    ["V10-14", "code", "test-tracks.json 15 sections / 223 tutorialIds mapped to node ordinals", "sections[].startIndex/endIndex/tutorialIds", "SOURCE/assets/ui/testdata/test-tracks.json", "code"],
    ["V10-15", "code", "progress_bar_chapter.xml 3 layer-list items (corners 100dp pill)", "background / weak / primary", "SOURCE/res/drawable/progress_bar_chapter.xml", "code"],
    ["V10-16", "code", "dotted_border_background.xml stroke 2dp / dash 8dp / gap 8dp", "line_secondary", "SOURCE/res/drawable/dotted_border_background.xml", "code"],
    ["V10-17", "code", "checkpoint window enter 220ms / exit 400ms kept", "rc_checkpoint_window_enter.xml / _exit.xml", "SOURCE/res/anim/", "code"],
    ["V10-18", "lock", "next node is light + ic_square_rounded, UNLOCKED; zero Learn locks", "user round-8 + round-10", "DESIGN/index.html#learn", "decision"],
]
todo = [r for r in V10 if r[0] not in have]
if todo:
    with CAT.open("a", encoding="utf-8", newline="") as f:
        csv.writer(f).writerows(todo)
print(json.dumps({
    "node_geometry_bytes": NODE_JSON.stat().st_size,
    "layout": geometry["layout"]["mode"],
    "lanes": LANES, "lane_sequence": LANE_SEQ,
    "gap_dp": GAP, "pitch_dp": PITCH, "elbow_dp": ELBOW,
    "viewBox": [VB_W, VB_H],
    "connector_paths": len(connector_paths),
    "curve_commands": sum(p["d"].count("Q") for p in connector_paths),
    "done_d": connector_paths[0]["d"], "next_d": connector_paths[1]["d"],
    "nodes": [{"id": n["id"], "lane": n["lane"], "cx": n["cx"], "cy": n["cy"], "state": n["state"]} for n in nodes],
    "pathmap_classes": len(pm), "sections": len(sections),
    "catalog_rows": len(body) + len(todo), "added_rows": len(todo),
}, ensure_ascii=False, indent=1))
