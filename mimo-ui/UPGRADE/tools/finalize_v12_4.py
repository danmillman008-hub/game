#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""finalize_v12_4.py — extra-button cleanup round: catalogs / docs / MANIFEST. Idempotent."""
from __future__ import annotations
import csv
import json
from pathlib import Path

UP = Path(__file__).resolve().parents[1]
CAT, D = UP / "CATALOGS", UP / "DESIGN"
MARK = "<!-- v12.4-cleanup -->"

ROWS = {
    "DESIGN_FEEDBACK.csv": [
        ["F-69", "صفحهٔ آزمون دکمههای اضافی دارد: «توضیح با هوش مصنوعی / اتمام آزمون / خروج»، پرچم کنار تایمر، «رد کردن سؤال»، متن تکراری «زمان تنظیم نشده»، دایرهٔ رادیویی سمت راست گزینهها، و چیپهای «توقف / تنظیم مجدد» بعد از ستکردن تایمر",
         "v12.4: ردیف چیپها به فقط «پاسخبرگ / پاسخنامه» خلاص شد (خروج همان X نوار ابزار است؛ اتمام آزمون از داخل پاسخبرگ؛ توضیح AI به کشوی پاسخنامه منتقل شد). پرچم، «رد کردن سؤال»، متن وضعیت تکراری و دایرهٔ رادیویی حذف شدند — گزینهها حالا با «۱.» شروع میشوند و کل باکس رنگ عوض میکند. تایمر یک دکمهٔ واحد شد: بزنی تنظیم/توقف/ادامه، و کنار زمانش علامت توقف-پلی و استاپ ظاهر میشود",
         "24_DESIGN_ROUND_12.md §۹, tools/build_exam_v12_4.py", "APPLIED"],
    ],
    "SCOPE_DECISIONS.csv": [
        ["D49", "صفحهٔ اجرای آزمون", "MINIMAL_EXAM_CONTROLS_V12_4",
         "حداقل کنترلها: فقط دو چیپ پاسخبرگ/پاسخنامه، X نوار ابزار برای خروج، «ثبت پاسخها و پایان» داخل پاسخبرگ برای اتمام، یک CTA تمامعرض ادامه + دو مربع ۴۸dp. «ادامه» بدون انتخاب همان رد کردن سؤال است. تایمر فقط یک چیپ در نوار ابزار؛ حالت اجرا داخل همان چیپ علامت pause/play و stop میگیرد. هیچ چیپ توقف/تنظیم مجدد جداگانهای وجود ندارد",
         "درخواست کاربر: «خیلی دکمه هارو اضافی گزاشتی اینهارو حدف کنی … صرفا یکی روی تایمر بزنه علامت ایست میاد»", "24_DESIGN_ROUND_12.md §۹"],
    ],
    "UI_FIDELITY_RULES.csv": [
        ["F45", " minimal controls / تایمر تکدکمهای", "هر کنترل فقط یکبار: خروج = X نوار ابزار (نه چیپ جدا)، اتمام = «ثبت پاسخها و پایان» در پاسخبرگ، AI = داخل پاسخنامه، پاسخبرگ/پاسخنامه = دو چیپ. شمارهٔ سؤال و تنظیم زمان دوبار نوشته نمیشوند. گزینهٔ تستی با شماره شروع میشود و نشانگر انتخاب، رنگ خود باکس است (بدون رادیو دایرهای). تایمر حالتدار: idle = «تنظیم زمان»، running/paused = شمارش معکوس + pause/play + stop داخل همان چیپ؛ کلیک روی خود چیپ توقف/ادامه است",
         "interaction_keyboard_view.xml / chapter_toolbar.xml / lesson_skip"],
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

## ۹. v12.4 — حذف دکمههای اضافی و تایمر تکدکمهای

> `<!-- v12.4-cleanup -->` · اسکریپت: `tools/build_exam_v12_4.py` (روی `tools/design_v12_3_template.html`). ساختار صفحهٔ آزمون همان v12.1 تأییدشده است؛ فقط اضافات حذف شدند.

### حذفشده

| چه بود | چرا | جایگزین |
|---|---|---|
| چیپ **«توضیح با هوش مصنوعی»** | دکمهٔ اضافی در بدنهٔ آزمون | همان action داخل **کشوی پاسخنامه** رفت (جایی که توضیح سؤال معنا دارد)؛ `#askAiResultBtn` صفحهٔ نتیجه هم سر جایش است |
| چیپ **«اتمام آزمون»** | تکرار | «ثبت پاسخها و پایان» داخل پاسخبرگ |
| چیپ **«خروج»** | «علامت ضربدر بالا هست، نیازی نیست» | همان `X` نوار ابزار (`data-sheet="exitSheet"`) |
| **پرچم** کنار تایمر | اضافی و باعث بدقلقیشدن دکمهٔ تایمر | پاسخبرگ فقط از چیپ «پاسخبرگ» باز میشود |
| چیپهای **«توقف» / «تنظیم مجدد»** | بعد از ستکردن تایمر ظاهر میشدند و اضافیاند | داخل خود چیپ تایمر (پایینتر) |
| **«رد کردن سؤال»** | «همون طرح بزنه ادامه … اگر چیزی انتخاب نکنه همون میشه» | `#nextQ` بدون گزینهٔ انتخابشده مستقیم سؤال بعدی میرود؛ رشتهٔ `lesson_skip` بعنوان شاهد کد در `data-code` فوتر ماند |
| **«زمان تنظیم نشده»** | «تنظیم زمان» دوبار نوشته شده بود؛ «زمان تنظیم شده یا نشده چه فرق داره؟» | فقط برچسب چیپ تایمر |
| **دایرهٔ رادیویی** سمت راست گزینهها | «همون 1. شروع بشه کافیه، چون موقع کلیک رنگ اون باکس هم عوض میشه» | گزینهها با `۱.` / `۲.` / `۳.` / `۴.` شروع میشوند؛ رنگ شماره هم با `.opt.on / .correct / .wrong` عوض میشود |

ردیف چیپهای ابزار حالا **فقط دو تاست**: «پاسخبرگ» و «پاسخنامه». فوتر همان **یک CTA بنفش تمامعرض + دو مربع ۴۸dp** است، بدون لینک اضافی.

### تایمر تکدکمهای

```
idle      [ 🕘 تنظیم زمان ]                       ← بزنی کشوی تنظیم باز میشود
running   [ 🕘 ۲۶۹:۴۲ | ⏸  ⏹ ]                    ← بزنی روی خود چیپ = توقف
paused    [ 🕘 ۲۶۹:۴۲ | ▶  ⏹ ]                    ← بزنی = ادامه
finished  [ 🕘 ۰۰:۰۰ ]                            ← کنترلها مخفی
```

همانطور که خواسته شد: «صرفا یکی روی تایمر بزنه علامت ایست میاد … علامت پلی و استاپ میاد کنار تایم». علامت توقف (`tm-bars`، دوبار خطی)، پلی (`ic_play` دکدشده از APK) و استاپ (`tm-square`) همگی **داخل همان چیپ ۵۲dp** و فقط در حالت اجرا نمایان میشوند؛ هیچ چیپ جداگانهای به بدنه اضافه نمیشود. `pauseOrResume()` مشترکِ کلیک روی چیپ و دکمهٔ کوچک pause/play است؛ استاپ تایمر را پاک میکند و برچسب به «تنظیم زمان» برمیگردد.

**بدون تغییر:** ۵ تب · مسیر قوسدار · ۷ بخش آزمون و قالبها · ۲۷۰ دقیقهٔ ثابت و تایمر فقط داخل آزمون · «پاسخبرگ»≠«پاسخنامه» · تکقفل · `section-practice` جدا · ۲۰ سؤال مجزا · فلشهای RTL (بعدی ← / قبلی →) · لوگوی `ic_survey` / `ic_cap` · تمام رفعباگهای v12.1 · اسنپشاتهای برگشت `design_v11_full.html` و `design_v12_1_template.html`.

**وریفای:** `verify_upgrade.py` PASS ۲۴۹/۲۴۹ · `check_v12_4.js` ۱۳۲ تست / ۰ خطا · `node --check` OK · کلیک روی ۱۸۳ المان تعاملی بدون خطای runtime · ۰ آیدی تکراری.
'''
    LOG.write_text(s, encoding="utf-8")
    print("round-12 log: §9 appended")

NOTES = D / "DESIGN_NOTES.fa.md"
s = NOTES.read_text(encoding="utf-8")
if MARK not in s:
    s += ("\n\n## ۹. v12.4 (حذف اضافات)\n\n`" + MARK + "` چیپهای «AI / اتمام آزمون / خروج / توقف / تنظیم مجدد»، پرچم کنار تایمر، "
          "«رد کردن سؤال»، متن تکراری «زمان تنظیم نشده» و دایرهٔ رادیویی گزینهها حذف شدند. ردیف ابزار فقط "
          "«پاسخبرگ / پاسخنامه» است؛ خروج = X نوار ابزار، اتمام = داخل پاسخبرگ، AI = داخل کشوی پاسخنامه. "
          "گزینهها با شماره شروع میشوند و کل باکس رنگ میگیرد. تایمر **یک دکمهٔ واحد** است: بزنی تنظیم/توقف/ادامه، "
          "و کنار زمانش pause/play + stop ظاهر میشود. ساختار v12.1 دستنخورده. PASS ۲۴۹/۲۴۹ · `check_v12_4.js` ۱۳۲/۰.\n")
    NOTES.write_text(s, encoding="utf-8")
    print("design notes updated")

wf = UP / "wireframes.html"
s = wf.read_text(encoding="utf-8").replace('DESIGN/index.html">DESIGN v12.3</a>', 'DESIGN/index.html">DESIGN v12.4</a>')
wf.write_text(s, encoding="utf-8")

mp = UP / "MANIFEST.json"
m = json.loads(mp.read_text(encoding="utf-8"))
m["date"] = "2026-11-04"
m["status"] = ("PLAN_ONLY + DESIGN v12.4 REVIEW (v12.3 rollback to v12.1 + extra exam buttons removed "
               "+ one-chip timer)")
dl = m["deliverables"]
dl["verification"] = "PASS"
dl["verification_checks"] = 249
dl["design_round"] = "v12.4 (REVIEW)"
stable = [p for p in UP.rglob("*") if p.is_file() and p.name not in ("SHA256SUMS.txt", "VERIFICATION_REPORT.json")]
dl["persian_docs"] = len(list(UP.glob("*.md")))
dl["csv_catalogs"] = len(list(CAT.glob("*.csv")))
dl["extracted_assets_files"] = len(stable)
dl["total_bytes"] = sum(p.stat().st_size for p in stable)
dl["v12_exam_ui"] = ("EXAM_UI_CODE_EVIDENCE.json + EXAM_PAGE_REFERENCES.json — v12.4: exam tool row reduced "
                     "to پاسخبرگ / پاسخنامه only; X exits; end exam from پاسخبرگ; AI in پاسخنامه; one-chip timer "
                     "with inline pause/play + stop; no radio circle; accepted v12.1 structure intact")
for x in [
    "v12.4: extra exam chips (AI / اتمام آزمون / خروج / توقف / تنظیم مجدد), the flag next to the timer, «رد کردن سؤال», the duplicate «زمان تنظیم نشده» line and the option radio circles were removed at the user's request",
    "v12.4: the timer is ONE chip — tap to set / pause / resume; while running it grows an inline pause-play + stop pair next to the countdown, no separate control chips",
    "v12.4: options start with their number (۱.) and the whole card changes colour on selection; AI explanation relocated into the پاسخنامه bottom sheet",
]:
    if x not in m["critical_findings"]:
        m["critical_findings"].append(x)
for cmd in ["python3 tools/build_exam_v12_4.py .", "python3 tools/finalize_v12_4.py ."]:
    if cmd not in m["reproduce"]:
        m["reproduce"].append(cmd)
m["design_round_12"]["status"] = "DESIGN v12 · REVIEW — superseded by v12.1 fixes, the v12.3 rollback and the v12.4 button cleanup (CURRENT)"
m["design_round_12"]["v12_4_cleanup"] = {
    "status": "APPLIED, awaiting final approval",
    "trigger": "user: خیلی دکمه هارو اضافی گزاشتی … اون خروج رو حدف کن … دایره نیاز نیست … رد کردن سوال اضافیه … دوبار نوشتی … پرچم حزف کن … صرفا یکی روی تایمر بزنه علامت ایست میاد",
    "script": "tools/build_exam_v12_4.py (runs on tools/design_v12_3_template.html)",
    "removed": ["lb-chip AI", "lb-chip اتمام آزمون", "lb-chip خروج", "lb-chip توقف", "lb-chip تنظیم مجدد",
                "ln-report flag", "lk-skip رد کردن سؤال", "timerStateText", "opt-radio"],
    "timer": "ONE chip: idle=تنظیم زمان, running/paused=countdown + inline pause/play + stop; tap the chip to pause/resume",
    "ai": "moved into #keySheet (پاسخنامه); #askAiResultBtn unchanged",
    "tests": "check_v12_4.js (132 checks / 0 errors) + verify_upgrade.py PASS 249/249",
    "unchanged": "all v11.1 acceptances + v12.1 bug fixes + v12.3 RTL arrows + rollback snapshots",
}
mp.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("MANIFEST updated; docs=%d csv=%d files=%d bytes=%d" %
      (dl["persian_docs"], dl["csv_catalogs"], len(stable), sum(p.stat().st_size for p in stable)))
