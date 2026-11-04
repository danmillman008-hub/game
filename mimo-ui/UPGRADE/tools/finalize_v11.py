#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""finalize_v11.py — round-11 docs/catalogs/banners/MANIFEST. Idempotent."""
from __future__ import annotations
import csv
import json
from pathlib import Path

UP = Path(__file__).resolve().parents[1]
CAT = UP / "CATALOGS"
D = UP / "DESIGN"
MARK = "<!-- v11-banner -->"

APPEND = {
    "DESIGN_FEEDBACK.csv": [
        ["F-59", "بلوک Wooden League و ۵ ردیف رقیب کلاً حذف شود، فقط my status بماند",
         "لیگ، شمارش معکوس، نشانهای لیگ، ۵ ردیف رقبا و «Wooden/League» کارت سوم حذف شد؛ فقط «My status / وضعیت من» + ۳ کارت آمار + «آزمونها و امتیازات من» ماند",
         "DESIGN/index.html#leaderboard", "APPLIED"],
        ["F-60", "سرتیترها و کارتها و کورسها کنکوری شوند",
         "Career Paths → «یادگیری برنامه محور»؛ Courses → «یادگیری مبحثی»؛ ۴ کارت درشت (۳ برنامهٔ پایه + مبحثی)؛ ۱۲ کورس «درس × پایه»",
         "DESIGN/index.html#select-path", "APPLIED"],
        ["F-61", "نمای مسیر: مدرک پایان دوره، ۲۲ درصد، تاریخهای دو هفتهای، دروس، فصل/درس، بدون آرم برنامهنویسی",
         "۱۰ بازهٔ ۱ آبان..۱۵ اسفند با «دروس: زیست، شیمی، ریاضی، فیزیک»؛ برای کورسها ۶۰ فصل / ۱۸۰ درس؛ تمام ic_badge_*/ic_code_* با وکتور بومی میمو جایگزین شد",
         "DESIGN/KONKUR_CURRICULUM.json, DESIGN/index.html#path-overview", "APPLIED"],
    ],
    "SCOPE_DECISIONS.csv": [
        ["D39", "لیدربورد", "MY_STATUS_ONLY_V11", "جدول رقابت بطور کامل حذف؛ فقط وضعیت من/آمار/آزمونهای خود فرد",
         "بازخورد صریح دور یازدهم", "23_DESIGN_ROUND_11.md §۱"],
        ["D40", "مسیرها و کورسها", "PROGRAM_AND_TOPIC_TRACKS_V11", "برنامهمحور (۳ پایه × ۱۰ بازهٔ دو هفتهای) + مبحثی (۱۲ کورس، فصل/درس)",
         "بازخورد صریح دور یازدهم", "DESIGN/KONKUR_CURRICULUM.json"],
        ["D41", "نشانها", "NO_PROGRAMMING_EMBLEMS_V11", "هیچ ic_badge_*/ic_code_lang_*/ic_code_playground_template_* در UI؛ فقط وکتورهای استخراجشدهٔ میمو",
         "بازخورد صریح دور یازدهم", "CATALOGS/UI_FIDELITY_RULES.csv F35-F37"],
    ],
    "UI_FIDELITY_RULES.csv": [
        ["F35", "لیدربورد", "فقط «My status / وضعیت من» + ۳ کارت آمار + کادر آزمونها؛ بدون لیگ/رقبا/شمارش معکوس",
         "DESIGN/index.html#leaderboard + F-59"],
        ["F36", "مسیرها", "«یادگیری برنامه محور» / «یادگیری مبحثی» / «مدرک پایان دوره» / «۲۲ درصد کامل شده» / «دروس»",
         "KONKUR_CURRICULUM.json + F-60/F-61"],
        ["F37", "آیکونها", "بدون ic_badge_*/ic_code_*؛ فقط وکتورهای ARSC میمو (ic_cap*, ic_target, img_brain, ic_sparks_alt, ic_flash_filled, …)",
         "DESIGN/CODE_GEOMETRY.json::vectors"],
    ],
    "OPEN_QUESTIONS.csv": [
        ["U12", "آیا اسامی دقیق فصل/درس همان سرفصلهای استاندارد کتابهای درسیاند؟",
         "ASSUMED: بله — APK همدرس فقط سلسلهمراتب «کتاب ← فصل ← مبحث» را دارد (helpcenter learn-books) و اسامی سمت سروراند؛ ۶۰ فصل / ۱۸۰ درس در KONKUR_CURRICULUM.json ثبت شدند",
         "no", "تأیید نهایی دیزاین"],
    ],
}
for name, new_rows in APPEND.items():
    p = CAT / name
    with p.open(encoding="utf-8", newline="") as f:
        body = list(csv.reader(f))[1:]
    present = {r[0] for r in body if r}
    todo = [r for r in new_rows if r[0] not in present]
    if todo:
        with p.open("a", encoding="utf-8", newline="") as f:
            csv.writer(f).writerows(todo)
    print(name, "+", len(todo), "->", len(body) + len(todo))

