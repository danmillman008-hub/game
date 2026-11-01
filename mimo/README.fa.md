# پیش‌نمایش یکپارچهٔ میمو (فارسی، راست‌به‌چپ)

یک پیش‌نمایش قابل اجرا در مرورگر که سه سامانهٔ مستقل را زیر یک پوستهٔ فارسی کنار هم می‌گذارد:

| زبانه | موتور | مالکیت داده | وضعیت |
|---|---|---|---|
| یادگیری | موتور آفلاین Mimo Learn (بازسازی‌شده بر پایهٔ قرارداد در `HANDOFF/`) | `localStorage` | کار می‌کند، آفلاین |
| تمرین و آزمون | EPM (موتور آزمون چهارگزینه‌ای، FastAPI + Vue) — **همهٔ ۲۵ بخش حفظ شده** | SQLite خودش | کار می‌کند |
| مکس | LearnHarness (Next.js) — دست‌نخورده | پوشهٔ دادهٔ خودش | باز می‌شود |
| رتبه‌بندی | Mimo (پوسته) | `localStorage` | کار می‌کند |
| پروفایل | Mimo (پوسته) | `localStorage` | کار می‌کند |

هیچ موتوری بازنویسی نشده، هیچ پایگاه‌داده‌ای مشترک نیست، و هیچ لایهٔ همگام‌سازی بین موتورها وجود ندارد.

## ۱. پیش‌نیازها

| ابزار | نسخه | برای چه |
|---|---|---|
| Python | 3.11 یا بالاتر | پوسته/پروکسی، موتور یادگیری، EPM، اعتبارسنج‌ها |
| Node.js + npm | 22 یا بالاتر | ساخت EPM، اجرای LearnHarness، آزمون‌های jsdom |
| git | هر نسخهٔ جدید | دریافت موتورها (یک‌بار) |
| اینترنت | فقط بار اول | دریافت و نصب موتورها |

## ۲. اجرا

```bash
# ویندوز (PowerShell)
.\mimo\start-preview.ps1

# لینوکس / مک
bash mimo/start-preview.sh
```

اسکریپت: وابستگی‌ها را بررسی می‌کند، موتورها را (اگر نبودند) نصب می‌کند، هر سرویس را مستقل بالا می‌آورد، آدرس را چاپ
می‌کند و در صورت شکست، پیام فارسی می‌دهد. سپس مرورگر را باز کنید:

```text
http://localhost:4000
```

توقف: `Ctrl+C`. هیچ پایگاه‌داده‌ای بازنویسی نمی‌شود؛ اگر `mimo/.runtime/` وجود داشته باشد، همان استفاده می‌شود.

اجرای سریع بدون موتورهای جانبی (فقط پوسته + یادگیری):

```bash
bash mimo/start-preview.sh --no-engines     # یا .\start-preview.ps1 -NoEngines
```

### پورت‌ها

| سرویس | پورت | آدرس | بیرونی؟ |
|---|---|---|---|
| پوسته/پروکسی | 4000 | `0.0.0.0:4000` | بله — تنها پورت لازم |
| EPM | 8765 | `127.0.0.1:8765` | نه |
| LearnHarness | 3000 | `127.0.0.1:3000` | نه |

## ۳. محل داده‌ها (سه انبار جدا)

| موتور | محل | نکته |
|---|---|---|
| یادگیری | `localStorage` کلید `mimo.learn.progress.v1` | پاک کردن مرورگر = پاک شدن پیشرفت |
| EPM | `mimo/.runtime/epm-data/question_bank.db` | با `EPM_DATA_DIR` تغییر می‌کند |
| LearnHarness | `mimo/.runtime/lh-data/` + `lh-auth.json` | با `LH_DATA_DIR` |

`mimo/.runtime/` و `mimo/engines/src/` در `.gitignore` هستند: دادهٔ کاربر و کد موتورها وارد مخزن نمی‌شوند.

## ۴. ارتباط موتورها

پوسته یک پروکسی معکوس است: `/practice/*` → EPM (پیشوند حذف می‌شود)، `/max/*` → LearnHarness (پیشوند حفظ می‌شود).
جزئیات و دلیل هر تصمیم: `docs/ARCHITECTURE.fa.md`. اگر موتوری بالا نباشد، پیام ۵۰۲ فارسی و دستور راه‌اندازی می‌آید.

## ۵. ساخت محتوا

### ۵.۱ محتوای موتور یادگیری (Mimo)

```text
content-templates/mimo-offline/
├── README.fa.md              ← گردش کار ۶ گامی
├── TEMPLATE.fa.md            ← راهنمای فیلدها + برگهٔ تقلب DSL
├── blank-content-pack/       ← بستهٔ خالی و معتبر
├── example-content-pack/     ← مثال کامل (علوم هفتم، چرخهٔ آب)
├── schema/content-pack.schema.json
└── validator/validate_pack.py
```

```bash
python3 mimo/content-templates/mimo-offline/validator/validate_pack.py my-pack
```

### ۵.۲ بانک سؤال EPM

