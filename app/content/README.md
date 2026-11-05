# فرم اطلاعاتی میمو (`app/content/`)

این پوشه **مقصد تمام اطلاعات تازه** است. تا وقتی داده وارد این فرم نشده،
هیچ چیزی وارد اپلیکیشن نمیشود.

| فایل | نقش |
|---|---|
| `MIMO_INFORMATION_FORM.json` | اسکیمای رسمی (JSON Schema 2020-12) — قرارداد الزامی بستهٔ محتوا |
| `CONTENT_FORM_TEMPLATE.json` | قالب خالی قابل پر کردن (همان «فرم») |
| `MIMO_INFORMATION_FORM.md` | شرح فارسی فیلدها، قواعد و نحوهٔ پر کردن |
| `PEDAGOGY.md` | پداگوژی و روش تدریس استخراجشده از تمام درسنامههای میمو |
| `PEDAGOGY_STATS.json` | آمار اندازهگیری‌شدهٔ واقعی (خروجی `tools/analyze_mimo_lessons.py`) |
| `EXAM_TEMPLATE.json` | قالب ۷ بخش آزمون بر اساس فرم و پداگوژی |
| `PRACTICE_TEMPLATE.json` | قالب نشستهای تمرین (همان پاسخگویی آزمون، بدون تایمر) |
| `source/` | خروجی خام OCR — **در `.gitignore` است، وارد گیت نمیشود** |

ترتیب کار: `OCR` → `ساختاردهی` → `پر کردن فرم` → `اعتبارسنجی` → `اتصال به اپ`.

ابزارها: `tools/analyze_mimo_lessons.py`، `tools/ocr_book.py`،
`tools/structure_book.py`، `tools/emit_templates.py`، `tools/validate_content.py`.
