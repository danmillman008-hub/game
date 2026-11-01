# ۰۰ — فهرست پایهٔ فورنزیک (Baseline inventory)

**کلاس شواهد:** VERIFIED_STATIC · **اطمینان:** HIGH
همهٔ اعداد این سند با ابزارهای موجود در `tools/` بازتولیدپذیرند. APK اصلی هرگز تغییر داده نشده است.

## ۱. موجودیت‌های ورودی

| موجودیت | حجم | SHA-256 | نقش |
|---|---|---|---|
| `Mimo_9.35 (1).z01` | 52,428,800 B | `1e3a4115…93b18` | بخش ۱ آرشیو چندبخشی |
| `Mimo_9.35 (1).z02` | 52,428,800 B | `1ac22ab2…4f539` | بخش ۲ |
| `Mimo_9.35 (1).zip` | 31,069,368 B | `91c67086…2b7` | بخش ۳ |
| `Mimo_9.35 (1).apk` (بازسازی‌شده) | 142,353,499 B | `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` | بستهٔ نهایی |

هش APK در این مرحله دوباره محاسبه شد و **با تحلیل قبلی یکسان است** ⇒ شواهد پیشین معتبر می‌مانند.
جزئیات در `APK_HASHES.json`.

## ۲. هویت بسته (اندازه‌گیری‌شده با androguard)

| ویژگی | مقدار | شواهد |
|---|---|---|
| Package | `com.getmimo` | `APK_FACTS.json` |
| Version name / code | `9.35` / `1792759685` | همان |
| minSdk / targetSdk / effectiveTarget | `28` / `36` / `36` | همان |
| Launcher (main activity) | **`com.getmimo.ui.SplashActivity_default`** | `APK_FACTS.json → main_activity` |
| Signing | v1 **و** v2 **و** v3 همه فعال | همان |
| گواهی | خودامضا، `CN=youarefinished`، O=Google، C=US، ۲۰۲۱-۱۱-۲۰ → ۲۰۴۶-۱۱-۱۴ | `certificate_details` |
| DEX | ۱۲ فایل (`classes.dex` … `classes12.dex`) | `APK_CONTENT_TREE.json` |
| Native | ۶ کتابخانه × ۲ ABI (`arm64-v8a`, `armeabi-v7a`) | همان |
| Assets | ۱۰,۵۶۴ فایل؛ `.json` = ۱۰,۳۲۷ | همان |
| کل ورودی‌های ZIP | ۱۴,۳۹۸ | همان |

**یافتهٔ تازه (نسبت به بلوپرینت قبلی):** اکتیویتی راه‌انداز یک **`activity-alias`** است
(`SplashActivity_default`). این همان مکانیزمی است که با `ChangeAppIconActivity` و
`settings_app_icon_*` جفت می‌شود: تغییر آیکون برنامه با فعال/غیرفعال‌کردن alias انجام می‌شود،
نه با تغییر drawable.

## ۳. کتابخانه‌های Native (پیش‌تر گزارش نشده بود)

| کتابخانه | مالک | نقش (استنباط) | کلاس |
|---|---|---|---|
| `librive-android.so` | Rive | رندر انیمیشن زنجیره/پایان فصل | VERIFIED_STATIC (نام) |
| `libsigner.so` | نامشخص | امضای درخواست/بسته؟ | **UNKNOWN** |
| `libyrf.so` | نامشخص | نام اختصاصی؛ بدون نماد قابل خواندن در فهرست | **UNKNOWN** |
| `libdatastore_shared_counter.so` | AndroidX DataStore | شمارندهٔ مشترک چندفرایندی (کاربران/جلسه) | VERIFIED_STATIC |
| `libandroidx.graphics.path.so` | AndroidX | مسیرهای گرافیکی (Compose/Rive) | VERIFIED_STATIC |
| `libc++_shared.so` | NDK | وابستگی استاندارد | VERIFIED_STATIC |

هیچ JNI سفارشیِ منطق آموزشی مشاهده نشد؛ منطق درس در DEX است.

## ۴. مجوزها (۲۴ مجوز درخواستی)

```
INTERNET, ACCESS_NETWORK_STATE, WAKE_LOCK, VIBRATE, RECEIVE_BOOT_COMPLETED,
POST_NOTIFICATIONS, com.google.android.c2dm.permission.RECEIVE, com.getmimo.permission.C2D_MESSAGE,
com.android.vending.BILLING, com.google.android.finsky.permission.BIND_GET_INSTALL_REFERRER_SERVICE,
ACCESS_ADSERVICES_AD_ID / _ATTRIBUTION / _CUSTOM_AUDIENCE / _TOPICS, com.google.android.gms.permission.AD_ID,
CAMERA, RECORD_AUDIO, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE,
USE_BIOMETRIC, USE_FINGERPRINT, FOREGROUND_SERVICE,
com.google.android.providers.gsf.permission.READ_GSERVICES, com.getmimo.DYNAMIC_RECEIVER_NOT_EXPORTED_PERMISSION
```
مجوزهای حساس: `CAMERA` + `RECORD_AUDIO` (احتمالاً برای تمرین‌های وب/پروژه و رکورد صدا در
پروژه‌ها؛ **UNKNOWN** بدون اجرا)، `WRITE_EXTERNAL_STORAGE` (ذخیرهٔ گواهی/تصویر)، `USE_BIOMETRIC`
(قفل بیومتریک پروفایل)، خانوادهٔ `AD_ID`/`ACCESS_ADSERVICES_*` (Adjust/Google Ads).

## ۵. کامپوننت‌های Manifest (خلاصه؛ فهرست کامل در `01_STATIC_CODE/ANDROID_COMPONENTS.md`)

| نوع | تعداد |
|---|---|
| Activity | ۶۱ (۳۶ از خود برنامه) |
| Service | ۱۹ |
| Receiver | ۲۰ |
| Provider | ۸ |
| Activity-alias | ≥۱ (`SplashActivity_default`) |

## ۶. آنچه در این فاز تغییر نکرد

هیچ‌یک از اسناد قبلی (`mimo-re/final/00…21`, `MIMO-REPORT.md`, `SENARIO_MIMO.md`,
`ARCHITECTURE_MIMO.md`) حذف یا بازنویسی نشد. فضای کاری جدید در
`mimo-re/complete-extraction/` ساخته شد و فقط به داده‌های استخراج‌شده ارجاع می‌دهد.
