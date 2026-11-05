**REVIEW — وضعیت تأیید رفتار. در این جلسه هیچ رفتاری `RUNTIME VERIFIED` یا `SERVER CONFIRMED` نشده است.**
دستور مادهٔ ۸ صریح است: «When an approved emulator and ADB environment are available …».
چنین محیط تأییدشدهٔ شبیهساز/ADB و محیط تست مجاز شبکهای در اختیار نبود؛ بنابراین مادهٔ ۸ به
**مستندسازی دقیق شواهد غایب** محدود شد، نه شبیهسازی مشاهده.

---

# RUNTIME_VERIFICATION — مشاهدهشده در برابر تأییدنشده

## ۱. وضعیت محیط

| پیشنیاز | وضعیت | شاهد |
|---|---|---|
| APK اصلی (تغییرنیافته) | ✅ موجود | `sha256=48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`، ۱۴۲٬۳۵۳٬۴۹۹ بایت |
| شبیهساز/Android SDK/emulator تأییدشده | ❌ غایب | هیچ `adb`, `emulator`, `aapt2`, `apksigner` در محیط تحلیل نصب/استفاده نشد |
| ADB / دستگاه | ❌ غایب | ۰ جلسه، ۰ `adb shell` |
| محیط تست شبکهای مجاز | ❌ غایب | ۰ درخواست/پاسخ ثبتشده |
| Ghidra / REA / JADX / Smali | ✅ استاتیک | چهار اجرای سبز workflow؛ ولی **هیچکدام اجراکنندهٔ اپ نیستند** |
| تغییر APK/DEX/منابع/شواهد | ❌ انجام نشد | تمام پارسرها read-only؛ `ANALYSIS/_INPUT/` بایتبهبایت با APK یکسان است |

## ۲. جدول رفتارهای درخواستی

| # | رفتار (مادهٔ ۸) | خروجی خواستهشده | وضعیت | شاهد تولیدشده |
|---|---|---|---|---|
| ۱ | راهاندازی اپ | screenshot + logcat | `UNKNOWN / تأییدنشده` | none |
| ۲ | ناوبری بین صفحات | screenshot + UI hierarchy + transition | `UNKNOWN / تأییدنشده` | none |
| ۳ | اسکرول مسیر یادگیری | screenshot + لاگ اسکرول | `UNKNOWN / تأییدنشده` | none |
| ۴ | انتخاب گره | UI hierarchy + screenshot | `UNKNOWN / تأییدنشده` | none |
| ۵ | پیشروی در درس | screenshot + logcat | `UNKNOWN / تأییدنشده` | none |
| ۶ | اتمام چپتر | screenshot + transition | `UNKNOWN / تأییدنشده` | none |
| ۷ | نمایش پاداش و پیشرفت | screenshot + مقادیر مشاهدهشده | `UNKNOWN / تأییدنشده` | none |
| ۸ | رفتار شبکه (فقط محیط تست مجاز) | request/response | `UNKNOWN / تأییدنشده` | none |

شمارش دقیق: **۰ اسکرینشات · ۰ ADB UI hierarchy · ۰ logcat · ۰ transition ضبطشده ·
۰ state change مشاهدهشده · ۰ network capture**.
هیچ استنتاج استاتیکی بهعنوان مشاهدهٔ اجرا برچسب نخورده است.

## ۳. شواهد غایب، موردبهمورد (Explicit missing evidence)

