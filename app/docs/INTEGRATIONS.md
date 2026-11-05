# اتصالهای این مرحله (گرهها · آزمونها · LearnHarness)

## ۱. گرههای آموزشی = اپ اصلی میمو

درخواست: «بخش گرهها نیاز به اصلاح دارد؛ گرههای آموزشی دقیقاً با اپ اصلی مچ شود».

**منبع حقیقت (کد، نه سلیقه):** `mimo-ui/UPGRADE/CATALOGS/MIMO_PATH_NODES.csv`
(PN-01…PN-18 ، V10-01…V10-18) و `DESIGN/NODE_CODE_GEOMETRY.json`،
همراه چک بصری `REFERENCE/mimo-01/02/10`.

| ویژگی | مقدار اپ اصلی | پیادهسازی |
|---|---|---|
| اندازه / شعاع / لبهٔ ۳بعدی | 92dp / 26dp / 8dp | `assets/node-match.css` + `NODE_SPEC` |
| آیکون | 48dp (چکِdoneـ 44dp) | همان |
| رابط | 10dp، قوس Q به شعاع 32dp، بنفشِانجامشده / یاسیِآینده | همان (`.connector path`) |
| حلقهٔ گرهٔ جاری | 60dp / کمان 8dp / 55% / برچسب `1/2` | `conic-gradient(from -90deg … 55%)` |
| حالتها | done / current-play / current-half / next(squircle، بدون قفل) / bolt-active / bolt-optional / locked | `src/nodes.js::applyOriginalNodes` |
| شبکهٔ نقطهای | نقطه 1.6dp / فاصله 26dp | همان |
| واژهنامهٔ شناور «A» | cx=340, cy=650 (حذفشده در v12.5-fa) | `.gloss-fab` بازگردانده شد |
| زمان انیمیشن checkpoint | ورود 220ms / خروج 400ms | `.just-unlocked` 220ms |

**تفاوت مهم با پروتوتایپ:** پروتوتایپ ۶ گرهٔ **ایستا** داشت؛ اپ اصلی گرهها را
از `PathMapViewModel` و پیشرفت واقعی میسازد. `src/nodes.js` همین کار را با
`progress.tutorialCompletions` انجام میدهد. برای اینکه ظاهر تأییدشده از بین
نرود، وقتی هنوز پیشرفتی ثبت نشده، `seedStates` همان ۶ حالت مصوب
(`done/done/cur-half/next/bolt-active/bolt-optional`) را نمایش میدهد.
`assertGeometry(window.NODE)` در بوت اجرا میشود و تطابق مقادیر با payload کد
را تأیید میکند (تستها چک میکنند `ok===true`).

> فایلهای محافظتشده (`DESIGN/index.html`, `proto.css`, `phone.html`) **بایتبهبایت
> دستنخورده** ماندهاند؛ لایهٔ وفاداری فقط در اپ، بعد از آنها لود میشود.

## ۲. قالب آزمونها + بررسی بخش تمرین

درخواست: «قالبی برای آزمونها بساز دقیقاً بر اساس قالب آموزشی… چون بخش تمرین
هم دارد خودت بررسی کن».

**بررسی انجام شد:** اپ هم `exam-hub` (۷ بخش مصوب)، هم `exam-run` (تایمر،
پاسخبرگ، پاسخنامه، پالت)، هم `practice-bank` و `section-practice` (گرهٔ bolt)
دارد. ساختن «آزمون دوم» برای تمرین تکرار و خطا بود. نتیجه:

- `content/EXAM_TEMPLATE.json`: ۷ بخش دقیقاً منطبق با `exam-hub`، هرکدام با
  `kind`, `minutes`, `policy`, `questionCount` و **قانون انتخاب** اعلامی
  (topicIds / ترکیب دشواری). مبتنی بر `MIMO_INFORMATION_FORM.json` و
  `PEDAGOGY.md`؛ نتیجه همان `exam-result` پروتوتایپ.
