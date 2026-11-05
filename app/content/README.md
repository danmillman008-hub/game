# فرم اطلاعاتی میمو (`app/content/`)

> 🧭 **مرجع فعلی (۲۰۲۶-۱۱-۰۵):** بستهٔ محتوای فعلی
> [`STRUCTURED_PACKAGE.json`](STRUCTURED_PACKAGE.json) است (ساختاریافته ولی
> `unreviewed`)؛ تشریح مدل ← [`../docs/MIMO_CONTENT_MODEL.md`](../docs/MIMO_CONTENT_MODEL.md)،
> وضعیت کلی ← [`../../README.md`](../../README.md) و
> [`../../docs/04_CURRENT_STATE.md`](../../docs/04_CURRENT_STATE.md).
> جدول و ابزارهای پایین مربوط به فاز فرم/OCRاند و همچنان معتبرند.

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
| `STRUCTURED_PACKAGE.json` | ★ بستهٔ فعلی: ۱ مسیر / ۴ بخش / ۲۰ درسنامه / ۲۰ فصل / ۱۲۰ ریزدرس / ۱۶۰ بلوک / ۲۰ پرسش؛ `structured` و `unreviewed`؛ ساختهشده توسط `tools/emit_structured_package.py` |
| `STARTER_PACKAGE.json` | بستهٔ آغازین قابلاستفاده: ۲۰ سؤال/پاسخ/توضیح **موجود** در پروتوتایپ، فرمسازگار و `placeholder`؛ توسط `tools/emit_starter_package.py` ساخته میشود |
| `source/` | خروجی خام OCR — **در `.gitignore` است، وارد گیت نمیشود** |

ترتیب کار: `OCR` → `ساختاردهی` → `پر کردن فرم` → `اعتبارسنجی` → `اتصال به اپ`.

ابزارها: `tools/analyze_mimo_lessons.py`، `tools/ocr_book.py`،
`tools/structure_book.py` (روش قدیمی)، `tools/emit_templates.py`، `tools/validate_content.py`،
`tools/emit_structured_package.py`، `tools/process_book.py`، `tools/build_output.py`.


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
آن میشوند. بستهٔ `STRUCTURED_PACKAGE.json` نیز فقط همان جملههای عینی پروتوتایپ
را در سلسلهمراتب اندازهگیریشدهٔ میمو چیده است؛ **درسنامهٔ کتاب هنوز بازبینی
نشده و وارد اپ نشده است**. داخل اپ: «استودیو یادگیری محلی ← وارد کردن بستهٔ محتوا».
