# ناوبری و معماری اطلاعات — همان ۴ تب، مقصدهای تازه

## ۱. ساختار ثابت

```
MainActivity (main_activity_content.xml)
├── contentFrame ......................... میزبان ۴ تب
├── container_bottombar
└── navigation_bar (bottom_navigation_menu.xml: ۴ آیتم)
      ├── Learn ................ مسیر درسی میمو (دستنخورده)
      ├── Practice ............. cv_practice_tab  → [ آزمونها ] [ مشاوره ] [ ابزارها ] [ درسهای موجود ]
      ├── Leaderboard .......... لیگ/دوستان/رقابت (همان leaderboard_*)
      └── Profile .............. پروفایل کنکوری (همان profile_*)
```

- ۶۱ اکتیویتی، ۶ alias، ۴۶ `<data>`، ۱ گراف ناوبری، `SplashActivity_default` alias از استخراج Mimo → گراف موجود **توسعه** مییابد، **جایگزین** نمیشود.
- زنجیرهٔ مودال Mimo حفظ شود: onboarding → daily goal → lesson → feedback → chapter finished → streak → leaderboard result. آزمونها به همین زنجیره وصل میشوند (`chapter_finished_fragment.xml` همان صفحهٔ نتیجه است).

## ۲. مقصدها (درون تب، بدون تب تازه)

| مسیر | تب | الگوی میمو | یادداشت |
|---|---|---|---|
| `exam/hub` | Practice | گرههای درسی | گرید ۳تایی |
| `exam/setup/{type}` | Practice | `base_modal_card` | باتمشیت |
| `exam/run/{examId}` | Practice | `lesson_interactive_*` | فولاسکرین موقت، ناوبری پنهان (الگوی خود میمو در درس) |
| `exam/result/{attemptId}` | Practice | `chapter_finished_fragment` | XP/streak |
| `exam/analysis/{attemptId}` | Practice | `report_lesson_fragment` | چارت/نقشهٔ ضعف |
| `exam/review/{topicId}` | Practice | `WrongView` معادل بومی | FSRS |
| `counseling/hub` | Practice | کارت/گره | ۷ قالب + خدمات |
| `counseling/templates` | Practice | گرید ۳تایی | ۷ قالب |
| `counseling/request` | Practice | مودال فرم | بدون پرداخت |
| `counseling/plans|reports|chat` | Practice/Profile | باتمشیت/کارت | `/Advisor/Plans` معادل |
| `ai/tutor` | همان محل | AI Tutor Compose | ظاهر frozen |
| `max/*` | (پشت AI) | پروکسی | prefix حفظ میشود |
| `leaderboard/*` | Leaderboard | موجود | دوستان/رقابت |
| `profile/*` | Profile | موجود | فیلدهای کنکوری |

## ۳. دیپلینکها

`konkur://exam/{examId}`, `konkur://exam/result/{attemptId}`, `konkur://counseling/template/{id}`, `konkur://max/session/{id}`, `konkur://review/{topicId}` — همگی به `contentFrame` تب مربوطه هدایت میشوند و back stack میمو را رعایت میکنند (بازگشت به هاب، نه خروج از اپ).

## ۴. قواعد رفتاری

- دکمهٔ بازگشت سختافزاری: در `exam/run` → پنل «خروج از آزمون؟»؛ در باتمشیتها → dismiss؛ در هاب → تب قبلی.
- در حالت آزمون، `navigation_bar` مثل حالت درس میمو پنهان میشود تا تمرکز حفظ شود (رفتار موجود، نه اختراع تازه).
- وضعیتها: قفل/`card_disabled` تا زمان بازشدن آزمون ماه؛ `card_outline` برای جاری؛ `accent_success` برای گذرانده.
- آفلاین: تمام مقصدها از بستهٔ محتوا/بانک محلی کار میکنند؛ `/max` و `/practice` در نبود سرور پیام `ai_tutor_offline_description` / معادل میمو نشان میدهند.

## ۵. پذیرش

- [ ] `bottom_navigation_menu.xml` عیناً ۴ آیتم (F0)
- [ ] ۰ `<item>` تازه، ۰ tab تازه در shell (F1)
- [ ] هر مقصد تازه یک دوسیهٔ مرجع از `mimo-ui/SCREENS/` دارد (F3)
- [ ] دیپلینکها + back stack + پنهانسازی ناوبری در آزمون تست شده
