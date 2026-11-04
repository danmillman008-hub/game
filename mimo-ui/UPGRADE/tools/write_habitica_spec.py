#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""write_habitica_spec.py — record Habitica SCORING SYSTEM rules for round 7.

The user supplied https://github.com/habitrpg/habitica and said:
  "از این پروژه استفاده کن سیستم امتیاز دهیش و هیچی قرار نیست قاتی بشه با
   اپلیکیشن خود ما ... یه جوری باشه فکر کنن برای میمو هست نه خود اپلیکیشن
   ینی زیادی تو چشم نزنه"

So ONLY the abstract scoring rules are recorded here. NO Habitica source code,
assets, strings, UI, fonts or colours are copied into the deliverable. The
upstream files were fetched read-only into /home/user/_work/hab/ (outside the
repo) and only their SHA-256 digests and rule descriptions are catalogued.

Writes:
  DESIGN/HABITICA_SCORING.json
  CATALOGS/HABITICA_SOURCES.csv
  CATALOGS/HABITICA_SCORING.csv
  CATALOGS/PRACTICE_VS_EXAM.csv
"""
import csv
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
UP = (HERE / "..").resolve()
OUT = UP / "DESIGN"
CAT = UP / "CATALOGS"
SCRATCH = Path("/home/user/_work/hab")

REPO = "https://github.com/habitrpg/habitica"
COMMIT = "12091ca02990533fdf38c2f0947397f0b4e39d59"
LICENSE = "GPL-3.0 code; BrowserQuest assets CC-BY-SA 3.0; HabitRPG assets/content CC-BY-NC-SA 3.0"

# local scratch filename -> upstream path, role
SOURCES = [
    ("website_common_script_ops_scoreTask.js", "website/common/script/ops/scoreTask.js", "core scoring: delta, EXP/GP/HP, checklist, reward"),
    ("website_common_script_fns_crit.js", "website/common/script/fns/crit.js", "critical hit chance & multiplier"),
    ("website_common_script_fns_updateStats.js", "website/common/script/fns/updateStats.js", "level-up, HP/MP/XP stat update"),
    ("website_common_script_libs_statsComputed.js", "website/common/script/libs/statsComputed.js", "computed INT/PER/STR/CON stats"),
    ("website_common_script_libs_taskDefaults.js", "website/common/script/libs/taskDefaults.js", "task types, defaults, priority, repeat"),
    ("website_common_script_constants.js", "website/common/script/constants.js", "MAX_HEALTH, MAX_LEVEL, MAX_STAT_POINTS"),
    ("website_common_script_index.js", "website/common/script/index.js", "public scoring helpers export"),
    ("statHelpers.js", "website/common/script/statHelpers.js", "toNextLevel, diminishingReturns"),
    ("predictableRandom.js", "website/common/script/fns/predictableRandom.js", "deterministic crit seed"),
    ("cron.js", "website/common/script/cron.js", "daily reset, Perfect Day, missed dailies"),
    ("server_cron.js", "website/server/libs/cron.js", "Perfect Day achievement, damage, MP"),
    ("tasks_controller.js", "website/server/controllers/api-v3/tasks.js", "priority enum 0.1/1/1.5/2"),
    ("content_tasks.js", "website/common/script/content/tasks.js", "task content defaults / sample labels"),
]

CONSTANTS = {
    "MAX_HEALTH": 50,
    "MAX_LEVEL": 100,
    "MAX_LEVEL_HARD_CAP": 9999,
    "MAX_STAT_POINTS": 100,
    "MAX_TASK_VALUE": 21.27,
    "MIN_TASK_VALUE": -47.27,
    "CLOSE_ENOUGH": 0.00001,
    "DELTA_BASE": 0.9747,
    "EXP_MULTIPLIER": 6,
    "HP_MULTIPLIER": 2,
    "CRIT_BASE_CHANCE": 0.03,
    "CRIT_BASE_MULTIPLIER": 1.5,
    "PRIORITY_TRIVIAL": 0.1,
    "PRIORITY_EASY": 1,
    "PRIORITY_MEDIUM": 1.5,
    "PRIORITY_HARD": 2,
    "PERFECT_DAY_STREAK_DAYS": 21,
    "DEFAULT_REWARD_VALUE": 10,
    "DEFAULT_TASK_VALUE": 0,
}

# rule id, group, formula / rule (our own words), upstream file, Mimo mapping
RULES = [
    ("HS-01", "task-types", "Four task types: habit (plus/minus), daily (checkbox + streak), todo (one-shot + checklist), reward (costs currency, no value change).", "website/common/script/libs/taskDefaults.js", "روتین روزانه: عادت / روزانه / کار امروز / پاداش"),
    ("HS-02", "defaults", "Default task: priority=1 (Easy), value=0, attribute=str; reward starts at value=10; daily streak starts at 0.", "website/common/script/libs/taskDefaults.js", "مقادیر پیشفرض داخل تب روتین"),
    ("HS-03", "priority", "Priority multipliers: Trivial 0.1, Easy 1, Medium 1.5, Hard 2 (per API enum), applied to delta/EXP/GP/HP.", "website/server/controllers/api-v3/tasks.js", "چیپهای ریز «سختی» روی هر کار"),
    ("HS-04", "value-clamp", "task.value clamped to [MIN_TASK_VALUE=-47.27, MAX_TASK_VALUE=21.27] before delta.", "website/common/script/ops/scoreTask.js", "محدودکنندهٔ امتیاز، داخل منطق"),
    ("HS-05", "delta", "delta = 0.9747 ** clamp(task.value), signed by direction: up=+delta, down=-delta; unchecking reverses the same delta.", "website/common/script/ops/scoreTask.js", "امتیازدهی نزولی/صعودی نرم"),
    ("HS-06", "checklist", "Checklist partial credit: daily down and todo up scale delta by completed/total (and by 1/total when shrinking); scores can be split.", "website/common/script/ops/scoreTask.js", "چکلیستهای کوچک داخل کارها"),
    ("HS-07", "exp", "exp += round(delta * (1 + INT*0.025) * priority * crit * 6); INT bonus only when positive delta.", "website/common/script/ops/scoreTask.js", "نوار XP روتین"),
    ("HS-08", "gp", "gp += ceil(delta * priority * crit * (1 + PER*0.02) * streakBonus); streakBonus = currStreak/100 + 1 (min +1).", "website/common/script/ops/scoreTask.js", "شمارندهٔ سکهٔ روتین (جدا از سکههای Learn)"),
    ("HS-09", "hp", "On down: hp += delta * (1 - min(CON,100)/250 clamped >=0.1) * priority * 2, result at most -1; hp bounded by MAX_HEALTH=50.", "website/common/script/ops/scoreTask.js", "نوار سلامت خیلی کم رنگ، بدون RPG"),
    ("HS-10", "crit", "crit chance = 0.03 * (1 + STR/100); crit multiplier = 1.5 + (4*STR)/(STR+200); deterministic predictableRandom(user).", "website/common/script/fns/crit.js", "یک «ضریب شانس» کمSer و اختیاری"),
    ("HS-11", "predictable-random", "predictableRandom uses a deterministic sin-based seed from user id + task id + date, so scoring is reproducible (no real RNG).", "website/common/script/fns/predictableRandom.js", "منطق قابل تکرار، بدون شانس واقعی"),
    ("HS-12", "level", "toNextLevel(lvl) = 25*lvl for lvl<5; 150 at lvl=5; round((lvl^2*0.25 + 10*lvl + 139.75)/10)*10 afterwards.", "website/common/script/statHelpers.js", "سطح روتین و نوار پیشرفت"),
    ("HS-13", "level-up", "On crossing toNextLevel: level+1, HP restored to 50, XP subtracts threshold, +1 stat point (capped 100).", "website/common/script/fns/updateStats.js", "افزایش سطح، بدون بنر پر زرقوبرق"),
    ("HS-14", "diminishing-returns", "diminishingReturns(bonus,max,halfway=max/2) = max*bonus/(bonus+halfway): higher bonuses saturate.", "website/common/script/statHelpers.js", "جلوگیری از انفجار امتیازات"),
    ("HS-15", "mp", "MP gain on positive delta, capped by statsComputed(user).maxMP; used for skill unlocks (not exposed in Mimo skin).", "website/common/script/ops/scoreTask.js", "فقط ثبت شده؛ در UI نمیآید"),
    ("HS-16", "daily-streak", "Completing a daily increments its streak; each 21 consecutive days grants an achievement; cron resets streaks for missed dailies.", "website/common/script/cron.js", "شمارندهٔ «روز پیاپی» Mimo"),
    ("HS-17", "perfect-day", "Perfect Day (all dailies done) grants a buff / achievement; MP buffer = max(10, 0.1*maxMP) * dailyChecked/(dailyDueUnchecked + dailyChecked).", "website/server/libs/cron.js", "یک نشان ریز «روز کامل»"),
    ("HS-18", "missed-daily", "Cron applies missed-daily damage at dayStart (custom dayStart, multiDaysCountAsOneDay=true); HP loss uses same priority scaling.", "website/server/libs/cron.js", "منطق پسزمینه، بدون اعلان پر سر و صدا"),
    ("HS-19", "reward", "Reward task: gp -= value (default 10), no delta/EXP/HP change; value stays constant.", "website/common/script/ops/scoreTask.js", "پاداش کوچک با سکهٔ روتین"),
    ("HS-20", "isolation", "All Habitica-derived rules live ONLY inside data-screen=routine; they are not wired to exam scores, leaderboard XP, Learn coins or lesson progress.", "DESIGN/index.html", "هیچی قرار نیست قاتی بشه با اپلیکیشن خود ما"),
    ("HS-21", "licensing", "Habitica code is GPL-3.0 and HabitRPG assets/content are CC-BY-NC-SA 3.0; only abstract rules + SHA-256 digests are recorded, no code/assets copied.", "LICENSE", "پاکسازی حقوقی / clean-room"),
    ("HS-22", "mimo-skin", "Routine tab uses ONLY Mimo tokens (card/button_primary/progress/TextLabel) and extracted Mimo vectors; no pixel art, avatars, RPG icons or new colours/fonts/radii.", "CATALOGS/DESIGN_TOKENS.json", "فکر کنن برای میمو هست، زیادی تو چشم نزنه"),
]

TASK_TYPES = [
    {"id": "habit", "fa": "عادت", "en": "Habit", "direction": "up/down", "icon": "ic_sparks_alt", "priority": "1", "streak": False},
    {"id": "daily", "fa": "روزانه", "en": "Daily", "direction": "up", "icon": "ic_calendar", "priority": "1", "streak": True},
    {"id": "todo", "fa": "کار امروز", "en": "To-Do", "direction": "up", "icon": "ic_task_completed", "priority": "1.5", "streak": False},
    {"id": "reward", "fa": "پاداش", "en": "Reward", "direction": "buy", "icon": "ic_coin", "priority": "1", "streak": False},
]

ISOLATION = [
    "data-screen=routine is the ONLY surface that reads HABITICA_SCORING.json",
    "No Habitica string, asset, avatar, font, colour or layout is used",
    "Exam hub / exam-run / exam-result / answer sheets / timer never import routine scoring",
    "Learn coins, path progress, leaderboard XP and AI chat are untouched",
    "Leaderboard Promotion Zone removed; routine scores are NOT a leaderboard",
    "Bolt checkpoint practice is a LEARN sub-screen, NOT an exam and NOT a routine",
]

PRACTICE_VS_EXAM = [
    ("PV-01", "surface", "data-screen=section-practice (class=screen mimo)", "data-screen=exam-hub / exam-run / exam-result (class=screen konkur)", "two separate screens, two skins"),
    ("PV-02", "entry", "lightning-bolt node inside the Learn path map", "5th bottom tab Practice + exam hub cards", "no shared entry point"),
    ("PV-03", "scope", "quiz from tutorialIds of the topic UP TO that section", "full Konkur exam with 7 labelled sections / field templates", "ازمون از مبحث تا اون بخشه"),
    ("PV-04", "timer", "no timer chip, no countdown, no auto-submit", "click chip -> number -> start -> reverse countdown, pause/resume, auto-submit", "timer ONLY inside exam"),
    ("PV-05", "answer sheet", "no پاسخبرگ / no پاسخنامه", "پاسخبرگ (chosen options) + پاسخنامه (descriptive + test key)", "policy split is exam-only"),
    ("PV-06", "answer key", "inline Mimo lesson feedback bottom sheet", "test key + descriptive explanations; pure-time opens key at finish", "no POLICY object in practice"),
    ("PV-07", "duration", "short checkpoint, no 270 min", "comprehensive fixed 270 min", "fixed time belongs to exam"),
    ("PV-08", "AI button", "none (Mimo lesson feedback)", "one توضیح با هوش مصنوعی on question + same on result", "no transfer of practice to AI chat"),
    ("PV-09", "dialogs", "Fully charged! / You've mastered the section! / Practice anyway", "پاسخبرگ / پاسخنامه / خروج / اتمام آزمون", "Mimo smart-practice dialogs only"),
    ("PV-10", "data", "test-tracks.json sections[].tutorialIds", "EXAM_SECTION_TEMPLATES.csv + EXAM_TYPES.csv", "separate data sources"),
    ("PV-11", "routine", "bolt practice is NOT a daily routine task", "routine scoring is ONLY in data-screen=routine", "three-way isolation"),
    ("PV-12", "code evidence", "PathMapScreenKt / SmartPractice* / ic_bolt* / rc_checkpoint_window_*", "Konkur plan catalogs (design-only, no Mimo code)", "code-first vs plan-first"),
]


def digest(name):
    p = SCRATCH / name
    if p.exists():
        return hashlib.sha256(p.read_bytes()).hexdigest(), p.stat().st_size
    return "", 0


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    CAT.mkdir(parents=True, exist_ok=True)

    src_rows = []
    for local, upstream, role in SOURCES:
        h, size = digest(local)
        src_rows.append({
            "local_scratch": "/home/user/_work/hab/" + local,
            "upstream_path": upstream,
            "url": REPO + "/blob/" + COMMIT + "/" + upstream,
            "sha256": h,
            "bytes": size,
            "license": LICENSE,
            "role": role,
        })

    doc = {
        "method": "READ_ONLY_RULE_EXTRACTION / no code or assets copied into the deliverable",
        "repo": REPO,
        "commit": COMMIT,
        "default_branch": "develop",
        "license": LICENSE,
        "user_instruction": "از این پروژه استفاده کن سیستم امتیاز دهیش و هیچی قرار نیست قاتی بشه با اپلیکیشن خود ما صرفا رابط کاربریش رو نمیخواد زیادی تغییر بدی ولی یه جوری باشه فکر کنن برای میمو هست نه خود اپلیکیشن ینی زیادی تو چشم نزنه",
        "interpretation": "only the scoring system; a quiet Mimo-skinned ششمین تب «روتین روزانه», isolated from everything else; MAX still forbidden",
        "constants": CONSTANTS,
        "taskTypes": TASK_TYPES,
        "rules": [
            {"id": r[0], "group": r[1], "rule": r[2],
             "upstream_file": r[3], "mimo_mapping": r[4]}
            for r in RULES
        ],
        "sources": src_rows,
        "isolation": ISOLATION,
        "counts": {"sources": len(src_rows), "rules": len(RULES),
                   "task_types": len(TASK_TYPES), "isolation_rules": len(ISOLATION)},
    }
    (OUT / "HABITICA_SCORING.json").write_text(
        json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")

    with (CAT / "HABITICA_SOURCES.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["local_scratch", "upstream_path", "url", "sha256", "bytes", "license", "role"])
        for r in src_rows:
            w.writerow([r["local_scratch"], r["upstream_path"], r["url"],
                        r["sha256"], r["bytes"], r["license"], r["role"]])

    with (CAT / "HABITICA_SCORING.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["rule_id", "group", "rule", "upstream_file", "mimo_mapping"])
        for r in RULES:
            w.writerow(r)

    with (CAT / "PRACTICE_VS_EXAM.csv").open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["row_id", "aspect", "learn_bolt_practice", "konkur_exam", "isolation_rule"])
        for r in PRACTICE_VS_EXAM:
            w.writerow(r)

    print(json.dumps({
        "output": str(OUT / "HABITICA_SCORING.json"),
        "bytes": (OUT / "HABITICA_SCORING.json").stat().st_size,
        "sources": len(src_rows),
        "hashes_resolved": sum(1 for r in src_rows if r["sha256"]),
        "rules": len(RULES),
        "practice_vs_exam_rows": len(PRACTICE_VS_EXAM),
    }, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
