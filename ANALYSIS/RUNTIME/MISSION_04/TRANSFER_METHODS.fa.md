# MISSION 04 — ارزیابی و اجرای روشهای انتقال (TRANSFER METHODS)

| شناسه | مقدار |
|---|---|
| Workflow run ID مرجع | **`41998643355`** (SUCCESS، 3m31s) |
| اجراهای انتقال | `41994008902` (شکست)، `41996366953` (موفق)، `41997137033`، `41997975847`، `41998643355` |
| Branch / commit | `arena/aebb90b7-game` / `92e87fe8d061ea4c11089f40a7c8ce73d34d816a` |
| پیکربندی شبیهساز | API 36 / Android 16 / `pixel_7` / `google_apis` / `x86_64` / headless |
| APK SHA-256 | `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` |
| Timestamp | `2026-11-05T08:23–09:03Z` |
| نتیجه | **انتقال انجام شد؛ `SHA_MATCH_OK`** |

## ۱. چهار پرسش الزامی §2 برای هر روش

| # | روش | ۱۴۲ MB؟ | runner دسترسی دارد؟ | SHA قابل تأیید؟ | قابل اجرا با ابزارها؟ | نتیجه واقعی |
|---|---|---|---|---|---|---|
| ۱ | E/F — HTTP موقت احرازشده روی preview sandbox | بله (۹ قطعه ۱۶ MiB) | ❌ | بله | بله | **شکست**: `HTTP/2 403` |
| ۲ | A/B — قطعات خصوصی stageشده در Google Drive + لینک موقت | بله (۲×~۷۱ MB) | ✅ | بله | بله | **موفق** |
| ۳ | C — artifactهای موجود GitHub Actions | — | — | — | — | رد شد در بررسی اولیه: ۲۶۸ artifact، هیچکدام ۱۴۲٬۳۵۳٬۴۹۹ بایت نیستند؛ مربوط به workflowهای `verify`/`mivi` روی شاخهٔ دیگر |
| ۴ | D — سرویسهای انتقال موقت عمومی | — | — | — | ❌ | رد شد: sandbox فقط به `github.com`, `codeload.github.com`, `api.github.com`, `registry.npmjs.org`, `pypi.org`, `files.pythonhosted.org` خروجی دارد (همهٔ میزبانهای دیگر `HTTP 000`) |

برای روش ۱، پاسخ پرسش ۲ منفی بود ⇒ طبق §2 «اگر بله، تست کن» تست شد و شکست خورد.
برای روش ۲ هر چهار پاسخ مثبت بود ⇒ تست شد و **کار کرد**. روش سوم genuinely متفاوت لازم نشد؛
حداکثر سه روش مجاز §8 نقض نشد.

## ۲. روش ۱ (E/F) — شکست دقیق و دلیل کنارگذاشتن

یک سرور فقطخواندنی موقت در workspace روی `0.0.0.0:8000` بالا آمد
(`/t/<token>/health`, `/count`, `/part/N`, `/apk`؛ توکن ۳۲hex، بدون چاپ در لاگ).
runner در `41994008902` و `41996366953` سه variant را امتحان کرد
(`plain`, `--noproxy *`, `User-Agent` مرورگری). خروجی دقیق:

```
m1_health[plain]=HTTP/2 403
content-type: application/json; charset=utf-8
via: 1.1 google
{"sandboxId":"...","message":"Sandbox is secured with traffic access token.
 Token header 'e2b-traffic-access-token' is missing","code":403}
m1_health[noproxy]=HTTP/2 403
m1_health[browser]=HTTP/2 403   (HTML: "Missing traffic access token · E2B")
```

**علت قطعی**: پروکسی preview پلتفرم نیازمند هدر `e2b-traffic-access-token` است که در
محیط دردسترس ایجنت وجود نداشت. این یک خطای صریح احراز هویت زیرساخت است، نه حدس یا
ابهام. بنابراین روش ۱ **یکبار** تست و کنار گذاشته شد؛ تکرار همان پیکربندی بهحساب
روش جدید نیامد. سرور موقت پس از آن `stop_process` شد. شاهد:
`LOGS/APK_TRANSFER_RUN_41996366953.txt`.

## ۳. روش ۲ (A/B) — چرا عملیتر و چگونه اجرا شد

