#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fail-closed verification of the Konkur-upgrade planning deliverable (v12.5)."""
from __future__ import annotations
import csv, hashlib, json, re, sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else "/home/user/game/mimo-ui/UPGRADE")
docs = ["README.md", "00_START_HERE.md", "01_CRAFT_ANYTHING_INSTALL.md",
        "02_UI_FIDELITY_CONTRACT.md", "03_EXAM_HUB.md", "04_AI_LEARN_HARNESS.md",
        "05_COUNSELING_HADAF_PLUS.md", "06_PROFILE_AND_GAMIFICATION.md",
        "07_LESSON_STRUCTURE_AND_QUESTIONS.md", "08_NAVIGATION_AND_IA.md",
        "09_DATA_MODEL_AND_BACKEND.md", "10_PHASED_ROADMAP.md",
        "11_EVIDENCE_AND_CROSSWALK.md", "12_RISKS_UNKNOWN_AND_QUESTIONS.md",
        "13_DESIGN_ROUND_2.md", "14_DESIGN_ROUND_3.md", "15_DESIGN_ROUND_4.md",
        "16_DESIGN_ROUND_5.md", "17_DESIGN_ROUND_6.md",
        "18_DESIGN_ROUND_7.md", "20_DESIGN_ROUND_8.md", "21_DESIGN_ROUND_9.md", "22_DESIGN_ROUND_10.md", "23_DESIGN_ROUND_11.md", "24_DESIGN_ROUND_12.md", "wireframes.html"]
csvs = {"UI_FIDELITY_RULES.csv": 46, "FEATURE_MAP.csv": 17, "EXAM_TYPES.csv": 11,
        "HADAF_TEMPLATES.csv": 7, "GAMIFICATION_MAP.csv": 13, "PHASES.csv": 8,
        "LEARNHARNESS_ACTIONS.csv": 32, "EVIDENCE_LEDGER.csv": 10, "OPEN_QUESTIONS.csv": 13,
        "DESIGN_FEEDBACK.csv": 70, "SCOPE_DECISIONS.csv": 50,
        "AI_PANEL_SPEC.csv": 27, "EPM_MINOR_OPTIONS.csv": 7,
        "EXAM_SECTION_TEMPLATES.csv": 7,
        "MIMO_CODE_GEOMETRY.csv": 200, "MIMO_SCREENSHOT_CROSSWALK.csv": 14,
        "ANSWER_SHEET_POLICY.csv": 5, "MIMO_LEARN_SUBSCREENS.csv": 868,
        "KONKUR_CURRICULUM.csv": 180,
        "MIMO_PATH_NODES.csv": 106, "PRACTICE_VS_EXAM.csv": 12}
checks, problems = [], []


def ck(name, ok, detail=""):
    checks.append({"check": name, "status": "PASS" if ok else "FAIL", "detail": detail})
    if not ok:
        problems.append(name + ": " + detail)


def rows(p):
    with p.open(encoding="utf-8", newline="") as f:
        return list(csv.reader(f))


for d in docs:
    p = ROOT / d
    ck("doc:" + d, p.is_file() and p.stat().st_size > 400, str(p.stat().st_size) if p.is_file() else "missing")
for name, n in csvs.items():
    p = ROOT / "CATALOGS" / name
    ck("csv:" + name, p.is_file() and len(rows(p)) - 1 == n,
       "%d rows" % (len(rows(p)) - 1) if p.is_file() else "missing")

# wireframe uses real tokens and states the legacy tabs
t = (ROOT / "wireframes.html").read_text(encoding="utf-8")
ck("wireframe:tokens", all(x in t for x in ["#7E4BDE", "#F6F7FB", "#E4E6F1", "#66BC5A", "#F05A6E"]),
   "Mimo palette present")
ck("wireframe:legacy-tabs", t.count('class="tab') >= 4 and 'data-code="Learn"' in t
   and ">یادگیری</div>" in t and ">تمرین</div>" in t and ">امتیازها</div>" in t and ">پروفایل</div>" in t,
   "v12.5-fa: archived v1 tabs are Persian; legacy EN labels kept as data-code evidence")
ck("wireframe:3col-grid", "repeat(3,minmax(0,1fr))" in t, "exam node grid")
ck("wireframe:v1-banner", "DESIGN/index.html" in t and "DESIGN v12" in t, "v1 archived, points to v12")

# ---- DESIGN v8 interactive prototype ----
D = ROOT / "DESIGN"
dt = (D / "index.html").read_text(encoding="utf-8") if (D / "index.html").is_file() else ""
ck("design:index", len(dt) > 20000, "%d chars" % len(dt))
ck("design:v12-header", "DESIGN v12" in dt and "دور دوازدهم" in dt, "design round 12 review")
ck("design:v7-archived", "DESIGN v7" in dt, "v7 archive line kept in spec")
ck("design:v6-archived", "DESIGN v6" in dt, "v6 archive line kept in spec")
ck("design:no-hub-timer", "exam-hub" in dt and "⏱ ۱۲:۴۵" not in dt, "timer removed from exam hub")
ck("design:timer-states", all(x in dt for x in ["timerSheet","timerStart","timerPause","timerReset","finished"]), "click-number-start-countdown")
ck("design:counseling-removed",
   'data-screen="counseling"' not in dt and "konkur-plan-v2" not in dt and "localStorage" not in dt and "goalSheet" not in dt,
   "counseling page PARKED / removed")
ck("design:ai-minimal", all(x in dt for x in
   ["chatThread","aiInput","aiSend","historySheet","histList","newChat","typing","aiContext"]), "minimal chat + history")
ck("design:ai-no-clutter", all(x not in dt for x in
   ["lhDock","sessList","Knowledge graph","BACKGROUND AGENTS"]), "no 32-button dock / sessions sidebar")
ck("design:lh-buttons", all(x in dt for x in
   ["Chains","Import notes","gemini-flash-lite-latest","medium","TEACH","PRACTICE"])
   and not re.search(r'<button[^>]*data-lh="Dictate"', dt) and "ic_microphone\" data-size=\"18\"" not in dt,
   "LH buttons restored, Dictate removed")
ck("design:epm-link", "askAi" in dt and "EPM" in dt, "minor EPM idea referenced in audit panel only")
ck("design:14views", dt.count('<button data-go=') == 14, "14 design views (routine view removed)")
ck("design:5tabs", dt.count('data-tab="') == 5 and all(x in dt for x in
   ['data-tab="Learn"','data-tab="Practice"','data-tab="AI"','data-tab="Leaderboard"','data-tab="Profile"'])
   and '>یادگیری</span>' in dt and '>تمرین</span>' in dt and '>هوش مصنوعی</span>' in dt
   and '>امتیازها</span>' in dt and '>پروفایل</span>' in dt and "var tabFa=" in dt
   and 'data-tab="MAX"' not in dt and 'data-tab="Routine"' not in dt,
   "5 Mimo tabs restored; MAX and روتین روزانه forbidden")
ck("design:learn", 'data-screen="learn"' in dt and "PathMapScreenKt" in dt and "overview-card" in dt and '<section class="screen mimo on" data-screen="learn">' in dt and dt.split('data-screen="learn"')[1].split("</section>")[0].count("path-note") == 0,
   "Learn rebuilt clean: 3 pills + overview header card, annotations removed")
ck("design:leaderboard", 'data-screen="leaderboard"' in dt and "selfbox" in dt and "آزمونها و امتیازات من" in dt,
   "leaderboard view with own info/scores/exams")
ck("design:answer-sheet", all(x in dt for x in
   ["answerSheetBtn","policyHint","keyTestSheet","keyDescSheet","POLICY","during:false","during:true"]), "answer sheet policy + two keys")
ck("design:answer-split", all(x in dt for x in
   ["پاسخبرگ","پاسخنامه","answerKeyBtn","keySheet","paletteSheet","keytabs"]) and "زمان خالص" in dt,
   "پاسخبرگ (chosen options) ≠ پاسخنامه (descriptive) + pure-time policy")
ck("design:labeled-sections", dt.count('class="cat-meta"') == 7 and "زمان ثابت ۲۷۰ دقیقه" in dt,
   "7 labeled sections with fixed-time comprehensive template")
ck("design:api-key-not-designed", "DOCUMENTED_ONLY" not in dt and "وارد کردن کلید API" in dt,
   "API key is a note only, no settings UI")
js = re.search(r"<script>(.*?)</script>", dt, re.S)
used = set(re.findall(r'\bq\("#([A-Za-z0-9_-]+)"\)', js.group(1))) if js else set()
defined = set(re.findall(r'id="([A-Za-z0-9_-]+)"', dt))
ck("design:js-ids", bool(js) and used <= defined, "%d used / %d defined; missing=%s" % (len(used), len(defined), sorted(used-defined)[:8]))
ck("design:notes", (D / "DESIGN_NOTES.fa.md").is_file() and (D / "DESIGN_NOTES.fa.md").stat().st_size > 2000, "design notes")

