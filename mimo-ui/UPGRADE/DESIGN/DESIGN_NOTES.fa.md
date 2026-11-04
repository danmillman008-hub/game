# یادداشتهای طراحی — DESIGN v9

> نسخهٔ جاری: **DESIGN v9 · REVIEW** (منتظر تأیید نهایی). نسخههای **DESIGN v6 / v7 / v8** بایگانی حسابرسیاند. همچنان **فقط پلن/دیزاین**؛ هیچ کد محصولی نوشته نشده است.

## ۱. اصل حاکم

بازآفرینی ۱۰۰٪ بخشهای اصلی میمو **از داخل کد و مهندسی معکوس**؛ ۱۴ اسکرینشات فقط `VISUAL_CROSSCHECK_ONLY`. منابع: `CATALOGS/DESIGN_TOKENS.json` (ARSC)، `SOURCE/values/values/dimen.xml`، `SOURCE/values/values/string.xml`، `SOURCE/res/drawable/*.xml`، `SOURCE/res/anim/`, `SOURCE/dex/UI_CLASSES.json`، `test-tracks.json`. فقط نام درسها/فصلها/مباحث کنکوری میشود؛ ۰ رنگ/فونت/شعاع/آیکون تازه.

## ۲. گرهها (دور نهم): یک خط عمودی واحد

همهٔ ۶ گره روی **محور x=196**، بدون قوس، بدون زانوی `Q`، بدون زیگزاگ. مسیر **یک `<path>` صاف `M196 0 V620`** با `linearGradient` سخت در محل گرهٔ فعلی (`41.61%`). مختصات هم در بیلد و هم در رانتایم از `NODE_CODE_GEOMETRY.json::nodeGeometry` خوانده میشود.

اعداد از کد (جایگزین حدسهای v8): شعاع **۱۶dp** (`glance_component_btn_square.xml → dimen`)، ضخامت خط **۶dp** (`lesson_progressbar_height`)، فاصلهٔ گرهها **۱۲dp** (`spacing_s`)، آیکن **۴۸dp** (`glance_component_btn_circle.xml`)، گرادیان سهلایهٔ `progress_bar_chapter.xml`، شکل `ic_square_rounded.xml`، بولتهای واقعی `ic_bolt_charged` / `ic_bolt_mastered`، انیمیشن ۲۲۰/۴۰۰ms از `rc_checkpoint_window_*`.

توالی خطی: انجامشده / انجامشده / فعلی (½ یا `ic_play`) / **بعدیِ بدون قفل** / بولت شارژشده / بولت تسلطیافته. حلقهٔ دوتایی سفید، گرادیان بنفش، تیک `ic_check_white`، نقطهچین و کتاب شناور حفظ شدند. **هیچ گرهٔ قفلی** وجود ندارد؛ تنها قفل همان کارت «آزمون نهایی / دو هفتگی» هاب آزمونهاست.

## ۳. مصوبات پابرجا

روتین روزانه و کل ایدهٔ Habitica حذف · دیکته حذف · یادداشتهای توضیحی داخل UI حذف (شواهد نامرئی `data-code`/`data-lh`) · **۷ بخش لیبلدار / قالب فیلد / پاسخنامهٔ تشریحی نگه داشته شد** · ۵ تب، `MAX` ممنوع · ظاهر آزمونها فقط پوستهٔ میمو (بدون تغییر معماری/تایمر/۲۷۰ دقیقه/پاسخبرگ≠پاسخنامه) · بولت ← `section-practice` جدا از آزمون · لیدربورد selfbox بدون Promotion Zone · چت مینیمال · RTL/شب · بدون Pro/پرداخت/MAX · «وارد کردن کلید API» فقط یادداشت.

## ۴. حقوقی / clean-room

هیچ دارایی، فونت، رشته یا کدی از Mimo 9.35، Hamdars، Hadaf Plus، LearnHarness، EPM یا Habitica کپی نشده است. subscription/cart/Pro و اسکرینشات رانتایم ممنوعاند.

## ۵. شواهد و وضعیت

`DESIGN/CODE_GEOMETRY.json` + `LEARN_CODE_GEOMETRY.json` + `NODE_CODE_GEOMETRY.json` (v9) → `tools/build_design_v9.py` → `DESIGN/index.html`. ۱۴ نما / ۵ تب / ۹۳ وکتور SVG / ۱۳۳ آیکن / ۰ خطای jsdom / وریفایر PASS. منتظر **تأیید نهایی**؛ بعدش تازه P0 شروع میشود.
