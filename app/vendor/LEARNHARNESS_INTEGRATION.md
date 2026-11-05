# اتصال LearnHarness به بخش «هوش مصنوعی»

**مخزن:** https://github.com/amosblomqvist/learnharness.git
**commit پینشده:** `713377f366771e3e4730e6acd1bc290e0ebc6d6e` (کلون `depth=1`، ۲۰۲۶-۱۱-۰۵)
**لایسنس:** **AGPL-3.0-only** — لایسنس کامل در `https://github.com/amosblomqvist/learnharness/blob/main/LICENSE`.
**نسخهٔ اپ:** 0.5.0 ·نسخهٔ اپ:** 0.5.0 · «An agent harness for learning».

> این سند، همراه `app/src/harness.js`، **قرارداد اتصال** است. کد منبع LearnHarness
> بهصورت کامل در این ریپو vendored نشده (۷۴۵KB فایلهای Next.js/Electron + وابستگیها)،
> چون اپ ما یک PWA آفلاین بدون بکاند است. بهجای آن، **همان معماری آموزشی** با
> یک ارائهدهندهٔ محلی پیادهسازی شده و قرارداد ارائهدهندهٔ خارجی مستند شده است.

## آنچه واقعاً از LearnHarness گرفته شد (وصل شد)

| مفهوم LearnHarness | پیادهسازی در اپ ما |
|---|---|
| Measure → Plan → Teach → Practice (۴ فاز README) | `harness.js`: `measure/plan/teach/practice` با همان نامها و همان ترتیب |
| «thinking fields» / پاسخ + اطمینان | فیلد `confidence` و `reasoning` در رکورد جلسه، ذخیره در `store.ai.harness` |
| Knowledge graph (گزارهها + زنجیرههای استدلال + لینک به جلسه) | `graph.propositions[]` با `sourcePage`، `links[]`، `sessionId`؛ فقط از محتوای موجود در فرم ساخته میشود |
| Practice جدا از Teach، بدون نامبردن مستقیم مبحث | `buildPracticeSession('topic', …)` از `exam-template.js` |
| «Your keys, your data» / ذخیرهٔ لوکال | `localStorage` اپ؛ هیچ کلید/توکن/درخواست شبکهای وجود ندارد |
| قابل مشاهدهبودن رفتار | `harness.getStatus()` و سطر وضعیت در صفحهٔ AI |

## آنچه **وصل نشده** (صادقانه)

- **هیچ مدل زبانی اجرا نمیشود.** LearnHarness برای اجرا به provider نیاز دارد
  (API key، Claude Code CLI، یا endpoint سازگار با OpenAI). READMEاش صریحاً میگوید
  «Local storage does not mean offline processing». اپ ما آفلاین و بدون بکاند است.
- بنابراین ارائهدهندهٔ پیشفرض **`LocalContentProvider`** است: هیچ متن، توضیح،
  پاسخ یا حدسی تولید نمیکند؛ فقط درسها و تستهای **موجود در
  `MIMO_INFORMATION_FORM.json`** را انتخاب و مرتب میکند. وقتی بستهٔ محتوا خالی است،
  پیام «منبعی ثبت نشده» برمئیگردد، نه پاسخ ساختگی.
- کامپوننتهای UI ریپو (۸۴ فایل TSX، Electron، `@xyflow/react`، …) پورت نشدند؛
  ظاهر بخش AI همان طرح تأییدشدهٔ v12.5-fa باقی ماند (از قبل بر اساس اسکرینشاتهای
  LearnHarness در `DESIGN/REFERENCE/` طراحی شده بود).

## قرارداد ارائهدهنده (برای وصل کردن اپ واقعی در آینده)

```js
// app/src/harness.js — Provider interface, بدون هیچ fetch در پیادهسازی پیشفرض
{
  id: 'local-content',              // یا 'learnharness-openai-compatible'
  status: 'ready' | 'not-configured',
  capabilities: ['select-lesson','select-question','graph'],  // نه 'generate-text'
  measure(goal, ctx), plan(measurement, ctx), teach(step, ctx), practice(plan, ctx)
}
```

برای اتصال واقعی: باید یه بکاند/endpoint و کلید توسط **کاربر** تنظیم شود،
سرویسدهنده آن را پروکسی کند (هیچ کلیدی در مرورگر/گیت ذخیره نمیشود)، و
`SERVER CONFIRMED` همچنان ۰ بماند تا زمانی که واقعاً تأیید شود. تا آن موقع،
وضعیت در UI دقیقاً «ارائهدهندهٔ خارجی پیکربندی نشده · موتور محلی فعال» است.

## اسناد بالادستی

`README.md`, `docs/architecture.md`, `docs/getting-started.md` در کلون
`/home/user/_work/learnharness/` (خارج از گیت) قابل مطالعهاند. تغییرات ما در
`app/src/harness.js` مستقلاند و کدی از آن ریپو کپی نشده است؛ بنابراین لایسنس
AGPL صرفاً بابت **ارجاع معماری و attribution** اینجا ذکر شد.
