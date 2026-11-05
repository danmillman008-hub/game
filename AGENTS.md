# AGENTS.md — قرارداد کار برای هر ایجنت / هوش مصنوعی روی این ریپو

**زبان کاربر: فارسی. پاسخ نهایی را به فارسی بده.** این سند را قبل از هر تغییری بخوان.

## ۱) ترتیب خواندن (الزامی)

1. `README.md` — نقشهٔ کلی
2. `docs/00_START_HERE.md` — جهتیابی ۵ دقیقهای
3. `docs/02_DECISIONS.md` — **قوانین لازمالاجرا** و تصمیمات لغوشده
4. `docs/03_ERRORS_AND_DEAD_ENDS.md` — بنبستها را دوباره امتحان نکن
5. `docs/04_CURRENT_STATE.md` — وضعیت دقیق امروز
6. `docs/05_ROADMAP.md` — کاری که قرار است انجام شود
7. `docs/06_EVIDENCE_INDEX.md` + `REPO_INDEX.json` — محل شواهد
8. سپس فایلهای فنی: `app/docs/MIMO_CONTENT_MODEL.md`،
   `app/docs/MIMO_NATIVE_NAVIGATION.md`، `app/docs/OUTPUT_GUIDE.md`

## ۲) قواعد سخت (هرگز نقض نکن)

| # | قانون |
|---|---|
| ۱ | فقط روی شاخهٔ **`arena/aebb90b7-game`** کار کن؛ شاخهٔ دیگری نساز، به جای دیگری push نکن. |
| ۲ | **`SERVER CONFIRMED=0`**. هیچ URL زنده، هدر Authorization، بدنهٔ درخواست، فرمول پاداش/امتیاز سرور، رتبه، یا رفتار API را «تأییدشده» اعلام نکن. استاتیک APK ≠ رانتایم. |
| ۳ | **بدون LLM، بدون شبکه، بدون کلید API، بدون متن تولیدشده.** در کد محصول `fetch(` / `XMLHttpRequest` / `WebSocket` / `EventSource` / `type="module"` خارجی / `AIza…` / `sk-…` مجاز نیست. `externalProvider: 'not-configured'` باید بماند. |
| ۴ | **محتوای درسنامه را نساز/حدس نزن.** فقط از منبع موجود (پروتوتایپ `QRAW` تأییدشده یا کتاب بعد از بازبینی انسانی) استخراج کن. `app/content/source/` (OCR خام، کتاب حق نشر دار) در `.gitignore` است؛ هرگز commit نشود. پیشنویس پردازششدهٔ کتاب `unreviewed` است و **وارد اپ نشود**. |
| ۵ | داراییهای مرجع **بایتبهبایت** دستنخورده بمانند: `mimo-ui/UPGRADE/DESIGN/index.html` (SHA `c356068daa5ccafbee46599897ad18bdf1e4f91f1ca23f36b1b8bd153dbfdb78`)، `app/assets/phone.html`، `proto.css`، `proto-data.js`، `proto-ui.js`. `verify_app.py` هش آنها را چک میکند. |
| ۶ | یادداشتهای **v12.5-fa صددرصد** رعایت شود: ۵ تب `Learn\|Practice\|AI\|Leaderboard\|Profile` با برچسب فارسی، ۳ چیپ (سکه/کلید ∞/استریک)، بدون تب مکس/روتین روزانه/Habitica/Dictate، بدون Pro/پرداخت، RTL فارسی، شواهد `data-code`/`data-lh` پنهان، **هیچ رنگ/فونت/شعاع/آیکون/فاصلهای تازه** (همه از توکنهای `proto.css` و وکتورهای ARSC)، هاب ۷بخشی آزمون، تایمر فقط داخل آزمون، «پاسخبرگ» ≠ «پاسخنامه»، چیپ AI، ۳ مسیر خروج، دکمهٔ سرتاسری Continue. |
| ۷ | میمو واقعی ۹٫۳۵ **۴ تب** دارد (M09)، ولی حکم کاربر ۵ تب است (F13). ترتیب/مقصد ۴ تب اصلی از M09، تب پنجم AI مصوب است. این تعارض را بیاجازهٔ جدید کاربر تغییر نده. |
| ۸ | خروجی `app/dist/` **تولیدی** است؛ دستی ویرایش نکن. منبع آن `app/native/index.html` + `app/src/native.js` + `app/tools/build_output.py` است. |
| ۹ | **اسناد تاریخی را پاک/بازنویسی نکن**: `mimo-ui/UPGRADE/*`، `ANALYSIS/MISSION_*`، گزارشهای فازها. فقط سند تازه اضافه کن و لینک بده. |
| ۱۰ | قبل از پایان کار: `npm test --prefix app`، `npm run verify --prefix app`، ولیدیتور محتوا، و `python3 docs/verify_docs.py` را اجرا کن و اعداد را صادقانه گزارش بده. |

