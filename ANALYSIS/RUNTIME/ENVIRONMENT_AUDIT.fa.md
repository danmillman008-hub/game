# مأموریت ۰۳ — حسابرسی محیط اجرا (ENVIRONMENT AUDIT)

**وضعیت کلی:** `RUNTIME VERIFIED` برای حقایق مربوط به runner، SDK، شبکه و شبیهساز.
**برچسبها:** فقط `OBSERVED` / `STATICALLY INFERRED` / `RUNTIME VERIFIED` / `SERVER CONFIRMED` / `UNKNOWN`.
**تاریخ:** ۲۰۲۶‑۱۱‑۰۵ (UTC ۰۱:۵۵–۰۱:۵۸) · **شاخه:** `arena/aebb90b7-game`
**SHA مورد انتظار APK اصلی:** `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`

## ۰. شناسهٔ اجراها

| Run ID | نتیجه | علت / دستاورد |
|---|---|---|
| `41949014303` | FAIL | `script:` چندخطی؛ خطا `/usr/bin/sh failed with exit code 1` |
| `41949615333` | FAIL | همان علت؛ تشخیص AVD اضافه شد و سالم بودن نصب اثبات شد |
| `41950152436` | SUCCESS | شبیهساز API 36 بوت شد؛ اسکرینشات یکنواخت خاکستری (خالی) |
| `41950695024` | SUCCESS | بیدار/آنلاک؛ اسکرینشات واقعی لانچر، ولی `uiautomator` هنوز شکست خورد |
| `41951780483` | SUCCESS **(مرجع نهایی)** | اسکرینشات کامل لانچر + سلسلهٔ UI (۱۶ گره) + شش معیار در `TEST_RESULTS.json` |

پروندهها: `ENVIRONMENT_AUDIT.txt`، `ENVIRONMENT_HOST.json`، `AVD_SETUP_DIAGNOSTIC.txt`، `RUN_INFO.txt`،
`DEVICE_PROPERTIES.txt` / `.json`، `LOGS/DISPLAY_STATE.txt`.

## ۱. پیشنیازهای runner — `RUNTIME VERIFIED`

| مورد | مقدار اندازهگیری‌شده | منبع |
|---|---|---|
| سیستمعامل | Ubuntu **26.04.1 LTS** (Resolute) | `ENVIRONMENT_AUDIT.txt` |
| هسته | `7.0.0-1019-azure` x86_64 | همان |
| CPU | Intel Xeon Platinum 8370C @ 2.80GHz، پرچم `vmx` | همان |
| تعداد هسته | `nproc=4` | همان |
| حافظه | 15 GiB کل / ~14 GiB آزاد | همان |
| دیسک | 145 GiB کل / **88 GiB آزاد** | همان |
| مجازیسازی | `/dev/kvm` موجود، `crw-rw---- root:kvm` | همان |
| udev KVM | قانون `99-kvm4all.rules` اعمال شد | گام Enable KVM |
| Java | OpenJDK Temurin **25.0.5** | همان |
| SDK | `/usr/local/lib/android/sdk`، `sdkmanager` + `avdmanager` موجود | همان |
| ADB | `1.0.41` / `37.0.1-15733141` | همان |
| دسترسی شبکه | `https://dl.google.com/` → HTTP 302؛ `repository2-3.xml` → **HTTP 200** | همان |

> **تصحیح فرضیه (M02):** گواهیهای `EV-M02-0001` و `EV-M02-0002` دربارهٔ «نبود ADB/SDK/KVM و غیرقابلدسترس بودن dl.google.com»
> **مختص sandbox محلی** بودند و همچنان برای آن محیط صادقاند. در runner واقعی GitHub Actions هر چهار مورد
> **نقض شد**: ADB/SDK/KVM موجود و `dl.google.com` پاسخگو است. `EV-M02-0005` («هیچ AVD/ورکفلو وجود ندارد») نیز
> اکنون برای مأموریت ۰۳ **منسوخ** است. این تمایز دامنه باید حفظ شود.

## ۲. تصویر سیستم و پروفایل — `RUNTIME VERIFIED`

- `system-images;android-36;google_apis;x86_64` موجود (rev 7)؛ دانلود و نصب شد: `x86_64-36_r07.zip`، `sdkmanager_install_exit=0`.
- `android-36;google_apis;arm64-v8a` **نیز موجود است**. این یافته، هشدار README اکشن (`arm64-v8a` محدود به سطوح API کمتر، مثلاً 30)
  را برای این مخزن تصاویر **نقض میکند**؛ با این حال تصویر arm64 روی میزبان x86 اجرا نشد.
