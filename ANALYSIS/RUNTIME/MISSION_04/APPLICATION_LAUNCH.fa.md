# MISSION 04 — اجرای برنامه واقعی (APPLICATION LAUNCH)

| شناسه | مقدار |
|---|---|
| Workflow run ID | **`41998643355`** |
| Branch / commit | `arena/aebb90b7-game` / `92e87fe8d061ea4c11089f40a7c8ce73d34d816a` |
| Timestamp | `2026-11-05T09:01:45Z` |
| پیکربندی شبیهساز | API 36 / Android 16 / `pixel_7` / `google_apis` / `x86_64` / headless |
| نتیجه | **Mimo اجرا شد، `pid=4266`، `IntroSlidesActivity` در foreground** |

## ۱. کشف Activity واقعی (نه حدس) — `OBSERVED`

```
$ adb shell cmd package resolve-activity --brief -a android.intent.action.MAIN -c android.intent.category.LAUNCHER com.getmimo
priority=0 preferredOrder=0 match=0x108000 specificIndex=-1 isDefault=false
com.getmimo/.ui.SplashActivity_default

resolved_launcher=com.getmimo/.ui.SplashActivity_default
```
`SplashActivity` ایستا یک «کاندید» بود؛ Activity قابلاجرا از `resolve-activity`
روی بستهٔ نصبشده بهدست آمد. (M03 مسیر `com.getmimo.ui.SplashActivity` و
M04 مسیر `_default` متفاوت ثبت کردند؛ هر دو `OBSERVED`اند و تفاوت ناشی از
alias/exported component است — حدسی دراینباره ثبت نمیشود.)

## ۲. فرمان اجرا و بررسی بیوقفه — `OBSERVED`

```
$ adb shell am start -n com.getmimo/.ui.SplashActivity_default
Starting: Intent { cmp=com.getmimo/.ui.SplashActivity_default }
am_start_exit=0
initial_focus_on_mimo=yes
pid=4266
```

| بررسی | خروجی واقعی |
|---|---|
| `pidof com.getmimo` | `4266` |
| `dumpsys activity activities \| grep mCurrentFocus` | `mCurrentFocus=Window{3fb7b94 u0 com.getmimo/com.getmimo.ui.onboarding.intro.IntroSlidesActivity}` |
| `mResumedActivity` | `topResumedActivity=ActivityRecord{80027096 u0 com.getmimo/.ui.onboarding.intro.IntroSlidesActivity t8}` |
| `dumpsys window \| grep mCurrentFocus` | همان پنجرهٔ `com.getmimo` |
| crash فوری | `FATAL EXCEPTION` / `Process: com.getmimo` یافت نشد |

`adb shell ps -A | grep com.getmimo` و `dumpsys activity processes` نیز در
`APPLICATION_LAUNCH.txt` ذخیره شدهاند. `IntroSlidesActivity` (صفحهٔ آغازین
onboarding) Activityای است که Splash پس از گذر به آن منتقل میکند؛
هر دو متعلق به همان بستهٔ `com.getmimo` هستند.

## ۳. تصویر و سلسلهمراتب UI واقعی — `OBSERVED`

| پرونده | اندازه | محتوا |
|---|---|---|
| `SCREENSHOTS/TEST-002_splash.png` | `34635` B | لحظهٔ ۳ ثانیه پس از `am start` |
| `SCREENSHOTS/TEST-003_initial_screen.png` | `65373` B | اولین صفحهٔ قابلاستفاده |
| `SCREENSHOTS/TEST-004_first_usable_screen.png` | `65373` B | کپی همان فریم، نام پایدار |
| `UI_HIERARCHY/TEST-003_initial_screen.xml` | XML اصلی `uiautomator dump` | **۱۵ گره `package="com.getmimo"`** |

متنهای استخراجشده از XML:
`Change your career`،
`Use your portfolio of projects to apply for a job and change your career`،
`Build projects`،
`Apply what you've learned and build real-world projects with step-by-step guidance`،
`Get started`، `I already have an account`.

```
mimo_nodes_in_ui_hierarchy=true
     15 package="com.getmimo"
```
تصویر نهایی (بازبینی چشمی `read_file`): اسلاید سوم کاروسل onboarding با عنوان
**Change your career**، دکمهٔ بنفش **Get started**، پیوند **I already have an account**
و سه نقطهٔ نشانگر صفحه — بدون dialog سیستم، بدون لانچر.
عکسی از صفحهٔ خانۀ Android **بهعنوان شاهد Mimo پذیرفته نشد**؛
دو اجرای نخست دقیقاً بههمین دلیل مردود اعلام شدند.

## ۴. لاگها و وضعیت ANR — `OBSERVED`

```
LOGS/ANR_DISMISSAL.txt: anr_dialog_attempt_1 none
  mCurrentFocus=Window{3fb7b94 u0 com.getmimo/...IntroSlidesActivity}
```
هیچ dialog `Application Not Responding` در این اجرا وجود نداشت، بنابراین حلقهٔ
رفع ANR وارد عمل نشد. `LOGS/LOGCAT_MIMO.txt`، `CRASH_AND_ERROR_LOGS.txt`
(شامل بافر crash)، و `LOGS/` کامل ذخیره شدهاند.

## ۵. محدوده — `NOT OBSERVED`

اجرای برنامه، فرآیند، Activity و UI اثبات شد. **هیچ تعاملی** انجام نشد:
دکمهها لمس نشدند، وارد حساب کاربری نشد، درخواست شبکهای به بکاند Mimo بررسی/تأیید
نشد، و هیچ credential، پاسخ جعلی، دورزدن احراز هویت، خرید یا TLS bypass بهکار نرفت.
مأموریت دقیقاً در **مرز احراز هویت** متوقف شد. `SERVER CONFIRMED = 0` و از اجرای
کلاینت هیچ نتیجهای دربارهٔ سرور استنتاج نمیشود.

**ارجاع شواهد:** `APPLICATION_LAUNCH.txt`، `LOGS/ANR_DISMISSAL.txt`،
`LOGS/UI_HIERARCHY_CHECK.txt`، `LOGS/SCREENSHOT_INFO.txt`، `SCREENSHOTS/`،
`UI_HIERARCHY/TEST-003_initial_screen.xml`، `LOGS/LOGCAT_MIMO.txt`.
