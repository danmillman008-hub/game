# درک ساختار محتوای میمو ۹٫۳۵ — تشخیص اشکال و بازسازی لایهٔ محتوا

> این سند پاسخ به ایراد «ساختار درسنامه و درس و سؤالات را متوجه نشدی» است.
> منبع همهٔ اعداد، داراییهای دیکدشدهٔ خود APK و اسناد M05/M07/M08/M09 در
> همین ریپو است؛ هیچ رفتار سروری ادعا نشده (`SERVER CONFIRMED=0`).

---

## ۱) اشکال دقیقاً کجا بود

| لایه | قبل از این بیلد | حقیقت میمو |
|---|---|---|
| متن «درس» | `app/assets/phone.html` → صفحهٔ lesson، پاراگراف «گاهی لازم است متنها را با شکستن خطوط، خواناتر کنیم…». **این یک نمونهدمو برای تست چیدمان خط است، نه درسنامه.** من همان را بهعنوان متن درس نشان میدادم | درسنامه یک `tutorial-*.json` جداگانه است با `interactiveContent` (DSL) |
| سلسلهمراتب | یک ID درس ← ۴ گام ثابت (slide/choice/gap/reveal) ساختگی | `track → sections[] → tutorialIds[] → tutorial{chapters[]} → chapter{type} → lessons[] → blocks[]` |
| سؤال | `learningPath.questionFor(id)` یک سؤال تصادفی از بانک ۲۰تایی با هش ID درس؛ یعنی سؤال ربطی به درس نداشت | هر ریزدرس بلوک تعاملی خودش را دارد؛ `<selection>` با `correct="true"` روی هر `<item>` |
| پاسخنامه | فقط «پاسخ درست گزینهٔ ۲» + همان توضیح کوتاه | `visible-if` سهحالته، بلوکهای CORRECT/WRONG بعد از Run، پاسخ تشریحی، بررسی سایر گزینهها |
| پیشرفت | `learningPath.complete()` و دفتر توکنها | ردیف ۱۱فیلدی `LessonProgress` با `tries/attempts/inQueue/publishSetVersion=753` و `isSolvedCorrectly ≡ tries>=1` |
| منبع کتاب | `structure_book.py` روی `GetTSVText()` دوتستونی → ۵۶۵ کاندیدای قاطی، `correctIndex:null`، وصلنشده به اپ | پاسخنامهٔ انتهای کتاب («گزینهٔ ۳» + «بررسی سایر گزینهها») و word boxes |

نتیجه: همانطور که گفتید، خروجی «یه نمونهٔ خام فرانگشتانی» بود. حق با شماست؛
من ناوبری و پوسته را درست کردم ولی **لایهٔ محتوا را دستنخورده رها کرده بودم**،
و ریشهٔ همان ایراد در خود پروتوتایپ `v12.5-fa` هم هست (صفحهٔ lesson آن یک
دموی typography است).

---

## ۲) ساختار واقعی (اندازهگیری، نه حدس)

### ۲٫۱ شمای دارایی — `VERIFIED_ASSET`، ۱۰٬۲۹۸ فایل معتبر
منبع: `ANALYSIS/MISSION_09/COMPLETE_LESSON_ENGINE_SPEC.md`،
`app/content/PEDAGOGY.md`، `ANALYSIS/MISSION_05/SAMPLES/`

```json
{ "tutorial": {
    "id": 904, "version": 1, "type": "course", "codeLanguage": "html",
    "title": "Discovering HTML and Tags",
    "descriptionContent": "…", "shortDescriptionContent": "…",
    "showInTrack": true, "iconBanner": "…",
    "chapters": [{
      "id": 17742, "title": "HTML Tags", "type": "practiceLevel1",
      "lessons": [{
        "title": "Intro", "id": 151410, "contentType": "interactive",
        "images": [], "interactiveContent": "<!DOCTYPE html><html><body>…",
        "hardModeSelected": false
      }]
    }]
} }
```

`contentType` = `interactive` (۱۴٬۲۴۸) یا `executableFiles` (۴٬۰۲۴).
`executableContent` شامل `instructions / files[{name,codeLanguage,content,
solvedContent}] / hints / hasVisualOutput`.

**اعداد کامل نسخهٔ ۷۵۳:** ۱۰ زبان، ۱۹ مسیر، ۱۴۴ بخش، ۱٬۰۲۹ درسنامه،
۱٬۹۴۷ فصل، ۱۸٬۲۷۲ ریزدرس، ۳۷٬۱۸۳ جایگذاری، میانگین **۲۱٫۲ کلمه** در هر
ریزدرس. یعنی میمو «درس طولانی» ندارد: واحد یادگیری یک مفهومِ کوتاه است و عمق
از **توالی و تکرار** میآید.

