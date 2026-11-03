#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Code-first Mimo 9.35 UI geometry extraction.

Reads the *decoded APK resource tree* (mimo-ui/SOURCE/res), the design-token
catalog and the DEX UI-class census, and emits a machine-readable geometry
file that DESIGN/index.html is generated from. Screenshots are used ONLY as a
visual cross-check -- every colour, dimension, type size, string and SVG path
below comes from the APK's own resource tables.

Usage:  python3 tools/extract_mimo_geometry.py [UPGRADE_ROOT]
"""
from __future__ import annotations
import csv, json, re, sys
from pathlib import Path

UP = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]).resolve()
MIMO = UP.parent                                    # .../mimo-ui
RES = MIMO / "SOURCE" / "res"
TOK = json.loads((MIMO / "CATALOGS" / "DESIGN_TOKENS.json").read_text(encoding="utf-8"))

VECTORS = [
    # bottom navigation -- exact ic_tab_* selector states
    "ic_cap", "ic_cap_filled", "ic_flash", "ic_flash_filled", "ic_trophy",
    "ic_trophy_filled", "ic_user_circle", "ic_user_circle_filled",
    "ic_chat_bubble", "ic_magic_wand", "ic_magic_wand_filled", "ic_ai_tutor",
    # path / chapter / lesson chrome
    "ic_coin", "ic_coins", "ic_streak_active", "ic_streak", "ic_sparks",
    "ic_sparks_alt", "ic_list_bulleted", "ic_check", "ic_check_thick",
    "ic_check_white", "ic_play", "ic_lock_alt_02", "ic_lock_outline",
    "ic_settings", "ic_close", "ic_flag", "ic_infinity", "ic_user_alert",
    "ic_arrow_left", "ic_arrow_right", "ic_arrow_back_24",
    # leaderboard / profile / playground
    "ic_leaderboard_league_1", "ic_leaderboard_league_2",
    "ic_leaderboard_league_3", "ic_leaderboard_league_4",
    "ic_leaderboard_league_5", "ic_leaderboard_league_locked",
    "ic_leaderboard_locked", "img_brain", "ic_code_playground_template_python",
    "ic_code_playground_template_js_only", "ic_code_playground_template_website",
    "ic_code_playground_template_react", "browser_view_header_dots",
    "ic_check_white", "ic_leaderboard_locked",
]
COLORS = [
    "background_primary", "background_secondary", "navbar_background",
    "navbar_text", "navbar_icon", "text_primary", "text_weak", "text_disabled",
    "text_reversed", "icon_primary", "icon_weak", "icon_disabled",
    "card_enabled", "card_pressed", "card_disabled", "card_outline",
    "line_primary", "button_primary", "button_primary_highlight",
    "button_primary_text", "button_secondary_highlight", "support_purple",
    "support_purple_light", "support_green", "support_yellow", "support_blue",
    "support_streak", "progress_primary", "progress_secondary", "progress_weak",
    "progress_empty", "progress_chapter_primary", "progress_chapter_background",
    "streak_primary", "accent_success", "accent_error", "code_highlight",
    "code_highlight_2", "code_primary", "code_background", "code_purple",
]
DIMS = [
    "spacing_xxs", "spacing_xs", "spacing_s", "spacing_m", "spacing_l",
    "spacing_xl", "spacing_xxl", "toolbar_height", "content_max_width",
    "cardview_corner_radius_large", "m3_alert_dialog_corner_size",
    "glance_component_button_corners", "m3_sys_shape_corner_value_extra_large",
    "bottom_sheet_content_max_width", "lesson_progress_navbar_height",
    "lesson_progressbar_height", "lesson_interaction_keyboard_button_height",
    "lesson_description_margin_top", "lesson_description_margin_bottom",
    "lesson_description_margin_start", "lesson_description_margin_end",
    "lesson_codeblock_corner_radius", "lesson_webviewblock_corner_radius",
    "lesson_content_margin_top", "lesson_content_margin_bottom",
    "lessonview_content_maxwidth", "profile_header_avatar_size",
    "leaderboard_league_header_height", "leaderboard_league_header_item_height",
    "leaderboard_league_header_item_width",
    "leaderboard_league_header_item_selected_height",
    "leaderboard_league_header_item_selected_width",
    "leaderboard_item_ranking_margin_start", "leaderboard_item_icon_margin_start",
    "leaderboard_item_name_margin_start", "leaderboard_item_sparks_margin_end",
]
STYLES = ["TextH1", "TextH2", "TextH3", "TextP1", "TextP2", "TextSubtitle",
          "TextLabel1", "TextLabel2", "TextLabel3", "TextButton1", "TextButton2",
          "TextLeaderboardItemTitle", "TextLessonCode"]
STRINGS = [
    "navigation_path", "navigation_practice", "navigation_leaderboard",
    "navigation_profile", "weekly", "leaderboard", "leaderboard_league_name_1",
    "leaderboard_league_name_2", "leaderboard_promotion_zone",
    "leaderboard_trophies_title", "no_trophies_yet_title", "no_trophies_yet_desc",
    "playgrounds", "playgrounds_empty_title", "playgrounds_empty_description",
    "playgrounds_create_new", "playgrounds_see_all", "create_playground",
    "codeplayground_template_label", "codeplayground_template_python_title",
    "codeplayground_template_python_description",
    "codeplayground_template_js_title", "codeplayground_template_website_title",
    "codeplayground_template_react_title", "codeplayground_template_website_description",
    "start_learning", "learn", "chapter", "continue_cta", "lesson_continue",
    "step_continue", "total_xp", "xp", "league", "user_profile", "friends_follow",
    "onboarding_get_started", "learn_on_your_phone", "report", "profile",
    "codeplayground_result_header_output", "path_see_course_overview",
    "path_overview_section_ordinal", "path_overview_certificate_percent_complete",
    "section_details_smart_practice_mastered_dialog_title",
]
LAYOUTS = [
    "bottom_navigation_menu.xml", "toolbar.xml", "chapter_toolbar.xml",
    "chapter_activity.xml", "lesson_noninteractive_fragment.xml",
    "lesson_description_textview.xml", "lesson_output_codeblock_textview.xml",
    "lesson_interactive_multiplechoice_fragment.xml", "profile_fragment.xml",
    "profile_info_card_view.xml", "profile_empty_trophies_item.xml",
    "profile_header.xml", "public_profile_fragment.xml",
    "leaderboard_fragment_active.xml", "leaderboard_item.xml",
    "leaderboard_promotion_divider.xml", "leaderboard_league_header_view.xml",
    "leaderboard_league_header_item.xml", "onboarding_pick_a_path.xml",
]


def vector(name: str) -> dict:
    p = RES / "drawable" / (name + ".xml")
    if not p.is_file():
        return {"missing": True}
    s = p.read_text(encoding="utf-8")
    vw = re.search(r'android:viewportWidth="([\d.]+)"', s)
    vh = re.search(r'android:viewportHeight="([\d.]+)"', s)
    w = re.search(r'android:width="([\d.]+)dip"', s)
    h = re.search(r'android:height="([\d.]+)dip"', s)
    tags = re.findall(r"<path\b([^>]*)/>", s)
    paths = []
    for t in tags:
        d = re.search(r'android:pathData="([^"]+)"', t)
        f = re.search(r'android:fillColor="([^"]+)"', t)
        a = re.search(r'android:fillAlpha="([\d.]+)"', t)
        ft = re.search(r'android:fillType="(\d+)"', t)
        if d:
            paths.append({"d": d.group(1), "fill": f.group(1) if f else None,
                          "alpha": a.group(1) if a else None,
                          "fillType": ft.group(1) if ft else None})
    return {"source": "res/drawable/" + name + ".xml",
            "viewport": [float(vw.group(1)) if vw else 24,
                         float(vh.group(1)) if vh else 24],
            "size_dp": [float(w.group(1)) if w else 24,
                        float(h.group(1)) if h else 24],
            "paths": paths, "sha_bytes": len(s.encode("utf-8"))}


def style(name: str) -> dict:
    raw = TOK["styles"].get(name, {}).get("default", [])
    out = {}
    for a in raw:
        if not isinstance(a, dict):
            continue
        k = a.get("attr", "").split("/")[-1]
        if k in {"textSize", "lineSpacingExtra", "fontFamily", "textAllCaps", "textColor"}:
            out[k] = a.get("value")
    return {"source": "res/values/styles.xml", "default": out}


def layout(name: str) -> dict:
    p = RES / "layout" / name
    if not p.is_file():
        return {"missing": True}
    s = p.read_text(encoding="utf-8")
    ids = re.findall(r'android:id="@(?:\+)?id/([^"]+)"', s)
    dims = sorted(set(re.findall(r'"([\d.]+)dip"', s)))
    refs = sorted(set(re.findall(r'"@(?:dimen|color|drawable|string|style)/([^"]+)"', s)))
    return {"source": "res/layout/" + name, "bytes": len(s.encode("utf-8")),
            "ids": ids, "literal_dip": [float(x) for x in dims], "refs": refs}


def main() -> None:
    geo = {
        "method": "CODE_FIRST / decoded APK resource tables (no screenshot tracing)",
        "apk_sha256": "48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a",
        "apk_version": "9.35 / 1792759685",
        "sources": {
            "vectors": "mimo-ui/SOURCE/res/drawable/*.xml (decoded AXML)",
            "tokens": "mimo-ui/CATALOGS/DESIGN_TOKENS.json (50,477 ARSC config rows)",
            "layouts": "mimo-ui/SOURCE/res/layout/*.xml (decoded AXML)",
            "dex": "mimo-ui/SOURCE/dex/UI_CLASSES.json (3,255 classes / Compose inventory)",
            "screenshots": "DESIGN/REFERENCE/*.jpg|webp -- visual cross-check ONLY",
        },
        "vectors": {n: vector(n) for n in VECTORS},
        "colors": {k: TOK["colors"].get(k, {"default": None, "night": None})
                   for k in COLORS},
        "dimens": {k: TOK["dimens"].get(k, {"default": None}) for k in DIMS},
        "styles": {k: style(k) for k in STYLES},
        "strings": {k: (TOK["strings"].get(k, {}).get("default")
                        if isinstance(TOK["strings"].get(k), dict) else None)
                    for k in STRINGS},
        "layouts": {n: layout(n) for n in LAYOUTS},
        "nav_menu": sorted(set(re.findall(
            r'android:id="@id/([^"]+)"',
            (RES / "menu" / "bottom_navigation_menu.xml").read_text(encoding="utf-8")))),
        "nav_tint_selector": (RES / "drawable" / "bottom_navigation_colors.xml")
            .read_text(encoding="utf-8").strip(),
    }
    dex = json.loads((MIMO / "SOURCE" / "dex" / "UI_CLASSES.json").read_text(encoding="utf-8"))
    geo["compose_path_classes"] = sorted({c["class"] for c in dex
        if "/path/map/" in c["class"] or "/path/overview/" in c["class"]
        or "PathMapScreenKt" in c["class"]})[:80]
    geo["compose_path_class_count"] = len(geo["compose_path_classes"])

    out = UP / "DESIGN" / "CODE_GEOMETRY.json"
    out.write_text(json.dumps(geo, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    # human-readable crosswalk: element -> exact code source -> exact value
    rows = [["element", "code_source", "attribute", "exact_value", "used_in_design"]]
    for n, v in geo["vectors"].items():
        rows.append(["vector:" + n, v.get("source", "missing"), "pathData",
                     (v["paths"][0]["d"][:110] + "…") if v.get("paths") else "MISSING",
                     "SVG icon rendered by icon() from CODE_GEOMETRY.json"])
    for k, v in geo["colors"].items():
        rows.append(["color:" + k, "res/values/colors.xml (ARSC)", "day / night",
                     "%s / %s" % (v.get("default"), v.get("night")), "CSS custom property"])
    for k, v in geo["dimens"].items():
        rows.append(["dimen:" + k, "res/values/dimens.xml", "default",
                     str(v.get("default")), "CSS --d-* spacing/size token"])
    for k, v in geo["styles"].items():
        rows.append(["style:" + k, "res/values/styles.xml", "textSize / font",
                     "%s / %s" % (v["default"].get("textSize"), v["default"].get("fontFamily")),
                     "CSS type scale"])
    for k, v in geo["strings"].items():
        rows.append(["string:" + k, "res/values/strings.xml", "default", str(v),
                     "unchanged Mimo chrome label"])
    for k, v in geo["layouts"].items():
        rows.append(["layout:" + k, v.get("source", "missing"), "literal dip / ids",
                     "%s / %d ids" % (",".join(str(x) for x in v.get("literal_dip", [])[:8]),
                                      len(v.get("ids", []))), "screen structure"])
    p = UP / "CATALOGS" / "MIMO_CODE_GEOMETRY.csv"
    with p.open("w", encoding="utf-8", newline="") as f:
        csv.writer(f).writerows(rows)
    print(json.dumps({
        "vectors": len(geo["vectors"]),
        "vectors_with_paths": sum(1 for v in geo["vectors"].values() if v.get("paths")),
        "colors": len(geo["colors"]), "dimens": len(geo["dimens"]),
        "styles": len(geo["styles"]), "strings": len(geo["strings"]),
        "layouts": len(geo["layouts"]), "compose_path_classes": geo["compose_path_class_count"],
        "csv_rows": len(rows) - 1, "json_bytes": out.stat().st_size,
    }, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
