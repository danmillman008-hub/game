#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""finalize_v12_3.py — rejection/rollback round: catalogs / docs / MANIFEST. Idempotent."""
from __future__ import annotations
import csv
import json
from pathlib import Path

UP = Path(__file__).resolve().parents[1]
CAT, D = UP / "CATALOGS", UP / "DESIGN"
MARK = "<!-- v12.3-rollback -->"

ROWS = {
    "DESIGN_FEEDBACK.csv": [
        ["F-68", "طرح چهارمدل v12.2 از بیخ ایراد داشت: پاسخبرگ بصورت کارت ۲۰ حبابی بالای صورت سؤال گذاشته شد و با چیپ موضوع/گزینهها قاتی شد؛ همچنین جهت فلشها در RTL اشتباه بود (بعدی →، قبلی ←)",
         "v12.3: چهارمدل بهطور کامل حذف و ساختار صفحهٔ آزمون دقیقاً به v12.1 (کامیت d356963) برگردانده شد — پاسخبرگ/پاسخنامه همچنان کشوی پایین، بدنهٔ سؤال تمیز، یک CTA بنفش تمامعرض + دو مربع ۴۸dp. فلشها اصلاح شدند: بعدی ← / قبلی و بازگشت →. لوگوی ic_survey که خود کاربر خواسته بود نگه داشته شد. ریپوی چینی mindskip/xzs (do.vue) و منابع RTL بعنوان چک مرجع ثبت شدند",
         "DESIGN/EXAM_PAGE_REFERENCES.json, 24_DESIGN_ROUND_12.md §۸", "APPLIED"],
    ],
    "SCOPE_DECISIONS.csv": [
        ["D48", "صفحهٔ اجرای آزمون", "ROLLBACK_TO_V12_1_STRUCTURE",
         "ساختار v12.1 مرجع قطعی صفحهٔ آزمون است؛ هیچ مدل چندگانه، پاسخبرگ درونصفحهای، ردیف ثبت سریع، انتخابگر مدل یا نشان مدل اضافه نمیشود. پاسخبرگ = کشو (bottom sheet) جدا، پاسخنامه = کشوی جدا، صورت سؤال + ۴ گزینه + feedback تمیز. ریپوی چینی فقط برای درک ساختار/چک متقابل، بدون کپی کد",
         "درخواست کاربر: «اون ساختار قبل از تغییرات صفحه ازمون ... رفرنس خوبیه ... این طرحی که زدی از بیخ ایراد داره»", "DESIGN/EXAM_PAGE_REFERENCES.json"],
    ],
    "UI_FIDELITY_RULES.csv": [
        ["F44", "جهت فلشها در RTL", "در رابط راستبهچپ، فلش «بعدی / ادامه / جلو» نوکش به چپ (←) است و فلش «قبلی / بازگشت / عقب» نوکش به راست (→). وکتورهای دکدشده: ic_arrow_left واقعاً ←، ic_arrow_right و ic_arrow_back_24 واقعاً →/←. دکمهٔ ادامهٔ آزمون ic_arrow_left میگیرد، مربع قبل و دکمهٔ بازگشت ic_arrow_right؛ بقیهٔ ic_arrow_* فقط وقتی dir=rtl با scaleX(-1) آینه میشوند",
         "https://simplelocalize.io/blog/posts/rtl-design-guide-developers/ · https://localization.saudisoft.com/rtl-design/"],
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

## ۸. v12.3 — ردّ چهارمدل، بازگشت به ساختار تأییدشده، اصلاح فلشها

> `<!-- v12.3-rollback -->` · اسکریپت: `tools/build_exam_v12_3.py` (روی `tools/design_v12_1_template.html` = کامیت `d356963`). مشخصات مراجع: **`DESIGN/EXAM_PAGE_REFERENCES.json`**.

### تصمیم

چهارمدل **v12.2 مردود شد و بهطور کامل برگردانده شد**. دلیل از زبان کاربر: «اون ساختار قبل از تغییرات صفحهٔ آزمون … رفرنس خوبیه … پاسخبرگ رو مثلاً آوردی گذاشتی بالا کلا قاتیپاتی شده». یعنی همان ساختار **v12.1** مرجع است، نه یک بازطراحی تازه.

| مورد | v12.2 (مردود) | v12.3 (جاری = v12.1) |
|---|---|---|
| پاسخبرگ | کارت ۲۰ حبابی **بالای** صورت سؤال، لابلای ردیف شماره / چیپ موضوع / گزینهها | **کشوی پایین صفحه** `#paletteSheet`، بازشونده از چیپ «پاسخبرگ» یا پرچم نوار ابزار |
| پاسخنامه | همان چیپها + سیاست مدلمحور | **کشوی جدا** `#keySheet` با `keyTestSheet` / `keyDescSheet`، همان policy قبلی |
| بدنهٔ سؤال | استریپ + ردیف ثبت سریع ۴تایی + کارت تحلیل + متن آزاد (همه باهم) | **تمیز**: شماره/تایمر ← چیپ موضوع ← صورت سؤال ← ۴ کارت `choice_list_item` ← feedback |
| فوتر | ۴ فوتر تعویضشونده | **یک** CTA بنفش تمامعرض «ادامه / بررسی پاسخ» + **دو** مربع ۴۸dp + لینک «رد کردن سؤال» |
| بقیه | انتخابگر ۴ مدل، نشان مدل، ۴ CTA | هیچکدام — همان چیزی که تأیید شده بود |

### اصلاح فلشها (RTL)

کاربر: «برای بعدی نوک پیکان باید به سمت چپ باشه برای قبلی به سمت راست». بررسی وکتورهای دکدشده و منابع وب هم همان را گفت:

- `ic_arrow_left` = `M21,11.25H5.31…L3.325,11.115` → نوک **چپ** ←
- `ic_arrow_right` = `M20.675,11.115…H3V12.75H18.69…` → نوک **راست** →
- `ic_arrow_back_24` = `M20,11H7.83…l-8,8 8,8…` → نوک **چپ** ←

| دکمه | قبل | بعد |
|---|---|---|
| `#nextQ` (ادامه / بررسی پاسخ) | `ic_arrow_right` → | **`ic_arrow_left` ←** (`data-arrow="next"`) |
| `#prevQ` (سؤال قبل) | `ic_arrow_back_24` ← | **`ic_arrow_right` →** (`data-arrow="prev"`) |
| بازگشت صفحهٔ نتیجه | `ic_arrow_back_24` ← | **`ic_arrow_right` →** (`data-arrow="back"`) |

بقیهٔ آیکونهای `ic_arrow_*` که اصلشان LTR است، فقط وقتی `dir="rtl"` با `scaleX(-1)` آینه میشوند؛ سه دکمهٔ بالا که صراحتاً RTL نوشته شدند، در حالت `dir="ltr"` آینه میشوند تا هر دو جهت درست بماند. منابع: [SimpleLocalize RTL guide](https://simplelocalize.io/blog/posts/rtl-design-guide-developers/)، [Saudisoft RTL checklist](https://localization.saudisoft.com/rtl-design/)، [Codestan](https://www.codestan.com/insights/ux-design-tips-arabic-rtl-2026)، [Shaheer Malik](https://www.shaheermalik.com/blog/arabic-website-design-rtl).

### چک متقابل با ریپوی چینی

`mindskip/xzs` / `iiSee/uexam` (xzs / uexam)، فایل `source/vue/xzs-student/src/views/exam/paper/do.vue` خوانده شد:

- بدنهٔ پاسخدهی تمیز است: `el-card` برای هر سؤال + `QuestionEdit` برای گزینهها؛ **هیچ کارت پاسخبرگ لابلای سؤالها نیست**.
- شمارهٔ سؤالها و «زمان باقیمانده» (زمان باقیمانده) در **یک نوار جداگانه/چسبان بالا**اند، نه داخل بدنهٔ سؤال.
- یک دکمهٔ اصلی «Submit» در انتهای برگه + «Cancel».
- پاسخ / «توضیح پاسخ» / پاسخ صحیح **بعد از submit** در `read.vue`، `QuestionAnswerShow.vue` و «دفتر غلطها» نمایش داده میشوند — حین آزمون نه.

نتیجه: همان شکل v12.1 (پاسخبرگ و پاسخنامه بهصورت پنل/کشوی جدا، بدنهٔ سؤال خلوت، صحت بعد از آزمون) درست بود. **هیچ کد، دارایی یا لایهای از آن ریپو کپی نشد**؛ فقط برای درک ساختار و چک متقابل استفاده شد. اسکرینشاتها همچنان فقط چک بصریاند.

### نگهداشتهشده / دستنخورده

- لوگوی هاب = `ic_survey.xml` و نتیجه = `ic_cap` (همان تغییری که در پیام قبل خواسته شده بود)؛ ماسکوت میمو برنگشت.
- تمام رفعباگهای v12.1 (اسکرول هاب/نتیجه، کلیک کل ردیف، چیپهای فیلتر، شمارهٔ پویای AI، ۲۰ سؤال مجزا، پوشش RTL، زیرنویس ردیفها و بوکمارک پرسؤال).
- ۵ تب · `MAX` ممنوع · مسیر قوسدار اورجینال · ۷ بخش لیبلدار و قالبها · ۲۷۰ دقیقهٔ ثابت و تایمر فقط داخل آزمون · «پاسخبرگ»≠«پاسخنامه» · تکقفل · تکدکمهٔ AI · `section-practice` جدا.
- مسیر برگشت همچنان `tools/design_v11_full.html` (v11.1 تأییدشده) و `tools/design_v12_1_template.html` (v12.1).

**وریفای:** `verify_upgrade.py` PASS ۲۴۱/۲۴۱ · `check_v12_3.js` ۱۲۲ تست / ۰ خطا · `node --check` OK · کلیک روی ۱۸۷ المان تعاملی بدون خطای runtime · ۰ آیدی تکراری.
'''
    LOG.write_text(s, encoding="utf-8")
    print("round-12 log: §8 rollback appended")

NOTES = D / "DESIGN_NOTES.fa.md"
s = NOTES.read_text(encoding="utf-8")
if MARK not in s:
    s += ("\n\n## ۸. v12.3 (بازگشت)\n\n`" + MARK + "` چهارمدل v12.2 **رد و حذف شد**؛ صفحهٔ آزمون دقیقاً به ساختار v12.1 "
          "(`d356963`) برگردانده شد: پاسخبرگ و پاسخنامه کشوهای جدا، بدنهٔ سؤال تمیز، یک CTA بنفش تمامعرض + دو مربع ۴۸dp. "
          "فلشها در RTL اصلاح شدند (بعدی ←، قبلی/بازگشت →). لوگوی `ic_survey` / `ic_cap` نگه داشته شد. "
          "مراجع RTL و ریپوی چینی `mindskip/xzs · do.vue` در `DESIGN/EXAM_PAGE_REFERENCES.json` ثبت شدند. "
          "PASS ۲۴۱/۲۴۱ · `check_v12_3.js` ۱۲۲/۰.\n")
    NOTES.write_text(s, encoding="utf-8")
    print("design notes updated")

wf = UP / "wireframes.html"
s = wf.read_text(encoding="utf-8").replace('DESIGN/index.html">DESIGN v12</a>', 'DESIGN/index.html">DESIGN v12.3</a>')
wf.write_text(s, encoding="utf-8")

mp = UP / "MANIFEST.json"
m = json.loads(mp.read_text(encoding="utf-8"))
m["date"] = "2026-11-04"
m["status"] = "PLAN_ONLY + DESIGN v12.3 REVIEW (v12.2 rejected; exam page rolled back to v12.1 + RTL arrows)"
dl = m["deliverables"]
dl["verification"] = "PASS"
dl["verification_checks"] = 241
dl["design_round"] = "v12.3 (REVIEW)"
dl["design_svg_vectors"] = 94
dl["v12_exam_ui"] = ("EXAM_UI_CODE_EVIDENCE.json + EXAM_PAGE_REFERENCES.json — v12.3: v12.2 four-model "
                     "redesign rejected and reverted to the accepted v12.1 single-CTA Mimo lesson UI; "
                     "answer sheet / key remain bottom sheets; RTL arrows corrected; ic_survey / ic_cap emblems")
stable = [p for p in UP.rglob("*") if p.is_file() and p.name not in ("SHA256SUMS.txt", "VERIFICATION_REPORT.json")]
dl["persian_docs"] = len(list(UP.glob("*.md")))
dl["csv_catalogs"] = len(list(CAT.glob("*.csv")))
dl["extracted_assets_files"] = len(stable)
dl["total_bytes"] = sum(p.stat().st_size for p in stable)
for x in [
    "v12.3: the v12.2 FOUR exam-page models were REJECTED by the user (answer sheet card placed above the stem made the question body incoherent); exam-run rolled back byte-for-byte to the accepted v12.1 structure at d356963",
    "v12.3: RTL directional arrows fixed — NEXT/ادامه now uses ic_arrow_left (arrowhead LEFT), PREVIOUS and BACK use ic_arrow_right (arrowhead RIGHT); other ic_arrow_* glyphs mirrored only under dir=rtl",
    "v12.3: cross-checked against mindskip/xzs (学之思) student exam page do.vue — clean question body, separate compact number/time bar, single submit, answers/解析 only after submit; used for understanding only, nothing copied",
]:
    if x not in m["critical_findings"]:
        m["critical_findings"].append(x)
for cmd in ["python3 tools/build_exam_v12_3.py .", "python3 tools/finalize_v12_3.py ."]:
    if cmd not in m["reproduce"]:
        m["reproduce"].append(cmd)
m["design_round_12"]["status"] = "DESIGN v12 · REVIEW — superseded by v12.1 fixes and the v12.3 rollback (CURRENT)"
m["design_round_12"]["v12_3_rollback"] = {
    "status": "APPLIED, awaiting final approval",
    "rejected": "v12.2 four exam-page models (inline answer-sheet strip above the stem, four footers, model picker)",
    "reference_of_record": "tools/design_v12_1_template.html @ d356963",
    "script": "tools/build_exam_v12_3.py (runs on the v12.1 snapshot)",
    "references": "DESIGN/EXAM_PAGE_REFERENCES.json",
    "arrow_fix": "next=ic_arrow_left (LEFT), prev/back=ic_arrow_right (RIGHT), RTL mirroring CSS",
    "emblem": "ic_survey (hub) / ic_cap (result) kept from the previous explicit request",
    "tests": "check_v12_3.js (122 checks / 0 errors) + verify_upgrade.py PASS 241/241",
    "unchanged": "all v11.1 acceptances + v12.1 bug fixes + rollback snapshots",
}
mp.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("MANIFEST updated; docs=%d csv=%d files=%d bytes=%d" %
      (dl["persian_docs"], dl["csv_catalogs"], len(stable), sum(p.stat().st_size for p in stable)))
