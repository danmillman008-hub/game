#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""finalize_v9.py — round-9 docs/catalogs/banners/MANIFEST. Idempotent."""
from __future__ import annotations
import csv
import json
from pathlib import Path

UP = Path(__file__).resolve().parents[1]
CAT = UP / "CATALOGS"
D = UP / "DESIGN"
MARK = "<!-- v9-banner -->"

APPEND = {
    "DESIGN_FEEDBACK.csv": ("F-53", [
        ["F-53", "معماری گرهها همچنان نیاز به توجه دارد؛ بهتر شبیهسازی کن", "بازبینی مجدد کد: ۱۳ شِیپ، ۱۰ وکتور، ۱۳۹۶ دایمنشن، ۲ انیمیشن؛ ۷ تصحیح عددی نسبت به v8", "21_DESIGN_ROUND_9.md §۲, DESIGN/NODE_CODE_GEOMETRY.json::code_fidelity", "APPLIED"],
        ["F-54", "قوس نده و گرهها رو در یک خط عمومی/عمودی قرار بده", "همهٔ ۶ گره روی محور x=196؛ بدون زیگزاگ/زانوی Q؛ مسیر = یک path صاف M196 0 V620 با گرادیان سخت", "DESIGN/index.html#learn, DESIGN/NODE_CODE_GEOMETRY.json::nodeGeometry.layout", "APPLIED"],
        ["F-55", "بازم کدش رو بازبینی کن و بهتر شبیهسازی کن", "شعاع ۱۶dp از dimen، ضخامت ۶dp، فاصلهٔ ۱۲dp، بولتهای ic_bolt_charged/mastered، توالی خطی حالتها، تایمینگ ۲۲۰/۴۰۰ms", "DESIGN/index.html, CATALOGS/MIMO_PATH_NODES.csv (V9-01..16)", "APPLIED"],
    ]),
    "SCOPE_DECISIONS.csv": ("D33", [
        ["D33", "چیدمان گرهها", "SINGLE_VERTICAL_LINE_NO_CURVES", "همهٔ گرهها محور x=196، یک خط صاف پیوسته، صفر فرمان قوس", "بازخورد دور نهم «قوس نده … یک خط»", "21_DESIGN_ROUND_9.md §۱"],
        ["D34", "اعداد هندسی", "RECODED_FROM_DIMEN_XML", "شعاع ۱۶dp / ضخامت ۶dp / فاصلهٔ ۱۲dp / آیکن ۴۸dp، همگی از منابع کد", "SOURCE/values/values/dimen.xml", "DESIGN/NODE_CODE_GEOMETRY.json::code_fidelity.dimens"],
        ["D35", "حالتها و وکتورها", "LINEAR_STATES_REAL_VECTORS", "done/done/current/next(بدون قفل)/ic_bolt_charged/ic_bolt_mastered", "PathMapViewModel + drawable vectors", "CATALOGS/MIMO_PATH_NODES.csv"],
    ]),
    "UI_FIDELITY_RULES.csv": ("F29", [
        ["F29", "یک خط عمودی واحد", "axis_x=196، ۶ گره، بدون قوس/زیگزاگ، ۱ path connector", "NODE_CODE_GEOMETRY.json::nodeGeometry.layout + F-54"],
        ["F30", "اعداد از کد", "corner 16dp / stroke 6dp / gap 12dp / icon 48dp", "dimen.xml + glance_component_btn_square.xml + progress_bar_chapter.xml"],
        ["F31", "بولتهای واقعی", "ic_bolt_charged و ic_bolt_mastered بهجای ic_flash/ic_bolt", "SOURCE/res/drawable/*.xml"],
    ]),
    "OPEN_QUESTIONS.csv": ("U10", [
        ["U10", "آیا «یک خط عمومی» بهمعنای محور عمودی صاف (بدون هیچ جابهجایی افقی) است؟", "ASSUMED: بله — عمومی = عمودی؛ ۶ گره همهمحور، بدون قوس. اگر منظور خط افقی یا جابهجایی ملایم بود، قابل برگشت است", "no", "تأیید نهایی دیزاین"],
    ]),
}
for name, (first_id, new_rows) in APPEND.items():
    p = CAT / name
    with p.open(encoding="utf-8", newline="") as f:
        existing = list(csv.reader(f))
    body = existing[1:]
    present = {r[0] for r in body if r}
    todo = [r for r in new_rows if r[0] not in present]
    if todo:
        with p.open("a", encoding="utf-8", newline="") as f:
            csv.writer(f).writerows(todo)
    print(name, "+", len(todo), "->", len(body) + len(todo))

