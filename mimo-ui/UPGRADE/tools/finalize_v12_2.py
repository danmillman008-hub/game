#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""finalize_v12_2.py — four exam-page models: catalogs / docs / MANIFEST. Idempotent."""
from __future__ import annotations
import csv
import json
from pathlib import Path

UP = Path(__file__).resolve().parents[1]
CAT = UP / "CATALOGS"
D = UP / "DESIGN"
MARK = "<!-- v12.2-models -->"

ROWS = {
    "DESIGN_FEEDBACK.csv": [
        ["F-67", "لوگوی ماسکوت میمو کنار «آزمونها» نباید باشد؛ و یک صفحهٔ واحد اجرای آزمون برای همهٔ انواع آزمون کافی نیست (تحلیلی میخواهد «بررسی پاسخ»، زماندار/جامع میخواهد «سؤال قبل/بعد» و «پاسخنامه»)",
         "v12.2: لوگوی هاب ← ic_survey.xml (تصویرسازی واقعی کوییز میمو)، نتیجه ← ic_cap؛ و ۴ مدل صفحهٔ اجرا ساخته شد: کنکوری/زمان خالص، تمرینی میمو، تحلیلی، تشریحی. مدلها از روی دکمههای دیزاینهای قبل + sp-opts بخش تمرین میمو + ساختار واقعی کنکور طراحی شدند",
         "DESIGN/EXAM_PAGE_MODELS.json, 24_DESIGN_ROUND_12.md §۸", "APPLIED"],
    ],
    "SCOPE_DECISIONS.csv": [
        ["D47", "صفحهٔ اجرای آزمون", "FOUR_EXAM_PAGE_MODELS_V12_2",
         "بهجای یک چیدمان واحد، ۴ مدل بر اساس data-kind انتخاب میشود: konkur (جامع/زماندار/جمع بندی)، practice (عادی)، analytical (تحلیلی)، descriptive (تشریحی). مدل کنکوری پاسخبرگ درونصفحهای + قبل/بعد + بدون اعلام صحت دارد؛ مدل تمرینی/تحلیلی «بررسی پاسخ» و feedback میمو دارند. انتخابگر ۴ مدل در پنل بررسی بیرون گوشی",
         "درخواست کاربر: «نیاز داره فکر کنی چند مدل صفحه برای آزمون بساز»", "DESIGN/EXAM_PAGE_MODELS.json"],
    ],
    "UI_FIDELITY_RULES.csv": [
        ["F43", "مدلهای صفحهٔ آزمون", "ناوبری و دکمهها تابع نوع آزموناند: Konkur = پاسخبرگ حین آزمون (۲۰ حباب) + ردیف ۴گانهٔ sp-opts + سؤال قبل/بعد + بدون اعلام صحت + پاسخنامه بعد؛ Mimo practice = یک CTA تمامعرض btn_submit/btn_continue_big + feedback؛ Analytical = feedback + تحلیل زنده + هر دو جهت؛ Descriptive = متن آزاد + تعویض سوال/تصحیح دستی. لوگوها فقط وکتورهای دکدشده (ic_survey / ic_cap)، بدون ماسکوت",
         "quiz_introduction_fragment.xml / section-practice sp-opts / EXAM_SECTION_TEMPLATES.csv"],
    ],
}
for name, rows in ROWS.items():
    p = CAT / name
    with p.open(encoding="utf-8", newline="") as f:
        body = list(csv.reader(f))[1:]
    present = {r[0] for r in body if r}
    todo = [r for r in rows if r[0] not in present]
    if todo:
        with p.open("a", encoding="utf-8", newline="") as f:
            csv.writer(f).writerows(todo)
    print(name, "+", len(todo), "->", len(body) + len(todo))