# ---- CODE-FIRST reconstruction (v5) ----
gp = D / "CODE_GEOMETRY.json"
ck("design:code-geometry", gp.is_file(), "CODE_GEOMETRY.json present")
if gp.is_file():
    g = json.loads(gp.read_text(encoding="utf-8"))
    ck("design:code-vectors", len(g["vectors"]) >= 40 and all(v.get("paths") for v in g["vectors"].values()),
       "%d vectors with pathData" % len(g["vectors"]))
    ck("design:code-colors", len(g["colors"]) >= 40 and len(g["dimens"]) >= 30 and len(g["styles"]) >= 10,
       "%d colors / %d dimens / %d styles" % (len(g["colors"]), len(g["dimens"]), len(g["styles"])))
    ck("design:code-layouts", len(g["layouts"]) >= 15 and g["compose_path_class_count"] >= 50,
       "%d AXML layouts / %d Compose path classes" % (len(g["layouts"]), g["compose_path_class_count"]))
    ck("design:code-method", "CODE_FIRST" in g["method"] and "no screenshot tracing" in g["method"],
       "method is code-first, screenshots are cross-check only")
    ck("design:svg-from-code", "var GEO=" in dt and "GEO.vectors" in dt and "fill-rule" in dt and "rgba(" in dt,
       "icons rendered from extracted pathData (AARRGGBB -> rgba)")
    ck("design:css-from-code", "--bg:" in dt and "body.night" in dt and "--progress:" in dt,
       "CSS custom properties injected from ARSC colour tables")
ck("design:build-tools", all((ROOT / "tools" / f).is_file() for f in
   ["extract_mimo_geometry.py", "build_design_v5.py", "design_v5_template.html",
    "extract_mimo_learn_v6.py", "build_design_v6.py", "design_v6_template.html",
    "extract_mimo_nodes_v7.py", "build_design_v7.py", "design_v7_template.html", "finalize_v7.py",
    "extract_mimo_nodes_v8.py", "build_design_v8.py", "design_v8_template.html", "finalize_v8.py",
    "extract_mimo_nodes_v9.py", "build_design_v9.py", "design_v9_template.html", "finalize_v9.py",
    "extract_mimo_nodes_v10.py", "build_design_v10.py", "design_v10_template.html", "finalize_v10.py",
    "design_v10_full.html", "build_design_v11.py", "design_v11_template.html", "finalize_v11.py",
    "design_v11_full.html", "build_design_v12.py", "design_v12_template.html", "finalize_v12.py",
    "fix_design_v12_1.py", "design_v12_1_template.html", "build_exam_v12_3.py",
    "design_v12_3_template.html", "finalize_v12_3.py", "build_exam_v12_4.py",
    "design_v12_4_template.html", "finalize_v12_4.py", "build_exam_v12_5.py",
    "design_v12_5_template.html", "finalize_v12_5.py"]),
   "reproducible extract -> build pipeline (v5..v11 archived + v12 current)")

# ---- 14 Mimo reference screenshots (visual cross-check only) ----
shots = ["mimo-01-learn-path-play.jpg","mimo-02-learn-path-half.jpg",
         "mimo-03-chapter-start-dialog.jpg","mimo-04-lesson-continue.jpg",
         "mimo-05-weekly-leaderboard.jpg","mimo-06-user-profile.jpg",
         "mimo-07-profile-trophies.jpg","mimo-08-create-playground.jpg",
         "mimo-09-onboarding.webp",
         "mimo-10-path-map-current.jpg","mimo-11-select-path-careers.jpg",
         "mimo-12-select-path-courses.jpg","mimo-13-path-overview-sections.jpg",
         "mimo-14-unfinished-track-dialog.jpg"]
ck("design:14screenshots", all((D / "REFERENCE" / s).is_file() and (D / "REFERENCE" / s).stat().st_size > 10000 for s in shots),
   "%d Mimo screenshots archived" % len(shots))
for i, (f, minsz) in enumerate([("learnharness-ui-user-screenshot.png", 10000),
                                ("learnharness-main-panel-user-screenshot.png", 10000),
                                ("lh-composer-user-screenshot.png", 5000),
                                ("lh-topbar-user-screenshot.png", 3000)], 1):
    p = D / "REFERENCE" / f
    ck("design:screenshot" + (str(i) if i > 1 else ""), p.is_file() and p.stat().st_size > minsz, f)
xw = (ROOT / "CATALOGS/MIMO_SCREENSHOT_CROSSWALK.csv").read_text(encoding="utf-8")
ck("design:screenshot-role", xw.count("VISUAL_CROSSCHECK_ONLY") == 14, "all 14 screenshots marked visual cross-check only")

# ---- AI exam buttons (one button, two places) ----
ck("design:ai-exam-button", all(x in dt for x in
   ["askAiBtn","askAiResultBtn","توضیح با هوش مصنوعی","صورت اشتباهات","پاسخ صحیح"]),
   "one AI button on question page + same button on result page")
ck("csv:answer-policy", (ROOT / "CATALOGS/ANSWER_SHEET_POLICY.csv").is_file()
   and "during_exam_answer_key" in (ROOT / "CATALOGS/ANSWER_SHEET_POLICY.csv").read_text(encoding="utf-8"),
   "machine-readable answer sheet / answer key policy")

# ---- DESIGN v6: Learn sub-screens, code-first deep extraction ----
ck("design:v6:no-onboarding", 'data-screen="onboarding"' not in dt and 'data-go="onboarding"' not in dt,
   "onboarding removed from design per user")
for scr in ["select-path","path-overview","section-detail"]:
    ck("design:v6:screen-"+scr, 'data-screen="%s"' % scr in dt, scr + " reconstructed")
ck("design:v6:three-lines", 'id="pathSwitchBtn"' in dt and 'data-nav="select-path"' in dt,
   "ic_list_bulleted three-lines icon opens Select Path")
ck("design:v6:overview-entry", 'id="overviewEntry"' in dt and 'data-nav="path-overview"' in dt,
   "path header card opens Path Overview")
ck("design:v6:ic-switch", 'id="overviewSwitch"' in dt and 'ic_switch' in dt,
   "two-way arrows open Select Path from Path Overview")
ck("design:v6:unfinished", all(x in dt for x in ["unfinishedModal","Unfinished track","personalised certificate","ic_mimo_mascot"])
   and ">مسیر ناتمام</h2>" in dt and ">باشه</button>" in dt,
   "Unfinished track modal from certificate strings")
ck("design:v6:career-content", all(x in dt for x in ["Career Paths","Full-Stack Developer","Back-End Developer","Courses","TypeScript","JS required","6/14"]),
   "Select Path career cards + course rows")
ck("design:v6:certificate", all(x in dt for x in ["Professional Certificate","22% Complete","2/9","path_overview_certificate_percent_complete"]),
   "certificate card from ARSC strings")
ck("design:v6:sections-from-code", all(x in dt for x in ["sectionRows","path_overview_section_ordinal","tutorialIds","Section Project","Coming soon"]),
   "numbered sections + tutorial ids rendered from shipped JSON")
ck("design:v6:no-max-tab", 'data-tab="MAX"' not in dt and "tabMap" in dt,
   "MAX tab forbidden; 5 tabs restored")
ck("design:v6:clean-learn", all(x in dt for x in ["1,272","ic_key","ic_infinity","overview-card","l10n1"]),
   "clean Learn: 3 pills + overview card + code-derived nodes")
lp = D / "LEARN_CODE_GEOMETRY.json"
ck("design:v6:learn-geometry", lp.is_file(), "LEARN_CODE_GEOMETRY.json present")
if lp.is_file():
    lg = json.loads(lp.read_text(encoding="utf-8"))
    ck("design:v6:learn-vectors", len(lg["vectors"]) >= 40 and all(v["paths"] for v in lg["vectors"].values()),
       "%d vectors with pathData" % len(lg["vectors"]))
    ck("design:v6:learn-strings", sum(len(v) for v in lg["strings"].values()) >= 140,
       "%d ARSC strings" % sum(len(v) for v in lg["strings"].values()))
    ck("design:v6:learn-layouts", len(lg["layouts"]) >= 15 and len(lg["navigation"]) >= 1,
       "%d AXML layouts / %d nav graphs" % (len(lg["layouts"]), len(lg["navigation"])))
    ck("design:v6:learn-content", len(lg["contentModel"]["sections"]) >= 15 and lg["contentModel"]["sections"][0]["tutorialIds"],
       "%d real sections with tutorialIds from test-tracks.json" % len(lg["contentModel"]["sections"]))
    ck("design:v6:learn-dex", sum(v["count"] for k,v in lg["dex"].items() if k != "literals") >= 250,
       "%d DEX classes" % sum(v["count"] for k,v in lg["dex"].items() if k != "literals"))
ck("design:v6:LEARN-payload", "var LEARN=" in dt and "LEARN.contentModel" in dt and "LEARN.counts" in dt,
   "sub-screens rendered from injected code payload")
