# MISSION 04 — نصب APK اصلی (APK INSTALLATION)

| شناسه | مقدار |
|---|---|
| Workflow run ID | **`41998643355`** |
| Branch / commit | `arena/aebb90b7-game` / `92e87fe8d061ea4c11089f40a7c8ce73d34d816a` |
| Timestamp | `2026-11-05T09:01:45Z` |
| پیکربندی شبیهساز | API 36 / Android 16 / `pixel_7` / `google_apis` / `x86_64` / headless |
| نتیجه | `adb install -r` → **Success**، `install_exit=0` |

## ۱. دستگاه و فرمانها — `OBSERVED`

```
$ adb devices -l
List of devices attached
emulator-5554   device product:sdk_gphone64_x86_64 model:sdk_gphone64_x86_64 device:emu64xa transport_id:1

$ adb install -r MIMO_ORIGINAL.apk
Performing Streamed Install
Success
install_exit=0
```

`adb devices -l` پیش از نصب اجرا شد تا مشخص شود نصب روی همان شبیهساز تأییدشده
`emu64xa` انجام میشود، نه روی دستگاه دیگری. نصب با `install_exit=0` و پیام
صریح `Success` تأیید شد؛ هیچ `INSTALL_FAILED_*` رخ نداد.

## ۲. شناسایی بسته با `pm` (نه حدس) — `OBSERVED`

```
$ adb shell pm list packages -3
package:com.getmimo
discovered_package=com.getmimo
```
نام بسته از خروجی واقعی `pm list packages -3` استخراج شد؛
`com.getmimo` در اسکریپت **حدس زده نشد** (متغیر `PKG` از خروجی `pm` پر میشود).

```
$ adb shell pm path com.getmimo
package:/data/app/~~879Bmb_9AvdhlA2xkfvv0g==/com.getmimo-x4L2K7k-G7wsdWMh6MHe7A==/base.apk

$ adb shell dumpsys package com.getmimo | grep -E 'primaryCpuAbi|versionCode|versionName|secondaryCpuAbi'
    primaryCpuAbi=arm64-v8a
    versionCode=1792759685 minSdk=28 targetSdk=36
    versionName=9.35
```
`secondaryCpuAbi=null` و مسیر کتابخانهٔ بومی `.../lib/arm64` میباشد.
نسخهٔ نصبشده دقیقاً **Mimo 9.35 / 1792759685** است، همان که در تحلیل ایستا
شناسایی شده بود؛ بنابراین APK جایگزینی نصب نشده است.

## ۳. ABI دستگاه و کتابخانههای بومی داخل APK — `OBSERVED`

```
ro.product.cpu.abilist=x86_64,arm64-v8a
ro.product.cpu.abilist64=x86_64,arm64-v8a
ro.product.cpu.abilist32=
ro.dalvik.vm.native.bridge=libndk_translation.so
```
فهرست `lib/` داخل APK (از فایل اصلی، بدون استخراج/تغییر):
`arm64-v8a`: ۶ کتابخانه، `armeabi-v7a`: ۶ کتابخانه، **بدون x86/x86_64**.
تحلیل کاملتر در `ABI_COMPATIBILITY.fa.md`.

## ۴. تشخیص خطاهای نصب (§5، انجامشده ولی بدون وقوع خطا)

دروازهٔ نصب برای ردهبندی خودکار خطاها آماده بود و خروجی `adb install` در
`APK_INSTALLATION.txt` بهطور کامل ذخیره شد. در این اجرا هیچکدام رخ ندادند:
`INSTALL_FAILED_NO_MATCHING_ABIS`، `INSTALL_FAILED_INVALID_APK`،
`INSTALL_FAILED_UPDATE_INCOMPATIBLE`، `INSTALL_PARSE_FAILED_*`،
`INSTALL_FAILED_INSUFFICIENT_STORAGE`، `dex2oat` failure.
عدم رخداد `NO_MATCHING_ABIS` با وجود نبود `x86_64` در APK، ناشی از
`arm64-v8a` در `cpu.abilist64` و پل ترجمهٔ `libndk_translation.so` است؛
این یک `OBSERVED` از نصب موفق است، نه پیشبینی.

## ۵. حفاظت از فایل اصلی — `OBSERVED`

هیچ `apktool`, `zipalign`, `apksigner`, تغییر DEX/منیفست/منابع، وصلهٔ `.so`،
بستهبندی مجدد یا `adb install --force-*` بهکار نرفت. تنها عملیات روی فایل،
خواندن، تقسیم باینری، الحاق و `sha256sum` بود.

**ارجاع شواهد:** `APK_INSTALLATION.txt`، `ABI_COMPATIBILITY.txt`،
`APK_SHA256.txt`، `DEVICE_PROPERTIES.txt`، `DEVICE_PROPERTIES.json`.