LOG = UP / "24_DESIGN_ROUND_12.md"
s = LOG.read_text(encoding="utf-8")
if MARK not in s:
    s += r'''

---

## ۸. v12.2 — چهار مدل صفحهٔ اجرای آزمون + لوگوی تازه

> `<!-- v12.2-models -->` · اسکریپت: `tools/build_exam_models_v12_2.py` (روی `tools/design_v12_1_template.html`). مشخصات ماشینخوان: **`DESIGN/EXAM_PAGE_MODELS.json`**.

### چرا چند مدل؟

یک صفحه نمیتواند هم «نشستن واقعی کنکور» باشد و هم «درس تعاملی میمو». کنکور: ۲۷۰ دقیقهٔ ثابت، پاسخبرگ **حین** آزمون پر میشود، هیچ صحتسنجیای به داوطلب اعلام نمیشود، پاسخنامه **بعد** منتشر میشود، و «سؤال قبل/بعد + رد کردن + علامتگذاری» ناوبری اصلیاند. میمو: یک دکمهٔ بنفش تمامعرض `btn_submit` ← پنل feedback سبز/قرمز ← `btn_continue_big`. کاربر هم دقیقاً همین تمایز را گفت: «در آزمونهای تحلیلی شاید بررسی پاسخ مهم باشه ولی در آزمونهای زماندار و بقیه سؤال بعدی سؤال قبلی و پاسخنامه … مهمتره».

سه منبع کنار هم گذاشته شد: **دکمههای دیزاینهای قبلی ما** (`qnav`/`qfoot` دور v11)، **بخش تمرین خود میمو** (`section-practice` با ردیف ۴گانهٔ `sp-opts` — ثبت سریع پاسخ بدون نمره دادن)، و **ساختار خود کنکور** (پاسخبرگ ۲۰ خانهای، پرش مستقیم به سؤال، زمان خالص، پاسخنامه بعد از آزمون). لایههای دکدشدهٔ `chapter_toolbar.xml`، `lesson_interactive_multiplechoice_fragment.xml`، `choice_list_item.xml`، `interaction_keyboard_view.xml`، `run_button_view.xml` و `lesson_interactive_feedback_bottom_sheet_dialog.xml` همچنان حکم ساختارند؛ اسکرینشاتها فقط چک بصری.

| # | مدل | آزمونها | بدنه | فوتر | بررسی پاسخ |
|---|---|---|---|---|---|
| **①** | **کنکوری / زمان خالص** `konkur` | جامع، زماندار، سرعتی، پومودورو، جمع بندی، نهایی | **پاسخبرگ درونصفحهای**: ۲۰ حباب با حالتهای پاسخ داده / جاری / علامتخورده و پرش مستقیم · صورت سؤال + ۴ کارت `choice_list_item` · **ردیف ۴گانهٔ ثبت سریع** (از `sp-opts` تمرین میمو، فقط ثبت میکند، نمره نمیدهد) · چیپهای پاسخبرگ/پاسخنامه/AI/اتمام/تایمر | مربع ۴۸dp «سؤال قبل» \| **CTA بنفش تمامعرض «سؤال بعد»** \| مربع ۴۸dp علامتگذاری + لینک «رد کردن سؤال» | ❌ هرگز (پاسخنامه طبق policy: جامع/جمعبندی بعد، زماندار حین) |
| **②** | **تمرینی میمو** `practice` | تکدرسی، مبحثی، این ماه، مرور غلطها، آزمون دوباره | همان `lesson_interactive` میمو + پنل feedback + پاسخبرگ و پاسخنامه حین آزمون | مربع قبل + مربع علامت + **یک CTA تمامعرض** `lesson_submit` «بررسی پاسخ» ← feedback ← `lesson_continue` «ادامه» + `lesson_skip` | ✅ |
| **③** | **تحلیلی** `analytical` | تحلیل زیست، تحلیل آزمون جامع، تحلیل غلطها | feedback + **کارت تحلیل زنده** (درصد، «اگر غلطها نزده میذاشتی»، نقشهٔ ضعف، میانگین زمان) | مربع قبل \| CTA «بررسی پاسخ» \| مربع بعد + دکمهٔ نمایش/پنهان تحلیل | ✅ |
| **④** | **تشریحی** `descriptive` | آزمون تشریحی | **بدون ۴ گزینه**: متن آزاد + شمارندهٔ واژه + پاسخبرگ هماهنگ | مربع قبل \| CTA «ثبت پاسخ» \| مربع بعد + چیپهای «تعویض سوال» / «تصحیح دستی» (همان قالب بخش ۷) | ❌ |

**انتخاب مدل:** هر کارت هاب با `data-kind` مدل خود را تعیین میکند (`MODEL_BY_KIND`). برای مرور سریع، پنل بررسی بیرون گوشی ۴ دکمهٔ «پیشنمایش مدل» دارد که همان مدل را باز میکند. نوار ۵۲dp بالا یک نشان مدل (`کنکوری / تمرینی / تحلیلی / تشریحی`) نشان میدهد.

### لوگو

ماسکوت میمو (`ic_mimo_mascot`) از **هاب آزمونها** و **صفحهٔ نتیجه** حذف شد:
- هاب ← **`ic_survey.xml`**: همان تصویرسازی واقعی کوییز میمو در `quiz_introduction_fragment.xml` (`iv_quiz_introduction`، ۱۸۰dp)، ۲۸ مسیر رنگی؛ به `GEO.vectors` اضافه و با همان رندرر وکتورها نقاشی شد (حالا ۹۴ وکتور).
- نتیجه ← **`ic_cap`** (کلاه فارغالتحصیلی)، سفید روی دایرهٔ `button_primary`.

هر دو وکتور دکدشدهٔ APKاند؛ هیچ لوگوی جدید/برند میمو باقی نماند.

**بدون تغییر:** ۵ تب و `MAX` ممنوع · مسیر قوسدار اورجینال · ۷ بخش لیبلدار + قالبها + پاسخنامهٔ تشریحی · ۲۷۰ دقیقهٔ ثابت و تایمر فقط داخل آزمون · «پاسخبرگ»≠«پاسخنامه» · تنها یک قفل هاب · تکدکمهٔ AI · `section-practice` جدا · ۲۰ سؤال مجزای v12.1 · مسیر برگشت `tools/design_v11_full.html`.

**وریفای:** `verify_upgrade.py` PASS ۲۴۵/۲۴۵ · `check_v12_2.js` ۱۳۷ تست / ۰ خطا · `node --check` OK · کلیک روی ۲۲۸ المان تعاملی بدون خطای runtime · ۰ آیدی تکراری.
'''
    LOG.write_text(s, encoding="utf-8")
    print("round-12 log: §8 appended")