lsub = ROOT / "CATALOGS/MIMO_LEARN_SUBSCREENS.csv"
ck("design:v6:sub-catalog", lsub.is_file() and len(rows(lsub)) - 1 == 868, "868 code-evidence rows")
ck("design:v6:build-bytes", len(dt) > 200000, "%d chars" % len(dt))

# ---- MAIN TASK: exact code-driven node geometry (v8) ----
ck("design:v10:nodes", all(x in dt for x in
   ["l10n1","l10n2","l10n3","l10n4","l10n5","l10n6","gloss-fab","hring",
    "M242 70 H280 Q312 70 312 102 V140","Q312 302 280 302","nodeGeometry","original_curved_zigzag"])
   and '<path d="M196 0 V620"' not in dt and "pathLineGrad" not in dt
   and 'class="gloss-fab"' not in dt and 'data-glossary="1"' not in dt
   and 'toast("واژهنامهٔ مبحث")' not in dt,
   "6 data-driven nodes, ORIGINAL curved zigzag restored, v9 straight line gone")
ck("design:v9:node-states", all(x in dt for x in
   ["node done","node cur","node next","node bolt active","node bolt optional","curInner",
    "ic_check_white","ic_square_rounded","ic_bolt_charged","ic_bolt_mastered"]),
   "linear states: done/done/current/next(unlocked)/charged bolt/mastered bolt")
ck("design:v8:no-locked-learn", not re.search(r'class="node locked|data-locked=|id="l8n\d+"[^>]*locked', dt)
   and 'class="sd-row locked' not in dt and 'node-start' not in dt,
   "ZERO locked Learn/section-detail nodes; START bubble removed")
ck("design:v8:one-lock-only", dt.count('data-icon="ic_lock_alt_02"') == 1
   and 'data-screen="exam-hub"' in dt,
   "exactly one lock: the pre-existing exam-hub biweekly/final exam card")
np_ = D / "NODE_CODE_GEOMETRY.json"
ck("design:v8:node-geometry", np_.is_file(), "NODE_CODE_GEOMETRY.json v8 present")
if np_.is_file():
    ng = json.loads(np_.read_text(encoding="utf-8"))
    ck("design:v8:node-vectors", len(ng["vectors"]) >= 55 and all(v["paths"] for v in ng["vectors"].values()),
       "%d vectors with pathData / %d misses" % (len(ng["vectors"]), ng["counts"]["vector_misses"]))
    ck("design:v8:node-strings", sum(len(v) for v in ng["strings"].values()) >= 85,
       "%d ARSC strings" % sum(len(v) for v in ng["strings"].values()))
    ck("design:v8:node-dex", ng["counts"]["pathmap_classes"] >= 90 and len(ng["dex"]["literals"]) >= 20,
       "%d PathMap DEX classes / %d literals" % (ng["counts"]["pathmap_classes"], len(ng["dex"]["literals"])))
    ck("design:v8:node-content", len(ng["contentModel"]["sections"]) >= 15
       and sum(s["tutorialCount"] for s in ng["contentModel"]["sections"]) >= 200,
       "%d sections / %d tutorialIds" % (len(ng["contentModel"]["sections"]),
                                         sum(s["tutorialCount"] for s in ng["contentModel"]["sections"])))
    geom = ng["nodeGeometry"]
    ck("design:v10:machine-geometry", geom["node"]["size_dp"] == 92 and geom["node"]["corner_radius_dp"] == 26
       and geom["node"]["lip_dp"] == 8 and geom["node"]["icon_dp"] == 48
       and geom["viewBox"] == [392, 720] and len(geom["nodes"]) == 6
       and len(geom["connector_paths"]) == 2
       and sum(p["d"].count("Q") for p in geom["connector_paths"]) == 5,
       "92dp/26dp/48dp + 392x720 + 6 nodes + 2 Q paths (5 rounded elbows)")
    L = geom["layout"]
    ck("design:v10:original-zigzag", L["mode"] == "original_curved_zigzag"
       and L["lanes"] == {"left": 80, "center": 196, "right": 312}
       and L["lane_sequence"] == ["center", "right", "center", "left", "center", "left"]
       and L["node_gap_dp"] == 24 and L["elbow_radius_dp"] == 32
       and L["curve"] is True and L["zigzag"] is True
       and L["one_continuous_connector"] is False
       and sorted({n["cx"] for n in geom["nodes"]}) == [80, 196, 312],
       "ORIGINAL 3-lane zigzag / 24dp gaps / 32dp Q elbows / no straight line")
    ck("design:v10:deep-code-review", geom["codeReview"]["pathmap_dex_classes"] == 92
       and geom["codeReview"]["track"]["section_count"] == 15
       and geom["codeReview"]["track"]["tutorial_id_count"] == 223
       and len(geom["codeReview"]["shapes"]) == 10
       and len(geom["codeReview"]["vectors_reviewed"]) == 10
       and "getFinishedStrokeColor()" in " ".join(geom["codeReview"]["arc_progress_methods"])
       and len(ng["code_fidelity"]["corrections_vs_v9"]) == 3,
       "92 PathMap DEX classes / 15 sections / 223 tutorialIds / ArcProgressView / 3 v9 reversions")
    ck("design:v10:no-misattribution", "lesson_progressbar_height" in geom["connector"]["stroke_source"]
       and "Glance widget" in geom["node"]["corner_source"]
       and geom["connector"]["stroke_dp"] == 10,
       "26dp corner & 10dp stroke restored; 16dp/6dp attributed to their real components")
    ck("design:v10:connector-segments", [p["role"] for p in geom["connector_paths"]] == ["done", "next"]
       and geom["connector_paths"][0]["color_token"] == "progress_chapter_primary"
       and geom["connector_paths"][1]["color_token"] == "progress_chapter_background",
       "two coloured connector segments split at the current node")
    ck("design:v8:states-removed", len(geom["states_removed"]) >= 4
       and "locked lesson" in geom["states_removed"][0],
       "locked/START/stray ring/debug chips listed as removed")
    ck("design:v8:lock-policy", "ZERO" in geom["lock_policy"] and len(ng["isolation"]) >= 4,
       "zero-lock policy + isolation contract")
    ck("design:v8:node-method", "CODE_FIRST" in ng["method"] and "VISUAL_CROSSCHECK_ONLY" in ng["method"],
       "code-first, screenshots cross-check only")
pcat = ROOT / "CATALOGS/MIMO_PATH_NODES.csv"
ck("design:v10:node-catalog", pcat.is_file() and len(rows(pcat)) - 1 == 106, "106 node code-evidence rows")
ck("design:v8:NODE-payload", "var NODE=" in dt and "NODE.nodeGeometry" in dt and "G.nodes.forEach" in dt,
   "prototype HTML rendered from the injected machine-readable geometry")

# ---- v8: routine & Habitica idea fully removed ----
ck("design:v8:no-routine-tab", 'data-tab="Routine"' not in dt and 'data-screen="routine"' not in dt
   and "var HAB=" not in dt and "HAB.constants" not in dt and "rtTasks" not in dt
   and dt.count('data-tab="') == 5,
   "tab/screen/payload removed from the prototype; 5 tabs only")
ck("design:v8:no-habitica-files", not (ROOT / "19_HABITICA_ROUTINE_SPEC.md").exists()
   and not (D / "HABITICA_SCORING.json").exists()
   and not (ROOT / "CATALOGS/HABITICA_SOURCES.csv").exists()
   and not (ROOT / "CATALOGS/HABITICA_SCORING.csv").exists()
   and not (ROOT / "tools/write_habitica_spec.py").exists(),
   "all Habitica / routine deliverable artifacts deleted")
ck("design:v8:no-dictate-in-ui", not re.search(r'<button[^>]*data-lh="Dictate"', dt)
   and "دیکته / Dictate" not in dt.split('<section class="screen konkur" data-screen="ai"')[1].split("</section>")[0],
   "Dictate button gone from AI composer")

# ---- v8: NO annotations inside the phone UI ----
ck("design:v8:no-policy-notes", all(x not in dt for x in
   ["زمان خالص آزمون</b> — حین آزمون", "تنها ایدهٔ جزیی گرفتهشده از EPM", "تایمر معکوس فقط داخل آزمون"])
   and 'q("#policyHint").innerHTML' not in dt
   and '<div class="hint" id="policyHint" hidden></div>' in dt,
   "the 3 quoted exam annotations removed; policyHint stays empty+hidden")
ui_vis = re.sub(r'<[^>]*\shidden\b[^>]*>', '', dt.split("</style>")[-1].split("<aside")[0])
note_texts = re.findall(r'<p class="note"[^>]*>(.*?)</p>', ui_vis, re.S)
banned_note = ["POLICY", "EPM", "ایدهٔ جزیی", "تایمر معکوس فقط", "زمان خالص آزمون",
               "DESIGN v", "ARSC", "pathData", "codechip", "data-screen"]
