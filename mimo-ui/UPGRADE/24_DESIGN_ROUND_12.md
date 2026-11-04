# دور دوازدهم طراحی — DESIGN v12 (بازسازی سطوح آزمون روی معماری واقعی میمو)
<!-- v12-banner -->
> ✅ **DESIGN v12 · CURRENT** — لاگ دور دوازدهم، جایگزین v11. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.

> **وضعیت:** `DESIGN v12 · REVIEW` — منتظر تأیید نهایی. همچنان **فقط پلن/دیزاین**؛ هیچ کد محصولی نوشته نشده.
> جایگزین `23_DESIGN_ROUND_11.md` بهعنوان حکم فعلی **سطوح آزمون**. معماری قوسدار، ۵ تب، لیدربورد «وضعیت من» و ۳ کارت برنامهمحور **دستنخورده**اند.
> **مسیر برگشت:** `tools/design_v11_full.html` (همان نسخهٔ تحویلشدهٔ قبل از این دور).

---

## ۱. مشکل و حکم

بخش آزمون یک «پوستهٔ جداگانه» (`class="screen konkur"`) با رنگ/تایپ/چیدمان خودش بود و انگار از اپ دیگری آمده بود. این دور آن پوسته **حذف** شد؛ سه صفحهٔ `exam-hub` / `exam-run` / `exam-result` حالا `exv12`اند و دقیقاً از همان توکنهای ARSC، وکتورها و تایپوگرافی بقیهٔ پروتوتایپ میمو استفاده میکنند.

**کد مبناست، اسکرینشات فقط چک بصری.** شواهد ماشینخوان: `DESIGN/EXAM_UI_CODE_EVIDENCE.json`.

## ۲. اصلاح دکمهها (موضوع اصلی درخواست)

| قبل (v11) | **بعد (v12)** |
|---|---|
| `.qnav`: دو دکمهٔ هموزن «سؤال قبل» + «سؤال بعد» | `.lk-row`: **یک** CTA بنفش تمامعرض `#nextQ` |
| `.qfoot`: نوار افقی اسکرولی ۷ دکمهای | دو مربع ۴۸dp چپ: `#prevQ` (سؤال قبل) و `#markQ` (علامتگذاری) |
| گزینهها: ردیفهای ساده با حاشیهٔ بنفش | `choice_list_item.xml`: کارت ۱۲dp، رادیو، minHeight ۴۸dp |
| بدون بازخورد | پنل `lesson_interactive_feedback_bottom_sheet_dialog` (سبز/قرمز + توضیح مبحث) |

منبع ساختار: **`interaction_keyboard_view.xml`** — خط ۱dp بالا، `btn_reset`/`btn_undo` مربعی ۴۸dp سمت چپ، و `RunButton` سمت راست که یا `btn_play` ۴۸dp نشان میدهد یا **`btn_continue_big` / `btn_submit` تمامعرض**. `run_button_view.xml` تأیید میکند CTA عرض کامل و حداقل ۱۴۰dp دارد. اسکرینشات `mimo-04-lesson-continue.jpg` همان دکمهٔ بنفش تمامعرض `CONTINUE` را نشان میدهد (فقط چک بصری).

**چرخهٔ واقعی سؤال** (از روی رشتهها):
1. `interaction_hint_single_choice` = «Tap the correct answer» → «گزینهٔ درست را انتخاب کنید».
2. انتخاب گزینه → CTA میشود `lesson_submit` = «بررسی پاسخ».
3. کلیک → `multiplechoice_background_correct/wrong` + پنل بازخورد با توضیح مبحث و ارجاع به کتاب.
4. CTA میشود `lesson_continue` = **«ادامه»** → سؤال بعد.
5. `lesson_skip` = «رد کردن سؤال» لینک آرام زیر فوتر؛ `#prevQ` سؤال قبل؛ پرش مستقیم از طریق پاسخبرگ.

## ۳. سه صفحه، جزءبهجزء

### نوار بالا — `chapter_toolbar.xml` (۵۲dp)
`btn_lesson_close` (`ic_close` → خروج) | مرکز: نام آزمون + `pb_chapter` نوار پیشرفت **۶dp** (`lesson_progressbar_height`, استایل `ProgressBarChapter`) | `timerChip` (تایمر، فقط داخل آزمون، ۲۷۰ دقیقهٔ ثابت) | `btn_lesson_report` (`ic_flag` → پاسخبرگ). خط زیرین ۱dp `line_primary`.

