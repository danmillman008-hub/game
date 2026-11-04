#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""extract_mimo_nodes_v7.py — deep code-first RE of Mimo 9.35 path-map NODES.

Round 7 user feedback: "the structure of the nodes ... still needs work" and
"the lightning-bolt nodes, when clicked, [open] a quiz of the topic up to that
section; careful, it must not be mixed with the exam section we have".

Reads ONLY decoded APK artifacts already produced by the static census:
  mimo-ui/CATALOGS/DESIGN_TOKENS.json        (ARSC strings/colors/dimens/styles)
  mimo-ui/SOURCE/res/drawable/*.xml          (exact android:pathData)
  mimo-ui/SOURCE/res/layout/*.xml            (decoded AXML)
  mimo-ui/SOURCE/res/anim/*.xml              (checkpoint window animations)
  mimo-ui/SOURCE/res/raw/practice.riv        (Rive practice animation)
  mimo-ui/SOURCE/assets/ui/testdata/test-tracks.json
  mimo-ui/SOURCE/dex/UI_CLASSES.json
  mimo-ui/SOURCE/dex/UI_STRING_LITERALS.txt

Writes:
  DESIGN/NODE_CODE_GEOMETRY.json
  CATALOGS/MIMO_PATH_NODES.csv

No screenshot is parsed; screenshots are visual cross-checks only.
"""
import csv
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
UP = (HERE / "..").resolve()
MIMO = (UP / "..").resolve()
CAT = MIMO / "CATALOGS"
SRC = MIMO / "SOURCE"
OUT = UP / "DESIGN"


def jload(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def default(v):
    return v.get("default", "") if isinstance(v, dict) else str(v)


def sha256(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def vector(name):
    """Decode one <vector> drawable; preserve exact android:pathData."""
    p = SRC / "res" / "drawable" / (name + ".xml")
    if not p.exists():
        return None
    s = p.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"<vector[^>]*viewportWidth=\"([\d.]+)\"[^>]*viewportHeight=\"([\d.]+)\"", s)
    if not m:
        m2 = re.search(r"<vector[^>]*viewportHeight=\"([\d.]+)\"[^>]*viewportWidth=\"([\d.]+)\"", s)
        if not m2:
            return None
        vw, vh = float(m2.group(2)), float(m2.group(1))
    else:
        vw, vh = float(m.group(1)), float(m.group(2))
    w = re.search(r"<vector[^>]*\sandroid:width=\"([\d.]+)dip\"", s)
    h = re.search(r"<vector[^>]*\sandroid:height=\"([\d.]+)dip\"", s)
    paths = []
    for pm in re.finditer(r"<path\b([^>]*)/>", s):
        a = pm.group(1)
        d = re.search(r'android:pathData="([^"]*)"', a)
        if not d:
            continue
        f = re.search(r'android:fillColor="([^"]*)"', a)
        ft = re.search(r'android:fillType="([^"]*)"', a)
        sw = re.search(r'android:strokeColor="([^"]*)"', a)
        paths.append({
            "d": d.group(1),
            "fill": f.group(1) if f else "#FF000000",
            "fillType": ft.group(1) if ft else "0",
            "stroke": sw.group(1) if sw else None,
        })
    if not paths:
        return None
    return {
        "name": name,
        "source": "res/drawable/" + name + ".xml",
        "widthDp": float(w.group(1)) if w else None,
        "heightDp": float(h.group(1)) if h else None,
        "viewportWidth": vw,
        "viewportHeight": vh,
        "paths": paths,
    }


# --------------------------------------------------------------------------
VECTORS = [
    # bolt / smart practice checkpoint nodes
    "ic_bolt", "ic_bolt_charged", "ic_bolt_mastered", "ic_mascot_practice",
    "ic_practice_tab_locked", "ic_flash", "ic_flash_filled",
    # lesson node states
    "ic_play", "ic_check_white", "ic_check_thick", "check_circle",
    "ic_lock_alt_02", "ic_lock_outline", "ic_lock_open_alt_02",
    # routine tab + quiet routine screen
    "ic_calendar", "ic_task_completed", "ic_target", "ic_sparks",
    "ic_sparks_alt", "ic_streak", "ic_streak_active", "ic_coin", "ic_coins",
    # AI panel tidy icons (round 7)
    "attachment", "ic_file", "ic_link_external", "ic_chat_bubble",
    "ic_microphone", "ic_chevron_down", "ic_plus", "ic_check_circle_alt_01",
    # shared Mimo chrome
    "ic_arrow_left", "ic_arrow_right", "ic_arrow_back_24", "ic_close",
    "bookmark", "bookmark_no_fill", "ic_help", "insert_drive_file",
    "ic_magic_wand", "ic_magic_wand_filled", "ic_key", "ic_infinity",
    "ic_list_bulleted", "ic_switch", "ic_badge_backend",
    "ic_badge_backend_professional", "ic_mimo_mascot", "ic_ai_tutor",
    "ic_cap", "ic_cap_filled", "ic_trophy", "ic_user_circle",
    "ic_user_circle_filled", "ic_settings",
]

LAYOUTS = [
    "chapter_activity", "chapter_toolbar", "chapter_finished_fragment",
    "chapter_finished_streak_fragment", "chapter_finished_leaderboard_fragment",
    "flash_bar_view", "flashbar_dropdown_layout", "progress_bar_mimo",
    "daily_sparks_goal_progress_view", "practice_tab_fragment",
    "lesson_interactive_multiplechoice_fragment",
    "lesson_interaction_selection_item_layout",
    "lesson_interactive_feedback_bottom_sheet_dialog",
    "lesson_noninteractive_fragment", "glance_circular_progress_indicator",
    "glance_linear_progress_indicator", "profile_certificate_view",
    "leaderboard_promotion_divider",
]

ANIMS = ["rc_checkpoint_window_enter", "rc_checkpoint_window_exit"]

STRING_GROUPS = {
    "path_nodes": r"^start_lesson$|^chapter$|^chapter_finished_loading$|^continue_cta$|^continue_learning$|^continue_next$|^continue_practicing$|^lesson_continue$|^lesson_skip$|^lesson_submit$|^lesson_try_again$|^lesson_streak|^lesson_feedback_|^lesson_description_|^path_map_next_section_eta|^path_see_course_overview$",
    "practice": r"^practice|^level_practice_multiplier$|^no_practice|^you_finished_all_practice_sessions$|^section_details_smart_practice|^section$|^sparks$",
    "section": r"^path_section_coming_soon|^alert_msg_section_setion_locked$|^path_overview_section_|^path_overview_certificate_percent_complete$|^certificates_unfinished_track_|^track_switcher_|^select_path$|^courses$",
    "routine": r"^daily_goal|^active_streak$|^best_streak_label$|^chapter_end_streak|^chapter_end_widget_intro|^chapter_end_progress_eta|^streak|^sparks$",
}

COLOR_NAMES = [
    "background_primary", "card_enabled", "card_disabled", "card_pressed",
    "button_primary", "button_primary_highlight", "progress_chapter_primary",
    "progress_chapter_background", "progress_primary", "progress_weak",
    "progress_empty", "icon_weak", "text_primary", "text_weak",
    "support_yellow", "support_green", "support_blue", "line_primary",
    "line_secondary", "accent_error", "accent_success",
    "support_purple_light", "code_highlight",
]
DIMEN_NAMES = [
    "spacing_xs", "spacing_s", "spacing_m", "spacing_l", "toolbar_height",
    "lesson_progressbar_height", "cardview_corner_radius_large",
    "glance_component_square_icon_button_corners",
    "glance_component_button_corners", "m3_alert_dialog_corner_size",
    "leaderboard_item", "profile_header_avatar_size", "content_max_width",
]

# catalogue: one row per reconstructed node / practice / isolation fact
NODE_ROWS = [
    ("PN-01", "section-header", "overview-card: kicker + title + 8px bar", "ic_badge_backend", "ViewsKt$OverviewEntryPointHeader; progress_bar_mimo.xml", "path-overview", "res/values/values/string.xml:path_see_course_overview", "SECTION header card"),
    ("PN-02", "section-header", "circular 12% ring on older Mimo builds", "ic_badge_backend_professional", "profile_certificate_view.xml CircularProgressIndicator 56dp", "path-overview", "res/layout/profile_certificate_view.xml", "ring token: indicatorColor=progress_primary"),
    ("PN-03", "node", "done: 92px rounded square, purple gradient, 8px dark lip", "ic_check_white", "PathMapScreenKt; cardview_corner_radius_large; button_primary_highlight", "chapter", "res/drawable/ic_check_white.xml", "3D lip from box-shadow 0 8px 0"),
    ("PN-04", "node", "current: white card, double purple ring, play triangle", "ic_play", "chapter_toolbar.xml; progress_bar_mimo.xml", "chapter", "res/drawable/ic_play.xml", "cur node: border 3px + 7px + 10px ring"),
    ("PN-05", "node", "current alt: white card with 1/2 conic progress ring", "ic_play", "glance_circular_progress_indicator.xml", "chapter", "res/layout/glance_circular_progress_indicator.xml", "1/2 state from screenshot mimo-02"),
    ("PN-06", "node", "locked: disabled card with white padlock", "ic_lock_alt_02", "alert_msg_section_setion_locked; card_disabled", "locked", "res/drawable/ic_lock_alt_02.xml", "toast: Unlock this section by finishing the previous one"),
    ("PN-07", "node", "bolt checkpoint: purple square with dark lightning", "ic_flash", "ic_bolt.xml; ic_bolt_charged.xml; ic_bolt_mastered.xml", "section-practice", "res/drawable/ic_bolt_mastered.xml", "round-7: separate LEARN checkpoint quiz"),
    ("PN-08", "node", "bolt checkpoint locked: disabled with white bolt", "ic_bolt", "ic_practice_tab_locked.xml; res/raw/practice.riv", "section-practice", "res/drawable/ic_practice_tab_locked.xml", "not yet charged"),
    ("PN-09", "node", "bolt checkpoint mastered: gold mastered bolt", "ic_bolt_mastered", "ModalData$SmartPracticeMasteredModal", "section-practice", "res/drawable/ic_bolt_mastered.xml", "You've mastered the section!"),
    ("PN-10", "connector", "rounded elbow path (right/down/left/down), not a bezier S", "", "PathMapScreenKt 73 classes; progress_chapter_primary", "", "SOURCE/dex/UI_CLASSES.json", "SVG path with Q elbows"),
    ("PN-11", "connector", "dotted 26px grid behind nodes", "", "radial-gradient(circle,var(--line2) 1.6px,transparent 1.7px)", "", "res/values/values/color.xml:line_secondary", "visual cross-check only"),
    ("PN-12", "chapter-start", "LEARN / CHAPTER 0/2 / START LEARNING card", "ic_cap_filled", "chapter_activity.xml; chapter_toolbar.xml; start_lesson", "lesson", "res/layout/chapter_activity.xml", "clicking ANY lesson node opens this"),
    ("PN-13", "chapter-start", "6dp chapter progress bar", "", "chapter_toolbar.xml @id/pb_chapter; lesson_progressbar_height", "", "res/layout/chapter_toolbar.xml", "style=ProgressBarChapter"),
    ("PN-14", "checkpoint", "checkpoint window enter/exit animations", "", "rc_checkpoint_window_enter.xml / exit (alpha 220ms)", "section-practice", "res/anim/rc_checkpoint_window_enter.xml", "checkpoint = bolt node"),
    ("PN-15", "checkpoint", "flash bar / dropdown UI for practice", "", "flash_bar_view.xml; flashbar_dropdown_layout.xml", "", "res/layout/flash_bar_view.xml", "Mimo practice chrome"),
    ("PN-16", "practice-quiz", "single-choice question + 4 options", "", "lesson_interactive_multiplechoice_fragment.xml", "", "res/layout/lesson_interactive_multiplechoice_fragment.xml", "Mimo lesson interaction, NOT exam"),
    ("PN-17", "practice-quiz", "option row layout", "", "lesson_interaction_selection_item_layout.xml", "", "res/layout/lesson_interaction_selection_item_layout.xml", "Mimo tokens only"),
    ("PN-18", "practice-quiz", "feedback bottom sheet", "", "lesson_interactive_feedback_bottom_sheet_dialog.xml", "", "res/layout/lesson_interactive_feedback_bottom_sheet_dialog.xml", "lesson_feedback_* strings"),
    ("PN-19", "practice-quiz", "Fully charged! / Practice anyway", "ic_mascot_practice", "section_details_smart_practice_charged_dialog_*; ModalData$SmartPracticeChargedModal", "", "res/values/values/string.xml", "smart practice charged modal"),
    ("PN-20", "practice-quiz", "You've mastered the section!", "ic_bolt_mastered", "section_details_smart_practice_mastered_dialog_*; ModalData$SmartPracticeMasteredModal", "", "res/values/values/string.xml", "smart practice mastered modal"),
    ("PN-21", "practice-quiz", "Practice more / Continue practicing / Practice optional", "", "practice_more; continue_practicing; practice_optional", "", "res/values/values/string.xml", "real ARSC labels"),
    ("PN-22", "practice-quiz", "Practice intro title + description", "ic_mascot_practice", "practice_intro_title; practice_intro_description", "", "res/values/values/string.xml", "Sharpen your skills with hands-on practice"),
    ("PN-23", "practice-quiz", "Practice multiplier / no exercises yet", "", "level_practice_multiplier; no_practice_exercises_yet", "", "res/values/values/string.xml", "practice states"),
    ("PN-24", "practice-quiz", "quiz stem derived from tutorialIds up to section", "", "test-tracks.json sections[].tutorialIds", "", "SOURCE/assets/ui/testdata/test-tracks.json", "ازمون از مبحث تا اون بخش"),
    ("PN-25", "isolation", "NO timer chip in section practice", "", "timer chip belongs to exam-run only", "", "DESIGN/index.html", "نباید قاتی شه با بخش آزمون"),
    ("PN-26", "isolation", "NO پاسخبرگ / پاسخنامه in section practice", "", "answer sheets belong to exam-run/exam-result", "", "DESIGN/index.html", "policy split preserved"),
    ("PN-27", "isolation", "NO exam hub / exam kind / 270 min in practice", "", "exam-hub, POLICY, EXAM_KIND are exam-only", "", "DESIGN/index.html", "separate data-screen"),
    ("PN-28", "isolation", "section practice uses class=screen mimo (Mimo skin)", "", "class=\"screen mimo\"", "", "DESIGN/index.html", "not class=screen konkur"),
    ("PN-29", "dex", "PathMapScreenKt Compose node classes", "", "Lcom/getmimo/ui/path/map/PathMapScreenKt*", "", "SOURCE/dex/UI_CLASSES.json", "73 classes matched"),
    ("PN-30", "dex", "GetPathMapState / GetPathMapDialogs", "", "Lcom/getmimo/interactors/path/GetPathMap*", "", "SOURCE/dex/UI_CLASSES.json", "path state + dialogs"),
    ("PN-31", "dex", "SmartPracticeChargedModal / MasteredModal", "", "Lcom/getmimo/ui/introduction/ModalData$SmartPractice*", "", "SOURCE/dex/UI_CLASSES.json", "2 modal data classes"),
    ("PN-32", "dex", "practice level literals", "", "PRACTICE_LEVEL_1 / _2 / _3", "", "SOURCE/dex/UI_STRING_LITERALS.txt", "practice progression"),
    ("PN-33", "dex", "practice redo / progress literals", "", "isPracticeProgress; isPracticeRedo", "", "SOURCE/dex/UI_STRING_LITERALS.txt", "practice state flags"),
    ("PN-34", "dex", "section / chapter index literals", "", "sectionIndex; chapterIndexInSection; sectionTitle", "", "SOURCE/dex/UI_STRING_LITERALS.txt", "node ordering"),
    ("PN-35", "routine-tab", "6th bottom tab روتین روزانه", "ic_calendar", "ic_calendar.xml; ic_task_completed.xml; daily_goal", "routine", "res/drawable/ic_calendar.xml", "explicit round-7 instruction"),
    ("PN-36", "routine-tab", "streak / sparks / coin Mimo icons", "ic_streak_active", "ic_streak_active; ic_sparks; ic_coin", "", "res/drawable/ic_streak_active.xml", "no Habitica assets"),
    ("PN-37", "routine-tab", "daily goal progress view", "", "daily_sparks_goal_progress_view.xml; daily_goal", "", "res/layout/daily_sparks_goal_progress_view.xml", "Mimo skin"),
    ("PN-38", "ai-top", "attach file: paperclip icon + short label", "attachment", "attachment.xml; ic_file.xml", "Import notes...", "res/drawable/attachment.xml", "اضافه کردن فایل"),
    ("PN-39", "ai-top", "conversation chain: link icon + clear label", "ic_link_external", "ic_link_external.xml; ic_chat_bubble.xml", "Chains", "res/drawable/ic_link_external.xml", "زنجیره گفت و گو"),
    ("PN-40", "ai-bottom", "voice dictate: microphone icon, kept in one row", "ic_microphone", "ic_microphone.xml", "Dictate", "res/drawable/ic_microphone.xml", "دیکته برای ویس"),
    ("PN-41", "ai-bottom", "model / effort chevrons", "ic_chevron_down", "ic_chevron_down.xml", "Model picker / Effort", "res/drawable/ic_chevron_down.xml", "tiny single line"),
    ("PN-42", "exam-page", "سؤال قبل / سؤال بعد clean pair", "ic_arrow_left", "ic_arrow_left.xml; ic_arrow_right.xml", "prevQ / nextQ", "res/drawable/ic_arrow_left.xml", "دو تا دکمه تر و تمیز"),
    ("PN-43", "exam-page", "bottom single line: پاسخبرگ + بقیه, not bold", "", "btn ghost, font-weight 400", "", "DESIGN/index.html", "اونها پایین باشند"),
    ("PN-44", "leaderboard", "Promotion Zone removed per user", "", "leaderboard_promotion_divider.xml archived only", "", "res/layout/leaderboard_promotion_divider.xml", "نیاز نیست"),
    ("PN-45", "screenshot", "mimo-01 play node / mimo-02 1/2 ring", "", "PathMapScreenKt + progress_bar_mimo.xml", "", "DESIGN/REFERENCE/mimo-01-learn-path-play.jpg", "VISUAL_CROSSCHECK_ONLY"),
    ("PN-46", "screenshot", "mimo-10 active bolt node + elbow path", "", "ic_bolt* + PathMapScreenKt", "", "DESIGN/REFERENCE/mimo-10-path-map-current.jpg", "VISUAL_CROSSCHECK_ONLY"),
    ("PN-47", "screenshot", "mimo-03 chapter start card", "", "chapter_toolbar.xml + start_lesson", "", "DESIGN/REFERENCE/mimo-03-chapter-start-dialog.jpg", "VISUAL_CROSSCHECK_ONLY"),
    ("PN-48", "screenshot", "mimo-05 promotion zone archived", "", "leaderboard_promotion_divider.xml", "", "DESIGN/REFERENCE/mimo-05-weekly-leaderboard.jpg", "VISUAL_CROSSCHECK_ONLY"),
    ("PN-49", "floating", "circular A-book / glossary affordance", "ic_file", "ic_file.xml + bookmark_no_fill.xml; circular card radius", "glossary", "res/drawable/ic_file.xml", "Mimo floating affordance, visual cross-check mimo-01"),
    ("PN-50", "screenshot", "mimo-02 half-progress ring + locked square", "", "glance_circular_progress_indicator.xml; card_disabled", "", "DESIGN/REFERENCE/mimo-02-learn-path-half.jpg", "VISUAL_CROSSCHECK_ONLY"),
]


def main():
    tokens = jload(CAT / "DESIGN_TOKENS.json")
    strings, colors, dimens, styles = (tokens[k] for k in ("strings", "colors", "dimens", "styles"))

    # 1. exact ARSC strings
    picked = {}
    for group, pat in STRING_GROUPS.items():
        picked[group] = {
            k: default(v) for k, v in sorted(strings.items())
            if re.search(pat, k) and default(v)
        }

    # 2. exact vector pathData
    vectors, misses = {}, []
    for n in VECTORS:
        v = vector(n)
        if v:
            vectors[n] = v
        else:
            misses.append(n)

    # 3. decoded AXML layouts (ids + styles only, no source copied)
    layouts = {}
    for n in LAYOUTS:
        p = SRC / "res" / "layout" / (n + ".xml")
        if not p.exists():
            continue
        s = p.read_text(encoding="utf-8", errors="replace")
        ids = sorted(set(re.findall(r'android:id="@(?:\+)?id/([A-Za-z0-9_]+)"', s)))
        layouts[n] = {
            "source": "res/layout/" + n + ".xml",
            "bytes": len(s.encode("utf-8")),
            "root": (re.search(r"<([A-Za-z][\w.]*)", s).group(1)
                     if re.search(r"<([A-Za-z][\w.]*)", s) else "merge"),
            "ids": ids[:24],
            "idCount": len(ids),
            "styles": sorted(set(re.findall(r'style="@style/([^"]+)"', s))),
        }

    # 4. checkpoint animations + Rive practice asset
    anims = {}
    for n in ANIMS:
        p = SRC / "res" / "anim" / (n + ".xml")
        if p.exists():
            s = p.read_text(encoding="utf-8", errors="replace")
            anims[n] = {"source": "res/anim/" + n + ".xml", "bytes": len(s.encode("utf-8")),
                        "xml": re.sub(r"\s+", " ", s.strip())[:300]}
    raw = []
    p = SRC / "res" / "raw" / "practice.riv"
    if p.exists():
        raw.append({"source": "res/raw/practice.riv", "bytes": p.stat().st_size,
                    "sha256": sha256(p), "role": "Mimo practice animation"})

    # 5. DEX class / literal evidence
    classes = jload(SRC / "dex" / "UI_CLASSES.json")
    names = [c["class"] for c in classes]
    groups = {}
    for key, pat in [
        ("path_map", r"PathMap"), ("smart_practice", r"SmartPractice"),
        ("practice_general", r"Practice"), ("chapter", r"Chapter"),
        ("section", r"Section"),
    ]:
        hit = sorted({n for n in names if re.search(pat, n, re.I)})
        groups[key] = {"count": len(hit), "samples": hit[:12]}
    literals_raw = (SRC / "dex" / "UI_STRING_LITERALS.txt").read_bytes().decode("utf-8", "replace")
    lits = []
    for line in literals_raw.splitlines():
        if re.search(r"practice|bolt|checkpoint|sectionIndex|chapterIndexInSection|tutorialIds|showPathSwitcher|PathMap", line, re.I):
            lits.append(line.strip()[:180])
    lits = sorted(set(l for l in lits if l))[:40]

    # 6. shipped content model for the checkpoint quiz
    # real schema: tracks[0].sections[] + tracks[0].tutorials[] (v6 evidence)
    cm = jload(SRC / "assets" / "ui" / "testdata" / "test-tracks.json")
    track = cm["tracks"][0]
    sections = []
    for s in track.get("sections", []):
        sections.append({
            "name": s.get("name", ""),
            "description": s.get("description", ""),
            "startIndex": s.get("startIndex"),
            "endIndex": s.get("endIndex"),
            "tutorialIds": s.get("tutorialIds", []),
            "tutorialCount": len(s.get("tutorialIds", [])),
        })
    tutorials = [{"id": u.get("id"), "type": u.get("type"),
                  "title": u.get("title", "")} for u in track.get("tutorials", [])]

    # 7. tokens relevant to node geometry
    tok = {
        "colors": {k: {"default": default(colors[k]), "night": (colors[k].get("night") or default(colors[k]))
                       if isinstance(colors[k], dict) else default(colors[k])}
                   for k in COLOR_NAMES if k in colors},
        "dimens": {k: default(dimens[k]) for k in DIMEN_NAMES if k in dimens},
        "styleNames": sorted([k for k in (styles.keys() if isinstance(styles, dict) else [])
                              if re.search(r"TextH|TextTitle|ProgressBarChapter|Glance\.AppWidget\.Circular", k)])[:24],
    }

    doc = {
        "method": "CODE_FIRST / decoded APK resource tables + DEX class inventory (no screenshot tracing)",
        "apk_sha256": "48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a",
        "round": "DESIGN v7 — path-map node reconstruction + bolt checkpoint quiz + routine tab",
        "sources": {
            "tokens": "mimo-ui/CATALOGS/DESIGN_TOKENS.json (50,477 ARSC config rows)",
            "vectors": "mimo-ui/SOURCE/res/drawable/*.xml (exact android:pathData)",
            "layouts": "mimo-ui/SOURCE/res/layout/*.xml (decoded AXML)",
            "anim": "mimo-ui/SOURCE/res/anim/rc_checkpoint_window_*.xml",
            "raw": "mimo-ui/SOURCE/res/raw/practice.riv",
            "content": "mimo-ui/SOURCE/assets/ui/testdata/test-tracks.json",
            "dex": "mimo-ui/SOURCE/dex/UI_CLASSES.json + UI_STRING_LITERALS.txt",
        },
        "strings": picked,
        "vectors": vectors,
        "layouts": layouts,
        "animations": anims,
        "rawAssets": raw,
        "dex": groups,
        "dexLiterals": lits,
        "contentModel": {
            "source": "SOURCE/assets/ui/testdata/test-tracks.json",
            "publishSetVersion": cm.get("publishSetVersion"),
            "trackTitle": track.get("title", ""),
            "trackCount": len(cm.get("tracks", [])),
            "sections": sections,
            "tutorials": tutorials,
            "tutorialCount": len(tutorials),
        },
        "tokens": tok,
        "isolation": [
            "section-practice (bolt checkpoint quiz) is a LEARN sub-screen, class=screen mimo",
            "section-practice has NO timer chip, NO پاسخبرگ/پاسخنامه, NO exam hub, NO 270 min, NO POLICY",
            "exam-hub / exam-run / exam-result remain the only Konkur exam surfaces",
            "routine scoring is isolated from exam scores, leaderboard XP and Learn coins",
        ],
        "counts": {
            "vectors": len(vectors), "vector_misses": len(misses),
            "strings": sum(len(v) for v in picked.values()),
            "layouts": len(layouts), "animations": len(anims),
            "rawAssets": len(raw), "dex_classes": sum(v["count"] for v in groups.values()),
            "dex_literals": len(lits), "sections": len(sections),
            "tutorial_ids": sum(s["tutorialCount"] for s in sections),
            "tutorials": len(tutorials),
            "catalog_rows": len(NODE_ROWS),
        },
        "vectorMisses": misses,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "NODE_CODE_GEOMETRY.json").write_text(
        json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")

    with (UP / "CATALOGS" / "MIMO_PATH_NODES.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["row_id", "kind", "item", "visual", "icon",
                    "code_crosswalk", "click_target", "source_path", "role"])
        for r in NODE_ROWS:
            w.writerow(r)

    print(json.dumps({
        "output": str(OUT / "NODE_CODE_GEOMETRY.json"),
        "bytes": (OUT / "NODE_CODE_GEOMETRY.json").stat().st_size,
        "catalog_rows": len(NODE_ROWS),
        "counts": doc["counts"],
        "vector_misses": misses,
    }, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