ck("design:v8:no-ui-annotations", all(x not in ui_vis for x in
   ['class="composer-note"', 'class="path-note"', 'class="sd-note"', 'class="hint"', 'class="lh"', 'codechip2'])
   and not re.search(r'\btitle="', dt)
   and len(note_texts) <= 3
   and all(w not in " ".join(note_texts) for w in banned_note),
   "no design/policy/EPM/timer/code annotations inside the phone UI (3 functional microcopy lines kept)")
ck("design:v8:inline-evidence", dt.count("data-code=") >= 15 and dt.count("data-lh=") >= 7,
   "evidence moved to invisible data-code / data-lh attributes")
ck("design:v8:exam-labels-kept", dt.count('class="cat-meta"') == 7
   and "قالب: تقویم ماه" in dt and "پاسخنامهٔ تشریحی" in dt and "تعویض سوال" in dt,
   "7 labelled exam sections + templates + descriptive answer text preserved")
ck("design:v8:exam-skin", all(x in dt for x in
   ["ic_trophy","ic_clock_black_24dp","ic_task_completed","ic_lock_alt_02","ic_file","ic_target","ic_sparks_alt","ic_arrow_back_24","ic_help"])
   and '--radius-card:' in dt and '--primary:' in dt and "var(--primary)" in dt
   and "border-radius:12px" in dt and "border-radius:16px" in dt,
   "real Mimo vectors + ARSC colours/radii/type; exam architecture untouched")
ck("design:v12:exam-architecture", all(x in dt for x in
   ["prevQ","nextQ","lk-cta","lk-square","result-foot","ic_arrow_left","ic_arrow_right","timerChip","answerSheetBtn","answerKeyBtn","exFeedback","QBANK","renderQuestion"])
   and "زمان ثابت ۲۷۰ دقیقه" in dt and "POLICY" in dt and "btn_continue_big" in dt,
   "single full-width CTA + one 48dp back square / answer sheets / 270 min / AI / question flow")
lb = re.search(r'<section class="screen mimo" data-screen="leaderboard".*?</section>', dt, re.S)
ck("design:v8:no-promo", bool(lb) and "Promotion Zone" not in lb.group(0) and "منطقهٔ صعود" not in lb.group(0) and 'class="promo"' not in lb.group(0),
   "Promotion Zone removed from leaderboard UI")
ck("design:v8:section-practice", all(x in dt for x in
   ['data-screen="section-practice"','data-scope="learn-practice"','practiceQuestions','practiceModal','practiceStart','Fully charged','Practice anyway'])
   and '>شارژ کامل!</button>' in dt and '>ساختار سلول و بافت</h2>' in dt and 'var P_FA=' in dt,
   "bolt nodes open an isolated Learn checkpoint quiz")
sp = re.search(r'<section class="screen mimo" data-screen="section-practice".*?</section>', dt, re.S)
ck("design:v8:practice-isolation", bool(sp) and all(x not in sp.group(0) for x in
   ["timerChip","پاسخبرگ","پاسخنامه","POLICY","270","exam-hub","توضیح با هوش مصنوعی"]),
   "section practice has NO exam controls / timer / answer sheets")
ck("design:v8:ai-header", all(x in dt for x in
   ["اضافه کردن فایل","زنجیره گفت و گو","attachment","ic_link_external","ai-top-left"]),
   "tidy AI top row: file icon + short label + conversation chain")
ck("design:v8:ai-footer", all(x in dt for x in
   ["ai-foot","data-mode=\"TEACH\"","data-mode=\"PRACTICE\"","flex-wrap:nowrap","gemini-flash-lite-latest","medium"])
   and ">آموزش</button>" in dt and ">تمرین</button>" in dt and ">مدل سریع " in dt
   and 'placeholder="دربارهٔ کدام مبحث' in dt,
   "TEACH/PRACTICE/model/medium on one tiny line, no Dictate")
ck("design:v8:build-bytes", len(dt) > 300000, "%d chars" % len(dt))

# ---- DESIGN v11: leaderboard / program tracks / topic courses ----
lbm = re.search(r'<section class="screen mimo" data-screen="leaderboard".*?</section>', dt, re.S)
lbb = lbm.group(0) if lbm else ""
ck("design:v11:leaderboard", bool(lbm) and ">وضعیت من</div>" in lbb and 'data-fa="وضعیت من"' in lbb
   and not re.search(r'>(?:My status|Day streak|XP total|Weekly XP|Comprehensive exam|Biology single-subject|Timed chemistry|Analytical / wrong answers)<', lbb)
   and "selfbox" in lbb and "آزمونها و امتیازات من" in lbb
   and all(x not in lbb for x in ["Wooden", "League", "6d 22h", "MIGUELBAOBAB", "mairi", "Aska", "sarah", "lucas", "lb-row", "league-row"]),
   "Wooden League + countdown + all 5 rival rows + league badges REMOVED; My status only")
ck("design:v11:headings", 'id="careerHeading" data-fa="یادگیری برنامه محور"' in dt
   and 'id="courseHeading" data-fa="یادگیری مبحثی"' in dt
   and ">یادگیری برنامه محور</h3>" in dt and ">یادگیری مبحثی</h3>" in dt,
   "Career Paths / Courses relabelled to program-based / topic-based learning")
ck("design:v11:cards-courses", "V11_CARDS" in dt and "V11_COURSES" in dt
   and "V11_CARDS.push" not in dt and 'data-v11="courses:' not in dt
   and all(x in dt for x in ["یادگیری همگام با برنامه آزمون دوازدهم",
                             "یادگیری همگام با برنامه آزمون یازدهم",
                             "یادگیری همگام با برنامه آزمون دهم"])
   and all(x in dt for x in ["زیست دهم", "ریاضی دهم", "شیمی دهم", "فیزیک دهم",
                             "زیست یازدهم", "ریاضی یازدهم", "شیمی یازدهم", "فیزیک یازدهم",
                             "زیست دوازدهم", "ریاضی دوازدهم", "شیمی دوازدهم", "فیزیک دوازدهم"]),
   "3 big program cards (duplicate topic card removed) + 12 subject x grade courses")
ck("design:v11:certificate", "مدرک پایان دوره" in dt and "۲۲ درصد کامل شده" in dt
   and "2/9" in dt and 'id="poKicker"' in dt and 'id="poTitle"' in dt,
   "certificate card relabelled; path overview is data-driven")
ck("design:v11:fortnight", all(x in dt for x in
   ["۱ آبان", "۱۵ آبان", "۱ آذر", "۱۵ آذر", "۱ دی", "۱۵ دی", "۱ بهمن", "۱۵ بهمن", "۱ اسفند", "۱۵ اسفند"])
   and "دروس: زیست، شیمی، ریاضی، فیزیک" in dt and '"lessons_label":"دروس"' in dt,
   "10 biweekly dates over 5 Persian months + «دروس» line with 4 subjects")
ck("design:v11:no-programming-icons", not re.search(r'data-icon="(ic_badge_|ic_code_lang_|ic_code_playground_template_)', dt)
   and "ic_cap_filled" in dt and "img_brain" in dt,
   "ZERO programming emblems/logos; decoded Mimo vectors used instead")
kp = D / "KONKUR_CURRICULUM.json"
ck("design:v11:curriculum-json", kp.is_file(), "KONKUR_CURRICULUM.json present")
if kp.is_file():
    k = json.loads(kp.read_text(encoding="utf-8"))
    ck("design:v11:curriculum-counts", k["round"] == "v11" and len(k["courses"]) == 12
       and k["chapter_count"] == 60 and k["lesson_count"] == 180
       and all(len(c["chapters"]) == 5 and all(ch["lessons"] for ch in c["chapters"]) for c in k["courses"]),
       "12 courses / 60 فصل / 180 درس with lesson names")
    ck("design:v11:curriculum-payload", "var KONKUR=" in dt and "KONKUR.courses" in dt,
       "prototype renders the machine-readable curriculum payload")
ck("design:v11:chapter-lessons", "v11RenderSection" in dt and "v11RenderOverview" in dt
   and "data-v11section" in dt and "فصل " in dt,
   "course overviews show فصل names + درس names, section detail shows real lessons")
ck("design:v11:geometry-unchanged", "M242 70 H280 Q312 70 312 102 V140" in dt
   and 'data-screen="exam-hub"' in dt and dt.count('data-tab="') == 5,
   "original curved zigzag + 5 tabs + exam architecture untouched")

# ---- DESIGN v12: exam surfaces on real Mimo lesson UI ----
erm = re.search(r'<section class="screen exv12" data-screen="exam-run".*?</section>', dt, re.S)
erb = erm.group(0) if erm else ""
ck("design:v12:code-evidence", (D / "EXAM_UI_CODE_EVIDENCE.json").is_file(), "EXAM_UI_CODE_EVIDENCE.json present")
ev = json.loads((D / "EXAM_UI_CODE_EVIDENCE.json").read_text(encoding="utf-8"))
ck("design:v12:evidence-layouts", ev["round"] == "v12" and all(k in ev["layouts"] for k in
   ["chapter_toolbar.xml", "lesson_interactive_multiplechoice_fragment.xml", "choice_list_item.xml",
    "interaction_keyboard_view.xml", "run_button_view.xml", "lesson_interactive_feedback_bottom_sheet_dialog.xml"]),
   "evidence lists every decoded layout used")