NOTES = D / "DESIGN_NOTES.fa.md"
s = NOTES.read_text(encoding="utf-8")
if MARK not in s:
    s += ("\n\n## ۸. v12.2 (چهار مدل صفحهٔ آزمون)\n\n"
          "`" + MARK + "` صفحهٔ اجرای آزمون دیگر یک مدل واحد نیست: "
          "**① کنکوری/زمان خالص** (پاسخبرگ درونصفحهای ۲۰ حباب + ردیف ۴گانهٔ `sp-opts` + سؤال قبل/بعد + بدون اعلام صحت)، "
          "**② تمرینی میمو** (یک CTA «بررسی پاسخ ← feedback ← ادامه»)، "
          "**③ تحلیلی** (feedback + تحلیل زنده + هر دو جهت ناوبری)، "
          "**④ تشریحی** (متن آزاد + تعویض سوال/تصحیح دستی). "
          "مدلها از `data-kind` کارتهای هاب انتخاب میشوند و از پنل بررسی قابل پیشنمایشاند. "
          "لوگوی هاب = `ic_survey.xml` و نتیجه = `ic_cap`؛ ماسکوت میمو حذف شد. "
          "مشخصات: `DESIGN/EXAM_PAGE_MODELS.json` · `tools/build_exam_models_v12_2.py` · PASS ۲۴۵/۲۴۵.\n")
    NOTES.write_text(s, encoding="utf-8")
    print("design notes updated")

