**REVIEW — MISSION 02.** اعداد این سند **همگی از بایتکد `classes.dex` استخراج شدهاند**؛
هیچکدام از اجرای واقعی برنامه بهدست نیامدهاند (`RUNTIME VERIFIED` = ۰).
دادهٔ مرجع همان shipped **v753** است؛ fixture v52 استفاده نشد. ثابتها در `PATH_GEOMETRY_CONSTANTS.json`.

---

# LEARNING_PATH_GEOMETRY — الگوریتم و اعداد واقعی مسیر

## ۱. آنچه *جدید* کشف شد (نسبت به مرحلهٔ ۱)

| یافته | شاهد | وضعیت |
|---|---|---|
| حلقهٔ ساختوضعیت گره درون `GetPathMapState$invoke$3::invokeSuspend` | `getSections()` @`0x9a9240`، `getTutorials()` @`0x9a927e`، `getType()` @`0x9a92f4`، `isRequired()` @`0x9a93e6`، **`isCompleted()` @`0x9a940c`**، `getIconBanner()` @`0x9a9434`، `getTitle()` @`0x9a943c`، `getChapters()` @`0x9a9444` | `OBSERVED/HIGH` |
| اتصال مسیر به Repository اتمام | `GetPathMapState$invoke$2::invokeSuspend` → `Lcom/getmimo/data/source/local/completion/a;->a(Track,…)` @`0x9a8f9c` | `OBSERVED/HIGH` |
| **۱۴۶ ثابت عددی** در ۱۱ کلاس `ui/path/map` (عمدتاً `Lcom/getmimo/ui/path/map/k;` = کامپوزابل R8شدهٔ `Views.kt`) | `PATH_GEOMETRY_CONSTANTS.json` | `OBSERVED/HIGH` |
| مقادیر `dp`مانند همراه مصرفکنندهٔ Compose | جدول §۳ | `OBSERVED` (عدد) / `STATICALLY INFERRED` (نقش) |

## ۲. ترتیب و ساختار گرهها — `OBSERVED` (داده v753)

همان ۱۹ مسیر / ۱۴۴ section / ۲٬۰۰۲ ارجاع tutorial / ۶ نوع
(`course`, `practiceRequired`, `practiceOptional`, `guidedProject`, `guidedProjectOptional`, `challenges`)
و **۰ نقض پیوستگی** `startIndex/endIndex` که در `LEARNING_PATH_ENGINE.fa.md` ثبت شد.
بیتازگی: حلقهٔ بالا **مستقیماً** `Track.getSections()` و `Track.getTutorials()` و
`Tutorial.isCompleted()` / `TutorialType.isRequired()` را میخواند — یعنیوضعیت گره از
همان مدل shipped ساخته میشود، نه از جدول جداگانهای. **`UNKNOWN`:** نگاشت دقیق
`type` + `isCompleted` + `isRequired` → رنگ/آیکون/قفل و ترتیب `if`ها در ۷۱ دستورالعمل
Ghidra برای `invoke$3` همچنان بازسازی نشده است.

## ۳. اعداد هندسی استخراجشده (همه `classes.dex`)

| مقدار (float32) | آفست دستورالعمل | متد | فراخوانی بلافاصله بعد | تفسیر |
|---|---|---|---|---|
| `4.0`, `6.0`, `12.0`, `3.0` | `0xab67c0`, `0xab67cc`, `0xab67f4`, `0xab6800` | `k;->v(...)` | `Lu3/c;->i0(F)F` | `STATICALLY INFERRED`: سازندهٔ `Dp` کامپوز (`u3/c` یک value class تکF است) — **انتساب به فاصلهٔ خاص اثبات نشده** |
| `20.0`, `10.0` | `0xab198c`, `0xab1992` | `k;->b(JZ…)` | `Lf0/a2;->p(Lx1/q;FF)Lx1/q;` | `INFERRED`: modifier دوبُعدی (`offset`/`padding`) |
| `8.0` | `0xab48ee` | `k;->k(...)` | `Lf0/g;-><init>(FZLf0/h;)V` | `INFERRED`: شعاع گوشه/شکل |
| `40.0` | `0xab49e4` | `k;->k(...)` | `Lf0/a2;->f(Lx1/q;F)Lx1/q;` | `INFERRED`: اندازه/فاصله |
| `24.0` | `0xab5052` | `k;->n(...)` | `Lf0/a2;->o(Lx1/q;F)Lx1/q;` | `INFERRED` |
| `24.0`, `8.0`, `6.0`, `4.0` | `0xab5f8c`, `0xab610c`, `0xab61e6`, `0xab61ea` | `k;->t(...)` | `Lf0/a2;->f`, `Lm0/g;->b(F)Lm0/f;`, `Lf0/c;->C(Lx1/q;FF)Lx1/q;` | `INFERRED` |
| `12.0` | `0xab4e08` | `k;->m(...)` | `Lg1/d0;->a0(I)V` | `INFERRED` |
| `180.0`, `270.0`, `90.0` | `0xab357a`, `0xab35c0`, `0xab361c` | `k;->h(LazyListState,…)` | `Lxn/d;-><init>(Lb1/z0;F)V` | `INFERRED`: زوایای چرخش (درجه) برای پیکان/مسیر |
| `88.0` | `0xaad1a6` | `ui/path/map/b;->invoke(...)` | `Lg1/v1;->getValue()` | `UNKNOWN` |
| `0.8` | `0xab6824` | `k;->v(...)` | `Le2/v;->b(JF)J` | `INFERRED`: آلفای رنگ |
| `-0.271367` @`0xab12b0`, `0.253592` @`0xab4d04` | ثابتهای `const` | `k;->B`, `k;->m` | `Lq1/b;->e(...)`, `Lg1/d0;->c0(I)` | `INFERRED`: افست/ضریب انیمیشن؛ فرمول `UNKNOWN` |
| `scrollPosition`, `scrollPositionX`, `scrollPositionY`, `instructionsScrollOffset` | رشتهها @`0x1e9081`, `0x1e9093`, `0x36528c`, `0x202266` | `toString()` کاتلین | — | فقط **نام فیلد**؛ مقدار `UNKNOWN` |