ck("design:v12:no-konkur-exam-skin", all('class="screen konkur" data-screen="'+n+'"' not in dt for n in
   ["exam-hub","exam-run","exam-result"]) and dt.count('class="screen exv12"') == 3,
   "the separate konkur skin is GONE from all 3 exam screens")
ck("design:v12:mimo-navbar", bool(erb) and all(x in erb for x in
   ["chapter_toolbar.xml","lesson_progress_navbar_height=52dp",'class="ln"','class="ln-x"',
    'data-icon="ic_close"','class="ln-prog"','id="examProgress"','id="timerWrap"','id="timerChip"']) and 'data-icon="ic_flag"' not in erb,
   "chapter_toolbar.xml: X | 6dp progress | ONE timer chip, no flag, 52dp")
ck("design:v12:choice-cards", bool(erb) and all(x in erb for x in
   ["lesson_interactive_multiplechoice_fragment.xml","rv_multiplechoice_options","choice_list_item.xml",
    "layout_choice_card_item.xml",'class="lb-choices"','class="opt-num"',
    "interaction_hint_single_choice"]) and 'class="opt-radio"' not in erb
   and "multiplechoice_background_selected.xml" in ev["drawables"],
   "ChoiceView + choice_list_item cards + TextInteractionHint")
ck("design:v12:feedback", bool(erb) and "lesson_interactive_feedback_bottom_sheet_dialog" in erb
   and 'id="exFeedback"' in erb and "multiplechoice_background_correct.xml" in ev["drawables"],
   "inline correct/wrong feedback panel from the real bottom-sheet layout")
ck("design:v12:single-cta", bool(erb) and all(x in erb for x in
   ["interaction_keyboard_view.xml","run_button_view.xml","btn_continue_big","btn_submit",
    "lesson_continue","lesson_skip",'class="lk-cta"','id="nextQ"','class="lk-square"','id="prevQ"','id="markQ"'])
   and all(x not in erb for x in ['class="qnav"',"سؤال قبل</button>","سؤال بعد</button>",'class="qfoot"']),
   "ONE full-width CTA + 48dp squares; the wrong equal prev/next pill pair is gone")
ck("design:v12:question-flow", all(x in dt for x in
   ["QBANK","renderQuestion","lesson_submit","lesson_skip","exFeedbackTitle","nextQLabel","examProgress"]),
   "select -> submit -> feedback -> continue -> next question")
ck("design:v12:hub-and-result", "quiz_introduction_fragment.xml" in dt and 'class="eh-hero"' in dt
   and "lesson_awesome_fragment.xml" in dt and 'class="rf-hero"' in dt
   and dt.count('class="cat-meta"') == 7 and 'data-icon="ic_lock_alt_02"' in dt,
   "Mimo quiz-intro hub rows + celebration result; 7 labelled sections + one lock kept")
ck("design:v12:contract-kept", dt.count('data-tab="') == 5 and 'data-tab="MAX"' not in dt
   and "زمان ثابت ۲۷۰ دقیقه" in dt and "M242 70 H280 Q312 70 312 102 V140" in dt
   and "askAiBtn" in dt and "askAiResultBtn" in dt and 'data-isolated="exam"' in dt,
   "5 tabs / no MAX / 270 min / curved zigzag / one AI button / isolated practice")
ck("design:v12:rollback", (ROOT / "tools/design_v11_full.html").is_file()
   and "V11_ROLLBACK_SNAPSHOT_V12" in (ROOT / "CATALOGS/SCOPE_DECISIONS.csv").read_text(encoding="utf-8"),
   "v11.1 snapshot kept as an explicit rollback path")

# ---- DESIGN v12.1: bug-fix pass over the v12 exam code ----
ck("design:v12.1:scroll", '.exv12[data-screen="exam-run"]{overflow:hidden}' in dt
   and ".exv12{direction:rtl;background:var(--bg);display:none;flex-direction:column;overflow:auto;padding:0}" in dt
   and ".exv12 .lb-body{flex:1;min-height:0;overflow:auto" in dt,
   "exam-hub / exam-result scroll as a whole; only exam-run keeps the pinned footer")
ck("design:v12.1:row-click", all(x in dt for x in
   ["function openExam(n)","QI=0;MARKS={}","var ehRows=qa('[data-screen=\"exam-hub\"] .grid3 > div')",
    'row.setAttribute("role","button")','e.key==="Enter"']),
   "the whole Mimo list row is clickable + keyboard activated; index resets per exam")
ck("design:v12.1:filters", dt.count('data-filter="') == 8 and "ehGroups" in dt
   and 'data-filter="all"' in dt and 'data-filter="5,6"' in dt,
   "8 filter chips wired to the 7 labelled sections")
ck("design:v12.1:qbank", "var QTOTAL=QBANK.length,QI=0,QCHECKED=false,MARKS={};" in dt
   and dt.count('\n    ["') == 20 and "var i=1;i<=20;i++" in dt
   and 'q("#examStep").textContent="سؤال "+fa(QI+1)+" از "+fa(QTOTAL)' in dt,
   "20 distinct questions + one QTOTAL + palette of 20 (no more hardcoded 3-of-20)")
ck("design:v12.1:ai-dynamic", 'setCtx("زمینه: "+q("#examTitle").textContent+" · سؤال "+fa(QI+1)+"' in dt,
   "AI context uses the live question number instead of a hardcoded «سؤال ۳»")
ck("design:v12.1:rtl", 'qa(".mimo,.exv12",ph)' in dt
   and 'T.state==="setting"' in dt and dt.count('ctl.hidden=true') >= 2,
   "RTL toggle covers exam screens; the single timer chip resets in setting state")
ck("design:v12.1:row-meta", 'className="row-meta"' in dt and ".exv12 .label .row-meta" in dt
   and ".exv12 .nodek .mini" not in dt,
   "hidden .mini badges moved into the row label as Mimo subtitles")
ck("design:v12.1:evidence", "bugfixes_v12_1" in ev and len(ev["bugfixes_v12_1"]) == 7,
   "7 code bugs documented in EXAM_UI_CODE_EVIDENCE.json")
ck("design:v12.1:no-regression", 'class="qnav"' not in dt and dt.count('class="cat-meta"') == 7
   and "M242 70 H280 Q312 70 312 102 V140" in dt and dt.count('data-tab="') == 5
   and "زمان ثابت ۲۷۰ دقیقه" in dt and dt.count('data-icon="ic_lock_alt_02"') == 1,
   "bug fixes did not touch the accepted v11.1 / v12 contract")
ck("docs:v12.1:log", "v12.1" in (ROOT / "24_DESIGN_ROUND_12.md").read_text(encoding="utf-8")
   and "B1" in (ROOT / "24_DESIGN_ROUND_12.md").read_text(encoding="utf-8"),
   "round-12 log documents every bug fix")
ck("scope:v12.1:catalogs", "F-66" in (ROOT / "CATALOGS/DESIGN_FEEDBACK.csv").read_text(encoding="utf-8")
   and "D46" in (ROOT / "CATALOGS/SCOPE_DECISIONS.csv").read_text(encoding="utf-8")
   and "F42" in (ROOT / "CATALOGS/UI_FIDELITY_RULES.csv").read_text(encoding="utf-8"),
   "bug-fix round recorded in feedback / decisions / fidelity rules")
man121 = json.loads((ROOT / "MANIFEST.json").read_text(encoding="utf-8"))
ck("manifest:v12.1", "v12.1" in man121["status"] and any("fix_design_v12_1.py" in c for c in man121["reproduce"]),
   "MANIFEST advertises the v12.1 fix pass + reproduce command")

# ---- DESIGN v12.3: reject the four-model pass, roll back, fix RTL arrows ----
ref123 = json.loads((D / "EXAM_PAGE_REFERENCES.json").read_text(encoding="utf-8"))
geo123 = json.loads(re.search(r"<script>var GEO=(.*?);</script>", dt, re.S).group(1))
eh123 = re.search(r'<section class="screen exv12" data-screen="exam-hub".*?</section>', dt, re.S).group(0)
er123 = re.search(r'<section class="screen exv12" data-screen="exam-result".*?</section>', dt, re.S).group(0)
ck("design:v12.3:rollback", all(x not in dt for x in
   ['id="ksStrip"', 'class="mf" data-exmodel=', 'class="modelpick"', "EXAM_PAGE_MODELS", "submitA"])
   and dt.count('class="lk-cta"') == 1 and dt.count('class="lk-square"') == 2
   and 'class="sheet" id="paletteSheet"' in dt and 'class="sheet" id="keySheet"' in dt
   and "id=\"answerSheetBtn\"" in dt and "id=\"answerKeyBtn\"" in dt,
   "v12.2 four models removed; answer sheet / key are bottom sheets again")
