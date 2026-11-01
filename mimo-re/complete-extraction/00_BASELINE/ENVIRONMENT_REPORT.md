# محیط تحلیل — گزارش واقعی (Environment report)

**کلاس:** VERIFIED_STATIC (مشاهدهٔ مستقیم محیط) · تاریخ اجرا: 2026-11-01

## ۱. وضعیت پایه

| مورد | مقدار |
|---|---|
| سیستم | Linux sandbox (بدون دسترسی root به مخازن بستهٔ سیستمی) |
| Python | 3.x با venv در `/tmp/venv` (androguard 4.1.4) |
| شبکهٔ خروجی | فقط `github.com`, `codeload.github.com`, `api.github.com`, `registry.npmjs.org`, `pypi.org`, `files.pythonhosted.org` |
| مخزن کاری | `/home/user/game` روی شاخهٔ `arena/ecb8af07-game` |
| APK | `/tmp/apk/Mimo_9.35 (1).apk` (خارج از مخزن، تغییرناپذیر) |

## ۲. آزمایش نصب ابزارها (نتیجهٔ واقعی، نه ادعا)

| ابزار | تلاش | نتیجه | اثر بر تحلیل |
|---|---|---|---|
| **JDK 17** | `pip download jdk4py` از PyPI | **موفق** — `jdk4py-25.0.2.1` (JRE کامل، `/tmp/jdk/jdk4py/java-runtime/bin/java`) | JVM موجود شد، اما بدون decompiler مفید نیست |
| **JADX** | `pip download jadx` | ناموفق (بسته در PyPI نیست) | — |
| **JADX (رسمی)** | `curl` از GitHub Releases (`skylot/jadx`) | **مسدود**: دارایی‌ها به `release-assets.githubusercontent.com` هدایت می‌شوند و TLS قطع می‌شود (`SSL_ERROR_SYSCALL`) | **decompilation ممکن نشد** |
| **apktool / baksmali / aapt2 / bundletool** | `command -v` + PyPI | هیچ‌کدام موجود نیست؛ معادل PyPI هم نیست | تحلیل منابع با androguard |
| **`smali` (PyPI 0.2.5)** | نصب و اجرا | شکست: بسته یک *اسمبلر* ناقص است (`smali.lib` موجود نیست) | کنار گذاشته شد |
| **androguard 4.1.4** | نصب‌شده | **کار می‌کند** (DEX/ARSC/AXML) | موتور اصلی تحلیل |
| **Graphviz `dot`, `mmdc`** | `command -v` | موجود نیست | دیاگرام‌ها فقط به‌صورت منبع Mermaid/DOT |
| **wkhtmltopdf / weasyprint** | `command -v` | موجود نیست | خروجی PDF تولید نمی‌شود |
| **emulator / adb / sdkmanager** | `command -v` | موجود نیست | **هیچ تست زمان‌اجرا انجام نشد** |
| **نوشتن پارسر DEX دست‌ساز** | کد در `tools/` | موفق؛ دو باگ مهم پیدا و رفع شد (آفست‌های هدر و `EncodedValue`) | کشف annotation‌های HTTP |

## ۳. دو کشف روش‌شناسی که مسیر را تغییر داد

1. **آفست‌های هدر DEX در پارسر اولیه اشتباه بود** (`string_ids_off` در `0x3C` است نه `0x40`).
   این خطا باعث شد پارسر قبلی `null` برگرداند و نتیجه‌گیری «هیچ annotation‌ای وجود ندارد» شود.
2. **androguard مقادیر annotion را به‌صورت `EncodedValue` برمی‌گرداند**، نه `str`. فیلتر
   `isinstance(v, str)` همهٔ مسیرهای API را حذف می‌کرد. با dereference کردن
   `EncodedValue.value` هر ۶۲ endpoint بازیابی شد (نگاه کنید به
   `10_BACKEND_API/API_CATALOG.md`).

نتیجهٔ عملی: **verification روش HTTP از UNKNOWN به VERIFIED_STATIC (با نقشهٔ annotation) ارتقا یافت**.

## ۴. آنچه در این محیط ممکن نشد

* خواندن کد جاوا/کاتلین بازتولیدشده: بدون JADX/dex2jar ممکن نیست. تنها شواهد سطح بایت‌کد
  (فهرست کلاس/متد، فراخوانی‌ها، رشته‌ها، annotation‌ها) در دسترس است.
* هر سناریوی زمان‌اجرا (بخش ۱۵ صفر درصد؛ همه `NOT_TESTED`).
* اعتبارسنجی رفتار سرور (بدون حساب و بدون مجوز دسترسی).

## ۵. تکرارپذیری

```bash
# JDK (اختیاری، برای مستندسازی محیط)
pip install --target /tmp/jdk jdk4py

# وابستگی تحلیل
python3 -m venv /tmp/venv && /tmp/venv/bin/pip install androguard==4.1.4

# بازتولید همهٔ شواهد این فضای کاری
/tmp/venv/bin/python tools/extract_annotations.py /tmp/x 01_STATIC_CODE/annotations.json
/tmp/venv/bin/python tools/build_api_catalog.py 01_STATIC_CODE/annotations.json ../data/endpoints.txt 10_BACKEND_API/API_ENDPOINTS
/tmp/venv/bin/python tools/build_static_artifacts.py /tmp/x 01_STATIC_CODE
/tmp/venv/bin/python tools/build_machine_artifacts.py "/tmp/apk/Mimo_9.35 (1).apk" .. .
```
