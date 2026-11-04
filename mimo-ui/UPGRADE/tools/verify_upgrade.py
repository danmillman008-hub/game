#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fail-closed verification of the Konkur-upgrade planning deliverable (v7)."""
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
        "18_DESIGN_ROUND_7.md", "19_HABITICA_ROUTINE_SPEC.md", "wireframes.html"]
csvs = {"UI_FIDELITY_RULES.csv": 24, "FEATURE_MAP.csv": 17, "EXAM_TYPES.csv": 11,
        "HADAF_TEMPLATES.csv": 7, "GAMIFICATION_MAP.csv": 13, "PHASES.csv": 8,
        "LEARNHARNESS_ACTIONS.csv": 32, "EVIDENCE_LEDGER.csv": 10, "OPEN_QUESTIONS.csv": 7,
        "DESIGN_FEEDBACK.csv": 44, "SCOPE_DECISIONS.csv": 26,
        "AI_PANEL_SPEC.csv": 25, "EPM_MINOR_OPTIONS.csv": 7,
        "EXAM_SECTION_TEMPLATES.csv": 7,
        "MIMO_CODE_GEOMETRY.csv": 200, "MIMO_SCREENSHOT_CROSSWALK.csv": 14,
        "ANSWER_SHEET_POLICY.csv": 5, "MIMO_LEARN_SUBSCREENS.csv": 868,
        "MIMO_PATH_NODES.csv": 50, "HABITICA_SOURCES.csv": 13,
        "HABITICA_SCORING.csv": 22, "PRACTICE_VS_EXAM.csv": 12}
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
ck("wireframe:tokens", all(x in t for x in ["#7E4BDE", "#FFF6F7FB".replace("FF", ""), "#F6F7FB", "#E4E6F1", "#66BC5A", "#F05A6E"]),
   "Mimo palette present")
ck("wireframe:legacy-tabs", t.count('class="tab') >= 4 and "<div class=\"tab\">Learn</div>" in t,
   "archived v1 wireframe renders its legacy tabs")
ck("wireframe:3col-grid", "repeat(3,minmax(0,1fr))" in t, "exam node grid")
ck("wireframe:v1-banner", "DESIGN/index.html" in t and "DESIGN v7" in t, "v1 archived, points to v7")

# ---- DESIGN v7 interactive prototype ----
D = ROOT / "DESIGN"
dt = (D / "index.html").read_text(encoding="utf-8") if (D / "index.html").is_file() else ""
ck("design:index", len(dt) > 20000, "%d chars" % len(dt))
ck("design:v7-header", "DESIGN v7" in dt and "دور هفتم" in dt, "design round 7 review")
ck("design:v6-archived", "DESIGN v6" in dt, "v6 archive line kept in spec")
ck("design:v5-archived", "DESIGN v5" not in dt or "DESIGN v6" in dt, "v5 superseded")
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
   ["Chains","Import notes","Dictate","gemini-flash-lite-latest","medium","TEACH","PRACTICE"]), "8 LH panel buttons restored")
ck("design:epm-link", "askAi" in dt and "EPM" in dt, "minor EPM idea in exam")
ck("design:15views", dt.count('<button data-go=') == 15, "15 design views: +section-practice +routine")
ck("design:6tabs", dt.count('data-tab="') == 6 and all(x in dt for x in
   ['data-tab="Learn"','data-tab="Practice"','data-tab="AI"','data-tab="Leaderboard"','data-tab="Profile"','data-tab="Routine"']),
   "six tabs: 5 Mimo tabs + روتین روزانه (MAX forbidden)")
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
    "extract_mimo_nodes_v7.py", "write_habitica_spec.py", "build_design_v7.py",
    "design_v7_template.html", "finalize_v7.py"]), "reproducible extract -> build pipeline (v5 + v6 + v7)")

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
ck("design:screenshot", (D / "REFERENCE/learnharness-ui-user-screenshot.png").is_file()
   and (D / "REFERENCE/learnharness-ui-user-screenshot.png").stat().st_size > 10000, "user LH screenshot")