ck("design:v12.3:rtl-arrows", 'data-icon="ic_arrow_left" data-arrow="next"' in dt
   and 'data-icon="ic_arrow_right" data-arrow="prev"' in dt
   and 'data-icon="ic_arrow_right" data-arrow="back"' in dt
   and '[dir="rtl"] [data-icon^="ic_arrow_"]:not([data-arrow]) svg{transform:scaleX(-1)}' in dt
   and '[dir="ltr"] [data-arrow] svg{transform:scaleX(-1)}' in dt,
   "NEXT arrowhead LEFT / PREVIOUS + BACK arrowhead RIGHT in RTL")
ck("design:v12.3:emblem", 'data-icon="ic_survey"' in eh123 and 'data-icon="ic_cap"' in er123
   and 'data-icon="ic_mimo_mascot"' not in eh123 and 'data-icon="ic_mimo_mascot"' not in er123
   and len(geo123["vectors"].get("ic_survey", {}).get("paths", [])) >= 20,
   "Mimo mascot replaced by ic_survey / ic_cap as requested")
ck("design:v12.3:references", ref123["round"] == "v12.3"
   and "mindskip/xzs" in json.dumps(ref123, ensure_ascii=False)
   and "do.vue" in json.dumps(ref123, ensure_ascii=False)
   and len(ref123["rtl_arrow_rule"]["sources"]) >= 3
   and ref123["reference_of_record"]["commit"] == "d356963",
   "RTL web sources + Chinese exam repo do.vue cross-check recorded")
ck("docs:v12.3:log", "v12.3" in (ROOT / "24_DESIGN_ROUND_12.md").read_text(encoding="utf-8")
   and "برگردانده" in (ROOT / "24_DESIGN_ROUND_12.md").read_text(encoding="utf-8"),
   "round-12 log documents the rejection + rollback")
ck("scope:v12.3:catalogs", "F-68" in (ROOT / "CATALOGS/DESIGN_FEEDBACK.csv").read_text(encoding="utf-8")
   and "D48" in (ROOT / "CATALOGS/SCOPE_DECISIONS.csv").read_text(encoding="utf-8")
   and "F44" in (ROOT / "CATALOGS/UI_FIDELITY_RULES.csv").read_text(encoding="utf-8"),
   "rollback round recorded in feedback / decisions / fidelity rules")
man123 = json.loads((ROOT / "MANIFEST.json").read_text(encoding="utf-8"))
ck("manifest:v12.3", "v12.3" in man123["status"]
   and any("build_exam_v12_3.py" in c for c in man123["reproduce"])
   and "EXAM_PAGE_REFERENCES.json" in man123["deliverables"].get("v12_exam_ui", ""),
   "MANIFEST advertises v12.3 + its reproduce command")

# ---- DESIGN v12.4: remove the extra exam buttons / ONE timer chip ----
# v12.5 correction: «توضیح با هوش مصنوعی» is back as the THIRD quiet chip, exactly
# where / how it was in v12.1 & v12.3, beside پاسخبرگ / پاسخنامه.
ck("design:v12.5:chip-row-restored", bool(erb) and dt.count('class="lb-chip"') == 3
   and all(x in erb for x in ['id="answerSheetBtn"', 'id="answerKeyBtn"', 'id="askAiBtn"'])
   and erb.index('id="answerSheetBtn"') < erb.index('id="answerKeyBtn"') < erb.index('id="askAiBtn"')
   and 'data-icon="ic_magic_wand" data-size="16" data-mono="1"' in erb
   and all(x not in erb for x in ['id="endExam"', 'id="skipQ"', 'id="timerStateText"',
                                  'class="ln-report"', 'class="lk-skip"'])
   and 'data-sheet="exitSheet"' not in erb.split('class="lb-tools"')[1].split('</div>')[0],
   "THREE quiet chips in the v12.1 order: پاسخبرگ / پاسخنامه / توضیح با هوش مصنوعی")
ck("design:v12.4:one-timer-chip", bool(erb) and all(x in erb for x in
   ['id="timerWrap"', 'id="timerControls"', 'id="timerPause"', 'id="timerReset"',
    'class="tm-bars"', 'class="tm-play"', 'class="tm-square"'])
   and "pauseOrResume" in dt and 'if(T.state==="running"||T.state==="paused"){pauseOrResume();return}' in dt,
   "ONE timer chip: tap to set / pause / resume + inline play/pause & stop next to the countdown")
ck("design:v12.4:no-radio", 'opt-radio' not in dt
   and dt.count('<span class="opt-num">') == 4
   and '.opt.on .opt-num{color:var(--primary)}' in dt,
   "option starts with its number; the whole card changes colour, no radio circle")
ks = dt.split('<div class="sheet" id="keySheet"')[1].split('<div class="sheet" id="exitSheet"')[0]
ck("design:v12.5:ai-restored-body", dt.count('id="askAiBtn"') == 1
   and dt.index('class="lb-tools"') < dt.index('id="askAiBtn"') < dt.index('<div class="sheet" id="keySheet"')
   and 'askAiBtn' not in ks and 'id="askAiResultBtn"' in dt,
   "AI chip restored in the exam body; the v12.4 duplicate inside #keySheet is removed")
ck("design:v12.4:no-duplicate-timer-text", "timerStateText" not in dt
   and erb.count('تنظیم زمان') >= 1 and dt.count('id="timerLabel"') == 1,
   "the timer label appears once; no «زمان تنظیم نشده» duplicate")
ck("docs:v12.4:log", "v12.4" in (ROOT / "24_DESIGN_ROUND_12.md").read_text(encoding="utf-8")
   and "تکدکمهای" in (ROOT / "24_DESIGN_ROUND_12.md").read_text(encoding="utf-8"),
   "round-12 log documents the button cleanup")
ck("scope:v12.4:catalogs", "F-69" in (ROOT / "CATALOGS/DESIGN_FEEDBACK.csv").read_text(encoding="utf-8")
   and "D49" in (ROOT / "CATALOGS/SCOPE_DECISIONS.csv").read_text(encoding="utf-8")
   and "F45" in (ROOT / "CATALOGS/UI_FIDELITY_RULES.csv").read_text(encoding="utf-8"),
   "button-cleanup round recorded in feedback / decisions / fidelity rules")
man124 = json.loads((ROOT / "MANIFEST.json").read_text(encoding="utf-8"))
ck("manifest:v12.4", "v12.4" in man124["status"]
   and any("build_exam_v12_4.py" in c for c in man124["reproduce"])
   and "v12.4" in json.dumps(man124.get("design_round_12", {}), ensure_ascii=False),
   "MANIFEST advertises v12.4 + its reproduce command")


# ---- DESIGN v12.5: editable minutes for ALL exams / three exit options / partial کارنامه ----
ck("design:v12.5:timer-manual", 'readOnly=true' not in dt and 'غیرقابل تغییر' not in dt
   and 'id="timerMinutes"' in dt and 'id="timerHint"' in dt
   and not re.search(r'id="timerMinutes"[^>]*\smax=', dt)
   and 'fld.removeAttribute("readonly")' in dt
   and 'q("#timerMinutes").value=EXAM_KIND==="comprehensive"?270:30' in dt
   and 'قابل تغییر' in dt,
   "#timerMinutes is editable in EVERY exam kind; 270 is only a preset, never a lock")
ck("design:v12.5:timer-presets", all('data-min="%d"' % m in dt for m in [15, 30, 45, 60, 90, 120])
   and 'm<1||m>300' not in dt,
   "the six quick presets ۱۵/۳۰/۴۵/۶۰/۹۰/۱۲۰ stay; the 300-minute ceiling is gone")
ck("design:v12.5:timer-3digit", 'm>=100?String(m):("0"+m).slice(-2)' in dt,
   "270 minutes renders as ۲۷۰:۰۰, not ۷۰:۰۰")
ex = dt.split('<div class="sheet" id="exitSheet"')[1].split('<div class="sheet" id="historySheet"')[0]
ck("design:v12.5:exit-three", ex.count('<button') == 3
   and all(x in ex for x in ['id="exitSaveBtn"', 'id="exitFinishBtn"', 'خروج و ذخیره',
                             'ادامهٔ آزمون', 'پایان آزمون و دیدن کارنامه', 'خروج و دیدن درصد'])
   and dt.count('<p class="note"') == 3,
   "#exitSheet has THREE options; no new .note annotation (still only 3 microcopy lines)")
ck("design:v12.5:save-resume", all(x in dt for x in
   ['var ANSWERS={},CHECKED={},SAVED=null;', 'function saveExam()', 'function resumeExam()',
    'id="resumeBar"', 'id="resumeBtn"', 'id="resumeText"', 'if(SAVED&&SAVED.exam===n.dataset.exam)'])
   and 'SAVED={exam:' in dt,
   "«خروج و ذخیره» really snapshots QI / answers / marks / timer and can be resumed later")