- `content/PRACTICE_TEMPLATE.json`: ۴ حالت تمرین (فصل / مبحث / بانک / غلطها)
  با **همان کامپوننتهای پاسخگویی آزمون** ولی `timed:false`، `retryAllowed:true`
  و بازخورد فوری. دقیقاً همان `scoreSession` محلی.
- `src/exam-template.js` + `tools/emit_templates.py`: انتخاب قطعی و قابلتست
  سؤالها، ساخت `buildExam()` / `buildPracticeSession()`، گزارش `shortfall`
  (کمبود سؤال پنهان نمیشود). وقتی بانک سؤال پر شود، همان توابع آزمون و تمرین
  واقعی را میسازند.
- وصلشدن: کلیک روی ردیف آزمون `exam.activeTemplate` را ذخیره میکند؛
  نشستهای تمرین `template` خود را در رکورد دارند (تست پذیرش دارد).

## ۳. LearnHarness در بخش هوش مصنوعی

درخواست: وصل کردن `github.com/amosblomqvist/learnharness` به تب AI.

- پین: `713377f366771e3e4730e6acd1bc290e0ebc6d6e`، لایسنس **AGPL-3.0-only**.
- جزئیات و حدود صداقت: `app/vendor/LEARNHARNESS_INTEGRATION.md`.
- `src/harness.js`: همان چهار فاز `Measure → Plan → Teach → Practice`،
  فیلدهای thinking/confidence، و گراف دانش (گزارهها + لینک به منبع/جلسه)،
  ذخیره در `store.ai.harness`.
- **ارائهدهندهٔ پیشفرض `LocalContentProvider`**: هیچ متن/جواب/توضیحی تولید
  نمیکند؛ فقط از درسها و تستهای موجود در فرم انتخاب میکند. وقتی منبعی ثبت
  نشده، صریحاً `no-source-registered` برمئیگردد، نه پاسخ ساختگی.
- وضعیت ارائهدهندهٔ خارجی: `not-configured` (بدون کلید، بدون بکاند، بدون
  `fetch`). قرارداد اتصال واقعی مستند شده است.
- UI: سطر وضعیت + ۴ چیپ فاز + دکمهٔ «شروع جلسه» در همان صفحهٔ تأییدشدهٔ AI،
  با کلاسهای موجود؛ پیامها از همان `.bubble` استفاده میکنند. دکمههای
  `TEACH/PRACTICE` موجود در پروتوتایپ هم به فازها وصل شدند.
- `window.APP.mountContentPackage(pkg)` در مرحلهٔ بعد منابع را به هارنس وصل
  میکند.

## ۴. کتاب (تمام ۸۴۸ صفحه، یک پاس)

- OCR کامل با `tools/ocr_book.py` در حال اجراست (resumable، خروجی خارج از گیت).
- `tools/structure_book.py` **تمام صفحات OCRشده را یکجا** به پیشنویس
  فرممحور تبدیل میکند: سؤالها، گزینهها، صفحهٔ مبدأ، confidence، و
  `correctIndex: null` وقتی پاسخنامهای یافت نشود (هیچ پاسخی جعل نمیشود).
- خروجی `content/source/…/draft-package.json` با `validate_content.py`
  اعتبارسنجی میشود ولی **`extracted/unreviewed`** است و وارد اپ نمیشود.
- گام بعد (وقتی منابع رسید): بازسازی ترتیب دوستونی از bboxهای TSV،
  تطبیق پاسخنامه، تخصیص `topicId`، ساخت `tracks/sections/lessons`،
  بازبینی → `reviewed` → جایگزینی `fixtures.js`.

## ۵. تستها

`npm test` → **۳۲/۳۲ PASS** (۲۴ تست مرحلهٔ قبل + ۸ تست وفاداری گره،
قالب آزمون/تمرین، و هارنس). `npm run verify` و `verify_upgrade.py` هم پابرجا.
