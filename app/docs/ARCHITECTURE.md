# معماری اپلیکیشن آفلاین

## اصل حاکم

**طرح تأییدشده تغییرناپذیر است؛ کد قابل بازنویسی است.** بنابراین لایهٔ «دارایی طرح»
از لایهٔ «منطق محصول» جدا شده و هیچ فایلی در `mimo-ui/UPGRADE/` ویرایش نشده است.

```
┌──────────────────────────────────────────────────────────────┐
│ DESIGN ASSETS (کپی بایتبهبایت، فقط خواندنی)                    │
│ proto.css · phone.html · proto-data.js · PROVENANCE.json      │
│ مبدأ: mimo-ui/UPGRADE/DESIGN/index.html (v12.5-fa, c356…)     │
└───────────────┬──────────────────────────────────────────────┘
                │ درج عینی در index.html
┌───────────────▼──────────────────────────────────────────────┐
│ RENDERER  proto-ui.js (کپی کاری + ۶ وصلهٔ مستند)              │
│ آیکونها، ۱۳ صفحهٔ تأییدشده، ویجت آزمون، تمرین مبحث، چت       │
│ وصلهها: null-guard کروم پروتوتایپ، hook ناوبری/ذخیره،        │
│         export کردن window.PROTO                             │
└───────────────┬──────────────────────────────────────────────┘
                │ window.PROTO_NAV / PROTO_PERSIST / PROTO
┌───────────────▼──────────────────────────────────────────────┐
│ APPLICATION CONTROLLER  src/app.js                           │
│ بوت/بازیابی، رویدادها، سه مسیر، وضعیت آزمون، انیمیشن        │
└───────┬───────────────┬──────────────┬───────────────────────┘
        │               │              │
┌───────▼─────┐ ┌───────▼──────┐ ┌─────▼───────────────────────┐
│ src/store.js│ │ src/engine.js│ │ src/routes.js / views.js     │
│ localStorage│ │ منطق خالص   │ │ ۳ مسیر + ماشین وضعیت + نماها │
│ اسکیما v1   │ │ (DOM-free)  │ │ (کامپوننتهای تأییدشده)      │
│ مهاجرت/امن  │ │              │ │                              │
└─────────────┘ └───────┬──────┘ └──────────────────────────────┘
                        │
                ┌───────▼───────┐
                │ src/fixtures.js│  دادهٔ آزمایشی جدا از محتوای نهایی
                └───────────────┘
```

## چرا کپی کاری `proto-ui.js`؟

رندرر پروتوتایپ تمام آیکونهای وکتوری، هندسهٔ گرهها، ۲۰ سؤال نمونه، ویجتهای
آزمون و تعاملات تأییدشده را دارد. بازنویسی کامل آن ریسک تغییر ناخواستهٔ طراحی
را بالا میبرد. بهجای آن، روی **یک کپی کاری** شش وصلهٔ کوچک و مستند اعمال شد
(اسکریپت `tools/extract_from_prototype.py`، قابل تکرار و idempotent):

1. `q("#themeBtn")` → guard (پوستهٔ محصول کروم پروتوتایپ را ندارد).
2. `q("#dirBtn")` → guard.
3. `go(name)` → `window.PROTO_NAV(name)` برای ذخیرهٔ آخرین صفحه.
4. `saveExam()` → `window.PROTO_PERSIST(SAVED)` برای ذخیرهٔ پایدار آزمون.
5. دو محل `SAVED=null` → پاک کردن اسنپشات ذخیرهشده.
6. `window.PROTO = {…}` → API رندرر برای کنترلر (`go`, `toast`, `paintIcons`,
   `questions`, `examState`, `setSaved`, `resumeExam`, `renderPractice`).

`proto.css`، `phone.html` و `proto-data.js` **هیچ وصلهای ندارند** و بایتبهبایت با
مبدأ برابرند ( tests/fidelity تست میکنند).

## صفحات جدید، بدون طراحی جدید

