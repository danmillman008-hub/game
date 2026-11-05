# مأموریت ۰۳ — نصب APK (APK INSTALLATION)

**نتیجه:** `BLOCKED` — **هیچ APKـای نصب نشد.** Test ID: `TEST-001` · وضعیت: `UNKNOWN` (نه `RUNTIME VERIFIED`).
**شناسهٔ اجرای مرجع:** `41950695024` · تاریخ UTC: `2026-11-05T01:44`–`01:50`
**API/پروفایل:** API 36 / Android 16 / `pixel_7` / `google_apis` / `x86_64` / headless
**SHA-256 مورد انتظار:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`
**اندازهٔ مورد انتظار:** ۱۴۲٬۳۵۳٬۴۹۹ بایت · بسته: `com.getmimo` · نسخه: `9.35`
**ارجاع اسکرینشات:** `SCREENSHOTS/TEST-000_emulator_home.png` (لانچر سیستم، **نه** Mimo)
**ارجاع لاگ:** `LOGS/DISPLAY_STATE.txt`، `LOGS/LOGCAT_000_system_sanitized.txt`، `CRASH_AND_ERROR_LOGS.txt`

## ۱. آنچه دقیقاً انجام نشد

`adb install -r` اجرا **نشد**؛ `adb shell pm path com.getmimo` اجرا نشد؛
`dumpsys package com.getmimo` اجرا نشد؛ هیچ فرآیند `com.getmimo`ـای روی دستگاه وجود نداشت.
بنابراین گزارههای زیر همگی `UNKNOWN`اند و هیچکدام تأیید یا رد نشدهاند:

- نصبپذیری عملی APK روی API 36؛
- بارگذاری ۱۲ کتابخانهٔ بومی `arm64-v8a` / `armeabi-v7a`؛
- نسخهٔ نصبشده، مسیر APK، امضای نصبشده، فرآیند و activity لانچر؛
- سازگاری با GMS / Play Store / Play Integrity.

## ۲. علت دقیق انسداد — `OBSERVED`

ورکفلو ورودی `apk_url` دارد، ولی در اجرا خالی بود. جستوجوی منبع مجاز، نتیجههای زیر را داد:

| منبع بررسیشده | نتیجه |
|---|---|
| مخزن Git | فقط `ttac-4.3.6.apk` (غیرمرتبط) ردیابی میشود؛ APK اصلی Mimo **در مخزن نیست** |
| ۱۲ پروندهٔ DEX در `ANALYSIS/_INPUT/` | کپی بایتیک DEXاند، **نه APK**؛ ساخت APK جایگزین از DEX ممنوع است |
| ورکفلوهای موجود شاخه و `main` | هیچ `APK_URL` / `MIMO_APK` / لینک دانلود Drive / مکانیزم دریافت APK یافت نشد |
| Secrets / Variables اکشنها | `gh secret list` ↔ `HTTP 403: Resource not accessible by integration`؛ `gh api .../actions/secrets` و `/variables` ↔ 403؛ `gh variable list` ↔ دستور ناشناخته. **نام هیچ credential خصوصی قابل enumeration نیست** |
| Release `apk-latest` (۲۰۲۶‑۱۰‑۲۵) | ۸ فایل `stock-*-{debug,release}-11e617d4…apk` با SHA و اندازههای کاملاً متفاوت (۱۳–۱۱۰ مگابایت). **Mimo 9.35 نیست** |
| Google Drive (پوشهٔ mimo) | سه_part آرشیو `Mimo_9.35 (1).z01` (۵۲٬۴۲۸٬۸۰۰ B)، `.z02` (همان)، `.zip` (۳۱٬۰۶۹٬۳۶۸ B) = ۱۳۵٬۹۲۶٬۹۶۸ B. مجوزها: **فقط owner** (`danmillman008@gmail.com`)، بدون لینک عمومی |
| sandbox محلی | پروندهٔ `Mimo_9.35 (1).apk` با SHA تأییدشده موجود است، ولی sandbox اجازهٔ خروجی به مقصد runner را ندارد و ** commit کردن APK در مخزن عمومی ممنوع است** |

نتیجه: **هیچ URL قابلدسترس و مجاز برای runner وجود ندارد.** آرشیوهای Drive خصوصیاند و باز کردن
دسترسی عمومی آنها یک تغییر امنیتی بر روی دارایی متعلق به کاربر است که بدون اذن صریح انجام نشد؛
همچنین URLهای کوتاهمدت pre-authorized در ورودیهای `workflow_dispatch` یک مخزن عمومی قابلرؤیتاند و
عملاً معادل افشای credential محسوب میشوند.

## ۳. محافظتهای رعایتشده

- APK اصلی به مخزن عمومی **commit نشد** و در `RUNNER_TEMP` خارج از مخزن نگهداری میشود.
- هیچ credential، توکن نشست یا دادهٔ خصوصی بارگذاری نشد؛ لاگها با فیلتر ایمیل/توکن پاکسازی شدند.
- **APK جایگزینی از روی DEX ساخته نشد**؛ در صورت عدم تطابق SHA، ورکفلو نصب را رد میکند
  (`APK_SHA256.txt` → «SHA MISMATCH -> refusing install»).
- هیچ دورزدن احراز هویت، پاسخ سرور جعلی، حساب غیرمجاز، خرید/پرداخت، روت، استخراج DB خصوصی،
  یا دورزدن TLS/pinning انجام نشد.

## ۴. دقیقاً چه چیزی این انسداد را برطرف میکند

یکی از این دو، هنگام اجرای دستی ورکفلو:

1. تأمین **یک URL منفرد و قابلدسترس برای runner** به همان فایل ۱۴۲٬۳۵۳٬۴۹۹ بایتی با SHA بالا
   (مثلاً artifact خصوصی / storage امضاشده)، از طریق ورودی `apk_url`؛ یا
2. اذن صریح برای باز کردن موقت دسترسی لینک به سه_part Drive و بازچینش آنها در runner
   (همراه با بررسی SHA پس از استخراج).

ورکفلو از قبل برای حالت (۱) کامل است: دانلود → `sha256sum` → تطابق → `adb install -r` →
`pm path` → `dumpsys package` → `resolve-activity` → `am start` → اسکرینشات / UI / logcat.
تا پیش از تأمین منبع، `TEST-001` و همهٔ تستهای وابسته `BLOCKED` باقی میمانند و
**هیچ ادعای «نصب تأییدشده» مطرح نمیشود**.
