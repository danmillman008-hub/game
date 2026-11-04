# پروفایل با ظاهر خود میمو + گیمیفیکشن سراسری و اجباری
<!-- v12-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v12](24_DESIGN_ROUND_12.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.
<!-- v11-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v11](23_DESIGN_ROUND_11.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.
<!-- v10-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v10](22_DESIGN_ROUND_10.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.
<!-- v9-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v9](21_DESIGN_ROUND_9.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.
<!-- v8-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v8](20_DESIGN_ROUND_8.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.
<!-- v7-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v7](18_DESIGN_ROUND_7.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.

> ⚠️ **بایگانی / superseded:** این سند مربوط به دورهای قبل است. طراحی فعلی **[DESIGN v6](17_DESIGN_ROUND_6.md)** است؛ صفحهٔ ورود حذف، یادگیری بازسازی و زیرصفحات «انتخاب مسیر / نمای مسیر / داخل مبحث» از کد اضافه شدند. لاگهای قدیمی صرفاً ردپای حسابرسیاند.

> 🔄 **DESIGN v5 (حکم فعلی) — بازآفرینی ۱۰۰٪ از داخل کد:** لاگ کامل ← `16_DESIGN_ROUND_5.md`، prototype ← `DESIGN/index.html`، هندسهٔ استخراجشده ← `DESIGN/CODE_GEOMETRY.json`.
> اصلاحیهٔ نامگذاری: دکمهٔ قدیمی «پاسخنامه» = **«پاسخبرگ»** (گزینههای زدهشده)؛ «پاسخنامه» دکمهای **جداگانه** برای جواب تشریحی/توضیحات است. یک دکمهٔ «توضیح با هوش مصنوعی» در صفحهٔ سؤالات + همان دکمه در صفحۀ آخر آزمون. لیدربورد اطلاعات/امتیازات/آزمونهای خود فرد را نشان میدهد. متن پایینتر، بایگانی دور قبل است و فقط برای ردیابی نگه داشته شده.


خواسته: «یه صفحه هم پروفایل کاربر هست که اون از ظاهر خود میمو استفاده کن… حتما باید گیمیفیکشن داشته باشه امتیاز تو ازمونها و بقیه قسمتها… دوسن مت و اون بخش مشاوره هم یه جورای از همون یه دیزاین اصلی میمو باید استفاده کنی».

## ۱. پروفایل = کامپوننتهای موجود، نه صفحهٔ تازه

| نیاز | لایوت Mimo موجود |
|---|---|
| قاب پروفایل | `profile_fragment.xml`, `profile_header_view.xml`, `profile_header_unlocked.xml`, `public_profile_activity.xml` |
| کارت اطلاعات | `profile_info_card_view.xml`, `settings_user_settings.xml` (نام/ایمیل/بیو/آواتار) |
| گواهیها/دستاوردها | `profile_certificates_view.xml`, `profile_certificates_item.xml`, `profile_certificates_max_item.xml`, `profile_trophies_item.xml`, `profile_empty_trophies_item.xml` |
| دوستان/دعوت | `profile_friend_item.xml`, `profile_friends_header.xml`, `profile_friends_invite_card.xml`, `profile_friends_empty.xml`, `public_profile_code_header_view.xml` |
| تنظیمات | `settings_fragment.xml`, `set_daily_goal_activity.xml`, `set_daily_goal_card.xml` |
| پیشرفت روزانه | `daily_sparks_goal_progress_view.xml` |

فیلدهای تازهٔ کنکور (پایه، رشتهٔ هدف، تراز کل، رتبه/سهمیه، روزهای باقیمانده تا کنکور — شاهد `motivational_phrase.json`) **در همان `profile_info_card_view`** و با همان ۱۲sp/۱۴sp/۱۶sp و `card_enabled` نمایش داده میشوند. رشتهٔ `daysRemainingToKunkor` بهصورت chip ایستا در هدر (همان جای `streak`).

## ۲. سیستم واحد امتیاز (از سند `19`: «one currency per mode»)

| واحد | منبع | کجا خرج/نمایش داده میشود |
|---|---|---|
| **Sparks / XP** | `daily_sparks_goal_progress_view.xml` (شمارندهٔ ۴۲sp)، `chapter_finished_stats` | هدف روزانه، لیگ، صفحهٔ پایان |
| **Streak (شعله)** | `streak_bottom_sheet_content.xml`, `streak_calendar_height 264dp` | تقویم هفتگی، نجاتدهندهٔ روزها |
| **League / رتبه** | `leaderboard_fragment_active.xml`, `leaderboard_league_header_view.xml`, `leaderboard_podium_item.xml`, ۲۴ لایوت نتیجه | تب Leaderboard، لیگ هفتگی |
| **نشان/جایزه** | `reward_box.xml`, `profile_trophies_item.xml`, `chapter_finished_*` | پروفایل، کمد جوایز |
| **تراز/درصد آزمون** | نتیجهٔ آزمون (جدید) | تحلیل آزمون، پروفایل، رقابت — **عدد جدا، نه پول تازه** |

قاعده: «دوسن مت» (تفسیر: بخش **دوستان/رفاقت و رقابت**) و مشاوره هم **در همین سیستم** تعریف میشوند، نه سیستم موازی؛ دقیقاً همان `leaderboard_*` و `profile_friends_*` میمو.

## ۳. جدول امتیازدهی سراسری (ماشینخوان در `CATALOGS/GAMIFICATION_MAP.csv`)

| رویداد | قاعده | واحد | منبع الهام |
|---|---|---|---|
| پاسخ درست در آزمون | `difficulty(1..5) × subjectFactor` (تخصصی ×۲) | XP | همدرس: «1 point for simple… 5 points for Olympiad», «specialized subjects have twice the points» |
| پاسخ غلط | `−⅓ × difficulty` (نمرهٔ منفی، قابلپیکربندی) | XP/درصد | هدفپلاس: `اثر نمرهٔ منفی` |
| اتمام آزمون زماندار | bonus تکمیل + bonus سرعت هوشمند (بدون تشویق عجله) | XP | خواسته |
| اولین تلاش /Without hint | ضریب ۱٫۲ | XP | `visible-if`/hints میمو |
| مرور غلط → درست دوبار متوالی | XP + حذف از لیست غلطها | XP + FSRS | همدرس «تمرین اشتباههای تمام مباحث» |
| درس/فصل کامل میمو | همان منطق `applyResult` موجود (دستنخورده) | Sparks | HANDOFF |
| هدف روزانه | همان `set_daily_goal_*` | Streak | Mimo |
| فعالسازی یکی از ۷ قالب | XP ثابت + streak تقویم | XP/Streak | هدفپلاس |
| اجرای روزِ برنامهٔ مشاور | XP + گزارش روزانه | XP | `report_model.json` |
| جلسهٔ AI/LearnHarness | XP برای «توضیح تفکر» و «بازبینی گراف» (نه صرفاً چت) | XP | LH thinking fields |
| دوستان/رقابت | امتیاز لیگ همان `leaderboard_*`؛ دعوت دوست = جایزهٔ `reward_box` | League | همدرس `comp-*`, هدفپلاس `league_model` |
| تحلیل آزمون ثبتشده | نشان «تحلیلگر» | نشان | هدفپلاس `تحلیل آزمون` |
| فلشکارت/پومودورو/کرنومتر | همان مدل امتیاز همدرس، به واحد میمو ترجمه شود | XP/Streak | helpcenter `start-points`, `study-time`, `study-pomodoro` |

**ضد تورم**: سقف روزانهٔ XP قابل کسب از بخشهای تازه (cap)، ثبت `xpPolicy` در Blueprint هر آزمون، و تست «هیچ مسیری XP بیکران تولید نمیکند».

## ۴. «دوسن مت» — تفسیر و طراحی

عبارت در پیام شما ابهام دارد؛ در این پلن بهعنوان **بخش دوستان / رفاقت و رقابت** تفسیر شد (شواهد: `comp` همدرس با ۶ درس `comp-start/comp-friends/comp-friendship/comp-messages/comp-prize/comp-history`؛ هدفپلاس `league_model.json` و `images/league/`؛ میمو `leaderboard_*` + `profile_friends_*`). if منظور دیگری بود، فقط `CATALOGS/OPEN_QUESTIONS.csv` و فاز P0 اصلاح میشود. طراحی: همان تب Leaderboard، همان `leaderboard_item.xml`، همان `reward_box`؛ چت دوستان با همان حبابهای میمو؛ رقابت «پنج دایره»ی همدرس بهصورت خلاصهٔ نتیجه در `chapter_finished_fragment.xml`.

## ۵. پذیرش فاز P6

- [ ] پروفایل با ۰ لایوت تازه؛ فقط دادهٔ کنکوری در کارتهای موجود
- [ ] تکتک رویدادهای جدول بالا یک `xpEvent` نسخهدار تولید میکنند و در outbox ثبت میشوند
- [ ] نمایش یکپارچه در `daily_sparks_goal_progress_view`, streak, league, trophies
- [ ] بخش مشاوره و دوستان/رقابت هیچ واحد پول/امتیاز جداگانهای نساختهاند
- [ ] نایت مُد، RTL، `contentDescription` و سقف روزانه تست شده