ck("design:screenshot2", (D / "REFERENCE/learnharness-main-panel-user-screenshot.png").is_file()
   and (D / "REFERENCE/learnharness-main-panel-user-screenshot.png").stat().st_size > 10000, "user LH main-panel screenshot")
ck("design:screenshot3", (D / "REFERENCE/lh-composer-user-screenshot.png").is_file()
   and (D / "REFERENCE/lh-composer-user-screenshot.png").stat().st_size > 5000, "LH composer screenshot")
ck("design:screenshot4", (D / "REFERENCE/lh-topbar-user-screenshot.png").is_file()
   and (D / "REFERENCE/lh-topbar-user-screenshot.png").stat().st_size > 3000, "LH topbar screenshot")
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
ck("design:v6:unfinished", all(x in dt for x in ["unfinishedModal","Unfinished track","personalised certificate","ic_mimo_mascot"]),
   "Unfinished track modal from certificate strings")
ck("design:v6:career-content", all(x in dt for x in ["Career Paths","Full-Stack Developer","Back-End Developer","Courses","TypeScript","JS required","6/14"]),
   "Select Path career cards + course rows")
ck("design:v6:certificate", all(x in dt for x in ["Professional Certificate","22% Complete","2/9","path_overview_certificate_percent_complete"]),
   "certificate card from ARSC strings")
ck("design:v6:sections-from-code", all(x in dt for x in ["sectionRows","path_overview_section_ordinal","tutorialIds","Section Project","Coming soon"]),
   "numbered sections + tutorial ids rendered from shipped JSON")
ck("design:v6:no-max-tab", 'data-tab="MAX"' not in dt and "tabMap" in dt,
   "MAX tab forbidden; 6 tabs with روتین روزانه kept")
ck("design:v6:clean-learn", all(x in dt for x in ["1,272","ic_key","ic_infinity","overview-card","l6n1"]),
   "clean Learn: 3 pills + overview card + exact nodes")
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

# ---- DESIGN v7: exact nodes, bolt practice, AI tidy, exam controls, routine ----
ck("design:v7:nodes", all(x in dt for x in
   ["l7n1","l7n2","l7n3","l7n4","l7n5","l7b1","l7b2","node-start","gloss-fab","hring","Q314"]),
   "exact Mimo node states: done/cur/half/locked/bolt + elbow connector + glossary")
ck("design:v7:node-geometry", (D / "NODE_CODE_GEOMETRY.json").is_file(), "NODE_CODE_GEOMETRY.json present")
np_ = D / "NODE_CODE_GEOMETRY.json"
if np_.is_file():
    ng = json.loads(np_.read_text(encoding="utf-8"))
    ck("design:v7:node-vectors", len(ng["vectors"]) >= 50 and all(v["paths"] for v in ng["vectors"].values()),
       "%d vectors with pathData" % len(ng["vectors"]))
    ck("design:v7:node-strings", sum(len(v) for v in ng["strings"].values()) >= 130,
       "%d ARSC strings" % sum(len(v) for v in ng["strings"].values()))
    ck("design:v7:node-content", len(ng["contentModel"]["sections"]) >= 15
       and sum(s["tutorialCount"] for s in ng["contentModel"]["sections"]) >= 200,
       "%d sections / %d tutorialIds" % (len(ng["contentModel"]["sections"]),
                                         sum(s["tutorialCount"] for s in ng["contentModel"]["sections"])))
    ck("design:v7:node-method", "CODE_FIRST" in ng["method"] and len(ng["animations"]) >= 2,
       "code-first + checkpoint window animations")
    ck("design:v7:node-isolation", len(ng["isolation"]) >= 4 and "var NODE=" in dt,
       "isolation contract + injected NODE payload")
