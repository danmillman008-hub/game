# گزارش مرحلهٔ دوم — اتصالها و آمادهسازی محتوا

**تاریخ:** ۲۰۲۶-۱۱-۰۵ · **شاخه:** `arena/aebb90b7-game`
**پیشنیاز:** اپ آفلاین v12.5-fa (commit `3eed9da3`) + فرم اطلاعاتی و پداگوژی (`00ca5d3d`)

## درخواستها و وضعیت

| # | درخواست | وضعیت |
|---|---|---|
| ۱ | «یکباره کل کتاب بره» (نه فصل پایلوت) | ✅ آرشیو ۱۲تکه بازسازی، PDF کامل ۸۴۸صفحهای استخراج، OCR **تمام کتاب** بهصورت یک پاس در حال اجرا؛ `structure_book.py` تمام صفحات را یکجا ساختاردهی میکند |
| ۲ | وصل `learnharness` به بخش AI | ✅ معماری ۴فازه + گراف دانش + ارائهدهندهٔ محلی؛ قرارداد خارجی و لایسنس AGPL مستند؛ UI در همان صفحهٔ مصوب |
| ۳ | اصلاح گرهها برای تطابق دقیق با اپ اصلی | ✅ لایهٔ وفاداری از روی کاتالوگ PN/V10 + `NODE_CODE_GEOMETRY.json`؛ داده محور شد |
| ۴ | قالب آزمونها + بررسی بخش تمرین | ✅ ۷ قالب آزمون + ۴ قالب تمرین؛ بررسی شد که تمرین نباید آزمون دوم شود |

## ۱) کتاب (همهٔ ۸۴۸ صفحه)

- پوشهٔ `zist` در Drive: `@BankBookkonkor (26).zip` + `.z01…z11` (۵۹۱٬۱۵۹٬۰۹۴ B).
- reconstruct → **`@BankBookkonkor (26).pdf`**: ۶۲۵٬۱۸۰٬۶۲۲ B، ۸۴۸ صفحه، تماماً تصویری.
- OCR: libtesseract 5.5.3 + `tessdata_best/fas` (از `api.github.com`)، 200dpi،
  ۶ worker، **resumable**، خروجی JSON هر صفحه (متن + confidence + bbox کلمات TSV)
  + manifest با SHA256 کتاب. خروجی در `app/content/source/` و در `.gitignore`.
- `structure_book.py`: تمام صفحات در **یک پاس** → پیشنویس فرممحور
  (`questions[]` با `trace.sourcePage` و `correctIndex: null` وقتی پاسخ نامعلوم است)
  + `STRUCTURE_REPORT.json`. پیشنویس `extracted/unreviewed` است و **وارد اپ نمیشود**.

> PaddleOCR: ریپو در دسترس بود، ولی وزنهای مدلش روی هاستهای بستهایان؛
> از معادل آفلاین استفاده شد. `SERVER CONFIRMED=0` پابرجاست.

## ۲) LearnHarness (تب هوش مصنوعی)

- پین `713377f366771e3e4730e6acd1bc290e0ebc6d6e` · AGPL-3.0-only.
- `src/harness.js`: `measure → plan → teach → practice`، گراف گزارهها،
  confidence/reasoning، ذخیره در `store.ai.harness`.
- **هیچ مدل زبانی/درخواست شبکهای اجرا نمیشود.** `LocalContentProvider` فقط
  محتوای موجود در فرم را انتخاب میکند؛ با فرم خالی پیام صریح
  «منبعی ثبت نشده» میدهد نه پاسخ ساختگی. ارائهدهندهٔ خارجی
  `not-configured` است.
- UI: سطر وضعیت + ۴ چیپ فاز + «شروع جلسه» در صفحهٔ AI، با کلاسهای موجود؛
  دکمههای `TEACH/PRACTICE` پروتوتایپ به فازها وصل شدند.
- `window.APP.mountContentPackage(pkg)` برای مرحلهٔ بعد آماده است.

## ۳) گرههای آموزشی = اپ اصلی

- `assets/node-match.css` + `src/nodes.js` (بعد از `proto.css` لود میشوند؛
  داراییهای محافظتشده بایتبهبایت دستنخوردهاند).
- 92/26/8dp، آیکون 48dp (چک 44)، رابط 10dp با قوس 32dp، حلقهٔ 60dp/8dp/55%،
  شبکهٔ نقطهای 1.6/26، واژهنامهٔ شناور «A»، انیمیشن 220ms.
- حالتها: `done / cur-play / cur-half / next / bolt-active / bolt-optional / locked`
  — **دادهمحور** از `progress`، با `seedStates` برای حفظ ۶ حالت مصوب در حالت
  بدون پیشرفت. `assertGeometry(window.NODE)` در بوت `ok===true` میدهد.

## ۴) قالب آزمون / تمرین

- `EXAM_TEMPLATE.json`: ۷ بخش منطبق `exam-hub` با قانون انتخاب، دقایق،
  سیاست پاسخنامه و همان کامپوننتهای پاسخگویی.
- `PRACTICE_TEMPLATE.json`: بررسی انجام شد → تمرین همان کامپوننتهاست،
  `timed:false`، retry و بازخورد فوری؛ آزمون دوم ساخته نشد.
- `src/exam-template.js` + `tools/emit_templates.py`: `buildExam`,
  `buildPracticeSession`, `selectQuestions`, گزارش `shortfall`.
- وصل: کلیک ردیف آزمون → `exam.activeTemplate`؛ رکورد نشست تمرین → `template`.

## ۵) آنچه **انجام نشده** (ادعای完成的 نمیشود)

- پر کردن نهایی درسنامهها و بانک تست: طبق گفتهٔ شما **مرحلهٔ بعد**، بعد از
  تحویل منابع. تا آن موقع `fixtures.js` همچنان `PLACEHOLDER` است.
- پیشنویس OCR نیازمند بازبینی است: صفحات دوستونی، جدولها و پاسخنامهها در
  متن خام درهم میریزند؛ `correctIndex` اکثر سؤالها `null` و
  `reviewStatus=unreviewed` است. bboxهای TSV برای بازسازی ستونها در گام بعد
  استفاده میشوند.
- اجرای واقعی LearnHarness با مدل: نیازمند endpoint/کلید و بکاند است؛
  در این بیلد آفلاین پیکربندی نشده و هیچ رفتاری جعل نشد.

## ۶) تستها و تحویل

- `npm test` → **۳۲/۳۲ PASS** (۸ تست جدید: وفاداری گره، قالبها، هارنس،
  نبود شبکه، وصلشدن ردیف آزمون/نشست تمرین).
- `npm run verify` → ۴۱/۴۱ PASS · `verify_upgrade.py` → ۲۵۹/۲۵۹ PASS.
- `validate_content.py` پیشنویس کتاب و قالب فرم را PASS میکند.
