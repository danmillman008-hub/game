# MISSION 04 — REVIEW نهایی: انتقال، نصب و اجرای APK اصلی Mimo 9.35

> **REVIEW** (گزارش نهایی، نه درخواست تأیید). نسخهٔ BLOCKED پیشین در
> `PREVIOUS_BLOCKED_REPORTS/MISSION_04_FINAL_REVIEW.fa.md` محفوظ است.

## ۰. شناسهٔ اجرای مرجع — `OBSERVED`

| شناسه | مقدار |
|---|---|
| Workflow run ID | **`41998643355`** |
| Job ID / نتیجه / مدت | `127148044003` / **SUCCESS** / 3m31s |
| Trigger | `push` روی `ANALYSIS/RUNTIME/_DISPATCH_TRIGGER` (`M04-TRANSFER-RUN-005`) |
| Branch | `arena/aebb90b7-game` |
| Commit فراخوان | `92e87fe8d061ea4c11089f40a7c8ce73d34d816a` |
| Commit شواهد خودکار | `1ce38a96` |
| Timestamp | `2026-11-05T09:01:45Z` |
| Workflow | `.github/workflows/mimo-runtime-verification.yml` |
| شبیهساز | API 36 / Android 16 / `pixel_7` / `google_apis` / `x86_64` / headless |
| Action پینشده | `reactivecircus/android-emulator-runner@b530d96654c385303d652368551fb075bc2f0b6b` |
| `SERVER CONFIRMED` | **0** |

## ۱. هفت معیار پذیرش (§9) — مستقیماً از `TEST_RESULTS.json`

| # | معیار | وضعیت | شاهد قطعی |
|---|---|---|---|
| ۱ | APK اصلی دقیق به runner رسید | ✅ `true` | `LOGS/APK_TRANSFER.txt`، `downloaded_bytes=142353499` |
| ۲ | SHA-256 کامل تطابق دارد | ✅ `true` | `APK_SHA256.txt` → `result=SHA_MATCH_OK` |
| ۳ | APK نصب میشود | ✅ `true` | `APK_INSTALLATION.txt` → `Success`, `install_exit=0` |
| ۴ | بسته و Activity واقعی شناسایی شد | ✅ `true` | `pm list packages -3` → `com.getmimo`؛ `resolve-activity` → `com.getmimo/.ui.SplashActivity_default` |
| ۵ | Mimo اجرا میشود | ✅ `true` | `am_start_exit=0`, `pid=4266`, `topResumedActivity=...IntroSlidesActivity` |
| ۶ | UI واقعی Mimo ثبت شد | ✅ `true` | `SCREENSHOTS/TEST-004_first_usable_screen.png` + XML با ۱۵ گره `com.getmimo` |
| ۷ | لاگها و شواهد اجرا حفظ شد | ✅ `true` | `LOGS/`, `UI_HIERARCHY/`, `SCREENSHOTS/`, `DEVICE_PROPERTIES.json` |

```
"sha_match": true
"success_criteria": { 1..7: true }
"mission_complete": true
"server_confirmed": 0
```
**نتیجه: ۷/۷ معیار محقق شد. مأموریت ۰۴ در محدودهٔ تعریفشده کامل است.**
این نتیجه صرفاً بر اساس شواهد همان اجرای `41998643355` اعلام میشود؛
موفقیت workflow در اجراهای `41996366953`، `41997137033` و `41997975847`
بهتنهایی مبنای اعلام موفقیت قرار نگرفت.

## ۲. زنجیرهٔ کامل واقعیات — `OBSERVED`

```
APK اصلی (142353499 B, SHA 48ce1740...7c7a)
  → تقسیم باینری 71176749 + 71176750 (بدون تغییر محتوا)
  → آپلود موقت link-only در Google Drive
  → دانلود توسط runner + الحاق + sha256sum → SHA_MATCH_OK
  → adb devices -l (emulator-5554 / emu64xa)
  → adb install -r → Success (exit 0)
  → pm list packages -3 → com.getmimo
  → pm path → /data/app/.../com.getmimo-.../base.apk
  → dumpsys package → 9.35 / 1792759685 / primaryCpuAbi=arm64-v8a
  → cmd package resolve-activity → com.getmimo/.ui.SplashActivity_default
  → am start → exit 0, pid 4266
  → mCurrentFocus / topResumedActivity = ...IntroSlidesActivity
  → 4× nativeloader lib/arm64/*.so : ok  (libndk_translation.so)
  → uiautomator dump → 15 گره com.getmimo
  → PNG واقعی: "Change your career" / "Get started" / "I already have an account"
```

