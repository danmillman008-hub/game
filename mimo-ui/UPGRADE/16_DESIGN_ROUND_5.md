# دور پنجم طراحی — بازآفرینی ۱۰۰٪ میمو **از داخل کد** (DESIGN v5 · FINAL DRAFT)

> ⚠️ **بایگانی / superseded:** این سند مربوط به دورهای قبل است. طراحی فعلی **[DESIGN v6](17_DESIGN_ROUND_6.md)** است؛ صفحهٔ ورود حذف، یادگیری بازسازی و زیرصفحات «انتخاب مسیر / نمای مسیر / داخل مبحث» از کد اضافه شدند. لاگهای قدیمی صرفاً ردپای حسابرسیاند.

**ورودی:** ۹ اسکرینشات تازۀ میمو + بازخورد شما در سه پیام پیاپی.
**خروجی:** `DESIGN/index.html` (v5، تولیدشده از `DESIGN/CODE_GEOMETRY.json`)، `tools/extract_mimo_geometry.py`، `tools/build_design_v5.py`، `tools/design_v5_template.html`، `CATALOGS/MIMO_CODE_GEOMETRY.csv`، `CATALOGS/MIMO_SCREENSHOT_CROSSWALK.csv`، `CATALOGS/ANSWER_SHEET_POLICY.csv`، بهروزرسانی ۱۴ سند/CSV و `MANIFEST.json`، لاگ حاضر.
**وضعیت:** `DESIGN v5 · FINAL DRAFT` — منتظر تأیید نهایی. هیچ کد محصولی نوشته نشده است.

---

## ۰. خلاصهٔ یکخطی

> «بخش یادگیری اصلاً شبیه میمو نبود» → **مسیر یادگیری و هفت صفحهٔ اصلی دیگر، مستقیماً از جداول منبع APK ۹٫۳۵ بازتولید شدند** (۴۶ وکتور، ۴۱ رنگ، ۳۶ دایمنشن، ۱۳ استایل متن، ۴۵ رشته، ۱۹ لایهٔ AXML، ۸۰ کلاس Composeی `PathMap*`)؛ اسکرینشاتها فقط **چک بصری**اند. «پاسخبرگ» و «پاسخنامه» از هم جدا شدند؛ «توضیح با هوش مصنوعی» = **یک** دکمه در صفحهٔ سؤالات + **همان** دکمه در صفحهٔ آخر آزمون؛ لیدربورد اطلاعات/امتیازات/آزمونهای خود فرد را نشان میدهد.

---

## ۱. حکم روششناسی شما (مهمترین تغییر این دور)

> «بهترین حالت بازسازی میمو از داخل کد و مهندسی معکوسشه نه از روی عکس … تا هر جایی که توانت داری از کد کندوکاو کن، نه اینکه صرفاً از روی عکس مپی کنی، چون کد دقیقاترین حالت ممکنه.»

پیش از این `DESIGN/index.html` با دست و با نگاه به خروجیهای استخراج نوشته میشد. در v5 یک **خط لولهٔ قابلتکرار** ساختیم:

```
mimo-ui/SOURCE/res/drawable/*.xml   (AXML دیکدشده)
mimo-ui/CATALOGS/DESIGN_TOKENS.json (50,477 ردیف ARSC)
mimo-ui/SOURCE/res/layout/*.xml     (AXML دیکدشده)
mimo-ui/SOURCE/res/values/*         (رنگ/دایمنشن/استایل/رشته)
mimo-ui/SOURCE/dex/UI_CLASSES.json  (3,255 کلاس، 174 کلاس حوزۀ path)
        │
        ▼  tools/extract_mimo_geometry.py
DESIGN/CODE_GEOMETRY.json  +  CATALOGS/MIMO_CODE_GEOMETRY.csv (200 ردیف)
        │
        ▼  tools/build_design_v5.py  (قالب tools/design_v5_template.html)
DESIGN/index.html  ← تمام متغیرهای CSS و تمام <svg> از مقادیر بالا تزریق میشوند
```