> ⚠️ **قید «از اجرای واقعی جدا کن»:** ستون «از اجرای واقعی» برای **همهٔ ردیفها خالی / ۰** است.
> هیچ `wm size`، `wm density`، UI hierarchy، اسکرینشات یا مقدار `Dp` مشاهدهشده وجود ندارد.
> وجود یک `const/high16 24.0` در کنار `Lf0/a2` **اثبات نمیکند** که «فاصلهٔ عمودی گرهها 24dp» است؛
> کلاس `f0/a2` توسط R8 تغییر نام یافته و هویت متدش (`padding` یا `size` یا `offset`) احراز نشده.
> بنابراین **هیچ فرمول مختصات، تابع منحنی یا عدد `dp` قطعی اعلام نمیشود.**

## ۴. جدول وضعیت مؤلفههای درخواستی مادهٔ ۳

| مؤلفه | وضعیت | شاهد / دلیل دقیق |
|---|---|---|
| مختصات X/Y گرهها | `UNKNOWN` | حلقهٔ `invoke$3` خوانده شد، ولی بدنهٔ محاسبهٔ `boxPosition`/`offsetXPx` در `k;->v/h/t` همراه ثابتها به طور معنایی دیابسک نشد |
| فاصلهٔ افقی / عمودی | `UNKNOWN` | ۱۴۶ ثابت عددی یافت شد؛ انتساب به فاصلهٔ مشخص `INFERRED` و اثباتنشده |
| ترتیب گرهها | `OBSERVED` | `tutorials[]` v753 + `getSections()/getTutorials()` @`0x9a9240`/`0x9a927e` |
| الگوریتم منحنی | `UNKNOWN` | `borderPath`, `radiusY`, `verticalEllipseRadius` فقط رشتهاند؛ `180/270/90` زوایااند ولی تابع منحنی بازسازی نشد؛ ۰ xref رشته→تابع |
| ارتباط Section ↔ گره | `OBSERVED` | `startIndex/endIndex` v753 + `getSections()` در همان حلقه |
| شکل ۶ نوع Node | `UNKNOWN` | `getType()` @`0x9a92f4` خوانده میشود؛ نگاشت به ظاهر نامشخص |
| Locked / Available / Completed | `UNKNOWN` | `isCompleted()` @`0x9a940c` و `isRequired()` @`0x9a93e6` خوانده میشوند؛ قاعدهٔ نهایی بازسازی نشد |
| محاسبهٔ Scroll Position | `UNKNOWN` | `scrollPosition/X/Y` فقط رشته؛ `job$1::invokeSuspend` @`0x50aa64b8` در Ghidra ۳۵ دستورالعمل دارد ولی معناش مشخص نیست |
| بازیابی موقعیت قبلی | `UNKNOWN` | `SaveableStateRegistry` در وابستگیها `INFERRED`؛ بدون `TEST-009` قابل اثبات نیست |
| انیمیشن جابهجایی/انتخاب | `UNKNOWN` | فقط `Lf0/g;-><init>(F…)`, `Lx/a1;` و `RepeatMode` در `k;->v` دیده شد؛ مقادیر و ترتیب `UNKNOWN` |

## ۵. دقیقاً چه متدهایی مبهم ماندهاند

| متد (`classes.dex`) | چرا مبهم است |
|---|---|
| `L…/ui/path/map/k;->h(Landroidx/compose/foundation/lazy/b;…)` | ۱۸۰/۲۷۰/۹۰ درجه و `LazyListState` دارد؛ رسم منحنی/پیمایش LazyColumn از ۳۴۰+ دستورالعملش بازسازی نشد |
| `k;->v(Ld2/c;…)` (۴۷۳ دستورالعمل قابلدسترسی) | بیشترین ثابتها (۴/۶/۱۲/۳/۰٫۸)؛ شاخههای `if` و نقش `Ld2/c;` (احتمالاً `Color`/`Shape`) نامشخص |
| `k;->B(…)` (۵۱۷ دستورالعمل) | `getRootView().getHeight()` و `a(JLu3/c;)F` دیده شد ولی تبدیل px↔dp احراز نشد |
| `PathMapScreenKt$PathMapScreen$10$1$job$1::invokeSuspend` | Ghidra `@0x50aa64b8`، ۳۵ دستورالعمل؛ `sget_object` + `invoke_static` بدون xref |
| `GetPathMapState$invoke$3::invokeSuspend` | Ghidra `@0x509a90c8`، ۷۱ دستورالعمل؛ ترتیب شرطها و state ساختهشده بازسازی نشد |

## ۶. شناسهها

`EV-M02-0013` (حلقهٔوضعیت)، `EV-M02-0014` (۱۴۶ ثابت)، `EV-M02-0015` (هندسه `UNKNOWN`)،
`EV-M02-0006` (دیکود ۱۲۲٬۵۴۶ متد). نمودار جریان در `COMPLETE_APPLICATION_FLOW.fa.md` بهروز شد.
EOF