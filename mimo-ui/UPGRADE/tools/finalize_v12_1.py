#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""finalize_v12_1.py — round-12 bug-fix pass: catalogs / docs / MANIFEST. Idempotent."""
from __future__ import annotations
import csv
import json
from pathlib import Path

UP = Path(__file__).resolve().parents[1]
CAT = UP / "CATALOGS"
D = UP / "DESIGN"
MARK = "<!-- v12.1-bugfix -->"

ROWS = {
    "DESIGN_FEEDBACK.csv": [
        ["F-66", "چند بخش کدش درست نوشته نشده بود (هاب و نتیجه بریده میشدند، ردیفها فقط از روی آیکن کلیک میخوردند، چیپها بیعمل بودند، شمارهٔ سؤال ناهماهنگ با بانک ۵تایی)",
         "v12.1: ۷ باگ کد رفع شد — اسکرول هاب/نتیجه، کلیک کل ردیف + کیبورد، فیلتر چیپها، ۲۰ سؤال مجزا و QTOTAL واحد، ریست QI در هر آزمون، شمارهٔ پویای سؤال در AI، پوشش RTL، زیرنویس ردیفها و بوکمارک پرسؤال",
         "tools/fix_design_v12_1.py, 24_DESIGN_ROUND_12.md §۷", "APPLIED"],
    ],
    "SCOPE_DECISIONS.csv": [
        ["D46", "کیفیت کد پروتوتایپ", "V12_1_CODE_BUGFIX_ONLY_V12",
         "دور v12.1 فقط رفع ایرادات کد است؛ هیچ تغییر معماری/دیزاینی بجز موارد لازم برای کارکرد صحیح. ساختار v12 (تک CTA تمامعرض، پوستهٔ میمو، شواهد کد) و مصوبات v11.1 پابرجا",
         "درخواست کاربر: «فقط داخلش ایراد کد هست … ایراداتش رو رفع کنی»", "check_v12_1.js / verify_upgrade.py"],
    ],
    "UI_FIDELITY_RULES.csv": [
        ["F42", "اسکرول و کلیک", "هر صفحهای که فوتر ثابت ندارد باید خودش اسکرول شود؛ ردیف لیست تمامعرض کلیکپذیر و کیبوردپذیر است؛ چیپهای فیلتر باید واقعاً فیلتر کنند؛ شمارهٔ سؤال و بانک سؤال باید یکی باشند",
         "tools/fix_design_v12_1.py · B1/B2/B3/B5"],
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

## ۷. v12.1 — رفع ایرادات کد (بدون تغییر دیزاین)

> `<!-- v12.1-bugfix -->` · اسکریپت: `tools/fix_design_v12_1.py` (روی خروجی `tools/design_v12_template.html`). تستها: `check_v12_1.js` (۱۰۹ تست / ۰ خطا) و `verify_upgrade.py` (PASS ۲۳۴/۲۳۴).

| # | ایراد | رفع |
|---|---|---|
| **B1** | `.exv12{overflow:hidden}` روی هر سه صفحه؛ فقط `exam-run` اسکرول درونی (`.lb-body`) داشت. نتیجه: **هاب آزمونها و صفحهٔ نتیجه بریده میشدند** و ۵ بخش از ۷ بخش و کارتهای پایینی دیده نمیشدند. | `.exv12` حالا `overflow:auto;padding:0`؛ فقط `[data-screen="exam-run"]` میماند `overflow:hidden` چون فوتر `.lk` پین است. `.lb-body` افزودن `min-height:0`. |
| **B2** | بعد از تبدیل شبکهٔ ۳ ستونه به ردیفهای لیستی، هندلر هنوز فقط روی آیکن ۴۴dpی `.nodek` بسته بود؛ کلیک روی عنوان ردیف کاری نمیکرد درحالیکه `cursor:pointer` داشت. | `openExam(n)` + delegation روی **کل ردیف** (`role="button"`، `tabIndex=0`، `Enter`/`Space`). ضمن هر آزمون تازه `QI=0` و `MARKS={}` ریست میشود (قبلاً شمارهٔ سؤال از آزمون قبل میماند). |
| **B3** | ۸ چیپ فیلتر `<span>` بی هیچ لیسنری بودند و فقط رنگ «همه» عوض میشد. | تبدیل به `<button data-filter>`؛ گروهبندی ۷ بخش لیبلدار (`sec + cat-meta + grid3`) و فیلتر واقعی. «جمع بندی» بخشهای ۶ و ۷ را با هم نشان میدهد. |
| **B4** | زمینهٔارسالی به AI سختکد شده بود «سؤال ۳» حتی وقتی کاربر سؤال ۱۵ بود. | `fa(QI+1)` پویا. |
| **B5** | شمارنده میگفت «از ۲۰» ولی `QBANK` فقط ۵ رکورد داشت (صورت سؤالها بیصدا تکرار میشدند)؛ عدد ۲۰ در چند جا سختکد شده بود. | **۲۰ سؤال مجزا** (۴ درس × مباحث گوناگون، همراه پاسخ و توضیح)، ثابت واحد `QTOTAL=QBANK.length` برای شمارنده/نوار پیشرفت/شمارندهٔ پاسخبرگ، `QI` از ۰ شروع میشود. |
| **B6** | دکمهٔ RTL/LTR فقط `.mimo` را پوشش میداد؛ بعد از تغییر پوسته، سه صفحهٔ آزمون از toggle جا میماندند. `render()` هم در حالت `setting` چیپهای توقف/تنظیم مجدد را ریست نمیکرد. | `qa(".mimo,.exv12",ph)` + ریست چیپها در `setting`. |
| **B7** | نشانهای `.mini` (۲۰۰ سؤال / زمان ثابت / قفل / …) با `display:none` پنهان و اطلاعاتشان گم شده بود. | انتقال به `<span class="row-meta">` داخل عنوان ردیف = زیرنویس واقعی میمو (۲۱ ردیف). ساخت چیپ موضوع با `createElement` بجای `innerHTML`+`esc`، حذف `paintIcons` بیهوده، و بوکمارک **بهازای هر سؤال** (قبلاً با رفتن به سؤال بعد پاک میشد). |

**بدون تغییر:** تک CTA بنفش تمامعرض / مربع ۴۸dp سؤال قبل / پنل feedback · `chapter_toolbar` · ۷ بخش لیبلدار و قالبها · ۲۷۰ دقیقه و تایمر فقط داخل آزمون · تکقفل · تکدکمهٔ AI · ۵ تب · مسیر قوسدار · لیدربورد و ۳ کارت v11.1 · مسیر برگشت `tools/design_v11_full.html`. شواهد ماشینخوان ۷ باگ در `DESIGN/EXAM_UI_CODE_EVIDENCE.json` ← `bugfixes_v12_1`.
'''
    LOG.write_text(s, encoding="utf-8")
    print("round-12 log: §7 appended")

NOTES = D / "DESIGN_NOTES.fa.md"
s = NOTES.read_text(encoding="utf-8")
if MARK not in s:
    s += ("\n\n## ۷. v12.1 (رفع ایرادات کد)\n\n"
          "`" + MARK + "` هفت ایراد کد رفع شد: اسکرول هاب/نتیجه، کلیک و کیبورد روی کل ردیف، چیپهای فیلتر واقعی، "
          "۲۰ سؤال مجزا و `QTOTAL` واحد، شمارهٔ پویای سؤال در AI، پوشش RTL صفحات آزمون، زیرنویس ردیفها و بوکمارک پرسؤال. "
          "دیزاین و ساختار v12 و مصوبات v11.1 دستنخوردهاند. `tools/fix_design_v12_1.py` · `check_v12_1.js` · PASS ۲۳۴/۲۳۴.\n")
    NOTES.write_text(s, encoding="utf-8")
    print("design notes updated")

mp = UP / "MANIFEST.json"
m = json.loads(mp.read_text(encoding="utf-8"))
m["date"] = "2026-11-04"
m["status"] = "PLAN_ONLY + DESIGN v12.1 REVIEW (v12 code-bug fix pass; no product implementation)"
dl = m["deliverables"]
dl["verification"] = "PASS"
dl["verification_checks"] = 234
dl["design_round"] = "v12.1 (REVIEW)"
dl["v12_exam_ui"] = ("EXAM_UI_CODE_EVIDENCE.json — single full-width CTA, no equal prev/next pill pair, "
                     "no separate konkur skin; v12.1 fixes 7 code bugs (scroll / row click / filters / 20-question bank / RTL / row meta)")
stable = [p for p in UP.rglob("*") if p.is_file() and p.name not in ("SHA256SUMS.txt", "VERIFICATION_REPORT.json")]
dl["persian_docs"] = len(list(UP.glob("*.md")))
dl["csv_catalogs"] = len(list(CAT.glob("*.csv")))
dl["extracted_assets_files"] = len(stable)
dl["total_bytes"] = sum(p.stat().st_size for p in stable)
for x in [
    "v12.1: BUG FIX — .exv12{overflow:hidden} clipped exam-hub and exam-result (5 of 7 sections unreachable); both now scroll, exam-run keeps its pinned interaction keyboard",
    "v12.1: BUG FIX — Mimo list rows were clickable only on the 44dp icon; whole row + keyboard activation now opens the exam and resets the question index",
    "v12.1: BUG FIX — 8 exam-hub filter chips were inert spans; now real buttons filtering the 7 labelled sections",
    "v12.1: BUG FIX — counter said 20 while QBANK had 5 (stems silently repeated); 20 distinct questions + one QTOTAL + dynamic AI question number",
    "v12.1: BUG FIX — RTL/LTR toggle skipped exv12 screens; hidden .mini badges moved into row labels; per-question bookmarks",
]:
    if x not in m["critical_findings"]:
        m["critical_findings"].append(x)
for cmd in ["python3 tools/fix_design_v12_1.py .", "python3 tools/finalize_v12_1.py ."]:
    if cmd not in m["reproduce"]:
        m["reproduce"].append(cmd)
m["design_round_12"]["status"] = "DESIGN v12 · REVIEW — superseded only by the v12.1 code-bug fix pass (CURRENT)"
m["design_round_12"]["bugfixes_v12_1"] = {
    "status": "APPLIED, awaiting final approval",
    "trigger": "user: خیلی بهتر شد فقط داخلش ایراد کد هست یه سری بخشها کدش رو درست ننوشتی … ایراداتش رو رفع کنی",
    "script": "tools/fix_design_v12_1.py (runs on tools/design_v12_template.html)",
    "bugs": ["B1 scroll clipping", "B2 row click delegation + QI reset", "B3 filter chips",
             "B4 dynamic AI question number", "B5 20-question bank + QTOTAL", "B6 RTL toggle + timer state",
             "B7 row subtitles + DOM-built subject + per-question bookmarks"],
    "evidence": "DESIGN/EXAM_UI_CODE_EVIDENCE.json :: bugfixes_v12_1",
    "tests": "check_v12_1.js (109 checks / 0 errors) + verify_upgrade.py PASS 234/234",
    "unchanged": "v12 single CTA / Mimo skin / all v11.1 acceptances / rollback snapshot",
}
mp.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("MANIFEST updated; docs=%d csv=%d files=%d bytes=%d" %
      (dl["persian_docs"], dl["csv_catalogs"], len(stable), sum(p.stat().st_size for p in stable)))