## ۳. ارزیابی روش انتقال (§2) — خلاصه

دو روش genuinely متفاوت تست شد (حداکثر سه مجاز بود):
1. **HTTP موقت احرازشده روی preview sandbox** — شکست صریح
   `HTTP/2 403: "Sandbox is secured with traffic access token. Token header
   'e2b-traffic-access-token' is missing"` (راهاندازی `41994008902` و
   `41996366953`)؛ نیازمند قابلیتی خارج از دسترس ایجنت بود ⇒ کنار گذاشته شد.
2. **قطعات باینری stageشده در Google Drive با لینک موقت** —
   چهار پرسش §2 همگی مثبت ⇒ تست شد ⇒ `SHA_MATCH_OK`.

روشهای C (artifactهای موجود) و D (سرویسهای انتقال عمومی) در بررسی انجامشده
رد شدند: ۲۶۸ artifact بدون اندازهٔ منطبق؛ sandbox تنها به شش میزبان مجاز خروجی
دارد. نیازی به سومین تلاش نبود. **هیچ اقدام کاربری لازم نشد** و مأموریت متوقف نگردید؛
هیچ URL امضاشده، توکن یا credential در لاگ/مخزن چاپ نشد.

## ۴. وضعیت امنیتی و پاکسازی — `OBSERVED`

- فایل اصلی workspace و سه_part خصوصی ازپیشموجود Drive دستنخوردهاند؛
  مالکیت/مجوز آنها تغییر نکرد.
- دو فایل موقت **جدید** ساخته شد، فقط بهصورت `anyoneWithLink / reader` و
  `allowFileDiscovery=false` بهاشتراک گذاشته شد، و **پس از اتمام اجرا**
  با `make_private` خصوصی و سپس با `trash_file` به سطل منتقل شدند.
- کپیهای محلی `/home/user/_work/split/*.bin`،
  `google_drive/M04_transfer_part1.bin` و فایل `TRANSFER_ENDPOINT.txt`
  حذف شدند. سرور موقت پورت ۸۰۰۰ متوقف شده است.
- **هیچ APKـای به مخزن commit نشد**؛ `git ls-files` فاقد فایل باینری APK است.

> **یادداشت امنیتی صادقانه**: در مراحل ابتدایی recovery، یک URL حاوی توکن
> (`/t/<token>`) در تاریخچهٔ عمومی Git قرار گرفت. سرور مربوطه متوقف شده،
> توکن در لاگها redact شده، و پروندهٔ پیکربندی حذف شده است؛ ولی **حذف توکن از
> تاریخچهٔ Git انجام نشده** و این مورد بهعنوان ریسک باقیمانده اعلام میشود،
> نه بهعنوان مشکل حلشده. اقدام دقیق لازم در صورت تمایل مالک مخزن:
> چرخش/ابطال آن توکن و پاکسازی تاریخچه (مثلاً `git filter-repo` + force-push)،
> که خارج از محدودهٔ این مأموریت و نیازمند اختیار مالک است.

## ۵. محدوده و موارد `NOT OBSERVED` / `UNKNOWN`

- اجرا در **مرز احراز هویت** متوقف شد: ورود، ثبتنام، لمس دکمهها، درخواست تأییدشده
  به سرور، پاسخهای بکاند، خرید/پرداخت، TLS/pinning bypass، حساب آزمایشی ساختگی،
  روت و استخراج DB خصوصی — **هیچکدام انجام نشد**.
- `SERVER CONFIRMED = 0`. اجرای کلاینت **هیچ نتیجهای** دربارهٔ سرور، APIها،
  نمرهدهی، هندسهٔ تمرینها یا منطق بازکردن قفل اثبات نمیکند (همچنان `UNKNOWN`).
