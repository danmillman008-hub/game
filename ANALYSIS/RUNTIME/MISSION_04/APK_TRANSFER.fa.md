# MISSION 04 — انتقال APK اصلی (APK TRANSFER)

| شناسه | مقدار |
|---|---|
| Workflow run ID مرجع | **`41998643355`** |
| Job / conclusion | `runtime` / SUCCESS (3m31s) |
| Branch / commit | `arena/aebb90b7-game` / `92e87fe8d061ea4c11089f40a7c8ce73d34d816a` |
| Timestamp UTC | `2026-11-05T09:01–09:03Z` |
| پیکربندی شبیهساز | API 36 / Android 16 / `pixel_7` / `google_apis` / `x86_64` / headless |
| فایل مبدأ | `/home/user/_work/apk/Mimo_9.35 (1).apk` (بدون تغییر) |
| مقصد runner | `$RUNNER_TEMP/MIMO_ORIGINAL.apk` |
| SHA-256 مورد انتظار | `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` |
| نتیجه | **`TRANSFER_RESULT=SHA_MATCH_OK`** |

## ۱. بررسی مستقل مبدأ — `OBSERVED`

```
$ ls -l '/home/user/_work/apk/Mimo_9.35 (1).apk'
-rw-r--r-- 1 user user 142353499 ... '/home/user/_work/apk/Mimo_9.35 (1).apk'
$ sha256sum '/home/user/_work/apk/Mimo_9.35 (1).apk'
48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
```
مسیر از قبل گزارش شده بود، ولی بهعنوان واقعیت پذیرفته نشد و دوباره وجود/اندازه/هش
آن بهطور مستقل محاسبه شد. فایل اصلی **خوانده شد و هیچگونه تغییر، فشردهسازی،
بستهبندی مجدد یا وصله** روی آن انجام نشد.

## ۲. آمادهسازی قطعات — `OBSERVED`

تقسیم باینری (نه ZIP، نه base64) برای عبور از سقف ۱۰۰ MB ابزار آپلود:

```
part1 = 71176749 B   sha256=bc4f1f194495f59da1f40adc6e33cae83d5759a8ad8add01a385009e9fc854c5
part2 = 71176750 B   sha256=d3756c70bba9c1c7e8e060415259e6b13e13bd449c76f50152a40b04ccf05c67
sha256(part1 || part2) = 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
```
دو فایل موقت در Google Drive آپلود شدند (دسترسی link-only موقت؛ جزئیات مجوز و
پاکسازی در `TRANSFER_METHODS.fa.md` §3).

## ۳. فرمانها و خروجی دقیق روی runner

اسکریپت: `ANALYSIS/RUNTIME/MISSION_04/transfer_apk.sh`، فراخوانی تکخطی
`bash ANALYSIS/RUNTIME/MISSION_04/transfer_apk.sh`.

```
curl -fsSL --max-time 900 --retry 2 \
     -o "$OUT.p1" "https://drive.usercontent.google.com/download?id=<part1>&export=download&confirm=t"
curl -fsSL --max-time 900 --retry 2 \
     -o "$OUT.p2" "https://drive.usercontent.google.com/download?id=<part2>&export=download&confirm=t"
cat "$OUT.p1" "$OUT.p2" > "$OUT"
stat -c %s "$OUT" ; sha256sum "$OUT"
```

خروجی ثبتشده در `LOGS/APK_TRANSFER.txt`:

```
== METHOD 1: temporary authenticated HTTP endpoint ==
m1=SKIPPED (disproved in run 41996366953: e2b-traffic-access-token required)

== METHOD 2: Google Drive staged chunks (link-only, temporary) ==
m2_part1_host=drive.usercontent.google.com exit=0 bytes=71176749 want=71176749
m2_part2_host=drive.usercontent.google.com exit=0 bytes=71176750 want=71176750
m2_concat_bytes=142353499
m2_part1_sha=bc4f1f194495f59da1f40adc6e33cae83d5759a8ad8add01a385009e9fc854c5
m2_part2_sha=d3756c70bba9c1c7e8e060415259e6b13e13bd449c76f50152a40b04ccf05c67
downloaded_bytes=142353499
downloaded_sha256=48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
TRANSFER_RESULT=SHA_MATCH_OK
```

هیچ URL، توکن یا credential در پروندهٔ بالا درج نشده است
(عنوان «URL values are intentionally never logged» + redaction خودکار).
پروندهٔ `TRANSFER_ENDPOINT.txt` توسط همان step حذف شد و در commit شواهد بهصورت
`delete mode 100644` دیده میشود.

## ۴. دروازهٔ SHA (§4) — `OBSERVED`

`APK_SHA256.txt` تولیدشده روی runner:

```
expected_sha256=48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
actual_sha256=48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
expected_bytes=142353499
actual_bytes=142353499
result=SHA_MATCH_OK
```
تطابق همزمان **هش کامل ۶۴رقمی** و **اندازهٔ دقیق** برقرار شد ⇒ نصب مجاز شد.
`runtime_smoke.sh` نیز پیش از `adb install` دوباره `sha256sum` گرفت و
`preverified_by_transfer_step=yes; runner-side curl skipped` ثبت کرد
(`LOGS/apk_download.txt`). در صورت عدم تطابق، اسکریپت با
`SHA MISMATCH -> refusing install. No substitute APK used.` متوقف میشد.

## ۵. تکرارپذیری بر روی پنج اجرا

| Run ID | نتیجه انتقال | نکته |
|---|---|---|
| `41994008902` | FAIL | روش ۱ → `403 e2b-traffic-access-token missing` |
| `41996366953` | **SHA_MATCH_OK** | روش ۲ نخستینبار موفق؛ نصب و اجرا انجام شد ولی `HOME` پس از launch برنامه را بکگراند کرد |
| `41997137033` | **SHA_MATCH_OK** | `IntroSlidesActivity` resumed؛ dialog ANR لانچر روی تصویر افتاد |
| `41997975847` | **SHA_MATCH_OK** | UI واقعی Mimo ثبت شد؛ باگ برخورد متغیر `B` در JSON |
| `41998643355` | **SHA_MATCH_OK** | اجرای مرجع نهایی؛ ۷/۷ معیار `true` |

هر پنج اجرا دقیقاً همان ۱۴۲٬۳۵۳٬۴۹۹ بایت و همان هش را منتقل کردند؛
هیچ APK جایگزین، هیچ `stock-*` و هیچ بیلد بازسازیشدهای استفاده نشد.

**ارجاع شواهد:** `LOGS/APK_TRANSFER.txt`، `APK_SHA256.txt`،
`LOGS/apk_download.txt`، `transfer_apk.sh`، `.github/workflows/mimo-runtime-verification.yml`.