- فایل اصلیworkspace بدون هیچ تغییری به **دو قطعهٔ باینری** تقسیم شد
  (هرکدام زیر سقف ۱۰۰ MB ابزار آپلود):
  `part1 = 71,176,749 B` (SHA `bc4f1f194495f59da1f40adc6e33cae83d5759a8ad8add01a385009e9fc854c5`)،
  `part2 = 71,176,750 B` (SHA `d3756c70bba9c1c7e8e060415259e6b13e13bd449c76f50152a40b04ccf05c67`).
  `sha256(part1 || part2)` محلی = هش اصلی ⇒ بایتها حفظ شدند.
- دو فایل موقت **جدید** (نه فایلهای خصوصی ازپیشموجود) در پوشهٔ مجاز Drive آپلود شدند؛
  دسترسی `anyoneWithLink / reader / allow_file_discovery=false` (لینک فقط، غیرقابل جستجو)
  صرفاً برای مدت اجرا.
- runner از `https://drive.usercontent.google.com/download?id=...&export=download&confirm=t`
  هر قطعه را گرفت، اندازهٔ هرکدام را جداگانه چک کرد، `cat` کرد و `sha256sum` گرفت.
- هیچ URL امضاشده، توکن یا credentialـای در لاگ/شاهد/commit چاپ نشد
  (`curl -sS` + `sed` redaction). پروندهٔ `TRANSFER_ENDPOINT.txt` بلافاصله پس از
  دانلود توسط همان step حذف شد (در commit شواهد، `delete mode` ثبت شده است).
- **پس از اتمام مأموریت**: دسترسی عمومی هر دو فایل با `make_private` لغو و هر دو با
  `trash_file` به سطل انتقال یافتند؛ کپیهای محلی `/home/user/_work/split/` و
  `google_drive/M04_transfer_part1.bin` نیز حذف شدند. **هیچ APKـای در مخزن commit نشد.**

تکرارپذیری: برای اجرای مجدد workflow باید قطعات دوباره staged شوند (فایلها عمداً پاک شدند).
دستور و ترتیب دقیق در `APK_TRANSFER.fa.md` و `transfer_apk.sh` ثبت شده است.

## ۴. روشهایی که عمداً بهکار نرفتند

- **commit کردن APK یا تکههایش در git**: نقض معیار «بدون commit کردن APK»؛ علاوه بر آن
  GitHub بلابهای بالای ۱۰۰ MB را رد میکند.
- **Release عمومی / Gist / Git blob**: میزبان `uploads.github.com` و
  `objects.githubusercontent.com` از sandbox قابلدسترس نیستند (`HTTP 000`) و قرار دادن
  APK در مخزن عمومی دائمی و غیرقابلحذف از تاریخچه است.
- **عمومی کردن سه_part اصلی Drive**: لزومی نداشت و فایلهای ازپیشموجود خصوصی
  دستنخورده باقی ماندند.
- **ساخت استک جدید / تصویر arm64 / docker-android**: نیاز نشد؛ همان runner تأییدشده M03
  کافی بود.

## ۵. تغییرات workflow (حداقلی، طبق §5)

| تغییر | دلیل |
|---|---|
| step جدید `Transfer and cryptographically verify the ORIGINAL APK` پیش از بوت | انتقال + دروازهٔ SHA قبل از هر `adb install` |
| `run: bash ANALYSIS/RUNTIME/MISSION_04/transfer_apk.sh` | پیادهسازی در فایل مستقل؛ فراخوانی تکخطی |
| `runtime_smoke.sh`: تشخیص APK preverified، skip دانلود، هدایت شواهد به `MISSION_04/` | جلوگیری از دانلود دوباره و از overwrite شدن شواهد M03 |
| افزودن رفع dialog ANR سیستم، `keyevent 224` بجای `26`، حذف `keyevent 3` پس از launch | تصویر واقعی Mimo بجای لانچر |
| سقف اسکرینشات ۱٫۵ MB ← ۴ MB | حفظ فریم واقعی برنامه |

**بدون تغییر**: SHA پین `b530d966…`، `api-level: 36`، `target: google_apis`،
`arch: x86_64`، `profile: pixel_7`، `disable-animations: false`،
`emulator-boot-timeout: 900`، `emulator-options`، و فراخوانی تکخطی
`script: bash ANALYSIS/RUNTIME/runtime_smoke.sh`.

**ارجاع شواهد:** `LOGS/APK_TRANSFER.txt`،
`LOGS/APK_TRANSFER_RUN_41996366953.txt`، `LOGS/APK_TRANSFER_RUN_41997137033.txt`،
`LOGS/APK_TRANSFER_RUN_41997975847.txt`، `transfer_apk.sh`.
