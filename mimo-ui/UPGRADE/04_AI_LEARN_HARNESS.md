# بخش هوش مصنوعی میمو — ظاهر عیناً همان، بکاند Learn Harness
<!-- v12-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v12](24_DESIGN_ROUND_12.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.
<!-- v11-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v11](23_DESIGN_ROUND_11.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.
<!-- v10-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v10](22_DESIGN_ROUND_10.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.
<!-- v9-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v9](21_DESIGN_ROUND_9.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.
<!-- v8-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v8](20_DESIGN_ROUND_8.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.
<!-- v7-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v7](18_DESIGN_ROUND_7.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.

> ⚠️ **بایگانی / superseded:** این سند مربوط به دورهای قبل است. طراحی فعلی **[DESIGN v6](17_DESIGN_ROUND_6.md)** است؛ صفحهٔ ورود حذف، یادگیری بازسازی و زیرصفحات «انتخاب مسیر / نمای مسیر / داخل مبحث» از کد اضافه شدند. لاگهای قدیمی صرفاً ردپای حسابرسیاند.

> 🔄 **DESIGN v5 (حکم فعلی) — بازآفرینی ۱۰۰٪ از داخل کد:** لاگ کامل ← `16_DESIGN_ROUND_5.md`، prototype ← `DESIGN/index.html`، هندسهٔ استخراجشده ← `DESIGN/CODE_GEOMETRY.json`.
> اصلاحیهٔ نامگذاری: دکمهٔ قدیمی «پاسخنامه» = **«پاسخبرگ»** (گزینههای زدهشده)؛ «پاسخنامه» دکمهای **جداگانه** برای جواب تشریحی/توضیحات است. یک دکمهٔ «توضیح با هوش مصنوعی» در صفحهٔ سؤالات + همان دکمه در صفحۀ آخر آزمون. لیدربورد اطلاعات/امتیازات/آزمونهای خود فرد را نشان میدهد. متن پایینتر، بایگانی دور قبل است و فقط برای ردیابی نگه داشته شده.


خواسته: «دقیقا ظاهر اون بخش هوش مصنوعی میمو رو نگه میداری ولی پشتش بک اندش رو باید وصل کنی لرن هارنس… داخل بقیه اپلیکیشنهای مشاوره هم همچین بخشی هست، هرچند رابط کاربریش مختصر باید تغییر کنه تا دکمههای لرن هارنس داخل یو آی دربیاد و حذف نشه».

## ۱. آنچه **نباید** تغییر کند (Frozen Surface)

از استخراج Mimo 9.35:

- نقطهٔ ورود: `res/layout/coding_keyboard_layout.xml` → `@id/btn_ai_tutor` و `@id/iv_ai_tutor_pulse` (پالس همان انیمیشن).
- متنها: ۲۸ رشتهٔ `ai_tutor_*` و `ai_*` عیناً: `ai_tutor_chat_header`, `ai_tutor_input_placeholder`, `ai_tutor_input_max_characters`, `ai_tutor_first_hint`, `ai_tutor_second_hint`, `ai_tutor_start_message`, `ai_tutor_intro_title`, `ai_tutor_intro_benefit_1..4`, `ai_tutor_intro_disclaimer`, `ai_tutor_error_message_template`, `ai_tutor_offline_description`, `ai_intro_no_chat_history`, `ai_mascot_name`, `ai_initial_prompt_*`, `ai_progress_banner_*`.
- سطح چت **Compose** است (هیچ `ai_tutor_*.xml` جداگانهای وجود ندارد؛ ۷۱ لایوت ComposeView)، بنابراین قرارداد بصری از روی همان کامپوننت Compose و توکنها حفظ میشود: هدر، حبابها، نوار ورودی، `ai_tutor_input_placeholder`، حالت آفلاین، بنر پیشرفت، خطا، ماسکات.
- پالس، `bottom_sheet_slide_in/out`، `flash_bar_view` برای پیامها.

**هیچ عنصری حذف نمیشود.** تنها افزودهٔ مجاز: یک **ردیف اکشن (Action Dock)** زیر نوار ورودی، برای نمایانکردن قابلیتهای Learn Harness.

## ۲. بکاند: Learn Harness پینشدهٔ خود ریپو

`/home/user/_work/prev/mimo/engines/pins.json`:

```json
{"repo": "https://github.com/amosblomqvist/learnharness.git",
 "commit": "e69e85269c064c6c9c49a8b06ae78c06e79c4a63",
 "license": "AGPL-3.0-only",
 "stack": "Next.js 16 (React 19) + its own Node server",
 "run": "next dev --port 3000 with LH_DATA_DIR + LH_AUTH_FILE isolated",
 "integration": "basePath=/max and reverse-proxied at /max (prefix kept)"}
```

- اسکریپت `mimo/engines/prepare_learnharness.py` همان `basePath: "/max"` را تزریق میکند؛ `start-preview.sh` پورت ۳۰۰۰ را پشت `/max/*` پروکسی میکند (پیشوند **حفظ** میشود، برخلاف `/practice/*` که حذف میشود).
- `LH_DATA_DIR` و `LH_AUTH_FILE` جدا از Mimo و EPM؛ **هیچ دیتاستور مشترکی** وجود ندارد (قاعدهٔ سند `19`).
- **LH بازنویسی نمیشود**: همان Next.js اجرا میشود؛ تنها لایهٔ فارسی/RTL و تزریق زمینه (context) به آن اضافه میشود.
- محتوای آموزشی LH: Measure → Plan → Teach → Practice، گراف دانش پایدار، confidence rail، thinking fields، hints، practice sessions. اینها دقیقاً همان «سازوکار یادگیری»ای هستند که باید پشت ظاهر میمو قرار بگیرند.

## ۳. زمینهای که به LH داده میشود (و آنچه داده نمیشود)

داده میشود: `lessonId`, `documentId`, `subject`, `topic`, `userLevel`, `recentMistakes[]`, `visible-if` وضعیت، `progress triple`، زبان `fa`.
**داده نمیشود**: پاسخ صحیح، `answerKey`، `offset`های نمرهدهی، کلید مدل، اطلاعات شخصی (قواعد سند `19` و «No secrets»ی craft-anything).

## ۴. دکمههای LH که باید «داخل UI دیده شوند و حذف نشوند»

از کامپوننتهای واقعی کلونشدهٔ LH (`components/home.tsx`, `new-session.tsx`, `top-bar.tsx`, `composer-actions.tsx`, `practice-cards.tsx`, `question-dock.tsx`, `graph-view.tsx`, `plan-window.tsx`, `confidence-rail.tsx`, `thinking-block.tsx`, `notes-import.tsx`, `dictation.tsx`, `session-navigation.tsx`). فهرست کامل در `CATALOGS/LEARNHARNESS_ACTIONS.csv`.

| اکشن LH | برچسب فارسی در ردیف اکشن میمو | رفتار |
|---|---|---|
| `Start session` / `aria-label="Start session"` | «جلسهٔ تازه» | شروع Measure→Plan |
| `Sessions` + `session-navigation` | «جلسهها» | لیست/ادامهٔ جلسه |
| `Plan window` / `Targets` | «نقشهٔ یادگیری» | نمایش dependency map |
| `Knowledge graph` / `Search nodes` | «گراف دانش» | نمودارگزارهها |
| `Practice` / `Next problem` / `Retest` | «تمرین» / «سؤال بعد» | نشست تمرین مجزا |
| `Check your understanding` | «بفهمم یا نه» | مرحلهٔ Teach |
| `Confidence rail` | «میزان اطمینان» | ثبت confidence |
| `Thinking fields` / «Think out loud» | «فکر کردن با صدای بلند» | فیلد تفکر |
| `Hint rung` | «راهنما» | نردبان راهنما |
| `Notes import` | «یادداشتهام» | واردکردن جزوه |
| `Researcher`, `Figure maker`, `PDF reader`, `Demo builder` | «پژوهش»، «شکل»، «PDF»، «نمونه» | ابزارهای پسزمینهای |
| `Model` / `Context` / `Cost` / `Steps` / `Settings` | «مدل»، «هزینه» | همان chipهای LH |
| `Dictation` | «گفتار» | دیکته (اختیاری) |
| `Stop` / `Abort` / `End this background process` | «توقف» | قطع جریان |

نمایش: همان `flash_bar_view.xml` / ردیف chip با `card_pressed`، `12dp`، `8dp` فاصله، اسکرول افقی RTL، `contentDescription` کامل؛ **بدون تغییر هدر، حباب، نوار ورودی، ماسکات و پالس**. در حالت آفلاین، chipها به `card_disabled` میروند و `ai_tutor_offline_description` نشان داده میشود (نه صفحهٔ خرید).

## ۴٫۱ جاسازی کنترلهای واقعی LH (بازخورد v2 — اسکرینشات کاربر)

خواستهٔ جدید: «دستیار هوشمند باید در ظاهر یو آی اون دکمههایی که لرنهارنس در یو آی خودش داره رو جا سازی شده باشه، صرفاً ظاهرش شبیه میمو باشه».

منبع: `DESIGN/REFERENCE/learnharness-ui-user-screenshot.png` (پیوست کاربر، ۱۷۹۶×۱۰۱۵، SHA-256 `c94a223aa07544f2f5768c45d61245ec41d7738bc459810797719086bdca945d`) + کامپوننتهای کلونشدهٔ LH. جدول کامل در `CATALOGS/LEARNHARNESS_ACTIONS.csv` (۲۶ ردیف) و پیادهمسازی قابل لمس در `DESIGN/index.html` → نمای «دستیار هوشمند».

| ناحیهٔ LH در اسکرینشات | جاسازی در پوستهٔ میمو |
|---|---|
| `+ TEACHING` / `PRACTICE` | «＋ آموزش» / «＋ تمرین» بالای کارت جلسهها |
| `SESSIONS` + `Search...` + `ALL/TEACHING/PRACTICE` | کارت جلسهها + جستجو + سه تب |
| لیست جلسهها `Waiting for input · 2d ago` | همان لیست با `card_enabled` |
| `Chains`, `Import notes…`, `$0.01` | ردیف بالا: زنجیرهها / یادداشتها / هزینه |
| `Knowledge graph` + «Start a session or import notes…» | کارت مرکزی با همان empty state |
| `What do you want to learn?` + دکمهٔ ارسال | نوار ورودی میمو (`ai_tutor_input_placeholder`) |
| `TEACH/PRACTICE`, `Dictate`, `gemini-flash-lite-latest`, `medium`, `Context`, `Steps`, `Cost` | ردیف زیر ورودی |
| `BACKGROUND AGENTS`, `SETTINGS` | ردیف جمعشوندهٔ پایین |
| ۱۵ اکشن کامپوننتی (Plan window, Confidence rail, …) | ردیف چیپ `lhDock` (برچسب فارسی + نام انگلیسی) |

**قاعدهٔ طلایی:** کنترلها = LH (**هیچکدام حذف نشود**)، پوسته = Mimo (رنگ/شعاع/فاصله/RTL/نایت مُد/ماسکات/پالس/حبابها/رشتههای `ai_tutor_*`). فقط برچسبها ترجمه و جاسازی میشوند؛ منطق LH همان `basePath=/max` و دیتاستور جدا باقی میماند.

## ۴٫۲ پنل مینیمال v3 — حکم نهایی (جایگزین §۴ و §۴٫۱)

> «واقعیتش این اصلا به درد نمیخوره، باید یه پنلی باشه شبیه همین پنلی که داریم باهات چت میکنیم… ساده مینیمال و شبیه دیزاین میمو… نهایت یه گزینهٔ هیتوری میزاری ولی باید در همین حد ساده باشه.»

**طرح v2 (۳۲ دکمهٔ جاسازیشدهٔ LH، سایدبار `SESSIONS`، کارت `Knowledge graph`، ردیف `TEACH/PRACTICE`/`Dictate`/مدل/`medium`/`Cost`) لغو شد.** جایگزین در `DESIGN/index.html` → نمای «دستیار هوشمند»:

| عنصر | وضعیت |
|---|---|
| هدر میمو: ماسکات ✦ + `ai_tutor_chat_header` + پالس | ✅ |
| حبابهای گفتگو (کاربر/دستیار)، RTL | ✅ |
| ورودی `ai_tutor_input_placeholder` + ارسال (دکمه / `Enter`) | ✅ |
| «در حال نوشتن…» + پاسخ جریانی | ✅ |
| **تاریخچه** (یک آیکن 🕘 ← لیست گفتگوها + «گفتگوی تازه») | ✅ **تنها گزینهٔ اضافی مجاز** |
| «پاسخها از LearnHarness میآیند · `/max`» | ✅ |
| ۳۲ کنترل LH | ❌ نمایش داده نمیشوند؛ بایگانی در `CATALOGS/LEARNHARNESS_ACTIONS.csv` (ستون `surface`) |

**منابع ایده:** اسکرینشات پنل اصلی LH (`DESIGN/REFERENCE/learnharness-main-panel-user-screenshot.png`) + `ChatView.vue` / `AiAssistant.vue` در EPM (لینکی که کاربر داد) = چت ساده + تاریخچه + پاسخ جریانی. مشخصات کامل: `DESIGN/DESIGN_NOTES.fa.md` §۳، `CATALOGS/AI_PANEL_SPEC.csv`, `14_DESIGN_ROUND_3.md`.

**جمعبدی تضادبا دور قبل:** «دکمههای LH داخل UI دربیاد و حذف نشه» ← v3 آن را به «قابلیتها پشت بکاند `/max` حذف نشوند، ولی در UI نمایش داده نشوند» تغییر داد. قابلیتها حذف نشدهاند؛ فقط پنل ساده شد. همچنان: ۰ تغییر در رشتههای `ai_tutor_*`، `@id/btn_ai_tutor` و `iv_ai_tutor_pulse` سر جای خود، دیتاستور `LH_DATA_DIR` جدا، ۰ ارسال پاسخنامه به مدل.

## ۴٫۴ دکمههای LH در چت مینیمال (v4 — حکم نهایی)

> «الان بهتره، هرچند در بخش چت با هوش مصنوعی این امکانات باید باشه، میتونی بهعنوان دکمه اضافه کنی بهش.»

چت سادهٔ v3 حفظ شد؛ **فقط ۸ دکمهٔ پنل اصلی LH** از دو اسکرینشات تازه (`DESIGN/REFERENCE/lh-composer-user-screenshot.png`, `lh-topbar-user-screenshot.png`) اضافه شدند:

| ناحیه | دکمهها |
|---|---|
| ردیف بالا | `Chains` · `Import notes...` · `Cost $0.01` |
| ردیف زیر ورودی | `TEACH / PRACTICE` · `Dictate` · `gemini-flash-lite-latest ▾` · `medium ▾` |
| هدر | 🕘 تاریخچه (همان تک گزینهٔ اضافی v3) |

ورودی: `What do you want to learn? · ai_tutor_input_placeholder`. ۱۵ اکشن کامپوننتی LH همچنان `ARCHIVED_NOT_RENDERED` در `CATALOGS/LEARNHARNESS_ACTIONS.csv`. قابلیتها پشت `/max` باقیاند؛ پاسخنامه/کلید آزمون هرگز به مدل ارسال نمیشود. مشخصات: `CATALOGS/AI_PANEL_SPEC.csv`, `15_DESIGN_ROUND_4.md` §۵.

📌 **یادداشت بدون طراحی UI (خواستهٔ صریح):** «تو تنظیمات یه بخش وارد کردن کلید API باشه تا بشه بخش چت رو راهانداخت… نیازی نیست الان تو UI طراحی کنی». الزام در `SCOPE_DECISIONS.csv` / `AI_PANEL_SPEC.csv` ثبت شد؛ **هیچ صفحهٔ تنظیمات یا فیلدی فعلاً طراحی نشد**.

## ۵. مقایسه با اپهای مشاوره (آموختهها)

- همدرس: `AIChatWebViewScreen`, `AiChatConversationScreen`, `AiChatInputBar`, `AiChatCubit`, `AiChatThemeCubit`, ۲۶ دارایی `assets/ai_chat/` (ربات، `Counselor.svg`, میکروفون، کپی، لایک/دیسلایک، `magic_pen`, `documents`, `gallery-send`, `question-square`, `volume`)، و درسهای UX `ai-ask` و `ai-credit`.
- هدفپلاس: `/Chatbot/conversations`, `/Chatbot/messages/stream`, انیمیشن `chatbot.json`, `اتاق رسمی هدفپلاس`, `/Chat/Admins`, `/Chat/Studying`.
- نتیجه: اپهای مشاوره AI را **بهصورت چتتمامصفحه + اعتبار/خرید** نشان میدهند؛ ما این الگو را **نمیپذیریم**، چون وفاداری به میمو اولویت دارد. فقط ایدهٔ «دکمههای قابلیت کنار ورودی» و «لایک/دیسلایک پاسخ» بهعنوان **چیپهای اختیاری در همان ردیف اکشن** گرفته میشود؛ «اعتبار/بسته/اشتراک» حذف میگردد.

## ۶. پذیرش فاز P4

- [ ] diff رشتههای `ai_tutor_*` = ۰ تغییر؛ `@id/btn_ai_tutor` و `iv_ai_tutor_pulse` سر جای خود
- [ ] `/max/*` پاسخ میدهد، `LH_DATA_DIR` جدا است، prefix حفظ شده
- [ ] ~~۱۶ اکشن LH در UI قابلرویتاند~~ ← لغو شد (v3/v4)؛ ۱۵ اکشن کامپوننتی بایگانیاند
- [ ] **v3:** پنل فقط چت + ورودی + ارسال + حداکثر یک «تاریخچه»؛ ۰ داک دکمه، ۰ سایدبار جلسهها، ۰ گراف دانش، ۰ ردیف ابزار
- [ ] **v3:** قابلیتهای ۳۲گانهٔ LH پشت `/max` باقیاند (حذف نشدهاند) ولی در UI رندر نمیشوند
- [ ] ~~تکتک کنترلهای اسکرینشات LH جاسازی و قابلکلیکاند~~ ← لغو شد توسط بازخورد v3
- [ ] پاسخ صحیح/کلید/answerKey هرگز در prompt ارسال نمیشود (تست خودکار)
- [ ] حالت آفلاین و خطا با همان رشتههای میمو
- [ ] **v4:** چت مینیمال + ۸ دکمهٔ پنل اصلی LH + تاریخچه؛ ۰ داک ۳۲تایی، ۰ سایدبار، ۰ گراف دانش
- [ ] **v4:** چت در **تب مستقل AI** است، قاتی Practice نشده (ناوبری ۵ تب)
- [ ] **v4:** کلید API فقط مستند است؛ ۰ طراحی UI
- [ ] نایت مُد و RTL تست شده؛ ۰ تب اضافی فراتر از ۵ تب مصوب
