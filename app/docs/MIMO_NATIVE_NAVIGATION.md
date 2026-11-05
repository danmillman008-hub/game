# ردیابی ناوبری: خروجی بومی ↔ میمو ۹٫۳۵

این سند نشان میدهد هر صفحه/گذر در خروجی جدید `app/dist/Mimo.html` از کدام
مدرک اندازهگیریشدهٔ میمو آمده، و کجا یادداشتهای پروتوتایپ `v12.5-fa`
(که باید صددرصد رعایت میشدند) بر ناوبری خام ارجح شدهاند.

منابع:
- `ANALYSIS/MISSION_09/COMPLETE_NAVIGATION_STATE_MACHINE.json`
- `ANALYSIS/MISSION_08/MIMO_NAVIGATION_GRAPH.json` (۴۶ صفحه / ۴۵ یال)
- `ANALYSIS/MISSION_09/COMPLETE_UI_RENDERER_CATALOG.md`
- `ANALYSIS/RUNTIME/MISSION_05/SCREENSHOTS/*.png`, `ANALYSIS/RUNTIME/MISSION_07/UI/*.png`
- `mimo-ui/UPGRADE/CATALOGS/*.csv` (F10–F47, PN-01…PN-11, GAMIFICATION_MAP)
- `mimo-ui/UPGRADE/DESIGN/index.html` (SHA `c356068d…`, بدون تغییر)

## ۱) ماشین حالت

| حالت M09 | پیادهسازی | محل |
|---|---|---|
| `STARTUP` / `ONBOARDING` | عمداً **بهعنوان صفحهای جداگانه اضافه نشده** (F18: «no onboarding screen»). مسیر مستقیم به `Learn` | `app/src/native.js` → `PROTO.go('learn')` |
| `AUTH_GATE` | «درگاه تمرین» با ساخت پروفایل **محلی**، بدون سرور/ایمیل | `native-gate`, `profile:create` |
| `MAIN` / `MainActivity` | پوستهٔ تأییدشدهٔ `phone.html` با `contentFrame`، `#tabs` | `app/native/index.html` |
| `CHAPTER` / `ChapterActivity` | پلیر درس تمامصفحه: `X ▬▬▬ ⚑` + دکمهٔ «ادامه» | `[data-screen="lesson"] .native-lesson` |
| `QUIT_DIALOG` | «Quit lesson» / «Choose a different path» / «Cancel» | `#nativeQuit`, `[data-quit]` |
| `PATH_PICKER` | `Select Path` / سه مسیر / شمار sectional | `select-path` (تأییدشده) + ۳ کارت |
| `PRACTICE_GATE` | «Lock in your learning» | `native-gate` |
| `G-AUTH`, `G-KEYS`, `G-QUIT`, `G-NETWORK` | گیت مهمان، کلید ∞، دیالوگ خروج، و نبود کامل شبکه | `store.js`, `native.js` |

چهار تب اندازهگیریشدهٔ M09 (`Learn / Practice / Leaderboard / Profile`) با همان
ترتیب و مقصد حفظ شدهاند؛ تب پنجم `AI` یادداشت مصوب F13 است. مقصدها:
`2131361976→Path`, `2131361974→Practice`, `2131361973→Leaderboard`,
`2131361975→Profile`.

## ۲) یادگیری (بخش حساس درخواست)

| عنصر اسکرینشات M07/M05 | پیادهسازی | یادداشت مصوب |
|---|---|---|
| ۳ چیپ بالا: `200` / key `∞` / flame `0` | ۳ چیپ زنده از دفتر توکنها؛ کلید همیشه `∞` | F14 |
| کارت «Python Developer / 1. Intro to Python» | همان کارت، با نام کتاب و فصل جاری از `KONKUR` | F15 |
| نقشهٔ زیگزاگ ۶ گره، کانکتور Q بنفش، گرید نقطهای | همان هندسهٔ `node-match.css` (`l10n1…l10n6`) بدون دستکاری | F19–F24, PN-01…PN-06 |
| گرهٔ جاری: کارت سفید + حلقهٔ دوتایی + `½` | `۱/۲` فارسی، حلقهٔ `conic-gradient` | PN-08…PN-10 |
| گرههای دیگر: کارت سفید + مثلث پخش سرمهای | `ic_play` با `currentColor = var(--text)` | PN-11؛ F37 (فقط آیکون مصوب) |
| گره تمامشده: بنفش + تیک سفید | `.node.done` + `ic_check_white` | PN-02, PN-07 |
| رعد بنفش = چکپوینت تمرین | همان `ic_bolt_charged` / `ic_bolt_mastered` | PN-12, PN-13 |
| بدون گره قفلشده | ۴ گره نخست به درسهای واقعی وصلاند، هیچ `locked`ای ساخته نمیشود | F25 |
| `X` / نوار پیشرفت ۶dp / پرچم | `.nl-top` با `direction:ltr` تا دقیقاً چپ→راست شود، `--progressbar` | F27, F28 |
| دکمهٔ سرتاسری بنفش `Continue` | `.native-cta` «ادامه»، تمامعرض | F30 |
| WebView MCQ «Guess the letter _ O G» | گام دوم: همان سؤال ۴گزینهای + توضیح موجود | F31, F33 |
| صفحهٔ کد `index.html` / `<button>Like</button>` | گام سوم: جای خالی با قطعههای متن موجود (بدون ادعای اجرای کد) | F32 |
| «Correct! DOG» | بنر بازخورد با متن موجود در بسته | F34 |
| نبود تبهای پایین داخل `ChapterActivity` | `data-fullscreen=1` → `#tabs` و نوار وضعیت جعلی مخفی | M09 |
| تولتیپ «Welcome to your learning path!» | اضافه **نشد** (F18) | F18 |

