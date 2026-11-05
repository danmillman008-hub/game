# MISSION 04 — تحلیل کراش و خطا (CRASH AND ERROR ANALYSIS)

| شناسه | مقدار |
|---|---|
| Workflow run ID (M04) | `41991896800` (presence-only probe، SUCCESS) |
| مرجع دستگاه (M03) | `41951780483` — API 36 / Android 16 / `pixel_7` / `google_apis` / `x86_64` |
| Branch / commit | `arena/aebb90b7-game` / `1ca5d6bc2c761c3555d189d5160e8f8316362fed` |
| APK SHA-256 | `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` |
| Timestamp | `2026-11-05T08:06Z` |
| نتیجه | **`BLOCKED`** — هیچ فرآیند `com.getmimo`ـای وجود نداشت که کراش کند |

## ۱. تمایز بنیادین — `OBSERVED`

«نبود خطا» در لاگ **بهمعنای سالم بودن برنامه نیست**، بلکه بهمعنای
**نبود برنامهای برای تولید خطا** است. بنابراین:

| مورد §6C | وضعیت | برچسب |
|---|---|---|
| Full logcat around installation and launch | نصب/اجرا انجام نشد ⇒ logcat مربوطی وجود ندارد | `BLOCKED` |
| `AndroidRuntime` errors | مشاهده نشد (بدون فرآیند برنامه) | `UNKNOWN` |
| `FATAL EXCEPTION` entries | مشاهده نشد | `UNKNOWN` |
| linker errors | مشاهده نشد | `UNKNOWN` |
| `UnsatisfiedLinkError` | مشاهده نشد | `UNKNOWN` |
| Application process termination | وجود نداشت | `UNKNOWN` |
| Native crash records (`tombstone`) | بررسی نشد (بدون اجرا) | `UNKNOWN` |

هیچ `FATAL EXCEPTION`ـای **ساختگی**، هیچ `logcat` جعلی و هیچ شبیهسازی کراشی
تولید نشد. §6C خواستهٔ «Full logcat around installation and launch» بهدلیل نبود
آن دو رویداد قابل انجام نبود.

## ۲. تنها لاگ واقعی M04 — `OBSERVED`

`LOGS/SECRET_PRESENCE_PROBE.txt`: خروجی probe منبع (۳۷ نام، ۰ PRESENT / ۳۷ ABSENT).
این لاگ **هیچ ارتباطی با رفتار برنامه** ندارد و صرفاً شاهد انسداد منبع است.
هیچ URL، token یا credentialـی در آن درج نشده است.

`LOGS/APK_SOURCE_INVESTIGATION.txt`: فرمانها و پاسخهای دقیق بررسی منبع، شامل
`HTTP 403`ـها، فهرست artifactها و نتایج Drive. پیامهای 403 **خطای برنامه** نیستند؛
خطای **دسترسی اداری**ـاند.

## ۳. خطاهای فرآیندی M04 (مستند، بدون پنهانکاری) — `OBSERVED`

| خطا / محدودیت | پیام دقیق | تأثیر |
|---|---|---|
| Secrets enumeration | `HTTP 403: Resource not accessible by integration` | نمیتوان نام secretها را فهرست کرد |
| Variables enumeration | همان 403 | نمیتوان متغیرها را فهرست کرد |
| Secret creation | `failed to fetch public key: HTTP 403 .../actions/secrets/public-key` | نمیتوان secret ساخت |
| `workflow_dispatch` (M03) | `HTTP 404` چون ورکفلو روی شاخهٔ غیرپیشفرض ثبت نمیشود | تریگر push فقطبا مسیر استفاده شد |
| artifact/log blob host از sandbox | `EOF` / `HTTP 000` (خارج از allowlist) | لاگها فقط از طریق runner/commit قابلخواندناند |
| `parseScript()` اکشن (M03) | `The process '/usr/bin/sh' failed with exit code 1` | با script تکخطی برطرف شد؛ همچنان پابرجا |

هیچکدام از اینها خطای نصب/اجرای Mimo نیست و نباید بهحساب کراش برنامه گذاشته شود.

## ۴. خطاهایی که در M03 رخ داده و رفع شد (زمینه)

- دو اجرای نخست M03 بهدلیل تقسیم `script:` به خطوط جداگانه شکست خوردند.
- `uiautomator dump` در اجراهای میانی `null root node` داد و در اجرای نهایی
  `41951780483` موفق شد (۱۶ گره لانچر).
- فریمبافر نخست خالی بود و پس از `keyevent 26/82/3` تصویر واقعی لانچر ثبت شد.

اینها مربوط به **محیط**اند و در M04 تکرار نشدند.

## ۵. حکم

تحلیل کراش و کتابخانههای بومی §8/§12/8 «Must be based on real runtime logs».
چنین لاگهایی وجود ندارند ⇒ **`BLOCKED`**؛ هیچ نتیجهای دربارهٔ سلامت،
سازگاری ABI یا پایداری برنامه صادر نمیشود.

**ارجاع شواهد:** `LOGS/SECRET_PRESENCE_PROBE.txt`،
`LOGS/APK_SOURCE_INVESTIGATION.txt`، `../CRASH_AND_ERROR_LOGS.txt` (M03)،
`ABI_COMPATIBILITY.fa.md`.
