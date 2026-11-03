# ۰۱ — روش کار و طبقهبندی شواهد

## ریپوی مورد استفاده

[`morluto/rea` — «Reverse Engineer Anything»](https://github.com/morluto/rea) را به عنوان
**چارچوب روششناسی** به کار بردیم (شاخهٔ `main`، نسخهٔ کلونشده در این نشست). اصول گرفتهشده:

- «بستهٔ ارسالشده» (shipped artifact) منبع حقیقت است؛ ادعاها باید به بایت/هش/محل دقیق وصل باشند.
- تفکیک **مشاهده** (observation) / **استخراج** (derivation) / **استنتاج** (inference) / **ناشناخته**.
- حفظ **پوشش و محدودیتها**: نبود شاهد ≠ نبود ویژگی؛ نتایج جزئی باید برچسب بخورند.
- هش و محل ورودی حفظ شود؛ بسته هرگز تغییر نکند.
- تحلیل ایستا، اجرا نیست: manifest/DEX/منابع مشاهدهٔ ایستا هستند، رفتار zaman اجرا نیست.

علاوه بر روش، **CLI رسمی همان ریپو** هم اجرا شد:

```
npx -y rea-agents@6.8.0 analyze-javascript-application SOURCE/assets/ui \
  --source-path lesson-webview.js --source-path lesson-webview-fonts.js … \
  --analysis-timeout-ms 120000 --format json
```

خروجی کامل و دستنخوردهٔ آن در `REFERENCE/REA_EVIDENCE/JS_EVIDENCE.json` است
(`evidence_id = ev_a3135ad9dd9a6441f057ed5dd2a23e3dd08c98780f79b2dc13953a0ea62f4a58`، ۳۳ فایل موجودی، ۲ فایل JS پارسشده، ۱٬۱۸۶ گره AST،
۸ محدودیت اعلامشده). تلاش برای تحلیل کل پوشه با باندلهای ۱–۲ مگابایتی Prettier/Spieglein
با `provider_timeout` مواجه شد؛ بنابراین انتخاب دقیق ۱۵ فایل نوشتهشده توسط خود Mimo انجام شد
و ۱۸ فایل خارج از دامنه **صادقانه** در شواهد REA علامت خوردهاند.

## زنجیرهٔ شواهد (کاملاً بازتولیدپذیر)

```
Google Drive/پوشهٔ `mimo`/  →  3 بخش z01+z02+zip  →  cat  →  unzip  →  Mimo_9.35 (1).apk
        ↓ هش هر ۳ بخش + هش APK (مطابق REFERENCE/PRIOR_WORK/APK_HASHES.json)
   zipfile + androguard 4.1.4 (AXML / ARSC / DEX) + REA CLI 6.8.0
        ↓
   SOURCE/ (عیناً یا دیکد)  →  CATALOGS/ (فهرست کامل)  →  SCREENS/ (پروندهها)  →  ATLAS/
        ↓
   tools/verify_ui.py  →  VERIFICATION_REPORT.json + SHA256SUMS.txt
```

| ابزار | نسخه | نقش | وضعیت |
|---|---|---|---|
| `androguard` | ۴٫۱٫۴ (PyPI) | AXML، ARSC، DEX، manifest | ✅ |
| `rea-agents` (CLI) | ۶٫۸٫۰ (npm) | شواهد رسمی JS/WebView | ✅ (با انتخاب مسیر) |
| `zipfile` / `hashlib` | Python ۳٫۱۱ | موجودی و هش | ✅ |
| Python خالص | — | ساخت پروندهها/اطلس/بازسازی | ✅ |
| JADX / Java 17 | — | دیکامپایل بدنهٔ متدها | ❌ در محیط موجود نبود |
| apktool / aapt2 / bundletool | — | — | ❌ |
| adb / emulator | — | تست زمان اجرا | ❌ |

**نتیجهٔ صادقانه:** کد XML/JS/CSS/ARSC «واقعی» است (دیکد بیهزینه)، ولی بدنهٔ متدهای
Kotlin/Java **دیکامپایل نشده**؛ به جای ادعای سورس، فهرست کامل کلاس/متد/آنوتیشن/لیترال/منبع
و ۱۰۹ اسکلت بازسازیشده با برچسب `RECONSTRUCTED` ارائه شد. این محدودیت در `11` و `13` ثبت شده.

## طبقهبندی ۱۴٬۳۹۸ عضو بسته

| کلاس | تعداد | رفتار |
|---|---|---|
| CONTENT_DATA | 10,308 | فهرست کامل با هش |
| UI_DRAWABLE | 1,319 | عیناً/دیکد + پرونده |
| UI_LAYOUT | 1,299 | عیناً/دیکد + پرونده |
| NON_UI | 633 | فهرست کامل با هش |
| UI_COLOR_STATE | 304 | عیناً/دیکد + پرونده |
| UI_WEBVIEW_ASSET | 254 | عیناً/دیکد + پرونده |
| UI_MOTION | 143 | عیناً/دیکد + پرونده |
| UI_RAW_ASSET | 76 | عیناً/دیکد + پرونده |
| UI_FONT | 15 | عیناً/دیکد + پرونده |
| UI_XML_CONFIG | 15 | عیناً/دیکد + پرونده |
| DEX_CODE | 12 | فهرست کامل با هش |
| NATIVE | 12 | فهرست کامل با هش |
| UI_MENU | 5 | عیناً/دیکد + پرونده |
| UI_MANIFEST | 1 | عیناً/دیکد + پرونده |
| UI_NAVIGATION | 1 | عیناً/دیکد + پرونده |
| UI_RESOURCE_TABLE | 1 | عیناً/دیکد + پرونده |

هر ردیف از `CATALOGS/APK_ENTRY_CENSUS.csv` شامل `sha256`، `crc32`، اندازه، کلاس، دلیل طبقهبندی
و **مسیر دقیق فایل تحویلی** است. کلاسهای `CONTENT_DATA` (محتوای درس) کد UI نیستند، ولی
تکتکشان با هش کامل فهرست شدهاند — «هیچی نمونه» در اینجا یعنی حتی دادهها هم گم نشدهاند.

## قاعدهٔ دیکد AXML

فایلهای `res/*.xml` در APK باینری AXML هستند. دیکد با `AXMLPrinter` انجام شد و سپس:

- `@7F0A013B` → `@id/chapter_activity_root` (حل شناسه از `resources.arsc`)
- `@7F060028` → `@color/background_secondary`
- `-1` / `-2` در `layout:width`/`layout:height` → `match_parent` / `wrap_content`
- مقادیر بولین/ابعاد/رنگ/کسری بر اساس `Res_value.data_type` فرمت شدند

نسخهٔ **خام قبل از این تبدیلات** در `SOURCE/_raw_axml/ALL_RAW_DECODED.json.gz` نگه داشته شده،
پس هیچ اطلاعاتی از بین نرفته است. صفر خطای دیکد ثبت شده (`CATALOGS/DECODE_ERRORS.json` خالی است).
