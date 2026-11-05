# ۵ · چه چیزی قرار است بسازیم (نقشهٔ راه صادقانه)

> اصل راهنما: **اول صحت محتوا، بعد گسترش رندررها، آخر تجربهٔ دستگاه.**
> تا وقتی محتوا `unreviewed` است، هیچ ویژگی تازهای «تمامشده» محسوب نمیشود.

## P0 — چیزی که کاربر واقعاً منتظرش است

### R1 · درسنامهٔ واقعی کتاب (بازبینی انسانی)
- ورودی: `app/content/source/biology-12/PROCESSED_DRAFT.json`
  (۸۴۸ صفحه، ۷۷۵ مدخل پاسخنامه، ۶۰۰ پیوند پرسش–پاسخ، ۳۰۰ پیشنویس ریزدرس).
- کار: اصلاح غلطهای OCR («یافته»→«یاخته»، «هغز استفوان»→«مغز استخوان»)،
  جداسازی ستونها، تأیید `correctIndex` و توضیح گزینهها، حذف joinهای مشکوک.
- خروجی: `STRUCTURED_PACKAGE.json` با `source.kind:'converted-book'`،
  `contentStatus:'reviewed'`، `reviewStatus:'approved'`، و `trace.sourceRef`
  به صفحه/شمارهٔ سؤال کتاب.
- **تعریف تمامشد:** `validate_content.py` سبز + `reviewStatus:'approved'` +
  همان ۴۵ تست + تأیید دستی ۲۰ پرسش نمونه. تا قبلش وضعیت `unreviewed` بماند.

### R2 · نگاشت واقعی `chapterRefFor()`
- الان انتخاب فصل/درس با هش ID انجام میشود، نه `curriculumId` میمو.
- کار: اتصال به `ANALYSIS/MISSION_09/COMPLETE_CURRICULUM_GRAPH.json`
  (۱۹ track / ۱۴۴ section / ۱٬۰۲۹ tutorial / ۱٬۹۴۷ chapter / ۳۷٬۱۸۳ placement)
  یا صرفاً نگاشت صریح ۲۰ فصل کتاب به ۲۰ درسنامهٔ بسته.
- **تعریف تمامشد:** هیچ `hashCode`/random در مسیر محتوا نماند؛ تستی اضافه شود
  که همان ورودی همیشه همان خروجی بدهد.

### R3 · حذف آخرین ردپای دموی چیدمان
- `app/assets/phone.html` همچنان حاوی «گاهی لازم است متنها را با شکستن خطوط…»
  است (بهعنوان سند تاریخی). `native.js` دیگر آن را نمیخواند و
  `verify_output.py` این را چک میکند.
- کار: اگر کاربر خواست، نسخهٔ پاکشده در یک فایل **جدید** ساخته شود و هش قدیمی
  در بایگانی بماند؛ `verify_app.py` بهروز شود. بدون اجازهٔ صریح، هش مصوب را نگه دار.

## P1 — کاملکردن موتور درس (پس از P0)

| # | کار | منبع اندازهگیری | تعریف تمامشد |
|---|---|---|---|
| R4 | رندرر `validatedInput` + مقایسهٔ `solvedContent` آفلاین | `COMPLETE_LESSON_ENGINE_SPEC.md` A6–A11 | تست ولیدیتور + UI |
| R5 | رندرر `InteractiveWebView` بهصورت محلی (بدون شبکه) | `COMPLETE_UI_RENDERER_CATALOG.md` | ۵ message kindها بومیشبیهسازی شوند؛ ۰ درخواست خارجی |
| R6 | بلوک `Reveal` / `noninteractiveSlide` / `executableFiles` (نمایش کد بدون اجرا) | همان کاتالوگ (۱۳٬۴۹۶ / ۹٬۸۳۷ / ۷٬۸۵۹ / ۳٬۸۴۷ / ۱٬۴۴۲ / ۱٬۰۷۹ جایگذاری) | حداقل ۸ خانوادهٔ رندرر پوشش داده شود |
| R7 | سطوح سختی (`hardModeSelected`, `hardModeContent`, `challengeLevel0–2`) | `PEDAGOGY.md` (چرخهٔ HOOK→…→RECOVERY) | تست چرخهٔ هفتگانهای |
| R8 | صف مرور غلطها بهصورت بیننشستهای | `COMPLETE_LEARNER_STATE_SPEC.md` | `inQueue` در `localStorage` پایدار بماند |

## P2 — سطوحی که همچنان placeholderاند

| # | سطح | وضعیت فعلی | هدف |
|---|---|---|---|
| R9 | بانک سؤال / آزمون | `QBANK` و `exam-template.js` نمونهاند | آزمون ۷بخشی واقعی با پاسخبرگ + پاسخنامه + تایمر، فقط محلی |
| R10 | `learning-path.js` | ۱۲ درس / ۶۰ فصل / ۱۸۰ درس ساختگی از `KONKUR` | جایگزینی با همان `STRUCTURED_PACKAGE` |
| R11 | Leaderboard / Profile | محتوایشان در رانتایم M08 دیده نشد (`UNKNOWN`) | یا حداقل «وضعیت من» مصوب v8، یا علامت `NOT MODELED` صادقانه |
| R12 | `ai-studio.js` / `harness.js` | `local-content (بدون LLM)`، هزینه `۰٫۰۰ دلار` | حفظ؛ فقط در صورت درخواست صریح کاربر و با قرارداد `EXTERNAL_PROVIDER_CONTRACT` تغییر کند |

## P3 — تجربه و توزیع

| # | کار | یادداشت |
|---|---|---|
| R13 | تست نصب واقعی PWA روی گوشی Android | `beforeinstallprompt` / `display:standalone` / آیکون maskable؛ فعلاً انجام نشده |
| R14 | اسکرینشات مرجع خودکار در CI | فعلاً Chromium خارج از ریپو (`@sparticuz/chromium`)؛ ۴۰+ شات در `/home/user/_work/shots/` هستند ولی commit نشدند |
| R15 | بیلد قابلتکرار بایتبهبایت | `BUILD_MANIFEST.json` دارای `generatedAt` و ZIP حاوی timestamp است؛ هش `Mimo.html` پایدار، هش ZIP نه |
| R16 | پاکسازی فایلهای ریشهٔ آپلود اولیه | فقط با اجازهٔ کاربر؛ اصل «اسناد تاریخی پاک نشوند» حاکم است |

## P4 — شکافهای تحلیلی (فقط اگر کاربر خواست)

`ANALYSIS/MISSION_09/FINAL_UNKNOWN_REGISTER.md` → «**No further broad discovery
mission is recommended**». موارد باقی: `U-WEB-001` (پل بومی WebView)،
فرمولهای پاداش وابسته به سرور، URL رانتایم، بدنهها/هدرها، ماتریس پاسخ درس.
بستنشان نیازمند **دستگاه/احراز هویت واقعی** است، نه تحلیل استاتیک بیشتر.
هرگز بهعنوان «انجام شد»گزارش نشود مگر با شواهد رانتایم تازه.

## ترتیب پیشنهادی برای ایجنت بعدی

```
R1 (محتوای بازبینیشده) → R2 (نگاشت قطعی) → R9 (آزمون واقعی)
   → R4/R5/R6/R7 (رندررها) → R10/R11 → R13 (دستگاه) → R14
```

هر مرحله: `npm test --prefix app` + `npm run verify --prefix app` +
`docs/verify_docs.py` + بهروزرسانی `04_CURRENT_STATE.md` و `REPO_INDEX.json`.

بعدی: [`06_EVIDENCE_INDEX.md`](06_EVIDENCE_INDEX.md)