# --------------------------------------------------------------------------
# docs
# --------------------------------------------------------------------------
DOC21 = r'''# دور نهم طراحی — DESIGN v9 (گرهها روی یک خط عمودی واحد)

> **وضعیت:** `DESIGN v9 · REVIEW` — منتظر تأیید نهایی. همچنان **فقط پلن/دیزاین**؛ هیچ کد محصولی نوشته نشده.
> **گفتۀ شما:** «معماری گرهها همچنان نیاز به توجه داره … قوس نده و گرهها رو در یک خط عمومی قرار بده … بازم بازبینی کن کدش رو و بهتر شبیهسازی کن».
> **تفسیر:** «خط عمومی» = **یک محور عمودی صاف**؛ یعنی حذف قوسها / زانوهای `Q` / زیگزاگ چپ‑راست. اگر منظورتان چیز دیگری بود، در `OPEN_QUESTIONS.csv` (U10) ثبت شده و برگشتپذیر است.
> جایگزین `20_DESIGN_ROUND_8.md` است؛ بقیهٔ مصوبات دور هشتم پابرجااند.

---

## ۱. چیدمان تازه: یک خط، صفر قوس

| | v8 | **v9** |
|---|---|---|
| محور گرهها | `196 / 312 / 196 / 80 / 196 / 80` (زیگزاگ) | **همه `x=196`** |
| مسیر | ۲ مسیر با زانوهای گرد `Q` | **۱ مسیر صاف `M196 0 V620`** |
| فرمانهای قوس | `Q` | **۰** (`Q/C/S/T/A` = صفر) |
| گرادیان | دو رنگ دوتکهای | **یک `linearGradient`** با توقف سخت دقیقاً روی گرهٔ فعلی (`41.61%`) |
| فاصلهٔ گرهها | ۱۰۶dp حدسی | **۱۲dp از `spacing_s`** |

شش گره در `cy = 50, 154, 258, 362, 466, 570` (گام ۱۰۴ = ۹۲ + ۱۲) روی `viewBox 392×620`، بالا و پایین ۴dp حاشیهٔ متقارن. **همهٔ مختصات، هم در CSS بیلد و هم در رانتایم، از `NODE_CODE_GEOMETRY.json::nodeGeometry` خوانده میشوند**؛ هیچ جایگذاری دستی وجود ندارد.

## ۲. بازبینی مجدد کد (چرا شبیهسازی بهتر شد)

منابع تازهخواندهشده: `values/values/dimen.xml` (۱۳۹۶ دایمنشن)، ۱۳ شِیپ `<shape>`، ۱۰ وکتور `pathData`، ۲ انیمیشن `rc_checkpoint_window_*`، `test-tracks.json`، ۹۲ کلاس `PathMap*`ی DEX. هفت تصحیح نسبت به v8:

| مورد | v8 (حدسی) | **v9 (از کد)** | منبع |
|---|---|---|---|
| شعاع گوشهٔ گره | ۲۶dp | **۱۶dp** | `glance_component_btn_square.xml → @dimen/glance_component_square_icon_button_corners` |
| ضخامت خط مسیر | ۱۰dp | **۶dp** | `dimen.xml :: lesson_progressbar_height` |
| فاصلهٔ گرهها | ۱۰۶dp | **۱۲dp** | `dimen.xml :: spacing_s` |
| اندازهٔ آیکن | ۴۴dp | **۴۸dp** | `glance_component_btn_circle.xml` size 48dp؛ `ic_bolt_mastered.xml` 48dp |
| لایههای پیشرفت | ۲ رنگ | **۳ لایه** | `progress_bar_chapter.xml`: background / weak / primary، شعاع ۱۰۰dp (قرصی) |
| شکل گره | `border-radius` CSS | **`pathData` واقعی** `ic_square_rounded.xml` (`M18.25,21H5.75…`) | `res/drawable/ic_square_rounded.xml` |
| بولتها | `ic_flash` / `ic_bolt` | **`ic_bolt_charged`** (#FFFFDA1B / #FFFFAB00) و **`ic_bolt_mastered`** (۴۸dp + جرقهها) | `res/drawable/*.xml` |

همچنین تایمینگ تعامل گره از انیمیشنهای واقعی چکپوینت گرفته شد: **ورود ۲۲۰ms / خروج ۴۰۰ms** (`rc_checkpoint_window_enter.xml` / `_exit.xml`). خط پسزمینه نقطهچین از `dotted_border_background.xml` (stroke 2dp / dash 8dp / gap 8dp) و رنگها از جداول ARSC باقی ماندند.

## ۳. توالی حالتها خطی و بدون قفل

`انجامشده → انجامشده → فعلی (حلقهٔ ½ / نسخهٔ ic_play) → بعدی (روشن، **بدون هیچ نماد قفل**) → بولت شارژشده → بولت تسلطیافته`.

در v8 یک گرهٔ «انجامشده» **زیر** گرهٔ فعلی بود که با پیشرفت خطی ناسازگار بود؛ اصلاح شد. گرهٔ «بعدی» فقط یک مربع گرد روشن با `ic_square_rounded` است، نه قفل. **صفر گرهٔ قفلی** در یادگیری / داخل مبحث / تمرین مبحث؛ تنها قفل مجاز همان **«آزمون نهایی / دو هفتگی»** بخش ۶ هاب آزمونهاست، دستنخورده.

## ۴. بدون تغییر (همهٔ مصوبات قبل)

۵ تب (`MAX` ممنوع) · روتین روزانه و ایدهٔ Habitica حذفشده · دیکته حذفشده · هیچ یادداشت طراحی/سیاست/EPM/تایمر داخل UI (شواهد در `data-code`/`data-lh` نامرئی) · **۷ بخش لیبلدار + قالب فیلد + پاسخنامهٔ تشریحی نگه داشته شد** · ۷ بخش، تایمر فقط داخل آزمون، ۲۷۰ دقیقهٔ ثابت، «پاسخبرگ» ≠ «پاسخنامه»، تکدکمهٔ AI · بولت ← `section-practice` جدا از هاب آزمون · لیدربورد بدون Promotion Zone · چت مینیمال + «اضافه کردن فایل» / «زنجیره گفت و گو» + TEACH/PRACTICE + `gemini-flash-lite-latest` + `medium` روی یک خط · RTL/فارسی + حالت شب · ۱۴ اسکرینشات فقط **چک بصری**.

ظاهر آزمونها همان پوستهٔ میمویی دور هشتم است (وکتورهای واقعی + رنگ/شعاع/تایپوگرافی ARSC) و در دور نهم **هیچ تغییری** نکرد.

## ۵. تحویل و اعتبارسنجی

`tools/extract_mimo_nodes_v9.py` → `DESIGN/NODE_CODE_GEOMETRY.json` (۱۳۷٬۹۱۱ بایت، `round: v9`) + `CATALOGS/MIMO_PATH_NODES.csv` (**۸۸ ردیف**) → `tools/build_design_v9.py` (از تمپلیت پاکشدهٔ v8) → `DESIGN/index.html`. خروجی: ۱۴ نما، ۵ تب، ۹۳ وکتور SVG، ۱۳۳/۱۳۳ آیکن رنگشده، ۶ گره، ۱ مسیر، ۰ قوس، ۰ قفل یادگیری، `node --check` OK، jsdom **۰ خطا**، وریفایر PASS. **DESIGN v8** بایگانی شد؛ تأیید نهایی همچنان **PENDING**.
'''

