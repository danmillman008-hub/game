# یادداشتهای طراحی — DESIGN v10

> نسخهٔ جاری: **DESIGN v10 · REVIEW** (منتظر تأیید نهایی). نسخههای **DESIGN v6 / DESIGN v7 / DESIGN v8 / DESIGN v9** بایگانی حسابرسیاند. همچنان **فقط پلن/دیزاین**؛ هیچ کد محصولی نوشته نشده.

## ۱. اصل

کد مبناست (`ARSC`، `dimen.xml`، `drawable/*.xml`، `pathData`، `anim`، `DEX`، `test-tracks.json`)؛ ۱۴ اسکرینشات فقط `VISUAL_CROSSCHECK_ONLY`. فقط نام درسها/فصلها کنکوری میشود؛ ۰ رنگ/فونت/شعاع/آیکون تازه.

## ۲. معماری اورجینال قوسدار (بازگشته)

درخواست «خط صاف» دور نهم **پس گرفته شد**. سه لاین `۸۰/۱۹۶/۳۱۲`، ترتیب `center/right/center/left/center/left`، فاصلهٔ **۲۴dp** (`spacing_l`) و گام ۱۱۶dp، زانوهای گرد `Q` به شعاع **۳۲dp** (`spacing_xl`) با الگوی `A/B/A/B/B`، دو قطعهٔ رنگی مسیر (بنفش تا گرهٔ فعلی، یاسی بعد از آن)، `viewBox 392×720`. شعاع گره **۲۶dp**، ضخامت مسیر **۱۰dp**، آیکن **۴۸dp**؛ ۱۶dp مال Glance widget و ۶dp مال نوار پیشرفت درس است. حالتها: انجامشده×۲ / فعلی (½ یا `ic_play`) / بعدیِ **بدون قفل** / `ic_bolt_charged` / `ic_bolt_mastered`. حلقهٔ دوتایی سفید، گرادیان سهلایهٔ `progress_bar_chapter`، نقطهچین و کتاب شناور حفظ شدند.

## ۳. کاوش عمیق کد

۹۲ کلاس `PathMap*`ی DEX در ۵ گروه، `ArcProgressView` با رنگهای finished/unfinished و `setStrokeWidth(F)`، **۱۵ فصل / ۲۲۳ `tutorialId`** از `test-tracks.json` با `startIndex/endIndex` که به `data-section` گرهها نگاشت شد، ۱۰ شِیپ AXML، ۱۰ وکتور `pathData`، ۱۳۹۶ دایمنشن، انیمیشن چکپوینت ۲۲۰/۴۰۰ms.

## ۴. مصوبات پابرجا

۵ تب (`MAX` ممنوع) · حذف روتین/Habitica و دیکته · حذف یادداشتهای داخل UI · **نگهداری ۷ بخش لیبلدار / قالب فیلد / پاسخنامهٔ تشریحی** · بدون تغییر معماری/تایمر/۲۷۰ دقیقه/«پاسخبرگ»≠«پاسخنامه» · **صفر گرهٔ قفلی** و تنها یک قفل «آزمون نهایی / دو هفتگی» در هاب · بولت ← `section-practice` جدا · لیدربورد selfbox بدون Promotion Zone · چت مینیمال · RTL/شب · بدون Pro/پرداخت · «وارد کردن کلید API» فقط یادداشت.

## ۵. clean-room و وضعیت

هیچ دارایی/کدی از Mimo، Hamdars، Hadaf Plus، LearnHarness، EPM یا Habitica کپی نشده. `DESIGN/index.html` از `NODE_CODE_GEOMETRY.json` هم در بیلد و هم رانتایم رندر میشود: ۱۴ نما / ۵ تب / ۹۳ وکتور / ۱۳۳ آیکن / ۰ خطای jsdom / وریفایر PASS. منتظر **تأیید نهایی**؛ بعدش تازه P0.
