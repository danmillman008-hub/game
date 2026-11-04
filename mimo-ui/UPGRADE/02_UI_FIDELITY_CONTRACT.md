# قرارداد وفاداری به UI/سازوکار Mimo — **مهمترین سند این دور**
<!-- v8-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v8](20_DESIGN_ROUND_8.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.
<!-- v7-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v7](18_DESIGN_ROUND_7.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.

> ⚠️ **بایگانی / superseded:** این سند مربوط به دورهای قبل است. طراحی فعلی **[DESIGN v6](17_DESIGN_ROUND_6.md)** است؛ صفحهٔ ورود حذف، یادگیری بازسازی و زیرصفحات «انتخاب مسیر / نمای مسیر / داخل مبحث» از کد اضافه شدند. لاگهای قدیمی صرفاً ردپای حسابرسیاند.

> 🔄 **DESIGN v5 (حکم فعلی) — بازآفرینی ۱۰۰٪ از داخل کد:** لاگ کامل ← `16_DESIGN_ROUND_5.md`، prototype ← `DESIGN/index.html`، هندسهٔ استخراجشده ← `DESIGN/CODE_GEOMETRY.json`.
> اصلاحیهٔ نامگذاری: دکمهٔ قدیمی «پاسخنامه» = **«پاسخبرگ»** (گزینههای زدهشده)؛ «پاسخنامه» دکمهای **جداگانه** برای جواب تشریحی/توضیحات است. یک دکمهٔ «توضیح با هوش مصنوعی» در صفحهٔ سؤالات + همان دکمه در صفحۀ آخر آزمون. لیدربورد اطلاعات/امتیازات/آزمونهای خود فرد را نشان میدهد. متن پایینتر، بایگانی دور قبل است و فقط برای ردیابی نگه داشته شده.


> مشکلی که خودتان گفتید: «بزرگترین مشکل عدم وفاداری به یو آی اصلی اپه… خیلی خیلی خیلی مهمه اینکه اپلیکیشن همون سازکار رو داشته باشه».
> این سند، پاسخ normative و قابلتست به آن است. **هر فاز اجرا بدون عبور از دروازههای F0…F9 مجاز به ادامه نیست.**

## ۱. منبع حقیقت (Source of Truth)

| منبع | مسیر | محتوا |
|---|---|---|
| استخراج ۰تا۱۰۰ دور قبل | `mimo-ui/` | ۱۴٬۳۹۸ عضو APK هش/طبقهبندیشده، ۱۲٬۹۱۵ شناسهٔ منبع، ۵۰٬۴۷۷ ردیف کانفیگ، ۲٬۸۵۹ AXML دیکدشده بدون خطا، **۱٬۲۹۹ لایوت**، **۲۷۶ دوسیه صفحه**، ۱۰۹ اسکلت Kotlin، ۵۳ ویوی سفارشی، ۱۶ سند فارسی |
| اطلس آفلاین | `mimo-ui/ATLAS/index.html` | نمایشگر self-contained تمام صفحات/لایوتها/توکنها |
| توکنها | `mimo-ui/CATALOGS/DESIGN_TOKENS.json`, `ATLAS/tokens.css` | ۱٬۱۹۸ رنگ، ۱٬۴۰۱ dimens/style/drawable، ۱۱۶ لوکال |
| راستیآزمایی | `mimo-ui/CATALOGS/VERIFICATION_REPORT.json` | `PASS` / ۱۸ چک / ۵٬۴۷۴ فایل هششده |

هیچ تصمیم بصری از حافظه، حدس، یا اسکرینشات اپهای دیگر گرفته نمیشود؛ فقط از این منابع.

## ۲. ناوبری — شاهد استخراج ۴ تب / **حکم محصول ۵ تب (v4)**

> ⚠️ **OVERRIDE صریح کاربر (دور چهارم):** «منوی پایین باید `learn / practice / ai / leaderboard / profile` باشه… صفحات چت با هوش مصنوعی رو قاتی بخش تمرین نکن».
> جدول زیر **واقعیت APK استخراجشده** است و بهعنوان شاهد بایگانی ماند؛ ولی **طرح نهایی محصول = ۵ تب** است. این تنها فاصلهٔ مجاز از استخراج خام میمو است و صرفاً بهدستور کاربر انجام شد. F0/F1 در `CATALOGS/UI_FIDELITY_RULES.csv` بر همین اساس بازنویسی شدند.

### ۲٫الف شاهد استخراج (APK واقعی): ۴ تب

`mimo-ui/SOURCE/res/menu/bottom_navigation_menu.xml`:

| ترتیب | id | آیکن | رشته | مقدار |
|---|---|---|---|---|
| ۱ | `bottom_navigation_item_track` | `ic_tab_learn` | `navigation_path` | Learn |
| ۲ | `bottom_navigation_item_practice` | `ic_tab_practice` | `navigation_practice` | Practice |
| ۳ | `bottom_navigation_item_leaderboard` | `ic_tab_leaderboard` | `navigation_leaderboard` | Leaderboard |
| ۴ | `bottom_navigation_item_profile` | `ic_tab_profile` | `navigation_profile` | Profile |

قالب: `main_activity_content.xml` با `contentFrame`, `navigation_bar`, `container_bottombar`.

**رد صریح انحرافها:**

| انحراف | منبع | حکم |
|---|---|---|
| ۵ تب `Learn / Practice / Max / Leaderboard / Profile` | `/home/user/_work/prev/mimo/shell/app.js` | ❌ تب `Max` ممنوع؛ ولی **۵ تب `Learn / Practice / AI / Leaderboard / Profile` بهحکم v4 الزامی است** |
| «۳ تب» در برخی اسناد قدیمی | `18_KONKUR_TRANSFER/ADAPTATION_PLAN.md` | ❌ اصلاح به **۵ تب (v4)** |
| قرار دادن موتورهای وب بهعنوان تب مستقل | همان پروتوتایپ | ❌ موتورها پشت مقصدهای درونتبی پروکسی میشوند |
| ساختن زبان بصری تازه برای کنکور | ریسک اصلی | ❌ ممنوع؛ فقط ترکیب مجدد کامپوننتهای موجود |

## ۳. قانون طلایی

> **هر صفحهٔ تازه = ترکیبی از کامپوننتها، توکنها، الگوهای ناوبری و رفتارهای ازپیشاستخراجشدهٔ Mimo. هیچ رنگ، فونت، شعاع، فاصله، انیمیشن، آیکن، متن یا الگوی تعامل تازهای تعریف نمیشود.**

بخشهای جدید **مقصد** هستند، نه **تب** و نه **برنامهٔ جدا**:

| بخش تازه | تب میزبان | نقطهٔ ورود از Mimo |
|---|---|---|
| هاب آزمونها | Practice | `practice_tab_fragment.xml` → `cv_practice_tab` (ComposeView) + `include @layout/toolbar` |
| مشاوره + ۷ قالب | Practice (کارت ورودی) / Leaderboard (رقابت) | `base_modal_card.xml`, `bottom_sheet_dialog`, `flash_bar_view.xml` |
| AI (ظاهر unchanged) | **تب مستقل AI (v4)**، نه داخل Practice | `coding_keyboard_layout.xml` → `btn_ai_tutor`, `iv_ai_tutor_pulse`؛ ۲۸ رشتهٔ `ai_tutor_*`؛ سطح چت Compose |
| پروفایل کنکوری | Profile | `profile_fragment.xml`, `profile_header_view.xml`, `profile_info_card_view.xml`, `profile_certificates_view.xml`, `profile_trophies_item.xml`, `profile_friends_*`, `public_profile_activity.xml`, `settings_fragment.xml` |
| دوستان/رقابت | Leaderboard | `leaderboard_fragment_active.xml`, `leaderboard_item.xml`, `leaderboard_podium_item.xml`, `leaderboard_result_*` |

## ۴. توکنهای الزامی (عیناً از استخراج)

رنگها (روز / شب):

| نقش | روز | شب |
|---|---|---|
| `background_primary` | `#FFF6F7FB` | `#FF252746` |
| `card_enabled` | `#FFFFFFFF` | `#FF3F4273` |
| `card_pressed` | `#FFF6F7FB` | `#FF333661` |
| `card_disabled` | `#FFE4E6F1` | `#FF1D1F32` |
| `card_outline` | `#FF7E4BDE` | `#FF885BDE` |
| `button_primary` | `#FF7E4BDE` | `#FF885BDE` |
| `text_primary` | `#FF252746` | `#FFFFFFFF` |
| `accent_success` | `#FF66BC5A` | `#FFA4E59B` |
| `error_default` | `#FFF05A6E` | `#FFF97F8D` |
| `code_background` | `#FFFFFFFF` | `#FF1D1F32` |
| `progress_chapter_primary` | `#FF8D60E2` | `#FFB89CED` |

ابعاد: فاصلهها `4 / 8 / 12 / 16 / 24 / 32 / 40dp`؛ نسخهٔ `sw600dp` برابر `6 / 12 / 16 / 24 / 36 / 48 / 60dp`؛ شعاع غالب `12dp`، بلوک کد `6dp`؛ `content_max_width 608dp`؛ `bottom_sheet_content_max_width 496dp`؛ `lesson_progressbar_height 6dp` (`sw600dp: 8dp`)؛ `coding_keyboard_height 64dp`؛ `modal_default_width 296dp` (`sw600dp: 360dp`)؛ `streak_calendar_height 264dp` (`sw600dp: 324dp`)؛ `toolbar_height`، `lesson_progress_navbar_height`، `lesson_feedback_sheet_peek_height 112dp`. تایپوگرافی ۱۲…۴۲sp (شمارندهٔ XP = ۴۲sp، متن ادیتور کد = ۱۵sp).

حرکت: ۷۲ `anim/`، ۴۷ `animator/`، ۲۴ interpolator، ۵۹ Rive، `bottom_sheet_slide_in/out`، `fade_in/out`، پالس AI، `ArcProgressView`، `lesson_progressbar`، `avatar_progress_bar`. صفحات تازه از همان منحنیها و مدتها استفاده میکنند.

## ۵. کامپوننتهای قابل استقرار مجدد

- ۷۱ لایوت دارای `ComposeView`، `ViewPager2` (نمایش درسها)، `FragmentContainerView`، `AppBarLayout` + `ChapterToolbar` / `include @layout/toolbar`، ۲٬۷۷۱ `<include>/<merge>`.
- ۵۳ ویوی سفارشی: `ArcProgressView`, `AvatarProgressBar`, `AnswerButtonGrid`, `CodingKeyboardView`, `ExpandableTextView`, `LessonFeedbackView`, `MimoCodeEditor`, `RiveAnimationView`, `ShimmerFrameLayout`, `StreakCalendarView`, `BottomSheetHandleView` …
- قطعات آماده: `base_modal_card.xml` ( modal عمومی )، `flash_bar_view.xml` (پیام/اقدام)، `reward_box.xml`، `daily_sparks_goal_progress_view.xml`، `streak_bottom_sheet_content.xml`، `chapter_finished_fragment.xml` (صفحهٔ نتیجه)، `leaderboard_result_*`، `report_lesson_fragment.xml`، `lesson_interactive_*` (سؤالات تک/چندگزینهای، جایخالی، ورودی اعتبارسنجیشده).

## ۶. دروازههای وفاداری (Fidelity Gates) — برای هر فاز

| id | چک قابلسنجش | معیار قبولی |
|---|---|---|
| F0 | تعداد آیتمهای `bottom_navigation_menu.xml` | دقیقاً ۴، با همان id/آیکن/رشته |
| F1 | تعداد تبای ساختهشده در shell | ۴؛ هیچ `Max`/`Exam`/`Counseling` tab وجود ندارد |
| F2 | منبع هر رنگ/فاصله/شعاع/فونت صفحهٔ تازه | قابل ردیابی به `DESIGN_TOKENS.json`؛ ۰ مقدار هاردکد تازه |
| F3 | منبع ساختار هر صفحهٔ تازه | حداقل یک دوسیه از `mimo-ui/SCREENS/` یا `LAYOUTS/` بهعنوان الگو ثبت شود |
| F4 | رفتار بازگشت/باتمشیت/مودال | همان زنجیرهٔ مودال Mimo؛ بستن با `iv_modal_close`، `backdrop dismiss` |
| F5 | حالتهای کارت | `card_enabled/pressed/disabled/outline` + نایت مُد، بدون حالت تازه |
| F6 | RTL | همهٔ صفحات فارسی `layoutDirection=rtl`؛ فقط کروم کد/فرمول LTR؛ اعداد فارسی طبق policy |
| F7 | دارایی | ۰ کپی از asset/رشته/کد Mimo، همدرس، هدفپلاس در محصول (clean-room) |
| F8 | تحلیل اثر | لیست `include`/`xref` صفحهٔ تازه با `mimo-ui/CATALOGS/LAYOUT_XREFS.csv` مقایسه شود |
| F9 | مقایسهٔ بصری | diff اطلس: صفحهٔ تازه در کنار دوسیهٔ مرجع، حداقل ۹۰٪ تطابق توکن/فاصله (تست خودکار + نگاه انسانی) |

**هرگونه تغییر ظاهری در بخش AI فقط در حد اضافهشدن دکمههای پنل اصلی Learn Harness مجاز است** (`04_AI_LEARN_HARNESS.md` §۴٫۴)؛ حذف هیچ عنصری مجاز نیست. ناوبری ۵تبهٔ v4 حکم صریح کاربر است.

## ۷. «سازوکار» یعنی چه (غیر از ظاهر)

وفاداری فقط رنگ نیست؛ این رفتارهاهمچنین باید حفظ شوند:

1. **مسیر درسی بهصورت گرههای پیشرونده** با حالتهای قفل/فعال/تکمیلشده و نوار پیشرفت ۶dp؛ هاب آزمون همین الگو را برای گرههای آزمون تکرار میکند.
2. **حلقهٔ درس**: نمایش → پاسخ → بازخورد فوری (`lesson_interactive_feedback_bottom_sheet_dialog.xml`) → XP → صفحهٔ پایان فصل → streak → لیدربورد.
3. **پیشرفت سهگانه** (`chapterProgress`, `tutorialProgress`, `trackProgress`) و `globalStats`؛ هر فیچر تازه باید به همان سهگانه بنشیند.
4. **آفلاین + outbox**: محتوا باندل، نتایج در صف، همگامسازی بعداً؛ موتورها دیتاستور جدا دارند.
5. **Daily goal / Sparks / Streak / League**: همان مدل امتیاز و همان `daily_sparks_goal_progress_view.xml`.
6. **مودال/باتمشیت بهجای صفحهٔ تمامصفحه** برای تنظیمات سریع؛ `contentDescription` و `TextInputLayout` برای دسترسپذیری.
7. **WebView lesson bridge** (`gesture/activity/focus/height`, `MimoLesson.postMessage`) برای درسهای تعاملی موجود؛ سؤالات کنکور یا همین پل را استفاده میکنند یا `lesson_interactive_*` بومی.

## ۸. ضدرگرسیون — چکلیست قبل از هر PR اجرایی

- [ ] `F0…F9` همگی PASS و نتیجه در `CATALOGS/FIDELITY_CHECKS.json` ثبت شده
- [ ] ناوبری دقیقاً ۵ تب `Learn / Practice / AI / Leaderboard / Profile` (F0 v4)؛ هیچ تب/صفحهای با نام موتور (`Max`, `Practice Machine`, `LearnHarness`) دیده نمیشود
- [ ] هیچ صفحهٔ اشتراک/پرداختی اضافه نشده است
- [ ] رشتههای `ai_tutor_*` تغییر نکردهاند
- [ ] نسخهٔ نایت مُد تست شده
- [ ] `ATLAS/index.html` همچنان مرجع است و دوسیهٔ صفحهٔ تازه به آن اضافه شده
