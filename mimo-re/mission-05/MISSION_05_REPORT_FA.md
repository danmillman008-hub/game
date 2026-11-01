# مأموریت ۵ — گزارش فارسی (خلاصه)

## Scope / دامنه
مهندسی معکوس نسخهٔ ۹.۳۵ اپلیکیشن Mimo (`com.getmimo`، versionCode 1792759685) بر پایهٔ داده‌های
موجود در مخزن؛ فقط **مشخصه‌سازی** (specification)، بدون ساخت کلون، بدون اجرای اپ، بدون تغییر APK.
هیچ متن، کد، گرافیک یا برند اختصاصی بازتولید نشده است.

## Method / روش
۱) همهٔ یافته‌های پیشین **پیش از اتکا** بازاعتبارسنجی شدند؛ دو آرتیفکت قدیمی (دامپ annotation و
کاتالوگ API) مردود شدند و از نو ساخته شدند. ۲) مکان‌یابی کد با **xref در سطح دستور** انجام شد، نه با
جست‌وجوی نام. ۳) ۳٫۳۲۳ کلاس با androguard DAD **بیرون از مخزن** (`/tmp/dad`) دیکامپایل شد؛ فقط
فهرست‌ها و کاتالوگ‌های مشتق‌شده commit می‌شوند.

## Sources / منابع
`evidence/DECOMPILE_MANIFEST_*.json` (هش SHA-256 هر dex، نسخهٔ ابزارها، زمان‌بندی)،
`evidence/API_CATALOG_V2.csv`، `evidence/ANNOTATIONS_V2.csv`، `evidence/DTO_CATALOG.csv`،
`evidence/ROOM_SQL_LITERALS.csv`، `evidence/TAG_ENUM.json`.

## Findings / یافته‌ها
- **پارسر درس تعاملی، کلاس‌های مبهم‌سازی‌شدهٔ `te.a`–`te.g` است** و بیرون از بستهٔ `com.getmimo` قرار
  دارد؛ بستهٔ `lessonparser` فقط **مدل‌ها** را دارد. این مهم‌ترین تصحیح ساختاری مأموریت است.
- زبان محتوا HTML-گونه است با **۲۹ تگ** (`Tag` با ترتیب ۰ تا ۲۸)، از جمله `code`, `content`,
  `interactions`, `interaction`, `options`, `option`, `output`, `collapsibleLines`.
- ارزیابی «ورودی اعتبارسنجی‌شده» نرمال‌سازی می‌شود: `toLowerCase(Locale.US)` و نگه‌داشتن فقط حروف،
  رقم، `<` و `.`؛ نتیجه سه‌حالته است (درست / درست با تصحیح / نادرست) و با تأخیر **۳۰۰ میلی‌ثانیه**
  اعمال می‌شود.
- ستون `tries` **پرچم ۰/۱ درستی** است، نه شمارنده: `isSolvedCorrectly() { return tries >= 1; }`.
  شمارندهٔ واقعی `attempts` است و «موفقیت در تلاش اول» یعنی `attempts == 1 && solved`.
- پایگاه‌دادهٔ محلی فقط **سه جدول** دارد (`lesson_progress`, `chapter_completions`,
  `tutorial_completions`)، هیچ migration ثبت نشده، و ردیف‌ها پس از تأیید سرور **حذف** می‌شوند؛
  یعنی پایگاه‌داده یک **بافر ارسال** است نه آرشیو.
- **۶۲ endpoint** در ۲۹ اینترفیس: `GET 28 · POST 24 · PATCH 4 · DELETE 4 · PUT 2`؛ **۸۵ اتصال
  پارامتر** (۴۵ path، ۲۰ body، ۱۷ query، ۳ header) و **۳۴ نوع پاسخ** که پیش‌تر ناشناخته بود.
- در بستهٔ بومی: `librive-android.so` (Rive)، `libsigner.so` (امضای Adjust)، `libyrf.so` که پل JNI
  بستهٔ مبهم `bin.ghost` است و یک دیالوگ مسدودکنندهٔ ۱۰ ثانیه‌ای را کنترل می‌کند.

## Evidence labels / برچسب‌ها
همهٔ یافته‌های ساختاری **VERIFIED_STATIC**؛ فعل‌های HTTP (به‌جز PATCH/PUT) **INFERRED_HIGH**؛
PATCH/PUT **INFERRED_MEDIUM**؛ **هیچ برچسب VERIFIED_RUNTIME وجود ندارد** چون در این محیط دستگاه،
شبیه‌ساز یا `adb` نیست. ۲۶ مورد باز در `evidence/UNRESOLVED_REGISTER.csv` ثبت شده است.

## Limitations / محدودیت‌ها
- خروجی DAD «شبه‌جاوا» است: modifierها حذف می‌شوند و نام متغیرها میان شاخه‌ها بازاستفاده می‌شود؛
  بنابراین هر ادعای حساس با رشتهٔ متنی، descriptor یا محل فراخوانی دوم تقاطع داده شده است.
- نبود JDK ⇒ نبود baksmali و aapt2 ⇒ تأیید در سطح smali و رمزگشایی منابع (رشته‌ها/تم‌ها) ممکن نیست.
- کلاس‌هایی که DAD تولید نکرد (مثل `AiTutorRepository` و اسمبلر analytics) برای این مأموریت نامرئی‌اند.

## Unresolved / موارد باز
`U-01` تکمیل خواندن `te.b`–`te.g`؛ `U-20` فهرست معتبر رویدادهای analytics؛ `U-22` آدرس پایهٔ API؛
`U-23` تفکیک PATCH از PUT؛ `U-04` تأیید در سطح smali.

## Reproduction / بازتولید
```bash
/tmp/venv/bin/python tools/decompile_apk.py --dex-dir /tmp/x --out /tmp/dad --filter 'Lcom/getmimo' \
  --inventory evidence/CLASS_INVENTORY_APP.csv --manifest evidence/DECOMPILE_MANIFEST_APP.json
/tmp/venv/bin/python tools/build_api_catalog_v2.py --annotations evidence/ANNOTATIONS_V2.csv \
  --csv evidence/API_CATALOG_V2.csv --json evidence/API_CATALOG_V2.json
python -m pytest 21_AUTOMATED_VALIDATION -q     # 29 passed
```