| آنچه نیاز است | آنچه فعلاً داریم | آنچه کم است |
|---|---|---|
| مختصات واقعی گرهها (X/Y) | نام فیلدها: `offsetX`, `offsetXPx`, `columnCount`, `dotRadius` | مقادیر `dp`/px، تابع تبدیل، `density`، جهت |
| فاصلهٔ عمودی/افقی گرهها | `mainAxisSpacing`, `crossAxisArrangementSpacing`, `itemSpacing` | مقادیر عددی و اینکه کدامیک اعمال میشود |
| منحنی مسیر | `verticalEllipseRadius`, `radiusY`, `borderPath`, `libandroidx.graphics.path.so` | تابع منحنی، control pointها، رسم واقعی |
| موقعیت اسکرول / بازیابی آن | `scrollPosition`, `scrollPositionX`, `instructionsScrollOffset`, `PathMapScreenKt$...$job$1::invokeSuspend @0x50aa64b8` | مقدار اولیه، `rememberSaveable`، رفتار پس از چرخش/بازگشت |
| وضعیت بصری گرهها | ۶ نوع `type` در v753 | نگاشت type → رنگ/آیکون/قفل/انیمیشن |
| فرمول امتیاز | `isSolvedCorrectly: intField >= 1` @`0x509744bc`؛ `rewardMultiplier`, `rewardedSparksForCorrectAnswer` | ضرایب، وزن first‑try، XP/Sparks/Coins واقعی |
| شرط پایان چپتر | `SELECT COUNT(DISTINCT chapter_id)`, `is_completed`, `chapter_end_progress_eta_*` | آستانهها، ترتیب صفحهها، `variant` |
| پاداش سروری | `PostProgressResponse::getDailyGoalCoinReward`, `/v1/user/rewards/{rewardId}/confirm` | بدنهٔ پاسخ، اثر شکست، زمانبندی confirm |
| ناوبری | ۹ deep-link filter، ۳۰۰ رشتهٔ routeمانند، ۱۰ کلاس `Navigation*` | گراف `NavHost`، routeهای واقعی، back stack |
| نشست/توکن | کلاسهای `ui/authentication/*` | ذخیرهٔ امن، تازهسازی، logout |
| WorkManager/سرویسها | ۱۹ service، ۲۰ receiver، جداول `WorkSpec` | زمانبندی واقعی و اثر آنها |

## ۴. آنچه *استاتیک* مشاهده شد (برچسب درست: `OBSERVED`)

اینها **RUNTIME VERIFIED نیستند** و صرفاً بایت/رشته/دستورالعملاند:

- ۱۲ DEX، ۲۹٬۴۵۴ class_def، ۱۲۲٬۵۴۶ `code_item`، ۱٬۲۸۴٬۵۴۲ نماد Ghidra.
- بدنهٔ disassembleشدهٔ ۱۲۲ تابع هدف (`GHIDRA/CONTROL_FLOW.txt`) ازجمله
  `LessonProgress::isSolvedCorrectly @0x509744bc` و `GetPathMapState$invoke$2::invokeSuspend @0x509a8f34`.
- ۶۸ عبارت SQL، ۵۳ تعریف Retrofit، ۶۸ رشتهٔ مسیر، ۹۴٬۴۰۱ ورودی منبع، ۱۲ کتابخانهٔ `.so`.
- ۵۳۹ `DebugMetadata`، ۸۴ فیلد ماشین حالت، ۶۵۲ کلاس suspend.
- shipped v753: ۱۹ مسیر / ۱۴۴ section / ۲٬۰۰۲ tutorial / ۰ نقض پیوستگی.

## ۵. پروتکل پیشنهادی برای وقتی محیط تأیید شد (اجرا نشده است)

1. نصب APK **اصلی و دستنخورده** روی emulator، بدون تغییر باینری و بدون دستکاری دادهٔ کاربر production.
2. `adb shell uiautomator dump` + `adb logcat` + اسکرینشات در هر گام؛ ثبت هش APK قبل/بعد.
3. دنباله: launch → onboarding/skip → MainActivity → تب Learn → اسکرول مسیر → انتخاب گره →
   اجرای درس → اتمام → صفحهٔ پایان چپتر → نمایش پاداش/پیشرفت.
4. فقط در **محیط تست مجاز**، ثبت درخواست/پاسخ نقاط `/progress`, `/completion`, `/rewards/*`.
5. مقایسهٔ مقادیر مشاهدهشده با فیلدهای استاتیک (`rewardMultiplier`, `scrollPositionX`, …) و
   **ارتقای برچسب فقط پس از تطابق واقعی**.

> ممنوعیتها: تغییر production user data ❌؛ جلوه دادن استنتاج استاتیک بهعنوان مشاهدهٔ runtime ❌؛
> ادعای شبکه بدون محیط مجاز ❌. هیچکدام انجام نشده است.

## ۶. پیامد بر سایر اسناد