```text
content-templates/epm-question-bank/
├── README.fa.md              ← ستون‌ها و قواعد
├── data/example-questions.csv
├── blank-bank/               ← اسکلت ESQ
├── tools/build_esq.py        ← CSV → ESQ 1.0 (قالب بومی EPM)
├── tools/validate_bank.py    ← ساختاری + اعتبارسنج بومی EPM
├── tools/import_bank.py      ← وارد‌سازی + انتشار در EPM
└── tools/e2e_exam_test.py    ← آزمون سرتاسری آزمون
```

```bash
cd mimo/content-templates/epm-question-bank
python3 tools/build_esq.py data/example-questions.csv example-bank/sample-bank.esq
python3 tools/validate_bank.py example-bank/sample-bank.esq
python3 tools/import_bank.py example-bank/sample-bank.esq --profile 6
```

قالب چهارگزینه‌ای/تک‌پاسخ است؛ گزارش کامل قالب بومی در `docs/EPM_QUESTION_FORMAT.md`.

### ۵.۳ پیکربندی LearnHarness (مکس)

- تنظیمات مدل از داخل خود LH انجام می‌شود (صفحهٔ تنظیمات).
- **بدون کلید**، «مکس» باز می‌شود و پیام فارسی «سرویس هوش مصنوعی تنظیم نشده» می‌دهد؛ هیچ پاسخ ساختگی تولید نمی‌شود.
- فایل نمونهٔ `.env` با `LH_DATA_DIR`/`LH_AUTH_FILE` در `mimo/.env.example` است — هیچ سری‌ای در آن نیست.

## ۶. بومی‌سازی

لایهٔ `host/overlay/fa.js` + دیکشنری‌ها. پوشش فعلی و روش افزودن ترجمه: `docs/LOCALIZATION.fa.md`.
اندازه‌گیری: `python3 mimo/tools/i18n_coverage.py`.

## ۷. آزمون‌ها

```bash
bash mimo/tools/run-tests.sh
```

شمارش واقعی و نتیجهٔ هر مجموعه: `docs/TEST_REPORT.md` (۵۰ آزمون این مرحله + ۵۴ آزمون قرارداد HANDOFF).

## ۸. محدودیت‌ها

خلاصه: ترجمهٔ EPM/LH کامل نیست، اسکرین‌شات و آزمون مرورگری ممکن نشد (بدون مرورگر)، توضیح پاسخ EPM شاید در UI بومی
نمایش داده نشود، LH در حالت توسعه اجرا می‌شود. فهرست کامل با گام بعدی: `docs/LIMITATIONS_AND_NEXT.md`.

## ۹. فهرست تحویل‌شدنی‌ها

| # | تحویل | مسیر |
|---|---|---|
| 1 | پیش‌نمایش قابل اجرا | `start-preview.sh` / `start-preview.ps1` |
| 2 | فرمان شروع ویندوز | `mimo/start-preview.ps1` |
| 3 | README فارسی | همین فایل |
| 4 | قالب محتوای میمو | `content-templates/mimo-offline/` |
| 5 | بستهٔ محتوای نمونه | `content-templates/mimo-offline/example-content-pack/` |
| 6 | اعتبارسنج | `content-templates/mimo-offline/validator/validate_pack.py` |
| 7 | بومی‌سازی فارسی EPM | `host/overlay/fa.js` + `host/overlay/dict-epm.json` |
| 8 | قالب بانک سؤال EPM | `content-templates/epm-question-bank/` |
| 9 | بانک وارد‌شدهٔ نمونه | `content-templates/epm-question-bank/example-bank/sample-bank.esq` |
| 10 | گزارش قالب بومی سؤال EPM | `docs/EPM_QUESTION_FORMAT.md` |
| 11 | رابط فارسی LH | `host/overlay/dict-max.json` |
| 12 | گزارش معماری یکپارچه‌سازی | `docs/ARCHITECTURE.fa.md` |
| 13 | اسکرین‌شات‌ها | **BLOCKED** — فهرست و دستور: `docs/screenshots/README.fa.md` |
| 14 | گزارش آزمون PASS/FAIL/BLOCKED | `docs/TEST_REPORT.md` |
| 15 | محدودیت‌ها و گام بعدی | `docs/LIMITATIONS_AND_NEXT.md` |

## ۱۰. ساختار پوشه

```text
mimo/
├── shell/          پوستهٔ پنج‌زبانه (HTML/CSS/JS، بدون چارچوب)
├── learn/          موتور یادگیری (DSL، رندر، تصحیح، ذخیره، محتوا)
├── content/        بسته‌های محتوا (نمونهٔ دمو)
├── content-templates/  قالب‌ها و ابزارهای تولید محتوا
├── host/           پروکسی معکوس + لایهٔ فارسی/RTL
├── engines/        pins.json، آماده‌سازی و دریافت موتورها (کد موتورها اینجا نمی‌ماند)
├── tools/          نصب، آزمون، پوشش ترجمه
├── docs/           معماری، گزارش‌ها، محدودیت‌ها
└── tests/          آزمون‌های DOM/پوشش/اعتبارسنج
```