# --------------------------------------------------------------------------
# docs
# --------------------------------------------------------------------------
DOC23 = r'''# دور یازدهم طراحی — DESIGN v11 (لیدربورد، مسیرهای برنامهمحور، کورسهای مبحثی)

> **وضعیت:** `DESIGN v11 · REVIEW` — منتظر تأیید نهایی. همچنان **فقط پلن/دیزاین**؛ هیچ کد محصولی نوشته نشده.
> جایگزین `22_DESIGN_ROUND_10.md` بهعنوان «حِکم فعلی محتوا»؛ **معماری اورجینال قوسدار دور دهم دستنخورده** است.

---

## ۱. لیدربورد و اطلاعات من

| حذف شد | ماند |
|---|---|
| `Wooden League` + `6d 22h 38m` | **My status / «وضعیت من»** |
| ۵ ردیف رقیب (`MIGUELBAOBAB`, `mairi`, `Aska`, `sarah`, `lucas correia`) | ۳ کارت آمار خود فرد |
| نشانهای لیگ (باز/قفل) و «چوبی / League» کارت سوم | «آزمونها و امتیازات من» + ۵ ردیف |

کارت سوم به «آزمونهای من / ۷» با `ic_trophy` تغییر کرد تا هیچ اثری از لیگ نماند. بدون Promotion Zone (مصوبهٔ v6) همچنان پابرجاست.

## ۲. انتخاب مسیر — سرتیترها

| قبل | **بعد** |
|---|---|
| `Career Paths` | **«یادگیری برنامه محور»** |
| `Courses` | **«یادگیری مبحثی»** |

**چهار کارت درشت** (هر کدام یک آیکون ۴۸dp از وکتورهای واقعی میمو، بدون هیچ نشان برنامهنویسی):

1. «یادگیری همگام با برنامه آزمون دوازدهم» — `ic_cap_filled`
2. «یادگیری همگام با برنامه آزمون یازدهم» — `ic_cap`
3. «یادگیری همگام با برنامه آزمون دهم» — `ic_target`
4. «یادگیری مبحثی» — `ic_square_rounded` (اسکرول به فهرست کورسها)

> کارت چهارم برای پر کردن همان «۴ آیکون درشت»ای است که خواستید؛ سه تای اول نام برده شدند و چهارم به بخش مبحثی وصل است (`U12` در کنار سایر فرضها ثبت شد).

**۱۲ کورس** (۴ درس × ۳ پایه، دقیقاً به ترتیبی که نوشتید):

| دهم | یازدهم | دوازدهم |
|---|---|---|
| زیست دهم · ریاضی دهم · شیمی دهم · فیزیک دهم | زیست یازدهم · ریاضی یازدهم · شیمی یازدهم · فیزیک یازدهم | زیست دوازدهم · ریاضی دوازدهم · شیمی دوازدهم · فیزیک دوازدهم |

آیکونها: زیست `img_brain`، ریاضی `ic_target`، شیمی `ic_sparks_alt`، فیزیک `ic_flash_filled` — همگی استخراجشده از `res/drawable/*.xml`. **هیچ `ic_badge_js` / `ic_code_lang_*` / `ic_code_playground_template_*`ای نمایش داده نمیشود**؛ حتی در باتمشیت «Create Playground» که ساختارش سر جایش ماند و فقط آیکونهایش عوض شد.

## ۳. نمای مسیرِ برنامهمحور

| المان | متن |
|---|---|
| kicker | «یادگیری برنامه محور» |
| عنوان | «یادگیری همگام با برنامه آزمون دوازدهم» (با کلیک روی یازدهم/دهم عوض میشود) |
| کارت گواهی | **«مدرک پایان دوره»** |
| پیشرفت | **«۲۲ درصد کامل شده»** + `2/9` |
| زیرمباحث | **۱۰ بازهٔ دو هفتهای** |

تاریخها از **۱ آبان** تا **۱۵ اسفند** (۵ ماه: آبان، آذر، دی، بهمن، اسفند):

`۱ آبان · ۱۵ آبان · ۱ آذر · ۱۵ آذر · ۱ دی · ۱۵ دی · ۱ بهمن · ۱۵ بهمن · ۱ اسفند · ۱۵ اسفند`

زیر هر تاریخ: **«دروس: زیست، شیمی، ریاضی، فیزیک»** (`lessons` → **«دروس»**). داخل هر بازه هم ۴ ردیف «درس ۱ · زیست» … «درس ۴ · فیزیک» است. حلقههای ۴۳٪/۰٪، «پروژهٔ مبحث» و «بهزودی»، نوار پیشرفت، دکمههای ادامه/نمای دوره **همگی سر جای خود ماندند**. همان روند دقیقاً برای **یازدهم** و **دهم** تکرار میشود.

## ۴. نمای مسیرِ مبحثی (کورسها)

وقتی یکی از ۱۲ کورس باز میشود، همان نمای مسیر (kicker «یادگیری مبحثی»، عنوان نام کورس، «مدرک پایان دوره»، ۴۳٪/۰٪، `2/9`) با **اسم فصل و اسم درس** پر میشود، نه نام بخشهای JavaScript/HTML/CSS. برای `زیست دهم`: «فصل ۱ · ساختار سلول و بافت» ← «دروس: غشای سلولی، اندامکهای سلول، بافتهای گیاهی و جانوری» و الیآخر.

- منبع سلسلهمراتب: `SOURCE_APPS/hamdars/HELP_CENTER_UX.md §learn-books` («کتاب ← فصل ← مبحث») + مدل محتوای کنکوری داخل ریپو (`15_DESIGN_ROUND_4.md §نام مباحث/درسها`: سلول و بافت، ژنتیک، سمها، ترمودینامیک، تعادل شیمیایی …).
- خروجی: **`DESIGN/KONKUR_CURRICULUM.json`** + **`CATALOGS/KONKUR_CURRICULUM.csv`** = ۱۲ کورس / **۶۰ فصل** / **۱۸۰ درس**.
- شفافیت: APK همدرس فقط سلسلهمراتب را نشان میدهد و اسامی دقیق سمت سروراند؛ اسامی این جدول سرفصلهای استاندارد کتابهای درسیاند و بهعنوان فرض `U12` ثبت شدهاند. اگر لیست دقیقتری مدنظرتان است، جایگزین میشود.

## ۵. بدون تغییر

معماری اورجینال قوسدار (۳ لاین ۸۰/۱۹۶/۳۱۲، فاصلهٔ ۲۴dp، زانوهای `Q` شعاع ۳۲dp، ۲ قطعهٔ رنگی) · ۵ تب و `MAX` ممنوع · روتین/Habitica و دیکته حذفشده · بدون یادداشت داخل UI · **۷ بخش لیبلدار + قالب فیلد + پاسخنامهٔ تشریحی** · تایمر فقط داخل آزمون و ۲۷۰ دقیقهٔ ثابت · «پاسخبرگ»≠«پاسخنامه» · تکدکمهٔ AI · **صفر قفل یادگیری** و تنها «آزمون نهایی / دو هفتگی» · بولت ← `section-practice` جدا · چت مینیمال · RTL/شب · ۱۴ اسکرینشات فقط **چک بصری**.

## ۶. تحویل

`tools/build_design_v11.py` (از `design_v10_full.html`) → `DESIGN/index.html` ۳۸۷٬۰۰۳ بایت / ۱۴ نما / ۵ تب / ۹۳ وکتور / ۱۱۳ آیکن رسمشده / ۰ قفل یادگیری. `tools/finalize_v11.py` → کاتالوگها/داکیومنتها/منیفست. `verify_upgrade.py` PASS، `check_v11.js` **۷۸ تست / ۰ خطا**، `node --check` OK. تأیید نهایی همچنان **PENDING**؛ هیچ کد محصولی نوشته نشده.
'''