- **`icon()`** در صفحه، `android:pathData` همان وکتورها را میگیرد، `#AARRGGBB` را به `rgba()` تبدیل میکند، `fillType=1` را به `fill-rule="evenodd"` نگاشت میکند و `viewportWidth/Height` را حفظ میکند. یعنی آیکنها **عیناً همان هندسۀ کد**اند، نه شبیهسازی دستی.
- **تمام متغیرهای CSS** (روز + شب) از `CODE_GEOMETRY.json` ساخته میشوند: `--bg`, `--card`, `--primary`, `--progress`, `--line`, `--text`, `--yellow`, `--blue`, `--green` … .
- **اندازهها** از کد: `TextH1=24sp`, `TextH2=20sp`, `TextH3=18sp`, `TextP2=16sp`, `TextLabel1=14sp`, `TextLabel3=12sp`, `toolbar_height=56dp`, `lesson_progressbar_height=6dp`, `leaderboard_item=60dp`, `profile_header_avatar_size=88dp`, `m3_alert_dialog_corner_size=28dp`, `glance_component_button_corners=24dp`, `cardview_corner_radius_large=12dp`.
- **رشتههای کروم** عیناً از `res/values/strings.xml`: `navigation_path=Learn`, `start_learning`, `weekly`, `leaderboard_league_name_1=Wooden League`, `leaderboard_promotion_zone`, `leaderboard_trophies_title`, `no_trophies_yet_title/desc`, `playgrounds`, `create_playground`, `codeplayground_template_label`, `lesson_continue=Continue`, `chapter=Chapter` و … . **فقط نام درس/فصل/مبحث کنکوری شد** (مثلاً `Web Development → زیستشناسی`، `HTML Basics → سلول و بافت`)؛ همانطور که خواستید.
- **هیچ فایل باینری، فونت، تصویر یا کدی از APK کپی نشده است**: وکتورها بهصورت متن `pathData` بازتولید شدند، فونت جایگزین سیستمی (Tahoma/Segoe UI) است و تصویرسازیها با CSS/SVG ساخته شدند.

### ۱٫۱ جایی که کد با عکس فرق داشت → **کد ملاک گرفته شد**

| مورد | کد Mimo ۹٫۳۵ | اسکرینشات شما | تصمیم v5 |
|---|---|---|---|
| نوار پایین | ۴ تب `Learn/Practice/Leaderboard/Profile` (`bottom_navigation_menu.xml`) | ۴ تب `Learn/Leaderboard/Community/Profile` (بیلد قدیمیتر) | **۵ تب** طبق حکم صریح دور چهارم شما؛ آیکنها/رنگ حالتها عیناً از `ic_tab_*` + `bottom_navigation_colors.xml` |
| رنگ «Promotion Zone» | `@color/support_green = #FF66BC5A` (`leaderboard_promotion_divider.xml`) | بنفش | **`support_green` کد** |
| متن حالت خالی Playgrounds | `playgrounds_empty_title = Explore Your Ideas` | «No playgrounds» | **متن کد** |
| جهت | ۱۶۱ کوالیفایر منبع، **۰ کوالیفایر RTL** (هیچ `values-fa/-ar/-he/-ur/-ps`) | LTR | نمای پیشفرض LTRِ ۱۰۰٪ میمو + دکمهٔ «فارسی / RTL» برای آینهسازی و لیبلهای فارسی |
| مسیر یادگیری | **Compose** است (`PathMapScreenKt`, `PathOverviewScreenKt`, `PathMapFragment` — ۸۰ کلاس)، لایهٔ XML ندارد | ۲ اسکرینشات (گرهٔ play و گرهٔ ۱/۲) | هندسهٔ گرهها/خطوط از ثابتهای کد (شعاع ۲۸dp، `progress_chapter_primary`, `card_disabled`, `button_primary_highlight`) + چک بصری؛ صادقانه بهعنوان «تنها بخش بدون AXML» ثبت شد |

---

## ۲. بازخوردهای این دور → تغییر (جدول ردیابی)