wf = UP / "wireframes.html"
s = wf.read_text(encoding="utf-8").replace('DESIGN/index.html">DESIGN v12</a>', 'DESIGN/index.html">DESIGN v12.2</a>')
wf.write_text(s, encoding="utf-8")

mp = UP / "MANIFEST.json"
m = json.loads(mp.read_text(encoding="utf-8"))
m["date"] = "2026-11-04"
m["status"] = "PLAN_ONLY + DESIGN v12.2 REVIEW (four exam-page models; no product implementation)"
dl = m["deliverables"]
dl["verification"] = "PASS"
dl["verification_checks"] = 245
dl["design_round"] = "v12.2 (REVIEW)"
dl["design_svg_vectors"] = 94
dl["v12_exam_ui"] = ("EXAM_UI_CODE_EVIDENCE.json + EXAM_PAGE_MODELS.json — v12.2 FOUR exam-page models "
                     "(konkur / practice / analytical / descriptive), single full-width CTA per model, "
                     "no equal prev/next pill pair, no separate konkur skin; ic_survey / ic_cap emblems")
stable = [p for p in UP.rglob("*") if p.is_file() and p.name not in ("SHA256SUMS.txt", "VERIFICATION_REPORT.json")]
dl["persian_docs"] = len(list(UP.glob("*.md")))
dl["csv_catalogs"] = len(list(CAT.glob("*.csv")))
dl["extracted_assets_files"] = len(stable)
dl["total_bytes"] = sum(p.stat().st_size for p in stable)
for x in [
    "v12.2: FOUR distinct exam-page models replace the single generic exam-run sheet — konkur (inline 20-bubble answer sheet + quick sp-opts bubbles + real prev/next + no grading), practice (Mimo SUBMIT->feedback->CONTINUE), analytical (feedback + live analysis + both nav directions), descriptive (written answer + تعویض سوال / تصحیح دستی)",
    "v12.2: exam-hub emblem changed from Mimo mascot to ic_survey.xml (the APK's real quiz illustration); exam-result uses ic_cap; GEO.vectors now 94",
    "v12.2: model chosen by each exam card's data-kind; 4-button reviewer picker outside the phone; Konkur structure (answer sheet during exam, key after) reconciled with Mimo practice grammar",
]:
    if x not in m["critical_findings"]:
        m["critical_findings"].append(x)
for cmd in ["python3 tools/build_exam_models_v12_2.py .", "python3 tools/finalize_v12_2.py ."]:
    if cmd not in m["reproduce"]:
        m["reproduce"].append(cmd)
m["design_round_12"]["status"] = "DESIGN v12 · REVIEW — superseded only by v12.1 fixes and the v12.2 four-model pass (CURRENT)"
m["design_round_12"]["exam_page_models_v12_2"] = {
    "status": "APPLIED, awaiting final approval",
    "trigger": "user: صفحهٔ اجرای آزمون یک مدل کافی نیست؛ تحلیلی «بررسی پاسخ» میخواهد، زماندار «سؤال بعدی/قبلی» و «پاسخنامه»؛ دیزاینهای قبلی + بخش تمرین میمو + ساختار کنکور را ببین و چند مدل بساز",
    "script": "tools/build_exam_models_v12_2.py (runs on tools/design_v12_1_template.html)",
    "spec": "DESIGN/EXAM_PAGE_MODELS.json",
    "models": ["konkur (comprehensive/timed/review)", "practice (normal)",
               "analytical", "descriptive"],
    "emblem": {"hub": "ic_survey.xml (quiz_introduction_fragment.xml)", "result": "ic_cap.xml",
               "removed": "ic_mimo_mascot from both exam surfaces"},
    "tests": "check_v12_2.js (137 checks / 0 errors) + verify_upgrade.py PASS 245/245",
    "unchanged": "all v11.1 acceptances + v12 single-CTA grammar per model + rollback snapshot",
}
mp.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("MANIFEST updated; docs=%d csv=%d files=%d bytes=%d" %
      (dl["persian_docs"], dl["csv_catalogs"], len(stable), sum(p.stat().st_size for p in stable)))