### بدنه — `lesson_interactive_multiplechoice_fragment.xml`
`ScrollView` با `lesson_content_margin_top=8dp`؛ `LessonDescriptionView` (TextH2 ۲۰sp / TextP1 ۱۸sp) بعنوان صورت سؤال؛ `tv_multiplechoice_hint`؛ `rv_multiplechoice_options` با ۴ گزینه (شعاع ۱۲dp، حاشیهٔ ۲dp، `selection_selected` / `support_green` / `support_coral`). فاصلهها ۴/۸/۱۲/۱۶/۲۴/۳۲dp و شعاعها ۱۲/۱۶dp مستقیماً از `dimen.xml`.

اقدامات ثانویه (پاسخبرگ، پاسخنامه، AI، اتمام، توقف/تنظیم مجدد تایمر، خروج) از نوار اسکرولی به **ردیف چیپهای آرام** بالای فوتر منتقل شدند؛ هیچکدام حذف نشدند.

### هاب آزمونها — `quiz_introduction_fragment.xml`
کارت معرفی (`ic_mimo_mascot` + عنوان + توضیح) + چیپهای فیلتر + **۷ بخش لیبلدار** (همان قالبها و «زمان ثابت ۲۷۰ دقیقه» محفوظ). شبکهٔ ۳ ستونهٔ گرهمانند تبدیل شد به **ردیفهای لیستی میمو**: آیکون ۴۴dp در مربع ۱۲dp + عنوان + حاشیهٔ `card_pressed`؛ دقیقاً ۲۱ ردیف و همان **یک قفل** «آزمون نهایی».

### نتیجه — `lesson_awesome_fragment.xml` / `chapter_finished_*`
صفحهٔ celebration: ماسکوت، «آزمون تمام شد!»، کارت آمار، کارت «صورت اشتباهات (منتقلشونده به AI)» و ردیف ۳ دکمه. پاسخنامه بهصورت خودکار بعد از آزمون جامع باز میشود.

## ۴. شواهد کد (همه از APK دیکدشده)

| فایل | آنچه گرفتیم |
|---|---|
| `chapter_toolbar.xml` | X، نوار ۶dp، پرچم، خط ۱dp، ارتفاع ۵۲dp |
| `lesson_interactive_fragment.xml` / `..._multiplechoice_fragment.xml` | ساختار ScrollView + Description + ChoiceView + Keyboard |
| `choice_view.xml` / `choice_list_item.xml` / `layout_choice_card_item.xml` | hint، RecyclerView، رادیو، TextP1 ۱۸sp، ۴۸dp |
| `multiplechoice_background_*.xml` | ۴ حالت unselected/selected/correct/wrong |
| `interaction_keyboard_view.xml` / `run_button_view.xml` | فوتر ۶۸dp، مربعهای ۴۸dp، CTA تمامعرض |
| `lesson_interactive_feedback_bottom_sheet_dialog.xml` | پنل بازخورد، `drawer_bottom_sheet_background` |
| `quiz_introduction_fragment.xml` | کارت معرفی + CTA شروع |
| `string.xml` | `lesson_continue` / `lesson_submit` / `lesson_skip` / `interaction_hint_single_choice` |
| `dimen.xml` / `color.xml` / `style.xml` | ۴…۴۰dp، رنگها، TextH1/H2/P1/P2/Label1/Button1 |

## ۵. بدون تغییر (مصوبات پابرجا)

معماری اورجینال قوسدار (۸۰/۱۹۶/۳۱۲، فاصلهٔ ۲۴dp، زانوهای `Q` ۳۲dp) · ۵ تب و `MAX` ممنوع · لیدربورد فقط «وضعیت من» · ۳ کارت برنامهمحور + ۱۲ کورس مبحثی · بدون آرم برنامهنویسی · روتین/Habitica و دیکته حذفشده · بدون یادداشت داخل UI · **۷ بخش لیبلدار + قالب فیلد + پاسخنامهٔ تشریحی** · تایمر فقط داخل آزمون و ۲۷۰ دقیقهٔ ثابت · «پاسخبرگ»≠«پاسخنامه» · تکدکمهٔ AI · **صفر قفل یادگیری** و تنها قفل «آزمون نهایی / دو هفتگی» · بولت ← `section-practice` جدا · چت مینیمال · ۱۴ اسکرینشات فقط **چک بصری**.

## ۶. تحویل

`tools/build_design_v12.py` (از `design_v11_full.html`) → `DESIGN/index.html` ۴۰۶٬۶۱۶ بایت / ۱۴ نما / ۵ تب / ۹۳ وکتور / ۰ خطای jsdom. `tools/finalize_v12.py` → کاتالوگها/داکیومنتها/منیفست. `verify_upgrade.py` PASS، `check_v12.js`، `node --check` OK. تأیید نهایی همچنان **PENDING**؛ هیچ کد محصولی نوشته نشده.
