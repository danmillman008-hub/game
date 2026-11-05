# MISSION 04 — یکپارچگی APK (APK INTEGRITY)

| شناسه | مقدار |
|---|---|
| Workflow run ID (M04) | `41991896800` (presence-only probe؛ **هیچ APKـای روی runner دانلود نشد**) |
| Workflow run ID (مرجع شبیهساز M03) | `41951780483` |
| Branch / commit | `arena/aebb90b7-game` / `1ca5d6bc2c761c3555d189d5160e8f8316362fed` |
| پیکربندی شبیهساز | API 36 / Android 16 / `pixel_7` / `google_apis` / `x86_64` / headless |
| APK SHA-256 کامل | `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` |
| اندازه | `142353499` بایت |
| Timestamp | `2026-11-05T08:02Z` |
| برچسبها | `OBSERVED` (تطابق محلی) / `BLOCKED` (تطابق روی runner) / `UNKNOWN` (فایل نصبشده) |

## ۱. هش کامل — `OBSERVED`

پرامپت هشدار داد: «Do not trust the abbreviated hash. Retrieve and compare the complete
original hash». هش ۶۴ رقمی کامل از دو منبع مستقل گرفته و مقایسه شد:

| منبع | فرمان / مسیر | نتیجه |
|---|---|---|
| پایگاه شواهد | `ANALYSIS/EVIDENCE_INDEX.json` → `EV-0001` | `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` |
| کپی مجاز workspace | `sha256sum '/home/user/_work/apk/Mimo_9.35 (1).apk'` | همان ۶۴ رقم، **تطابق کامل** |
| اندازه | `stat -c %s` | `142353499` — مطابق `APK_COMPLETE_INVENTORY.json` |
| اسناد M03 | جستوجوی ۹ هش ۶۴رقمی دیگر | مربوط به سه_part Drive و سایر پروندهها؛ **هیچکدام هش APK تلقی نشد** |

پیشوند `48ce1740` و پایان `7c7a` تأیید شد، ولی **صرفاً بهعنوان تطابق کمکی**؛
مبنای تصمیم، هش ۶۴رقمی کامل بود.

## ۲. تطابق هشِ APK دریافتشده روی runner ⇒ `BLOCKED`

معیار ۳ مأموریت، تطبیق SHA-256 **APKـای است که به runner رسیده**، نه کپی محلی.
هیچ دانلودی انجام نشد ⇒ `sha256sum "$RUNNER_TEMP/MIMO_ORIGINAL.apk"` اجرا نشد،
پروندهٔ `APK_SHA256.txt` تولید نشد، و گام «Fail immediately if checksum differs»
هرگز فراخوانی نشد.

این تمایز عمداً حفظ میشود تا «تطابق هش محلی» بهاشتباه بهعنوان
«تطابق هش APK مستقرشده روی دستگاه» ارتقا نیابد.

## ۳. محافظت از یکپارچگی در workflow — `OBSERVED`

بدون اینکه اجرا شود، مسیر نرمافزاری بررسی و سختگیرانهتر شد:

- `EXPECTED_APK_SHA256` بهصورت پیشفرض همان هش کامل ۶۴رقمی است.
- `runtime_smoke.sh` پیش از نصب:
  `ACTUAL_SHA=$(sha256sum "$APK" | cut -d' ' -f1)` → مقایسه با `EXPECTED_APK_SHA256`؛
  در صورت عدم تطابق: `SHA MISMATCH -> refusing install` و **خروج بدون `adb install`**.
- هیچ APK جایگزین، هیچ بازسازی از DEX، هیچ وصلهٔ کتابخانهٔ بومی و هیچ تغییر امضا انجام نشد.
- `curl -fsSL` و redaction URL اضافه شد تا هش/منبع در لاگ افشا نشود.
- APK فقط در `$RUNNER_TEMP` خارج از مخزن نوشته میشود؛ `find "$R" -name '*.apk' -delete`
  در گام پاکسازی، و `git add -f ANALYSIS/RUNTIME` شامل `$RUNNER_TEMP` نمیشود.

## ۴. وضعیت نهایی یکپارچگی

| گزاره | برچسب |
|---|---|
| هش کامل APK اصلی از `EV-0001` و کپی workspace تطابق دارد | `OBSERVED` |
| هش APK دانلودشده روی runner تطابق داده شد | `BLOCKED` |
| هش APK نصبشده / امضای نصبشده روی دستگاه | `UNKNOWN` |
| امضای v2+v3 و سلامت ZIP (M02 `EV-M02-0003`) | `OBSERVED` (بدون تغییر، بدون اجرا) |

**ارجاع شواهد:** `LOGS/APK_SOURCE_INVESTIGATION.txt`،
`../runtime_smoke.sh` (بخش `APK_URL supplied`)،
`.github/workflows/mimo-runtime-verification.yml`،
`ANALYSIS/EVIDENCE_INDEX.json` → `EV-0001`.