`src/views.js` در زمان اجرا سه سطح را به DOM اضافه میکند تا `phone.html` عیناً
دستنخورده بماند: `study-plan`، `practice-bank`، `settingsModal`، چیپهای مسیر در
`select-path`، چیپهای نماهای لیدربورد، و ورودی بانک سؤال در `exam-hub`.
همه از کلاسهای موجود (`.sp-top`, `.sd-hero`, `.chips/.chip`, `.selfbox`,
`.selfrow`, `.sp-q/.sp-opt`, `.banner.warn`, `.modal-card`, `.plink`, `.lb-row`)
و همان متغیرهای CSS استفاده میکنند. `motion.css` فقط `transition`/`@keyframes`
اضافه میکند و هیچ رنگ یا فونت hard-coded ندارد.

## اسکیمای وضعیت (store v1)

| شاخه | محتوا |
|---|---|
| `identity` | کاربر مهمان محلی، بدون حساب/توکن |
| `meta` | `offlineOnly:true`, `serverConfirmed:false`, `placeholderContent:true` |
| `economy` | سکه، کلید، streak، xp، تعداد آزمونها (مقادیر بذر پروتوتایپ) |
| `settings` | تم، RTL، صدا، لمس، کاهش انیمیشن، هدف روزانه |
| `route` | `mode` ∈ `{direct, exam, study-plan}`, `pathId`, `studyPlan` |
| `progress` | `lessonRows[]` با فیلدهای M09، `chapterCompletions`, `tutorialCompletions`, `unlocks` |
| `exam` | `saved` (اسنپشات)، `status`, `activeKind`, `results[]` |
| `practice` | `sessions[]`, `active`, `bankCursor` |
| `leaderboard`, `ai` | نما و گفتگوی محلی |
| `navigation` | آخرین `screen`/`tab` + تاریخچهٔ ۲۰تایی |
| `syncQueue` | صف محلی بادوام (تصمیم معماری مستقل؛ هیچ حملونقلی وجود ندارد) |

`createStore(storage)` قابل تزریق است؛ در Node با `memoryStorage()` تست میشود.
`migrate()` کلیدهای ناشناخته را حذف، JSON خراب را تحمل، نسخه را ارتقا و فلگهای
قابلیت (`meta`) را هر بار از مقادیر امن بازسازی میکند.

## مرز شواهد M09 (فقط مرجع خواندنی)

| برچسب | معنا | نمونه در کد |
|---|---|---|
| `VERIFIED` | مشاهدهٔ runtime/static در M07/M08/M09 | `isSolvedCorrectly ≡ tries>=1`، شکل ۱۱فیلدی `LessonProgress`، `publishSetVersion=753`، `selection == all(selected==isCorrect)`، `fillTheGap/spell == ordered equality`، ۵ تب `NavigationBar.setActive` |
| `SHAPE_ONLY` | فقط شکل داده مستند است | `chapterCompletion()` از ردیفهای محلی |
| `DESIGN_CHOICE` | قانون مستقل ما، **ادعایی دربارهٔ میمو نیست** | قفل ترتیبی، امتیازدهی جلسه، جوایز، صف همگامسازی، ماشین مراحل برنامه |

موارد `INFERRED` / `UNKNOWN` / وابسته به سرور مطلقاً بهعنوان رفتار قطعی میمو
ارائه نشدهاند: فرمول پاداش، رتبهبندی سروری، ack صف، WebView درس، سیاست واقعی
باز کردن قفلها، احراز هویت و هر پاسخ `/v1/` وجود ندارند. `SERVER CONFIRMED=0`.

## آفلاین بودن

هیچ `fetch` / `XMLHttpRequest` / `WebSocket` در کد محصول نیست. `server.js` فقط
فایل استاتیک سرو میکند (هیچ API، پروکسی یا بکاندی ندارد). `sw.js` تنها برای
درخواستهای `GET` همان مبدأ، ابتدا شبکه و سپس کش را امتحان میکند تا پوسته بعد
از قطع ارتباط هم بالا بیاید.