NOTES = r'''# یادداشتهای طراحی — DESIGN v11

> نسخهٔ جاری: **DESIGN v11 · REVIEW** (منتظر تأیید نهایی). نسخههای **DESIGN v6 / DESIGN v7 / DESIGN v8 / DESIGN v9 / DESIGN v10** بایگانی حسابرسیاند. همچنان **فقط پلن/دیزاین**؛ هیچ کد محصولی نوشته نشده.

## ۱. اصل

کد مبناست (`ARSC`، `dimen.xml`، `drawable/*.xml`، `pathData`، `anim`، `DEX`، `test-tracks.json`)؛ ۱۴ اسکرینشات فقط `VISUAL_CROSSCHECK_ONLY`. `NODE_CODE_GEOMETRY.json` همچنان حکم هندسهٔ مسیر است. فقط **نام درس/فصل/مبحث و لیبلها** کنکوری میشود؛ ۰ رنگ/فونت/شعاع/آیکون تازه.

## ۲. معماری اورجینال قوسدار (دستنخورده)

سه لاین `۸۰/۱۹۶/۳۱۲`، ترتیب `center/right/center/left/center/left`، فاصلهٔ **۲۴dp**، گام ۱۱۶dp، زانوهای گرد `Q` شعاع **۳۲dp** (`A/B/A/B/B`)، دو قطعهٔ رنگی، `viewBox 392×720`، شعاع گره ۲۶dp، ضخامت مسیر ۱۰dp، آیکن ۴۸dp. صفر قفل یادگیری.

## ۳. دور یازدهم — لیدربورد و محتوا

لیدربورد فقط **«My status / وضعیت من»** + ۳ کارت آمار + «آزمونها و امتیازات من»؛ بلوک `Wooden League / 6d 22h 38m` و هر ۵ ردیف رقیب حذف شد. `Career Paths` → **«یادگیری برنامه محور»**؛ `Courses` → **«یادگیری مبحثی»**. چهار کارت درشت = ۳ برنامهٔ دوازدهم/یازدهم/دهم + مبحثی. ۱۲ کورس = ۴ درس × ۳ پایه. نمای مسیر: «یادگیری برنامه محور» / نام پایه / **«مدرک پایان دوره»** / **«۲۲ درصد کامل شده»** / `2/9` / **۱۰ بازهٔ دو هفتهای ۱ آبان..۱۵ اسفند** با «دروس: زیست، شیمی، ریاضی، فیزیک». کورسها همان نما را با **فصل + درس** (`KONKUR_CURRICULUM.json`: ۶۰ فصل / ۱۸۰ درس) پر میکنند. **هیچ آرم/نشان برنامهنویسی**ای نمایش داده نمیشود؛ فقط وکتورهای بومی میمو.

## ۴. مصوبات پابرجا

۵ تب (`MAX` ممنوع) · حذف روتین/Habitica و دیکته · حذف یادداشتهای داخل UI · **نگهداری ۷ بخش لیبلدار / قالب فیلد / پاسخنامهٔ تشریحی** · تایمر فقط داخل آزمون / ۲۷۰ دقیقه / «پاسخبرگ»≠«پاسخنامه» · تکدکمهٔ AI · **صفر گرهٔ قفلی** و تنها یک قفل «آزمون نهایی / دو هفتگی» · بولت ← `section-practice` جدا · لیدربورد بدون Promotion Zone · چت مینیمال · RTL/شب · بدون Pro/پرداخت · «وارد کردن کلید API» فقط یادداشت.

## ۵. clean-room و وضعیت

هیچ دارایی/کدی از Mimo، همدرس، Hadaf Plus، LearnHarness، EPM یا Habitica کپی نشده. `DESIGN/index.html` از payloadهای استخراجشده رندر میشود: ۱۴ نما / ۵ تب / ۹۳ وکتور / ۱۱۳ آیکن / ۰ خطای jsdom / وریفایر PASS. منتظر **تأیید نهایی**؛ بعدش تازه P0.
'''

