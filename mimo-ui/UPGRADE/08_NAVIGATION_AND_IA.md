# ناوبری و معماری اطلاعات — **۵ تب** (حکم نهایی v4)
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


> ⚠️ استخراج Mimo 9.35 چهار تب داشت؛ بهدستور صریح کاربر در دور چهارم، طرح محصول **۵ تب** شد و چت AI تب مستقل گرفت. جزئیات override در `02_UI_FIDELITY_CONTRACT.md` §۲ و `15_DESIGN_ROUND_4.md` §۲.

## ۱. ساختار ثابت

```
MainActivity (main_activity_content.xml)
├── contentFrame ......................... میزبان ۵ تب
├── container_bottombar
└── navigation_bar (v4: ۵ آیتم)
      ├── Learn ................ مسیر درسی میمو (دستنخورده؛ فقط نام مباحث کنکوری)
      ├── Practice ............. cv_practice_tab → [ هاب آزمونها ] (۷ بخش لیبلدار، اسکرول یکصفحهای)
      ├── AI ................... چت مینیمال + دکمههای LH + تاریخچه (تب مستقل، قاتی Practice نشده)
      ├── Leaderboard .......... لیگ/دوستان/رقابت (همان leaderboard_*)
      └── Profile .............. پروفایل کنکوری (همان profile_*) + تنظیمات (کلید API فقط یادداشت)
```

- ترتیب دقیق: `Learn / Practice / AI / Leaderboard / Profile`. ۰ تب ششم، ۰ تب `Max`، ۰ تب موتور.
- زنجیرهٔ مودال Mimo حفظ شود: onboarding → daily goal → lesson → feedback → chapter finished → streak → leaderboard result. آزمونها به همین زنجیره وصل میشوند.
- **بخش Learn عیناً میمو**: گرهها، نوار پیشرفت، streak، کارت هدف و باتمشیتها؛ تنها تفاوت = نام درسها/مباحث (زیست/شیمی/فیزیک/…).

## ۲. مقصدها

| مسیر | تب | الگوی میمو | یادداشت |
|---|---|---|---|
| `learn/*` | Learn | موجود | دستنخورده، فقط محتوای کنکوری |
| `exam/hub` | Practice | گرههای درسی | **۷ بخش لیبلدار + فیلد قالب + اسکرول** |
| `exam/setup/{type}` | Practice | `base_modal_card` | باتمشیت |
| `exam/run/{examId}` | Practice | `lesson_interactive_*` | فولاسکرین موقت، ناوبری پنهان، تایمر داخل آزمون |
| `exam/answersheet/{attemptId}` | Practice | باتمشیت | «پاسخنامه» حین آزمون فقط برای انواع مجاز |
| `exam/result/{attemptId}` | Practice | `chapter_finished_fragment` | پاسخنامهٔ تستی + تشریحی + تحلیل |
| `exam/analysis/{attemptId}` | Practice | `report_lesson_fragment` | چارت/نقشهٔ ضعف/شبیهسازی غلطها |
| `exam/review/{topicId}` | Practice | `WrongView` معادل بومی | FSRS |
| `ai/tutor` | **AI** | AI Tutor Compose | چت مینیمال؛ ظاهر frozen |
| `ai/history` | AI | باتمشیت | گفتگوها + «گفتگوی تازه» |
| `max/*` | (پشت AI) | پروکسی | prefix حفظ میشود |
| `leaderboard/*` | Leaderboard | موجود | دوستان/رقابت |
| `profile/*` | Profile | موجود | فیلدهای کنکوری |
| `settings/api-key` | Profile | `settings_fragment` | **الزام مستند، ولی فعلاً طراحی UI نشده** (v4) |
| `counseling/*` | — | — | **PARKED (v3)**؛ هیچ مسیر فعالی |

## ۳. دیپلینکها

`konkur://exam/{examId}`, `konkur://exam/result/{attemptId}`, `konkur://ai/session/{id}`, `konkur://review/{topicId}` — همگی به `contentFrame` تب مربوطه هدایت میشوند و back stack میمو را رعایت میکنند (بازگشت به هاب، نه خروج از اپ).

## ۴. قواعد رفتاری

- دکمهٔ بازگشت سختافزاری: در `exam/run` → پنل «خروج از آزمون؟»؛ در باتمشیتها → dismiss؛ در هاب → تب قبلی.
- در حالت آزمون، `navigation_bar` مثل حالت درس میمو پنهان میشود.
- وضعیتها: قفل/`card_disabled` تا زمان بازشدن آزمون ماه؛ `card_outline` برای جاری؛ `accent_success` برای گذرانده.
- آفلاین: تمام مقصدها از بستهٔ محتوا/بانک محلی کار میکنند؛ `/max` در نبود کلید API پیام `ai_tutor_offline_description` نشان میدهد.

## ۵. پذیرش

- [ ] ناوبری دقیقاً **۵ تب** بهترتیب `Learn / Practice / AI / Leaderboard / Profile` (F0 v4)
- [ ] چت AI داخل Practice نیست؛ `Max` و هر تب اضافی ممنوع (F1 v4)
- [ ] Learn عین میمو، فقط نام مباحث/درسها فرق دارد
- [ ] هاب آزمون ۷ لیبل + قالب مشخص + اسکرول در همان صفحه
- [ ] هر مقصد تازه یک دوسیهٔ مرجع از `mimo-ui/SCREENS/` دارد (F3)
- [ ] دیپلینکها + back stack + پنهانسازی ناوبری در آزمون تست شده