ck("design:v12.5:partial-report", all(x in dt for x in
   ['function score()', 'function renderReport(partial)', 'id="resPartial"', 'id="resPct"',
    'renderReport(!!partial)', 'finishExam("پایان آزمون و دیدن کارنامه",true)',
    'q("#resRank").textContent="—"']),
   "the third exit option computes a partial درصد from answered-so-far; a full finish restores the whole کارنامه")
ck("design:v12.5:no-stale-v12.4-text", all(x not in dt for x in
   ['comprehensive fixed 270 min', 'AI via پاسخنامه', 'timerFixedHint', 'قالب ثابت:'])
   and 'v12.5' in dt,
   "stale v12.4 labels/hints (fixed 270, relocated AI, 270 دقیقهٔ ثابت) are superseded")
ck("docs:v12.5:log", "v12.5" in (ROOT / "24_DESIGN_ROUND_12.md").read_text(encoding="utf-8")
   and "v12.5" in (D / "DESIGN_NOTES.fa.md").read_text(encoding="utf-8")
   and "DESIGN v12.5" in (ROOT / "wireframes.html").read_text(encoding="utf-8")
   and "v12.5-fa-localization" in (ROOT / "24_DESIGN_ROUND_12.md").read_text(encoding="utf-8")
   and "v12.5-fa-localization" in (D / "DESIGN_NOTES.fa.md").read_text(encoding="utf-8"),
   "round-12 §10 + design notes §10 + wireframes link document the v12.5 corrections")
ck("scope:v12.5:catalogs", "F-70" in (ROOT / "CATALOGS/DESIGN_FEEDBACK.csv").read_text(encoding="utf-8")
   and "D50" in (ROOT / "CATALOGS/SCOPE_DECISIONS.csv").read_text(encoding="utf-8")
   and "F46" in (ROOT / "CATALOGS/UI_FIDELITY_RULES.csv").read_text(encoding="utf-8")
   and "F-71" in (ROOT / "CATALOGS/DESIGN_FEEDBACK.csv").read_text(encoding="utf-8")
   and "D51" in (ROOT / "CATALOGS/SCOPE_DECISIONS.csv").read_text(encoding="utf-8")
   and "F47" in (ROOT / "CATALOGS/UI_FIDELITY_RULES.csv").read_text(encoding="utf-8"),
   "v12.5 correction round recorded in feedback / decisions / fidelity rules")
man125 = json.loads((ROOT / "MANIFEST.json").read_text(encoding="utf-8"))
ck("manifest:v12.5", "v12.5" in man125["status"]
   and any("build_exam_v12_5.py" in c for c in man125["reproduce"])
   and "v12_5_corrections" in man125["design_round_12"]
   and "v12_5_localization" in man125["design_round_12"]
   and any("localize_v12_5_fa.py" in c for c in man125["reproduce"]),
   "MANIFEST advertises v12.5 + its reproduce command + the correction record")

# ---- docs / catalogs ----
ck("docs:v10:22", "DESIGN v10" in (ROOT / "22_DESIGN_ROUND_10.md").read_text(encoding="utf-8")
   and "Q312 70" in (ROOT / "22_DESIGN_ROUND_10.md").read_text(encoding="utf-8"),
   "v10 final log + original curved geometry")
ck("docs:v9:21", "DESIGN v9" in (ROOT / "21_DESIGN_ROUND_9.md").read_text(encoding="utf-8"), "v9 log archived / retracted")
ck("docs:v8:20", "DESIGN v8" in (ROOT / "20_DESIGN_ROUND_8.md").read_text(encoding="utf-8"), "v8 log archived")
ck("docs:v10:notes", "DESIGN v10" in (D / "DESIGN_NOTES.fa.md").read_text(encoding="utf-8")
   and "NODE_CODE_GEOMETRY.json" in (D / "DESIGN_NOTES.fa.md").read_text(encoding="utf-8"), "v10 design notes")
ck("docs:v10:banners", sum("<!-- v10-banner -->" in (ROOT / d).read_text(encoding="utf-8") for d in docs if d.endswith(".md")) >= 21,
   "archived docs carry v10 superseded banner")
ck("docs:v11:23", "DESIGN v11" in (ROOT / "23_DESIGN_ROUND_11.md").read_text(encoding="utf-8")
   and "KONKUR_CURRICULUM" in (ROOT / "23_DESIGN_ROUND_11.md").read_text(encoding="utf-8"),
   "v11 final log + curriculum evidence")
ck("docs:v11:notes", "DESIGN v11" in (D / "DESIGN_NOTES.fa.md").read_text(encoding="utf-8")
   and "KONKUR_CURRICULUM.json" in (D / "DESIGN_NOTES.fa.md").read_text(encoding="utf-8"), "v11 design notes")
ck("docs:v11:banners", sum("<!-- v11-banner -->" in (ROOT / d).read_text(encoding="utf-8") for d in docs if d.endswith(".md")) >= 22,
   "archived docs carry v11 superseded banner")
ck("docs:v12:24", "DESIGN v12" in (ROOT / "24_DESIGN_ROUND_12.md").read_text(encoding="utf-8")
   and "interaction_keyboard_view.xml" in (ROOT / "24_DESIGN_ROUND_12.md").read_text(encoding="utf-8"),
   "v12 final log + decoded-layout evidence")
ck("docs:v12:notes", "DESIGN v12" in (D / "DESIGN_NOTES.fa.md").read_text(encoding="utf-8")
   and "EXAM_UI_CODE_EVIDENCE.json" in (D / "DESIGN_NOTES.fa.md").read_text(encoding="utf-8"), "v12 design notes")
ck("docs:v12:banners", sum("<!-- v12-banner -->" in (ROOT / d).read_text(encoding="utf-8") for d in docs if d.endswith(".md")) >= 23,
   "archived docs carry v12 superseded banner")
ck("docs:v7:18", "DESIGN v7" in (ROOT / "18_DESIGN_ROUND_7.md").read_text(encoding="utf-8"), "v7 log archived")
ck("scope:v8", all(x in (ROOT / "CATALOGS/SCOPE_DECISIONS.csv").read_text(encoding="utf-8") for x in
   ["REMOVED_ENTIRELY_V8","FIVE_TABS_RESTORED","DICTATE_REMOVED","NO_ANNOTATIONS_IN_UI","ONE_LOCK_ONLY","NODE_CODE_FIRST_V8"]),
   "all 6 round-8 decisions recorded")
ck("scope:feedback-v8", all(x in (ROOT / "CATALOGS/DESIGN_FEEDBACK.csv").read_text(encoding="utf-8") for x in
   ["F-45","F-46","F-47","F-48","F-49","F-50","F-51","F-52"]),
   "all 8 round-8 corrections recorded")
ck("scope:v9", all(x in (ROOT / "CATALOGS/SCOPE_DECISIONS.csv").read_text(encoding="utf-8") for x in
   ["SINGLE_VERTICAL_LINE_NO_CURVES","RECODED_FROM_DIMEN_XML","LINEAR_STATES_REAL_VECTORS"])
   and all(x in (ROOT / "CATALOGS/DESIGN_FEEDBACK.csv").read_text(encoding="utf-8") for x in
   ["F-53","F-54","F-55"]),
   "all 3 round-9 decisions + 3 round-9 corrections recorded")
ck("scope:v12", all(x in (ROOT / "CATALOGS/SCOPE_DECISIONS.csv").read_text(encoding="utf-8") for x in
   ["EXAM_SURFACES_CODE_FIRST_V12","SINGLE_FULLWIDTH_CTA_V12","V11_ROLLBACK_SNAPSHOT_V12"])
   and all(x in (ROOT / "CATALOGS/DESIGN_FEEDBACK.csv").read_text(encoding="utf-8") for x in
   ["F-63","F-64","F-65"]) and "U13" in (ROOT / "CATALOGS/OPEN_QUESTIONS.csv").read_text(encoding="utf-8"),
   "3 round-12 decisions + 3 corrections + rollback question recorded")
ck("scope:v11", all(x in (ROOT / "CATALOGS/SCOPE_DECISIONS.csv").read_text(encoding="utf-8") for x in
   ["MY_STATUS_ONLY_V11","PROGRAM_AND_TOPIC_TRACKS_V11","NO_PROGRAMMING_EMBLEMS_V11","THREE_CARDS_ONLY_V11"])
   and all(x in (ROOT / "CATALOGS/DESIGN_FEEDBACK.csv").read_text(encoding="utf-8") for x in
   ["F-59","F-60","F-61","F-62"]) and "U12" in (ROOT / "CATALOGS/OPEN_QUESTIONS.csv").read_text(encoding="utf-8"),
   "all 3 round-11 decisions + 3 corrections + curriculum assumption recorded")
ck("scope:v10", all(x in (ROOT / "CATALOGS/SCOPE_DECISIONS.csv").read_text(encoding="utf-8") for x in
   ["ORIGINAL_CURVED_ZIGZAG_RESTORED","NUMBERS_REATTRIBUTED","DEEP_CODE_REVIEW_V10"])
   and all(x in (ROOT / "CATALOGS/DESIGN_FEEDBACK.csv").read_text(encoding="utf-8") for x in
   ["F-56","F-57","F-58"]),
   "all 3 round-10 decisions + 3 round-10 corrections recorded")