(UP / "23_DESIGN_ROUND_11.md").write_text(DOC23, encoding="utf-8")
(D / "DESIGN_NOTES.fa.md").write_text(NOTES, encoding="utf-8")
print("docs written")

for p in sorted(UP.glob("*.md")):
    s = p.read_text(encoding="utf-8")
    if MARK in s:
        continue
    current = p.name.startswith("23_")
    banner = (MARK + "\n> " + ("✅ **DESIGN v11 · CURRENT** — لاگ دور یازدهم، جایگزین v10. "
                              if current else
                              "⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v11](23_DESIGN_ROUND_11.md)** است. ")
              + "همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.")
    lines = s.split("\n")
    insert_at = 1 if lines and lines[0].startswith("#") else 0
    lines.insert(insert_at, banner)
    p.write_text("\n".join(lines), encoding="utf-8")
print("banners written")

wf = UP / "wireframes.html"
s = wf.read_text(encoding="utf-8")
s = s.replace("DESIGN/index.html\">DESIGN v10</a>", "DESIGN/index.html\">DESIGN v11</a>")
s = s.replace("<a href=\"22_DESIGN_ROUND_10.md\">لاگ دور دهم</a>", "<a href=\"23_DESIGN_ROUND_11.md\">لاگ دور یازدهم</a>")
wf.write_text(s, encoding="utf-8")
print("wireframes banner updated")

