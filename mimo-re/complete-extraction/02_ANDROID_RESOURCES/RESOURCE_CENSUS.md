# ۰۲ — سرشماری منابع اندروید (اندازه‌گیری‌شده)

منبع: `RESOURCE_CENSUS.csv` (پارس مستقیم ZIP؛ APK دست‌نخورده). کل فایل‌های `res/` = **۳,۱۷۷**.

## ۱. توزیع پوشه‌ها (بزرگ‌ترین‌ها)

| پوشهٔ res | فایل | خوانش |
|---|---|---|
| `drawable` (+ night/density variants) | ۹۰۸ + ۱۶۵ + ۶۵ + ۲۹ + ۲۳ + … | تصویرسازی دستی/برداری |
| `layout` | ۸۰۹ | UI عمدتاً **XML View** است، نه Compose |
| `layout-v33` | ۳۱۹ | سازگاری اندروید ۱۳+ |
| `layout-v31` | ۱۵۰ | Material You / Splash screen |
| `color` (+ v31) | ۲۵۵ + ۳۵ | سلکتورها و توکن‌های رنگ |
| `anim` / `animator` / `interpolator` | ۷۲ / ۴۷ / ۲۴ | حرکت‌های ریز (Sheet، Placeholder) |
| `raw` (+ night) | ۶۱ + ۱۵ | صدا/فونت/دادهٔ خام |
| `font` | ۱۵ | Aeonik Pro/Fono/Mono + optimistic_vf + roboto |
| `xml` | ۱۵ | backup rules، data extraction rules، … |
| `navigation` | ۱ | `nav_onboarding_graph.xml` |

## ۲. دارایی‌های assets (۱۰,۵۶۴ فایل)

| گروه | فایل | یادداشت |
|---|---|---|
| بسته‌های محتوا `lessons-<lang>/tracks` | ۱,۰۳۰–۱,۰۳۲ به‌ازای هر زبان × ۱۰ | ۱۰,۳۰۴ فایل JSON |
| آیکون‌های مشترک (SVG) | ۲۱۵ | `lessons-common/icons` |
| انیمیشن Rive | ۵۹ فایل `.riv` | زنجیره/جشن/شخصیت‌ها |
| WebView درس | `lesson-webview.js`, `lesson-webview-fonts.js`, `highlight.min.js`, `styles/`, `beautify/`, `prettier/`, `snippets/` | رندر کد و برجسته‌سازی |
| فیکسچر تست | `testdata/45-1-1.html`, `test-tutorial.json`, `mock/tracks.json` | شاهد آزمون طلایی پارسر |
| protobuf | ۶۹ فایل `.proto`-associated | انتقال داخلی Firebase |

## ۳. فناوری UI هر سطح (و نه بیشتر)

| سطح | فناوری | شاهد |
|---|---|---|
| اکتیویتی‌های درس/مسیر/پروفایل | View + ViewBinding (XML) | ۸۰۹ layout + نام Binding در خطاهای «Missing required view with ID» |
| مربی هوشمند | Compose | `AiTutorBottomSheetKt`, `AiTutorViewsKt` |
| کیبورد کدنویسی | Compose | `ui.projects.components.CodingKeyboardKt` |
| ویجت زنجیره | Glance (Compose for widgets) | `androidx.glance` ۱۹۶ کلاس، `MimoStreakWidget$provideGlance` |
| بلوک‌های `<webview>` درس | WebView + پل JS | `addJavascriptInterface`, `removeJavascriptInterface`, `lesson-webview.js` |
| انیمیشن جشن | Rive | ۵۹ فایل `.riv` + ۹۸۳ کلاس |

> **نکتهٔ صداقت:** «هر صفحه از چه فناوری‌ای استفاده می‌کند» فقط در سطح **خانواده** قابل اثبات است.
> تخصیص دقیق per-screen بدون اجرا انجام نشد و در `SCREEN_CATALOG.md` با
> `technology: PARTIALLY_VERIFIED` علامت خورده است.