- اطمینان از Play Store / Play Integrity / Billing در تصویر `google_apis`
  همچنان `UNKNOWN` است؛ هشدار «Google Play services out of date» ثبت شد.
- مسیر `armeabi-v7a` و تصویر بومی `arm64-v8a` آزمایش نشدند؛
  پایداری بلندمدت و صفحات پس از onboarding `NOT OBSERVED`اند.
- تحلیل ایستا، REA/Ghidra، `mimo-ui/UPGRADE`، v12.5-fa، ZIP/MANIFEST،
  `verify_upgrade.py` و شواهد M01–M03 **دستنخورده** باقی ماندند؛
  diff مسیرهای محافظتشده نسبت به نسخهٔ قبل خالی است.

## ۶. فهرست تحویلها

| پرونده | وضعیت |
|---|---|
| `TRANSFER_METHODS.fa.md` | ✅ جدید — ارزیابی A–F، چهار پرسش، شکست دقیق روش ۱ |
| `APK_TRANSFER.fa.md` | ✅ جدید — فرمانها، خروجی، پنج اجرا |
| `APK_INTEGRITY.fa.md` | ✅ بازنویسی واقعی — `SHA_MATCH_OK` |
| `APK_INSTALLATION.fa.md` | ✅ بازنویسی واقعی — `Success`, `com.getmimo` |
| `APPLICATION_LAUNCH.fa.md` | ✅ بازنویسی واقعی — `pid=4266`, `IntroSlidesActivity` |
| `ABI_COMPATIBILITY.fa.md` | ✅ بازنویسی واقعی — ترجمهٔ ARM64 موفق |
| `CRASH_AND_ERROR_ANALYSIS.fa.md` | ✅ بازنویسی واقعی — بدون crash Mimo |
| `MISSION_04_FINAL_REVIEW.fa.md` | ✅ این REVIEW |
| `INITIAL_APPLICATION_OBSERVATIONS.fa.md` | ✅ بازنویسی واقعی |
| `TEST_RESULTS.json` | ✅ تولیدشده توسط runner، ۷/۷ `true` (دستکاری نشد) |
| `DEVICE_PROPERTIES.json` / `.txt` | ✅ تولیدشده توسط runner |
| `APK_SHA256.txt`, `APK_INSTALLATION.txt`, `APPLICATION_LAUNCH.txt`, `ABI_COMPATIBILITY.txt`, `CRASH_AND_ERROR_LOGS.txt` | ✅ خام |
| `SCREENSHOTS/` (TEST-000/002/003/004) | ✅ PNG واقعی |
| `UI_HIERARCHY/TEST-003_initial_screen.xml` | ✅ XML اصلی |
| `LOGS/` | ✅ انتقال، دانلود، logcat، ANR، UI، اسکرینشات + بایگانی ۴ اجرای پیشین |
| `PREVIOUS_BLOCKED_REPORTS/` | ✅ ۱۱ گزارش BLOCKED محفوظ (حذف نشدند) |

## ۷. حکم نهایی

> **MISSION 04 — RECOVERED / COMPLETE (۷/۷).**
> APK اصلی و تغییرنیافتهٔ Mimo 9.35 با هش کامل تأییدشده به runner منتقل،
> روی همان شبیهساز تأییدشدهٔ Android 16 نصب، و بهصفحهٔ onboarding واقعی
> برنامه رسانده شد. تصویر، XML، logcat، فرآیند و Activity همگی در مخزن محفوظاند.
> مأموریت در مرز احراز هویت متوقف شد؛ `SERVER CONFIRMED` همچنان `0` است و
> هیچ ادعایی دربارهٔ بکاند mimo از اجرای کلاینت استنتاج نمیشود.

**منبع اصلی:** `TEST_RESULTS.json` (run `41998643355`)،
`.github/workflows/mimo-runtime-verification.yml`،
`ANALYSIS/RUNTIME/runtime_smoke.sh`،
`ANALYSIS/RUNTIME/MISSION_04/transfer_apk.sh`.
