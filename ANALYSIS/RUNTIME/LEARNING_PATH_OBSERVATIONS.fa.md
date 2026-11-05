# مأموریت ۰۳ — مشاهدات Learning Path

**نتیجه:** `UNKNOWN` — **هیچ مشاهدهای از Learning Path برنامه Mimo انجام نشد.**
**Test ID:** `TEST-004`، `TEST-005`، `TEST-006` · **Run:** `41951780483` · **تاریخ UTC:** ۲۰۲۶‑۱۱‑۰۵T01:58
**API/پروفایل/APK SHA:** 36 / Android 16 / `pixel_7` / `google_apis` / `x86_64` / SHA مورد انتظار `48ce1740…7c7a`
**اسکرینشات:** فقط `SCREENSHOTS/TEST-000_emulator_home.png` (لانچر سیستم؛ **هیچ گرهای از Mimo در آن نیست**)
**لاگ:** `LOGS/DISPLAY_STATE.txt`، `CRASH_AND_ERROR_LOGS.txt` · **اطمینان:** `UNKNOWN`

## ۱. چرا هیچ مشاهدهای وجود ندارد

APK نصب نشد ⇒ برنامهای اجرا نشد ⇒ به صفحهای از Learning Path نرسیدیم.
هیچ `screencap`، `uiautomator dump`، `dumpsys activity` یا logcat مربوط به
`PathMapFragment` / composableهای مسیر وجود ندارد. هیچ تعاملی (انتخاب گره، اسکرول، لمس) انجام نشد.

## ۲. تفکیک پیکسل اندازهگیری‌شده از dp استنتاجی

| کمیت | مقدار | برچسب |
|---|---|---|
| ابعاد فیزیکی صفحهٔ دستگاه | `1080x2400` px | `RUNTIME VERIFIED` (دستگاه) |
| چگالی | `420` dpi | `RUNTIME VERIFIED` (دستگاه) |
| تبدیل نظری `px = dp × (420/160) = dp × 2.625` | فرمول مقیاس پلتفرم | `STATICALLY INFERRED` |
| مختصات X/Y گرهها، فواصل، شعاع، انحنا، ضخامت خط | — | `UNKNOWN` |

`UI_HIERARCHY/TEST-000_emulator_home.xml` نیز `bounds` **اندازهگیری‌شدهٔ واقعی**
برای لانچر سیستم دارد (مثلاً آیکون Gmail در `[314,1491][519,1764]`، ریشه `[0,0][1080,2400]`).
اینها پیکسلهای **لانچر**اند، نه مؤلفههای Mimo، و نباید بهعنوان هندسهٔ مسیر یادگیری تفسیر شوند.
این اعداد **هیچ اطلاعی** دربارهٔ هندسهٔ Learning Path نمیدهند. هیچ پیکسلی از UI برنامه
اندازهگیری نشد؛ بنابراین **ادعای pixel-perfect یا حتی تقریبی مطرح نمیشود**.

## ۳. مقایسه با شواهد ایستا (بدون تأیید اجرا)

| منبع ایستا | محتوا | وضعیت اجرا |
|---|---|---|
| `PATH_GEOMETRY_CONSTANTS.json` | ۱۴۶ ثابت در ۱۱ کلاس؛ `4.0/6.0/12.0/3.0 → Lu3/c;->i0(F)F`، `20.0/10.0 → Lf0/a2;->p(...)`، `180.0/270.0/90.0 → Lxn/d;-><init>(...)`، `0.8 → Le2/v;->b(JF)J` | `OBSERVED` در بایتکد؛ نقش معنایی `STATICALLY INFERRED`؛ **هیچکدام `RUNTIME VERIFIED` نیست** |
| `LEARNING_PATH_GEOMETRY.fa.md` (M02) | ۳۱ فیلد، آفست دقیق، xref=0 | بدون تغییر؛ `UNKNOWN` برای معنا |
| `COMPLETE_COMPONENT_GRAPH.json` | حلقهٔ وضعیت گرهها: `isCompleted/isRequired/getType` روی v753 | `OBSERVED` بایتکد؛ رفتار بصری `UNKNOWN` |
| shipped `tracks.json` v753 | ۱۹ track / ۱۴۴ section / ۲۰۰۲ ارجاع tutorial / ۱٬۰۲۹ tutorial | `OBSERVED` در منابع؛ چینش بصری `UNKNOWN` |
| Ghidra run3 | `GetPathMapState$invoke$2 @0x509a8f34`، `$invoke$3 @0x509a90c8`، `GetPathMapDialogs$invoke$2 @0x509a8900`، `PathMapFragment$onCreate$1 @0x50aa5178` | `OBSERVED` دیساسمbly؛ اجرا `UNKNOWN` |
| `EV-M02-0014`، `EV-M02-0015`، `EV-M02-0016` | ترتیب خواندن وضعیت، ۱۴۶ لیترال، و UNKNOWN بودن dp/X/Y/منحنی/اسکرول/انیمیشن | **بدون تغییر** |

## ۴. وضعیت ابزاری ثبتشده

در اجراهای پیشین `uiautomator dump` با `null root node` شکست خورده بود؛
در **اجرای مرجع نهایی** موفق شد و `UI_HIERARCHY/TEST-000_emulator_home.xml`
(۱۶ گره، ۶٬۶۶۱ بایت) تولید کرد. ولی تمام گرهها متعلق به
`com.google.android.apps.nexuslauncher`اند و **هیچ گره، مؤلفه یا مختصاتی از Learning Path
Mimo در آن وجود ندارد**. بنابراین وجود XML، خلأ هندسی این پرونده را پر نمیکند.
محدودیت «عدم نمایش مؤلفههای Compose توسط UIAutomator» همچنان **آزمون نشده** است،
چون هیچ صفحهای Compose اجرا نشد؛ آن مورد `UNKNOWN` میماند و شکست موقت سطح سیستم
نباید بهحساب Compose گذاشته شود.

## ۵. فهرست دقیق موارد `UNKNOWN`

موقعیت و شکل گرهها (شش حالت بصری)، فاصلهٔ عمودی/افقی، منحنیها و کنترلپوینتها،
مرزبندی sectionها، رنگ/اندازهٔ حالت locked / available / completed،
نحوهٔ انتخاب گره، اسکرول و بازیابی موقعیت، انیمیشنها،
تطابق عینی با تصاویر طراحی v12 Drive، و هرگونه مقایسهٔ پیکسلی.
هیچکدام اندازهگیری یا مشاهده نشدهاند.
