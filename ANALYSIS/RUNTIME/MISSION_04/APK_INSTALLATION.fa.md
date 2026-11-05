# MISSION 04 — نصب APK (APK INSTALLATION)

| شناسه | مقدار |
|---|---|
| Workflow run ID (M04) | `41991896800` — **presence-only probe؛ هیچ شبیهساز/ADBـای اجرا نشد** |
| مرجع پیکربندی دستگاه (M03) | run `41951780483`، API 36 / Android 16 / `pixel_7` / `google_apis` / `x86_64` |
| Branch / commit | `arena/aebb90b7-game` / `1ca5d6bc2c761c3555d189d5160e8f8316362fed` |
| APK SHA-256 | `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` |
| Timestamp | `2026-11-05T08:06Z` |
| نتیجه | **`BLOCKED`** — `adb install -r` اجرا نشد |

## ۱. فرمانهای خواستهشده در §4 و وضعیت دقیق آنها

| فرمان | اجرا | خروجی |
|---|---|---|
| `adb devices -l` | ❌ در M04 اجرا نشد | (M03: `emulator-5554 device ... emu64xa`) |
| `adb install -r ORIGINAL.apk` | ❌ **اجرا نشد** | `BLOCKED` |
| `adb shell pm list packages -3` | ❌ اجرا نشد | `UNKNOWN` |
| `adb shell pm path <verified_package_name>` | ❌ اجرا نشد | `UNKNOWN` |

دلیل: طبق §13 «If APK access is blocked: Deliver a complete blocker report. Do not
waste time repeating environment setup». ازآنجاکه `APK_SOURCE_AND_AUTHORIZATION.fa.md`
نبود منبع مجاز را اثبات کرد، **هیچ بوت AVD و هیچ فرمان ADBـای تکرار نشد**.
اجرای `adb devices` بدون APK هیچ شاهد جدیدی دربارهٔ نصب تولید نمیکرد.

## ۲. نام بسته — `STATICALLY INFERRED` (نه `RUNTIME VERIFIED`)

§4: «Do not guess the package name». نام بسته **حدس زده نشد**؛ از manifest ایستای
`APK_COMPLETE_INVENTORY.json` / `EV-0001` گرفته شد: `com.getmimo`، نسخهٔ `9.35`.
اما تأیید آن روی دستگاه (`pm path` / `dumpsys package`) انجام **نشد**،
پس برچسب آن `STATICALLY INFERRED` است و **نه** `RUNTIME VERIFIED`.
هیچ `pm list packages -3`ـای برای کشف نام بستهٔ نصبشده اجرا نشد.

## ۳. فیلدهای خواستهشده §4 — همگی `UNKNOWN` / `BLOCKED`

| فیلد | مقدار | برچسب |
|---|---|---|
| Installation exit code | اجرا نشد | `BLOCKED` |
| Complete installation output | وجود ندارد | `BLOCKED` |
| Package name | `com.getmimo` (از manifest) | `STATICALLY INFERRED` |
| Version name | `9.35` (از manifest) | `STATICALLY INFERRED` |
| Version code | `1792759685` (از `APK_COMPLETE_INVENTORY.json`) | `STATICALLY INFERRED` |
| Installed APK paths | اندازهگیری نشد | `UNKNOWN` |
| APK SHA-256 (روی runner) | تطابق داده نشد | `BLOCKED` |
| Device ABI | `x86_64,arm64-v8a` (M03، run `41951780483`) | `RUNTIME VERIFIED` (M03، حملشده) |
| APK ABI list | `arm64-v8a` ۶ + `armeabi-v7a` ۶ = ۱۲ `.so` (M02) | `STATICALLY INFERRED` |
| Native library directories | بررسی نشد | `UNKNOWN` |

## ۴. کلاسهای خطای احتمالی §4 — هیچکدام رخ نداد

`ABI incompatibility`، `Missing native dependencies`، `SDK incompatibility`،
`Signature conflict`، `Insufficient storage`، `Package parsing failure`،
`Unsupported native library format`: **هیچکدام مشاهده نشد**، زیرا نصبی انجام نشد.
هیچکدام نیز **رد نشدند**؛ بنابراین همگی `UNKNOWN`اند، نه «سالم».
§4 میگوید «Use evidence, not assumptions» — بنابراین هیچ پیشبینیای دربارهٔ
موفقیت یا شکست نصب ثبت نمیشود.

## ۵. محافظتها — `OBSERVED`

- APK اصلاح، rebuild، repack، patch نشد؛ کتابخانههای بومی دستکاری نشدند.
- هیچ APK غیرمرتبطی (سه_part Drive، `stock-*` release، artifact `app-debug-apk`،
  شش APK دیگر Drive) جایگزین نشد.
- نصب فقط پس از تطابق کامل SHA مجاز است (ر.ک. `APK_INTEGRITY.fa.md`).

**ارجاع شواهد:** `LOGS/SECRET_PRESENCE_PROBE.txt`، `APK_SOURCE_AND_AUTHORIZATION.fa.md`،
`../DEVICE_PROPERTIES.json` (M03)، `ANALYSIS/APK_COMPLETE_INVENTORY.json`.
