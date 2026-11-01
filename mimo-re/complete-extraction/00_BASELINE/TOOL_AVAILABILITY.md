# دسترسی ابزارها (Tool availability) — اندازه‌گیری‌شده

| ابزار | موجود؟ | نسخه/مسیر | یادداشت |
|---|---|---|---|
| `java` (jdk4py JRE) | ✅ | `/tmp/jdk/jdk4py/java-runtime/bin/java` | فقط JRE؛ `javac` همراه نیست |
| `javac` | ❌ | — | مانع ساخت ابزار جاوا |
| JADX | ❌ | — | دارایی GitHub Releases مسدود |
| dex2jar / baksmali | ❌ | — | در PyPI نیست |
| apktool / aapt2 / bundletool | ❌ | — | — |
| androguard | ✅ | 4.1.4 در `/tmp/venv` | AXML + ARSC + DEX |
| پارسر DEX داخلی | ✅ | `tools/extract_annotations.py` | برای annotation‌ها و مقادیر رمزگذاری‌شده |
| Graphviz `dot` | ❌ | — | دیاگرام‌ها منبع متنی |
| Mermaid CLI | ❌ | — | — |
| pytest | ✅ | در `/tmp/venv` | برای بخش ۱۶ |
| adb / emulator | ❌ | — | بدون تست زمان‌اجرا |
| `file`, `7z` | ❌ | — | شناسایی نوع فایل با پایتون |

## جایگزین‌های به‌کاررفته

| نیاز | جایگزین | محدودیت باقی‌مانده |
|---|---|---|
| decompile به جاوا | فهرست کلاس/متد + call graph + رشته‌ها + annotation | منطق درون‌متدی قابل خواندن نیست |
| تحلیل منابع | androguard ARSC/AXML + پارس XML داخلی | مقادیر config-محور (night/density) با برچسب قطعی نیست |
| تست زمان‌اجرا | هیچ | همهٔ سناریوها `NOT_TESTED` |
| اجرای کد درس | هیچ | قرارداد سرور از روی DTO بازسازی شده، نه از اجرا |