### ۲٫۲ DSL و پارسر — `Lte/c.b(String)` @14378108
`interactiveContent` رشتهٔ HTML/XMLمانند است، نه JSON:

| تگ | ماژول |
|---|---|
| `<p>` | `Lte/d.a` Paragraph |
| `<code version="2" codelang="html" name="index.html">` | Code (با `<content><text value=…/>`) |
| `<selection iscode="false" multiple="multiple">` + `<item correct="true">` | Selection |
| `<img visible-if="always">` | Image |
| `<webview content="…escaped HTML…">` | Webview |
| `<interaction type="fillTheGap">`, `validatedInput` | Interaction |
| `<database>`, `<output>` | Database / Output |
| `html/body/ناشناخته` | **حذف** میشوند |

`gm.h.a(List)` → ۹ خانواده: `InteractiveWebView, FillTheGap, Spell,
Selection, ValidatedInput, SingleChoice, MultipleChoice, Reveal, None`.
توزیع جایگذاریها: `fillTheGap ۱۳٬۴۹۶`، `MultipleChoice ۹٬۸۳۷`،
`executableFiles ۷٬۸۵۹`، `validatedInput ۳٬۸۴۷`، `InteractiveWebView ۱٬۴۴۲`،
`noninteractiveSlide ۱٬۰۷۹`. DSL خراب → لیست خالی → اسلاید.

### ۲٫۳ ولیدیتورها (A6–A11، عیناً از DEX)
```
fillTheGap : selected.size == correctTokens.size && ترتیب/حروف یکسان (case-sensitive)
selection  : list.all { it.selected == it.isCorrect }
spell      : همان، بدون فاصله در join
validatedInput : lowercase + نگهداری فقط حروف/ارقام و KEEP = < > ( ) : { } , .
                normalize(user) != normalize(expected) → wrong
                user == expected → exact / else → partial (delay 300ms)
executable : userFiles.content == shipped solvedContent (ترتیب مهم)
isSolvedCorrectly() : tries >= 1   ← «تلاش» پاداش میگیرد، نه فقط پاسخ درست
```
`V()` (درست) و `X()` (غلط) هر دو ردیف پیشرفت میسازند؛ `Y(Z)` قفل دوباراجرا
دارد؛ `RunButton$State` هشت حالت `RUN_ENABLED…NOT_SHOWN`.

### ۲٫۴ پداگوژی (`app/content/PEDAGOGY.md`)
`chapter.type` سختی را **در ساختار** کدگذاری میکند:
`practiceLevel1 (۸۱۰) → practiceLevel2 (۱۷۴) → practiceLevel3 (۵۲۲)`،
`challengeLevel0 (۴۵) → 1 (۱۴) → 2 (۳۸۲)`.
نسبت «انجام» به «توضیح» ≈ **۴٫۵ : ۱** (۵٬۰۴۸ دستور انجام در برابر ۱٬۱۰۹ تعریف).
چرخه: `HOOK → DO → CHECK → FEEDBACK → REPEAT → CHALLENGE → RECOVERY`.

### ۲٫۵ سؤال و پاسخنامه
صورت سؤال → ۴ گزینه (`AnswerButtonGrid`) → نوار تعامل → باتمشیت بازخورد.
«پاسخبرگ» (گزینههای زدهشده) ≠ «پاسخنامه» (جواب تشریحی/بررسی سایر گزینهها).
کتاب منبع ما هم دقیقاً همین شکل را دارد: صفحات پاسخنامه با
`N - گزینة «۳» <توضیح>` و `بررسی سایر گزینهها: گزینه (۱): …`.

---

## ۳) چه چیزی الان ساخته شد

### الف) بستهٔ محتوای ساختاریافته — `app/content/STRUCTURED_PACKAGE.json`
تولیدشده با `app/tools/emit_structured_package.py`، **بدون اختراع هیچ جملهای**:
صورت سؤال، گزینهها، پاسخ و توضیح عیناً از `QRAW` پروتوتایپ تأییدشده گرفته
شده و فقط در سلسلهمراتب بومی میمو چیده شدهاند.

| سطح | تعداد |
|---|---:|
| tracks / sections | ۱ / ۴ (زیست، شیمی، فیزیک، ریاضی) |
| tutorials (درسنامه) | ۲۰ |
| chapters (مبحث، `practiceLevel1/2/3`) | ۲۰ |
| micro-lessons (ریزدرس) | ۱۲۰ |
| typed blocks | ۱۶۰ |
| questions (همه `correctIndex` مشخص) | ۲۰ |

