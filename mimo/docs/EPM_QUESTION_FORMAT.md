# گزارش قالب سؤال بومی EPM — چه چیزی واقعاً پشتیبانی می‌شود

وضعیت: `VERIFIED_STATIC` (خواندن مستقیم کد و schema در مخزن EPM، commit `14c1b276…`) و `VERIFIED_RUNTIME` برای مسیر
وارد‌سازی/آزمون (10 اِستور در `tools/e2e_exam_test.py` روی موتور در حال اجرا).

هدف: پیش از هر تغییر، مشخص شود EPM برای «آزمون چهارگزینه‌ای تک‌پاسخ» به چه تغییری نیاز دارد. نتیجه: **هیچ تغییری لازم نبود.**

## ۱. نوع سؤال — تنها یک نوع وجود دارد

```text
backend docs/schemas/esq-1.0.schema.json → $defs.question.type.enum = ["single_choice"]
```

- تنها نوع موجود `single_choice` است؛ «چندگزینه‌ای با چند پاسخ درست» وجود ندارد.
- `question.required = [questionKey, number, type, stem, score]`؛ `additionalProperties: false` (فیلد خودسرانه پذیرفته نمی‌شود).

## ۲. گزینه‌ها — موتور «چهارگزینه‌ای» را تحمیل نمی‌کند

```text
$defs.option = { key: pattern ^[A-Z]$, content: string ≤20000, contentBlocks?: [text|image|table|audio|separator] }
$defs.question.properties.options.maxItems = 26
```

- موتور **تا ۲۶ گزینه** می‌پذیرد و تعداد دقیق ۴ را الزام نمی‌کند.
- شناسهٔ گزینه، کلید حرفی (`A`…`Z`) است — پایدار و مستقل از متن گزینه. برای نمایش فارسی، همان کلیدها با «الف/ب/پ/ت»
  یا A/B/C/D نشان داده می‌شوند؛ خواستهٔ محصول `A/B/C/D` بود و حفظ شد.

## ۳. پاسخ درست — فایل جداگانه، دقیقاً یک کلید

```text
answers/<year>.json = { paperKey, answers: { <questionKey>: { correctOption: ^[A-Z]$, score?: number } } }
```

- کلید پاسخ از صورت سؤال **جدا** است؛ هر سؤال در فایل پاسخ فقط یک `correctOption` دارد.
- نبود کلید ⇒ سؤال بدون پاسخ؛ موتور آن را «بی‌پاسخ» حساب می‌کند و در آزمون همیشه نادرست است. به همین دلیل
  `validate_bank.py` نبود کلید و کلید خارج از A–D را خطا می‌داند.

## ۴. توضیح پاسخ — فیلد بومی ندارد

`schema` هیچ فیلدی برای explanation ندارد. تنها جای ممکن `question.metadata` است (شیء آزاد). قالب ما توضیح فارسی را در
`metadata.explanation` می‌نویسد (`explanation_language: "fa"`).

- `VERIFIED_STATIC`: `metadata` در schema بدون محدودیت نوع است، پس وارد‌سازی آن را رد نمی‌کند.
- `GENUINELY_UNKNOWN`: آیا رابط EPM این توضیح را نمایش می‌دهد یا نه. در کد فرانت‌اند نمایشی برای `metadata.explanation`
  پیدا نشد؛ بنابراین توضیح «حفظ می‌شود» ولی «نمایش داده می‌شود» اثبات نشده است. (جزو محدودیت‌های اعلام‌شده.)

## ۵. تصویر و ریاضی

- تصویر بومی: `imageBlock = { blockKey, type:"image", assetId, alt, caption?, required? }` و `assetId` باید در
  `assets/index.json` همان بسته ثبت شده باشد. یعنی تصویر **از طریق دارایی‌های بسته** پشتیبانی می‌شود، نه با URL دلخواه.