- تصاویر API 35 بهصورت **جداگانه** فهرست شدند و هیچکدام بهعنوان API 36 برچسب نخوردند.
- پروفایل `pixel_7` = `id: 40` موجود؛ `avdmanager create avd ... --device pixel_7` با `exit=0` موفق بود (`AVD_SETUP_DIAGNOSTIC.txt`).
- `ldd emulator` هیچ کتابخانهٔ گمشده report نکرد (خروجی `grep not found` = 1 یعنی بدون تطابق)؛
  `libtinfo.so.6` و `libncurses.so.6` موجوداند. مانع رایج قدیمی `libncurses.so.5` رخ نداد.
- `target=google_apis` انتخاب شد؛ `google_apis_playstore` **استفاده نشد**. دلیل: روی دستگاه واقعی
  `pm path com.google.android.gms` → `/product/priv-app/PrebuiltGmsCore/PrebuiltGmsCore.apk`،
  یعنی GMS حاضر است. این **اثبات نمیکند** که برنامهٔ Play Store / Play Integrity / Billing حاضر است؛
  بنابراین نیاز به تصویر playstore همچنان `UNKNOWN` است مگر با اجرای APK بررسی شود.

## ۳. کشف مهم: رفتار اکشن پینشده — `OBSERVED`

`src/script-parser.ts` در commit پینشده، ورودی `script:` را **خطبهخط** جدا میکند و هر خط را در
یک فرآیند جداگانهٔ `sh -c` اجرا میکند (`main.ts` → `exec.exec('sh', ['-c', script])`). بنابراین:

- متغیرها، `heredoc`ها و بلوکهای چندخطی بین خطوط **باقی نمیمانند**؛
- دو اجرای اول دقیقاً به همین دلیل شکست خوردند: خط سوم `mkdir -p "$R/..."` با `$R` خالی،
  `mkdir -p /SCREENSHOTS` را اجرا کرد و با `exit 1` شکست؛
- خطا ربطی به KVM، تصویر سیستم، AVD یا `disable-animations` **نداشت**.

**راهحل:** کل آزمون به پروندهٔ `ANALYSIS/RUNTIME/runtime_smoke.sh` منتقل شد و ورودی اکشن به
یک خط واحد تبدیل شد: `script: bash ANALYSIS/RUNTIME/runtime_smoke.sh`. پس از آن اجرا موفق شد.

## ۴. انحراف از مشخصات تریگر — `OBSERVED` (افشا شده)

درخواست مأموریت «فقط `workflow_dispatch`» بود. `gh workflow run mimo-runtime-verification.yml` با
`HTTP 404` رد شد: GitHub تنها ورکفلوهای موجود در **شاخهٔ پیشفرض** را برای `workflow_dispatch` ثبت میکند،
در حالی که این نشست به `arena/aebb90b7-game` محدود است و اجازهٔ push به `main` ندارد.
برای اجرای واقعی، یک تریگر `push` **فقط با مسیر** `ANALYSIS/RUNTIME/_DISPATCH_TRIGGER` و **فقط** روی
همان شاخه افزوده شد؛ بنابراین workflow روی pushهای معمولی اجرا **نمیشود** و همچنان دستی است.
`workflow_dispatch` با همان ورودیها حفظ و قابلاستفاده است (مثلاً پس از ادغام به شاخهٔ پیشفرض).

## ۵. مشخصات دستگاه واقعی — `RUNTIME VERIFIED`

| ویژگی | مقدار |
|---|---|
| `ro.build.version.sdk` | **36** (درخواستی 36 ⇒ تطابق) |
| `ro.build.version.release` | **16** |
| `ro.product.model` | `sdk_gphone64_x86_64` |
| `adb devices` | `emulator-5554 device ... emu64xa` |
| `ro.product.cpu.abilist` | `x86_64,arm64-v8a` |
| `ro.dalvik.vm.native.bridge` | `libndk_translation.so` |
| `ro.product.cpu.abilist32` | **خالی** |
| `wm size` | `1080x2400` (پیکسل اندازهگیری‌شده) |
| `wm density` | `420` |
| `sys.boot_completed` | `1` |
| `mWakefulness` | `Awake` |
| لانچر | `com.google.android.apps.nexuslauncher/.NexusLauncherActivity` |
| مقیاس انیمیشن | `window_animation_scale=1.0`، `transition_animation_scale=1.0` |
| پرچمهای اکشن | `-no-window -gpu swiftshader_indirect -noaudio -no-boot-anim -no-snapshot`، `disable-animations: false`، `emulator-boot-timeout=900` |