چهار گام درس (`slide → MultipleChoice → fillTheGap → reveal`) از
`COMPLETE_UI_RENDERER_CATALOG.md` گرفته شدهاند. رویدادهای WebView در M07
صفر بوده و نام پل `lesson-webview.js` بهصورت زنده تأیید نشده؛ بنابراین
هیچ ادعای اجرای کد، پل بومی یا امتیازدهی سروری نشده است.

## ۳) بقیهٔ بخشها

| بخش | منبع | وضعیت |
|---|---|---|
| هاب آزمون ۷ بخشی، پیشفرض جامع ۲۷۰ دقیقهای | `EXAM_SECTION_TEMPLATES.csv`, `PRACTICE_VS_EXAM.csv` | همان `exam-hub` تأییدشده |
| تایمر فقط داخل آزمون، یک چیپ، ۳ مسیر خروج | F39–F42 | حفظ شده |
| «پاسخبرگ» ≠ «پاسخنامه» | `ANSWER_SHEET_POLICY.csv` | حفظ شده |
| چیپ هوش مصنوعی | F43 | حفظ شده + اتصال به `native-studio` |
| لیدربورد ۳ نما | پروتوتایپ | همان |
| پروفایل: تم شب، هدف روزانه، ساختار توکنها، خروجی | `app/src/native.js` | ردیفهای تازه با همان توکنها |
| AI: چهار فاز، گراف، توکن زمینه | `COMPLETE_LESSON_ENGINE_SPEC.md` | محلی، بدون LLM |

## ۴) یادداشتهای `v12.5-fa` که صددرصد حفظ شدند

- پنج تب دقیق `Learn|Practice|AI|Leaderboard|Profile` با برچسبهای فارسی؛
  **نه** تب مکس/روتین روزانه/Habitica/Dictate؛ نه Pro و پرداخت. (F13, F46)
- هیچ رنگ، فونت، شعاع، آیکون یا فاصلهای تازه: تمام مقادیر از `:root` همان
  `proto.css` و وکتورهای ARSC در `proto-data.js`. (F2, F10–F12, F37)
- `bg #F6F7FB`، شب `#252746`، `button #7E4BDE`، `progress #8D60E2`،
  `TextH1 24sp`، `TextP2 16sp`، toolbar 56dp، card radius 12dp. (F1, F3)
- پنج dimensای که در `proto.css` بیرون از `:root` افتاده بودند (`--sp-m`،
  `--sp-s`، `--toolbar`، `--progressbar`، `--radius-card`) فقط در
  `native.css` با **همان مقادیر مصوب** تعریف شدند تا نوار پیشرفت ۶dp و
  شعاع ۱۲dp واقعاً اعمال شوند؛ مقدار تازهای ابداع نشد.
- شواهد فنی پنهان (`data-code` / `data-lh`)؛ هیچ یادداشت توضیحی قابل مشاهده
  داخل گوشی؛ RTL و فارسی پیشفرض. (F5, F6, F47)
- `data-scope="learn-practice"` جدا از هاب آزمون؛ فلشهای RTL؛ حداقل کنترلها.
- فایل `mimo-ui/UPGRADE/DESIGN/index.html` و `app/assets/phone.html`،
  `proto.css`، `proto-data.js`، `proto-ui.js` **بایتبهبایت دستنخورده** ماندند؛
  تغییرات فقط در پوستهٔ تازه (`app/native/index.html`)، `native.css`،
  `native.js`، بیلدر/ورایفایر/تستها و `app/dist/` اعمال شد.

## ۵) لایهٔ محتوا (بازسازی بعد از ایراد کاربر)

ناوبری بهتنهایی کافی نبود: صفحهٔ درس پروتوتایپ یک دموی چیدمان خط بود و بیلد
قبل همان را بهعنوان درسنامه نشان میداد. اکنون مودال فصل، فهرست ریزدرسهای
واقعی بستهٔ `STRUCTURED_PACKAGE.json` را نشان میدهد و پلیر درس شش صفحهٔ
تایپشده (`hook → check → feedback → explain → practice → recap`) را با
ولیدیتورها و ردیفهای `LessonProgress` اجرا میکند. تشریح کامل ساختار، اعداد
اندازهگیریشده از APK و حدود صداقت: `app/docs/MIMO_CONTENT_MODEL.md`.

## ۶) حدود صداقت

`SERVER CONFIRMED=0`. استاتیک APK و اسکرینشاتها نمیتوانند URL زنده،
هدر Authorization، بدنهٔ درخواست، فرمول پاداش یا رفتار سرور را ثابت کنند.
در این بیلد: بدون `fetch`/XHR/WebSocket/EventSource، بدون کلید API، بدون
تولید متن، `externalProvider: 'not-configured'`. محتوای درس `placeholder`
و برچسب «بازبینینشده» دارد تا زمان تحویل منابع تأییدشده.