هر ریزدرس شش نقش پداگوژیک را طی میکند:
`hook (صورت سؤال) → check (چهارگزینهای) → feedback (پاسخنامهٔ تشریحی +
وضعیت تکتک گزینهها) → explain (درسنامه) → practice (جای خالی) → recap`.
هر بلوک `trace.sourceRef` دارد. `validate_content.py` روی فرم اطلاعاتی PASS است.

### ب) موتور محتوا — `app/src/content-engine.js`
`parseDSL` (همان ۹ تگ، حذف ناشناختهها)، `interactionType`،
`normalizeValidatedInput`، `validateAnswer` (A6–A11)، `submit` با
`V()/X()` و ردیف ۱۱فیلدی `LessonProgress`، `advance` برای اسلایدها،
`isSolvedCorrectly = tries>=1`، و **صف غلطها** (`reviewQueue`، خروج بعد از
۲ پاسخ درست متوالی، تاریخچه هرگز پاک نمیشود).

### ج) پردازش واقعی کتاب — `app/tools/process_book.py`
جایگزین پاس تخت قدیمی. خطوط را از **word boxes** بازسازی میکند
(گروهبندی `block/par/line`، مرتبسازی راستبهچپ بر اساس `x`، سپس `y`)،
فارسی را محافظهکارانه نرمال میکند (هیچ واژهای تصحیح/تولید نمیشود)،
خطوط کمکیفیت را حذف میکند، و پاسخنامه را با **همپوشانی واژهای متن عینی**
به پرسشها وصل میکند (شمارهٔ سؤال در هر فصل تکرار میشود، پس شماره بهتنهایی
کلید نیست).

| خروجی پردازش ۸۴۸ صفحه | مقدار |
|---|---:|
| خطوط بازسازیشده | ۴۴٬۳۴۹ |
| مدخل پاسخنامه | ۷۷۵ |
| مدخل دارای «بررسی سایر گزینهها» | ۴۷۵ |
| پرسش چهارگزینهای | ۶۰۸ |
| پرسش متصل به پاسخنامه | ۶۰۰ |
| ریزدرس از نثر پراعتماد | ۳۰۰ |

خروجی `PROCESSED_DRAFT.json` در `app/content/source/` (خارج از گیت) با
`reviewStatus:unreviewed` است و **وارد اپ نشده**: OCR کتاب پر از خطاست
(مثلاً «یافته» بهجای «یاخته»)، و نمایش آن بهعنوان درسنامه همان اشتباه قبلی
بود. این ابزار مسیر جایگزینی محتوای نهایی بعد از بازبینی انسانی است.

### د) رابط کاربر
- مودال فصل حالا **فهرست ۶ ریزدرس واقعی** را با نقش و نوع رندرر نشان میدهد.
- پلیر درس ۶ صفحهٔ تایپشده دارد: نوار `X ▬▬▬ ⚑`، نقش پداگوژیک،
  درسنامه، ۴ گزینه، باتمشیت بازخورد (درست/غلط + پاسخ تشریحی + شمارهٔ تلاش
  + `tries` + وضعیت صف مرور)، پاسخنامهٔ چهارگزینهای، جای خالی، جمعبندی.
- دکمهٔ «ادامه» تا قبل از پاسخ غیرفعال است (`SUBMIT_DISABLED`).
- منبع، دشواری و وضعیت بازبینی هر سؤال زیر آن نوشته شده است.
- متن دموی چیدمان پروتوتایپ دیگر خوانده نمیشود.

---

## ۴) آنچه همچنان صادقانه ناتمام است

- **درسنامهٔ نهایی کتاب وارد نشده**: بستهٔ فعلی `contentStatus:structured`
  ولی `reviewStatus:unreviewed` و منبع آن بانک تأییدشدهٔ پروتوتایپ است،
  نه کتاب. ۲۰ پرسش، نمونهٔ کامل یک ساختار است، نه کل محتوای کنکور.
- پیشنویس book/OCR نیازمند مقایسه با تصویر صفحههاست؛ `correctIndex`های
  استخراجشده اعتبار انسانی ندارند.
- فرمولهای پاداش، رتبه، همگامسازی و رفتار زندهٔ `/v1/` هرگز مشاهده نشدند
  (`SERVER CONFIRMED=0`)؛ پل وبویو M07 صفر رویداد داشت.
- بدون LLM، بدون شبکه، بدون کلید API، بدون تولید متن؛
  `externalProvider: not-configured`.

مسیرهای دقیق: `app/content/MIMO_INFORMATION_FORM.json`،
`app/content/PEDAGOGY.md`، `ANALYSIS/MISSION_09/COMPLETE_LESSON_ENGINE_SPEC.md`،
`ANALYSIS/MISSION_09/COMPLETE_CURRICULUM_GRAPH.json`.