NOTES = r'''# یادداشتهای طراحی — DESIGN v9

> نسخهٔ جاری: **DESIGN v9 · REVIEW** (منتظر تأیید نهایی). نسخههای **DESIGN v6 / v7 / v8** بایگانی حسابرسیاند. همچنان **فقط پلن/دیزاین**؛ هیچ کد محصولی نوشته نشده است.

## ۱. اصل حاکم

بازآفرینی ۱۰۰٪ بخشهای اصلی میمو **از داخل کد و مهندسی معکوس**؛ ۱۴ اسکرینشات فقط `VISUAL_CROSSCHECK_ONLY`. منابع: `CATALOGS/DESIGN_TOKENS.json` (ARSC)، `SOURCE/values/values/dimen.xml`، `SOURCE/values/values/string.xml`، `SOURCE/res/drawable/*.xml`، `SOURCE/res/anim/`, `SOURCE/dex/UI_CLASSES.json`، `test-tracks.json`. فقط نام درسها/فصلها/مباحث کنکوری میشود؛ ۰ رنگ/فونت/شعاع/آیکون تازه.

## ۲. گرهها (دور نهم): یک خط عمودی واحد

همهٔ ۶ گره روی **محور x=196**، بدون قوس، بدون زانوی `Q`، بدون زیگزاگ. مسیر **یک `<path>` صاف `M196 0 V620`** با `linearGradient` سخت در محل گرهٔ فعلی (`41.61%`). مختصات هم در بیلد و هم در رانتایم از `NODE_CODE_GEOMETRY.json::nodeGeometry` خوانده میشود.

اعداد از کد (جایگزین حدسهای v8): شعاع **۱۶dp** (`glance_component_btn_square.xml → dimen`)، ضخامت خط **۶dp** (`lesson_progressbar_height`)، فاصلهٔ گرهها **۱۲dp** (`spacing_s`)، آیکن **۴۸dp** (`glance_component_btn_circle.xml`)، گرادیان سهلایهٔ `progress_bar_chapter.xml`، شکل `ic_square_rounded.xml`، بولتهای واقعی `ic_bolt_charged` / `ic_bolt_mastered`، انیمیشن ۲۲۰/۴۰۰ms از `rc_checkpoint_window_*`.

توالی خطی: انجامشده / انجامشده / فعلی (½ یا `ic_play`) / **بعدیِ بدون قفل** / بولت شارژشده / بولت تسلطیافته. حلقهٔ دوتایی سفید، گرادیان بنفش، تیک `ic_check_white`، نقطهچین و کتاب شناور حفظ شدند. **هیچ گرهٔ قفلی** وجود ندارد؛ تنها قفل همان کارت «آزمون نهایی / دو هفتگی» هاب آزمونهاست.

## ۳. مصوبات پابرجا

روتین روزانه و کل ایدهٔ Habitica حذف · دیکته حذف · یادداشتهای توضیحی داخل UI حذف (شواهد نامرئی `data-code`/`data-lh`) · **۷ بخش لیبلدار / قالب فیلد / پاسخنامهٔ تشریحی نگه داشته شد** · ۵ تب، `MAX` ممنوع · ظاهر آزمونها فقط پوستهٔ میمو (بدون تغییر معماری/تایمر/۲۷۰ دقیقه/پاسخبرگ≠پاسخنامه) · بولت ← `section-practice` جدا از آزمون · لیدربورد selfbox بدون Promotion Zone · چت مینیمال · RTL/شب · بدون Pro/پرداخت/MAX · «وارد کردن کلید API» فقط یادداشت.

## ۴. حقوقی / clean-room

هیچ دارایی، فونت، رشته یا کدی از Mimo 9.35، Hamdars، Hadaf Plus، LearnHarness، EPM یا Habitica کپی نشده است. subscription/cart/Pro و اسکرینشات رانتایم ممنوعاند.

## ۵. شواهد و وضعیت

`DESIGN/CODE_GEOMETRY.json` + `LEARN_CODE_GEOMETRY.json` + `NODE_CODE_GEOMETRY.json` (v9) → `tools/build_design_v9.py` → `DESIGN/index.html`. ۱۴ نما / ۵ تب / ۹۳ وکتور SVG / ۱۳۳ آیکن / ۰ خطای jsdom / وریفایر PASS. منتظر **تأیید نهایی**؛ بعدش تازه P0 شروع میشود.
'''

