#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""extract_mimo_nodes_v8.py — DEEP code-first reconstruction of Mimo path-map NODES.

Round 8 user feedback (main task):
  "اون گره و نود هارو واقعا باید خیلی خیلی خیلی وقت بزاری و درست دربیاری"
  "هیچ بخش قفلی نیاز نیست باشه به جز یک بخش ... در آزمونها ... همین الانش داخل
   دیزاین موجود هست"

So this extractor:
  * reads the REAL ARSC colour/dimen/style tables (not guesses),
  * reads exact android:pathData for every node-state vector,
  * reads the shipped shape/progress/shadow drawables,
  * inventories ALL PathMap DEX classes (104) and tutorial/practice literals,
  * writes an explicit, machine-readable nodeGeometry (size, radius, 3D lip,
    dotted grid, rounded-elbow connector, current double ring + 1/2 ring,
    bolt states, floating book affordance),
  * marks screenshots VISUAL_CROSSCHECK_ONLY (mimo-01/02/10),
  * declares ZERO locked nodes in the Learn path; the only lock in the whole
    prototype is the already-existing exam-hub «آزمون نهایی / دو هفتگی» card.

Writes:
  DESIGN/NODE_CODE_GEOMETRY.json
  CATALOGS/MIMO_PATH_NODES.csv
