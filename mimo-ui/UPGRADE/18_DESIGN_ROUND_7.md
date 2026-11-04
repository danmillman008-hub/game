# دور هفتم طراحی — DESIGN v7 (گرهها، تمرین مبحث، روتین روزانه)
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
> ✅ **DESIGN v7 · CURRENT** — لاگ دور هفتم؛ جایگزین نسخههای قبل. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.

> **وضعیت:** `DESIGN v7 · REVIEW` — منتظر تأیید نهایی. همچنان **فقط پلن/دیزاین**؛ هیچ کد محصولی نوشته نشده.
> **روش:** کندوکاو **عمیقتر از داخل کد APK** (`values/values/string.xml`، `res/drawable/*.xml`، `res/layout/*.xml`، `res/anim/*`، `res/raw/practice.riv`، `test-tracks.json`، DEX) + قواعد امتیازدهی Habitica فقط بهصورت خلاصهشده. اسکرینشاتها فقط **چک بصری**. جایگزین `17_DESIGN_ROUND_6.md` است.
> **گفتۀ شما:** «خیلی خیلی خیلی خوبه … ولی چند تا اصلاح ریز مونده».

---

## ۱. گرههای مسیر یادگیری (code-first)

ابزار تازه `tools/extract_mimo_nodes_v7.py` → `DESIGN/NODE_CODE_GEOMETRY.json` (۱۱۶٬۸۴۹ بایت) و `CATALOGS/MIMO_PATH_NODES.csv` (۵۰ ردیف). شمارش: **۵۵ وکتور دقیق `android:pathData`** (بدون خطا)، **۱۴۱ رشتهٔ ARSC**، **۱۷ لایهٔ AXML**، **۲ انیمیشن checkpoint**، `practice.riv`، **۱۵ فصل / ۲۲۳ شناسهٔ `tutorialId`** از `test-tracks.json`، **۳۸۰ کلاس DEX** و ۴۰ لیترال DEX.

| گره | شکل | سند کد | چک بصری |
|---|---|---|---|
| انجامشده | مربع ۹۲px، شعاع ۲۶dp، گرادیان بنفش، لبهٔ سهبعدی ۸px، `ic_check_white` | `button_primary_highlight`, `cardview_corner_radius_large`, `PathMapScreenKt` | mimo-10, mimo-01 |
| فعلی | کارت سفید + حلقهٔ دوتایی بنفش + `ic_play`، برچسب START | `chapter_toolbar.xml`, `progress_bar_mimo.xml`, `start_lesson` | mimo-01 |
| نیمهتمام | حلقهٔ ½ (conic) روی کارت سفید | `glance_circular_progress_indicator.xml` | mimo-02 |
| قفل | `card_disabled` + `ic_lock_alt_02` | `alert_msg_section_setion_locked` | mimo-01 |
| رعدوبرق | `ic_bolt` / `ic_bolt_charged` / `ic_bolt_mastered`، مربع بنفش یا روشن | `ic_practice_tab_locked`, `res/raw/practice.riv`, `rc_checkpoint_window_enter/exit` (alpha ۲۲۰ms) | mimo-01, mimo-10 |
| اتور | مسیر **Q با گوشهٔ گرد** (راست/پایین/چپ/پایین)، نه منحنی بزیه v6 | `PathMapScreenKt` (۷۳ کلاس)، `progress_chapter_primary` | mimo-10 |
| شناور | دایرهٔ کوچک کتاب/واژهنامه (A) | `ic_file.xml` + `bookmark_no_fill.xml` | mimo-01 |

کد ملاک است: اختلاف `mimo-01` (دو چیپ و کارت فصل ۱۲٪) با `mimo-10` (سه چیپ و کارت نمای مسیر) با **حکم v6 + کد** حل شد؛ ساختار گرهها، اتور و نقطهچین ۲۶px از کد آمدند و عکسها فقط چک شدند. فقط **نام درس/مبحث** کنکوری است. ۰ رنگ/فونت/شعاع/آیکون تازه.

## ۲. گره رعدوبرق ← «تمرین مبحث تا همان فصل» (جدا از آزمون)

صفحهٔ تازهٔ `data-screen="section-practice"` (`class="screen mimo"`, `data-scope="learn-practice"`):

- صورت ۳ سؤال از `test-tracks.json → sections[].tutorialIds` **تا همان فصل** رندر میشود (گرهٔ ۳ ← ۶۱ درس، گرهٔ ۵ ← ۹۰ درس).
- چیدمان سؤال/گزینه از `lesson_interactive_multiplechoice_fragment.xml` + `lesson_interaction_selection_item_layout.xml`؛ فیدبک از `lesson_feedback_keep_going`.
- دیالوگها دقیقاً از ARSC: `section_details_smart_practice_charged_dialog_title = Fully charged!`، `mastered_dialog_title = You've mastered the section!`، `practice_anyway = Practice anyway`، `you_finished_all_practice_sessions`. ماسکات `ic_mascot_practice`، DEX `ModalData$SmartPracticeChargedModal/MasteredModal`.
- **تفکیک سهگانه** (جدول کامل `CATALOGS/PRACTICE_VS_EXAM.csv`، ۱۲ ردیف): تمرین مبحث / آزمون کنکور / روتین روزانه. در تمرین مبحث هیچ `timerChip`، `پاسخبرگ`، `پاسخنامه`، `POLICY`، ۲۷۰ دقیقه، هاب آزمون یا دکمهٔ «توضیح با هوش مصنوعی» وجود ندارد. آزمون کنکور همچنان `exam-hub / exam-run / exam-result` است.