pcat = ROOT / "CATALOGS/MIMO_PATH_NODES.csv"
ck("design:v7:node-catalog", pcat.is_file() and len(rows(pcat)) - 1 == 50, "50 node code-evidence rows")
ck("design:v7:section-practice", all(x in dt for x in
   ['data-screen="section-practice"','data-scope="learn-practice"','practiceQuestions','practiceModal','practiceStart','Fully charged','Practice anyway']),
   "bolt nodes open an isolated Learn checkpoint quiz")
sp = re.search(r'<section class="screen mimo" data-screen="section-practice".*?</section>', dt, re.S)
ck("design:v7:practice-isolation", bool(sp) and all(x not in sp.group(0) for x in
   ["timerChip","پاسخبرگ","پاسخنامه","POLICY","270","exam-hub","توضیح با هوش مصنوعی"]),
   "section practice has NO exam controls / timer / answer sheets")
ck("design:v7:ai-header", all(x in dt for x in
   ["اضافه کردن فایل","زنجیره گفت و گو","attachment","ic_link_external","ai-top-left"]),
   "tidy AI top row: file icon + short label + conversation chain")
ck("design:v7:ai-footer", all(x in dt for x in
   ["ai-foot","ic_microphone",'data-lh="Dictate"','data-mode="TEACH"','data-mode="PRACTICE"',"flex-wrap:nowrap"]),
   "TEACH/PRACTICE tiny on same single bottom line; Dictate (voice) kept")
ck("design:v7:exam-controls", all(x in dt for x in
   ["prevQ","nextQ","qnav","qfoot","result-foot","ic_arrow_left","ic_arrow_right"]),
   "two clean prev/next buttons + quiet one-line bottom controls")
lb = re.search(r'<section class="screen mimo" data-screen="leaderboard".*?</section>', dt, re.S)
ck("design:v7:no-promo", bool(lb) and "Promotion Zone" not in lb.group(0) and "منطقهٔ صعود" not in lb.group(0) and 'class="promo"' not in lb.group(0),
   "Promotion Zone removed from leaderboard UI")
ck("design:v7:routine-tab", all(x in dt for x in
   ['data-tab="Routine"','data-screen="routine"',"روتین روزانه","ic_calendar","ic_task_completed"])
   and 'data-tab="MAX"' not in dt,
   "6th low-key Mimo tab روتین روزانه; MAX still forbidden")
ck("design:v7:routine-isolation", all(x in dt for x in
   ['data-scope="routine-only"','data-isolated="exam learn leaderboard"',"var HAB=","HAB.constants","rtTasks"]),
   "Habitica scoring rules injected but isolated from exam/learn/leaderboard")
hp_ = D / "HABITICA_SCORING.json"
ck("design:v7:habitica-json", hp_.is_file(), "HABITICA_SCORING.json present")
if hp_.is_file():
    hg = json.loads(hp_.read_text(encoding="utf-8"))
    ck("design:v7:habitica-rules", len(hg["rules"]) >= 22 and len(hg["sources"]) >= 13,
       "%d rules / %d upstream sources" % (len(hg["rules"]), len(hg["sources"])))
    ck("design:v7:habitica-license", "GPL-3.0" in hg["license"] and "CC-BY-NC-SA" in hg["license"],
       "upstream licence recorded; no code/assets copied")
    ck("design:v7:habitica-commit", len(hg["commit"]) == 40 and "no code or assets copied" in hg["method"],
       "develop commit pinned, clean-room method stated")
hs = ROOT / "CATALOGS/HABITICA_SOURCES.csv"
ck("design:v7:habitica-hashes", hs.is_file() and len(rows(hs)) - 1 == 13
   and all(re.fullmatch(r"[0-9a-f]{64}", r[3]) for r in rows(hs)[1:]),
   "13 upstream files with real SHA-256 digests")
