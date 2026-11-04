# مدل داده، موتورها، پروکسی، آفلاین و RTL
<!-- v9-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v9](21_DESIGN_ROUND_9.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.
<!-- v8-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v8](20_DESIGN_ROUND_8.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.
<!-- v7-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v7](18_DESIGN_ROUND_7.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.

> ⚠️ **بایگانی / superseded:** این سند مربوط به دورهای قبل است. طراحی فعلی **[DESIGN v6](17_DESIGN_ROUND_6.md)** است؛ صفحهٔ ورود حذف، یادگیری بازسازی و زیرصفحات «انتخاب مسیر / نمای مسیر / داخل مبحث» از کد اضافه شدند. لاگهای قدیمی صرفاً ردپای حسابرسیاند.

> 🔄 **DESIGN v5 (حکم فعلی) — بازآفرینی ۱۰۰٪ از داخل کد:** لاگ کامل ← `16_DESIGN_ROUND_5.md`، prototype ← `DESIGN/index.html`، هندسهٔ استخراجشده ← `DESIGN/CODE_GEOMETRY.json`.
> اصلاحیهٔ نامگذاری: دکمهٔ قدیمی «پاسخنامه» = **«پاسخبرگ»** (گزینههای زدهشده)؛ «پاسخنامه» دکمهای **جداگانه** برای جواب تشریحی/توضیحات است. یک دکمهٔ «توضیح با هوش مصنوعی» در صفحهٔ سؤالات + همان دکمه در صفحۀ آخر آزمون. لیدربورد اطلاعات/امتیازات/آزمونهای خود فرد را نشان میدهد. متن پایینتر، بایگانی دور قبل است و فقط برای ردیابی نگه داشته شده.


## ۱. موتورهای پینشدهٔ خود ریپو (باز استفاده، نه بازنویسی)

`mimo/engines/pins.json`:

| موتور | ریپو / کامیت | لایسنس | استک | مسیر پروکسی |
|---|---|---|---|---|
| LearnHarness | `amosblomqvist/learnharness` @ `e69e85269c064c6c9c49a8b06ae78c06e79c4a63` | AGPL-3.0-only | Next.js 16 / React 19 | `/max/*` — **پیشوند حفظ میشود**، `basePath: "/max"` |
| EPM | `mo9652962-ai/english-multiple-choice-practice-machine` @ `14c1b276297258e51d05281bdc1dfaf750a2b564` | GPL-3.0-only | FastAPI + Vue 3 / Vite | `/practice/*` — **پیشوند حذف میشود**، `base=/practice/`, `VITE_API_ROOT=/practice/api` |

`mimo/start-preview.sh`: shell پورت ۴۰۰۰، EPM ۸۷۶۵، LearnHarness ۳۰۰۰؛ iframe هممیزبان؛ **دیتاستور جدا** (`LH_DATA_DIR`, `LH_AUTH_FILE`, `EPM_DATA_DIR`). این قراردادها عیناً حفظ میشوند؛ فقط لایهٔ فارسی/RTL و تزریق زمینه اضافه میگردد. لایسنسها در `mimo/ATTRIBUTION.md` / `COMPLIANCE_NOTES.fa.md` رعایت شوند.

## ۲. موجودیتها

| موجودیت | کلیدها | منبع |
|---|---|---|
| `UserProfile` | `userId, grade, field, targetMajor, totalScore, quota, daysToKonkur, locale=fa` | فرم هدفپلاس + `user.json`, `motivational_phrase.json` |
| `ExamBlueprint` | `examId, type, scope[], questionCount, durationSec, negativeMarking, difficultyMix, answerKeyVersion, seed, xpPolicy, retryPolicy, panelSet, version` | سند `19` + این پلن |
| `Question` | `questionKey, paperKey, unitKey, subjectId, topicId, difficulty(1..5), options[4], answerKeyVersion, explanationPerOption, error_code, equation, figure, rtlMarker` | ESQ 1.0 + HANDOFF DSL |
| `Attempt` | `attemptId, examId, startedAt(monotonic), elapsedSec, answers[], unanswered[], wrong[], score, percent, simulatedPercent, rank, percentile, xpEarned, synced` | هدفپلاس `report_model` + میمو `applyResult` |
| `Mistake` | `questionKey, attemptId, error_code, topicId, fsrsDue, consecutiveCorrect, resolvedAt` | EPM `WrongView` + FSRS |
| `CounselingPlan` | `templateId(1..7), weekStart, blocks[], advisorId, goals[], report[]` | ۷ تصویر `study_schedule` + `/Advisor/Plans` |
| `XpEvent` | `eventId, source, amount, capBucket, createdAt, outbox` | سیستم واحد میمو |
| `LhSession` | `sessionId, graphRef, contextInjected (بدون answerKey)` | LH |

## ۳.Room و outbox

جدولهای میمو (`HANDOFF/schema`) دستنخورده میمانند؛ جداول تازه `exam_blueprint`, `question_bank`, `attempt`, `mistake`, `counseling_plan`, `xp_event`, `lh_session_ref` به همان الگوی migration و `outbox` اضافه میشوند. تمام نوشتها ابتدا محلی، سپس همگامساز؛ `synced` flag؛ تضادها با `answerKeyVersion` حل میشوند. حداکثر ۴۰ رویداد تحلیلی (قاعدهٔ سند `19`)، بدون Firebase/RevenueCat، بدون صفحهٔ پرداخت.

## ۴. RTL / بومیسازی

- `fa` از قبل در ARSC میمو وجود دارد (۱۱۶ لوکال)، ولی `lessons-fa` وجود نداشت → بستهٔ محتوای فارسی **جدید** ساخته میشود، با همان ساختار JSON میمو.
- جهت `rtl` سراسری؛ فقط بلوک `<equation>`, کد و اعداد لاتین LTR. نیمفاصله، اعداد فارسی، `ۀ`/`ی` عربی نرمالسازی شوند.
- اعداد در چارتها و تایمر: سیاست واحد (پیشنهاد: اعداد فارسی در متن، لاتین در تایمر/فرمول برای ثبات عرض).
- `contentDescription` برای تمام گرهها/چیپها؛ حداقل کنتراست همان توکنهای میمو؛ `TalkBack` و `TalkBack` focus order راست به چپ.

## ۵. امنیت / تمامیت

- پاسخنامه و `answerKey` هرگز به کلاینت AI/LLM ارسال نمیشود.
- `questionContentHash` (ESQ) + `answerKeyVersion` برای جلوگیری از تغییر silently.
- تایمر مونوتونیک + علامت `integrityFlags` برای تشخیص kill/بازگشت به عقب ساعت.
- هیچ کلید/توکن/مسیر محلی در ریپو (قاعدهٔ «No secrets»).

## ۶. پذیرش

- [ ] `/max/*` و `/practice/*` با پیشوند صحیح پاسخ میدهند؛ دیتاستورها جدا
- [ ] قطع شبکه → تمام مسیرهای یادگیری/آزمون/مرور آفلاین کار میکنند
- [ ] migration قدیمی خراب نمیشود؛ outbox دوبارهایجاد نتیجه نمیدهد
- [ ] ۰ پاسخنامه در prompt؛ ۰ کلید در لاگ/ریپو
- [ ] RTL و نایت مُد در تمام صفحات تازه