### تصحیح فرضیهٔ ABI (بسیار مهم)
نگرانی ایستای مأموریت ۰۳ این بود که APK فقط کتابخانههای `arm64-v8a` / `armeabi-v7a` دارد و روی
`x86_64` اجرا نخواهد شد. روی دستگاه واقعی: **ترجمهٔ ۶۴بیتی ARM فعال است**
(`abilist` شامل `arm64-v8a` و `native_bridge=libndk_translation.so`)، ولی `abilist32` خالی است،
پس مسیر ۳۲بیتی `armeabi-v7a` در دسترس نیست. نتیجه:
`STATICALLY INFERRED` → «مسیر `arm64-v8a` محتملاً قابل بارگذاری است؛ مسیر `armeabi-v7a` نه».
هیچکدام `RUNTIME VERIFIED` نیست، زیرا **APK نصب نشد**. تصویر `arm64-v8a` API 36 نیز بوت نشد تا
این فرضیه مستقیماً آزمون شود؛ بنابراین ناسازگاری ABI همچنان `UNKNOWN` باقی میماند.

## ۶. محدودیتها و تصحیح ابزاری

- در اجراهای پیشین (`41950152436` و اجرای تشخیصی بعدی)، `uiautomator dump` با
  `ERROR: null root node returned by UiTestAutomationBridge` شکست خورد،
  `/sdcard/window.xml` ساخته نشد و `adb pull` با `exit=1` رد شد.
- در **اجرای مرجع نهایی `41951780483`** همان فرمان موفق شد
  (`LOGS/uiautomator_000.txt`): `UI hierchary dumped to: /sdcard/window.xml`،
  `uiautomator_exit=0`، `1 file pulled ... (6661 bytes)`، `uiautomator_pull_exit=0`.
  اکنون `UI_HIERARCHY/TEST-000_emulator_home.xml` موجود است: **۱۶ گره**،
  همگی از بستهٔ `com.google.android.apps.nexuslauncher`،
  متنهای `Thu, Nov 5` / `Gmail` / `Photos` / `YouTube` / `Phone` / `Messages` / `Chrome`،
  و `bounds` ریشه `[0,0][1080,2400]` ⇒ `RUNTIME VERIFIED` برای **UI لانچر سیستم**.
- این سلسلهٔ UI **فقط لانچر سیستم** است. محدودیت «عدم نمایش مؤلفههای Compose توسط
  UIAutomator» آزمون **نشد**، چون هیچ صفحهای Compose و هیچ برنامهای از Mimo اجرا نشد؛
  آن محدودیت `UNKNOWN` است. شکستهای موقت سطح سیستم نباید بهحساب Compose گذاشته شوند.
- اجرای `41950152436` پیش از بیدار کردن دستگاه، فریمبافر **کاملاً خالی** (۱۵٬۵۸۴ بایت) داد؛
  پس از `keyevent 26/82/3` و انتظار، تصویر واقعی لانچر (۱٬۳۷۰٬۵۶۱ بایت،
  شاخص تنوع بایت ۱۲۵ مقدار متمایز / نسبت فشردهسازی ۰٫۱۳۳۷) ثبت شد.
  `LOGS/SCREENSHOT_ENTROPY.txt` فقط یک **شاخص تقریبی** است، نه اثبات محتوای UI.

## ۷. دامنهٔ تغییرات

فقط `.github/workflows/mimo-runtime-verification.yml` و `ANALYSIS/RUNTIME/` تغییر کردند.
هیچ ابزار RE جدید، JEB، JADX جدید، تغییری در `mimo-ui/UPGRADE`، `v12.5-fa`، ZIP/MANIFEST،
`verify_upgrade.py`، طراحیهای v12 در Drive، APK/DEX/منابع اصلی یا `EVIDENCE_INDEX.json` انجام نشد.
`budtmo/docker-android` بهکار نرفت، چون اکشن اصلی موفق شد.
