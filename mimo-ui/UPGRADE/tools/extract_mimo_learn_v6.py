#!/usr/bin/env python3
"""extract_mimo_learn_v6.py — code-first reverse engineering of Mimo 9.35 Learn sub-screens.

Reads ONLY decoded APK artifacts that were produced by the earlier static census:
  mimo-ui/CATALOGS/DESIGN_TOKENS.json  (ARSC strings/colors/dimens/styles)
  mimo-ui/SOURCE/res/drawable/*.xml    (decoded vector pathData)
  mimo-ui/SOURCE/res/layout/*.xml     (decoded AXML)
  mimo-ui/SOURCE/res/navigation/*.xml (decoded nav graphs)
  mimo-ui/SOURCE/assets/ui/testdata/test-tracks.json (content model shipped in APK)
  mimo-ui/SOURCE/dex/UI_CLASSES.json  (DEX class/method inventory)
  mimo-ui/SOURCE/dex/UI_STRING_LITERALS.txt

Writes:
  DESIGN/LEARN_CODE_GEOMETRY.json
  CATALOGS/MIMO_LEARN_SUBSCREENS.csv

No screenshot is parsed. Screenshots are visual cross-checks only.
"""
import csv
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


def vector(name):
    """Decode a single <vector> drawable into viewport + paths (exact pathData preserved)."""
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


