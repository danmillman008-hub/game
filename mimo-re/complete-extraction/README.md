# استخراج کامل Mimo 9.35 — فضای کاری مشخصات قابل ساخت

> این پوشه **در کنار** نتایج مأموریت‌های قبلی ساخته شده و هیچ سند قبلی را تغییر نداده است.
> گزارش قبلی: `../MIMO-REPORT.md`، `../final/00..21`، `../SENARIO_MIMO.md`، `../ARCHITECTURE_MIMO.md`.

## از کجا شروع کنم؟

| اگر می‌خواهید… | برو به |
|---|---|
| نمای کلی و لینک همهٔ فایل‌ها | **`report.html`** |
| بدانید چه چیزی اثبات‌شده و چه چیزی نامعلوم است | `FINAL_COMPLETENESS_AUDIT.md` |
| معماری کل سیستم | `COMPLETE_SYSTEM_ARCHITECTURE.md` + `.mmd` |
| فهرست همهٔ ادعاها با شاهد | `MASTER_EVIDENCE_DATABASE.csv` (۷۳ ردیف) |
| فهرست نادانسته‌ها | `MASTER_UNKNOWN_REGISTER.csv` (۲۴ ردیف) |
| زبان درس و الگوریتم تصحیح | `05_LESSON_DSL/DSL_SPECIFICATION.md` |
| اجرای واقعی پارسر | `tools/lesson_dsl.py` + `16_AUTOMATED_TESTS/` |
| قرارداد API | `10_BACKEND_API/API_CATALOG.md` + `VERB_MAPPING.md` |
| ساخت محصول جدید | `17_BUILD_READY_SPEC/` |
| انتقال به کنکور | `18_KONKUR_TRANSFER/TRANSFER_MATRIX.md` |

## ساختار ۱۸ حوزه

```
00_BASELINE    هش/هویت/مجوز/محیط/ابزار
01_STATIC_CODE فهرست کلاس، گراف فراخوانی، نقشهٔ مبهم‌سازی، وابستگی، native، کامپوننت‌ها
02_ANDROID_RESOURCES سرشماری res/assets و فناوری UI هر خانواده
03_UI_UX      ۱۹۲ سطح، ماتریس حالت، کامپوننت، ناوبری، سیستم طراحی، (بدون اسکرین‌شات)
04_CONTENT_MODEL مدل دامنه، نسخه‌داری، دروازه‌گذاری، JSON Schema، ERD
05_LESSON_DSL ۲۷ تگ، گرامر EBNF، مرجع بلوک، سنجش، بازخورد، رندرر، اجرای کد، AST، ۴ فیکسچر
06_EXECUTION_ENGINE ماشین حالت، اجراکنندهٔ درس/کد، چک‌لیست قراردادها
07_PEDAGOGY   ساختار برنامه، گراف، سختی، مسیر، تسلط، تمرین
08_AI_TUTOR   قرارداد پرامپت/ابزار، مونتاژ زمینه، حفاظ، سهمیه، محدودیت‌ها
09_PROGRESS_GAMIFICATION پیشرفت، XP، استریک، کلید، لیدربورد
10_BACKEND_API کاتالوگ ۶۲ مسیر، نقشهٔ فعل، احراز، خطا، نرخ، گروه‌ها، ۲۶۵ stub DTO
11_DATABASE_PERSISTENCE سه جدول Room + DDL، همگام‌سازی، کش، صف، مهاجرت
12_SUBSCRIPTIONS مدل محصول، جریان پی‌وال، تخفیف، RevenueCat
13_REMOTE_CONFIG فهرست پرچم‌ها، آزمایش‌ها، قرارداد پیکربندی
14_ANALYTICS_NOTIFICATIONS ابزارها، اعلان‌ها، ۹ deep link، کاتالوگ خام
15_RUNTIME_TESTING برنامهٔ ۲۴ سناریو (NOT_TESTED) + وابستگی‌های غایب + پوشش
16_AUTOMATED_TESTS ۲۳ آزمون pytest (سبز)
17_BUILD_READY_SPEC تجزیه، مدل داده، API، بک‌لاگ، ریسک
18_KONKUR_TRANSFER ماتریس ۳۲ قابلیت، نبایدها، برنامهٔ ۳ فاز
tools/        همهٔ ابزارهای بازتولید + شمارنده‌ها + تولید گزارش
```

## بازتولید

```bash
python3 -m venv /tmp/venv && /tmp/venv/bin/pip install androguard==4.1.4 pytest
# APK در /tmp/apk/Mimo_9.35 (1).apk (خارج از مخزن)
/tmp/venv/bin/python tools/extract_annotations.py /tmp/x 01_STATIC_CODE/annotations.json
/tmp/venv/bin/python tools/build_api_catalog.py 01_STATIC_CODE/annotations.json ../data/endpoints.txt 10_BACKEND_API/API_ENDPOINTS
/tmp/venv/bin/python tools/build_static_artifacts.py /tmp/x 01_STATIC_CODE
/tmp/venv/bin/python tools/build_machine_artifacts.py "/tmp/apk/Mimo_9.35 (1).apk" .. .
/tmp/venv/bin/python tools/dsl_census.py /tmp/x/assets/lessons-en/tracks 05_LESSON_DSL
/tmp/venv/bin/python tools/lesson_dsl.py --validate-corpus /tmp/x/assets/lessons-en/tracks 05_LESSON_DSL/DSL_VALIDATION_REPORT.json
python3 tools/build_master_registers.py && python3 tools/build_report.py
cd 16_AUTOMATED_TESTS && /tmp/venv/bin/python -m pytest -q
```

## قواعد رعایت‌شده

* APK هرگز تغییر/بازبسته/توزیع نشد.
* هیچ تلاشی برای دور زدن احراز هویت/پرداخت/DRM انجام نشد.
* هیچ متن/تصویر/برند Mimo بازتولید نشد؛ فیکسچرها تألیف خودمان‌اند.
* هر ادعا: وضعیت + اطمینان + مسیر شاهد.
* هیچ آزمون زمان‌اجرا ادعا نشده است (۰ از ۲۴).
