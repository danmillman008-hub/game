# MISSION 04 — یکپارچگی فایل اصلی (APK INTEGRITY)

| شناسه | مقدار |
|---|---|
| Workflow run ID | **`41998643355`** |
| Job ID / نتیجه | `127148044003` / SUCCESS |
| Branch / commit | `arena/aebb90b7-game` / `92e87fe8d061ea4c11089f40a7c8ce73d34d816a` |
| Timestamp | `2026-11-05T09:01:45Z` |
| پیکربندی شبیهساز | API 36 / Android 16 / `pixel_7` / `google_apis` / `x86_64` / headless |
| نتیجه | `result=SHA_MATCH_OK` — **بایت به بایت همان APK** |

## ۱. زنجیرهٔ اثبات — `OBSERVED`

| مرحله | اندازه (بایت) | SHA-256 | محل شاهد |
|---|---|---|---|
| فایل اصلی workspace | `142353499` | `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` | `APK_TRANSFER.fa.md` §1 |
| قطعهٔ ۱ | `71176749` | `bc4f1f194495f59da1f40adc6e33cae83d5759a8ad8add01a385009e9fc854c5` | `LOGS/APK_TRANSFER.txt` |
| قطعهٔ ۲ | `71176750` | `d3756c70bba9c1c7e8e060415259e6b13e13bd449c76f50152a40b04ccf05c67` | `LOGS/APK_TRANSFER.txt` |
| الحاق روی runner | `142353499` | `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` | `APK_SHA256.txt` |
| بستهٔ نصبشده (از `pm path`) | همان فایل، بدون نصب مجدد از مبدأ دیگر | — | `APK_INSTALLATION.txt` |

`71176749 + 71176750 = 142353499` ⇒ هیچ بایتی حذف/اضافه نشد.
تطابق هش **کامل ۶۴ رقمی** (نه هش جزئی و نه فقط اندازه) برقرار است.

## ۲. خروجی دقیق `APK_SHA256.txt`

```
expected_sha256=48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
actual_sha256=48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
expected_bytes=142353499
actual_bytes=142353499
result=SHA_MATCH_OK
```

## ۳. دروازه و قواعد عدمجایگزینی — `OBSERVED`

- `transfer_apk.sh`: `sha256sum` و `stat -c %s` روی فایل الحاقشده؛
  عدم تطابق ⇒ شکست step و عدم بوت شبیهساز.
- `runtime_smoke.sh`: دروازهٔ دوم پیش از نصب؛
  `sha_match=false` ⇒ `SHA MISMATCH -> refusing install. No substitute APK used.`
  و تمام معیارها `false` باقی میماند.
- فایل نصبشده دقیقاً `$RUNNER_TEMP/MIMO_ORIGINAL.apk` است؛
  هیچ `stock-*.apk`، هیچ artifact قدیمی، هیچ بیلد `debug` و هیچ APK شبیهساز
  جایگزین نشد. هیچ `zip -FF`، `apktool`, وصلهٔ DEX/منیفست/کتابخانه/امضا انجام نشد.
- نتیجهٔ نصب `Success` و `versionName=9.35` / `versionCode=1792759685`
  خود تأیید ثانویه بر سالم بودن بسته است.

## ۴. نکتهٔ شفافیت دربارهٔ اجرای `41997975847`

در آن اجرا `APK_SHA256.txt` و `LOGS/APK_TRANSFER.txt` هر دو `SHA_MATCH_OK` داشتند،
اما `TEST_RESULTS.json` بهدلیل برخورد متغیر شل `B` (بازاستفاده در حلقهٔ رفع dialog ANR،
که متغیر `EXPECTED_BYTES` را خراب میکرد) اشتباهاً `sha_match=false` نوشت.
این باگ صرفاً در **گزارشدهی** بود، نه در انتقال: هش واقعی هرگز ناسازگار نبود.
در `92e87fe8` متغیر به `ANR_B` تغییر نام یافت و دروازهٔ SHA علاوه بر مقایسهٔ مستقیم،
`result=SHA_MATCH_OK` را از پروندهٔ معتبر نیز میپذیرد. اجرای `41998643355` نتیجه داد:
`"sha_match": true`، معیارهای ۱ و ۲ هر دو `true`. شاهد مقایسهای:
`LOGS/APK_TRANSFER_RUN_41997975847.txt`.

## ۵. محدوده — `NOT OBSERVED`

یکپارچگی **فایل** اثبات شد؛ این بهمعنای تأیید امضای رمزنگاری توسعهدهنده در برابر
مرجع رسمی، تأیید محتوای سرور، یا پاسخ بکاند نیست. `SERVER CONFIRMED` همچنان `0` است.

**ارجاع شواهد:** `APK_SHA256.txt`، `LOGS/APK_TRANSFER.txt`،
`LOGS/apk_download.txt`، `APK_INSTALLATION.txt`، `TEST_RESULTS.json`.
