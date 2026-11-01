# ۰۱ — معماری کد ایستا (Static code architecture)

**وضعیت شواهد:** VERIFIED_STATIC برای ساختار؛ **بدون decompilation** (JDK/JADX در دسترس نبود).
هر ادعای «رفتار متد» در این سند یا INFERRED است یا ذکر نشده.

## ۱. اعداد پایه (اندازه‌گیری‌شده)

| سنجه | مقدار | منبع |
|---|---|---|
| کل کلاس‌ها | ۲۹,۴۵۴ | `CLASS_INDEX.json.gz` |
| کلاس‌های برنامه (`com.getmimo.*`) | ۳,۱۳۳ | همان |
| کلاس‌های مبهم‌شده (نام یک/دو حرفی) | ۱۴,۶۰۸ | `OBFUSCATION_MAP.csv.gz` |
| یال‌های گراف فراخوانی (سطح کلاس) | ۱۹۹,۸۲۳ | `CALL_GRAPH/edges.csv.gz` |
| یال‌های app→app | ۶,۱۰۸ | `STATIC_SUMMARY.json` |
| annotation نمونه‌ها | ۲۹,۷۴۳ (۳۶ نوع متمایز) | `annotations.json.gz` |
| نقطه‌های پایانی دارای annotation | ۶۲ | `10_BACKEND_API/API_ENDPOINTS.json` |

## ۲. توزیع نقش‌ها (طبقه‌بندی خودکار با شاهد)

| نقش | تعداد | شاهد |
|---|---|---|
| `Unknown` (کلاس‌های نام‌دار بدون قاعدهٔ اختصاصی) | ۱۴,۲۵۲ | — |
| `ObfuscatedUnresolved` | ۱۴,۵۰۴ | بدون شاهد معنایی |
| `Analytics` | ۴۷۹ | بستهٔ `analytics` |
| `AiTutor` | ۸۲ | بستهٔ `aitutor` |
| `LessonParser` | ۴۳ | بستهٔ `lessonparser` |
| `Dao` | ۳۳ | رشتهٔ SQL در بایت‌کد |
| `WhenMappings` | ۳۰ | جدول `$WhenMappings` کاتلین |
| `Serializer` | ۱۶ | `$$serializer` |
| `ApiSurface` | ۱۵ | رشتهٔ `/v1/…` |

> هشدار متدولوژیک: نقش‌ها **استنباط** از نام بسته/رشته/ارث‌بری هستند، نه خواندن کد.
> ستون `confidence` در `OBFUSCATION_MAP.csv.gz` همین را منعکس می‌کند (۱۴٬۶۰۸ ردیف، همه LOW/MEDIUM).

## ۳. نقشهٔ مبهم‌سازی (روش)

برای کلاس‌های تک‌حرفی از این شواهد استفاده شد:
ارث‌بری/اینترفیس‌ها، امضای متدها و پارامترها، رشته‌های ثابت، نوع فیلدها، annotation‌ها،
و مقصد/مبدأ یال‌های گراف فراخوانی. نمونه‌های پرارزش که با همین روش شناسایی شدند:

| شناسه | نقش پیشنهادی | شاهد اصلی | اطمینان |
|---|---|---|---|
| `Lie0/f;`, `Lie0/o;`, `Lie0/n;`, `Lie0/b;`, `Lie0/p;` | annotation‌های HTTP (GET/POST/PUT/DELETE/PATCH) | ۶۲ مسیر API به‌عنوان مقدار annotation | HIGH (از طریق هم‌بستگی) |
| `Lcom/getmimo/data/source/remote/progress/LessonProgressApi;` | API پیشرفت | مسیر `/v1/tutorials/{tutorialId}/progress` | HIGH |
| `Ldh/a;` | API ذخیرهٔ فایل درس | `…/savefiles` و `…/savedFiles` | HIGH |
| `Lhg/c;` | API اجرای کد | `/v1/code/runfiles`, `…/runFiles` | HIGH |
| `Lio/customer/...` | Customer.io inbox/Gist | مسیرهای `/api/v1/...` | HIGH (نام بسته) |

## ۴. گراف فراخوانی — یافته‌های ساختاری

پرجفت‌ترین یال‌های درون‌برنامه‌ای (`STATIC_SUMMARY.json`):
`ChapterActivity → ChapterViewModel` (۳۲)، `ChapterViewModel → ChapterViewModel` (۳۰)،
`ObserveUserLeaderboardResult → Leaderboard` (۳۶)، `GetPathMapState → Tutorial` (۲۵).
یعنی هستهٔ UI روی `ChapterActivity/ChapterViewModel` متمرکز است و مدل‌های دامنه
(`Tutorial`, `Leaderboard`, `CodeLanguage`) از use-case ها تغذیه می‌شوند — همان الگوی
MVI + interactor که در بلوپرینت قبلی گفته شد، اما این‌بار با شاهد گراف.

## ۵. محدودیت قطعی

* بدون decompiler، **هیچ ادعایی دربارهٔ منطق درون‌متدی** (شرط‌ها، فرمول‌ها، ترتیب) مطرح نشده است.
* `libsigner.so` و `libyrf.so` تحلیل نمادین نشدند (بدون ابزار ELF) ⇒ **UNKNOWN**.
* `com.segment` (۱۳۷ کلاس) و `org.ocpsoft` (۹۲) و `org.joda` (۷۲) برای اولین بار در این
  فاز شمارش شدند؛ نقش Segment (روتر تحلیلی) **استنباط** از نام است.
