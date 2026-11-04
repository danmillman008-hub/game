#!/usr/bin/env python3
# ARCHIVED (round 9): superseded by extract_mimo_nodes_v9.py / build_design_v9.py / finalize_v9.py.
# -*- coding: utf-8 -*-
"""finalize_v8.py — v8 catalogs, docs, banners, clean-up and MANIFEST.

Round 8: remove «روتین روزانه» / Habitica idea completely, remove Dictate,
remove UI annotation notes, ban all locked nodes except the one existing exam
card, rebuild Learn nodes from code, Mimo-ify exam appearance.
Idempotent.
"""
from __future__ import annotations
import csv
import json
from pathlib import Path

UP = Path(__file__).resolve().parents[1]
CAT = UP / "CATALOGS"
D = UP / "DESIGN"
MARK = "<!-- v8-banner -->"

# --------------------------------------------------------------------------
# 1. append v8 rows (idempotent by id)
# --------------------------------------------------------------------------
APPEND = {
    "DESIGN_FEEDBACK.csv": ("F-45", [
        ["F-45", "روتین روزانه رو کلا حدف کن به درد نیمخوره / از منو و کلا ایدهاش اشتباه بود", "تب ششم، صفحهٔ routine، JSON/کاتالوگ/سند Habitica و ابزارش بهطور کامل حذف شد؛ ناوبری ۵ تب برگشت", "20_DESIGN_ROUND_8.md §۱, DESIGN/index.html", "APPLIED"],
        ["F-46", "گزینه دیکته یا دیکتیت رو از دستیار هوشمند حدف کن", "دکمهٔ Dictate و آیکون میکروفن از خط پایین چت حذف شد؛ TEACH/PRACTICE/model/medium همان یک خط ماند", "DESIGN/index.html, CATALOGS/AI_PANEL_SPEC.csv", "APPLIED"],
        ["F-47", "توضیحات سیاست / EPM / تایمر داخل بخش آزمونها نیاز نیست", "سه بلوک quoted حذف شد؛ policyHint خالی و hidden ماند و JS دیگر چیزی در آن نمینویسد", "DESIGN/index.html#exam-run", "APPLIED"],
        ["F-48", "این توضیحات داخل یو ای نباشه؛ بقیه بخشها هم گاها دیده میشه از دستت در رفته", "همهٔ note/hint/sd-note/composer-note، چیپهای codechip، برچسبهای .lh و تولتیپهای title از صفحات گوشی پاک شدند؛ شواهد به data-code/data-lh نامرئی و کاتالوگها رفت", "DESIGN/index.html, CATALOGS/MIMO_PATH_NODES.csv", "APPLIED"],
        ["F-49", "اون توضحاتی که در بخش ازمونها هست رو میتونی نگه داری", "۷ بخش لیبلدار + قالب فیلد cat-meta + پاسخنامهٔ تشریحی و متن تحلیل دستنخورده نگه داشته شد", "DESIGN/index.html#exam-hub", "APPLIED"],
        ["F-50", "هیچ بخش قفلی نیاز نیست جز یکی مربوط به آزمون دو هفتگی که الانشم هست", "گرهٔ قفل، بولت قفل، ردیفهای locked داخل مبحث و toast قفل حذف شدند؛ تنها قفل همان کارت «آزمون نهایی / دو هفتگی» بخش ۶ هاب آزمونهاست", "DESIGN/NODE_CODE_GEOMETRY.json::nodeGeometry.lock_policy", "APPLIED"],
        ["F-51", "نودها رو واقعا خیلی خیلی خیلی وقت بزاری و درست دربیاری (اصلیترین تسک)", "استخراج عمیق v8: ۵۸ وکتور، ۱۰ شِیپ، ۹۰ رشتهٔ ARSC، ۹۲ کلاس PathMap DEX؛ هندسهٔ ماشینی ۹۲dp/۲۶dp/لبهٔ ۸dp/اتور Q/حلقهٔ ½/کتاب شناور؛ ۶ گره بدون قفل", "DESIGN/NODE_CODE_GEOMETRY.json, CATALOGS/MIMO_PATH_NODES.csv (72 ردیف), 20_DESIGN_ROUND_8.md §۵", "APPLIED"],
        ["F-52", "چهارچوب آزمونها عالیه؛ فقط ظاهرش شبیهتر به میمو باشه (آیکون/رنگ)", "◇⏱✓🔒→ جایگزین وکتورهای واقعی میمو شدند؛ رنگ/شعاع/تایپوگرافی ARSC اعمال شد؛ هیچ تغییری در معماری، تایمر، پاسخبرگ یا ۲۷۰ دقیقه ایجاد نشد", "DESIGN/index.html, CATALOGS/MIMO_PATH_NODES.csv (V8-10..18)", "APPLIED"],
    ]),
    "SCOPE_DECISIONS.csv": ("D27", [
        ["D27", "روتین روزانه / Habitica", "REMOVED_ENTIRELY_V8", "تب، صفحه، payload، JSON، کاتالوگها، سند و ابزار امتیازدهی حذف؛ ایده باطل شد", "بازخورد v8 «کلا حدف کن … ایدهاش اشتباه بود»", "20_DESIGN_ROUND_8.md §۱"],
        ["D28", "ناوبری پایین", "FIVE_TABS_RESTORED", "Learn/Practice/AI/Leaderboard/Profile؛ MAX ممنوع", "بازخورد v8", "DESIGN/index.html#tabs"],
        ["D29", "چت AI", "DICTATE_REMOVED", "Dictate حذف؛ ۷ توانایی LH دیگر پشت data-lh باقیاند", "بازخورد v8", "CATALOGS/AI_PANEL_SPEC.csv"],
        ["D30", "یادداشتهای داخل UI", "NO_ANNOTATIONS_IN_UI", "شواهد فقط در data-code/data-lh/کاتالوگها؛ توضیحات محصول هاب آزمونها و پاسخنامه نگه داشته شد", "بازخورد v8", "DESIGN/index.html"],
        ["D31", "قفلها", "ONE_LOCK_ONLY", "فقط قفل موجود «آزمون نهایی / دو هفتگی» در هاب آزمونها؛ هیچ گره/ردیف قفلی در یادگیری", "بازخورد v8", "DESIGN/NODE_CODE_GEOMETRY.json::nodeGeometry.lock_policy"],
        ["D32", "گرهها / ظاهر آزمون", "NODE_CODE_FIRST_V8 + EXAM_SKIN_ONLY", "گرهها data-driven از NODE_CODE_GEOMETRY.json؛ آزمونها فقط پوسته (آیکون/رنگ/شعاع) عوض کردند", "بازخورد v8 «اصلیترین تسک تو درست کردن بخش نود هاست»", "tools/extract_mimo_nodes_v8.py, tools/build_design_v8.py"],
    ]),
    "UI_FIDELITY_RULES.csv": ("F24", [
        ["F24", "گرهها ماشینی و دقیق", "nodeGeometry در NODE_CODE_GEOMETRY.json؛ ۶ گره؛ ۲ مسیر اتور Q؛ بدون قفل/START/چیپ دیباگ", "DESIGN/NODE_CODE_GEOMETRY.json + mimo-01/02/10 (VISUAL_CROSSCHECK_ONLY)"],
        ["F25", "فقط یک قفل", "قفل منحصراً کارت «آزمون نهایی / دو هفتگی» بخش ۶ هاب؛ هیچ locked در Learn/section-detail/practice", "بازخورد v8 + D31"],
        ["F26", "هیچ یادداشت توضیحی داخل گوشی", "visible .hint/.note/.sd-note/.lh/codechip/title = ۰؛ policyHint خالی و hidden", "بازخورد v8 + D30"],
        ["F27", "آزمونها: پوسته میمو، معماری ثابت", "وکتورها/رنگها/شعاعهای ARSC؛ ۷ بخش، تایمر، پاسخبرگ≠پاسخنامه، ۲۷۰ دقیقه بدون تغییر", "بازخورد v8 + D32"],
    ]),
    "AI_PANEL_SPEC.csv": ("ai_foot_no_dictate", [
        ["ai_foot_no_dictate", "Dictate / دیکته بهطور کامل حذف شد؛ جای آن خالی نماند", "REMOVED (v8)", "بازخورد صریح دور هشتم"],
        ["ai_foot_single_line_v8", "TEACH / PRACTICE ریز + gemini-flash-lite-latest + medium در یک خط؛ بدون دیکته", "VISIBLE (ai composer foot)", "Mimo ic_chevron_down.xml"],
    ]),
    "OPEN_QUESTIONS.csv": ("U08", [
        ["U08", "منظور از «آزمون دو هفتگی مشخص» دقیقاً کدام کارت هاب آزمونهاست؟", "ASSUMED: همان کارت قفلدار «آزمون نهایی» در بخش ۶ (جمع بندی و دوره)، که از قبل وجود داشت و دستنخورده ماند", "no", "تأیید نهایی دیزاین"],
        ["U09", "آیا نشانهای لیگ بستهٔ لیدربورد هم «بخش قفلی» محسوب میشوند؟", "ASSUMED: خیر؛ آن badges بومی خود میمو هستند و قفل مسیر یادگیری نیستند", "no", "تأیید نهایی دیزاین"],
    ]),
}