"""
from __future__ import annotations
import csv
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
UP = (HERE / "..").resolve()
MIMO = (UP / "..").resolve()
CAT = MIMO / "CATALOGS"
SRC = MIMO / "SOURCE"
OUT = UP / "DESIGN"

TOK = json.loads((CAT / "DESIGN_TOKENS.json").read_text(encoding="utf-8"))
APK_SHA = "48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a"


def default(v):
    return v.get("default", "") if isinstance(v, dict) else str(v)


def vector(name):
    p = SRC / "res" / "drawable" / (name + ".xml")
    if not p.exists():
        return None
    s = p.read_text(encoding="utf-8", errors="replace")
    vw = re.search(r'viewportWidth="([\d.]+)"', s)
    vh = re.search(r'viewportHeight="([\d.]+)"', s)
    if not (vw and vh):
        return None
    w = re.search(r'android:width="([\d.]+)dip"', s)
    h = re.search(r'android:height="([\d.]+)dip"', s)
    paths = []
    for pm in re.finditer(r"<path\b([^>]*)/>", s):
        a = pm.group(1)
        d = re.search(r'android:pathData="([^"]*)"', a)
        if not d:
            continue
        f = re.search(r'android:fillColor="([^"]*)"', a)
        ft = re.search(r'android:fillType="([^"]*)"', a)
        paths.append({"d": d.group(1), "fill": f.group(1) if f else "#FF000000",
                      "fillType": ft.group(1) if ft else "0"})
    if not paths:
        return None
    return {"name": name, "source": "res/drawable/" + name + ".xml",
            "widthDp": float(w.group(1)) if w else None,
            "heightDp": float(h.group(1)) if h else None,
            "viewportWidth": float(vw.group(1)), "viewportHeight": float(vh.group(1)),
            "paths": paths}


# ---- exact node-state vectors + exam-surface Mimo vectors -------------------
VECTORS = [
    "ic_check_white", "ic_check_thick", "ic_check", "check_circle",
    "ic_check_circle_alt_01", "ic_play", "ic_square_rounded",
    "ic_bolt", "ic_bolt_charged", "ic_bolt_mastered", "ic_flash", "ic_flash_filled",
    "ic_mascot_practice", "ic_practice_tab_locked", "ic_task_completed",
    "ic_file", "ic_help", "bookmark", "bookmark_no_fill", "insert_drive_file",
    "ic_coin", "ic_coins", "ic_key", "ic_infinity", "ic_streak", "ic_streak_active",
    "ic_sparks", "ic_sparks_alt", "ic_calendar", "calendar_today",
    "ic_clock_black_24dp", "ic_trophy", "ic_trophy_filled", "ic_target",
    "ic_list_bulleted", "ic_switch", "ic_cap", "ic_cap_filled",
    "ic_arrow_left", "ic_arrow_right", "ic_arrow_back_24", "ic_chevron_down",
    "ic_chevron_right", "ic_close", "ic_plus", "ic_microphone", "attachment",
    "ic_link_external", "ic_chat_bubble", "ic_magic_wand", "ic_magic_wand_filled",
    "ic_user_circle", "ic_user_circle_filled", "ic_settings", "ic_ai_tutor",
    "ic_badge_backend", "ic_badge_backend_professional", "ic_mimo_mascot",
]

SHAPE_DRAWABLES = [
    "rounded_background_primary", "rounded_background_secondary", "bg_circular",
    "ic_square_rounded", "progress_bar_chapter", "progress_bar_mimo",
    "shadow_bottom", "shadow_top", "bg_reward_label", "dotted_border_background",
]

ARSC_COLORS = [
    "button_primary", "button_primary_highlight", "progress_chapter_primary",
    "progress_chapter_background", "progress_chapter_weak", "support_purple_light",
    "card_enabled", "card_disabled", "card_pressed", "background_primary",
    "background_secondary", "text_primary", "text_weak", "line_primary",
    "line_secondary", "icon_weak", "support_shadow", "shadow_color",
]
ARSC_DIMENS = [
    "cardview_corner_radius_large", "glance_component_square_icon_button_corners",
    "glance_component_button_corners", "glance_component_circle_icon_button_corners",
    "m3_sys_shape_corner_value_extra_extra_large", "m3_sys_shape_corner_value_extra_large",
    "m3_sys_shape_corner_value_large", "m3_sys_shape_corner_value_medium",
    "m3_alert_dialog_corner_size", "lesson_progressbar_height", "toolbar_height",
    "spacing_xs", "spacing_s", "spacing_m", "spacing_l",
]
ARSC_STYLES = ["ProgressBarChapter", "RcCheckpointWindowAnimation",
               "RcCheckpointWindowAnimation.Sheet", "TextH1", "TextH2", "TextP2",
               "TextLabel1", "TextLabel3"]

STRING_GROUPS = {
    "chapter_start": r"^start_lesson$|^chapter$|^chapter_finished_loading$|^continue_cta$|^continue_learning$|^continue_next$|^continue_practicing$|^lesson_continue$|^lesson_skip$|^lesson_submit$|^lesson_try_again$|^lesson_feedback_|^lesson_streak_generic$|^path_map_next_section_eta",
    "practice": r"^practice|^level_practice_multiplier$|^no_practice|^you_finished_all_practice_sessions$|^section_details_smart_practice",
    "section": r"^section$|^path_section_coming_soon|^path_overview_section_|^path_overview_certificate_percent_complete$|^certificates_unfinished_track_|^track_switcher_|^select_path$|^courses$",
    "mimo_daily_goal": r"^daily_goal|^active_streak$|^best_streak_label$|^lesson_streak_generic$",
}

# ---- exact geometry derived from Mimo tokens + visual cross-check -----------
NODE_GEOMETRY = {
    "method": "CODE_FIRST_TOKENS + VISUAL_CROSSCHECK_ONLY (mimo-01 / mimo-02 / mimo-10)",
    "viewBox": [392, 620],
    "node": {
        "size_dp": 92, "corner_radius_dp": 26, "lip_dp": 8, "icon_dp": 44,
        "lip_color_token": "button_primary_highlight",
        "done_gradient_tokens": ["progress_chapter_primary", "button_primary"],
        "optional_bg_token": "card_disabled",
        "state_source": "PathMapScreenKt 81 composables + PathMapViewModel$onTutorialClick",
    },
    "grid": {"dot_dp": 1.6, "spacing_dp": 26, "color_token": "line_secondary"},
    "connector": {
        "stroke_dp": 10, "elbow_radius_dp": 32,
        "done_color_token": "progress_chapter_primary",
        "next_color_token": "progress_chapter_background",
        "note": "rounded Q elbows (right/down/left/down), NOT a bezier S curve",
    },
    "current": {
        "outer_border_dp": 3, "gap_dp": 7, "outer_ring_dp": 3,
        "inner_border_dp": 2, "ring_size_dp": 60, "ring_stroke_dp": 8,
        "ring_progress_percent": 55, "ring_label": "1/2",
        "play_vector": "ic_play", "ring_source": "glance_circular_progress_indicator.xml",
    },
    "nodes": [
        {"id": "l8n1", "state": "done", "cx": 196, "cy": 70, "icon": "ic_check_white", "click": "chapter"},
        {"id": "l8n2", "state": "done", "cx": 312, "cy": 176, "icon": "ic_check_white", "click": "chapter"},
        {"id": "l8n3", "state": "current", "cx": 196, "cy": 282, "icon": "ic_play", "click": "chapter", "ring": "1/2"},
        {"id": "l8n4", "state": "done", "cx": 80, "cy": 388, "icon": "ic_check_white", "click": "chapter"},
        {"id": "l8n5", "state": "bolt_active", "cx": 196, "cy": 494, "icon": "ic_flash", "click": "section-practice", "practice": 4},
        {"id": "l8n6", "state": "bolt_optional", "cx": 80, "cy": 600, "icon": "ic_bolt", "click": "section-practice", "practice": 6},
    ],
    "connector_paths": [
        {"role": "done", "d": "M242 70 H280 Q312 70 312 102 V130 M312 222 V250 Q312 282 280 282 H242"},
        {"role": "next", "d": "M150 282 H112 Q80 282 80 314 V342 M80 434 V462 Q80 494 112 494 H150 M196 540 V568 Q196 600 164 600 H126"},
    ],
    "affordances": [
        {"id": "gloss-fab", "type": "floating_book_dictionary", "cx": 340, "cy": 600,
         "source": "mimo-01 / mimo-02 bottom-right circular book with A"},
    ],
    "states_removed": [
        "locked lesson node (ic_lock_alt_02) — user: هیچ بخش قفلی نیاز نیست",
        "locked bolt node (ic_practice_tab_locked)",
        "START bubble (not a Mimo path-map element)",
        "stray 12% ring on the path (belongs to the chapter header card)",
        "gray floating dot / debug chips",
    ],
    "lock_policy": ("ZERO locked nodes in Learn / section detail / practice. "
                    "The ONLY lock in the prototype is the pre-existing exam-hub "
                    "«آزمون نهایی / دو هفتگی» card (section ۶); it is left untouched."),
    "screenshots": ["mimo-01-learn-path-play.jpg", "mimo-02-learn-path-half.jpg",
                    "mimo-10-path-map-current.jpg"],
}

# ---- catalog rows -----------------------------------------------------------
ROWS = [
    ("PN-01", "geometry", "node 92dp / corner 26dp / 3D lip 8dp", "PathMapScreenKt + cardview_corner_radius_large + button_primary_highlight", "DESIGN/NODE_CODE_GEOMETRY.json::nodeGeometry.node", "mimo-10"),
    ("PN-02", "geometry", "done node: gradient progress_chapter_primary -> button_primary", "ARSC progress_chapter_primary #FF8D60E2 / button_primary #FF7E4BDE", "CATALOGS/DESIGN_TOKENS.json", "mimo-10"),
    ("PN-03", "geometry", "3D lip uses button_primary_highlight #FF6E3EC8", "box-shadow 0 8px 0 var(--primary-hi)", "CATALOGS/DESIGN_TOKENS.json", "mimo-01"),
    ("PN-04", "geometry", "dotted grid: 1.6dp dot / 26dp spacing", "radial-gradient(circle,var(--line2)...)/26px", "line_secondary #FFE4E6F1", "mimo-01"),
    ("PN-05", "connector", "rounded Q elbows radius 32dp, stroke 10dp", "M242 70 H280 Q312 70 312 102 V130", "progress_chapter_primary", "mimo-10"),
    ("PN-06", "connector", "upcoming part is light lavender", "progress_chapter_background #FFE4E6F1", "CATALOGS/DESIGN_TOKENS.json", "mimo-01"),
    ("PN-07", "node", "done state: white ic_check_white 44dp", "ic_check_white.xml pathData", "res/drawable/ic_check_white.xml", "mimo-01/02/10"),
    ("PN-08", "node", "current state: white card + 3dp purple border + 7dp gap + 3dp outer ring", "border + double box-shadow", "glance_circular_progress_indicator.xml", "mimo-01/02"),
    ("PN-09", "node", "current inner thin 2dp line_secondary outline", "::before inset 6px", "line_secondary", "mimo-01/02"),
    ("PN-10", "node", "current 1/2 progress ring: 60dp circle, 8dp stroke, 55% arc", "conic-gradient(from -90deg,var(--progress) 0 55%)", "glance_circular_progress_indicator.xml", "mimo-02"),
    ("PN-11", "node", "current play variant: dark navy ic_play", "ic_play.xml fill #FF252746", "res/drawable/ic_play.xml", "mimo-01"),
    ("PN-12", "node", "bolt_active: purple 3D node with dark navy ic_flash", "ic_flash.xml fill #FF252746", "res/drawable/ic_flash.xml", "mimo-10"),
    ("PN-13", "node", "bolt_optional: card_disabled node with white ic_bolt", "ic_bolt.xml mono white", "res/drawable/ic_bolt.xml", "mimo-01/02"),
    ("PN-14", "node", "charged/mastered bolt vectors archived in code", "ic_bolt_charged / ic_bolt_mastered / ic_bolt_mastered 48dp", "res/drawable/*.xml", "code-only"),
    ("PN-15", "affordance", "floating circular book/dictionary with A", "ic_file.xml + bookmark_no_fill.xml + CSS outline", "res/drawable/ic_file.xml", "mimo-01/02"),
    ("PN-16", "toolbar", "3 pills: coin 1,272 / key infinity / streak 0", "PathToolbarKt$RowWithKeys + PathToolbarButtonType", "SOURCE/dex/UI_CLASSES.json", "mimo-10"),
    ("PN-17", "toolbar", "course bar with ic_list_bulleted three-lines", "ic_list_bulleted.xml + track_switcher_title", "res/drawable/ic_list_bulleted.xml", "mimo-10"),
    ("PN-18", "header", "overview card: kicker + section title + 8px bar", "ViewsKt$OverviewEntryPointHeader + progress_bar_mimo.xml", "res/layout/progress_bar_mimo.xml", "mimo-10"),
    ("PN-19", "header", "older chapter pill with 12% ring archived", "profile_certificate_view.xml CircularProgressIndicator 56dp", "res/layout/profile_certificate_view.xml", "mimo-01/02"),
    ("PN-20", "state", "NO locked node: done/current/bolt only", "user round-8 explicit order", "18_DESIGN_ROUND_7.md / 20_DESIGN_ROUND_8.md", "decision"),
    ("PN-21", "state", "NO START bubble on path", "chapter start is a modal (chapter_toolbar.xml)", "res/layout/chapter_toolbar.xml", "decision"),
    ("PN-22", "state", "NO debug chips / gray dot", "visual cleanliness per user", "mimo-10", "decision"),
    ("PN-23", "lock", "only lock kept: exam-hub آزمون نهایی / دو هفتگی (section ۶)", "pre-existing design, untouched", "DESIGN/index.html#exam-hub", "user exception"),
    ("PN-24", "chapter", "clicking any lesson node opens Start learning card", "start_lesson / chapter_toolbar.xml / 6dp progress", "SOURCE/values/values/string.xml", "mimo-03"),
    ("PN-25", "practice", "bolt node opens section-practice up to that section", "sections[].tutorialIds (publishSetVersion 52)", "SOURCE/assets/ui/testdata/test-tracks.json", "user v7"),
    ("PN-26", "practice", "fully charged dialog", "section_details_smart_practice_charged_dialog_title", "SOURCE/values/values/string.xml", "code"),
    ("PN-27", "practice", "mastered dialog", "section_details_smart_practice_mastered_dialog_title", "SOURCE/values/values/string.xml", "code"),
    ("PN-28", "practice", "practice anyway CTA", "section_details_smart_practice_practice_anyway", "SOURCE/values/values/string.xml", "code"),
    ("PN-29", "practice", "checkpoint window animation 220ms alpha", "rc_checkpoint_window_enter/exit + RcCheckpointWindowAnimation", "res/anim/*.xml", "code"),
    ("PN-30", "practice", "practice.riv animation asset", "res/raw/practice.riv", "SOURCE/res/raw/practice.riv", "code"),
    ("PN-31", "dex", "PathMapScreenKt composables", "Lcom/getmimo/ui/path/map/PathMapScreenKt*", "SOURCE/dex/UI_CLASSES.json", "code"),
    ("PN-32", "dex", "PathMapViewModel onTutorialClick / onNextSectionShown", "Lcom/getmimo/ui/path/map/PathMapViewModel*", "SOURCE/dex/UI_CLASSES.json", "code"),
    ("PN-33", "dex", "GetPathMapState / GetPathMapDialogs", "Lcom/getmimo/interactors/path/GetPathMap*", "SOURCE/dex/UI_CLASSES.json", "code"),
    ("PN-34", "dex", "PracticeOptionalIntroKt / TutorialSpotlightKt", "Lcom/getmimo/ui/path/map/PracticeOptionalIntroKt*", "SOURCE/dex/UI_CLASSES.json", "code"),
    ("PN-35", "dex", "PathToolbarButtonType enum", "Lcom/getmimo/ui/path/map/PathToolbarButtonType", "SOURCE/dex/UI_CLASSES.json", "code"),
    ("PN-36", "dex", "SmartPractice modal data", "ModalData$SmartPracticeChargedModal / MasteredModal", "SOURCE/dex/UI_CLASSES.json", "code"),
    ("PN-37", "dex", "isCompleted / practiceOptional literals", "UI_STRING_LITERALS.txt", "SOURCE/dex/UI_STRING_LITERALS.txt", "code"),
    ("PN-38", "shape", "rounded_background_primary 12dp", "res/drawable/rounded_background_primary.xml", "SOURCE/res/drawable", "code"),
    ("PN-39", "shape", "progress_bar_chapter 100dp corners", "res/drawable/progress_bar_chapter.xml", "SOURCE/res/drawable", "code"),
    ("PN-40", "shape", "ic_square_rounded 24dp rounded square", "res/drawable/ic_square_rounded.xml", "SOURCE/res/drawable", "code"),
    ("PN-41", "shape", "bg_circular ring shape", "res/drawable/bg_circular.xml", "SOURCE/res/drawable", "code"),
    ("PN-42", "shape", "shadow_bottom gradient", "res/drawable/shadow_bottom.xml + shadow_color", "SOURCE/res/drawable", "code"),
    ("PN-43", "color", "support_shadow #FF252746", "CATALOGS/DESIGN_TOKENS.json", "CATALOGS/DESIGN_TOKENS.json", "code"),
    ("PN-44", "color", "progress_chapter_weak #339C75E6 ring", "CATALOGS/DESIGN_TOKENS.json", "CATALOGS/DESIGN_TOKENS.json", "code"),
    ("PN-45", "screenshot", "mimo-01: done + play + 2 bolts + book", "VISUAL_CROSSCHECK_ONLY", "DESIGN/REFERENCE/mimo-01-learn-path-play.jpg", "cross-check"),
    ("PN-46", "screenshot", "mimo-02: done + double ring + 1/2 ring + 2 bolts + book", "VISUAL_CROSSCHECK_ONLY", "DESIGN/REFERENCE/mimo-02-learn-path-half.jpg", "cross-check"),
    ("PN-47", "screenshot", "mimo-10: 4 done checks + active bolt + elbow connector", "VISUAL_CROSSCHECK_ONLY", "DESIGN/REFERENCE/mimo-10-path-map-current.jpg", "cross-check"),
    ("PN-48", "screenshot", "mimo-03: Start learning chapter card", "VISUAL_CROSSCHECK_ONLY", "DESIGN/REFERENCE/mimo-03-chapter-start-dialog.jpg", "cross-check"),
    ("PN-49", "screenshot", "mimo-05: leaderboard (promotion zone archived)", "VISUAL_CROSSCHECK_ONLY", "DESIGN/REFERENCE/mimo-05-weekly-leaderboard.jpg", "cross-check"),
    ("PN-50", "screenshot", "mimo-13/14: path overview + unfinished track", "VISUAL_CROSSCHECK_ONLY", "DESIGN/REFERENCE/*.jpg", "cross-check"),
]

V8_ROWS = [
    ("V8-01", "decision", "روتین روزانه / Habitica scoring idea fully removed", "user: کلا حدف کن به درد نیمخوره / ایدهاش اشتباه بود", "20_DESIGN_ROUND_8.md", "decision"),
    ("V8-02", "decision", "bottom nav back to 5 tabs; MAX still forbidden", "user round-8", "DESIGN/index.html#tabs", "decision"),
    ("V8-03", "decision", "Dictate removed from AI composer", "user round-8", "DESIGN/index.html#ai", "decision"),
    ("V8-04", "decision", "all design/policy/EPM/timer annotation notes removed from phone UI", "user round-8", "DESIGN/index.html", "decision"),
    ("V8-05", "decision", "exam-hub labels/templates + descriptive answer text KEPT", "user: اون توضحاتی که در بخش ازمونها هست رو میتونی نگه داری", "DESIGN/index.html#exam-hub", "decision"),
    ("V8-06", "decision", "exam appearance Mimo-ified (icons + colours only, no architecture change)", "user round-8", "DESIGN/index.html", "decision"),
    ("V8-07", "decision", "exam architecture/timer/answer sheets/270 min UNCHANGED", "user: چهارچوبش الان عالیه", "DESIGN/index.html", "decision"),
    ("V8-08", "ai", "attachment + زنجیره گفت و گو top row kept, tidy", "res/drawable/attachment.xml + ic_link_external.xml", "CATALOGS/AI_PANEL_SPEC.csv", "code"),
    ("V8-09", "ai", "TEACH/PRACTICE + model + medium on one tiny bottom line", "ic_chevron_down.xml", "CATALOGS/AI_PANEL_SPEC.csv", "code"),
    ("V8-10", "exam-icon", "◇ replaced by real Mimo vectors per exam kind", "ic_trophy / ic_file / ic_target / ic_sparks_alt", "SOURCE/res/drawable/*.xml", "code"),
    ("V8-11", "exam-icon", "⏱ replaced by ic_clock_black_24dp", "res/drawable/ic_clock_black_24dp.xml", "SOURCE/res/drawable", "code"),
    ("V8-12", "exam-icon", "✓ replaced by ic_task_completed", "res/drawable/ic_task_completed.xml", "SOURCE/res/drawable", "code"),
    ("V8-13", "exam-icon", "🔒 (only allowed lock) replaced by ic_lock_alt_02", "res/drawable/ic_lock_alt_02.xml", "SOURCE/res/drawable", "code"),
    ("V8-14", "exam-icon", "back arrow / help replaced by Mimo vectors", "ic_arrow_back_24 / ic_help", "SOURCE/res/drawable", "code"),
    ("V8-15", "exam-style", "cat-meta restyled as Mimo card (12dp radius, no dashed line)", "cardview_corner_radius_large", "CATALOGS/DESIGN_TOKENS.json", "code"),
    ("V8-16", "exam-style", "nodek restyled as Mimo square card (20dp, 2px line, 4dp lip)", "glance_component_square_icon_button_corners", "CATALOGS/DESIGN_TOKENS.json", "code"),
    ("V8-17", "exam-style", "chips restyled as Mimo pills (card-pressed / primary)", "glance_component_button_corners 24dp", "CATALOGS/DESIGN_TOKENS.json", "code"),
    ("V8-18", "exam-style", "Mimo TextH2/TextLabel1 typography + toolbar 56dp", "toolbar_height 56dp / TextH2 20sp", "CATALOGS/DESIGN_TOKENS.json", "code"),
    ("V8-19", "lock", "locked lesson rows removed from section detail", "user round-8", "DESIGN/index.html#section-detail", "decision"),
    ("V8-20", "lock", "Coming soon label kept in path overview (not a lock)", "path_section_coming_soon", "SOURCE/values/values/string.xml", "code"),
    ("V8-21", "code", "title tooltips converted to data-code audit attributes", "no visible code annotations in UI", "DESIGN/index.html", "decision"),
    ("V8-22", "code", "visible .lh debug labels removed; data-lh audit kept", "8 LH capabilities remain behind /max", "CATALOGS/AI_PANEL_SPEC.csv", "decision"),
]


def main():
    colors = {k: {"default": default(TOK["colors"][k]),
                  "night": (TOK["colors"][k].get("night") or default(TOK["colors"][k]))
                  if isinstance(TOK["colors"][k], dict) else default(TOK["colors"][k])}
              for k in ARSC_COLORS if k in TOK["colors"]}
    dimens = {k: default(TOK["dimens"][k]) for k in ARSC_DIMENS if k in TOK["dimens"]}
    styles = {k: TOK["styles"][k] for k in ARSC_STYLES if k in TOK["styles"]}

    strings = {}
    for group, pat in STRING_GROUPS.items():
        strings[group] = {k: default(v) for k, v in sorted(TOK["strings"].items())
                          if re.search(pat, k) and default(v)}

    vectors, misses = {}, []
    for n in VECTORS:
        v = vector(n)
        if v:
            vectors[n] = v
        else:
            misses.append(n)

    shapes = {}
    for n in SHAPE_DRAWABLES:
        p = SRC / "res" / "drawable" / (n + ".xml")
        if p.exists():
            s = p.read_text(encoding="utf-8", errors="replace")
            shapes[n] = {"source": "res/drawable/" + n + ".xml",
                         "bytes": len(s.encode("utf-8")),
                         "xml": re.sub(r"\s+", " ", s.strip())[:420]}

    classes = json.loads((SRC / "dex" / "UI_CLASSES.json").read_text(encoding="utf-8"))
    names = sorted({c["class"] for c in classes})
    pathmap = [n for n in names if re.search(r"/ui/path/map/|/interactors/path/GetPathMap|SmartPractice", n)]
    pathmap_detail = {
        "path_map_screen": [n for n in pathmap if "PathMapScreenKt" in n],
        "path_map_viewmodel": [n for n in pathmap if "PathMapViewModel" in n],
        "path_map_overlay": [n for n in pathmap if any(k in n for k in ("PracticeOptionalIntro", "TutorialSpotlight", "ResubscribeMascot", "ViewsKt", "PathToolbar"))],
        "interactors": [n for n in pathmap if "interactors" in n],
        "smart_practice": [n for n in pathmap if "SmartPractice" in n],
    }
    literals_raw = (SRC / "dex" / "UI_STRING_LITERALS.txt").read_bytes().decode("utf-8", "replace")
    lits = sorted({l.strip()[:170] for l in literals_raw.splitlines()
                   if re.search(r"isCompleted|practiceOptional|chapterIndexInSection|sectionIndex|sectionTitle|PRACTICE_LEVEL|isPractice|tutorialIds|PathMap", l, re.I)})

    cm = json.loads((SRC / "assets" / "ui" / "testdata" / "test-tracks.json").read_text(encoding="utf-8"))
    track = cm["tracks"][0]
    sections = [{"name": s.get("name", ""), "description": s.get("description", ""),
                 "startIndex": s.get("startIndex"), "endIndex": s.get("endIndex"),
                 "tutorialIds": s.get("tutorialIds", []),
                 "tutorialCount": len(s.get("tutorialIds", []))}
                for s in track.get("sections", [])]
    tutorials = [{"id": u.get("id"), "type": u.get("type"), "title": u.get("title", "")}
                 for u in track.get("tutorials", [])]

    doc = {
        "method": "CODE_FIRST / ARSC tables + exact pathData + AXML shapes + DEX inventory (screenshots VISUAL_CROSSCHECK_ONLY)",
        "apk_sha256": APK_SHA,
        "round": "DESIGN v8 — exact path-map NODE reconstruction (main task)",
        "sources": {
            "tokens": "mimo-ui/CATALOGS/DESIGN_TOKENS.json (50,477 ARSC config rows)",
            "vectors": "mimo-ui/SOURCE/res/drawable/*.xml (exact android:pathData)",
            "shapes": "mimo-ui/SOURCE/res/drawable/*.xml (shape/layer-list)",
            "strings": "mimo-ui/SOURCE/values/values/string.xml (1,721 names)",
            "content": "mimo-ui/SOURCE/assets/ui/testdata/test-tracks.json",
            "dex": "mimo-ui/SOURCE/dex/UI_CLASSES.json + UI_STRING_LITERALS.txt",
            "screenshots": "14 Mimo screenshots, VISUAL_CROSSCHECK_ONLY",
        },
        "nodeGeometry": NODE_GEOMETRY,
        "tokens": {"colors": colors, "dimens": dimens, "styles": styles},
        "strings": strings,
        "vectors": vectors,
        "shapes": shapes,
        "dex": {"pathmap_class_count": len(pathmap), "groups": pathmap_detail,
                "literals": lits[:40]},
        "contentModel": {
            "source": "SOURCE/assets/ui/testdata/test-tracks.json",
            "publishSetVersion": cm.get("publishSetVersion"),
            "trackTitle": track.get("title", ""),
            "trackCount": len(cm.get("tracks", [])),
            "sections": sections, "tutorials": tutorials,
            "tutorialCount": len(tutorials),
        },
        "isolation": [
            "section-practice (bolt checkpoint quiz) is a LEARN sub-screen, class=screen mimo",
            "section-practice has NO timer chip, NO پاسخبرگ/پاسخنامه, NO exam hub, NO 270 min, NO POLICY",
            "exam-hub / exam-run / exam-result remain the only Konkur exam surfaces",
            "NO Habitica /Daily Routine idea: removed entirely in round 8",
            "NO locked nodes in Learn/section-detail/practice; only the pre-existing exam-hub lock stays",
        ],
        "counts": {
            "vectors": len(vectors), "vector_misses": len(misses),
            "shapes": len(shapes), "strings": sum(len(v) for v in strings.values()),
            "colors": len(colors), "dimens": len(dimens), "styles": len(styles),
            "pathmap_classes": len(pathmap), "dex_literals": len(lits),
            "sections": len(sections),
            "tutorial_ids": sum(s["tutorialCount"] for s in sections),
            "catalog_rows": len(ROWS) + len(V8_ROWS),
        },
        "vectorMisses": misses,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "NODE_CODE_GEOMETRY.json").write_text(
        json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    with (UP / "CATALOGS" / "MIMO_PATH_NODES.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["row_id", "kind", "item", "code_crosswalk", "source_path", "visual_crosscheck"])
        for r in ROWS + V8_ROWS:
            w.writerow(r)
    print(json.dumps({
        "output": str(OUT / "NODE_CODE_GEOMETRY.json"),
        "bytes": (OUT / "NODE_CODE_GEOMETRY.json").stat().st_size,
        "catalog_rows": len(ROWS) + len(V8_ROWS),
        "counts": doc["counts"], "vectorMisses": misses,
    }, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