## ۳) محیط و ابزار (چیزهایی که وجود ندارند / محدودیتها)

- دسترسی اینترنت فقط به `github.com`, `codeload.github.com`, `api.github.com`,
  `registry.npmjs.org`, `pypi.org`, `files.pythonhosted.org`.
- **هیچ شبیهساز/ADB/KVMـی در دسترس نیست**؛ مأموریتهای رانتایم M03–M09 از طریق
  GitHub Actions runner انجام شدند. `workflow_dispatch` روی شاخه ۴۰۴ میداد.
- مرورگر سیستمی (`chromium`/`firefox`) نصب نیست. برای اسکرینشات واقعی از
  `@sparticuz/chromium` + `puppeteer-core` (npm) با
  `LD_LIBRARY_PATH=/tmp/al2023/lib:/tmp` استفاده شد؛ خارج از ریپو، commit نشد.
- OCR: `PaddleOCR` مسدود، `rapidocr-onnxruntime` نیازمند `libGL.so.1`،
  PEP 668 → venv در `/home/user/_work/ocr_venv`. **OCR ۸۴۸/۸۴۸ کامل شده؛ دوباره اجرا نکن.**
- `CairoSVG`/ImageMagick برای SVG→PNG شکست خوردند؛ `PIL` فقط در venv بالا.
- `python3` سیستمی `jsonschema` ندارد؛ ولیدیتور فرم `app/tools/validate_content.py`
  بدون وابستگی است. بیلدر `app/tools/build_output.py` هم بدون وابستگی است (رجیستری
  ماژول ساده، **نه esbuild**).

## ۴) کارهای روتین

| میخواهی… | بکن |
|---|---|
| خروجی تکفایل را بسازی | `python3 app/tools/emit_structured_package.py && python3 app/tools/build_output.py` |
| محتوای تازه وارد کنی | فرم `app/content/MIMO_INFORMATION_FORM.json` → `validate_content.py` → `emit_structured_package.py` → rebuild |
| کتاب را پردازش کنی | `python3 app/tools/process_book.py` (خروجی در `app/content/source/`، خارج از گیت) |
| اپ توسعهای را ببینی | `cd app && npm start` (پیشنمایش ۳۰۰۰/۳۰۰۱ از `app/dist/` سرو میشود) |
| تغییری بدوی | تستها + ورایفایرها + `docs/04_CURRENT_STATE.md` و `REPO_INDEX.json` را بهروز کن |

## ۵) اسناد «قدیمی / گمراهکننده» که باید با احتیاط خواند

- `mimo-ui/UPGRADE/00_START_HERE.md` و `README.md` بنرهای `superseded` فراوان و
  «حکم فعلی = DESIGN v4» دارند؛ ⚠️ **بایگانی / superseded**؛ **حکم فعلی محصول = دو بازسازی آخر**
  (`2042db0d`, `9179b8c4`) و خروجی `app/dist/`. اسناد آن پوشه بایگانی پلناند.
- `app/OUTPUT_REPORT.md` شامل گزارش خروجی **ردشده** (قدیمی) است؛ سربرگ تازهٔ آن
  توضیح میدهد که جایگزین شده.
- `app/README.md` / `app/content/README.md` ممکن است اعداد تست قدیمی داشته باشند؛
  اعداد معتبر در `docs/04_CURRENT_STATE.md` است.

## ۶) لحن و صداقت

کاربر چند بار صریحاً به «نمونهٔ خام / فاجعه / درک نکردن اپ اصلی» اعتراض کرد.
پس: **ادعا نکن، عدد بده، منبع بده، ناتمامها را بگو**. اگر چیزی را نمیدانی بنویس
`UNKNOWN`؛ اگر چیزی فقط استاتیک است بنویس `VERIFIED_STATIC`، نه رانتایم.
