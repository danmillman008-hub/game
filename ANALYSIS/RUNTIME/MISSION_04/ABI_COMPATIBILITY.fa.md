# MISSION 04 — سازگاری ABI و ترجمهٔ بومی (ABI COMPATIBILITY)

| شناسه | مقدار |
|---|---|
| Workflow run ID | **`41998643355`** |
| Branch / commit | `arena/aebb90b7-game` / `92e87fe8d061ea4c11089f40a7c8ce73d34d816a` |
| Timestamp | `2026-11-05T09:01:45Z` |
| پیکربندی شبیهساز | API 36 / Android 16 / `pixel_7` / `google_apis` / `x86_64` / headless |
| نتیجه | نصب و بارگذاری `.so`ـهای `arm64-v8a` روی `x86_64` **موفق** |

## ۱. حقایق اندازهگیری شده — `OBSERVED`

| منبع | مقدار |
|---|---|
| APK (تحلیل ایستا، بدون تغییر) | `lib/arm64-v8a/` = ۶ `.so`؛ `lib/armeabi-v7a/` = ۶ `.so`؛ **هیچ `x86`/`x86_64`** |
| `pm dumpsys package com.getmimo` | `primaryCpuAbi=arm64-v8a`، `secondaryCpuAbi=null` |
| `ro.product.cpu.abilist` | `x86_64,arm64-v8a` |
| `ro.product.cpu.abilist64` | `x86_64,arm64-v8a` |
| `ro.product.cpu.abilist32` | *(خالی)* |
| `ro.dalvik.vm.native.bridge` | `libndk_translation.so` |
| `/system/lib64/libndk_translation*` | موجود (فهرست در `ABI_COMPATIBILITY.txt`) |
| device fingerprint | `google/sdk_gphone64_x86_64/emu64xa:16/BE2A.250530.026.F3/13894323:userdebug/dev-keys` |

## ۲. بارگذاری واقعی کتابخانهها در logcat — `OBSERVED`

همگی با PID `4266` (همان فرآیند Mimo) و نتیجهٔ `: ok`:

```
11-05 09:01:54.612  4266  4266 D nativeloader: Load .../lib/arm64/libyrf.so ... : ok
11-05 09:01:55.041  4266  4266 D nativeloader: Load .../lib/arm64/libdatastore_shared_counter.so ... : ok
11-05 09:01:55.723  4266  4266 D nativeloader: Load .../lib/arm64/librive-android.so ... : ok
11-05 09:01:55.828  4266  4266 D nativeloader: Load .../lib/arm64/libsigner.so ... : ok
```

هیچ `UnsatisfiedLinkError`، `dlopen failed`، `library "..." not found` مربوط به
`com.getmimo`، و هیچ `native crash` / `linker` fatal در `LOGS/LOGCAT_MIMO.txt`
یافت نشد. ردیابی `dex2oat` در `APK_INSTALLATION.txt` بدون خطا ثبت شد.

## ۳. پاسخ به پرسش §5 (ARM64 در برابر x86_64) — `OBSERVED`

پرسش مطرحشده: «آیا نبودن `x86_64` در APK منجر به شکست نصب/اجرا میشود؟»
پاسخ اندازهگیریشده **خیر، در این پیکربندی خاص**:

1. تصویر `google_apis / x86_64` API 36 هر دو ABI را در `abilist64` اعلام میکند.
2. `libndk_translation.so` بهعنوان native bridge فعال است.
3. `PackageManager` بسته را با `primaryCpuAbi=arm64-v8a` نصب کرد،
   `adb install` خروجی `Success` داد و `INSTALL_FAILED_NO_MATCHING_ABIS` رخ نداد.
4. چهار کتابخانهٔ `arm64` در زمان اجرا بار شدند و برنامه تا صفحهٔ onboarding پیش رفت.

یعنی ترجمهٔ ARM64→x86_64 برای **این نسخه و این مسیر اجرا** کافی بود.

## ۴. محدوده — `NOT OBSERVED`

- `abilist32` خالی است؛ مسیر `armeabi-v7a` / 32 بیتی **آزمایش نشد** و
  هیچ ادعایی دربارهٔ آن نمیشود.
- تصویر `arm64-v8a` API 36 هرگز بوت نشد؛ مقایسهای بین تصویر بومی ARM و ترجمه
  انجام نشد.
- تمام مسیرهای کد و all 6+6 کتابخانه اجرا نشدند؛ فقط کتابخانههایی که برنامه در
  onboarding بار کرد مشاهده شدند. صفحات بعدی، پخش محتوا، و مسیرهای بومی دیگر
  `NOT OBSERVED` باقی میمانند.
- هیچ تصویر سیستمی، `build.prop`، کتابخانه، یا APKـای برای «سازگار کردن» تغییر
  نیافت؛ این صرفاً گزارش رفتار پیکربندی موجود M03 است.

**ارجاع شواهد:** `ABI_COMPATIBILITY.txt`، `APK_INSTALLATION.txt`،
`DEVICE_PROPERTIES.txt`، `DEVICE_PROPERTIES.json`، `LOGS/LOGCAT_MIMO.txt`.
