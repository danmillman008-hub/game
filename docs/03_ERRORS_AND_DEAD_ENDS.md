# ۳ · شکستها، باگها، بنبستها و خروجیهای ردشده

> هدف: **هیچ ایجنتی دوباره همین مسیرها را نرود.** هر مورد: «چه شد / چرا / حالا
> چکار کن». خطاهای حلشده هم آمدند تا علائمشان قابل تشخیص باشد.

## ۱) خروجیهایی که کاربر رد کرد (مهمترینها)

| خروجی | ایراد کاربر | تشخیص فنی | وضعیت |
|---|---|---|---|
| `543a20ba` تکفایل + پنلها | «**فاجعه**» | پوستهٔ شبیهساز گوشی با نوار وضعیت جعلی `9:41`، کادر دور دستگاه، پنلهای ادمین/بازبینی؛ صفحهٔ «درس» همان دموی چیدمان پروتوتایپ | جایگزینشد با `2042db0d` |
| همان بیلد، لایهٔ محتوا | «ساختار درسنامه و درس و سؤالات رو اصلاً متوجه نشدی… یه نمونهٔ خام فرانگشتانی… حتی پروتوتایپ هم همین مشکل رو داره» | پاراگراف «گاهی لازم است متنها را با شکستن خطوط…» = **دموی typography** بود، نه درسنامه؛ به هر درس با هش ID یک سؤال تصادفی از `QBANK` چسبانده میشد؛ هیچ سلسلهمراتب/پاسخنامه/ولیدیتور/ردیف پیشرفتی نبود | جایگزینشد با `9179b8c4` |

**درس آموخته:** طراح ظاهر ≠ محتوا. پروتوتایپ `v12.5-fa` عمداً صفحهٔ lesson را
برای تست شکستن خط ساخته؛ محتوای واقعی میمو در ۱۰٬۲۹۸ فایل `tutorial-*.json`
است (`ANALYSIS/MISSION_09/COMPLETE_LESSON_ENGINE_SPEC.md`).

## ۲) محدودیتهای محیط / ابزار (دوباره امتحان نکن)

| مانع | نتیجه | جایگزین انجامشده |
|---|---|---|
| emulator / ADB / KVM در sandbox | در دسترس نیست | اجراها از طریق GitHub Actions runner (M03–M09) |
| `workflow_dispatch` | ۴۰۴ روی شاخه | workflow جداگاهٔ path-scoped |
| M07 `Java.registerClass` / `dev.spawn` / API-36 defaults | شکست | هوک مستقیم `Activity/Fragment/WebView` در M09 (۱۸۱ هوک، ۷۲ entry واقعی) |
| `btn_lesson_close` | مسیر اشتباه | از M07 پرهیز شد |
| M08 reflection / pid-only observer | رد شد | hookهای هدفمند |
| `okhttp_missing TypeError`, `retrofit2=0` | نتوانستند URL زنده بگیرند | `ANALYSIS/MIMO_API_SURFACE.json` = استاتیک |
| `PaddleOCR` | هاستها مسدود | Tesseract (`libtesseract 5.5.3/fas`) |
| `rapidocr-onnxruntime` | نیازمند `libGL.so.1` | همان Tesseract |
| PEP 668 | نصب سیستمی ممنوع | venv در `/home/user/_work/ocr_venv` |
| `PIL` در `python3` سیستمی | ImportError | فقط venv بالا |
| CairoSVG / ImageMagick SVG→PNG | `libcairo` / delegate شکست | آیکونها مستقیماً PNG شدند |
| `chromium`/`firefox` سیستمی | نصب نیست | `@sparticuz/chromium` + `puppeteer-core` از npm، با `LD_LIBRARY_PATH=/tmp/al2023/lib:/tmp` (خارج از ریپو) |
| `jsonschema` | نصب نیست | ولیدیتور بدون وابستگی `app/tools/validate_content.py` |
| esbuild | بیلدر **رجیستری ماژول پایتون** است، نه esbuild | `app/tools/build_output.py` |
| Drive `unzip -o -q` | exit 2 / `BadZipFile` (آرشیو splitsشده) | PDF بازسازیشدهٔ `@BankBookkonkor (26)_extract.pdf`؛ دوباره دانلود/استخراج نکن |