`LEARNING_PATH_ENGINE.fa.md` و `LESSON_AND_SCORING_ENGINE.fa.md` بنابراین
**هیچ ادعای پیکسلبهپیکسل، مقدار `dp`، ضریب امتیاز یا `SERVER CONFIRMED`** ندارند.
`COVERAGE_REPORT.fa.md` سطر `runtime_verified_behaviours = 0` و
`server_confirmed_responses = 0` را با مخرج «تعریفنشده» ثبت کرده است.
`EVIDENCE_INDEX.json` شامل ۱۱ ورودی `UNKNOWN` است که ۷ تای آنها دقیقاً رفتارهای مادهٔ ۸اند.

---

# ضمیمهٔ MISSION 02 — ممیزی محیط اجرا (انجامشده ۲۰۲۶-۱۱-۰۵)

> **این ضمیمه جایگزین محتوای بالا نیست؛ الحاق است.** نتیجهٔ ممیزی: محیط اجرا **آماده نیست**،
> بنابراین طبق مادهٔ ۱ هیچ نصب/دانلود گستردهای انجام نشد و آزمایش آغاز نشد.

## E-۱. هویت و سلامت APK (بدون تغییر)

| مورد | مقدار | وضعیت |
|---|---|---|
| SHA-256 | `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` | `OBSERVED` — با نسخهٔ تأییدشدهٔ قبلی **MATCH** |
| اندازه | ۱۴۲٬۳۵۳٬۴۹۹ بایت / ۱۴٬۳۹۸ عضو ZIP | `OBSERVED` |
| `zipfile.testzip()` | OK (همهٔ اعضا قابل خواندن) | `OBSERVED` |
| APK Signing Block | @`141062144`، اندازه ۴٬۰۸۸، شناسههای `0x7109871a` (v2) و `0xf05368c0` (v3) + verity padding | `OBSERVED` |
| `versionName` / `versionCode` | `9.35` / `1792759685` | `OBSERVED` |
| `minSdk` / `targetSdk` / `compileSdk` | ۲۸ / **۳۶** / ۳۷ | `OBSERVED` |
| مشخصات بومی | ۱۲ کتابخانهٔ `.so` در `arm64-v8a` و `armeabi-v7a` | `OBSERVED` |

**نتیجه:** APK از نظر ساختاری قابل نصب است (*installable artifact*)؛ ولی «قابل اجرا بودن» فقط روی
دستگاه/شبیهساز قابل اثبات است و **هیچ دستگاهی وجود ندارد** → `RUNTIME VERIFIED` = ۰.

## E-۲. وضعیت محیط (اندازهگیری واقعی)

| بررسی | نتیجه |
|---|---|
| `adb`, `emulator`, `sdkmanager`, `avdmanager`, `aapt`, `aapt2`, `apksigner`, `zipalign`, `fastboot`, `qemu-system-x86_64`, `java`, `javac` | **همه ABSENT** (`command -v`) |
| `ANDROID_HOME` / `ANDROID_SDK_ROOT` / `JAVA_HOME` | **هیچکدام تعریف نشده** |
| مسیرهای SDK | `/opt/android-sdk`, `/usr/lib/android-sdk`, `~/Android`, `~/.android`, `/sdk`, `TOOLS/android-sdk` → **همه غایب** |
| `/dev/kvm`، `/dev/dri`، `/dev/bus/usb` | **غایب**؛ `lsusb` هم نصب نیست |
| فرایندهای adb/emulator/qemu | **۰** |
| میزبان | Debian 12 (bookworm)، `Linux 6.1.158+ x86_64`، Xeon 2.6GHz، محیط container |
| قابلیت مجازیسازی | پرچم `vmx`/`svm` در `/proc/cpuinfo` **یافت نشد** |
| دسترسی شبکهای | `dl.google.com` → `000`، `developer.android.com` → `000` (allowlist خروجی فقط ۶ میزبان GitHub/npm/PyPI است) |
| AVD در مخزن | هیچ workflowـی شامل `avd`, `adb`, `android-emulator`, `sdkmanager`, `system-image` نیست |

### مشخصات درخواستی که قابل ثبت نیستند

| خواستهٔ مادهٔ ۱ | وضعیت |
|---|---|
| نسخهٔ Android | `UNKNOWN` — هیچ دستگاهی برای `getprop ro.build.version.release` وجود ندارد |
| ابعاد صفحه (`wm size`) | `UNKNOWN` — نیازمند `adb shell` |
| تراکم پیکسل (`wm density`) | `UNKNOWN` — نیازمند `adb shell` |
| وضعیت دستگاه (root/debuggable/battery/online) | `UNKNOWN` — نیازمند `adb devices` |

