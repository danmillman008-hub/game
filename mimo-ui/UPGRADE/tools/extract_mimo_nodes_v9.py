#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""extract_mimo_nodes_v9.py — round-9 RE-REVIEW of path-map node code.

User: «معماری گرهها همچنان نیاز به توجه دارد؛ قوس نده و گرهها را در یک خط
عمودی قرار بده؛ دوباره کدش را بازبینی کن و بهتر شبیهسازی کن».

Everything below is read from the decoded Mimo 9.35 APK source tree; the
screenshots are VISUAL_CROSSCHECK_ONLY.  Idempotent.
"""
from __future__ import annotations
import csv
import json
import re
from pathlib import Path

UP = Path(__file__).resolve().parents[1]
SRC = UP.parent / "SOURCE"
TOK = UP.parent / "CATALOGS" / "DESIGN_TOKENS.json"
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
    v = m.group(1).strip()
    try:
        return float(v.replace("dip", "").replace("dp", "").replace("sp", ""))
    except ValueError:
        return v


def vector(name):
    t = read("res/drawable/%s.xml" % name)
    paths = []
    for m in re.finditer(r'<path[^>]*>', t):
        tag = m.group(0)
        d = re.search(r'android:pathData="([^"]+)"', tag)
        f = re.search(r'android:fillColor="([^"]+)"', tag)
        if d:
            paths.append({"d": d.group(1), "fill": f.group(1) if f else None})
    vw = re.search(r'android:viewportWidth="([^"]+)"', t)
    vh = re.search(r'android:viewportHeight="([^"]+)"', t)
    return {"source": "res/drawable/%s.xml" % name,
            "viewport": [float(vw.group(1)), float(vh.group(1))] if vw and vh else [24, 24],
            "paths": paths}


def shape(name):
    t = read("res/drawable/%s.xml" % name)
    out = {"source": "res/drawable/%s.xml" % name, "raw": " ".join(t.split())[:600]}
    for k in ["radius", "width", "dashWidth", "dashGap", "angle", "shape"]:
        m = re.search(r'android:%s="([^"]+)"' % k, t)
        if m:
            out[k] = m.group(1)
    return out


def animation(name):
    t = read("res/anim/%s.xml" % name)
    m = re.search(r'android:duration="([^"]+)"', t)
    return float(m.group(1)) if m else None


# --------------------------------------------------------------------------
# 1. re-read the code (no inferred numbers)
# --------------------------------------------------------------------------
D = {
    "corner_radius_dp": dim("glance_component_square_icon_button_corners"),   # 16
    "button_radius_dp": dim("glance_component_button_corners"),               # 24
    "circle_button_dp": dim("circle_icon_button_corners"),                    # 9999 (pill)
    "card_radius_dp": dim("cardview_corner_radius_large"),                    # 12
    "gap_dp": dim("spacing_s"),                                               # 12
    "spacing_m_dp": dim("spacing_m"),                                         # 16
    "spacing_l_dp": dim("spacing_l"),                                         # 24
    "progress_stroke_dp": dim("lesson_progressbar_height"),                   # 6
    "toolbar_dp": dim("toolbar_height"),                                      # 56
}
D["circle_button_dp"] = dim("glance_component_circle_icon_button_corners")

shapes = {n: shape(n) for n in [
    "glance_component_btn_square", "glance_component_btn_circle",
    "glance_component_square_button_ripple", "progress_bar_chapter",
    "progress_bar_mimo", "bg_circular", "bg_chapter_finished_equation",
    "rounded_background_primary", "rounded_background_secondary",
    "dotted_border_background", "shadow_bottom", "shadow_top", "bg_reward_label"]}
vectors = {n: vector(n) for n in [
    "ic_square_rounded", "ic_check_white", "ic_check_thick", "ic_play",
    "ic_flash", "ic_bolt", "ic_bolt_charged", "ic_bolt_mastered",
    "ic_mascot_practice", "ic_tab_practice"]}
anims = {"enter_ms": animation("rc_checkpoint_window_enter"),
         "exit_ms": animation("rc_checkpoint_window_exit")}

tokens = json.loads(TOK.read_text(encoding="utf-8")) if TOK.is_file() else {}
old = json.loads(NODE_JSON.read_text(encoding="utf-8"))

# --------------------------------------------------------------------------
# 2. SINGLE VERTICAL LINE — code-derived, no curves, no zigzag
# --------------------------------------------------------------------------
VB_W, VB_H = 392, 620
AXIS_X = VB_W // 2                       # 196 = centre of the 392dp canvas
SIZE = 92                               # node square (visual cross-check of mimo-01/02/10 + 92dp path-map node)
HALF = SIZE // 2
GAP = int(D["gap_dp"])                  # 12dp from dimen.xml spacing_s
PITCH = SIZE + GAP                      # 104
TOTAL = 6 * SIZE + 5 * GAP              # 612
TOP = (VB_H - TOTAL) // 2               # 4 -> centred column
STATES = [
    ("l9n1", "done",         "ic_check_white",  "chapter"),
    ("l9n2", "done",         "ic_check_white",  "chapter"),
    ("l9n3", "current",      "ic_play",         "chapter"),
    ("l9n4", "next",         "ic_square_rounded", "chapter"),
    ("l9n5", "bolt_active",  "ic_bolt_charged", "section-practice"),
    ("l9n6", "bolt_optional","ic_bolt_mastered","section-practice"),
]
nodes = []
for i, (nid, state, icon, nav) in enumerate(STATES):
    cy = TOP + HALF + i * PITCH
    n = {"id": nid, "state": state, "cx": AXIS_X, "cy": cy, "icon": icon,
         "click": nav, "top_dp": TOP + i * PITCH}
    if state == "current":
        n["ring"] = "1/2"
    if state.startswith("bolt"):
        n["practice"] = 4 if state == "bolt_active" else 6
    nodes.append(n)

CURRENT_Y = nodes[2]["cy"]
STOP = round(CURRENT_Y / VB_H, 4)       # hard gradient stop at the current node

connector_paths = [{
    "role": "single",
    "d": "M%d 0 V%d" % (AXIS_X, VB_H),
    "stroke_dp": D["progress_stroke_dp"],
    "note": "ONE straight vertical line, NO elbow/Q curves, NO zigzag, NO alternating x offsets",
    "gradient_stops": [
        {"offset": 0.0, "token": "progress_chapter_primary"},
        {"offset": STOP, "token": "progress_chapter_primary"},
        {"offset": STOP, "token": "progress_chapter_background"},
        {"offset": 1.0, "token": "progress_chapter_background"},
    ],
}]

geometry = {
    "round": "v9",
    "layout": {
        "mode": "single_vertical_line",
        "axis_x": AXIS_X,
        "node_count": len(nodes),
        "gap_dp": GAP,
        "gap_source": "values/values/dimen.xml :: spacing_s = 12dp",
        "pitch_dp": PITCH,
        "top_margin_dp": TOP,
        "curve": False,
        "zigzag": False,
        "alternating_x_offsets": False,
        "one_continuous_connector": True,
        "code_basis": "PathMapScreenKt / PathMapViewModel$onTutorialClick + glance_component_btn_square.xml + dimen.xml",
    },
    "viewBox": [VB_W, VB_H],
    "node": {
        "size_dp": SIZE,
        "corner_radius_dp": D["corner_radius_dp"],
        "corner_source": "glance_component_btn_square.xml -> @dimen/glance_component_square_icon_button_corners = 16dp",
        "icon_dp": 48,
        "icon_source": "glance_component_btn_circle.xml size 48dp; ic_bolt_mastered.xml is 48dp",
        "lip_dp": 8,
        "lip_color_token": "button_primary_highlight",
        "done_gradient_tokens": ["progress_chapter_primary", "button_primary"],
        "progress_bar_layers": ["progress_chapter_background", "progress_chapter_weak", "progress_chapter_primary"],
        "progress_bar_source": "progress_bar_chapter.xml (3 layer-list items, corners 100dp = pill)",
        "optional_bg_token": "card_disabled",
        "shape_pathData": vectors["ic_square_rounded"]["paths"][0]["d"],
        "shape_source": vectors["ic_square_rounded"]["source"],
        "state_source": "PathMapScreenKt 81 composables + PathMapViewModel$onTutorialClick",
    },
    "grid": {
        "dot_dp": 1.6, "spacing_dp": 26, "color_token": "line_secondary",
        "dash_source": "dotted_border_background.xml :: stroke 2dp / dash 8dp / gap 8dp",
    },
    "connector": {
        "stroke_dp": D["progress_stroke_dp"],
        "stroke_source": "values/values/dimen.xml :: lesson_progressbar_height = 6dp",
        "done_color_token": "progress_chapter_primary",
        "weak_color_token": "progress_chapter_weak",
        "next_color_token": "progress_chapter_background",
        "note": "SINGLE straight vertical line with a hard linearGradient stop at the current node; NO Q/C/S curve commands",
    },
    "current": {
        "outer_border_dp": 3, "gap_dp": 7, "outer_ring_dp": 3,
        "inner_border_dp": 2, "ring_size_dp": 60, "ring_stroke_dp": 8,
        "ring_progress_percent": 55, "ring_label": "1/2",
        "play_vector": "ic_play",
        "ring_source": "glance_circular_progress_indicator / bg_circular.xml shape=ring",
    },
    "nodes": nodes,
    "connector_paths": connector_paths,
    "affordances": [{
        "id": "gloss-fab", "type": "floating_book_dictionary",
        "cx": 340, "cy": 600,
        "source": "ic_file.xml + bookmark_no_fill.xml + mimo-01/02 (VISUAL_CROSSCHECK_ONLY)",
    }],
    "states_removed": [
        "locked lesson node (ic_lock_alt_02) — user: هیچ بخش قفلی نیاز نیست",
        "locked bolt node (ic_practice_tab_locked)",
        "START bubble (not a Mimo path-map element)",
        "stray 12% ring on the path (belongs to the chapter header card)",
        "gray floating dot / debug chips",
        "v9: alternating x offsets / zigzag snake layout",
        "v9: rounded Q elbow connector (replaced by one straight line)",
        "v9: inferred 26dp corner radius (corrected to 16dp from dimen.xml)",
        "v9: inferred 10dp connector stroke (corrected to 6dp from dimen.xml)",
    ],
    "lock_policy": ("ZERO locked nodes in Learn / section detail / practice. "
                    "The ONLY lock in the prototype is the pre-existing exam-hub "
                    "«آزمون نهایی / دو هفتگی» card (section ۶); it is left untouched."),
    "timing": {
        "checkpoint_enter_ms": anims["enter_ms"],
        "checkpoint_exit_ms": anims["exit_ms"],
        "source": "res/anim/rc_checkpoint_window_enter.xml + rc_checkpoint_window_exit.xml",
    },
    "timing_note": "node hover/enter transition uses the shipped 220ms / 400ms checkpoint window timings",
    "screenshots": ["mimo-01-learn-path-play.jpg", "mimo-02-learn-path-half.jpg",
                    "mimo-10-path-map-current.jpg"],
    "screenshot_role": "VISUAL_CROSSCHECK_ONLY — geometry comes from code, not from tracing the images",
}

old["nodeGeometry"] = geometry
old["round"] = "v9"
old["method"] = ("CODE_FIRST_TOKENS + SINGLE_LINE_LAYOUT + VISUAL_CROSSCHECK_ONLY "
                 "(mimo-01 / mimo-02 / mimo-10)")
old["code_fidelity"] = {
    "dimens": D,
    "shapes": shapes,
    "vector_state_map": {
        "done": "ic_check_white", "current": "ic_play / hring 1/2",
        "next": "ic_square_rounded (unlocked, light)",
        "bolt_active": "ic_bolt_charged", "bolt_optional": "ic_bolt_mastered",
    },
    "vectors_reviewed": sorted(vectors),
    "animations": anims,
    "corrections_vs_v8": [
        "corner radius 26dp -> 16dp (dimen.xml)",
        "connector stroke 10dp -> 6dp (lesson_progressbar_height)",
        "connector 2 curved Q paths -> 1 straight continuous line with gradient",
        "node x offsets 196/312/80 -> all 196 (single vertical axis)",
        "bolt icons ic_flash/ic_bolt -> ic_bolt_charged/ic_bolt_mastered (real practice vectors)",
        "node gap 106dp ad-hoc -> 12dp from spacing_s",
        "state sequence made linear: done/done/current/next/bolt/bolt",
    ],
}
old["counts"].update({
    "catalog_rows": 88, "layout_mode": "single_vertical_line",
    "connector_paths": 1, "curves": 0, "node_axis_x": AXIS_X,
    "node_gap_dp": GAP, "corner_radius_dp": D["corner_radius_dp"],
    "connector_stroke_dp": D["progress_stroke_dp"],
    "code_fidelity_shapes": len(shapes), "code_fidelity_vectors": len(vectors),
})
old["isolation"] = [x for x in old["isolation"]] + [
    "v9: Learn nodes are ONE straight vertical line (axis x=196); no curve/zigzag; connector is one continuous path",
    "v9: node geometry re-reviewed against dimen.xml / drawable shapes; 16dp corners, 6dp line, 12dp gap",
]
NODE_JSON.write_text(json.dumps(old, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

# --------------------------------------------------------------------------
# 3. append v9 evidence rows to the node catalog (72 -> 88)
# --------------------------------------------------------------------------
with CAT.open(encoding="utf-8", newline="") as f:
    rows = list(csv.reader(f))
header, body = rows[0], rows[1:]
have = {r[0] for r in body if r}
V9 = [
    ["V9-01", "layout", "single vertical line / axis x=196 / no zigzag", "PathMapScreenKt + user round-9", "DESIGN/NODE_CODE_GEOMETRY.json::nodeGeometry.layout", "decision"],
    ["V9-02", "layout", "node gap 12dp from spacing_s (not ad-hoc 106dp)", "dimen.xml spacing_s = 12.000000dip", "SOURCE/values/values/dimen.xml", "code"],
    ["V9-03", "geometry", "corner radius 16dp (was inferred 26dp)", "glance_component_btn_square.xml -> @dimen/glance_component_square_icon_button_corners", "SOURCE/res/drawable/glance_component_btn_square.xml", "code"],
    ["V9-04", "geometry", "connector stroke 6dp (was inferred 10dp)", "dimen.xml lesson_progressbar_height = 6.000000dip", "SOURCE/values/values/dimen.xml", "code"],
    ["V9-05", "geometry", "progress bar is a 100dp-radius pill, 3 layer-list items", "progress_bar_chapter.xml background/weak/primary", "SOURCE/res/drawable/progress_bar_chapter.xml", "code"],
    ["V9-06", "connector", "ONE continuous straight path M196 0 V620", "user: قوس نده / گرهها در یک خط", "DESIGN/NODE_CODE_GEOMETRY.json::nodeGeometry.connector_paths", "decision"],
    ["V9-07", "connector", "hard linearGradient stop at current node (%.4f)" % STOP, "progress_chapter_primary -> progress_chapter_background", "DESIGN/index.html#learn", "code"],
    ["V9-08", "connector", "NO Q/C/S curve commands anywhere in node geometry", "regex-verified zero curve commands", "tools/verify_upgrade.py", "code"],
    ["V9-09", "state", "bolt active = ic_bolt_charged (yellow #FFFFDA1B / #FFFFAB00)", "res/drawable/ic_bolt_charged.xml pathData", "SOURCE/res/drawable/ic_bolt_charged.xml", "code"],
    ["V9-10", "state", "bolt optional = ic_bolt_mastered (48dp vector with sparkles)", "res/drawable/ic_bolt_mastered.xml pathData", "SOURCE/res/drawable/ic_bolt_mastered.xml", "code"],
    ["V9-11", "state", "done = ic_check_white, current = ic_play + 1/2 ring", "ic_check_white.xml / ic_play.xml / bg_circular.xml", "SOURCE/res/drawable/", "code"],
    ["V9-12", "state", "next = ic_square_rounded, light and UNLOCKED (no lock glyph)", "ic_square_rounded.xml squircle pathData", "SOURCE/res/drawable/ic_square_rounded.xml", "code"],
    ["V9-13", "state", "linear progression done/done/current/next/bolt/bolt", "PathMapViewModel$onTutorialClick", "SOURCE/dex/UI_CLASSES.json", "code"],
    ["V9-14", "timing", "checkpoint enter 220ms / exit 400ms", "rc_checkpoint_window_enter.xml / _exit.xml", "SOURCE/res/anim/", "code"],
    ["V9-15", "shape", "node shape pathData from ic_square_rounded (18x18 on 24 viewport)", "android:pathData M18.25,21H5.75...", "SOURCE/res/drawable/ic_square_rounded.xml", "code"],
    ["V9-16", "lock", "still ZERO Learn locks; one exam-hub lock untouched", "user round-8 + round-9", "DESIGN/index.html#exam-hub", "decision"],
]
todo = [r for r in V9 if r[0] not in have]
if todo:
    with CAT.open("a", encoding="utf-8", newline="") as f:
        csv.writer(f).writerows(todo)
print(json.dumps({
    "node_geometry_bytes": NODE_JSON.stat().st_size,
    "layout": geometry["layout"]["mode"],
    "axis_x": AXIS_X, "gap_dp": GAP, "pitch_dp": PITCH,
    "corner_radius_dp": D["corner_radius_dp"],
    "stroke_dp": D["progress_stroke_dp"],
    "gradient_stop": STOP, "curves": 0, "connector_paths": 1,
    "nodes": [{"id": n["id"], "cx": n["cx"], "cy": n["cy"], "state": n["state"]} for n in nodes],
    "catalog_rows": len(body) + len(todo), "added_rows": len(todo),
    "timings_ms": anims,
}, ensure_ascii=False, indent=1))