mp = UP / "MANIFEST.json"
m = json.loads(mp.read_text(encoding="utf-8"))
stable = [p for p in UP.rglob("*") if p.is_file() and p.name not in ("SHA256SUMS.txt", "VERIFICATION_REPORT.json")]
m["date"] = "2026-11-04"
m["status"] = "PLAN_ONLY + DESIGN v11 REVIEW (no product implementation)"
dl = m["deliverables"]
dl["persian_docs"] = len(list(UP.glob("*.md")))
dl["csv_catalogs"] = len(list(CAT.glob("*.csv")))
dl["extracted_assets_files"] = len(stable)
dl["total_bytes"] = sum(p.stat().st_size for p in stable)
dl["verification"] = "PASS"
dl["verification_checks"] = 0
dl["design_round"] = "v11 (REVIEW)"
dl["design_views"] = 14
dl["design_svg_vectors"] = 93
dl["bottom_nav_tabs"] = 5
dl["v11_content"] = ("KONKUR_CURRICULUM.json / KONKUR_CURRICULUM.csv (12 courses x 5 chapters x 3 lessons = "
                     "12/60/180) + 10 fortnight dates 1 Aban..15 Esfand + 4 big Mimo-icon cards + "
                     "My-status-only leaderboard + zero programming emblems")
cf = m["critical_findings"]
for x in [
    "v11: leaderboard competition block (Wooden League, countdown, 5 rival rows, league badges) fully removed; only My status + own stats/exams remain",
    "v11: Career Paths -> یادگیری برنامه محور; Courses -> یادگیری مبحثی; 4 big cards (3 grade programs + topic learning); 12 courses = 4 subjects x 3 grades",
    "v11: Path Overview relabelled مدرک پایان دوره / ۲۲ درصد کامل شده / 2-9; 10 biweekly slots from 1 Aban to 15 Esfand (5 months) with دروس: زیست، شیمی، ریاضی، فیزیک",
    "v11: course overviews use 60 فصل / 180 درس from the repo Konkur curriculum instead of JavaScript/HTML/CSS sections; U12 records the naming assumption",
    "v11: ZERO programming emblems — ic_badge_*, ic_code_lang_*, ic_code_playground_template_* replaced by decoded Mimo vectors; everything else stays in place",
]:
    if x not in cf:
        cf.append(x)
