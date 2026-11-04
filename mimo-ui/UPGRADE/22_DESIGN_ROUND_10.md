# دور دهم طراحی — DESIGN v10 (بازگشت به معماری اورجینال قوسدار)
<!-- v11-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v11](23_DESIGN_ROUND_11.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.
<!-- v10-banner -->
> ✅ **DESIGN v10 · CURRENT** — لاگ دور دهم، جایگزین v9. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.

> **وضعیت:** `DESIGN v10 · REVIEW` — منتظر تأیید نهایی. همچنان **فقط پلن/دیزاین**؛ هیچ کد محصولی نوشته نشده.
> **گفتۀ شما:** «من حرفمو پس میگیرم … همون معماری اورجینال رو به کار ببر … اون خطی که قوس داشت … بیشتر کد رو بکاوی و دقیقاً بازسازی کن».
> نتیجه: **درخواست دور نهم (خط صاف تکمسیر) لغو شد** و معماری اصلی میمو برگشت، منتها با کاوش عمیقتر کد. جایگزین `21_DESIGN_ROUND_9.md`.

---

## ۱. برگشت معماری اورجینال

| | v9 (لغوشد) | **v10 (اورجینال)** |
|---|---|---|
| لاینها | فقط `x=196` | **`۸۰ / ۱۹۶ / ۳۱۲`** (چپ / وسط / راست) |
| جابهجایی | صفر | **center → right → center → left → center → left** |
| فاصلهٔ بین گرهها | ۱۲dp (تقریباً چسبیده) | **۲۴dp واقعی** (`spacing_l`) |
| مسیر | ۱ خط صاف `M196 0 V620` | **۲ قطعهٔ رنگی با ۵ زانوی گرد `Q`** |
| شعاع زانو | — | **۳۲dp** (`spacing_xl`) |
| الگوی زانو | — | **A/B/A/B/B** (خروج افقی←ورود عمودی / خروج عمودی←ورود افقی) |

شبکه کاملاً از `dimen.xml` استخراج شد: گام `۱۱۶ = ۹۲ + ۲۴` هم برای فاصلهٔ عمودی و هم فاصلهٔ لاینها، `viewBox 392×720`، حاشیهٔ بالا/پایین ۲۴dp. مسیر بنفش (`progress_chapter_primary`) تا گرهٔ فعلی و یاسی (`progress_chapter_background`) بعد از آن؛ دقیقاً همان چیزی که در `mimo-01` / `mimo-02` / `mimo-10` دیده میشود (فقط **چک بصری**).

```
done  = M242 70 H280 Q312 70 312 102 V140  ·  M312 232 V270 Q312 302 280 302 H242
next  = M150 302 H112 Q80 302 80 334 V372  ·  M80 464 V502 Q80 534 112 534 H150
        M196 580 V618 Q196 650 164 650 H126
```

## ۲. کاوش عمیقتر کد (خواستهٔ اصلی این دور)

| منبع | یافتهٔ تازه |
|---|---|
| `SOURCE/dex/UI_CLASSES.json` | **۹۲ کلاس** `PathMapScreenKt` / `PathMapViewModel` / `ViewsKt$PathMap` / `TutorialSpotlightKt` / `PracticeOptionalIntroKt` / `GetPathMapState/Dialogs` / `ModalData$SmartPractice*`، در ۵ گروه |
| همان | `Lcom/getmimo/ui/streaks/ArcProgressView;` با `getFinishedStrokeColor()` / `getUnfinishedStrokeColor()` / `setStrokeWidth(F)` / `onDraw(Canvas)` / `RectF` → مبنای مفهوم **دو رنگ خط** |
| `assets/ui/testdata/test-tracks.json` | **۱۵ فصل / ۲۲۳ `tutorialId`** با `startIndex`/`endIndex`؛ شمارهٔ ترتیب هر گره به فصل متناظر نگاشت شد (`data-section`) |
| `values/values/dimen.xml` | ۱۳۹۶ دایمنشن: `spacing_l=24`، `spacing_xl=32`، `glance_component_btn_circle=48dp`، `lesson_progressbar_height=6` |
| `res/drawable/progress_bar_chapter.xml` | ۳ لایهٔ layer-list (پسزمینه / کممرنگ / اصلی) با شعاع ۱۰۰dp |
| `res/drawable/dotted_border_background.xml` | stroke 2dp / dash 8dp / gap 8dp → نقطهچین پسزمینه |
| `res/drawable/glance_component_btn_square.xml` | شعاع ۱۶dp **مال دکمهٔ مربعی Glance widget** است، نه گرهٔ مسیر |
| `res/anim/rc_checkpoint_window_*.xml` | ورود ۲۲۰ms / خروج ۴۰۰ms |
| ۱۰ وکتور `pathData` | `ic_check_white`, `ic_play`, `ic_square_rounded`, `ic_flash`, `ic_bolt`, `ic_bolt_charged`, `ic_bolt_mastered`, `ic_mascot_practice`, `ic_check_thick`, `ic_tab_practice` |

**دو انتساب اشتباه v9 اصلاح شد:** شعاع گره **۲۶dp** برگشت (۱۶dp مال Glance widget بود) و ضخامت مسیر **۱۰dp** برگشت (۶dp مال نوار پیشرفت **درس** بود، نه خط مسیر). آیکن ۴۸dp، وکتورهای واقعی بولت، گرادیان سهلایه، گرهٔ «بعدیِ بدون قفل» و تایمینگ ۲۲۰/۴۰۰ms از v9 **حفظ** شدند.

## ۳. حالتها و قفلها

`انجامشده → انجامشده → فعلی (حلقهٔ ½ / نسخهٔ ic_play) → بعدی (روشن، ic_square_rounded، **بدون قفل**) → ic_bolt_charged → ic_bolt_mastered`. گرهٔ فعلی همان کارت سفید حلقهدوتایی است؛ حالت ½ / پلی با دکمههای پنل بازبینی (بیرون گوشی) قابل نمایش است. **صفر گرهٔ قفلی** در یادگیری / داخل مبحث / تمرین مبحث؛ تنها قفل مجاز همان **«آزمون نهایی / دو هفتگی»** بخش ۶ هاب آزمونهاست، دستنخورده.

## ۴. بدون تغییر

۵ تب (`MAX` ممنوع) · روتین روزانه / Habitica حذفشده · دیکته حذفشده · هیچ یادداشت طراحی/سیاست/EPM/تایمر داخل UI · **۷ بخش لیبلدار + قالب فیلد + پاسخنامهٔ تشریحی نگه داشته شد** · تایمر فقط داخل آزمون، ۲۷۰ دقیقهٔ ثابت، «پاسخبرگ» ≠ «پاسخنامه»، تکدکمهٔ AI · ظاهر میمویی آزمونها (فقط پوسته) · بولت ← `section-practice` جدا از هاب · لیدربورد بدون Promotion Zone · چت مینیمال · RTL/فارسی + شب · ۱۴ اسکرینشات فقط **چک بصری**.

## ۵. تحویل

`extract_mimo_nodes_v10.py` → `NODE_CODE_GEOMETRY.json` (۱۴۴٬۵۸۴ بایت، `round: v10`) + `MIMO_PATH_NODES.csv` (**۱۰۶ ردیف**) → `build_design_v10.py` (از تمپلیت پاک v9) → `DESIGN/index.html`. ۱۴ نما / ۵ تب / ۹۳ وکتور SVG / ۱۳۳ آیکن / ۶ گره / ۲ مسیر / ۵ قوس / ۰ قفل یادگیری / `node --check` OK / jsdom **۰ خطا** / وریفایر PASS. **DESIGN v9** بایگانی شد؛ تأیید نهایی همچنان **PENDING** و هیچ کد محصولی نوشته نشده است.
