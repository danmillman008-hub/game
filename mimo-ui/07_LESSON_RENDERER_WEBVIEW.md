# ۰۷ — رندرر درس و ادیتور کد (کد واقعی WebView)

همهٔ فایلهای این بخش **عیناً** از `assets/` بسته کپی شدهاند در `SOURCE/assets/ui/`.
شواهد رسمی تحلیل آنها با CLI ریپوی `morluto/rea` در `REFERENCE/REA_EVIDENCE/JS_EVIDENCE.json`.

## ۱. `assets/lesson-webview.js` — پل ژست و اندازه (۸٬۱۸۹ بایت)

این فایل تزریقی به هر صفحهٔ درس است. سه جایگزین زمان ساخت/تزریق دارد:
`__MIMO_DOCUMENT_ID__`, `__MIMO_TOUCH_SLOP_CSS_PX__`, `__MIMO_FONT_SCRIPT__`.

**پروتکل پیام** (همهٔ انواع، بدون حذف):

| `kind` | فیلدها | معنی |
|---|---|---|
| `gesture` | `decision: 'ready'\|'web'\|'lesson'`, `startedAt` | مالکیت ژست بین ViewPager درس و محتوای وب |
| `activity` | `result: 'mimo.activity.correct'\|'wrong'\|'completed'` | نتیجهٔ تمرین تعاملی از iframe |
| `focus` | `focused: bool` | آیا `input/textarea/contentEditable` فocus دارد (برای کیبورد کد) |
| `height` | `height: int` | ارتفاع `body` + margin، برای `WebView` بادقت `Math.ceil` |

همهٔ پیامها از طریق `MimoLesson.postMessage(JSON.stringify({documentID, ...payload}))`
به سمت نیتیو میروند.

**منطق مالکیت ژست (دقیقاً همانطور که نوشته شده):**

- `pointerdown`/`touchstart` (capture, passive, فقط `event.isTrusted`) یک `gesture` تازه میسازد؛
  لمس چندگانه بلافاصله `web` اعلام میکند.
- `belongsToWeb(target)` بالا رفتن از `composedPath` تا `body`: `draggable=true`،
  `isContentEditable`، `input/textarea/select`، `touchAction` غیر از
  `auto|manipulation|pan-y|pan-up|pan-down`، یا عنصر scrollable → مالکیت وب.
- `iframe` بدون پل → حتماً وب (`claim()`)، تا تعویض درس رخ ندهد.
- `requestAnimationFrame` جهت حرکت را تعیین میکند: `dy > dx` → `lesson` (سوایپ درس)،
  در غیر این صورت `web`؛ آستانه `__MIMO_TOUCH_SLOP_CSS_PX__`.
- `Event.prototype.preventDefault` و `Element.prototype.setPointerCapture` **پوشانده شدهاند**
  تا جاهایی که کد درس جلوی رویداد نیتیو را میگیرد، مالکیت وب ثبت شود.
- `pointercancel` لمسی نادیده گرفته میشود (Chromium هنگام pan لغو میکند ولی لمس ادامه دارد)؛
  پاکسازی `gesture` در `requestAnimationFrame` بعد از آخرین move انجام میشود.
- `setupLayout()` viewport را `width=device-width, initial-scale=1, maximum-scale=1,
  user-scalable=no` میگذارد، `:root { color-scheme: light dark; }` تزریق میکند،
  فونتاسکریپت را میگذارد، `focusin/focusout` را گزارش میدهد و با
  `ResizeObserver` + `MutationObserver` + `load` + `document.fonts.ready` ارتفاع را میفرستد.
- فقط در frames بالا (`window === window.top`) گوشدهندهٔ `message` برای
  `mimo.activity.correct/wrong/completed` نصب میشود.

## ۲. `assets/lesson-webview-fonts.js` (۶۰۴ بایت)

