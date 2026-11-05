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
| `STARTER_PACKAGE.json` | بستهٔ آغازین قابلاستفاده: ۲۰ سؤال/پاسخ/توضیح **موجود** در پروتوتایپ، فرمسازگار و `placeholder`؛ توسط `tools/emit_starter_package.py` ساخته میشود |
| `source/` | خروجی خام OCR — **در `.gitignore` است، وارد گیت نمیشود** |

ترتیب کار: `OCR` → `ساختاردهی` → `پر کردن فرم` → `اعتبارسنجی` → `اتصال به اپ`.

ابزارها: `tools/analyze_mimo_lessons.py`، `tools/ocr_book.py`،
`tools/structure_book.py`، `tools/emit_templates.py`، `tools/validate_content.py`.


### بستهٔ آغازین و فیلد `tutorials[]`

اسکیما اکنون یک ویژگی سطحبالای `tutorials[]` دارد (پیشتر فقط `$defs.tutorial`
تعریف شده بود و محل نگهداریاش وجود نداشت). `LocalContentProvider` در
`src/harness.js` همین آرایه را میخواند؛ بنابراین بستهای که وارد اپ میشود باید
هم `tracks[].sections[].tutorialIds` و هم `tutorials[]` داشته باشد.

```bash
python3 app/tools/emit_starter_package.py                 # ساخت از proto-ui.js
python3 app/tools/validate_content.py app/content/STARTER_PACKAGE.json
```

هیچ محتوای جدیدی در بستهٔ آغازین نوشته نشده است؛ منابع نهایی که رسیدند جایگزین
آن میشوند. داخل اپ: «استودیو یادگیری محلی ← وارد کردن بستهٔ محتوا».