| # | گفتهٔ شما | تغییر v5 | محل |
|---|---|---|---|
| F-21 | «بخش یادگیری اصلاً شبیه میمو درنیومده … دقیقاً و دقیقاً و دقیقاً همون، صرفاً اسم مباحث ویرایش شود» | مسیر یادگیری ۱۰۰٪ بازتولید: قرصهای سکه/استریک، نوار درس، پسزمینهٔ نقطهای، قرص فصل با حلقهٔ ۱۲٪، گرههای اسکورگل با لبهٔ سهبعدی، خطوط وصلکننده، گرههای انجامشده/جاری/قفل/رعد، دکمهٔ شناور «A»، نوار پایین با وکتورهای واقعی | `index.html#learn`, `CODE_GEOMETRY.json` |
| F-22 | «چهارچوب کلی نرمافزار دقیقاً باید یکی باشه، فقط تو بخشهای جدید سخت نمیگیرم» | ۷ صفحهٔ اصلی دیگر هم از AXML کد ساخته شدند: کارت شروع فصل، صفحهٔ درس، لیدربورد هفتگی، پروفایل کاربر، پروفایل، صفحهٔ ورود، باتمشیت «Create Playground» | `index.html` (۱۱ نما) |
| F-23 | «پاسخبرگ همونیه که بهاشتباه دکمهٔ پاسخنامه شده؛ گزینههای زده را نشون میده» | دکمه و باتمشیت به **«پاسخبرگ»** تغییر نام یافت؛ شبکهٔ ۲۰ سؤال + شمارهٔ گزینۀ انتخابشدهٔ هر سؤال را نشان میدهد؛ پاسخ صحیح تا اتمام آزمون مخفی است | `#answerSheetBtn`, `#paletteSheet` |
| F-24 | «یه دکمهٔ پاسخنامه هم نیازه؛ وقتی میزنه جواب تشریحی و توضیحات سؤال بیاد بالا» | دکمهٔ **جداگانهٔ «پاسخنامه»** → باتمشیت بالا میآید با دو تب: «پاسخ تشریحی» (پیشفرض) و «پاسخ تستی» | `#answerKeyBtn`, `#keySheet`, `#keyDescSheet`, `#keyTestSheet` |
| F-25 | «این نباید در هر آزمونی باشه؛ یه سری آزمونها خالص وقت آزمون باشه و در آخر آزمون اون صفحه بیاد» | `POLICY` چهارگانه: عادی/زماندار/تحلیلی → پاسخبرگ + پاسخنامه حین آزمون؛ جامع/جمعبندی/نهایی → **زمان خالص** (هیچکدام حین آزمون) و **در پایان، صفحهٔ پاسخنامه بهصورت خودکار باز میشود** | `POLICY`, `applyPolicy()`, `finishExam()`, `CATALOGS/ANSWER_SHEET_POLICY.csv` |
| F-26 | «اینو یه دکمه بکن قشنگ … یه دکمه با اسم «توضیح با هوش مصنوعی» به همون صفحۀ اجرای آزمون … و همین دکمه رو به صفحۀ آخر آزمون هم اضافه کن که صورت اشتباهات + جوابشون + صورت سؤال رو منتقل کنه» | **دقیقاً یک دکمه** در صفحهٔ سؤالات (`#askAiBtn`) و **همان دکمه** در صفحهٔ آخر (`#askAiResultBtn`)؛ دومی ۳ سؤال غلط را با **صورت سؤال + پاسخ انتخابشدهٔ شما + پاسخ صحیح** به چت مینیمال میبرد. بدون پنل، بدون داک، بدون دکمۀ تازه | `#askAiBtn`, `#askAiResultBtn`, `WRONG[]`, `setCtx()` |
| F-27 | «در لیدربورد اطلاعات و امتیازات و آزمونها و این چیزای خود فرد مشخص بشه» | ردیف آبی خود فرد + ۳ کارت آمار (`profile_info_card_view.xml`: روز متوالی / امتیاز کل / لیگ) + کادر «آزمونها و امتیازات من» با ۵ ردیف (درصد، رتبه، تعداد سؤال، غلطها، XP هفته) + نمای «پروفایل کاربر» | `index.html#leaderboard`, `#user-profile` |
| F-28 | «بازسازی از داخل کد، نه مپ کردن عکس» | خط لولۀ `extract → geometry → build` (بند ۱)، ۹ اسکرینشات صرفاً در `MIMO_SCREENSHOT_CROSSWALK.csv` با نقش `VISUAL_CROSSCHECK_ONLY` | `tools/*`, `CODE_GEOMETRY.json` |

---

## ۳. صفحات اصلیِ بازآفرینیشده و سند کد هرکدام

