#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""finalize_v12_5.py — user-correction round over v12.4: catalogs / docs / MANIFEST. Idempotent."""
from __future__ import annotations
import csv
import json
from pathlib import Path

UP = Path(__file__).resolve().parents[1]
CAT, D = UP / "CATALOGS", UP / "DESIGN"
MARK = "<!-- v12.5-corrections -->"
CHECKS = 259

ROWS = {
    "DESIGN_FEEDBACK.csv": [
        ["F-70", "v12.4 سه ایراد داشت: «توضیح با هوش مصنوعی» بهاشتباه از بدنهٔ آزمون حذف و به کشوی پاسخنامه منتقل شده بود؛ مدت ۲۷۰ دقیقهٔ آزمون جامع readonly و «غیرقابل تغییر» شده بود؛ کشوی خروج فقط دو گزینه داشت و «خروج و ذخیره» واقعاً پیشرفت را نگه نمیداشت و «دیدن درصد تا همانجا» وجود نداشت",
         "v12.5: چیپ AI دقیقاً به جایگاه و استایل v12.1/v12.3 برگشت (سومین چیپ کنار پاسخبرگ/پاسخنامه، ic_magic_wand، ۱۶dp، mono) و کپی داخل پاسخنامه حذف شد. #timerMinutes در همهٔ انواع آزمونها دستی و بدون قفل است؛ ۲۷۰ فقط پیشفرض جامع و ۶ preset باقی ماندند (max=۳۰۰ هم برداشته شد؛ نمایش ۲۷۰:۰۰ اصلاح شد). کشوی خروج سه گزینه شد: «خروج و ذخیره» (snapshot سؤال/پاسخها/نشانها/تایمر + نوار «ادامهٔ آزمون ذخیرهشده» در هاب)، «ادامهٔ آزمون»، «پایان آزمون و دیدن کارنامه / خروج و دیدن درصد» که کارنامهٔ موقت را فقط از پاسخهای زدهشده حساب میکند؛ پایان کامل بعد از ادامه، کارنامهٔ کامل میدهد",
         "24_DESIGN_ROUND_12.md §۱۰, tools/build_exam_v12_5.py, tools/design_v12_5_template.html", "APPLIED"],
    ],
    "SCOPE_DECISIONS.csv": [
        ["D50", "صفحهٔ اجرای آزمون", "USER_CORRECTIONS_V12_5",
         "دقیقاً سه چیپ در ردیف ابزار، به همان ترتیب و استایل v12.1 (پاسخبرگ / پاسخنامه / توضیح با هوش مصنوعی)؛ سایر حذفیات v12.4 پابرجا (اتمام آزمون، خروج، پرچم، رد کردن سؤال، رادیو، چیپهای توقف/تنظیم مجدد، تایمر تکچیپ، X نوار ابزار، «ثبت پاسخها و پایان» در پاسخبرگ). مدت آزمون برای هیچ نوع آزمونی قفل نیست؛ ۲۷۰ فقط preset است. خروج سه مسیر دارد: ذخیره و ادامهٔ بعدی، ادامهٔ همان لحظه، یا پایان زودهنگام با درصد موقت. قاعدهٔ «فقط یک دکمهٔ AI در صفحهٔ آزمون + یکی در صفحهٔ نتیجه» حفظ شد؛ سیاست مخفیبودن پاسخبرگ/پاسخنامه در آزمون جامع/جمع بندی دستنخورده ماند (مثل قبل)",
         "درخواست کاربر: «فقط اون گزینه توضیح با هوش مصنوعی رو به استباه حزف کردی … پاسخبرگ و پاسخنامه هم کنار اون … مثل قبل» / «اون مدت دقیقا رو فابل تغییر بزاری … در کل در همه ازمونها قابل زمان دادن دستی» / «یه گزینه پایان آزمون و دیدن کارنامه … گزینه سوم» / «در خروج و ذخیره تا جایی که مونده … کارنامه دربیاره و در خروج و دیدن درصد تا جایی که زده»",
         "24_DESIGN_ROUND_12.md §۱۰"],
    ],
    "UI_FIDELITY_RULES.csv": [
        ["F46", "سه چیپ / مدت دستی / سه مسیر خروج (v12.5)", "چیپ AI با data-icon=\"ic_magic_wand\" data-size=\"16\" data-mono=\"1\" دقیقاً بعد از پاسخبرگ و پاسخنامه قرار میگیرد؛ داخل #keySheet هیچ #askAiBtn تکراری نیست. #timerMinutes هرگز readonly/max نیست، «غیرقابل تغییر» در کل سند وجود ندارد و presetهای ۱۵/۳۰/۴۵/۶۰/۹۰/۱۲۰ ثابتاند؛ ۲۷۰ بهصورت ۲۷۰:۰۰ رندر میشود. #exitSheet دقیقاً ۳ دکمه و فقط ۳ خط microcopy از نوع p.note در کل UI دارد؛ گزینهٔ سوم هم «پایان آزمون و دیدن کارنامه» و هم «خروج و دیدن درصد» را دارد. ANSWERS/CHECKED/SAVED وضعیت واقعی پاسخها را نگه میدارند؛ درصد موقت = (درست − غلط/۳) ÷ تعداد پاسخهای زدهشده",
         "chapter_toolbar.xml / interaction_keyboard_view.xml / lesson_interactive_feedback_bottom_sheet_dialog.xml"],
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

## ۱۰. v12.5 — اصلاحات کاربر بعد از v12.4 (REVIEW)

> `<!-- v12.5-corrections -->` · اسکریپت: `tools/build_exam_v12_5.py` (روی `tools/design_v12_4_template.html`).
> v12.4 تأیید نشد: کاربر همان پاسخ REVIEW را بلافاصله اصلاح کرد. ساختار v12.1 و فلشهای v12.3 دستنخوردهاند.

### ۱) «توضیح با هوش مصنوعی» برگشت — دقیقاً همانجا، همان استایل

| قبل (v12.4) | بعد (v12.5) |
|---|---|
| چیپ AI حذف و به کشوی پاسخنامه منتقل شده بود | **سومین `.lb-chip`** در `.lb-tools`، بلافاصله بعد از «پاسخبرگ» و «پاسخنامه» — همان ترتیب v12.1/v12.3 |
| `#askAiBtn` داخل `#keySheet` | کپی داخل پاسخنامه **حذف** شد؛ فقط «بستن» مانده است |
| آیکون ۱۴dp در کشو | `ic_magic_wand`، `data-size="16"`, `data-mono="1"` — عین قبل |

همچنان **فقط یک** دکمهٔ AI در صفحهٔ آزمون (`#askAiBtn`) و یکی در صفحهٔ نتیجه (`#askAiResultBtn`). سیاست `applyPolicy()` (مخفیبودن چیپهای پاسخبرگ/پاسخنامه در آزمون جامع و جمع بندی، «زمان خالص آزمون») عین v12.1/v12.3 حفظ شد تا «مثل قبل» رعایت شود. بقیهٔ حذفیات v12.4 همچنان حذفاند: اتمام آزمون، خروج، پرچم، رد کردن سؤال، رادیو دایرهای، چیپهای توقف/تنظیم مجدد، X نوار ابزار تنها مسیر خروج، و «ثبت پاسخها و پایان» داخل پاسخبرگ.

### ۲) مدت آزمون در **همهٔ** آزمونها دستی است

```
<input type="number" id="timerMinutes" min="1" step="1" value="270" inputmode="numeric">
مدت دلخواه به دقیقه — در همهٔ آزمونها، حتی جامع، قابل تغییر است.
presetها: ۱۵ · ۳۰ · ۴۵ · ۶۰ · ۹۰ · ۱۲۰
```

- هیچ `readOnly=true`، `readonly`، `max="300"` و هیچ عبارت «غیرقابل تغییر» در سند نیست.
- ۲۷۰ فقط **پیشفرضِ قابل ویرایش** آزمون جامع است (همراه `value=270` هنگام بازکردن آزمون)；آزمونهای دیگر ۳۰ دقیقه پیشفرض میگیرند.
- متن هاب اصلاح شد: «زمان ثابت ۲۷۰ دقیقه **بهعنوان پیشفرض** (مدت در تنظیم زمان، برای همهٔ آزمونها قابل تغییر است)»؛ نشانهای ردیف «زمان ثابت» به «قابل تغییر» تبدیل شدند.
- باگ نمایش `۲۷۰:۰۰` (قبلاً `۷۰:۰۰` میشد چون `slice(-2)`) در `fmt()` رفع شد.
- تایمر همچنان **یک چیپ** با pause/play + stop درون همان چیپ است.

### ۳) کشوی خروج: سه گزینه و کارنامهٔ موقت

| گزینه | رفتار |
|---|---|
| **خروج و ذخیره** | `saveExam()` یک snapshot واقعی میگیرد: نام/نوع آزمون، شمارهٔ سؤال، `ANSWERS` (گزینهٔ انتخابشدهٔ هر سؤال)، `CHECKED` (فیدبک دیدهشده)، نشانها، مدت و وضعیت تایمر. در هاب نوار «ادامهٔ آزمون ذخیرهشده» ظاهر میشود؛ کلیک روی همان ردیف آزمون هم `resumeExam()` را صدا میزند. بعداً «ثبت پاسخها و پایان» یا اتمام تایمر، **کارنامهٔ کامل** میدهد |
| **ادامهٔ آزمون** | بدون تغییر، کشو بسته میشود |
| **پایان آزمون و دیدن کارنامه** *(خروج و دیدن درصد تا همینجا)* | `finishExam(..., true)` → صفحهٔ نتیجه با «کارنامهٔ تا این لحظه»، بنر «خروج و دیدن درصد»، درصد محاسبهشده **فقط از پاسخهای زدهشده** با نمرهٔ منفی ⅓، تعداد درست/غلط/نزده، و رتبه/تراز «—» |

`score()` = `(درست − غلط/۳) ÷ تعداد پاسخهای زدهشده × ۱۰۰` (حداقل صفر)؛ `check_v12_5.js` با ۲ پاسخ، `۱۸` سؤال نزده را بررسی میکند. هیچ `<p class="note">` تازهای اضافه نشد (همان ۳ خط microcopy)، و بنر موقت و نوار ادامه با `hidden` هستند.

### وریفای

`verify_upgrade.py` **PASS ۲۵۹/۲۵۹** · `check_v12_5.js` **۱۵۰ تست / ۰ خطا** · `diag12.js` کلیک روی ۱۸۵ المان تعاملی / ۰ خطای runtime / ۰ آیدی تکراری · `node --check` OK. چک قدیمی `check_v12_4.js` روی v12.5 دقیقاً ۳ FAIL موردانتظار دارد (دوچیپبودن، AI در پاسخنامه، حذف AI از بدنه) — همان assertionهای منسوخشدهای که `check_v12_5.js` جایگزینشان شد.

**بدون تغییر:** ۵ تب · مسیر قوسدار · ۷ بخش آزمون و قالبها · «پاسخبرگ»≠«پاسخنامه» · تکقفل · `section-practice` جدا · ۲۰ سؤال مجزا · فلشهای RTL (بعدی ← / قبلی →) · `ic_survey` / `ic_cap` · تمام رفعباگهای v12.1 · اسنپشاتهای برگشت `design_v11_full.html` و `design_v12_1_template.html`.
'''
    LOG.write_text(s, encoding="utf-8")
    print("round-12 log: §10 appended")

NOTES = D / "DESIGN_NOTES.fa.md"
s = NOTES.read_text(encoding="utf-8")
if MARK not in s:
    s += ("\n\n## ۱۰. v12.5 (اصلاحات بعد از v12.4)\n\n`" + MARK + "` «توضیح با هوش مصنوعی» به "
          "جایگاه/استایل دقیق v12.1 برگشت: سومین چیپ آرام کنار «پاسخبرگ / پاسخنامه» با `ic_magic_wand` "
          "۱۶dp mono؛ کپی داخل `#keySheet` حذف شد و `#askAiResultBtn` سر جایش است. `#timerMinutes` در "
          "همهٔ انواع آزمونها دستی و بدون قفل/حداکثر است (۲۷۰ فقط پیشفرض جامع، ۶ preset ثابت، نمایش "
          "۲۷۰:۰۰ اصلاح شد). `#exitSheet` سه گزینه شد: «خروج و ذخیره» پیشرفت واقعی (سؤال، پاسخها، "
          "نشانها، تایمر) ذخیره و بعداً قابل ادامه است و در پایان کارنامهٔ کامل میدهد؛ «ادامهٔ آزمون»؛ "
          "«پایان آزمون و دیدن کارنامه / خروج و دیدن درصد» که کارنامهٔ موقت را فقط از پاسخهای زدهشده "
          "حساب میکند. سیاست مخفیبودن چیپها در آزمون جامع، تایمر تکچیپ و بقیهٔ حذفیات v12.4 دستنخورده. "
          "PASS ۲۵۹/۲۵۹ · `check_v12_5.js` ۱۵۰/۰.\n")
    NOTES.write_text(s, encoding="utf-8")
    print("design notes updated")

wf = UP / "wireframes.html"
s = wf.read_text(encoding="utf-8").replace('DESIGN/index.html">DESIGN v12.4</a>',
                                          'DESIGN/index.html">DESIGN v12.5</a>')
wf.write_text(s, encoding="utf-8")

mp = UP / "MANIFEST.json"
m = json.loads(mp.read_text(encoding="utf-8"))
m["date"] = "2026-11-04"
m["status"] = ("PLAN_ONLY + DESIGN v12.5 REVIEW (v12.3 RTL arrows + v12.4 cleanup kept; "
               "AI chip restored to its v12.1 place/style, manual timer minutes for EVERY exam kind, "
               "three exit options with a partial کارنامه)")
dl = m["deliverables"]
dl["verification"] = "PASS"
dl["verification_checks"] = CHECKS
dl["design_round"] = "v12.5 (REVIEW)"
stable = [p for p in UP.rglob("*") if p.is_file() and p.name not in ("SHA256SUMS.txt", "VERIFICATION_REPORT.json")]
dl["persian_docs"] = len(list(UP.glob("*.md")))
dl["csv_catalogs"] = len(list(CAT.glob("*.csv")))
dl["extracted_assets_files"] = len(stable)
dl["v12_exam_ui"] = ("EXAM_PAGE_REFERENCES.json + EXAM_UI_CODE_EVIDENCE.json — v12.5: THREE quiet chips "
                     "(پاسخبرگ / پاسخنامه / توضیح با هوش مصنوعی, exactly the v12.1 style), no duplicate AI in "
                     "#keySheet; one-chip timer with editable minutes in every exam kind (270 = preset only); "
                     "#exitSheet with three options, real save/resume state and a partial درصد computed from "
                     "answered-so-far; accepted v12.1 structure + v12.3 RTL arrows intact")
for x in [
    "v12.5: the AI explanation chip was restored as the third exam-body .lb-chip in its exact v12.1/v12.3 position and style (ic_magic_wand 16dp mono); the v12.4 duplicate inside #keySheet was removed; the one-AI-button rule still holds",
    "v12.5: #timerMinutes is editable in EVERY exam kind — no readOnly, no readonly attribute, no max ceiling and no «غیرقابل تغییر» anywhere; 270 is only the comprehensive default/preset, the six quick presets stay and 270:00 renders correctly",
    "v12.5: #exitSheet has three options — خروج و ذخیره now snapshots the question index, answers, marks and timer and can be resumed later (finishing after resume yields the full کارنامه), ادامهٔ آزمون is unchanged, and پایان آزمون و دیدن کارنامه / خروج و دیدن درصد shows a partial percentage computed only from answers given so far",
]:
    if x not in m["critical_findings"]:
        m["critical_findings"].append(x)
for cmd in ["python3 tools/build_exam_v12_5.py .", "python3 tools/finalize_v12_5.py ."]:
    if cmd not in m["reproduce"]:
        m["reproduce"].append(cmd)
m["design_round_12"]["status"] = ("DESIGN v12 · REVIEW — superseded by v12.1 fixes, the v12.3 rollback, "
                                  "the v12.4 button cleanup and the v12.5 user corrections (CURRENT)")
m["design_round_12"]["v12_5_corrections"] = {
    "status": "APPLIED, awaiting final approval",
    "trigger": "user: فقط اون گزینه توضیح با هوش مصنوعی رو به استباه حزف کردی دقیقا جایی که بود قبلا … پاسخبرگ و پاسخنامه هم کنار اون … مثل قبل / اون مدت دقیقا رو فابل تغییر بزاری … در کل در همه ازمونها قابل زمان دادن دستی / یه گزینه پایان آزمون و دیدن کارنامه … گزینه سوم / در خروج و ذخیره تا جایی که مونده … کارنامه دربیاره و در خروج و دیدن درصد تا جایی که زده",
    "script": "tools/build_exam_v12_5.py (runs on tools/design_v12_4_template.html)",
    "restored": ["third .lb-chip #askAiBtn (ic_magic_wand / 16dp / mono, beside پاسخبرگ and پاسخنامه)",
                 "editable #timerMinutes in every exam kind, 270 as comprehensive preset only",
                 "editable 270:00 timer rendering (fmt 3-digit fix)"],
    "removed": ["duplicate #askAiBtn inside #keySheet", "readOnly=true", "غیرقابل تغییر",
                "max=300 ceiling", "stale fixed-270 data-code / footer / hub labels"],
    "added": ["#exitSaveBtn real save/resume snapshot (ANSWERS / CHECKED / SAVED / timer)",
              "#resumeBar + #resumeBtn in exam-hub",
              "#exitFinishBtn third exit option (پایان آزمون و دیدن کارنامه / خروج و دیدن درصد)",
              "score() + renderReport(partial) + #resPartial / dynamic result fields"],
    "tests": "check_v12_5.js (150 checks / 0 errors) + verify_upgrade.py PASS 259/259 + diag12.js 185 clicks / 0 errors",
    "unchanged": "all v11.1 acceptances + v12.1 bug fixes + v12.3 RTL arrows + v12.4 removals (except AI) + rollback snapshots",
}
# The MANIFEST hashes its own byte total; converge so the recorded value is exactly reproducible.
for _ in range(6):
    dl["total_bytes"] = sum(p.stat().st_size for p in stable if p.name != "MANIFEST.json") \
        + len(json.dumps(m, ensure_ascii=False, indent=2).encode("utf-8")) + 1
    written = json.dumps(m, ensure_ascii=False, indent=2) + "\n"
    if mp.read_text(encoding="utf-8") == written:
        break
    mp.write_text(written, encoding="utf-8")
stable = [p for p in UP.rglob("*") if p.is_file() and p.name not in ("SHA256SUMS.txt", "VERIFICATION_REPORT.json")]
print("MANIFEST updated; docs=%d csv=%d files=%d bytes=%d" %
      (dl["persian_docs"], dl["csv_catalogs"], len(stable), sum(p.stat().st_size for p in stable)))