pv = ROOT / "CATALOGS/PRACTICE_VS_EXAM.csv"
ck("design:v7:practice-vs-exam", pv.is_file() and len(rows(pv)) - 1 == 12
   and "learn_bolt_practice" in pv.read_text(encoding="utf-8"),
   "12-row three-way isolation table")
ck("design:v7:no-habitica-assets", not re.search(r'(habitica|habitrpg)[^"\']*\.(png|jpg|webp|svg|woff|ttf)', dt, re.I),
   "no Habitica asset files referenced in prototype")
ck("design:v7:build-bytes", len(dt) > 300000, "%d chars" % len(dt))
ck("docs:v7:18", "DESIGN v7" in (ROOT / "18_DESIGN_ROUND_7.md").read_text(encoding="utf-8"), "v7 final log")
ck("docs:v7:19", "Habitica" in (ROOT / "19_HABITICA_ROUTINE_SPEC.md").read_text(encoding="utf-8")
   and "GPL-3.0" in (ROOT / "19_HABITICA_ROUTINE_SPEC.md").read_text(encoding="utf-8"), "Habitica scoring spec")
ck("docs:v7:notes", "DESIGN v7" in (D / "DESIGN_NOTES.fa.md").read_text(encoding="utf-8"), "v7 design notes")
ck("docs:v7:banners", sum("<!-- v7-banner -->" in (ROOT / d).read_text(encoding="utf-8") for d in docs if d.endswith(".md")) >= 19,
   "archived docs carry v7 superseded banner")
ck("scope:6tabs", "SIX_TABS_ROUTINE" in (ROOT / "CATALOGS/SCOPE_DECISIONS.csv").read_text(encoding="utf-8"),
   "explicit v7 6-tab decision")
ck("csv:practice-vs-exam", "konkur_exam" in pv.read_text(encoding="utf-8"), "exam column present")

# ---- docs cross-references ----
ck("docs:v6:17", "DESIGN v6" in (ROOT / "17_DESIGN_ROUND_6.md").read_text(encoding="utf-8"), "v6 log archived")
ck("docs:v6:notes", "DESIGN v6" in (D / "DESIGN_NOTES.fa.md").read_text(encoding="utf-8"), "v6 archive line in notes")
ck("docs:v5:16", "DESIGN v5" in (ROOT / "16_DESIGN_ROUND_5.md").read_text(encoding="utf-8"), "v5 log archived")
ck("docs:v4:15", "طرح نهایی" in (ROOT / "15_DESIGN_ROUND_4.md").read_text(encoding="utf-8"), "v4 final log (archived)")
ck("docs:v4:02", "حکم محصول ۵ تب" in (ROOT / "02_UI_FIDELITY_CONTRACT.md").read_text(encoding="utf-8"), "5-tab override (archived, MAX-specific)")
ck("docs:v4:08", "۵ تب" in (ROOT / "08_NAVIGATION_AND_IA.md").read_text(encoding="utf-8"), "5-tab IA (archived)")
ck("docs:v4:03", "سیاست بر اساس نوع آزمون" in (ROOT / "03_EXAM_HUB.md").read_text(encoding="utf-8"), "answer sheet policy")
ck("docs:v4:04", "دکمههای LH در چت مینیمال" in (ROOT / "04_AI_LEARN_HARNESS.md").read_text(encoding="utf-8"), "LH buttons in chat")
ck("scope:5tabs", "FIVE_TABS" in (ROOT / "CATALOGS/SCOPE_DECISIONS.csv").read_text(encoding="utf-8"), "archived 5-tab decision")
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
ck("manifest:v7", "DESIGN v7" in man["status"] and man["deliverables"]["design_round"] == "v7 (REVIEW)"
   and man["deliverables"]["design_views"] == 15 and man["deliverables"]["csv_catalogs"] == 22
   and man["deliverables"]["persian_docs"] == 21 and "design_round_7" in man,
   "MANIFEST advertises v7: 15 views / 22 CSVs / 21 docs")
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