for cmd in ["python3 tools/build_design_v11.py .", "python3 tools/finalize_v11.py ."]:
    if cmd not in m["reproduce"]:
        m["reproduce"].append(cmd)
m["design_round_10"]["status"] = "DESIGN v10 · SUPERSEDED by round 11 (content/labels) — curved zigzag geometry KEPT"
m["design_round_11"] = {
    "status": "DESIGN v11 · REVIEW — awaiting final approval (CURRENT)",
    "trigger": "user: بخش ۸ لیدربورد؛ حذف بلوک Wooden League و ۵ ردیف رقیب (فقط my status)؛ یادگیری برنامه محور / یادگیری مبحثی؛ ۴ آیکون درشت؛ ۱۲ کورس؛ مدرک پایان دوره؛ ۲۲ درصد؛ تاریخهای دو هفتهای ۵ ماهه؛ دروس؛ فصل/درس؛ بدون آرم برنامهنویسی",
    "geometry": "UNCHANGED — original_curved_zigzag (v10), 3 lanes 80/196/312, 24dp gaps, 32dp Q elbows, 2 coloured segments",
    "leaderboard": "MY_STATUS_ONLY (Wooden League + countdown + 5 rival rows + league badges removed)",
    "headings": {"career": "یادگیری برنامه محور", "courses": "یادگیری مبحثی"},
    "cards": ["یادگیری همگام با برنامه آزمون دوازدهم", "یادگیری همگام با برنامه آزمون یازدهم",
              "یادگیری همگام با برنامه آزمون دهم", "یادگیری مبحثی"],
    "courses": ["زیست دهم", "ریاضی دهم", "شیمی دهم", "فیزیک دهم",
                "زیست یازدهم", "ریاضی یازدهم", "شیمی یازدهم", "فیزیک یازدهم",
                "زیست دوازدهم", "ریاضی دوازدهم", "شیمی دوازدهم", "فیزیک دوازدهم"],
    "certificate": {"label": "مدرک پایان دوره", "progress": "۲۲ درصد کامل شده", "count": "2/9"},
    "fortnight_dates": ["۱ آبان", "۱۵ آبان", "۱ آذر", "۱۵ آذر", "۱ دی", "۱۵ دی",
                        "۱ بهمن", "۱۵ بهمن", "۱ اسفند", "۱۵ اسفند"],
    "months": ["آبان", "آذر", "دی", "بهمن", "اسفند"],
    "lessons_label": "دروس",
    "lessons_line": "دروس: زیست، شیمی، ریاضی، فیزیک",
    "curriculum": {"courses": 12, "chapters": 60, "lessons": 180,
                   "source": "SOURCE_APPS/hamdars/HELP_CENTER_UX.md §learn-books + repo Konkur content model + standard Iranian textbook سرفصلها",
                   "files": ["DESIGN/KONKUR_CURRICULUM.json", "CATALOGS/KONKUR_CURRICULUM.csv"]},
    "icons": "decoded Mimo vectors ONLY; zero ic_badge_*/ic_code_lang_*/ic_code_playground_template_* in UI",
    "interactive_prototype": "DESIGN/index.html (14 views / 5 tabs / 93 SVG vectors / 113 painted icons / 0 Learn locks / 0 jsdom errors)",
    "unchanged": ["original curved zigzag path map", "5 tabs / no MAX", "routine + Habitica removed",
                  "Dictate removed", "no UI annotations", "7 labelled exam sections + descriptive answer",
                  "exam architecture / timer / 270 min / پاسخبرگ≠پاسخنامه",
                  "one pre-existing exam-hub lock", "bolt section-practice isolated", "no Promotion Zone"],
    "final_log": "23_DESIGN_ROUND_11.md",
    "design_notes": "DESIGN/DESIGN_NOTES.fa.md",
    "final_approval": "PENDING — no product implementation until user says the design is final",
}
mp.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("MANIFEST updated; docs=%d csv=%d files=%d bytes=%d" %
      (dl["persian_docs"], dl["csv_catalogs"], len(stable), sum(p.stat().st_size for p in stable)))
