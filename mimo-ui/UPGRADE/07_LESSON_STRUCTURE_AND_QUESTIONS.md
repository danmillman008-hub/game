# ساختار داخلی، چیدمان سؤالات و مرور/حذف غلطها
<!-- v11-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v11](23_DESIGN_ROUND_11.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.
<!-- v10-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v10](22_DESIGN_ROUND_10.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.
<!-- v9-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v9](21_DESIGN_ROUND_9.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.
<!-- v8-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v8](20_DESIGN_ROUND_8.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.
<!-- v7-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v7](18_DESIGN_ROUND_7.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.

> ⚠️ **بایگانی / superseded:** این سند مربوط به دورهای قبل است. طراحی فعلی **[DESIGN v6](17_DESIGN_ROUND_6.md)** است؛ صفحهٔ ورود حذف، یادگیری بازسازی و زیرصفحات «انتخاب مسیر / نمای مسیر / داخل مبحث» از کد اضافه شدند. لاگهای قدیمی صرفاً ردپای حسابرسیاند.

> 🔄 **DESIGN v5 (حکم فعلی) — بازآفرینی ۱۰۰٪ از داخل کد:** لاگ کامل ← `16_DESIGN_ROUND_5.md`، prototype ← `DESIGN/index.html`، هندسهٔ استخراجشده ← `DESIGN/CODE_GEOMETRY.json`.
> اصلاحیهٔ نامگذاری: دکمهٔ قدیمی «پاسخنامه» = **«پاسخبرگ»** (گزینههای زدهشده)؛ «پاسخنامه» دکمهای **جداگانه** برای جواب تشریحی/توضیحات است. یک دکمهٔ «توضیح با هوش مصنوعی» در صفحهٔ سؤالات + همان دکمه در صفحۀ آخر آزمون. لیدربورد اطلاعات/امتیازات/آزمونهای خود فرد را نشان میدهد. متن پایینتر، بایگانی دور قبل است و فقط برای ردیابی نگه داشته شده.


خواسته: «ساختار داخلیش و نحوهٔ سوالات چیده شدن و مرور غلطها هم میتونی همون میمو رو استفاده کنی یا حتی ارتقا بدی… کلی کار قبلا تو ریپو انجام شده حتما ازش استفاده کن».

## ۱. پایهٔ الزامی (از HANDOFF ریپو، بدون تغییر)

| قرارداد | مسیر | قانون |
|---|---|---|
| DSL درس | `mimo/HANDOFF/docs/dsl.md`, `mimo/learn/dsl.js` | ۲۷ تگ، ۱۲ ویژگی، ساختار بلوکی `<lesson><block>...` |
| `visible-if` | `18_KONKUR_TRANSFER/`, `mimo/learn/grade.js` | سه مقدار `true/false/unknown` — ناشناخته ≠ نادرست |
| نمرهدهی آفست | `mimo/HANDOFF/data/grading_vectors.json` | ۱۲ وکتور، `partial`, `offset`، آرایهٔ پاسخ |
| پیشرفت | `mimo/learn/store.js` | `chapterProgress`, `tutorialProgress`, `trackProgress`, `globalStats` |
| آفلاین | بستهٔ محتوا + `outbox` | محتوا باندل، نتایج در صف |
| وبویو | `mimo-ui/REFERENCE/REA_EVIDENCE/JS_EVIDENCE.json` | `gesture/activity/focus/height`, `MimoLesson.postMessage` |

**اینها دستنخورده میمانند**؛ ارتقا فقط لایهای روی آنهاست (قاعدهٔ وفاداری).

## ۲. ارتقاهای مجاز (همگی از شواهد دو اپ/موتورها)

| ارتقا | دلیل/شاهد | پیادهسازی |
|---|---|---|
| `<equation>`, `<figure>`, `<table>` | سؤالات کنکور فرمول/شکل/جدول دارند | بلوکهای تازهٔ DSL در همان پارسر، با MathJax/`flutter_tex`-معادل بومی و LTR محدود به بلوک |
| `rtlMarker`, Persian normalizer | فارسی، اعراب، نیمفاصله، اعداد فارسی | نرمالساز قبل از مقایسهٔ پاسخ |
| `answerKeyVersion`, `questionVersion` | سند `19`: «answer-key versioning, integrity» | هر تلاش دو نسخه را ذخیره کند؛ تغییر کلید، نتایج قدیمی را باطل نمیکند |
| `error_code` + پاسخ تشریحیِ هر گزینه | همدرس: «اشتباه پاسخ دادی، پاسخ تشریحی رو ببین»، «درجه سختی سؤال» | `grading_vectors` با `explanation` و `difficulty(1..5)` غنی شود |
| نمرهٔ منفی ⅓ و `unanswered` | هدفپلاس: «اثر نمرهٔ منفی», «تعداد سوالات نزده» | لایهٔ `examGrade` جدا از `applySubmission` درس |
| شبیهسازی «اگه غلطها رو نزده میذاشتی، درصدت…» | هدفپلاس | محاسبهٔ سه سناریو در پنل نتیجه |
| پاسخبرگ / پالت سؤال | `answer_sheet.svg`, `اسم پاسخبرگ`, `ثبت پاسخها و محاسبهٔ خودکار درصد` | گرید ۳تایی همان گرهها |
| `تعویض سوال` / `حذف سوال` / «دو گزینهٔ غلط رو حذف کن» | همدرس | اکشنهای `lesson_interactive_*` |
| مرور هوشمند FSRS | EPM `WrongView`, `FSRS`, همدرس «مرور مبحث» / «برنامهریزی هوشمند» | صف `reviewQueue` با فاصلهٔ تکرار؛ غلط بعد از ۲ پاسخ درست متوالی خارج شود |
| بانک سؤال نسخهدار | EPM `docs/question-bank-format.md` (ESQ 1.0 ZIP: `manifest/papers/answers/labels/assets`, `paperKey/unitKey/questionKey`, `contentVersion`) | قالب `konkur-bank-v1` الهامگرفته، با `LICENSE` و هش محتوا |
| ۵…۴۰۰ سؤال، ۴ شکل سؤال از ۷ فلشکارت | هدفپلاس «تعداد سوال باید بین ۵ تا ۴۰۰ باشه»؛ همدرس «در هر دور از یادگیری از 7 فلشکارت به ۴ شکل مختلف سوال پرسیده میشه» | محدودهٔ Blueprint + چرخش قالب سؤال |
| تحلیل بر حسب درس/مبحث | `AnalyisByLessonsScreenWidget` همدرس، `Chart of Test Scores` | همان `report_lesson_fragment.xml` |

## ۳. چیدمان سؤال (ثابت، از میمو)

`lesson_interactive_singlechoice_fragment.xml`, `..._multiplechoice_fragment.xml`, `..._fillthegap_fragment.xml`, `..._validatedinput_fragment.xml`, `..._reveal_fragment.xml`, `interaction_keyboard_with_lesson_feedback.xml`, `lesson_interactive_feedback_bottom_sheet_dialog.xml`. ترتیب: صورت سؤال → گزینهها (۴، `AnswerButtonGrid`) → نوار تعامل → باتمشیت بازخورد. در **حالت آزمون** فقط بازخورد تا پایان به تعویق میافتد؛ چیدمان، فونت، فاصله، ریپل و انیمیشنها عیناً میمانند.

## ۴. جریان غلطها (Wrong-Answer Lifecycle)

```
attempt(wrong) → mistake{questionKey, answerKeyVersion, error_code, topicId, difficulty, ts}
   → reviewQueue (FSRS) → «تمرین اشتباههای تمام مباحث» / «آزمون دوباره»
   → پاسخ تشریحی + راهنما + «دو گزینهٔ غلط رو حذف کن» + «تعویض سوال»
   → correct × 2 متوالی → resolved (از لیست خارج، ولی در history میماند)
   → XP «جبران» + نشان + بهروزرسانی نقشهٔ ضعف/تراز
```

قواعد: حذف غلط **هیچوقت بهمعنای پاککردن تاریخچه نیست** (هدفپلاس: «این پاسخبرگ… برای همیشه پاک میشه» → ما فقط پاککردن پاسخبرگ بهدرخواست کاربر را مجاز میکنیم، نه حذف شواهد یادگیری). ثبت در outbox، قابل همگامسازی آفلاین.

## ۵. ردیابی تصمیمات قبلی ریپو

`19_KONKUR_PRODUCT_TRANSFER_SPEC.md` (۴۲ ردیف ماتریس، سه حالت A LearnHarness / B EPM exam centre / C study-plan card path)، `18_KONKUR_TRANSFER/TRANSFER_MATRIX.md` (۳۲ ردیف، ۸ قرارداد، ۱۲ الگو، ۷ ساخت تازه: timed exam، rank/percentile، weakness map، FSRS، parent/teacher report، authoring panel)، `WHAT_NOT_TO_COPY.md`, `ADAPTATION_PLAN.md` (۳ فاز ۸ هفتهای) — همگی خوانده و در `10_PHASED_ROADMAP.md` ادغام شدند؛ موارد «Mimo has no exam mode → needs timer, scoring policy, question-bank rotation, answer-key versioning, integrity» عیناً به فازهای P1…P3 رفتند.

## ۶. پذیرش فاز P2/P3

- [ ] ۱۲ وکتور نمرهدهی قدیمی همچنان PASS (رگرسیون صفر)
- [ ] DSL تازه با ۲۷ تگ قدیمی سازگار است؛ `unknown` همچنان `unknown` است
- [ ] هر تلاش `answerKeyVersion` دارد؛ تغییر کلید، تاریخچه را خراب نمیکند
- [ ] نمرهٔ منفی، نزده، تشریحی و شبیهسازی سهسناریو تست شده
- [ ] FSRS + حذف بعد از ۲ پاسخ درست + تاریخچهٔ پایدار
- [ ] چیدمان سؤال diff بصری با `lesson_interactive_*` = ۰ تغییر
