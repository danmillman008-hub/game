# فرم اطلاعاتی میمو — قرارداد ورود اطلاعات جدید

**نسخه:** ۱٫۰ · **اسکیما:** `MIMO_INFORMATION_FORM.json` (JSON Schema 2020-12)
**قالب خالی:** `CONTENT_FORM_TEMPLATE.json`
**هدف:** هرچیزی که از کتاب زیست (درسنامه، تست، پاسخنامه، تصویر، سرفصل) درمیآید،
**فقط** در قالب این فرم وارد اپلیکیشن میشود. تا وقتی بستهای از اعتبارسنجی رد نشود،
`app/src/fixtures.js` جایگزین نمیشود.

---

## ۱. فرم از کجا آمده (مبنای شواهد)

| دسته فیلد | منبع | وضعیت |
|---|---|---|
| `track/section/tutorial/chapter/lesson` و نام فیلدها | `assets/lessons-en/tracks/tracks.json` و ۱۰۲۹ فایل `tutorial-*.json`، `publishSetVersion=753` | **عینی** (دارایی دیکدشدهٔ APK) |
| `contentType`, `chapter.type`, `hardModeSelected`, `images[]`, `interactiveContent` | همان فایلها | **عینی** |
| نام رندررها (`fillTheGap`, `MultipleChoice`, `validatedInput`, `executableFiles`, `InteractiveWebView`, `noninteractiveSlide`) | `ANALYSIS/MISSION_09/COMPLETE_LESSON_ENGINE_SPEC.md` و گراف درسنامه | **مستند** |
| `isSolvedCorrectly = tries>=1`، validators | M07 stage 6 / M09 | **VERIFIED** |
| `trace`, `blocks[]`, `pedagogicalRole`, `learningObjectives`, `questions[]`, `exams[]` | **اضافهٔ ما** برای تبدیل کتاب | **DESIGN_CHOICE** — ادعایی دربارهٔ میمو نیست |

هیچ فیلدی برای احراز هویت، همگامسازی، امتیاز سروری، رتبه یا پاسخ `/v1/` تعریف
نشده؛ `SERVER CONFIRMED=0` همچنان پابرجاست.

---

## ۲. سلسلهمراتب (همانند میمو)

```
package
└── tracks[]            (مسیر / کتاب)
    └── sections[]      (فصل / سرفصل)
        └── tutorialIds[] → tutorials (درسنامه)
            └── chapters[]  (مبحث، با سطح practiceLevel*/challengeLevel*)
                └── lessons[]  (ریزدرس ≈۲۱ کلمه، یک مفهوم)
                    └── blocks[]  (اتم محتوای تایپشده)
questions[]  ← تمام تستهای book  (بانک تست + مباحث آزمون)
exams[]      ← ترکیب سؤالها در ۷ سطح مصوب پروتوتایپ
provenance   ← ردگیری: صفحه، خط، confidence OCR، وضعیت بازبینی
```

> نکته: در میمو `sections[]` فقط شناسهٔ `tutorialIds` را نگه میدارد؛ آبجکت
> `tutorial` در فایل جداگانهای است. در این فرم همان تمایز حفظ شده تا بعداً بشود
> بدون تغییر اپ، بستهٔ محتوا را به فرمت بومی میمو سریالایز کرد.

---

## ۳. فیلدهای کلیدی و قواعد پر کردن

| فیلد | الزامی | قاعده |
|---|---|---|
| `formVersion` | ✅ | دقیقاً `"1.0.0"` |
| `publishSetVersion` | ✅ | دقیقاً `753` |
| `source.kind` | ✅ | `converted-book` برای محتوای کتاب |
| `source.contentStatus` | ✅ | `placeholder → extracted → structured → reviewed → approved` |
| `trace.sourceRef` | ✅ | `book:<package>:page-<n>:block-<n>`؛ **هیچ جملهای بدون صفحهٔ مبدأ مجاز نیست** |
| `trace.ocrConfidence` | توصیه | عدد ۰–۱۰۰ از OCR؛ زیر ۶۰ حتماً `reviewStatus=unreviewed` میماند |
| `trace.reviewStatus` | ✅ | `verified` فقط بعد از بازبینی انسانی/مقایسه با تصویر صفحه |
| `lesson.title` | ✅ | کوتاه، نام همان یک مفهوم |
| `lesson.pedagogicalRole` | ✅ | یکی از `hook/explain/example/check/practice/feedback/recap/challenge` |
| `lesson.blocks[]` | ✅ | حداقل یک بلاک؛ `renderer` حتماً از فهرست مجاز |
| `block.contentFa` | ✅ | متن فارسی **بدون اختراع محتوا**؛ ترجمه/بازنویسی وفادار به صفحهٔ مبدأ |
| `question.options[]` | ✅ | ۲–۶ گزینه، `correctIndex` صفرپایه |
| `question.explanationFa` | توصیه | فقط اگر در کتاب پاسخنامه وجود داشته باشد؛ وگرنه خالی + `notes` |
| `question.topicId` | ✅ | اتصال تست به مبحث آزمون |
| `exam.kind` | ✅ | یکی از ۷ سطح پروتوتایپ نهایی (`comprehensive/timed/single/topic/monthly/analytical/review`) |
| `exam.policy` | ✅ | `unknown` وقتی سیاست پاسخنامه در کتاب مشخص نیست — **حدس زده نمیشود** |

### قواعد سختگیرانه

1. **عدم اختراع:** هیچ جمله، مثالی، توضیح یا پاسخی که در صفحهٔ مبدأ نباشد وارد
   `contentFa` / `explanationFa` نمیشود. جای خالی با `contentStatus=extracted`
   و `notes` مشخص میشود، نه با متن ساختگی.
2. **تفکیک placeholder:** بستهٔ نمونهٔ فعلی اپ (`src/fixtures.js`) همچنان
   `PLACEHOLDER` است و تا `contentStatus=reviewed` جایگزین نمیشود.
3. **کپییرایت:** خروجی خام OCR کتاب در `app/content/source/` نگهداری و در
   `.gitignore` قرار دارد؛ فقط بستهٔ ساختاریافته و ردگیری وارد گیت میشود.
4. **دوزبانه:** محتوا `fa` است؛ `interactiveContent` بومی میمو در زمان build از
   `blocks[]` ساخته میشود تا همان رندررهای پروتوتایپ استفاده شوند.
5. **آزمون/تمرین:** تستها دوبار استفاده میشوند — بهعنوان `questions[]` (بانک)
   و بهعنوان `practiceQuestionIds` داخل `chapter` (بدون محدودیت زمان) و
   `exams[].questionIds` (با تایمر). همان ساختار پاسخگویی آزمون حفظ میشود.

---

## ۴. نحوهٔ استفاده

```bash
# ۱) اندازهگیری پداگوژی (انجام شده)
python3 app/tools/analyze_mimo_lessons.py

# ۲) OCR کتاب (خروجی خارج از گیت)
python3 app/tools/ocr_book.py --pdf /home/user/_work/zist/@BankBookkonkor\ \(26\).pdf \
    --out app/content/source/biology-12 --workers 4

# ۳) پر کردن CONTENT_FORM_TEMPLATE.json ← ساختاردهی صفحات

# ۴) اعتبارسنجی بسته نهایی
python3 app/tools/validate_content.py app/content/biology-12.package.json
```

اعتبارسنجی بدون وابستگی خارجی اجرا میشود و `$ref`, `enum`, `const`,
`required`, `minItems`, `pattern`, `additionalProperties:false` را چک میکند.
