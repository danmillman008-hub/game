# مأموریت ۰۳ — مقایسهٔ مشاهدات با `EVIDENCE_INDEX.json`

**منبع:** `ANALYSIS/EVIDENCE_INDEX.json` — ۳۳۶ رکورد، واژگان پنجگانهٔ وضعیت،
شمارش `OBSERVED=246 / STATICALLY INFERRED=67 / UNKNOWN=23 / RUNTIME VERIFIED=0 / SERVER CONFIRMED=0`.
**توجه دامنهای:** این پرونده **فقط میخواند** و ایندکس را تغییر نمیدهد؛ مأموریت ۰۳ اجازهٔ
تغییر خارج از ورکفلو و `ANALYSIS/RUNTIME/` نداد. دلتاها در همین پرونده ثبت میشوند.
**Run:** `41950695024` · **APK SHA:** `48ce1740…7c7a` · **تاریخ UTC:** ۲۰۲۶‑۱۱‑۰۵T01:43–01:50

## ۱. نگاشت رکوردها

| ID ایندکس | گزارهٔ پیشین | وضعیت پیشین | وضعیت پس از M03 | توضیح دقیق |
|---|---|---|---|---|
| `EV-0001` | SHA اصلی APK تطابق دارد | `OBSERVED` | `OBSERVED` | بدون تغییر؛ روی runner هم بهعنوان مقدار **مورد انتظار** استفاده شد، نه فایل نصبشده |
| `EV-M02-0001` | نبود ADB/emulator/SDK/KVM | `OBSERVED` | `OBSERVED` (محلی) + `RUNTIME VERIFIED` (runner) | گزاره مختص sandbox محلی است؛ در runner نقض شد. تمایز دامنه حفظ شود |
| `EV-M02-0002` | `dl.google.com` غیرقابلدسترس | `OBSERVED` | `OBSERVED` (محلی) + نقضشده در runner | runner: HTTP 302 / 200 |
| `EV-M02-0003` | هش APK، ZIP سالم، امضای v2+v3 | `OBSERVED` | `OBSERVED` | بدون تغییر، بدون نصب |
| `EV-M02-0004` | `allowBackup=false` / non-debuggable ⇒ `run-as` ناممکن | `OBSERVED` | `OBSERVED` + `UNKNOWN` (اجرا) | روی دستگاه آزمون نشد؛ هیچ استخراج DB انجام نشد |
| `EV-M02-0005` | targetSdk 36 نیازمند Android 16؛ **هیچ AVD/ورکفلو** وجود ندارد | `OBSERVED` | بخش دوم **منسوخ** | اکنون ورکفلو و AVD API 36 وجود دارد و بوت شد |
| `EV-M02-0006..0013` | بایتکد، یالها، افعال HTTP، زنجیرهٔ پیشرفت | `OBSERVED` | `OBSERVED` | **هیچکدام** به `RUNTIME VERIFIED` ارتقا نیافت |
| `EV-M02-0014/0015` | حلقهٔ وضعیت گرهها، ۱۴۶ لیترال هندسی | `OBSERVED` | `OBSERVED` | بدون مشاهدهٔ بصری |
| `EV-M02-0016/0017/0018` | هندسی، فرمولها، قانون unlock | `UNKNOWN` | `UNKNOWN` | بدون تغییر |
| `EV-M02-0019..0027` | TEST-001..009 اجرا نشده «چون emulator/ADB تأییدشده نبود» | `UNKNOWN` | `UNKNOWN` با **علت تصحیحشده** | emulator/ADB اکنون هست؛ علت جدید = نبود منبع مجاز APK |

## ۲. رکوردهای جدید (فقط در این پرونده، نه در ایندکس)

| ID موقت | مشاهده | برچسب مجاز |
|---|---|---|
| `M03-001` | emulator API 36 / Android 16 بوت شد | `RUNTIME VERIFIED` |
| `M03-002` | ADB 37.0.1، SDK، KVM، RAM/disk/dl.google.com | `RUNTIME VERIFIED` |
| `M03-003` | 1080x2400 px @420dpi، `sys.boot_completed=1` | `RUNTIME VERIFIED` |
| `M03-004` | لانچر `NexusLauncherActivity` و اسکرینشات واقعی | `RUNTIME VERIFIED` |
| `M03-005` | `cpu_abilist=x86_64,arm64-v8a`، `libndk_translation.so`، `abilist32` خالی | `RUNTIME VERIFIED` |
| `M03-006` | GMS Core حاضر؛ انیمیشنها `1.0` | `RUNTIME VERIFIED` |
| `M03-007` | `uiautomator` شکست سطح سیستم (`null root node`) | `OBSERVED` |
| `M03-008` | NativeBridge ⇒ `arm64-v8a` محتملاً قابل بارگذاری | `STATICALLY INFERRED` |
| `M03-009` | نصب/اجرای APK، UI برنامه، تعامل، پاسخ سرور | `UNKNOWN` |
| `M03-010` | هیچ پاسخ backendـای | `SERVER CONFIRMED` = ۰ |

## ۳. شمارش نهایی برچسبها (مخرج صریح)

| برچسب | تعداد در ایندکس M02 | افزودهٔ M03 (مستند، نه ویرایش ایندکس) |
|---|---|---|
| `OBSERVED` | ۲۴۶ / ۳۳۶ | +۱ (`M03-007`) |
| `STATICALLY INFERRED` | ۶۷ / ۳۳۶ | +۱ (`M03-008`) |
| `UNKNOWN` | ۲۳ / ۳۳۶ | +۱ (`M03-009`)؛ ۹ تست همچنان ۰/۹ |
| `RUNTIME VERIFIED` | **۰ / ۳۳۶** | +۶ (`M03-001..006`) — همگی **حقایق محیط/دستگاه** |
| `SERVER CONFIRMED` | **۰ / ۳۳۶** | **۰** |

> حیاتی: شش `RUNTIME VERIFIED` جدید **همگی مربوط به runner و شبیهساز**اند،
> نه به معماری، هندسه، امتیازدهی یا API برنامه. بنابراین تعداد
> `RUNTIME VERIFIED` مربوط به **رفتار Mimo** همچنان **۰** است.
> اسکرینشات لانچر سیستم هیچ گواهی بر backend یا برنامه Mimo نیست.