(UP / "21_DESIGN_ROUND_9.md").write_text(DOC21, encoding="utf-8")
(D / "DESIGN_NOTES.fa.md").write_text(NOTES, encoding="utf-8")
print("docs written")

# --------------------------------------------------------------------------
# banners
# --------------------------------------------------------------------------
for p in sorted(UP.glob("*.md")):
    s = p.read_text(encoding="utf-8")
    if MARK in s:
        continue
    current = p.name.startswith("21_")
    banner = (MARK + "\n> " + ("✅ **DESIGN v9 · CURRENT** — لاگ دور نهم، جایگزین v8. "
                              if current else
                              "⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v9](21_DESIGN_ROUND_9.md)** است. ")
              + "همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.")
    lines = s.split("\n")
    insert_at = 1 if lines and lines[0].startswith("#") else 0
    lines.insert(insert_at, banner)
    p.write_text("\n".join(lines), encoding="utf-8")
print("banners written")

wf = UP / "wireframes.html"
s = wf.read_text(encoding="utf-8")
s = s.replace("DESIGN/index.html\">DESIGN v8</a>", "DESIGN/index.html\">DESIGN v9</a>")
s = s.replace("(گرههای دقیق از کد، حذف روتین روزانه، حذف دیکته، پاکسازی توضیحات، پوستهٔ میمویی آزمونها)",
              "(گرهها روی یک خط عمودی واحد و بدون قوس، حذف روتین/دیکته/توضیحات، پوستهٔ میمویی آزمونها)")