| نما | لایه/کلاس کد | وکتورهای بهکاررفته | مقادیر کد |
|---|---|---|---|
| مسیر یادگیری | `PathMapScreenKt`, `PathMapFragment`, `PathOverviewScreenKt`, `PathMapViewModel` (DEX) | `ic_coin`, `ic_streak_active`, `ic_list_bulleted`, `ic_check_white`, `ic_play`, `ic_lock_alt_02`, `ic_flash` | `progress_chapter_primary #8D60E2`, `progress_chapter_background #E4E6F1`, `card_disabled #E4E6F1`, شعاع ۲۸dp |
| کارت شروع فصل | `chapter_toolbar.xml`, `chapter_activity.xml`, `progress_bar_chapter.xml` | `ic_cap_filled` | `start_learning`, `chapter`, `lesson_progressbar_height=6dp`, `m3_alert_dialog_corner_size=28dp` |
| صفحهٔ درس | `lesson_noninteractive_fragment.xml`, `lesson_description_textview.xml`, `lesson_output_codeblock_textview.xml`, `browser_view_header_dots.xml` | `ic_close`, `ic_flag`, `ic_streak`, `ic_infinity`, `browser_view_header_dots` | `TextP2=16sp`, `TextLessonCode=14sp/aeonik_mono`, `code_highlight`, `lesson_codeblock_corner_radius=4dp`, `lesson_interaction_keyboard_button_height=48dp` |
| لیدربورد هفتگی | `leaderboard_fragment_active.xml`, `leaderboard_item.xml`, `leaderboard_league_header_view.xml`, `leaderboard_promotion_divider.xml` | `ic_leaderboard_league_1..5`, `ic_leaderboard_league_locked`, `ic_flash_filled` | `leaderboard_league_header_height=100dp`, آیتم ۵۲×۵۰dp / منتخب ۶۲×۶۰dp، ردیف ۶۰dp، رتبه ۲۴dp، آواتار ۴۰dp، `support_yellow #F4D055`, `support_blue #3890FA`, `support_green #66BC5A` |
| پروفایل کاربر | `public_profile_fragment.xml`, `profile_info_card_view.xml` | `ic_user_alert`, `ic_streak_active`, `img_brain`, `ic_flash_filled` | `profile_header_avatar_size=88dp`, آیکن کارت ۳۲dp، `TextH3=18sp`, `TextLabel3=12sp` تمامحروف |
| پروفایل | `profile_fragment.xml`, `profile_header.xml`, `profile_empty_trophies_item.xml`, `border_dashed.xml` | `ic_settings`, `ic_cap_filled`, `ic_leaderboard_locked` | `toolbar_height=56dp`, `border_dashed`: stroke 2dp / dash 8dp / gap 8dp / radius 12dp، آیکن ۸۰dp، حاشیۀ متن ۶۰dp |
| صفحهٔ ورود | `onboarding_pick_a_path.xml` | تصویرسازی CSS (بدون کپی دارایی) | `onboarding_get_started`, `view_pager_dots_margin`, نوار ۶dp |
| باتمشیت ساخت آزمون | `codeplayground_template_*` | `ic_code_playground_template_python/js_only/website/react` | `create_playground`, `codeplayground_template_label`, `bottom_sheet_corner_radius=12dp` |
| نوار پایین | `bottom_navigation_menu.xml`, `ic_tab_learn|practice|leaderboard|profile.xml`, `bottom_navigation_colors.xml` | `ic_cap(_filled)`, `ic_flash(_filled)`, `ic_magic_wand(_filled)`, `ic_trophy(_filled)`, `ic_user_circle(_filled)` | `icon_primary #252746` / `icon_weak #A3A5C3`, برچسب ۱۲sp |

---

## ۴. سیاست پاسخبرگ / پاسخنامه (ماشینخوان)

| نوع آزمون | حین آزمون: «پاسخبرگ» | حین آزمون: «پاسخنامه» | پایان آزمون |
|---|---|---|---|
| عادی / تکدرسی / مبحثی / دوباره / تشریحی | ✅ | ✅ | پاسخبرگ + پاسخ تستی + پاسخ تشریحی + تحلیل |
| زماندار | ✅ | ✅ | همان |
| تحلیلی | ✅ | ✅ | همان + شبیهسازی «اگر غلطها نزده میذاشتی» |
| **جامع (۲۷۰ دقیقهٔ ثابت)** | ❌ | ❌ | **صفحۀ پاسخنامه خودکار باز میشود** + پاسخ تستی/تشریحی + تحلیل |
| **جمعبندی / دوره / نهایی** | ❌ | ❌ | **همان، زمان خالص آزمون** |

فایل ماشینخوان: `CATALOGS/ANSWER_SHEET_POLICY.csv`. ثابت ماند: تایمر فقط داخل آزمون (کلیک ← عدد ← شروع ← معکوس، توقف/ادامه، ثبت خودکار در صفر)، جامع = ۲۷۰ دقیقهٔ غیرقابلتغییر، هاب = یک صفحۀ اسکرولی با ۷ بخش لیبلدار و قالب فیلد مشخص.

---

## ۵. انتقال زمینه به هوش مصنوعی (دقیقاً همان «خیلی کم»)

| دکمه | صفحه | زمینۀ منتقلشده |
|---|---|---|
| `#askAiBtn` «توضیح با هوش مصنوعی» | اجرای آزمون / همان صفحۀ سؤالات | نام آزمون + شمارهٔ سؤال + **صورت سؤال** + **گزینۀ انتخابشدهٔ کاربر** |
| `#askAiResultBtn` «توضیح با هوش مصنوعی» | صفحۀ آخر آزمون (نتیجه) | **صورت ۳ سؤال غلط** + **پاسخ هرکدام** + **پاسخ صحیح**؛ بهصورت یک حباب زمینه در همان چت مینیمال |