## ۳) خطاهای کد که حل شدند (علائم برای آینده)

- `KeyError:'properties'` در ولیدیتور فرم → رفع.
- `DOMException: insertBefore` هنگام تزریق صفحات → ترتیب درج اصلاح شد.
- لیترال `</script` و `<!--` داخل اسکریپت inlined → بیلدر حالا assert میکند.
- `SOURCE_SLOT` دوبار تزریق میشد → دقیقاً یکبار.
- رگکس قرمزپوشانی broad، بیلدر را خراب کرد → **همان اسکریپت دوباره اجرا نشود**.
- M09 `%s/%d` TypeErrors خطوط ۱۵۷۱/۲۷۲۷ → رفع؛ توکن FB قرمزپوشانی شد؛
  ردپاهای خام M08 هنوز توکن تاریخی دارند (بایگانی).
- jsdom: getter `navigator`, import مطلق, خطای `//` → الگوی `tests/harness.mjs`.
- `.hexdigest()` → `.digest('hex')`؛ exam result / مخرج بانک؛ `GetTSVText()` → `GetTSVText(0)`.
- یک واژهٔ چینی تصادفی (معادل «وضعیت») وارد متن فارسی شده بود → حذف شد؛ `verify_docs.py` حالا CJK چک میکند.
- `verify_app.py` گم شده بود → restore.
- `store.get()` **فقط یک آرگومان** میگیرد و برای مسیر ناموجود `undefined` برمیگرداند؛
  `content-engine.js` اول `undefined` میگرفت و `.length` میترکید → تابع `read()` اصلاح شد.
- `proto-ui.js` در `go()` خطاهای `PROTO_NAV` را **بیصدا catch میکند**
  (`try{window.PROTO_NAV(name)}catch(e){}`)؛ پس باگهای هوک ناوبری در کنسول دیده
  نمیشوند → مستقیماً `window.PROTO_NAV(name)` صدا بزن تا خطا آشکار شود.
- تزریق اسکریپت Service Worker با `replace('</body>', …, 1)` داخل **رشتهٔ JS**
  باندل افتاد و `index.html` را با `SyntaxError` خراب کرد → حالا `rfind('</body>')`.
- `calc(100% - 2 * var(--sp-m))` با dimens تعریفنشده → عرض دکمه ۱۸۰px میشد؛
  با تعریف توکنها و `calc(100% - var(--sp-m) - var(--sp-m))` رفع شد.

## ۴) بنبستهای تحلیلی (نتایج منفی هم سنداند)

- M05 fixtureها سرفصل نبودند؛ M09 **ماتریس پاسخ درس اجرا نشد**
  (`reached_chapter=false`, `lesson_matrix_not_executed`).
- WebView: ۰ رویداد پل جاوااسکریپت؛ نام کلاس/متد interface، payload و callbackها
  `UNKNOWN` (`FINAL_UNKNOWN_REGISTER.md → U-WEB-001`). تنها رفتار اندازهگیریشده:
  گزینهٔ غلط `Q` → «Try again»، درست `D` → «Correct! / D O G».
- هیچ فرمول امتیاز/XP/پاداش، رتبه، همگامسازی یا `publishSetVersion` زندهای از
  سرور دیده نشد. `isSolvedCorrectly ≡ tries>=1` استاتیک/رانتایم M07 است.
- M08 چهار تب `Learn/Practice/Leaderboard/Profile` دید، ولی **محتوای
  Practice/Leaderboard/Profile مشاهده نشد** (`UNKNOWN`).
- آمار API: پایههای `api.mimo.org`, `api-testing.mimo.org`,
  `api-production.8-lives-cat.io`, `engine.api.gist.build` استاتیکاند؛
  کدام در رانتایم انتخاب میشود مشخص نشد.