## E-۳. موانع دقیق (چه چیزی کم است)

1. **شبیهساز/AVD و system image:** نصبشده نیست. تهیهٔ آن نیازمند دانلود image اندروید ۳۶
   (`targetSdk=36`) در حد صدها مگابایت است → «دانلود گسترده»؛ طبق دستور بدون مجوز انجام نشد.
2. **KVM:** `/dev/kvm` غایب است؛ حتی با نصب ابزار، شتابسازی شبیهساز ممکن نیست.
3. **`adb` و پل USB:** غایب؛ بنابراین `uiautomator dump`, `logcat`, `screencap`, `am start` همگی ناممکناند.
4. **حساب آزمایشی مجاز:** ارائه نشده است. خرید واقعی/تغییر حساب/عملیات مخرب **انجام نشد**.
5. **محیط تست شبکهای مجاز:** وجود ندارد؛ `usesCleartextTraffic` و `networkSecurityConfig` در Manifest
   حضور دارند و خروجی شبکه محدود به ۶ میزبان است → ثبت request/response ناممکن است.
6. **`android:allowBackup=false`** و نبود `android:debuggable`: حتی با ADB،
   `adb backup` و `run-as` نمیتوانند پایگاهدادهٔ Room (`mimo.db`) را بخوانند.
   مشاهدهٔ «وضعیت محلی قبل/بعد از تکمیل درس» بدون root یا بیلد قابلدیباگ (که تغییر APK ممنوع است) ممکن نیست.
7. **وابستگی به سرویسها:** Manifest شامل Firebase/Adjust/RevenueCat/Facebook/Ads است؛
   حتی با شبیهساز، اجرای سناریو نیازمند دسترسی به سرورهای Mimo است که در allowlist نیستند.

## E-۴. شناسههای آزمایش (مادهٔ ۶)

| شناسه | آزمایش | وضعیت | خروجی تولیدشده |
|---|---|---|---|
| TEST-001 | Application Launch | **NOT EXECUTED** | none |
| TEST-002 | Learning Path Entry | **NOT EXECUTED** | none |
| TEST-003 | Node Selection | **NOT EXECUTED** | none |
| TEST-004 | Lesson Execution | **NOT EXECUTED** | none |
| TEST-005 | Lesson Completion | **NOT EXECUTED** | none |
| TEST-006 | Reward Display | **NOT EXECUTED** | none |
| TEST-007 | Progress Persistence | **NOT EXECUTED** | none |
| TEST-008 | Next Node Unlock | **NOT EXECUTED** | none |
| TEST-009 | Return After Relaunch | **NOT EXECUTED** | none |

شمارش دقیق: **۰/۹ آزمایش = ۰٪** · ۰ اسکرینشات · ۰ ADB UI hierarchy · ۰ logcat ·
۰ transition ضبطشده · ۰ تغییروضعیت مشاهدهشده · ۰ پاسخ شبکه.
هیچیک `RUNTIME VERIFIED` یا `SERVER CONFIRMED` برچسب نخوردهاند.

## E-۵. کاری که با این مانع انجام شد

بهجای توقف، **اثبات استاتیک ارتباطات** انجام شد (بدون تکرار موجودی مرحلهٔ ۱):
دیکودر کنترلجریانآگاه `Dalvik` روی ۱۲ DEX، ۱۲۲٬۵۴۶ متد / ۳٬۰۶۴٬۵۹۳ دستورالعمل /
۵۵۲٬۶۲۵ فراخوانی / ۳۹۱٬۵۵۶ دسترسی فیلد، ۶٬۰۱۶ جفتفراخوانی درون `com/getmimo`،
حل ۵۳ فعل HTTP از بایتکد Retrofit (با ۶ تصحیح)، و ۱۴۶ ثابت عددی در کامپوزابل مسیر.
جزئیات: `COMPLETE_COMPONENT_GRAPH.json`, `DEX_BYTECODE_EVIDENCE.json`,
`HTTP_VERBS_RESOLVED.json`, `PATH_GEOMETRY_CONSTANTS.json`, `COMPLETE_APPLICATION_FLOW.fa.md`.

> **هیچ استنتاج استاتیکی جایگزین مشاهدهٔ runtime نشده است.**