def main():
    tokens = jload(CAT / "DESIGN_TOKENS.json")
    strings, colors, dimens, styles = (tokens[k] for k in ("strings", "colors", "dimens", "styles"))

    # ---- 1. exact string resources that define the Learn sub-screens ----
    string_groups = {
        "track_switcher": r"^track_switcher_|^select_path$|^courses$|^course$|^section$|^search_tracks$|^switch_role$|^reactivation_switch_course$|^lesson_confirm_exit_choose_different_path$|^onboarding_adapted_see_all_courses$|^onboarding_path_type_career_path|^onboarding_path_type_career_paths$|^onboarding_pick_a_path_recommendation_subtitle$",
        "path_overview": r"^path_overview_|^path_see_course_overview$|^path_section_coming_soon|^path_coming_soon|^path_project_preview_label$|^back_to_path$|^path_map_|^alert_msg_section_setion_locked$|^path_completion_estimation_|^path_password_",
        "certificate": r"^certificates_professional_title$|^certificates_unfinished_track_|^certificates_finished_track_|^certificates_of_completion$|^certificate$|^certificates_download$|^path_overview_certificate_",
        "section_details": r"^section_details_|^section$|^chapter_|^lesson_|^path_overview_section_",
    }
    picked = {}
    for group, pat in string_groups.items():
        picked[group] = {
            k: default(v) for k, v in sorted(strings.items())
            if re.search(pat, k) and default(v)
        }

    # ---- 2. exact vectors used by these screens ----
    vector_names = [
        "ic_list_bulleted", "ic_switch", "two_way_arrows", "ic_close",
        "ic_key", "ic_key_big", "ic_key_disabled", "ic_unlimited_keys",
        "ic_coin", "ic_coins", "ic_streak_active", "ic_streak", "ic_sparks",
        "ic_infinity", "check_circle", "ic_check", "ic_check_thick", "ic_check_white",
        "ic_play", "ic_lock_alt_02", "ic_lock_outline", "ic_arrow_right", "ic_arrow_left",
        "ic_badge_backend_professional", "ic_badge_backend", "ic_badge_fullstack",
        "ic_badge_frontend", "ic_badge_python_dev", "ic_badge_html", "ic_badge_css",
        "ic_badge_js", "ic_badge_ts", "ic_badge_react", "ic_badge_sql", "ic_badge_python",
        "ic_code_lang_html", "ic_code_lang_css", "ic_code_lang_python", "ic_code_lang_sql",
        "ic_mimo_mascot", "ic_mascot_practice", "ic_certificate_completed",
    ]
    vectors, vector_misses = {}, []
    for n in vector_names:
        v = vector(n)
        if v:
            vectors[n] = v
        else:
            vector_misses.append(n)

    # ---- 3. exact AXML layouts ----
    layout_names = [
        "onboarding_select_path_fragment", "onboarding_pick_a_path",
        "onboarding_path_completion_estimation_fragment",
        "search_track_fragment", "search_tracks_list_item",
        "profile_certificate_view", "profile_certificates_item", "profile_certificates_view",
        "certificate_activity", "certificate_download_dialog_fragment",
        "chapter_toolbar", "chapter_activity", "chapter_finished_fragment",
        "lesson_noninteractive_fragment", "practice_tab_fragment",
        "bottom_navigation_menu",
    ]
    layouts = {}
    for n in layout_names:
        p = SRC / "res" / ("menu" if n == "bottom_navigation_menu" else "layout") / (n + ".xml")
        if n == "bottom_navigation_menu":
            p = SRC / "res" / "menu" / "bottom_navigation_menu.xml"
        if p.exists():
            s = p.read_text(encoding="utf-8", errors="replace")
            layouts[n] = {
                "source": str(p.relative_to(MIMO)),
                "bytes": len(s.encode("utf-8")),
                "ids": sorted(set(re.findall(r'android:id="@(?:\+)?id/([A-Za-z0-9_]+)"', s))),
                "styles": sorted(set(re.findall(r'style="@style/([A-Za-z0-9_.]+)"', s))),
                "dimens": sorted(set(re.findall(r'@dimen/([A-Za-z0-9_]+)', s))),
                "colors": sorted(set(re.findall(r'@color/([A-Za-z0-9_]+)', s))),
                "strings": sorted(set(re.findall(r'@string/([A-Za-z0-9_]+)', s))),
                "drawables": sorted(set(re.findall(r'@drawable/([A-Za-z0-9_]+)', s))),
                "views": sorted(set(re.findall(r"<([A-Za-z0-9_.]+)\b", s))),
                "xml": s,
            }

    # ---- 4. navigation graph edges (code-level routing) ----
    nav = {}
    for p in sorted((SRC / "res" / "navigation").glob("*.xml")):
        s = p.read_text(encoding="utf-8", errors="replace")
        frags = re.findall(r'<fragment[^>]*android:name="([^"]+)"[^>]*android:id="@\+?id/([A-Za-z0-9_]+)"', s)
        acts = re.findall(r'<action[^>]*android:id="@\+?id/([A-Za-z0-9_]+)"[^>]*app:destination="@\+?id/([A-Za-z0-9_]+)"', s)
        nav[p.name] = {
            "source": str(p.relative_to(MIMO)),
            "fragments": [{"id": b, "class": a} for a, b in frags],
            "actions": [{"id": a, "destination": b} for a, b in acts],
        }

    # ---- 5. content model shipped inside the APK (real track/section/tutorial schema) ----
    tracks_path = SRC / "assets" / "ui" / "testdata" / "test-tracks.json"
    tracks = jload(tracks_path)
    mock_path = SRC / "assets" / "ui" / "mock" / "tracks.json"
    mock = jload(mock_path)
    content_model = {
        "source": str(tracks_path.relative_to(MIMO)),
        "publishSetVersion": tracks.get("publishSetVersion"),
        "trackCount": len(tracks.get("tracks", [])),
        "trackKeys": sorted(tracks["tracks"][0].keys()),
        "sectionKeys": sorted(tracks["tracks"][0]["sections"][0].keys()) if tracks["tracks"][0].get("sections") else [],
        "tutorialKeys": sorted(tracks["tracks"][0]["tutorials"][0].keys()),
        "sections": [
            {"name": s["name"], "description": s["description"],
             "startIndex": s["startIndex"], "endIndex": s["endIndex"],
             "tutorialIds": s.get("tutorialIds", []),
             "tutorialCount": len(s.get("tutorialIds", []))}
            for s in tracks["tracks"][0].get("sections", [])
        ],
        "tutorials": tracks["tracks"][0].get("tutorials", []),
        "careerPathSectionCount": len(tracks["tracks"][0].get("sections", [])),
        "secondSource": str(mock_path.relative_to(MIMO)),
        "secondPublishSetVersion": mock.get("publishSetVersion"),
        "secondTrackCount": len(mock.get("tracks", [])),
    }

    # ---- 6. DEX classes / literals that define behaviour ----
    classes = jload(SRC / "dex" / "UI_CLASSES.json")
    class_pats = {
        "path_map": r"ui/path/map/",
        "path_overview": r"ui/path/overview/",
        "path_switcher": r"ObservePathSwitcherState|interactors/path/",
        "select_path": r"onboarding/selectpath/",
        "certificate": r"ui/certificates/|interactors/certificates/",
        "section_model": r"content/model/track/",
    }
    dex = {}
    for g, pat in class_pats.items():
        names = sorted({c["class"] for c in classes if re.search(pat, c["class"])})
        dex[g] = {"count": len(names), "classes": names}
    lit_path = SRC / "dex" / "UI_STRING_LITERALS.txt"
    lits = lit_path.read_bytes().decode("utf-8", errors="replace").splitlines()
    lit_pat = re.compile(r"showPathSwitcher|key_path_switcher|SectionJson|TrackIdKt|onNextSection|sectionIndex|sectionTitle|PathOverview|isCareerPath|chaptersCompleted|sectionEstimatedCompletionByIndex|SectionEta|CompleteOrUnlocked|SectionProject")
    dex["literals"] = sorted({l.strip() for l in lits if lit_pat.search(l)})

    # ---- 7. exact design tokens used by these screens ----
    color_pat = re.compile(r"^(card_|progress_|background_|text_|icon_|line_|surface|outline|support_|button_)", re.I)
    dimen_pat = re.compile(r"^(spacing_|cardview_|lesson_|toolbar_|m3_alert_dialog_|glance_component_|profile_header_|content_max_width_|sheet_|icon_size_|general_margin_)", re.I)
    style_pat = re.compile(r"^(Text|Widget\.Mimo|Mimo|ShapeAppearance\.Mimo|Theme\.Mimo)", re.I)
    tok = {
        "colors": {k: default(v) for k, v in sorted(colors.items()) if color_pat.search(k)},
        "dimens": {k: default(v) for k, v in sorted(dimens.items()) if dimen_pat.search(k)},
        "styleNames": sorted([k for k in styles if style_pat.search(k)]),
    }

    geom = {
        "generator": "tools/extract_mimo_learn_v6.py",
        "method": "code-first static reverse engineering of decoded APK resources; no screenshot parsing",
        "apk": "com.getmimo 9.35 / versionCode 1792759685",
        "strings": picked,
        "vectors": vectors,
        "vectorMisses": vector_misses,
        "layouts": layouts,
        "navigation": nav,
        "contentModel": content_model,
        "dex": dex,
        "tokens": tok,
    }
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "LEARN_CODE_GEOMETRY.json").write_text(
        json.dumps(geom, ensure_ascii=False, indent=1), encoding="utf-8")

    # ---- 8. flat evidence catalog: one row per reconstructed Learn sub-screen element ----
    rows = []

    def row(area, screen, element, exact_value, code_source, kind, role):
        rows.append({
            "area": area, "screen": screen, "element": element,
            "exact_value_from_code": exact_value, "code_source": code_source,
            "evidence_kind": kind, "design_role": role,
            "screenshots": "VISUAL_CROSSCHECK_ONLY",
        })

    for g, vals in picked.items():
        for k, v in vals.items():
            row("strings", g, k, v, "CATALOGS/DESIGN_TOKENS.json :: strings." + k, "ARSC string", "keep verbatim")
    for n, v in vectors.items():
        row("vectors", "learn-chrome", n, str(len(v["paths"])) + " path(s), viewport " + str(v["viewportWidth"]) + "x" + str(v["viewportHeight"]),
            v["source"], "decoded vector pathData", "render exact SVG geometry")
    for n, v in layouts.items():
        row("layouts", n, "AXML", str(v["bytes"]) + " bytes / " + str(len(v["ids"])) + " ids", v["source"], "decoded AXML", "structural skeleton")
    for n, v in nav.items():
        for a in v["actions"]:
            if re.search(r"path|course", a["id"] + a["destination"], re.I):
                row("navigation", n, a["id"], a["destination"], v["source"], "nav graph action", "screen transition")
    for s in content_model["sections"]:
        row("content", "path-overview", "section " + str(content_model["sections"].index(s) + 1),
            s["name"] + " | " + s["description"] + " | " + str(s["startIndex"]) + "-" + str(s["endIndex"]) + " | " + str(s["tutorialCount"]) + " tutorials",
            content_model["source"], "shipped JSON content model", "section ordinal + description + lesson count")
    for t in content_model["tutorials"]:
        row("content", "select-path", "tutorial " + str(t.get("id")), str(t.get("title")) + " | " + str(t.get("type")),
            content_model["source"], "shipped JSON content model", "course row / lesson id")
    for g, v in dex.items():
        if g == "literals":
            for l in v:
                row("dex", "behaviour", "DEX literal", l, "SOURCE/dex/UI_STRING_LITERALS.txt", "DEX string literal", "behaviour evidence")
        else:
            for c in v["classes"]:
                row("dex", g, "class", c, "SOURCE/dex/UI_CLASSES.json", "DEX class", "screen/viewmodel evidence")
    for k, v in tok["colors"].items():
        row("tokens", "learn-chrome", "color " + k, v, "CATALOGS/DESIGN_TOKENS.json :: colors", "ARSC color", "exact token")
    for k, v in tok["dimens"].items():
        row("tokens", "learn-chrome", "dimen " + k, v, "CATALOGS/DESIGN_TOKENS.json :: dimens", "ARSC dimen", "exact token")
    for k in tok["styleNames"]:
        row("tokens", "learn-chrome", "style " + k, "TextAppearance", "CATALOGS/DESIGN_TOKENS.json :: styles", "ARSC style", "exact token")

    p = CAT.parent / "UPGRADE" / "CATALOGS" / "MIMO_LEARN_SUBSCREENS.csv"
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    print("LEARN_CODE_GEOMETRY.json", (OUT / "LEARN_CODE_GEOMETRY.json").stat().st_size, "bytes")
    print("strings", {k: len(v) for k, v in picked.items()})
    print("vectors", len(vectors), "misses", vector_misses)
    print("layouts", len(layouts), "nav graphs", len(nav))
    print("content sections", len(content_model["sections"]), "tutorials", len(content_model["tutorials"]))
    print("dex classes", {k: v["count"] for k, v in dex.items() if k != "literals"}, "literals", len(dex["literals"]))
    print("tokens", len(tok["colors"]), "colors /", len(tok["dimens"]), "dimens /", len(tok["styleNames"]), "styles")
    print("MIMO_LEARN_SUBSCREENS.csv", len(rows), "rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