s = s.replace('<a href="20_DESIGN_ROUND_8.md">لاگ دور هشتم</a>', '<a href="21_DESIGN_ROUND_9.md">لاگ دور نهم</a>')
wf.write_text(s, encoding="utf-8")
print("wireframes banner updated")

# archived v8 builders
for f in ["tools/build_design_v8.py", "tools/finalize_v8.py", "tools/extract_mimo_nodes_v8.py"]:
    p = UP / f
    s = p.read_text(encoding="utf-8")
    if "ARCHIVED (round 9)" not in s:
        lines = s.split("\n")
        i = 1 if lines and lines[0].startswith("#!") else 0
        lines.insert(i, "# ARCHIVED (round 9): superseded by extract_mimo_nodes_v9.py / build_design_v9.py / finalize_v9.py.")
        p.write_text("\n".join(lines), encoding="utf-8")
print("v8 tools marked archived")

# --------------------------------------------------------------------------
# MANIFEST
# --------------------------------------------------------------------------
mp = UP / "MANIFEST.json"
m = json.loads(mp.read_text(encoding="utf-8"))
stable = [p for p in UP.rglob("*") if p.is_file() and p.name not in
          ("SHA256SUMS.txt", "VERIFICATION_REPORT.json")]
m["date"] = "2026-11-04"
m["status"] = "PLAN_ONLY + DESIGN v9 REVIEW (no product implementation)"
dl = m["deliverables"]
dl["persian_docs"] = 22
dl["csv_catalogs"] = 20
dl["extracted_assets_files"] = len(stable)
dl["total_bytes"] = sum(p.stat().st_size for p in stable)
dl["verification"] = "PASS"
dl["verification_checks"] = 0
dl["design_round"] = "v9 (REVIEW)"
dl["design_views"] = 14
dl["design_svg_vectors"] = 93
dl["bottom_nav_tabs"] = 5
dl["node_code_evidence"] = ("DESIGN/NODE_CODE_GEOMETRY.json v9 (single_vertical_line / axis x=196 / "
                            "16dp corners / 6dp connector / 12dp gap / 48dp icons / 0 curves / "
                            "1 continuous path / 58 vectors / 92 PathMap DEX classes / 223 tutorialIds) "
                            "+ CATALOGS/MIMO_PATH_NODES.csv (88 rows)")
