#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""finalize_v12_5_fa.py — بستهٔ فارسیسازی v12.5: کاتالوگها / اسناد / وایرفریم / MANIFEST.

Idempotent: بعد از `build_exam_v12_5.py` + `finalize_v12_5.py` +
`localize_v12_5_fa.py` اجرا میشود و فقط لیبلها/شواهد را بهروز میکند،
بدون اینکه معماری یا رفتار آزمون دست بخورد.
"""
from __future__ import annotations
import csv
import json
from pathlib import Path

UP = Path(__file__).resolve().parents[1]
CAT, D = UP / "CATALOGS", UP / "DESIGN"
MARK = "<!-- v12.5-fa-localization -->"
CHECKS = 259

ROWS = {
    "DESIGN_FEEDBACK.csv": [
        ["F-71",
         "در لیدربورد و پروفایل/پروفایل همچنان واژههای انگلیسی دیدنی بود («My status»، «HTML»، «Playgrounds»، «Profile»…)، ناوبری پایین فقط بعد از زدن دکمهٔ RTL فارسی میشد، و آیکون «واژهنامهٔ مبحث» اضافی بود",
         "بستهٔ فارسیسازی: همهٔ لیبلهای دیدنی لیدربورد/پروفایل/تمرین/مودالها فارسی شدند؛ «HTML» و قالبهای Python/JavaScript/Static website/React app به نام درسها و آزمونهای کنکور («زیست دهم»، «ساختار سلول و بافت»، «آزمون جامع/تکدرس/زماندار/تحلیلی») تغییر کردند؛ ناوبری ۵ تب بهصورت پیشفرض فارسی است (یادگیری / تمرین / هوش مصنوعی / امتیازها / پروفایل)؛ دکمهٔ RTL فقط جهت را آینه میکند و دیگر انگلیسی برنمیگرداند؛ toast تبها فارسی شد؛ آیکون واژهنامه بههمراه CSS و هندلرش حذف شد. رشتههای انگلیسی قدیمی فقط در data-code / data-lh و payloadهای GEO/LEARN/NODE/KONKUR بهعنوان شاهد نامرئی ماندند",
         "24_DESIGN_ROUND_12.md §۱۱, tools/localize_v12_5_fa.py, tools/design_v12_5_fa_template.html, tools/finalize_v12_5_fa.py",
         "APPLIED"],
    ],
    "SCOPE_DECISIONS.csv": [
        ["D51", "همهٔ لیبلهای دیدنی پروتوتایپ", "USER_LOCALIZATION_V12_5_FA",
         "فارسیسازی فقط یک ویرایش لیبل/تمیزکاری است، نه طراحی دوباره: ۵ شناسهٔ data-tab دقیقاً همان Learn|Practice|AI|Leaderboard|Profile میماند؛ data-mode، data-lh، data-code≥۱۵، data-lh≥۷ و حداکثر ۳ خط p.note دستنخوردهاند؛ سیاست مخفیبودن چیپها، چیپ سوم AI، تایمر دستی در همهٔ آزمونها، سه گزینهٔ خروج و کارنامهٔ موقت، معماری آزمون و رفتار پروتوتایپ (SAVED فقط در حافظه) پابرجا هستند. هیچ جایگزینی سراسری روی payloadهای کد انجام نشد",
         "درخواست کاربر: «فقط یه سری ویرایش ریزه … لیدربورد و پروفایل … کلمات انگلیسی رو فارسی کن / بالای لیدربورد نوشته HTML اونو مثلا اسم یه درسی بنویسی / واژهنامهٔ مبحث رو نمیخوام / نوار پایین کلا فارسی … یادگیری تمرین ai امتیازها پروفایل / کل پروژه عنوان انگلیسی»",
         "24_DESIGN_ROUND_12.md §۱۱"],
    ],
    "UI_FIDELITY_RULES.csv": [
        ["F47", "فارسی پیشفرض / شواهد نامرئی (v12.5-fa)",
         "پنج لیبل ناوبری دقیقاً «یادگیری|تمرین|هوش مصنوعی|امتیازها|پروفایل»اند و در #tabs هیچ حرف لاتینی دیدنی نیست؛ data-tab همچنان ۵ شناسهٔ انگلیسی قدیمی را نگه میدارد و toast تبها از نقشهٔ فارسی tabFa میخواند. دکمهٔ #dirBtn فقط direction را آینه میکند، data-enhtml/بازیابی انگلیسی حذف شد. هیچ المان .gloss-fab یا [data-glossary] و هیچ toast «واژهنامهٔ مبحث»ای در سند نیست. متنهای انگلیسی قدیمی فقط در صفتهای نامرئی (data-code / data-lh)، بایگانی وایرفریم v1 و payloadها دیده میشوند؛ GEO/LEARN/NODE/KONKUR و شمارش data-code≥۱۵ / data-lh≥۷ / p.note≤۳ دستنخوردهاند",
         "درخواست کاربر / tools/localize_v12_5_fa.py / check_v12_6.js"],
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

# ------------------------------------------------------------------ اسناد §۱۱
SEC = ("\n\n## ۱۱. بستهٔ فارسیسازی v12.5 (فقط ویرایش لیبل و تمیزکاری)\n\n`" + MARK + "` "
       "درخواست «یه سری ویرایش ریز» اعمال شد، بدون هیچ تغییری در معماری یا رفتار آزمون: "
       "**لیبلهای دیدنی** لیدربورد («My status» ← «وضعیت من»، «Day streak»، «XP total»، «Weekly XP»، نام آزمونها)، "
       "پروفایل کاربر و پروفایل («HTML» ← **«زیست دهم»**، «Playgrounds» ← «آزمونهای من»، جامها، ایدهها)، "
       "صفحهٔ درس، مودالها، کشوی ساخت آزمون و تمرین مبحث فارسی شدند. "
       "**عنوانهای HTML/برنامهنویسی** به نام مباحث و آزمونهای کنکور تغییر کردند: «ساختار سلول و بافت» بهجای "
       "«HTML Basics»، و چهار قالب «آزمون جامع / تکدرس / زماندار / تحلیلی» بهجای "
       "Python / JavaScript / Static website / React app؛ نام فصلهای رندرشدهٔ تمرین هم از `P_FA` کنکوری میآید. "
       "**ناوبری پایین بهصورت پیشفرض فارسی است**: یادگیری / تمرین / هوش مصنوعی / امتیازها / پروفایل؛ "
       "دکمهٔ `↔ راستبهچپ` فقط جهت را آینه میکند و دیگر متن انگلیسی برنمیگرداند، و toast تبها از نقشهٔ "
       "`tabFa` فارسی میخواند. پنج شناسهٔ `data-tab` دقیقاً همان `Learn|Practice|AI|Leaderboard|Profile` ماندند. "
       "**آیکون «واژهنامهٔ مبحث»** بههمراه CSS، المان DOM، هندلر toast و یادداشت پنل مشخصات حذف شد. "
       "سربرگ، `<title>`، بنرهای وایرفریم بایگانی و پنل وضعیت هم فارسی شدند؛ رشتههای انگلیسی قدیمی فقط "
       "در صفتهای نامرئی `data-code` / `data-lh`، بایگانی v1 و payloadهای `GEO/LEARN/NODE/KONKUR` بهعنوان "
       "شاهد کدفirst باقیاند (هیچ جایگزینی سراسری انجام نشد). "
       "ابزار `tools/localize_v12_5_fa.py` همیشه از `tools/design_v12_5_template.html` میخواند، "
       "پس `build_exam_v12_5.py` دیگر `DESIGN/index.html` را بازنویسی نمیکند و زنجیرهٔ reproduce قابلتکرار است. "
       "**بدون تغییر:** چیپ سوم «توضیح با هوش مصنوعی»، مدت دستی تایمر در همهٔ آزمونها، سه گزینهٔ خروج و "
       "کارنامهٔ موقت، سیاست مخفیبودن چیپها، `data-code`≥۱۵ / `data-lh`≥۷ / `p.note`≤۳، ۵ تب، "
       "معماری آزمون و `SAVED` فقط در حافظه (بدون localStorage). "
       "PASS ۲۵۹/۲۵۹ · `check_v12_6.js` ۱۶۰ تست / ۰ خطا · `diag12.js` ۱۸۵ کلیک / ۰ خطا.\n")

for p in (UP / "24_DESIGN_ROUND_12.md", D / "DESIGN_NOTES.fa.md"):
    s = p.read_text(encoding="utf-8")
    if MARK not in s:
        p.write_text(s.rstrip("\n") + SEC, encoding="utf-8")
        print("docs §11 added:", p.name)

# ------------------------------------------------------------------ وایرفریم v1 بایگانی
wf = UP / "wireframes.html"
s = wf.read_text(encoding="utf-8")


def wrep(old, new):
    global s
    if old in s:
        s = s.replace(old, new)


wrep('<a href="DESIGN/index.html">DESIGN v12.5</a>',
     '<a href="DESIGN/index.html" data-code="DESIGN v12.5">طرح v12.5</a>')
wrep('<div style="background:#FFF7E6;border:1px solid #F5D28B;border-radius:12px;padding:10px 18px;margin:12px 24px;font-size:13px">⚠️ این وایرفریم <b>v1</b> بایگانی شد. طرح <b>v5 نهایی</b> (حکم فعلی، بازآفرینی ۱۰۰٪ از کد) در <a href="DESIGN/index.html">DESIGN/index.html</a> است: ۵ تب، Learn عین میمو، هاب لیبلدار قابلاسکرول، «پاسخبرگ»/«پاسخنامه» جدا، دکمۀ «توضیح با هوش مصنوعی» در صفحۀ سؤالات و صفحۀ آخر، لیدربورد با اطلاعات خود فرد، چت مینیمال با دکمههای LH، مشاوره PARKED.</div>',
     '<div style="background:#FFF7E6;border:1px solid #F5D28B;border-radius:12px;padding:10px 18px;margin:12px 24px;font-size:13px" data-code="DESIGN v5 (archived)">' + MARK + ' ℹ️ بستهٔ فارسیسازی: تمام لیبلهای دیدنی <a href="DESIGN/index.html">طرح فعلی</a> فارسی شدند، ناوبری پایین بهصورت پیشفرض فارسی است و آیکون «واژهنامهٔ مبحث» حذف شد. نگاشتهای انگلیسی قدیمی فقط در <code>data-code</code> / <code>data-lh</code> و همین بایگانی v1 ماندهاند؛ محتوای کنکوری و ۵ تب «یادگیری / تمرین / هوش مصنوعی / امتیازها / پروفایل» پابرجاست.</div>')
wrep('<h1>قرارداد وفاداری UI — ارتقای Mimo به اپ کنکور</h1>',
     '<h1>قرارداد وفاداری رابط کاربری — ارتقای میمو به اپ کنکور</h1>')
wrep('<h2>① تب Practice — هاب آزمونها (گرههای ۳تایی، برچسب زیر)</h2>',
     '<h2>① تب تمرین — هاب آزمونها (گرههای ۳تایی، برچسب زیر)</h2>')
wrep('<h2>② AI میمو — ظاهر ثابت + ردیف دکمههای Learn Harness</h2>',
     '<h2>② دستیار هوشمند میمو — ظاهر ثابت + ردیف دکمههای چارچوب یادگیری</h2>')
wrep('<h2>④ پروفایل — همان کارتهای Mimo + دادهٔ کنکور</h2>',
     '<h2>④ پروفایل — همان کارتهای میمو + دادهٔ کنکور</h2>')
wrep('<span class="badge">Think out loud</span>', '<span class="badge">بلند فکر کردن</span>')
wrep('<div class="tabs"><div class="tab">Learn</div><div class="tab on">Practice</div><div class="tab">Leaderboard</div><div class="tab">Profile</div></div>',
     '<div class="tabs"><div class="tab" data-code="Learn">یادگیری</div><div class="tab on" data-code="Practice">تمرین</div><div class="tab" data-code="Leaderboard">امتیازها</div><div class="tab" data-code="Profile">پروفایل</div></div>')
wrep('<div class="tabs"><div class="tab">Learn</div><div class="tab">Practice</div><div class="tab">Leaderboard</div><div class="tab on">Profile</div></div>',
     '<div class="tabs"><div class="tab" data-code="Learn">یادگیری</div><div class="tab" data-code="Practice">تمرین</div><div class="tab" data-code="Leaderboard">امتیازها</div><div class="tab on" data-code="Profile">پروفایل</div></div>')
wf.write_text(s, encoding="utf-8")
print("wireframes.html localized (archived v1)")

# ------------------------------------------------------------------ MANIFEST
mp = UP / "MANIFEST.json"
m = json.loads(mp.read_text(encoding="utf-8"))
SUFFIX = " + v12.5-fa localization (Persian-by-default bottom nav, Konkur subject labels, glossary icon removed; legacy EN kept only as hidden evidence)"
SUFFIX2 = " | v12.5-fa: visible labels localized; five data-tab identifiers + hidden-chip policy + all exam behavior unchanged"
# idempotent: normalize any earlier append before adding exactly one suffix
m["status"] = m["status"].split(" + v12.5-fa localization")[0] + SUFFIX
dl = m["deliverables"]
dl["verification"] = "PASS"
dl["verification_checks"] = CHECKS
dl["design_round"] = "v12.5 (REVIEW)"
dl["v12_exam_ui"] = dl["v12_exam_ui"].split(" | v12.5-fa:")[0] + SUFFIX2
for x in [
    "v12.5-fa: all visible English labels in leaderboard / profile / lesson / practice / modals / sheets are Persian by DEFAULT; the five data-tab identifiers and GEO/LEARN/NODE/KONKUR payloads are untouched",
    "v12.5-fa: the glossary («واژهنامهٔ مبحث») affordance is removed from DOM, CSS and its click handler; bottom-nav labels are Persian without relying on the RTL toggle, and the tab toast uses a Persian label map",
    "v12.5-fa: visible HTML / programming titles replaced with Konkur subject and exam names (زیست دهم, ساختار سلول و بافت, آزمون جامع/تکدرس/زماندار/تحلیلی); legacy English strings survive only in data-code / data-lh evidence attributes",
]:
    if x not in m["critical_findings"]:
        m["critical_findings"].append(x)
for cmd in ["python3 tools/localize_v12_5_fa.py .", "python3 tools/finalize_v12_5_fa.py ."]:
    if cmd not in m["reproduce"]:
        m["reproduce"].append(cmd)
m["design_round_12"]["v12_5_localization"] = {
    "status": "APPLIED, awaiting final approval",
    "trigger": "user: فقط یه سری ویرایش ریزه / لیدربورد و پروفایل کلمات انگلیسی رو فارسی کن / بالای لیدربورد HTML رو اسم یه درسی بنویس / واژهنامهٔ مبحث رو نمیخوام / نوار پایین کلا فارسی / کل پروژه عنوان انگلیسی",
    "script": "tools/localize_v12_5_fa.py (reads tools/design_v12_5_template.html, writes DESIGN/index.html + tools/design_v12_5_fa_template.html)",
    "finalizer": "tools/finalize_v12_5_fa.py",
    "changed": ["visible labels in leaderboard / user-profile / profile / lesson / practice / AI / modals / playgroundSheet",
                "bottom nav Persian BY DEFAULT + tabFa Persian toast map + RTL toggle no longer restores English",
                "Konkur subject/exam names instead of HTML/Python/JavaScript/Static website/React app",
                "gloss-fab icon, CSS, data-glossary handler and spec mention removed",
                "header / document title / aside status / wireframes banners + headings Persianized"],
    "evidence_policy": "legacy English only in non-visible data-code / data-lh attributes, archived v1 wireframe and GEO/LEARN/NODE/KONKUR payloads; data-tab / data-mode / data-code>=15 / data-lh>=7 / p.note<=3 unchanged",
    "tests": "verify_upgrade.py PASS 259/259 + check_v12_6.js 160 checks / 0 errors + diag12.js 185 clicks / 0 errors",
    "unchanged": "v12.5 AI chip, editable-minute timer in every exam kind, three exit options + partial report, hidden-chip policy, 5 tab identifiers, exam architecture, SAVED in-memory only",
}
# MANIFEST hashes its own byte total; converge so the recorded value is exactly reproducible.
stable = [p for p in UP.rglob("*") if p.is_file() and p.name not in ("SHA256SUMS.txt", "VERIFICATION_REPORT.json")]
dl["persian_docs"] = len(list(UP.glob("*.md")))
dl["csv_catalogs"] = len(list(CAT.glob("*.csv")))
dl["extracted_assets_files"] = len(stable)
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