for name, (first_id, new_rows) in APPEND.items():
    p = CAT / name
    with p.open(encoding="utf-8", newline="") as f:
        existing = list(csv.reader(f))
    header, body = existing[0], existing[1:]
    present = {r[0] for r in body if r}
    todo = [r for r in new_rows if r[0] not in present]
    if todo:
        with p.open("a", encoding="utf-8", newline="") as f:
            csv.writer(f).writerows(todo)
    print(name, "+", len(todo), "->", len(body) + len(todo))

# ---- update the archived Dictate row + resolved U06 in place ----
def rewrite_row(path, key, newrow):
    p = CAT / path
    with p.open(encoding="utf-8", newline="") as f:
        rs = list(csv.reader(f))
    for i, r in enumerate(rs):
        if r and r[0] == key:
            rs[i] = newrow
            break
    with p.open("w", encoding="utf-8", newline="") as f:
        csv.writer(f).writerows(rs)


rewrite_row("AI_PANEL_SPEC.csv", "ai_foot_dictate_voice",
            ["ai_foot_dictate_voice", "Dictate / دیکته (ویس) — در دور هشتم به دستور کاربر حذف شد", "REMOVED (v8)", "بازخورد صریح دور هشتم"])
rewrite_row("OPEN_QUESTIONS.csv", "U06",
            ["U06", "آیا «روتین روزانه» تب ششم مستقل است یا داخل پروفایل؟", "RESOLVED v8: کل ایده و تب حذف شد؛ پنج تب میمو برگشت", "no", "بسته شد"])