۶ قانون `@font-face` میسازد: `Aeonik Pro` × {regular 400, medium 500, bold 700} ×
{normal, italic}، با `font-display: swap` و آدرس
`https://lesson.mimo.invalid/fonts/aeonik_pro_<face>_<variant>.otf`
(دامنهٔ `.invalid` نشان میدهد فونت توسط WebView/asset loader جایگزین میشود، نه از شبکه).

## ۳. استایل نحو کد — دو فایل، تفاوت کامل

`assets/styles/mimo_code_style.min.css` (روشن) و `mimo_code_style_dark.min.css` (تیره)
همان ۹ کلاس `hljs-*` با پالت جداگانهاند:

| کلاس | روشن | تیره |
|---|---|---|
| `.hljs` پسزمینه / متن | `#fff` / `#252746` | `#1d1f32` / `#fff` |
| کامنت | `#7a7ca6` | `#9293a2` |
| keyword / formula | `#bb6e8d` | `#f9bfd7` |
| literal / link / meta / symbol | `#226ec9` | `#86bdfe` |
| tag / attribute / section / regexp | `#cf4053` | `#f97f8d` |
| string / bullet | `#337a29` | `#97e58d` |
| title / class / built_in | `#b88e02` | `#fbdf83` |
| number / type / variable / attr | `#844a30` | `#db9f83` |
| doctag / strong | `#6e3ec8` | `#b99af4` |
| addition / deletion | `#337a29` / `#cf4053` | `#97e58d` / `#f97f8d` |

> نکتهٔ واقعی و جالب: در هر دو فایل چند تا تایپو وجود دارد (`hjls-meta-string`,
> `hjls-function`, `hlsj-selector-attr`) — چون اینها کد shipped هستند، عیناً حفظ شدهاند.

## ۴. باندلها و وابستگیها (همهٔ ۱۱ فایل JS)

| فایل | بایت | نقش |
|---|---|---|
| `lesson-webview.js` | ۸٬۱۸۹ | پل نیتیو ↔ وب (کد خود Mimo) |
| `lesson-webview-fonts.js` | ۶۰۴ | تزریق `@font-face` |
| `highlight.min.js` | ۴۳٬۷۴۲ | برجستهسازی نحو |
| `beautify/beautify.min.js` | ۷۴٬۴۹۶ | فرمت JS |
| `beautify/beautify-css.min.js` | ۲۰٬۴۲۹ | فرمت CSS |
| `beautify/beautify-html.min.js` | ۴۲٬۶۴۴ | فرمت HTML |
| `prettier/standalone.js` | ۱٬۰۵۸٬۹۳۵ | هستهٔ Prettier |
| `prettier/parser-babylon.js` | ۲۶۶٬۲۳۹ | پارسر JS |
| `prettier/parser-html.js` | ۱۱۰٬۶۷۸ | پارسر HTML |
| `prettier/parser-postcss.js` | ۳۵۱٬۸۲۶ | پارسر CSS |
| `spieglein/editor.bundle.js` | ۲٬۳۶۹٬۳۷۵ | ادیتور کد `Spieglein.init()` |

`prettier/index.html` چهار اسکریپت بالا را به ترتیب لود میکند؛
`spieglein/index.html` شامل `<div id="editor">`، Material Symbols و `Spieglein.init()` است.
۱۳ فایل `testdata/*.html` فیکسچرهای طلایی رندرر درساند (`127-0-1.html` … `641-4-9.html`).

## ۵. شواهد رسمی REA

`REFERENCE/REA_EVIDENCE/JS_EVIDENCE.json`: `evidence_id=ev_a3135ad9dd9a6441f057ed5dd2a23e3dd08c98780f79b2dc13953a0ea62f4a58`،
۳۳ فایل در موجودی، ۲ فایل JS پارسشده، ۱٬۱۸۶ گره AST، ۵۹ گره / ۶۵ یال گراف،
و ۸ محدودیت صریح (از جمله « eighteen inventoried files outside analysis scope» و
«اسکریپت inline در `spieglein/index.html` تحلیل نشد»). محدودیتها عیناً در `11` منعکس شدهاند.