dl["v9_changes"] = "re-reviewed node code; ONE straight vertical line (no curve/zigzag); corrected 7 code-derived numbers; real charged/mastered bolt vectors; linear unlocked state sequence"
cf = m["critical_findings"]
v9 = [
    "v9: node architecture re-reviewed from dimen.xml / drawable shapes / anim resources; 7 v8 inferred numbers corrected (16dp corner, 6dp line, 12dp gap, 48dp icon, 3-layer progress, real squircle pathData, real bolt vectors)",
    "v9: ALL 6 Learn nodes on ONE vertical axis (x=196); ONE continuous straight connector M196 0 V620; ZERO Q/C/S curve commands; hard gradient stop at the current node",
    "v9: linear state sequence done/done/current/next(unlocked)/ic_bolt_charged/ic_bolt_mastered; still ZERO Learn locks (one exam-hub lock untouched)",
    "v9: 220ms enter / 400ms exit node transitions from rc_checkpoint_window_enter.xml / _exit.xml",
]
for x in v9:
    if x not in cf:
        cf.append(x)
rep = m["reproduce"]
for cmd in ["python3 tools/extract_mimo_nodes_v9.py .",
            "python3 tools/build_design_v9.py .",
            "python3 tools/finalize_v9.py ."]:
    if cmd not in rep:
        rep.append(cmd)
m["design_round_8"]["status"] = "DESIGN v8 · SUPERSEDED by v9 (single-line node layout) — archived audit trail"
m["design_round_9"] = {
    "status": "DESIGN v9 · REVIEW — awaiting final approval (CURRENT)",
    "trigger": "user: معماری گرهها همچنان نیاز به توجه داره / قوس نده و گرهها رو در یک خط عمومی قرار بده / بازم کدش رو بازبینی کن و بهتر شبیهسازی کن",
    "interpretation": "خط عمومی = محور عمودی صاف واحد؛ ثبتشده بهعنوان فرض U10 در OPEN_QUESTIONS.csv",
    "main_task": "re-review node code + single straight vertical line + better simulation",
    "method": "CODE_FIRST / extract_mimo_nodes_v9.py -> NODE_CODE_GEOMETRY.json -> build_design_v9.py -> DESIGN/index.html",
    "layout": {"mode": "single_vertical_line", "axis_x": 196, "gap_dp": 12,
               "connector_paths": 1, "curve_commands": 0, "connector_d": "M196 0 V620",
               "corner_radius_dp": 16, "stroke_dp": 6, "icon_dp": 48},
    "code_corrections": 7,
    "interactive_prototype": "DESIGN/index.html (14 views / 5 tabs / 93 SVG vectors / 133 painted icons / 6 nodes / 0 Learn locks / 0 jsdom errors)",
    "unchanged": ["5 tabs / no MAX", "routine + Habitica removed", "Dictate removed", "no UI annotations",
                  "7 labelled exam sections + descriptive answer text", "exam architecture / timer / 270 min / پاسخبرگ≠پاسخنامه",
                  "one pre-existing exam-hub lock", "bolt section-practice isolated"],
    "final_log": "21_DESIGN_ROUND_9.md",
    "design_notes": "DESIGN/DESIGN_NOTES.fa.md",
    "final_approval": "PENDING — no product implementation until user says the design is final",
}
mp.write_text(json.dumps(m, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("MANIFEST updated; stable files=%d bytes=%d" % (len(stable), sum(p.stat().st_size for p in stable)))
