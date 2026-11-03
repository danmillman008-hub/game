#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fail-closed verification of the Konkur-upgrade planning deliverable."""
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
        "13_DESIGN_ROUND_2.md", "14_DESIGN_ROUND_3.md", "15_DESIGN_ROUND_4.md", "wireframes.html"]
csvs = {"UI_FIDELITY_RULES.csv": 10, "FEATURE_MAP.csv": 17, "EXAM_TYPES.csv": 11,
        "HADAF_TEMPLATES.csv": 7, "GAMIFICATION_MAP.csv": 13, "PHASES.csv": 8,
        "LEARNHARNESS_ACTIONS.csv": 32, "EVIDENCE_LEDGER.csv": 10, "OPEN_QUESTIONS.csv": 5,
        "DESIGN_FEEDBACK.csv": 20, "SCOPE_DECISIONS.csv": 11,
        "AI_PANEL_SPEC.csv": 19, "EPM_MINOR_OPTIONS.csv": 6,
        "EXAM_SECTION_TEMPLATES.csv": 7}
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

# wireframe uses real tokens and states the 4 tabs
t = (ROOT / "wireframes.html").read_text(encoding="utf-8")
ck("wireframe:tokens", all(x in t for x in ["#7E4BDE", "#FFF6F7FB".replace("FF", ""), "#F6F7FB", "#E4E6F1", "#66BC5A", "#F05A6E"]),
   "Mimo palette present")
ck("wireframe:legacy-tabs", t.count('class="tab') >= 4 and "<div class=\"tab\">Learn</div>" in t,
   "archived v1 wireframe renders its legacy tabs")
ck("wireframe:3col-grid", "repeat(3,minmax(0,1fr))" in t, "exam node grid")
ck("wireframe:v1-banner", "DESIGN/index.html" in t, "v1 archived, points to v2")

# ---- DESIGN v2 interactive prototype ----
D = ROOT / "DESIGN"
dt = (D / "index.html").read_text(encoding="utf-8") if (D / "index.html").is_file() else ""
ck("design:index", len(dt) > 20000, "%d chars" % len(dt))
ck("design:v4-header", "DESIGN v4" in dt and "FINAL" in dt, "final version 4")
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
ck("design:6views", dt.count('<button data-go=') == 6, "6 design views, counseling PARKED")
ck("design:5tabs", dt.count('data-tab="') == 5 and all(x in dt for x in
   ['data-tab="Learn"','data-tab="Practice"','data-tab="AI"','data-tab="Leaderboard"','data-tab="Profile"']),
   "five tabs Learn/Practice/AI/Leaderboard/Profile")
ck("design:learn", 'data-screen="learn"' in dt and "همان الگوی گرههای میمو" in dt, "Learn identical to Mimo")
ck("design:leaderboard", 'data-screen="leaderboard"' in dt, "leaderboard view")
ck("design:answer-sheet", all(x in dt for x in
   ["answerSheetBtn","policyHint","keyTestSheet","keyDescSheet","POLICY","during:false","during:true"]), "answer sheet policy + two keys")
ck("design:labeled-sections", dt.count('class="cat-meta"') == 7 and "زمان ثابت ۲۷۰ دقیقه" in dt,
   "7 labeled sections with fixed-time comprehensive template")
ck("design:api-key-not-designed", "DOCUMENTED_ONLY" not in dt and "وارد کردن کلید API" in dt,
   "API key is a note only, no settings UI")
js = re.search(r"<script>(.*?)</script>", dt, re.S)
used = set(re.findall(r'\$\("#([A-Za-z0-9_-]+)"\)', js.group(1))) if js else set()
defined = set(re.findall(r'id="([A-Za-z0-9_-]+)"', dt))
ck("design:js-ids", bool(js) and used <= defined, "%d used / %d defined; missing=%s" % (len(used), len(defined), sorted(used-defined)[:8]))
ck("design:notes", (D / "DESIGN_NOTES.fa.md").is_file() and (D / "DESIGN_NOTES.fa.md").stat().st_size > 2000, "design notes")
ck("design:screenshot", (D / "REFERENCE/learnharness-ui-user-screenshot.png").is_file()
   and (D / "REFERENCE/learnharness-ui-user-screenshot.png").stat().st_size > 10000, "user LH screenshot")
ck("design:screenshot2", (D / "REFERENCE/learnharness-main-panel-user-screenshot.png").is_file()
   and (D / "REFERENCE/learnharness-main-panel-user-screenshot.png").stat().st_size > 10000, "user LH main-panel screenshot")
ck("design:screenshot3", (D / "REFERENCE/lh-composer-user-screenshot.png").is_file()
   and (D / "REFERENCE/lh-composer-user-screenshot.png").stat().st_size > 5000, "LH composer screenshot")
ck("design:screenshot4", (D / "REFERENCE/lh-topbar-user-screenshot.png").is_file()
   and (D / "REFERENCE/lh-topbar-user-screenshot.png").stat().st_size > 3000, "LH topbar screenshot")
ck("docs:v4:15", "طرح نهایی" in (ROOT / "15_DESIGN_ROUND_4.md").read_text(encoding="utf-8"), "v4 final log")
ck("docs:v4:02", "حکم محصول ۵ تب" in (ROOT / "02_UI_FIDELITY_CONTRACT.md").read_text(encoding="utf-8"), "5-tab override")
ck("docs:v4:08", "۵ تب" in (ROOT / "08_NAVIGATION_AND_IA.md").read_text(encoding="utf-8"), "5-tab IA")
ck("docs:v4:03", "سیاست بر اساس نوع آزمون" in (ROOT / "03_EXAM_HUB.md").read_text(encoding="utf-8"), "answer sheet policy")
ck("docs:v4:04", "دکمههای LH در چت مینیمال" in (ROOT / "04_AI_LEARN_HARNESS.md").read_text(encoding="utf-8"), "LH buttons in chat")
ck("scope:5tabs", "FIVE_TABS" in (ROOT / "CATALOGS/SCOPE_DECISIONS.csv").read_text(encoding="utf-8"), "5-tab decision")
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
    ck("apk:" + slug + ":dart", (ROOT / "SOURCE_APPS" / slug / "dart" / "STRINGS_ALL.txt").is_file(), "Dart snapshot strings")
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
