# MISSION 04 — سازگاری کتابخانههای بومی ARM (ABI COMPATIBILITY)

| شناسه | مقدار |
|---|---|
| Workflow run ID (M04) | `41991896800` (بدون شبیهساز) |
| مرجع دستگاه (M03) | `41951780483` — API 36 / Android 16 / `pixel_7` / `google_apis` / `x86_64` |
| Branch / commit | `arena/aebb90b7-game` / `1ca5d6bc2c761c3555d189d5160e8f8316362fed` |
| APK SHA-256 | `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` |
| Timestamp | `2026-11-05T08:06Z` |
| برچسب کلی | `UNKNOWN` (آزمون نشد) |

## ۱. آنچه واقعاً روی دستگاه اندازهگیری شد — `RUNTIME VERIFIED` (M03، حملشده)

از `../DEVICE_PROPERTIES.json` / `../LOGS/DISPLAY_STATE.txt` (run `41951780483`):

```
ro.product.cpu.abilist      = x86_64,arm64-v8a
ro.product.cpu.abilist64    = x86_64,arm64-v8a
ro.product.cpu.abilist32    = (خالی)
ro.dalvik.vm.native.bridge  = libndk_translation.so
```

پرامپت §7 دقیقاً همین مقادیر را ذکر کرده و هشدار داده:
«This does NOT prove that the APK will run». این هشدار پذیرفته شد.

## ۲. محتوای بومی APK — `STATICALLY INFERRED` (M02، بدون تکرار تحلیل)

از `APK_COMPLETE_INVENTORY.json` / M02 (تحلیل ایستا تکرار **نشد**):

- `lib/arm64-v8a/` : ۶ فایل `.so`
- `lib/armeabi-v7a/` : ۶ فایل `.so`
- مجموع ۱۲ کتابخانه؛ **هیچ `x86` / `x86_64`ـای وجود ندارد**
- `minSdk=28`، `targetSdk=36`، GMS 20 / Firebase 64 / RevenueCat 4 / Adjust 1 نشانگر.

## ۳. پرسشهای §7 و پاسخ صادقانه

| پرسش §7 | نتیجه M04 | برچسب |
|---|---|---|
| APK native library contents | ۱۲ `.so` فقط ARM (M02) | `STATICALLY INFERRED` |
| Actual selected ABI | نصب انجام نشد ⇒ انتخاب ABI توسط `PackageManager` مشاهده نشد | `UNKNOWN` |
| Whether ARM64 translation is available | `libndk_translation.so` حاضر، `abilist` شامل `arm64-v8a` | `RUNTIME VERIFIED` (M03) |
| Whether **native libraries load successfully** | آزمون نشد | `UNKNOWN` |
| Whether app crashes during native initialization | آزمون نشد | `UNKNOWN` |
| Exact ABI failure (در صورت بروز) | هیچ خطایی مشاهده نشد، چون اجرایی نبود | `UNKNOWN` |

## ۴. استنتاج مجاز — `STATICALLY INFERRED`

وجود `libndk_translation.so` و `arm64-v8a` در `abilist` **محتمل** میسازد که
کتابخانههای ۶۴بیتی ARM ترجمه شوند؛ `abilist32` خالی است، بنابراین مسیر
`armeabi-v7a` (۳۲بیتی) در این تصویر Android 16 در دسترس نیست.
این صرفاً یک استنتاج است: §7 «Do not claim compatibility until the application has
successfully executed relevant code». چنین اجرایی رخ نداد ⇒ **هیچ ادعای سازگاری نمیشود**.

همچنین `system-images;android-36;google_apis;arm64-v8a` در `sdkmanager --list`
M03 موجود بود، ولی **بوت نشد**؛ بنابراین مسیر ARM64 بومی نیز `UNKNOWN` است.

## ۵. پیشنهاد مجاز §7 (بدون ایجاد زیرساخت جدید)

§7 اجازه میدهد «A physical ARM64 Android device or authorized remote ARM64
environment may be proposed as a separate next step». این گزینه **فقط بهعنوان
پیشنهاد جداگانه** ثبت میشود و هیچ استک جدیدی ساخته نشد:
تصویر arm64 API 36 نصب نشد، `budtmo/docker-android` بهکار نرفت،
هیچ شبیهساز دومی ایجاد نشد.

## ۶. اصلاح نکردن APK — `OBSERVED`

هیچ `.so`ـای وصله، حذف، اضافه یا جایگزین نشد؛ هیچ `lib/x86_64` ساخته نشد؛
هیچ تغییری در manifest یا امضا انجام نشد. در صورت شکست ABI در آینده،
طبق §7 فقط «مستندسازی خطای دقیق» مجاز است.

**ارجاع شواهد:** `../DEVICE_PROPERTIES.json`، `../LOGS/DISPLAY_STATE.txt`،
`../ENVIRONMENT_AUDIT.fa.md`، `ANALYSIS/APK_COMPLETE_INVENTORY.json`.
