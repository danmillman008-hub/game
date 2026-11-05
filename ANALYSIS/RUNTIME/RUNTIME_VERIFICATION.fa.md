# مأموریت ۰۳ — بازبینی اجرای واقعی (RUNTIME VERIFICATION)

> این پرونده **بازبینی (REVIEW)** است، نه درخواست تأیید. هدف آن جدا کردن دقیق
> «آنچه روی شبیهساز واقعی دیدیم» از «آنچه از کد استنتاج کردیم» است.
> مأموریت **کامل اعلام نمیشود**.

**شاخه:** `arena/aebb90b7-game` · **Run مرجع:** `41951780483` (موفق) · **تاریخ UTC:** ۲۰۲۶‑۱۱‑۰۵T01:55–01:58
**ورکفلو:** `.github/workflows/mimo-runtime-verification.yml`
**اکشن:** `reactivecircus/android-emulator-runner@b530d96654c385303d652368551fb075bc2f0b6b` (v2.35.0)
**API/پروفایل:** 36 / Android 16 / `google_apis` / `x86_64` / `pixel_7` / headless
**APK SHA-256:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` (**فقط مقدار مورد انتظار**)

---

## بخش ۱ — WHAT WE KNOW (حقایق ایستا، پیش از این مأموریت)

`OBSERVED` / `STATICALLY INFERRED`، از `APK_COMPLETE_INVENTORY.json`، `DEX_BYTECODE_EVIDENCE.json`،
`HTTP_VERBS_RESOLVED.json`، `PATH_GEOMETRY_CONSTANTS.json`، `COMPLETE_COMPONENT_GRAPH.json`،
`EVIDENCE_INDEX.json` (۳۳۶ رکورد) و اسناد Ghidra/REA/JADX:

- بسته `com.getmimo` نسخهٔ `9.35`، ۱۲ DEX، ۲۹٬۴۵۴ class_defs، ۱۲۲٬۵۴۶ method،
  targetSdk 36، ۲۴ permission، ۶۱ activity.
- زنجیرهٔ ایستای پیشرفت درس: `isSolvedCorrectly` → `storeLessonProgress` →
  `addOrUpdateLessonProgressInQueue` → DAO → `POST /v1/tutorials/{tutorialId}/progress` →
  `getReachedGoal` / `getDailyGoalCoinReward` → نتیجهای همگامسازی پایان فصل.
- ۵۳ نقطهٔ HTTP با فعل حلشده؛ ۶ تصحیح فعل؛ ۱۴۶ ثابت هندسی؛ shipped `tracks.json` v753
  (۱۹ track / ۱۴۴ section).
- معماری لایهای **همگانی نیست** (`ui → repository_remote` ۸۹ یال عبور مستقیم).
- فرمولهای دقیق امتیاز، dp/X/Y، تابع منحنی، قانون باز شدن گره بعدی، رفتار اسکرول،
  انیمیشنها و payload/پاسخ سرور: `UNKNOWN`.

## بخش ۲ — WHAT WE INFER (استنتاجها، بدون اجرای برنامه)

- `STATICALLY INFERRED`: با توجه به `cpu_abilist=x86_64,arm64-v8a` و
  `native_bridge=libndk_translation.so`، کتابخانههای `arm64-v8a` محتملاً قابل ترجمهاند؛
  `abilist32` خالی است ⇒ مسیر ۳۲بیتی `armeabi-v7a` در دسترس نیست.
- `STATICALLY INFERRED`: حضور `PrebuiltGmsCore` نیاز به تصویر `google_apis_playstore` را
  برای GMS Core کاهش میدهد، ولی حضور Play Store / Billing / Play Integrity را اثبات نمیکند.
- `STATICALLY INFERRED`: لانچر بهاحتمال زیاد `SplashActivity` است؛ بدون `resolve-activity` قطعی نیست.

## بخش ۳ — WHAT WE VERIFIED AT RUNTIME (واقعاً روی دستگاه دیده شد)

| Test ID | زمان UTC | مشاهده | نتیجه | برچسب | ارجاع |
|---|---|---|---|---|---|
| `ENV-001` | 01:55:48 | Ubuntu 26.04.1، 4 vCPU، 15 GiB RAM، 88 GiB آزاد، `vmx`، `/dev/kvm` | موفق | `RUNTIME VERIFIED` | `ENVIRONMENT_AUDIT.txt` |
| `ENV-002` | 01:55:48 | ADB 1.0.41 / 37.0.1، SDK در `/usr/local/lib/android/sdk` | موفق | `RUNTIME VERIFIED` | همان |
| `ENV-003` | 01:55:48 | `dl.google.com` → 302، `repository2-3.xml` → 200 | موفق | `RUNTIME VERIFIED` | همان |
| `ENV-004` | 01:56:32 | `android-36;google_apis;x86_64` نصب شد؛ `pixel_7` موجود؛ AVD ساخته شد | موفق | `RUNTIME VERIFIED` | `AVD_SETUP_DIAGNOSTIC.txt` |
| `TEST-000` | 01:57:58 | `sys.boot_completed=1`، API **36** / Android **16**، مدل `sdk_gphone64_x86_64` | موفق | `RUNTIME VERIFIED` | `DEVICE_PROPERTIES.json` |
| `TEST-000` | 01:57:58 | `1080x2400` px، density `420` | موفق | `RUNTIME VERIFIED` | همان |
| `TEST-000` | 01:58:21 | `mWakefulness=Awake`، لانچر `NexusLauncherActivity` resumed | موفق | `RUNTIME VERIFIED` | `LOGS/DISPLAY_STATE.txt` |
| `TEST-000` | 01:58:21 | انیمیشنها `1.0` (`disable-animations: false`) | موفق | `RUNTIME VERIFIED` | همان |
| `TEST-000` | 01:58:21 | اسکرینشات واقعی صفحهٔ خانهٔ Android 16، ۱٬۳۷۰٬۵۶۱ بایت | موفق | `RUNTIME VERIFIED` | `SCREENSHOTS/TEST-000_emulator_home.png` |
| `TEST-000` | 01:58:21 | `uiautomator dump` موفق؛ XML با **۱۶ گره** لانچر (۶٬۶۶۱ بایت) | موفق | `RUNTIME VERIFIED` | `UI_HIERARCHY/TEST-000_emulator_home.xml` |
| `TEST-001..009` | 01:58:26 | بدون APK مجاز ⇒ **۰/۹ اجرا، ۹/۹ BLOCKED** | مسدود | `UNKNOWN` | `TEST_RESULTS.json` |

**شش معیار موفقیت (تفکیکشده، همانطور که خواسته شد):**

| # | معیار (فهرست ششگانهٔ مأموریت) | وضعیت |
|---|---|---|
| ۱ | شبیهساز بوت شد **و** وجود SDK/ADB/نسخهٔ اندروید/مشخصات دستگاه اثبات شد | ✅ `RUNTIME VERIFIED` |
| ۲ | APK نصب شد | ❌ `BLOCKED` |
| ۳ | برنامه اجرا شد / صفحهٔ واقعی بدون کراش | ❌ `BLOCKED` |
| ۴ | UI مشاهده شد | ⚠️ **فقط UI لانچر سیستم**؛ UI مربوط به Mimo = `UNKNOWN` |
| ۵ | تعامل کاربر آزمون شد | ❌ فقط `keyevent 26/82/3` برای بیدار کردن دستگاه؛ هیچ تعاملی با برنامه = `UNKNOWN` |
| ۶ | رفتار backend تأیید شد | ❌ `SERVER CONFIRMED` = **۰** |

> `TEST_RESULTS.json` دقیقاً همین شش معیار را در `six_success_criteria` دارد؛
> اثبات SDK/ADB/مشخصات دستگاه در فیلد جداگانهٔ
> `sdk_adb_android_version_device_specs_proven` و مشاهدهٔ `TEST-000` در
> `device_observation` ثبت شده است (نیمهٔ دوم معیار پذیرش شمارهٔ ۱، نه معیار هفتم).

## بخش ۴ — WHAT WE STILL DO NOT KNOW

همهٔ موارد `UNKNOWN` باقیمانده از M02 **بدون تغییر**اند: قانون unlock گره بعدی،
X/Y و dp دقیق، تابع منحنی، بازیابی اسکرول، انیمیشنها، فرمولهای Sparks/XP/Coins،
آستانههای فصل/ streak / daily goal / league، payload و پاسخ واقعی سرور، رفتار آفلاین/ retry،
ناوبری و back stack، ترتیب init برنامه/DI، شش حالت بصری گره، ترتیب احراز هویت/نشست،
deobfuscation کامل R8. به اینها اضافه میشود: نصبپذیری واقعی APK، بارگذاری `.so`ها،
لانچر قطعی، صفحهٔ اول، محدودیت Compose در UIAutomator، و نیاز واقعی به `google_apis_playstore`.

---

## پوشش با مخرج صریح

| شاخص | مخرج | صورت | درصد |
|---|---|---|---|
| TEST-001..009 اجراشده | ۹ | **۰** | ۰٪ |
| TEST-001..009 مسدود | ۹ | ۹ | ۱۰۰٪ |
| حقایق دستگاه تأییدشده در اجرا | ۱۰ ردیف `TEST-000`/`ENV` | ۱۰ | ۱۰۰٪ (فقط محیط) |
| پاسخهای `SERVER CONFIRMED` | ۵۳ نقطهٔ HTTP | **۰** | ۰٪ |
| یالهای `RUNTIME VERIFIED` | ۶٬۰۱۶ جفت / ۱۰٬۹۵۴ یال | **۰** | ۰٪ |
| هندسی قطعی | ۷ | **۰** | ۰٪ |
| فرمول قطعی امتیاز | ۸ | **۰** | ۰٪ |
| تصحیح فرضیهها در این مأموریت | ۴ فرضیهٔ محیطی | ۴ | ۱۰۰٪ (همگی مربوط به محیط، **نه** معماری برنامه) |

> تعداد پرونده یا تابع معیار اتمام نیست. **مأموریت کامل اعلام نمیشود**؛
> تنها لایهٔ «محیط اجرا» برای نخستین بار بهصورت واقعی تأیید شد.