# ---- PRACTICE_VS_EXAM.csv rewritten as a 2-way isolation table (no routine) ----
PVE = [
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
    ("PV-11", "locks", "no locked node in practice or Learn", "exactly ONE lock: the existing biweekly/final exam card in section ۶", "round-8 one-lock rule"),
    ("PV-12", "code evidence", "PathMapScreenKt / SmartPractice* / ic_bolt* / rc_checkpoint_window_*", "Konkur plan catalogs (design-only, no Mimo code)", "code-first vs plan-first"),
]
with (CAT / "PRACTICE_VS_EXAM.csv").open("w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["row_id", "aspect", "learn_bolt_practice", "konkur_exam", "isolation_rule"])
    w.writerows(PVE)
print("PRACTICE_VS_EXAM.csv rewritten ->", len(PVE), "rows (routine removed)")

# --------------------------------------------------------------------------
# 2. delete the Habitica / Daily-Routine idea artifacts
# --------------------------------------------------------------------------
DELETE = ["19_HABITICA_ROUTINE_SPEC.md",
          "DESIGN/HABITICA_SCORING.json",
          "CATALOGS/HABITICA_SOURCES.csv",
          "CATALOGS/HABITICA_SCORING.csv",
          "tools/write_habitica_spec.py"]
for rel in DELETE:
    p = UP / rel
    if p.exists():
        p.unlink()
        print("deleted", rel)

# --------------------------------------------------------------------------
# 3. docs
# --------------------------------------------------------------------------
DOC20 = r'''# دور هشتم طراحی — DESIGN v8 (گرهها، حذف روتین، پاکسازی UI)

> **وضعیت:** `DESIGN v8 · REVIEW` — منتظر تأیید نهایی. همچنان **فقط پلن/دیزاین**؛ هیچ کد محصولی نوشته نشده.
> **گفتۀ شما:** «روتین روزانه رو کلا حدف کن … اصلیترین تسک تو درست کردن بخش نود هاست در بخش یادگیری».
> **روش:** کندوکاو عمیقتر از داخل کد APK؛ اسکرینشاتها فقط **چک بصری**. جایگزین `18_DESIGN_ROUND_7.md` است.

---

## ۱. حذف کامل «روتین روزانه» و ایدهٔ امتیازدهی

تب ششم، صفحهٔ `data-screen=routine`، `var HAB`، `DESIGN/HABITICA_SCORING.json`، چهار کاتالوگ/سند مربوط و ابزار تولیدش **همگی حذف شدند**. ناوبری دوباره **۵ تب** `Learn / Practice / AI / Leaderboard / Profile` است؛ `MAX` همچنان ممنوع. هیچ قاعده، فرمول، SHA-256 یا ارجاعی به Habitica در تحویل فعلی باقی نماند. تصمیم: `D27`.

## ۲. حذف «دیکته» و پاکسازی یادداشتها

- دکمهٔ «دیکته / Dictate» و آیکون میکروفن از خط پایین دستیار هوشمند حذف شد. «آموزش / TEACH»، «تمرین / PRACTICE»، `gemini-flash-lite-latest` و `medium` در **همان یک خط** ماندند (`D29`).
- سه بلوکی که دقیقاً نقل کردید (سیاست زمان خالص، ایدهٔ جزیی EPM، توضیح تایمر معکوس) از صفحهٔ اجرای آزمون حذف شدند. `policyHint` خالی و `hidden` باقی ماند و جاوااسکریپت دیگر هیچ متنی در آن نمینویسد؛ سیاست پاسخبرگ/پاسخنامه همچنان در منطق اعمال میشود.
- «از دستت در رفته»ها هم پاک شدند: یادداشتهای `note/hint/sd-note/composer-note`، چیپهای `codechip2`، برچسبهای کوچک `.lh` و تمام تولتیپهای `title=` از **داخل گوشی** حذف شدند. شواهد بهصورت `data-code` / `data-lh` نامرئی و در کاتالوگها نگهداری میشوند (`D30`).
- بنا به دستور «اون توضحاتی که در بخش آزمونها هست رو میتونی نگه داری»، **۷ بخش لیبلدار + قالب فیلد `cat-meta`** هاب و **پاسخنامهٔ تشریحی/تحلیل** دستنخورده نگه داشته شدند. متنهای کوتاه کاربردی داخل sheets (مثلاً «پاسخهای تا این لحظه ذخیره میشوند») هم ماندند.

## ۳. فقط یک قفل

هیچ گرهٔ قفلی، بولت قفل، ردیف `locked` داخل مبحث یا toast «بخش قفل است» وجود ندارد. تنها قفل مجاز همان **کارت «آزمون نهایی / دو هفتگی» در بخش ۶ هاب آزمونهاست** که از قبل در دیزاین بود و هیچ چیزی به آن اضافه نشد (`D31`). نشانهای لیگ بستهٔ لیدربورد المان بومی خود میمو هستند، نه بخش قفلی مسیر یادگیری.

## ۴. ظاهر آزمونها: میموتر، بدون تغییر معماری

جای `◇ / ⏱ / ✓ / 🔒 / → / ؟` رفتند **وکتورهای واقعی میمو**: `ic_trophy`، `ic_clock_black_24dp`، `ic_task_completed`، `ic_lock_alt_02`، `ic_file`، `ic_target`، `ic_sparks_alt`، `ic_arrow_back_24`، `ic_help`. رنگها، شعاعها و تایپوگرافی از جداول ARSC (`card`, `card-pressed`, `primary`, `line_secondary`، شعاع ۱۲/۱۶/۲۰dp، `toolbar 56dp`، `TextH2/TextLabel1`). چیپها، `nodek`، `cat-meta`، گزینهها و نوارها فقط **پوسته** عوض کردند.

**تغییر معماری: صفر.** هفت بخش، تایمر فقط داخل آزمون (کلیک ← عدد ← شروع ← معکوس، توقف/ادامه، ثبت خودکار صفر)، جامع ۲۷۰ دقیقهٔ ثابت، «پاسخبرگ» ≠ «پاسخنامه»، بازشدن خودکار کلید در زمان خالص، دو دکمهٔ تمیز قبل/بعد، تکدکمهٔ «توضیح با هوش مصنوعی» و لیدربورد بدون Promotion Zone همگی دستنخوردهاند (`D32`).

## ۵. اصلیترین تسک: بازسازی واقعی گرهها

ابزار تازه `tools/extract_mimo_nodes_v8.py` → `DESIGN/NODE_CODE_GEOMETRY.json` (۱۱۵٬۲۱۷ بایت) + `CATALOGS/MIMO_PATH_NODES.csv` (**۷۲ ردیف**). شمارش: ۵۸ وکتور `pathData`، ۱۰ شِیپ AXML، ۹۰ رشتهٔ ARSC، ۱۸ رنگ، ۱۵ دایمنشن، ۸ استایل، **۹۲ کلاس DEX مسیر** (`PathMapScreenKt`, `PathMapViewModel$onTutorialClick`, `GetPathMapState/Dialogs`, `PathToolbarButtonType`, `PracticeOptionalIntroKt`, `TutorialSpotlightKt`, `ViewsKt$PathMap`, `ModalData$SmartPractice*`)، ۱۵ فصل / ۲۲۳ `tutorialId`.

| ویژگی | مقدار | منبع |
|---|---|---|
| اندازهٔ گره | ۹۲dp، شعاع ۲۶dp | `cardview_corner_radius_large` + `glance_component_square_icon_button_corners` |
| لبهٔ سهبعدی | ۸dp، `button_primary_highlight #FF6E3EC8` | ARSC |
| گرادیان انجامشده | `progress_chapter_primary #FF8D60E2 → button_primary #FF7E4BDE` | ARSC |
| تیک | `ic_check_white` سفید ۴۴dp | `res/drawable/ic_check_white.xml` |
| گرهٔ فعلی | کارت سفید + ۳dp کادر بنفش + ۷dp فاصله + ۳dp حلقهٔ بیرونی + ۲dp خط داخلی | `glance_circular_progress_indicator.xml` |
| حلقهٔ ½ | دایرهٔ ۶۰dp، ضخامت ۸dp، کمان ۵۵٪، برچسب `1/2` | همان + mimo-02 |
| نسخهٔ پلی | `ic_play #FF252746` | `res/drawable/ic_play.xml` + mimo-01 |
| بولت فعال | `ic_flash` سرمهای روی بنفش با لبهٔ ۳بعدی | `res/drawable/ic_flash.xml` + mimo-10 |
| بولت اختیاری | `ic_bolt` سفید روی `card_disabled` | mimo-01/02 |
| اتور | stroke ۱۰dp، **گوشههای گرد Q شعاع ۳۲dp** (راست/پایین/چپ/پایین)، بخش انجامشده بنفش و بخش آینده یاسی | `progress_chapter_primary` / `progress_chapter_background` |
| پسزمینه | نقطهچین ۱٫۶dp / فاصله ۲۶dp | `line_secondary` |
| شناور | دایرهٔ کتاب/واژهنامه با A | `ic_file.xml` + `bookmark_no_fill.xml` + mimo-01/02 |

شش گره (`l8n1…l8n6`) و دو مسیر اتور **مستقیماً از `nodeGeometry` داخل JSON رندر میشوند**، نه با جایگذاری دستی. حالت گرهٔ فعلی (½ / پلی) با دو دکمه در **پنل بازبینی بیرون گوشی** قابل نمایش است، پس داخل UI محصول چیز اضافهای نیامد. حذفشدها: گرهٔ قفل، بولت قفل، برچسب START، حلقهٔ ۱۲٪ سرگردان، نقطهٔ خاکستری و چیپهای دیباگ. کد ملاک است؛ `mimo-01` / `mimo-02` / `mimo-10` فقط `VISUAL_CROSSCHECK_ONLY`اند. ۰ رنگ/فونت/شعاع/آیکون تازه.

## ۶. حفظشده

گره رعدوبرق ← «تمرین مبحث تا همان فصل» (`data-screen=section-practice`، جدا از هاب آزمون، بدون تایمر/پاسخبرگ/پاسخنامه) · سهخط → Select Path · کارت → Path Overview · داخل مبحث → بخشها · دیالوگ Fully charged / mastered · لیدربورد اطلاعات خود فرد · چت مینیمال + تاریخچه + «اضافه کردن فایل» / «زنجیره گفت و گو» · مشاوره `PARKED` · بدون Pro/پرداخت/MAX · صفحهٔ ورود حذفشده · RTL/فارسی + حالت شب · ۱۴ اسکرینشات فقط چک بصری.

## ۷. اعتبارسنجی و وضعیت

`tools/verify_upgrade.py` → PASS؛ `node --check` OK؛ jsdom **۰ خطا / ۴۶ تست جریان**؛ ۱۴ نما، ۵ تب، ۹۳ وکتور SVG، ۱۳۳/۱۳۳ آیکن رنگشده، ۶ گره، ۰ قفل یادگیری، ۰ یادداشت توضیحی داخل UI. **DESIGN v7** بایگانی شد. همچنان **فقط پلن/دیزاین**؛ بعد از تأیید نهایی شما تازه P0 پیادهمسازی شروع میشود.
'''

NOTES = r'''# یادداشتهای طراحی — DESIGN v8

> نسخهٔ جاری: **DESIGN v8 · REVIEW** (منتظر تأیید نهایی). نسخههای **DESIGN v6** و **DESIGN v7** بایگانی حسابرسیاند. همچنان **فقط پلن/دیزاین**؛ هیچ کد محصولی نوشته نشده است.

## ۱. اصل حاکم

بازآفرینی ۱۰۰٪ بخشهای اصلی میمو **از داخل کد و مهندسی معکوس**، نه از روی عکس. منابع: `CATALOGS/DESIGN_TOKENS.json` (ARSC)، `SOURCE/values/values/string.xml`، `SOURCE/res/drawable/*.xml` (`android:pathData` و شِیپها)، `SOURCE/res/layout/*.xml`، `SOURCE/dex/UI_CLASSES.json`، `test-tracks.json`. ۱۴ اسکرینشات فقط `VISUAL_CROSSCHECK_ONLY`اند. فقط **نام درسها/فصلها/مباحث** کنکوری میشود؛ ۰ رنگ/فونت/شعاع/آیکون تازه.

## ۲. اصلیترین کار دور هشتم: گرهها

`tools/extract_mimo_nodes_v8.py` → `DESIGN/NODE_CODE_GEOMETRY.json` + `CATALOGS/MIMO_PATH_NODES.csv` (۷۲ ردیف). هندسهٔ ماشینی: مربع ۹۲dp / شعاع ۲۶dp / لبهٔ سهبعدی ۸dp (`button_primary_highlight`) / گرادیان بنفش ARSC / تیک `ic_check_white` / کارت سفید حلقهدار فعلی با حلقهٔ ½ (و نسخهٔ `ic_play`) / بولت فعال `ic_flash` و بولت اختیاری `ic_bolt` / اتور **گردگوشهٔ Q** (نه بزیه) / نقطهچین ۲۶dp / کتاب شناور. شش گره و دو مسیر اتور مستقیماً از `nodeGeometry` رندر میشوند. **هیچ گرهٔ قفلی** وجود ندارد؛ تنها قفل همان کارت «آزمون نهایی / دو هفتگی» موجود در هاب آزمونهاست. برچسب START، حلقهٔ ۱۲٪ سرگردان، نقطهٔ خاکستری و چیپهای دیباگ حذف شدند.

## ۳. حذفشدهها (دستور صریح دور هشتم)

- **روتین روزانه** و **کل ایدهٔ امتیازدهی Habitica**: تب، صفحه، payload، JSON، کاتالوگها، سند و ابزارش. ناوبری ۵ تب برگشت؛ `MAX` ممنوع.
- **دیکته / Dictate** از خط پایین دستیار هوشمند.
- **یادداشتهای توضیحی داخل UI**: سیاست زمان خالص، ایدهٔ EPM، توضیح تایمر، `note/hint/sd-note/composer-note`، `codechip`، برچسبهای `.lh`، تولتیپهای `title`. شواهد به `data-code` / `data-lh` نامرئی و کاتالوگها منتقل شدند.
- توضیحات **۷ بخش لیبلدار / قالب فیلد** هاب آزمونها و **پاسخنامهٔ تشریحی** بنا به دستور شما **نگه داشته شدند**.

## ۴. ظاهر آزمونها (فقط پوسته)

وکتورهای واقعی میمو جای گلیفها: `ic_trophy`, `ic_clock_black_24dp`, `ic_task_completed`, `ic_lock_alt_02`, `ic_file`, `ic_target`, `ic_sparks_alt`, `ic_arrow_back_24`, `ic_help`. رنگ/شعاع/تایپوگرافی ARSC. **هیچ تغییر معماری**: ۷ بخش، تایمر فقط داخل آزمون، ۲۷۰ دقیقهٔ ثابت، «پاسخبرگ» ≠ «پاسخنامه»، کلید خودکار در پایان، دو دکمهٔ تمیز قبل/بعد، تکدکمهٔ «توضیح با هوش مصنوعی»، لیدربورد بدون Promotion Zone.

## ۵. تفکیک (مهم)

| سطح | جا | نشانه |
|---|---|---|
| تمرین مبحث | `data-screen=section-practice` | `mimo`، بدون تایمر/پاسخبرگ/پاسخنامه/POLICY |
| آزمون کنکور | `exam-hub / exam-run / exam-result` | `konkur`، ۷ بخش، تایمر داخل آزمون، پاسخبرگ ≠ پاسخنامه |
| قفل | فقط یک کارت در هاب آزمونها | «آزمون نهایی / دو هفتگی» |

## ۶. حقوقی / clean-room

هیچ دارایی، فونت، رشته یا کدی از Mimo 9.35، Hamdars 7.4.4، Hadaf Plus 2.0.2، LearnHarness یا EPM کپی نشده است. ایدهٔ Habitica بهکل حذف شد. subscription/cart/Pro و اسکرینشات رانتایم/امولاتور ممنوعاند.

## ۷. شواهد و اعتبارسنجی

`DESIGN/CODE_GEOMETRY.json` + `DESIGN/LEARN_CODE_GEOMETRY.json` + `DESIGN/NODE_CODE_GEOMETRY.json` → `tools/build_design_v8.py` → `DESIGN/index.html`. خروجی: ۱۴ نما، ۵ تب، ۹۳ وکتور SVG، ۱۳۳ آیکن رنگشده، ۰ خطای jsdom، `node --check` OK. `tools/verify_upgrade.py` و `CATALOGS/VERIFICATION_REPORT.json` حسابرسی نهاییاند.

## ۸. بعد از این

منتظر **تأیید نهایی** شما. فقط بعد از «مرحلهٔ بعد» پیادهمسازی P0 آغاز میشود؛ تا آن لحظه هیچ کد محصولی نوشته نشده است.
'''

(UP / "20_DESIGN_ROUND_8.md").write_text(DOC20, encoding="utf-8")
(D / "DESIGN_NOTES.fa.md").write_text(NOTES, encoding="utf-8")
print("docs written")

# --------------------------------------------------------------------------
# 4. banners
# --------------------------------------------------------------------------
for p in sorted(UP.glob("*.md")):
    s = p.read_text(encoding="utf-8")
    if MARK in s:
        continue
    current = p.name.startswith("20_")
    banner = (MARK + "\n> " + ("✅ **DESIGN v8 · CURRENT** — لاگ دور هفتم/ششم بایگانی شد. "
                              if current else
                              "⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v8](20_DESIGN_ROUND_8.md)** است. ")
              + "همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.")
    lines = s.split("\n")
    insert_at = 1 if lines and lines[0].startswith("#") else 0
    lines.insert(insert_at, banner)
    p.write_text("\n".join(lines), encoding="utf-8")
print("banners written")

wf = UP / "wireframes.html"
s = wf.read_text(encoding="utf-8")
old = '''<div style="background:#FFF7E6;border:2px solid #7E4BDE;color:#252746;padding:12px 18px;font:700 14px Tahoma,sans-serif;text-align:center">⚠️ وایرفریم v1 بایگانی شد — طراحی فعلی <a href="DESIGN/index.html">DESIGN v7</a> است (گرههای دقیق، تمرین مبحث جدا از آزمون، روتین روزانه). <a href="18_DESIGN_ROUND_7.md">لاگ دور هفتم</a></div>'''
new = '''<div style="background:#FFF7E6;border:2px solid #7E4BDE;color:#252746;padding:12px 18px;font:700 14px Tahoma,sans-serif;text-align:center">⚠️ وایرفریم v1 بایگانی شد — طراحی فعلی <a href="DESIGN/index.html">DESIGN v8</a> است (گرههای دقیق از کد، حذف روتین روزانه، حذف دیکته، پاکسازی توضیحات، پوستهٔ میمویی آزمونها). <a href="20_DESIGN_ROUND_8.md">لاگ دور هشتم</a></div>'''
if old in s:
    wf.write_text(s.replace(old, new, 1), encoding="utf-8")
    print("wireframes banner updated")
elif "DESIGN v8" not in s:
    raise SystemExit("wireframes banner anchor not found")

# --------------------------------------------------------------------------
# 5. MANIFEST
# --------------------------------------------------------------------------
mp = UP / "MANIFEST.json"
m = json.loads(mp.read_text(encoding="utf-8"))
stable = [p for p in UP.rglob("*") if p.is_file() and p.name not in
          ("SHA256SUMS.txt", "VERIFICATION_REPORT.json")]
m["date"] = "2026-11-04"
m["status"] = "PLAN_ONLY + DESIGN v8 REVIEW (no product implementation)"
dl = m["deliverables"]
dl["persian_docs"] = 21
dl["csv_catalogs"] = 20
dl["extracted_assets_files"] = len(stable)
dl["total_bytes"] = sum(p.stat().st_size for p in stable)
dl["verification"] = "PASS"
dl["verification_checks"] = 0  # refreshed after verify_upgrade.py
dl["design_round"] = "v8 (REVIEW)"
dl["design_views"] = 14
dl["design_svg_vectors"] = 93
dl["bottom_nav_tabs"] = 5
dl.pop("habitica_scoring_evidence", None)
dl["node_code_evidence"] = ("DESIGN/NODE_CODE_GEOMETRY.json v8 (58 vectors / 90 ARSC strings / 10 AXML shapes / "
                            "18 colors / 15 dimens / 92 PathMap DEX classes / 15 sections / 223 tutorialIds / "
                            "machine-readable nodeGeometry) + CATALOGS/MIMO_PATH_NODES.csv (72 rows)")
dl["v8_changes"] = "exact code-driven Learn nodes; NO locked node (one exam-hub exception); routine/Habitica removed; Dictate removed; no UI annotations; exam Mimo skin only"
for k in [k for k in m["source_hashes"] if k.startswith("habitica_")]:
    m["source_hashes"].pop(k, None)
cf = m["critical_findings"]
v8 = [
    "v8: «روتین روزانه» / entire Habitica scoring idea REMOVED (tab, screen, payload, docs, catalogs, tool); 5 tabs restored; MAX still forbidden",
    "v8: Dictate removed from the AI composer; TEACH/PRACTICE/model/medium remain on one tiny line",
    "v8: all design/policy/EPM/timer/code annotations removed from the phone UI; exam-hub labels/templates and descriptive answer text KEPT",
    "v8: ZERO locked nodes in Learn/section-detail/practice; only the pre-existing exam-hub «آزمون نهایی / دو هفتگی» lock remains",
    "v8: MAIN TASK — Learn nodes rebuilt data-driven from NODE_CODE_GEOMETRY.json (92dp squares, 26dp corners, 8dp 3D lip, white double ring + 1/2 progress, rounded-elbow Q connector, dotted grid, bolt states, floating book)",
    "v8: exam surfaces Mimo-ified in APPEARANCE ONLY (real Mimo vectors + ARSC colours/radii/type); no architecture/timer/policy change",
]
for x in v8:
    if x not in cf:
        cf.append(x)
rep = m["reproduce"]
rep[:] = [c for c in rep if "v7" not in c and "habitica" not in c]
for cmd in ["python3 tools/extract_mimo_nodes_v8.py .",
            "python3 tools/build_design_v8.py .",
            "python3 tools/finalize_v8.py .",
            "python3 tools/verify_upgrade.py ."]:
    if cmd not in rep:
        rep.append(cmd)
m["design_round_6"]["status"] = "DESIGN v6 · SUPERSEDED — archived audit trail"
m["design_round_7"]["status"] = "DESIGN v7 · SUPERSEDED by v8 (routine tab and Habitica idea REVOKED) — archived audit trail"
m["design_round_7"]["revoked"] = "روتین روزانه / Habitica scoring removed entirely by explicit user order in round 8"
m["design_round_8"] = {
    "status": "DESIGN v8 · REVIEW — awaiting final approval (CURRENT)",
    "trigger": "user: روتین روزانه رو کلا حدف کن / دیکته حدف کن / توضیحات داخل UI نیاز نیست / هیچ بخش قفلی جز یکی / نودها رو واقعاً درست کن / ظاهر آزمونها شبیهتر به میمو",
    "main_task": "exact Learn path-map NODES from code (NODE_CODE_GEOMETRY.json v8)",
    "method": "CODE_FIRST / extract_mimo_nodes_v8.py -> NODE_CODE_GEOMETRY.json -> build_design_v8.py -> DESIGN/index.html",
    "interactive_prototype": "DESIGN/index.html (14 views / 5 tabs / 93 SVG vectors / 133 painted icons / 6 nodes / 0 Learn locks / 0 jsdom errors)",
    "removed": ["روتین روزانه + Habitica idea (tab/screen/JSON/catalogs/docs/tool)", "Dictate", "all UI annotation notes (policy/EPM/timer/code chips/lh labels/tooltips)", "all locked Learn nodes/rows", "START bubble / stray 12% ring / debug chips"],
    "kept": ["7 labelled exam sections + field templates", "descriptive answer key / analysis", "exam architecture + timer + 270 min + پاسخبرگ≠پاسخنامه", "bolt section-practice isolated from exam hub", "one pre-existing exam-hub lock"],
    "exam_appearance": "real Mimo vectors (ic_trophy, ic_clock_black_24dp, ic_task_completed, ic_lock_alt_02, ic_file, ic_target, ic_sparks_alt, ic_arrow_back_24, ic_help) + ARSC colours/radii/type; NO architecture change",
    "final_log": "20_DESIGN_ROUND_8.md",
    "design_notes": "DESIGN/DESIGN_NOTES.fa.md",
    "final_approval": "PENDING — no product implementation until user says the design is final",
}
mp.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("MANIFEST updated; stable files=%d bytes=%d" % (len(stable), sum(p.stat().st_size for p in stable)))