هیچ پنل تازهای در آزمون ساخته نشد؛ چت همچنان مینیمال + تاریخچه + ۸ دکمۀ پنل اصلی LH است. منبع ایده: `EPM_MINOR_OPTIONS.csv` (`ask_ai_explain`)؛ همانطور که گفتید «اگر جوابشونم منتقل کنه همراه با صورت سؤال که خیلی بهتر» → هر سه بخش منتقل شد.

---

## ۶. آنچه **حفظ** شد (بدون دستکاری)

- ۵ تب `Learn / Practice / AI / Leaderboard / Profile`؛ چت AI تب مستقل دارد و قاتی Practice نشده، تب ششم/`Max` ممنوع.
- هاب آزمون: ۷ بخش لیبلدار، قالب فیلد مشخص، یک صفحۀ اسکرولی؛ جامع = ۲۷۰ دقیقه.
- ماشین حالت تایمر `idle → setting → running ⇄ paused → finished`، فقط داخل آزمون.
- چت مینیمال + تاریخچه + ۸ دکمۀ LH (`Chains`, `Import notes...`, `Cost $0.01`, `TEACH/PRACTICE`, `Dictate`, مدل، `medium`)؛ ۱۵ اکشن کامپوننتی بایگانی.
- «وارد کردن کلید API در تنظیمات» = **صرفاً یادآوری مستند، بدون طراحی UI**.
- مشاوره = **PARKED**؛ هیچ صفحه/ابزاری برایش طراحی نشد.
- بدون اشتراک/پرداخت/Pro؛ بدون FSRS/RAG/FTS/۳D/واژگان/A4.
- RTL + حالت شب (دکمههای بالای صفحه)؛ ۰ رنگ/فونت/شعاع/آیکن تازه.
- **هیچ کد محصولی نوشته نشده**؛ تمام فایلها پلن/طرح/شواهداند.

---

## ۷. محدودیتهای صادقانۀ این دور

1. مسیر یادگیری در ۹٫۳۵ با **Jetpack Compose** رسم میشود (لایهٔ XML ندارد). اندازۀ دقیق گرهها و انحنای خطوط داخل DEX کامپایل شده است و بدون JADX/Java 17 (در این محیط موجود نیست) قابل خواندن نیست؛ بنابراین آن بخش از ثابتهای کد + چک بصری اسکرینشات بازسازی شد. همهٔ صفحات دیگر مستقیماً از AXML آمدند.
2. فونت `aeonik_pro_*` / `aeonik_fono_*` / `aeonik_mono` **کپی نشد** (قانون cleanroom)؛ اندازههای sp عیناً اعمال شدند و خانوادهٔ جایگزین سیستمی استفاده شد.
3. تصویرسازیهای ماسکات/جام/جعبۀ Playgrounds با CSS/SVG ساخته شدند، نه کپی دارایی.
4. بدون رانتایم/امولاتور/اسکرینشات زنده؛ RE همچنان ایستا است.
5. اسکرینشاتها بیلد قدیمیتری از میمو را نشان میدهند (تب `Community`)؛ اختلافها در بند ۱٫۱ و `MIMO_SCREENSHOT_CROSSWALK.csv` ثبت و **کد ۹٫۳۵ ملاک** قرار گرفت.

---

## ۸. چکلیست نهایی پیش از پیادهمسازی

- [x] `tools/extract_mimo_geometry.py` اجرا میشود و ۲۰۰ ردیف شاهد کدی میسازد
- [x] `tools/build_design_v5.py` همان مقادیر را به `DESIGN/index.html` تزریق میکند
- [x] ۹ اسکرینشات با SHA-256 در `DESIGN/REFERENCE/` و `MIMO_SCREENSHOT_CROSSWALK.csv` ثبت شدند (نقش: چک بصری)
- [x] ۱۱ نمای طراحی؛ ۵ تب؛ ۷ بخش لیبلدار؛ `node --check` بیخطا
- [x] «پاسخبرگ» ≠ «پاسخنامه»؛ سیاست زمان خالص + باز شدن خودکار صفحۀ پایان
- [x] یک دکمۀ «توضیح با هوش مصنوعی» در صفحۀ سؤالات + همان دکمه در صفحۀ آخر
- [x] لیدربورد: اطلاعات/امتیازات/آزمونهای خود فرد
- [x] `VERIFICATION_REPORT.json` = PASS، ۰ آلودگی CJK، حالت شب، RTL
- [ ] **تأیید نهایی شما** ← سپس مرحلۀ پیادهمسازی (P0 به بعد؛ P5 همچنان PARKED)