## ۳. چت AI: بالا مرتب، پایین تکخط

- بالا: ایموجیها حذف شدند → **گیرهٔ کاغذ** `attachment.xml` + «**اضافه کردن فایل**» (کوتاهترین واضح؛ «الصاق فایل» مترادف)، و `ic_link_external` + «**زنجیره گفت و گو**». دو چیپ در یک ردیف، آیکون متمایز، بدون شلوغی. ۸ دکمهٔ LH پنل اصلی حفظ شد.
- پایین: **TEACH / PRACTICE ریز** و در **همان یک خط** `Dictate` (با `ic_microphone`، ویس — جدا/حذف نشد)، `gemini-flash-lite-latest` و `medium` (chevron). `flex-wrap:nowrap`، فونت ۹px.
- چت همچنان مینیمال + تاریخچه + تکدکمهٔ «توضیح با هوش مصنوعی» در صفحهٔ سؤالات و نتیجه. «وارد کردن کلید API» فقط یادداشت الزام، بدون UI.

## ۴. صفحهٔ سؤال و لیدربورد

- دو دکمهٔ تمیز **«سؤال قبل» / «سؤال بعد»** (با `ic_arrow_left` / `ic_arrow_right`) در ردیف `qnav`.
- پایینش **یک خط** sticky و کمضخامت (`qfoot`): «پاسخبرگ»، «پاسخنامه»، «خروج»، «اتمام آزمون»، «توضیح با هوش مصنوعی»، «توقف»، «تنظیم مجدد» — `font-weight:400`، بدون `btn primary`، بدون حجیمسازی. همان الگو در صفحهٔ نتیجه (`result-foot`).
- **Promotion Zone / «منطقهٔ صعود» حذف شد**؛ `selfbox` و اطلاعات/امتیازات/آزمونهای خود فرد پابرجا. تایمر و سیاست پاسخبرگ/پاسخنامه دستنخورده.

## ۵. روتین روزانه (تب ششم)

دستور صریح: «در نوار پایین یه بخش دیگریم باید اضافه بشود به اسم روتین روزانه … از این پروژه استفاده کن سیستم امتیازدهیش و هیچی قرار نیست قاتی بشه با اپلیکیشن خود ما … یه جوری باشه فکر کنن برای میمو هست نه خود اپلیکیشن ینی زیادی تو چشم نزنه».

- تب ششم **کمسر و صدا** `Routine` با `ic_calendar` / `ic_task_completed`؛ فونت ۹px؛ **MAX همچنان ممنوع**. حکم قبلی «۵ تب» ناظر به جلوگیری از تب MAX بود و اینک بهروزرسانی شد (`D26`).
- `DESIGN/HABITICA_SCORING.json` + `CATALOGS/HABITICA_SOURCES.csv` (۱۳ فایل منبع با SHA-256، کامیت `12091ca02990533fdf38c2f0947397f0b4e39d59`، شاخهٔ `develop`) + `CATALOGS/HABITICA_SCORING.csv` (۲۲ قاعده) + `19_HABITICA_ROUTINE_SPEC.md`.
- پیادهمسازی تعاملی: چهار نوع کار (عادت / روزانه / کار امروز / پاداش)، ضریب سختی `0.1 / 1 / 1.5 / 2`، نوار XP/سطح، سکهٔ روتین، استریک، سلامت و Perfect Day. فرمولها به زبان خودمان بازنویسی شدند: `delta = 0.9747^value`، `EXP = round(delta × (1+INT×0.025) × priority × crit × 6)`، `GP = ceil(delta × priority × crit × (1+PER×0.02) × (streak/100+1))`، `HP` با `CON`، `crit` قطعی، `toNextLevel`، `diminishingReturns`، ۲۱ روز.
- **ایزولاسیون کامل**: امتیازات روتین به آزمونها، لیدربورد، سکههای Learn یا چت وصل نیست؛ هیچ کد/دارایی/رشته/فونت/رنگ/آیکونی از Habitica کپی نشده (کد آن GPL-3.0 و داراییها CC-BY-NC-SA است)؛ پوسته فقط توکنها و وکتورهای استخراجشدهٔ میمو. جزئیات حقوقی و قواعد در `19_HABITICA_ROUTINE_SPEC.md`.

## ۶. حفظشده / وضعیت

هاب تکصفحهای ۷ بخش لیبلدار · تایمر فقط داخل آزمون (کلیک ← عدد ← شروع ← معکوس، توقف/ادامه، ثبت خودکار در صفر) · جامع ۲۷۰ دقیقهٔ ثابت · «پاسخبرگ» ≠ «پاسخنامه» و بازشدن خودکار کلید در زمان خالص · تکدکمهٔ AI در سؤالات و نتیجه · لیدربورد اطلاعات خود فرد · چت مینیمال + تاریخچه · مشاوره **PARKED** · بدون Pro/پرداخت/MAX · صفحهٔ ورود حذفشده · RTL + حالت شب · ۱۴ اسکرینشات فقط چک بصری.

**DESIGN v6** بایگانی شد. خروجی نهایی: `DESIGN/index.html` (۱۵ نمای تعاملی، ۶ تب، ۹۰ وکتور SVG، ۱۲۵/۱۲۵ آیکن رنگشده، ۰ خطای jsdom). **منتظر تأیید نهایی شما**؛ بعد از «مرحلهٔ بعد» تازه P0 پیادهمسازی شروع میشود.