pv = ROOT / "CATALOGS/PRACTICE_VS_EXAM.csv"
ck("csv:practice-vs-exam", pv.is_file() and len(rows(pv)) - 1 == 12
   and "learn_bolt_practice" in pv.read_text(encoding="utf-8")
   and "konkur_exam" in pv.read_text(encoding="utf-8"),
   "12-row two-way isolation table, no routine column")

# ---- docs cross-references ----
ck("docs:v6:17", "DESIGN v6" in (ROOT / "17_DESIGN_ROUND_6.md").read_text(encoding="utf-8"), "v6 log archived")
ck("docs:v6:notes", "DESIGN v6" in (D / "DESIGN_NOTES.fa.md").read_text(encoding="utf-8"), "v6 archive line in notes")
ck("docs:v5:16", "DESIGN v5" in (ROOT / "16_DESIGN_ROUND_5.md").read_text(encoding="utf-8"), "v5 log archived")
ck("docs:v4:15", "طرح نهایی" in (ROOT / "15_DESIGN_ROUND_4.md").read_text(encoding="utf-8"), "v4 final log (archived)")
ck("docs:v4:02", "حکم محصول ۵ تب" in (ROOT / "02_UI_FIDELITY_CONTRACT.md").read_text(encoding="utf-8"), "5-tab override (archived, MAX-specific)")
ck("docs:v4:08", "۵ تب" in (ROOT / "08_NAVIGATION_AND_IA.md").read_text(encoding="utf-8"), "5-tab IA (archived)")
ck("docs:v4:03", "سیاست بر اساس نوع آزمون" in (ROOT / "03_EXAM_HUB.md").read_text(encoding="utf-8"), "answer sheet policy")
ck("docs:v4:04", "دکمههای LH در چت مینیمال" in (ROOT / "04_AI_LEARN_HARNESS.md").read_text(encoding="utf-8"), "LH buttons in chat")
ck("scope:5tabs", "FIVE_TABS" in (ROOT / "CATALOGS/SCOPE_DECISIONS.csv").read_text(encoding="utf-8"), "restored 5-tab decision")
ck("scope:code-first", "CODE_FIRST" in (ROOT / "CATALOGS/SCOPE_DECISIONS.csv").read_text(encoding="utf-8"), "code-first decision")
ck("csv:exam-policy", "answer_sheet_policy" in (ROOT / "CATALOGS/EXAM_TYPES.csv").read_text(encoding="utf-8"), "policy column")
ck("docs:v3:14", "تصمیمات دامنهای" in (ROOT / "14_DESIGN_ROUND_3.md").read_text(encoding="utf-8"), "v3 log")
ck("docs:v3:04", "پنل مینیمال v3" in (ROOT / "04_AI_LEARN_HARNESS.md").read_text(encoding="utf-8"), "minimal AI spec")
ck("docs:v3:05", "PARKED" in (ROOT / "05_COUNSELING_HADAF_PLUS.md").read_text(encoding="utf-8"), "counseling parked")
ck("scope:parked", "PARKED" in (ROOT / "CATALOGS/SCOPE_DECISIONS.csv").read_text(encoding="utf-8"), "scope decisions")
for f,mark in [("03_EXAM_HUB.md","فقط داخل آزمون"),
               ("04_AI_LEARN_HARNESS.md","جاسازی کنترلهای واقعی LH"),
               ("05_COUNSELING_HADAF_PLUS.md","برنامهریز هفتگی قابلاستفاده")]:
    ck("docs:v2:" + f, mark in (ROOT / f).read_text(encoding="utf-8"), mark)

# extracted source apps
for slug, sha, entries in [("hamdars", "9e362f08670174a3e8a3b319b5a2f687da8ecf7896ea78ea2ec70b95dd817be3", 1363),
                           ("hadaf_plus", "b282f578b255fecc4b72ee74f2ce79eb5bbcde35f3515690342b7fa37a5bbf43", 1516)]:
    m = json.loads((ROOT / "SOURCE_APPS" / slug / "META.json").read_text(encoding="utf-8"))
    ck("apk:" + slug + ":sha", m["sha256"] == sha, m["sha256"][:16])
    ck("apk:" + slug + ":census", len(rows(ROOT / "SOURCE_APPS" / slug / "APK_CENSUS.csv")) - 1 == entries,
       str(m["zip_entries"]))
    ck("apk:" + slug + ":dart", (ROOT / "SOURCE_APPS" / slug / "dart" / "STRINGS_ALL.txt").is_file(),
       "Dart snapshot strings")
    ck("apk:" + slug + ":persian", (ROOT / "SOURCE_APPS" / slug / "dart" / "PERSIAN_UTF16.txt").is_file(),
       "UTF-16LE Persian strings")
ck("helpcenter:ux-doc", "start-home" in (ROOT / "SOURCE_APPS/hamdars/HELP_CENTER_UX.md").read_text(encoding="utf-8"),
   "33 lessons / 149 steps")
ck("hadaf:7templates", len(rows(ROOT / "CATALOGS/HADAF_TEMPLATES.csv")) - 1 == 7, "7 ready-made plans")

# craft-anything install
ca = ROOT / "CRAFT_ANYTHING"
ck("craft:adapter", (ca / "craft_adapter.py").is_file(), "agent-facing CLI")
ck("craft:upstream-docs", (ca / "upstream_docs/tools.md").is_file() and len(list((ca / "upstream_docs/schemas").glob("*.json"))) >= 4,
   "vendored docs + schemas")
ck("craft:workspace", all((ca / "workspace" / f).is_file() for f in
                          ["craft.json", "investigation.cany.json", "plan.json", "unknowns.json", "brief.md"]),
   "5 workspace files")
led = json.loads((ROOT / "CATALOGS/EVIDENCE_LEDGER.json").read_text(encoding="utf-8"))
ck("craft:evidence", led["count"] == 13, str(led["count"]) + " records")
ck("craft:phases", len(json.loads((ca / "workspace/plan.json").read_text(encoding="utf-8"))) == 8, "8 planned phases")

# MANIFEST coherence
man = json.loads((ROOT / "MANIFEST.json").read_text(encoding="utf-8"))
ck("manifest:v12", "DESIGN v12" in man["status"] and man["deliverables"]["design_round"].startswith("v12")
   and man["deliverables"]["design_views"] == 14 and man["deliverables"]["csv_catalogs"] == 21
   and man["deliverables"]["persian_docs"] == 25 and "design_round_12" in man
   and man["design_round_11"]["status"].startswith("DESIGN v11 · SUPERSEDED")
   and man["design_round_12"]["button_correction"]["after"].startswith("single full-width purple CTA")
   and man["design_round_12"]["rollback"].startswith("tools/design_v11_full.html"),
   "MANIFEST advertises v12: 14 views / 21 CSVs / 25 docs / single CTA / rollback snapshot")
# +3 = this check itself + docs:no-cjk + sums (the three checks after this point)
EXPECTED_CHECKS = len(checks) + 3
ck("manifest:checks", man["deliverables"]["verification_checks"] == EXPECTED_CHECKS,
   "verification_checks=%d expected %d" % (man["deliverables"]["verification_checks"], EXPECTED_CHECKS))

# no CJK contamination in generated Persian docs
cjk = re.compile(r"[\u4e00-\u9fff\u3040-\u30ff\u3400-\u4dbf]")
bad = []
for p in sorted(ROOT.rglob("*")):
    if p.is_file() and p.suffix in {".md", ".csv", ".html"} and "upstream_docs" not in str(p):
        if cjk.search(p.read_text(encoding="utf-8", errors="ignore")):
            bad.append(str(p.relative_to(ROOT)))
ck("docs:no-cjk", not bad, ", ".join(bad))

# SHA256SUMS for every deliverable (excluding the sums file itself)
files = sorted(p for p in ROOT.rglob("*") if p.is_file() and p.name != "SHA256SUMS.txt")
lines = []
for p in files:
    h = hashlib.sha256(p.read_bytes()).hexdigest()
    lines.append("%s  %s" % (h, p.relative_to(ROOT).as_posix()))
(ROOT / "CATALOGS/SHA256SUMS.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")
ck("sums", True, "%d files hashed" % len(files))

verdict = "PASS" if not problems else "FAIL"
report = {"verdict": verdict, "checks": len(checks), "passed": sum(1 for c in checks if c["status"] == "PASS"),
          "failed": problems, "details": checks, "files_hashed": len(files)}
(ROOT / "CATALOGS/VERIFICATION_REPORT.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({"verdict": verdict, "checks": len(checks), "passed": report["passed"],
                  "failed": problems, "files_hashed": len(files)}, ensure_ascii=False, indent=2))
sys.exit(0 if verdict == "PASS" else 1)
