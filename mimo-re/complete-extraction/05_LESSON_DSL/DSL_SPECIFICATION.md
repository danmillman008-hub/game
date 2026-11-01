# ۰۵ — مشخصات کامل زبان درس (Lesson DSL)

**کلاس شواهد:** VERIFIED_STATIC (پارس کامل بستهٔ انگلیسی: ۲۰,۳۰۶ سند درس).
اعداد این سند در این فاز **دوباره اندازه‌گیری** شد و با گزارش قدیمی متفاوت است (بخش ۷).

## ۱. ساختار کلی سند

هر درس تعاملی یک رشتهٔ HTML-مانند است که **سه لایه** دارد:

```
<!DOCTYPE html><html><body>
    ┌─ لایهٔ ۱: محتوای غنی
    │  <p>متن …</p> <p visible-if="wrong">بازخورد خطا …</p>
    │  <strong>/<em>/<br>/<img src="…" />/<a href="…">
    ├─ لایهٔ ۲: بلوک کد
    │  <code version="2" codelang="html" name="index.html" visible-if="always">
    │     <content>  ← توکن‌های از پیش شکسته‌شده (syntax highlighting سمت محتوا)
    │        <text value="&lt;h1&gt;" class="keyword" />
    │        <text type="break" />               ← خط جدید
    │     </content>
    │     <interactions>
    │        <interaction type="fillTheGap" isDefault="true">
    │           <options>
    │              <option startIndex="70" endIndex="78" />                ← جای خالی صحیح (بازهٔ توکن)
    │              <option correct="false"><content><text value="&lt;p&gt;" /></content></option>  ← گزینهٔ انحرافی
    │           </options>
    │        </interaction>
    │        <interaction type="validatedInput" isDefault="true" startIndex="108" endIndex="113" />
    │     </interactions>
    │  </code>
    ├─ لایهٔ ۳: بلوک‌های تعاملی دیگر
    │  <selection iscode="false" multiple="multiple">
    │     <item value="1" correct="true">…</item><item value="2" correct="false">…</item>
    │  </selection>
    │  <webview version="2" style="embedded" visible-if="always" interaction="feedback"
    │           content="&lt;!doctype html&gt;…" />   ← HTML داخل attribute، escape شده
    │  <database visible-if="always" bootstrapScript="CREATE TABLE …; INSERT …;">
    │     <tables><table name="Friends"><header content="name" /><row><data content="…" /></row></table></tables>
    │     <output>…</output>
    │  </database>
</body></html>
```

## ۲. هستان‌شناسی ۲۷ تگ (شمارش واقعی)

| خانواده | تگ‌ها | تعداد عنصر (open) |
|---|---|---|
| پوشش سند | `html`, `body`, `head`, `style` | ۲۰,۳۰۷ سند |
| متن | `p`, `strong`, `em`, `br`, `a`, `img` | ۴۳,۸۰۵ / ۱,۲۸۳ / ۴۳۷ / ۲۱۸ / ۲ / ۱۴۳ |
| کد | `code`, `content`, `text` | ۹۴,۹۷۸ / ۴۱,۲۲۱ / ۳۶۹,۱۰۷ |
| سنجش جای خالی | `interactions`, `interaction`, `options`, `option` | ۱۱,۷۲۹ / ۱۱,۷۲۹ / ۹,۹۵۷ / ۴۳,۹۶۳ |
| سنجش انتخاب | `selection`, `item` | ۷,۳۵۶ / ۲۰,۲۴۸ |
| پیش‌نمایش | `webview` | ۹۳۰ |
| پایگاه داده | `database`, `tables`, `table`, `header`, `row`, `data`, `output` | ۵۷۴ / ۵۷۴ / ۱,۲۸۷ / ۳,۱۶۸ / ۵,۲۲۰ / ۱۰,۴۷۴ / ۵,۷۸۴ |

جزئیات هر تگ/attribute در `BLOCK_REFERENCE.md` و فایل‌های `DSL_*.csv`.

## ۳. قانون طلایی: اندیس‌ها **آفست کاراکتر** روی متن بازسازی‌شده‌اند

> این بخش در میانهٔ کار **اصلاح شد**. فرض اولیهٔ «اندیس توکن» با اعتبارسنجی روی ۲۰,۳۰۶ سند رد شد
> (۸۶۸ نقض محدوده). تاریخ خطا در `SEMANTICS_CORRECTION.md` ثبت شده است.

```
source = concat(value of every <text> in <content>, with "\n" for <text type="break"/>)
بازهٔ [startIndex, endIndex) = source[startIndex:endIndex]        (۰-پایه، نیم‌باز)
```

* متنِ گزینهٔ صحیح = همان زیررشتهٔ `source` (بدون trim).
* `text type="break"` **یک کاراکتر `\n`** مصرف می‌کند.
* گزینه‌ها و ورودی‌ها همیشه در ۲۹,۰۹۳ بازهٔ صحیح + ۱,۷۷۲ بازهٔ `validatedInput`:
  همه در محدودهٔ `len(source)` بودند **پس از اصلاح** (۰ نقض؛ `DSL_VALIDATION_REPORT.json`).
* عرض بازه: میانه **۴ کاراکتر**، صدک ۹۵ = **۱۵**، بیشینه ۶۰ (`</button>`، `console.log(...)`).

### چند جای خالی در یک بلوک

یک `<interaction type="fillTheGap">` می‌تواند **چند** بازهٔ `<option startIndex endIndex/>` داشته باشد
(مثال واقعی: `<h1>Level 1</h1>` با سه بازهٔ ۰–۴، ۴–۱۱، ۱۱–۱۶).
توزیع تعداد جای خالی در ۲۱,۱۰۸ بلوک کد:

| جای خالی | بلوک |
|---|---|
| ۰ (فقط نمایش کد) | ۱۱,۱۵۱ |
| ۱ | ۱,۸۷۰ |
| ۲ | ۲,۲۷۹ |
| ۳ | ۲,۷۷۴ |
| ۴ | ۱,۶۸۲ |
| ۵ | ۸۰۹ |

⇒ مدل درست: `Block { gaps: Gap[] , distractors: string[] }`، نه «یک جای خالی + گزینه‌ها».

## ۴. مدل سنجش (چهار مکانیزم، یک قرارداد)

| مکانیزم | تگ | ورودی کاربر | معیار درستی | بازخورد |
|---|---|---|---|---|
| `fillTheGap` | `interaction type="fillTheGap"` | پر کردن هر جای خالی از میان چیپ‌ها | `source[g] == chip` برای همهٔ جای خالی‌ها | `p visible-if="wrong"` |
| `validatedInput` | `interaction type="validatedInput"` | تایپ آزاد در بازه | `equals(source[s:e], input)` | همان |
| `selection` | `selection` + `item` | انتخاب چندگانه | مجموعهٔ انتخاب‌شده = مجموعهٔ `correct="true"` | همان |
| `database` | `database` + `output` | نوشتن/اجرای SQL | مقایسهٔ ساختاری نتیجه با `tables` | — |

**چیپ‌ها از کجا می‌آیند؟** مجموعهٔ چیپ‌ها = همهٔ بازه‌های صحیح (۲۹,۰۹۳) + گزینه‌های انحرافی
(۱۴,۸۷۰) که با هم مخلوط می‌شوند. این توضیح می‌دهد چرا گزینهٔ انحرافی در همان `<options>`
تعریف شده است: **همان استخر چیپ**.
## ۵. قرارداد `visible-if`

| مقدار | معنا | فراوانی (بستهٔ انگلیسی) |
|---|---|---|
| `always` | همیشه (در `code`/`webview`/`img`/`database`) | ۱۷,۴۷۶ + ۷۶۸ + ۱۳۹ + ۵۷۴ |
| `wrong` | فقط وقتی پاسخ همان بلوک نادرست شد | ۱۹,۱۰۱ (روی `p`) |
| `correct` | فقط وقتی درست شد (توضیح تکمیلی) | ۸۵ (روی `p`) + ۸۸ (روی `webview`) |

هیچ مقدار دیگری مشاهده نشد ⇒ دامنه **بسته** است (VERIFIED_STATIC، HIGH).

## ۶. بلوک کد: توکن‌های از پیش رنگ‌آمیزی‌شده

`<text class="…">` فقط در ۱,۹۴۱ مورد کلاس دارد (بقیه خام). دامنهٔ کلاس‌ها:
`string` ۵۸۸، `keyword` ۵۲۳، `name` ۲۸۳، `number` ۲۱۶، `built_in` ۱۲۱، `attr` ۶۸،
`attribute` ۶۷، `selector-class` ۲۷، `literal` ۲۵، `meta` ۲۰، `selector-tag` ۳.

⇒ رنگ‌آمیزی **در زمان تألیف** انجام شده، نه در کلاینت. کلاینت فقط کلاس→رنگ نگاشت می‌کند
(۹ رنگ نحو در `03_UI_UX/DESIGN_SYSTEM.md`). این تصمیم، هم‌خوان با الزام «بازیکن بدون پارسر زبان» است.

## ۷. بازاندازه‌گیری در برابر گزارش قدیمی (تفاوت‌ها توضیح داده می‌شود)

| سنجه | گزارش قدیمی | اندازه‌گیری امروز | توضیح |
|---|---|---|---|
| تگ‌های DSL | ۲۶ | **۲۷** | `head`/`style` در گزارش قدیمی یکجا شمرده شده بود |
| `<text>` | ۲۳۵,۹۷۳ | **۳۶۹,۱۰۷** | قدیمی فقط `interactiveContent`؛ امروز `interactiveContent` + `hardModeContent` |
| گزینهٔ جای خالی | ۱۷,۵۲۶ | **۲۹,۰۹۳ بازهٔ صحیح + ۱۴,۸۷۰ انحرافی** | تفکیک «بازه» از «گزینهٔ انحرافی» قبلاً انجام نشده بود |
| `visible-if=wrong` / `correct` | ۱۳,۰۴۳ / ۱۴۳ | **۱۹,۱۰۱ / ۱۷۳** | همان دلیل دامنهٔ اسکن |
| جای خالی (بازه) | ۱۷,۵۲۶ | **۲۹,۰۹۳** | جمع `option startIndex` در همهٔ بلوک‌ها |
| سند درس | — | **۲۰,۳۰۶** (= ۱۴,۲۴۸ تعاملی + ۶,۰۵۸ نسخهٔ سخت) | انطباق کامل با شمارش `contentType` |

**اقدام:** اعداد قدیمی در `MIMO-REPORT.md` بازنویسی **نمی‌شوند**؛ این سند منبع معتبر جدید است.

## ۸. فیکسچر و آزمون

`fixtures/` شامل ۴ سند کوچک **تألیف‌شده توسط ما** (نه کپی محتوا) و `TEST_VECTORS.md` شامل
۲۴ بردار آزمون است. اجرای آزمون‌ها: `cd 16_TESTS && pytest -q` (همه سبز، بخش ۱۶).
