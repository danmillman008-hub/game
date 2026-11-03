# یادداشتهای طراحی — دور ششم (DESIGN v6)

> **فقط دیزاین/پلن.** هیچ کد محصولی نوشته نشده. جایگزین یادداشتهای v5 است.

## اصل روش
بازسازی **از داخل کد APK**، نه از روی عکس. اسکرینشاتها فقط چک بصریاند.

خط لولهٔ قابلتکرار:
```
tools/extract_mimo_geometry.py   → DESIGN/CODE_GEOMETRY.json
tools/extract_mimo_learn_v6.py   → DESIGN/LEARN_CODE_GEOMETRY.json + CATALOGS/MIMO_LEARN_SUBSCREENS.csv (۸۶۸ ردیف شاهد)
tools/build_design_v6.py         → DESIGN/index.html
```
منابع خواندهشده: جداول ARSC (`DESIGN_TOKENS.json`)، `res/drawable/*.xml` (`android:pathData`)،
`res/layout/*.xml` (AXML)، `res/navigation/nav_onboarding_graph.xml`،
`assets/ui/testdata/test-tracks.json`، `dex/UI_CLASSES.json`، `dex/UI_STRING_LITERALS.txt`.
نتیجه: ۱۵۰ رشته، ۴۱ وکتور، ۱۶ لایه، ۱۵ فصل واقعی، ۲۷۲ کلاس DEX، ۶۸ رنگ / ۶۲ دایمنشن / ۲۱۳ استایل.

---

## ۱. صفحهٔ ورود حذف شد
شما گفتید «فعلاً به صفحهٔ ورود که صفحهٔ ۷ هست نیازی نداریم».
صفحهٔ `onboarding` کاملاً از سوییچر و نماها حذف شد؛ شاهد تصویری
`mimo-09-onboarding.webp` فقط بایگانی است.

## ۲. صفحهٔ یادگیری تمیز شد
عوامل شلوغی v5 حذف شدند: حلقهٔ ۱۲٪، چیپ «پیشرفت ۱/۲»، نوشتهٔ توضیحی **داخل گوشی**،
قرص فصل و FAB اضافه. جایگزین:
- **۳ چیپ**: سکه ۱٬۲۷۲ / کلید ∞ / استریک ۰ → `PathToolbarKt$RowWithKeys`، `ic_key`، `ic_infinity`.
- **کارت سربرگ مسیر**: «Career path» / «3. Arrays & Functions» / نوار پیشرفت ۴۳٪
  → `ViewsKt$OverviewEntryPointHeader` + `progress_bar_mimo.xml` (شعاع ۱۰۰dp).
- **سهخط `ic_list_bulleted`** کنار نام مسیر، قابلکلیک → `Select Path`.
- مسیر مارپیچ تمیز ۵ گرهای → `PathMapScreenKt`، `ic_check_white`، `ic_flash`.

## ۳. صفحاتی که نساخته بودم، ساخته شدند

### `Select Path` (سهخط)
`select_path`، `track_switcher_career_paths`، ۴ کارت مسیر شغلی
(منتخب با کادر `card_outline #7E4BDE`)، `courses`، ۶ ردیف تکدرس
(`track_switcher_typescript_label = "JS required"`،
`track_switcher_react_label = "HTML, CSS and JS requi…"` با ellipsize)،
حلقههای ۵۶dp از `profile_certificate_view.xml`، badgeها از `ic_badge_*` / `ic_code_lang_*`.
پشتش: `ObservePathSwitcherState` (۵۱ کلاس)، `showPathSwitcher`، `key_path_switcher_on_exit_enabled`.

### `Path Overview` (کارت مسیر)
`onboarding_path_type_career_path`، دکمهٔ `ic_switch`،
`certificates_professional_title`، «22% Complete» (`path_overview_certificate_percent_complete`)،
`2/9`، و فصلهای شمارهدار با `path_overview_section_ordinal = "%d. %s"`؛
**نام/توضیح/تعداد درس مستقیم از `test-tracks.json :: tracks[0].sections[]`**.
پشتش: `PathOverviewScreenKt`، `OverviewEtaCardKt`، `PathOverviewViewModel`.

### `Section detail` (داخل مبحث)
فهرست درسها با **شناسههای واقعی `tutorialIds`**، وضعیت ✓/▶/🔒،
`path_overview_section_project_label = "Section Project"`،
`path_section_coming_soon = "Coming soon"`،
`alert_msg_section_setion_locked`،
`lesson_continue` → کارت شروع فصل → صفحهٔ درس.

### `Unfinished track` (دیالوگ)
`certificates_unfinished_track_dialog_title/text/action` عیناً،
شعاع ۲۸dp، ماسکات `ic_mimo_mascot` (۲۹ مسیر). با کلیک روی مسیر ناتمام / کارت گواهی / «Coming soon» باز میشود.

---

## ۴. گراف کلیک
```
Learn ──سهخط──▶ Select Path ──درس──▶ Section detail ──Continue──▶ Chapter ──▶ Lesson
  │                  ▲                     │
  └──کارت مسیر──▶ Path Overview ─ic_switch┘  └──See course overview──▶ Path Overview
                       ├──فصل──▶ Section detail
                       └──گواهی──▶ Unfinished track
```

## ۵. حفظشده از دورهای قبل
۵ تب `Learn / Practice / AI / Leaderboard / Profile` (نه MAX) · ۷ بخش لیبلدار هاب آزمون ·
تایمر فقط داخل آزمون (کلیک ← عدد ← شروع ← معکوس، ۲۷۰ دقیقۀ ثابت) ·
**«پاسخبرگ»** = گزینههای زدهشده / **«پاسخنامه»** = جواب تشریحی + کلید تستی ·
زمان خالص آزمون برای جامع/جمعبندی/نهایی ·
**یک** دکمهٔ «توضیح با هوش مصنوعی» در صفحهٔ سؤالات + **همان** دکمه در صفحهٔ نتیجه ·
چت مینیمال + تاریخچه + ۸ دکمهٔ LH · لیدربورد با اطلاعات/امتیازات/آزمونهای خود فرد ·
بخش مشاوره `PARKED` · بدون Pro/پرداخت/اشتراک ·
«وارد کردن کلید API» فقط یادآوری، **الان در UI طراحی نشده**.

## ۶. تفاوت کد و عکس (کد ملاک است)
- منوی AXML چهارتبه است؛ `mimo-10` نسخهای با تب MAX نشان میدهد؛
  **حکم صریح شما** ۵ تب با AI است و MAX راه نیافت.
- نام فصلها در `test-tracks.json` با اسکرینشات فرق دارد؛ ساختار/رشتهها/حلقهها از کد آمدند،
  فقط **نام درس و مبحث** کنکوری شد.
- APK هیچ کوالیفایر RTL ندارد → نمای پیشفرض LTRِ ۱۰۰٪ میمو + دکمهٔ «فارسی / RTL».

## ۷. تست
`node --check` ✓ · اجرای واقعی DOM (jsdom): ۰ خطا، ۱۳ نما، ۹۹/۹۹ آیکن SVG،
همهٔ جریانها، RTL/LTR، حالت شب، تایمر، پاسخبرگ/پاسخنامه و دکمههای AI ✓ ·
`VERIFICATION_REPORT.json` = PASS · ۱۴ اسکرینشات فقط چک بصری.

**منتظر تأیید نهایی**؛ بعد از «مرحلهٔ بعد» ← P0 پیادهمسازی.
