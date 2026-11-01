# ۰۵ب — مرجع بلوک‌ها (هر تگ: کارکرد، attributeها، الزام رندر، نوع داده)

فراوانی‌ها = تعداد عنصر در بستهٔ انگلیسی (open tag). منبع: `DSL_TAG_CENSUS.csv`.

## ۱. پوشش

| تگ | n | الزام رندرر | یادداشت |
|---|---|---|---|
| `html`,`body` | ۲۰,۳۰۷ | wrapper | بدون attribute؛ باید تحمل شود |
| `head`,`style` | ۱ | نادیده گرفتن امن | فقط در ۱ سند؛ CSS درون‌خطی مجاز نیست |
| `p` | ۴۳,۸۰۵ | پاراگراف | تنها تگ متنی که `visible-if` می‌گیرد |
| `strong`,`em` | ۱,۲۸۳ / ۴۳۷ | تأکید | semantics دسترس‌پذیر |
| `br` | ۲۱۸ | شکست خط | self-closing |
| `a` | ۲ | لینک | ۲ نمونه؛ در محصول جدید بهتر است ممنوع/کنترل‌شده باشد |
| `img` | ۱۴۳ | تصویر از منابع بسته | `src` گاهی **UUID** است نه مسیر (`5d5e1f86-…`) ⇒ جدول نگاشت لازم |

## ۲. کد

| تگ | n | attributeها | الزام رندرر |
|---|---|---|---|
| `code` (بلوک) | **۲۱,۱۰۸** | `version=2`, `codelang`, `name`, `visible-if` | تب فایل + ادیتور/نمایش |
| `content` | ۴۱,۲۲۱ (۲۱,۱۰۸ بدنهٔ کد + ۱۴,۸۷۰ گزینهٔ انحرافی + …) | — | نگهدارندهٔ توکن‌ها |
| `text` | ۳۶۹,۱۰۷ | `value`, `type=break`, `class` | توکن؛ `break` = خط جدید |

* `codelang` ∈ {html 5,245 · javascript 5,037 · python 3,575 · jsx 3,028 · css 2,353 · sql 694 · swift 644 · typescript 245 · bash 186 · none 61 · text 40}
* `name` ۳۳۹ مقدار متمایز؛ ۲۰ پرتکرار: `index.html` 5,154 · `script.js` 4,174 · `script.py` 3,155 · `style.css` 2,263 · `index.jsx` 1,337 · `App.jsx` 795 · `script.sql` 694 · `main.swift` 643 · `app.js` 549 · `script.ts` 243 …
* مسیرهای پوشه‌ای هم وجود دارد (`order_tools/validation.py`) ⇒ رندرر باید درخت فایل را پشتیبانی کند.

## ۳. سنجش جای خالی

| تگ | n | attributeها | معنا |
|---|---|---|---|
| `interactions` | ۱۱,۷۲۹ | — | نگهدارنده |
| `interaction` | ۱۱,۷۲۹ | `type`, `isDefault=true`, `startIndex`, `endIndex` | `fillTheGap` ۹,۹۵۷ (دارای `<options>`) / `validatedInput` ۱,۷۷۲ (self-closing) |
| `options` | ۹,۹۵۷ | — | فقط برای `fillTheGap` |
| `option` (بازه) | ۲۹,۰۹۳ | `startIndex`, `endIndex` | جای خالی صحیح = **آفست کاراکتر** روی `source` |
| `option` (انحرافی) | ۱۴,۸۷۰ | `correct=false` + `<content>` | گزینهٔ نادرست با محتوای غنی |

**قاعده (اصلاح‌شده):** یک `fillTheGap` = یک **استخر گزینه** برای **چند** جای خالی.
توزیع تعداد جای خالی بر ۲۱,۱۰۸ بلوک: ۰→۱۱,۱۵۱ · ۱→۱,۸۷۰ · ۲→۲,۲۷۹ · ۳→۲,۷۷۴ · ۴→۱,۶۸۲ ·
۵→۸۰۹ · ۶→۳۶۵ · ۷→۱۰۰ · ۸→۵۱ · ۹→۱۱ · ۱۰→۸ · ۱۱→۳ · ۱۲→۵.
مجموع بازه‌های صحیح ۲۹,۰۹۳ و انحرافی ۱۴,۸۷۰ ⇒ چیپ‌ها از هر دو ساخته می‌شوند.

## ۴. انتخاب چندگانه

| تگ | n | attributeها | معنا |
|---|---|---|---|
| `selection` | ۷,۳۵۶ | `multiple=multiple`, `iscode` | همه `multiple` هستند (۷,۳۵۶/۷,۳۵۶) |
| `item` | ۲۰,۲۴۸ | `value` (۰..۶), `correct` | دقیقاً ۱ گزینهٔ درست در هر بلوک (۷,۳۵۶) |

`iscode` فقط ۶۱ نمونه `true` دارد ⇒ متن گزینه‌ها معمولاً غنی (شامل `<code>` درون‌خطی).

## ۵. پیش‌نمایش WebView

| attribute | مقادیر | معنا |
|---|---|---|
| `version` | `2` (همه) | نسخهٔ قرارداد پل JS |
| `style` | `embedded` (۲۸۶) | ارتفاع درون‌خطی |
| `interaction` | `feedback` ۷۵ · `unlock` ۲۶ | **نقطهٔ کلیدی**: پیش‌نمایش می‌تواند شرط پیشرفت باشد |
| `content` | HTML escape‌شده | مقادیر واقعی: ۱۴ نمونهٔ کوچک («Hello, world»…) + HTML کامل |

`interaction="unlock"` یعنی کاربر باید در پیش‌نمایش تعامل کند تا بلوک باز شود (INFERRED، شاهد
نام + `addJavascriptInterface`). این تنها جایی است که درس به **کد اجراشده در کلاینت** نیاز دارد.

## ۶. پایگاه داده (درس SQL)

| تگ | n | attributeها | معنا |
|---|---|---|---|
| `database` | ۵۷۴ | `bootstrapScript`, `visible-if` | اسکریپت seed (`CREATE TABLE` + `INSERT`) |
| `tables` | ۵۷۴ | — | نتیجهٔ مورد انتظار |
| `table` | ۱,۲۸۷ | `name` (۷۷ نام: `Result`, `students`, `enrolled`…) | یک جدول نتیجه |
| `header` | ۳,۱۶۸ | `content` | نام ستون |
| `row` | ۵,۲۲۰ | — | ردیف |
| `data` | ۱۰,۴۷۴ | `content` | سلول |
| `output` | ۵,۷۸۴ | متن | خروجی متنی (برای دستورهای غیر SELECT) |

⇒ اجرای SQL در کلاینت (SQLite با seed) و مقایسهٔ ساختاری نتیجه با `tables` انجام می‌شود.
شاهد اضافی: `sourceDatabaseTables`/`solutionDatabaseTables` در درس‌های کدی.

## ۷. بلوک‌های جدید لازم برای محصول هدف (NEW)

| بلوک | چرا Mimo ندارد | طرح پیشنهادی |
|---|---|---|
| `math` | محتوای Mimo برنامه‌نویسی است | LaTeX با KaTeX در WebView، fallback SVG |
| `diagram` | — | SVG + برچسب تعاملی |
| `grammar` | — | متن راست‌به‌چپ + اعراب |
| `audio` | — | پخش + سنجش تلفظ (اختیاری) |
| `figure` (شکل کنکوری) | — | تصویر برداری + نقاط قابل کلیک |
