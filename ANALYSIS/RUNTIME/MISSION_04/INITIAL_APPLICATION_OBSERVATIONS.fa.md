# MISSION 04 — مشاهدات اولیه از برنامه در حال اجرا

| شناسه | مقدار |
|---|---|
| Workflow run ID | **`41998643355`** |
| Branch / commit | `arena/aebb90b7-game` / `92e87fe8d061ea4c11089f40a7c8ce73d34d816a` |
| Timestamp | `2026-11-05T09:01:45Z` |
| پیکربندی شبیهساز | API 36 / Android 16 / `pixel_7` / `google_apis` / `x86_64` / headless |

> این پرونده جایگزین نسخهٔ BLOCKED همنام (محفوظ در `PREVIOUS_BLOCKED_REPORTS/`) شده است.

## `OBSERVED` — مشاهدات مستقیم

- `com.getmimo` نصب و با PID `4266` در حال اجرا است
  (`adb shell ps -A`, `pidof`).
- Activity پیشزمینه:
  `com.getmimo/com.getmimo.ui.onboarding.intro.IntroSlidesActivity`
  (`mCurrentFocus`، `topResumedActivity`).
- صفحهٔ قابلرویت: سومین اسلاید کاروسل onboarding،
  عنوان **Change your career**، توضیح
  «Use your portfolio of projects to apply for a job and change your career»،
  دکمهٔ **Get started** و پیوند **I already have an account**،
  بههمراه نشانگر سه نقطهای صفحه.
- سلسلهمراتب UI شامل ۱۵ گره با `package="com.getmimo"` است؛
  شناسهها: `com.getmimo:id/vp_intro_slides`،
  `tv_onboarding_page_title`، `tv_onboarding_page_description`،
  `compose_content`، و عناصر دکمه/پیوند. متن اسلایدهای دیگر
  (`Build projects`، «Apply what you've learned ...») نیز در همان XML موجود است،
  که نشان میدهد کاروسل بارگذاری شده است.
- تصویر `SCREENSHOTS/TEST-004_first_usable_screen.png` (`65373` B) همین محتوا را
  بهصورت چشمی نشان میدهد؛ نه لانچر است و نه dialog سیستم.
- چهار کتابخانهٔ بومی `arm64` بار شدند (`: ok`)؛ Google Play services هشدار
  «out of date» داد ولی مانع رندر صفحه نشد.
- بافر crash خالی از `FATAL EXCEPTION` متعلق به Mimo است.

## `NOT OBSERVED` — مرز مأموریت

هیچ لمس دکمه، ورود به حساب، ناوبری درونبرنامه، بارگذاری درس، درخواست تأییدشده
به سرور، یا مشاهدهٔ پاسخ بکاند انجام نشد. بنابراین دربارهٔ جریان ثبتنام،
احراز هویت، محتوای دورهها، نمرهدهی، یا هندسۀ صفحات بعدی هیچ ادعایی ثبت نمیشود.
`SERVER CONFIRMED = 0`؛ مأموریت در مرز احراز هویت متوقف شد.

**ارجاع شواهد:** `SCREENSHOTS/TEST-004_first_usable_screen.png`،
`UI_HIERARCHY/TEST-003_initial_screen.xml`، `APPLICATION_LAUNCH.txt`،
`LOGS/LOGCAT_MIMO.txt`، `TEST_RESULTS.json`.
