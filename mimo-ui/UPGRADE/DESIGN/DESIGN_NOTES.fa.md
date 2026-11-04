# یادداشتهای طراحی — DESIGN v8

> نسخهٔ جاری: **DESIGN v8 · REVIEW** (منتظر تأیید نهایی). نسخههای **DESIGN v6** و **DESIGN v7** بایگانی حسابرسیاند. همچنان **فقط پلن/دیزاین**؛ هیچ کد محصولی نوشته نشده است.

## ۱. اصل حاکم

بازآفرینی ۱۰۰٪ بخشهای اصلی میمو **از داخل کد و مهندسی معکوس**، نه از روی عکس. منابع: `CATALOGS/DESIGN_TOKENS.json` (ARSC)، `SOURCE/values/values/string.xml`، `SOURCE/res/drawable/*.xml` (`android:pathData` و شِیپها)، `SOURCE/res/layout/*.xml`، `SOURCE/dex/UI_CLASSES.json`، `test-tracks.json`. ۱۴ اسکرینشات فقط `VISUAL_CROSSCHECK_ONLY`اند. فقط **نام درسها/فصلها/مباحث** کنکوری میشود؛ ۰ رنگ/فونت/شعاع/آیکون تازه.

## ۲. اصلیترین کار دور هشتم: گرهها

`tools/extract_mimo_nodes_v8.py` → `DESIGN/NODE_CODE_GEOMETRY.json` + `CATALOGS/MIMO_PATH_NODES.csv` (۷۲ ردیف). هندسهٔ ماشینی: مربع ۹۲dp / شعاع ۲۶dp / لبهٔ سهبعدی ۸dp (`button_primary_highlight`) / گرادیان بنفش ARSC / تیک `ic_check_white` / کارت سفید حلقهدار فعلی با حلقهٔ ½ (و نسخهٔ `ic_play`) / بولت فعال `ic_flash` و بولت اختیاری `ic_bolt` / اتور **گردگوشهٔ Q** (نه بزیه) / نقطهچین ۲۶dp / کتاب شناور. شش گره و دو مسیر اتور مستقیماً از `nodeGeometry` رندر میشوند. **هیچ گرهٔ قفلی** وجود ندارد؛ تنها قفل همان کارت «آزمون نهایی / دو هفتگی» موجود در هاب آزمونهاست. برچسب START، حلقهٔ ۱۲٪ سرگردان، نقطهٔ خاکستری و چیپهای دیباگ حذف شدند.

## ۳. حذفشدهها (دستور صریح دور هشتم)

- **روتین روزانه** و **کل ایدهٔ امتیازدهی Habitica**: تب، صفحه، payload، JSON، کاتالوگها، سند و ابزارش. ناوبری ۵ تب برگشت؛ `MAX` ممنوع.
- **دیکته / Dictate** از خط پایین دستیار هوشمند.
- **یادداشتهای توضیحی داخل UI**: سیاست زمان خالص، ایدهٔ EPM، توضیح تایمر، `note/hint/sd-note/composer-note`، `codechip`، برچسبهای `.lh`، تولتیپهای `title`. شواهد به `data-code` / `data-lh` نامرئی و کاتالوگها منتقل شدند.
- توضیحات **۷ بخش لیبلدار / قالب فیلد** هاب آزمونها و **پاسخنامهٔ تشریحی** بنا به دستور شما **نگه داشته شدند**.

## ۴. ظاهر آزمونها (فقط پوسته)

وکتورهای واقعی میمو جای گلیفها: `ic_trophy`, `ic_clock_black_24dp`, `ic_task_completed`, `ic_lock_alt_02`, `ic_file`, `ic_target`, `ic_sparks_alt`, `ic_arrow_back_24`, `ic_help`. رنگ/شعاع/تایپوگرافی ARSC. **هیچ تغییر معماری**: ۷ بخش، تایمر فقط داخل آزمون، ۲۷۰ دقیقهٔ ثابت، «پاسخبرگ» ≠ «پاسخنامه»، کلید خودکار در پایان، دو دکمهٔ تمیز قبل/بعد، تکدکمهٔ «توضیح با هوش مصنوعی»، لیدربورد بدون Promotion Zone.

## ۵. تفکیک (مهم)

| سطح | جا | نشانه |
|---|---|---|
| تمرین مبحث | `data-screen=section-practice` | `mimo`، بدون تایمر/پاسخبرگ/پاسخنامه/POLICY |
| آزمون کنکور | `exam-hub / exam-run / exam-result` | `konkur`، ۷ بخش، تایمر داخل آزمون، پاسخبرگ ≠ پاسخنامه |
| قفل | فقط یک کارت در هاب آزمونها | «آزمون نهایی / دو هفتگی» |

## ۶. حقوقی / clean-room

هیچ دارایی، فونت، رشته یا کدی از Mimo 9.35، Hamdars 7.4.4، Hadaf Plus 2.0.2، LearnHarness یا EPM کپی نشده است. ایدهٔ Habitica بهکل حذف شد. subscription/cart/Pro و اسکرینشات رانتایم/امولاتور ممنوعاند.

## ۷. شواهد و اعتبارسنجی

`DESIGN/CODE_GEOMETRY.json` + `DESIGN/LEARN_CODE_GEOMETRY.json` + `DESIGN/NODE_CODE_GEOMETRY.json` → `tools/build_design_v8.py` → `DESIGN/index.html`. خروجی: ۱۴ نما، ۵ تب، ۹۳ وکتور SVG، ۱۳۳ آیکن رنگشده، ۰ خطای jsdom، `node --check` OK. `tools/verify_upgrade.py` و `CATALOGS/VERIFICATION_REPORT.json` حسابرسی نهاییاند.

## ۸. بعد از این

منتظر **تأیید نهایی** شما. فقط بعد از «مرحلهٔ بعد» پیادهمسازی P0 آغاز میشود؛ تا آن لحظه هیچ کد محصولی نوشته نشده است.
