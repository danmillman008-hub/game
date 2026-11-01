# ۰۵ج — مشخصات رندرر درس (قابل ساخت)

هدف: یک تیم مستقل بتواند از روی این سند، رندرر تعاملی را بسازد.

## ۱. خط لوله (pipeline)

```
payload JSON ──► DSLTokenizer ──► BlockTree ──► Layout ──► InteractionController
                     │                │             │              │
                 tokens+schema    code/text/    lists, RTL    chips, inputs,
                                  selection    handling      check/feedback
```

## ۲. مدل گره‌ها (AST)

```ts
type Node =
  | { k: "paragraph", visibleIf: "always"|"wrong"|"correct", spans: Span[] }
  | { k: "code", name: string, lang: Lang, version: 2, visibleIf: Vis,
      source: string, gaps: Range[], inputs: Range[], chips: string[] }
  | { k: "selection", multiple: boolean, isCode: boolean,
      items: { value: number, correct: boolean, spans: Span[] }[] }
  | { k: "webview", version: 2, style?: "embedded",
      interaction?: "feedback"|"unlock", visibleIf: Vis, html: string }
  | { k: "database", visibleIf: Vis, bootstrapSql: string,
      expected: { name: string, headers: string[], rows: string[][] }[],
      output?: string }
  | { k: "image", src: string, visibleIf: Vis }
  | { k: "break" } | { k: "strong"|"em", spans: Span[] }
type Range = { start: number, end: number }   // character offsets into source
```

## ۳. الگوریتم پارس (الزامی برای بازتولید دقیق)

1. بلوک کد = `<code>` دارای `codelang` یا `name`. (۷۳,۸۷۰ `<code>` درون‌خطی را رد کن.)
2. از بدنهٔ بلوک، ابتدا `<interactions>…</interactions>` را جدا کن (ترتیب ثابت نیست!).
3. `source` = الحاق `value` همهٔ `<text>`ها؛ `type="break"` ⇒ `"\n"`.
4. هر `<option startIndex endIndex/>` یک **جای خالی** است؛ `<option correct="false">` یک **چیپ انحرافی**.
5. `<interaction type="validatedInput" startIndex endIndex/>` یک ورودی آزاد است.
6. `<selection>` ⇒ آیتم‌ها با `value`/`correct`؛ `multiple` همیشه true.
7. `<database>` ⇒ `bootstrapScript` + `tables/table/header/row/data` + `output`.

## ۴. چیدمان و برهم‌کنش

| جزء | قاعده | اندازه |
|---|---|---|
| پاراگراف | فاصلهٔ بالا `lesson_description_margin_top 30dip` | — |
| بلوک کد | شعاع ۶dip، تب فایل در بالا، ارتفاع ۱۵sp متن | `lesson_codeblock_corner_radius` |
| جای خالی | یک «خانه» هم‌اندازهٔ زیررشته، چیپ‌ها در نوار پایین | عرض بازه: میانه ۴، صدک ۹۵ ۱۵ کاراکتر |
| ورودی آزاد | خانهٔ متنی راست‌چین در همان جای بازه | — |
| نوار چیپ | چیپ‌ها مخلوط، بعد از استفاده مصرف می‌شوند | تا ۱۲ بازه + تا ۵ انحرافی |
| دکمهٔ بررسی | پایین، ثابت | — |
| بازخورد | در محل خود بلوک، جای `p visible-if` | — |

## ۵. حالت‌ها و انتقال

```
UNANSWERED ──(پر شدن همهٔ جای خالی‌ها)──► READY_TO_CHECK ──(check)──┬─► CORRECT ──► [next lesson]
      ▲                                     ▲                     └─► WRONG ──► (ویرایش) ──► READY_TO_CHECK
      └──────────(پاک کردن چیپ)────────────┘
```
* `visible-if="wrong"` فقط در حالت `WRONG` رندر می‌شود و **با اولین ویرایش پاک نمی‌شود** تا
  کاربر دوباره بررسی کند (INFERRED از رشته‌های «try again»).
* `visible-if="correct"` در حالت `CORRECT`.

## ۶. دسترس‌پذیری و RTL (الزام محصول هدف، در Mimo نیست)

| موضوع | قاعدهٔ پیشنهادی |
|---|---|
| جای خالی | `contentDescription = "جای خالی ۲ از ۳"` + متن پاسخ فعلی |
| چیپ | اعلام «گزینه»، نه «دکمه» |
| متن RTL | پاراگراف راست‌به‌چپ، **کد چپ‌به‌راست** (مستقل از زبان) |
| اعداد | ارقام فارسی در متن، ارقام لاتین در کد |
| بازخورد | `liveRegion="polite"` روی ناحیهٔ بازخورد |

## ۷. کارایی

* ۲۱,۱۰۸ بلوک و میانهٔ ۱۰ درس در فصل ⇒ رندر تنبل (فقط درس جاری).
* `source` هر بلوک کوچک است (میانه در حد چند صد کاراکتر) ⇒ بدون streaming لازم.
* تصاویر با `src` نوع UUID ⇒ نیاز به جدول نگاشت `resourceId → drawable`.
