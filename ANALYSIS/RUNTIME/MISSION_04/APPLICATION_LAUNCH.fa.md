# MISSION 04 — اجرای برنامه (APPLICATION LAUNCH)

| شناسه | مقدار |
|---|---|
| Workflow run ID (M04) | `41991896800` (presence-only probe) |
| مرجع دستگاه (M03) | `41951780483` — API 36 / Android 16 / `pixel_7` / `google_apis` / `x86_64` |
| Branch / commit | `arena/aebb90b7-game` / `1ca5d6bc2c761c3555d189d5160e8f8316362fed` |
| APK SHA-256 | `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` |
| Timestamp | `2026-11-05T08:06Z` |
| نتیجه | **`BLOCKED`** — هیچ Activityـای از Mimo اجرا نشد |

## ۱. فرمانهای §5 — وضعیت

| فرمان | اجرا | نتیجه |
|---|---|---|
| `adb shell cmd package resolve-activity --brief <package>` | ❌ | `BLOCKED` |
| `adb shell monkey -p <package> 1` | ❌ | `BLOCKED` |
| `adb shell am start -n <verified_activity>` | ❌ | `BLOCKED` |
| `dumpsys activity activities` / `dumpsys window` (focus) | ❌ در M04 | `UNKNOWN` |
| `pidof com.getmimo` | ❌ | `UNKNOWN` |

لانچر واقعی **کشف نشد**. کاندیداهای ایستا (`com.getmimo.ui.SplashActivity` و
`com.getmimo.ui.main.MainActivity`، هر دو exported با ۳ intent-filter) از manifestاند
و برچسبشان `STATICALLY INFERRED` است؛ بدون `resolve-activity` نمیتوان یکی را قطعی دانست.
طبق §5 «Do not guess the package name / launch the verified Activity»،
هیچ Activityـای بهصورت حدسی اجرا نشد.

## ۲. فیلدهای خواستهشده §5

| فیلد | مقدار | برچسب |
|---|---|---|
| Activity resolution output | وجود ندارد | `BLOCKED` |
| Launch command and exit status | وجود ندارد | `BLOCKED` |
| Current focused activity | M04: اندازهگیری نشد؛ M03: `NexusLauncherActivity` | `UNKNOWN` (M04) |
| Foreground process | وجود ندارد | `UNKNOWN` |
| Process PID | وجود ندارد | `UNKNOWN` |
| Boot timestamp | M03: `2026-11-05T01:57:58Z` | `RUNTIME VERIFIED` (M03، حملشده) |
| Launch timestamp | وجود ندارد | `BLOCKED` |

## ۳. هشدار §5 رعایت شد: لانچر ≠ UI برنامه

`../SCREENSHOTS/TEST-000_emulator_home.png` و
`../UI_HIERARCHY/TEST-000_emulator_home.xml` (۱۶ گره) متعلق به
**لانچر سیستم Pixel**اند. این پروندهها **بهعنوان شاهد اجرای Mimo** ارائه نمیشوند.
در `SCREENSHOTS/README.txt` و `UI_HIERARCHY/README.txt` همین تمایز ثبت شده است.
§5: «A successful launch requires evidence that the Mimo process and its actual
application Activity are running» — چنین شاهدی وجود ندارد ⇒ `BLOCKED`.

## ۴. زنجیرهٔ وابستگی

```
منبع مجاز APK  ──BLOCKED──▶  دانلود  ──BLOCKED──▶  تطابق SHA روی runner
   ──BLOCKED──▶  adb install  ──BLOCKED──▶  resolve-activity
   ──BLOCKED──▶  am start  ──BLOCKED──▶  فرآیند/Activity واقعی Mimo
```

هیچ حلقهای از این زنجیره شبیهسازی یا جایگزین نشد. **ادعای «برنامه اجرا شد» مطرح نمیشود.**

**ارجاع شواهد:** `APK_INSTALLATION.fa.md`، `APK_SOURCE_AND_AUTHORIZATION.fa.md`،
`../APPLICATION_LAUNCH.fa.md` (M03)، `../runtime_smoke.sh`.