- حسابرسی هدفپلاس: تک `AIzaSyBU…` = Firebase/Google Services (قرمزپوشانی)،
  `Bearer` = توکن کاربر، `/ZistAI/*` و `/Chatbot/*` روی
  `https://gateway.hadafplus.app`. **هیچ** کلید OpenAI/Gemini/Anthropic/GPT،
  `sk-…`، یا اثری دقیق از «شرکت یارانی / Yara / AvalAI / Liara».
  `gemini-flash-lite-latest` داخل `phone.html` فقط **برچسب پروتوتایپ** است،
  نه شاهد هدفپلاس. `ANALYSIS/MIMO_API_SURFACE.json` مربوط به **Mimo** است،
  نه هدفپلاس.
- `structure_book.py` قدیمی روی متن دوتستونی `GetTSVText()` → ۵۶۵ کاندیدای
  قاطی با `correctIndex:null`. جایگزین: `process_book.py` با word boxes.

## ۵) خطاهای پردازش محتوا (چرا کتاب وارد اپ نشد)

- OCR ۸۴۸ صفحه کامل است ولی میانگین اطمینان **۷۸٫۱**؛ نمونهٔ واقعی:
  «یافته» بهجای «یاخته»، «هغز استفوان» بهجای «مغز استخوان»، شمارهها و
  گزینهها در هم ریختهاند.
- پرسشنامهها در هر فصل شمارهشان از ۱ شروع میشود؛ پس شماره بهتنهایی کلید
  اتصال پاسخنامه نیست → join با همپوشانی واژهای متن عینی اضافه شد (۶۰۰/۶۰۸).
- با این حال `PROCESSED_DRAFT.json` همچنان `unreviewed` است و **عمداً وارد اپ
  نشده**؛ نشان دادنش همان اشتباه «نمونهٔ خام» را تکرار میکرد.
- `STARTER_PACKAGE.json` فقط ۲۰ سؤال/پاسخ موجود پروتوتایپ است (`placeholder`)؛
  `STRUCTURED_PACKAGE.json` همان جملهها را در سلسلهمراتب بومی میمو چیده
  (`structured`, `unreviewed`). هیچکدام «درسنامهٔ نهایی کتاب» نیستند.

## ۶) بستهبندی / توزیع

- `app/index.html` چندفایلهای است و با `file://` کار نمیکند (ESM محدود میشود)؛
  `sw.js` هم نیازمند `http(s)`. **همیشه `app/dist/Mimo.html` تحویل بده.**
- PWA نصبشدنی فقط روی HTTPS/localhost؛ `file://` بدون نصب هم کامل کار میکند.
- خروجی in-app خودش را base64 در `<head>` دارد؛ اگر `SLOT` دوبار تزریق شود یا
  `</script` داخل رشته بیاید، بیلد میشکند (چکهای بیلدر را نگه دار).
- `beforeinstallprompt` / «افزودن به صفحهٔ اصلی» فقط در مرورگر گوشی معنا دارد؛
  تست فیزیکی نصب PWA انجام **نشده**.

## ۷) مواردی که عمداً انجام نشدند

- نصب مدل زبانی / پروکسی سروری / کلید کاربر.
- اجرای کد کاربر در درسهای `executableFiles` (فقط مقایسهٔ `solvedContent`
  بهصورت آفلاین پیاده شد؛ اجرای واقعی `SERVER_DEPENDENT`).
- حذف «پاسخبرگ» قدیمی: به «پاسخبرگ» (گزینههای زدهشده) تغییر نام یافت و
  «پاسخنامه» دکمهای **جداگانه** شد.
- حذف تاریخچهٔ غلطها: صف مرور غلطها بعد از ۲ پاسخ درست `resolved` میکند ولی
  رکوردها باقی میمانند.
- `/max` و ۲۹ اکشن بکندی `LEARNHARNESS_ACTIONS.csv`: تب مکس ممنوع است.

بعدی: [`04_CURRENT_STATE.md`](04_CURRENT_STATE.md)