- ریاضی: بلوک اختصاصی ریاضی وجود ندارد؛ متن `content`/`stem` هر رشتهٔ ≤20000 نویسه‌ای است، پس فرمول‌های ساده با
  نویسه‌های ریاضی/یونیکد نوشته می‌شوند (همان کاری که بانک نمونه می‌کند). KaTeX بومی نیست.

## ۶. انواع واحد — تناقض مستند و کد

```text
docs/schemas/esq-1.0.schema.json → $defs.unit.type.enum = [cloze, reading, part_b]
backend/app/services/esq.py       → allowed = {cloze, reading, part_b, listening, word_bank, paragraph_matching}
```

اعتبارسنج **زمان اجرا** (که ورودی را واقعاً می‌پذیرد) شش نوع را قبول می‌کند و مستند JSON Schema قدیمی‌تر است.
سازندهٔ بانک، شش نوع کد را مبنا گذاشته و نام‌های ناشناخته را با خطای فارسی رد می‌کند (نوع ناشناخته ⇐ `reading` فقط در
CSVهای قدیمی که نوع را خالی گذاشته‌اند).

## ۷. دامنهٔ انتخاب سؤال در آزمون

```python
# backend/app/routers/exam.py
count: int = Field(20, ge=5, le=100)
_pick_questions(connection, profile_id, count) → random.sample(rows, min(count, len(rows)))
# rows = questions JOIN units JOIN papers WHERE papers.profile_id = :profile_id
```

- آزمون از **پروفایل بانک** انتخاب می‌شود؛ عرض `count` بین ۵ و ۱۰۰.
- مهم: هیچ پروفایل پیش‌فرض «فارسی» وجود ندارد. اگر `profile_id` داده نشود، بانک‌های چینی موجود در نصب هم وارد قرعه
  می‌شوند. پیش‌نمایش، پروفایل اختصاصی `پیش‌نمایش میمو` (id=6) را می‌سازد و آزمون همیشه با همان اجرا می‌شود.

## ۸. مسیر واقعی وارد‌سازی

```text
POST /api/question-banks/imports        multipart: file(.esq|.zip ≤100MiB), profile_id?
   → import_jobs (detected_format='esq-1.0', status='draft')
POST /api/question-banks/imports/{id}/publish
   → papers/units/questions/options در همان SQLite
```

بانک نمونه با همین مسیر وارد شد: job 1 (پروفایل ۱) و job 2 (پروفایل ۶)، هر دو `published`، جزوهٔ «بانک نمونهٔ کانکور
(نمایشی)» با ۶ سؤال. هیچ‌کدام از ۲۵ بخش رابط EPM حذف یا پنهان نشد.

## ۹. نتیجهٔ بررسی «آیا باید تنظیمات تغییر کند؟»

| نیاز محصول | پشتیبانی بومی | تغییر لازم |
|---|---|---|
| صورت سؤال | `stem` (+`stemBlocks`) | هیچ |
| دقیقاً ۴ گزینه | `options` با `maxItems 26` | در **قالب** اعمال شد، نه در موتور |
| دقیقاً ۱ پاسخ درست | `answers[…]` تک‌کلید | هیچ |
| شناسهٔ پایدار گزینه | `option.key` | هیچ |
| تصویر اختیاری | `imageBlock` + assets | هیچ (استفاده نشد) |
| توضیح اختیاری | فقط `metadata` | ذخیره در `metadata`؛ نمایش اثبات‌نشده |
| متادیتای درس/پایه/فصل | `unit.title`/`unit.type`/`metadata` | هیچ |
| برچسب A/B/C/D | کلیدهای حرفی | هیچ |

تنها تغییر واقعی در EPM: بازنویسی میزبان `registry.npmmirror.com` در `frontend/package-lock.json` (نصب وابستگی در
این محیط) و ساخت فرانت‌اند با `--base=/practice/` + `VITE_API_ROOT=/practice/api`. هیچ فایل منطق برنامه تغییر نکرد.
