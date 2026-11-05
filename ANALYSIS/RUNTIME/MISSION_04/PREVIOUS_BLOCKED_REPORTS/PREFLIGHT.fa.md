# MISSION 04 — PREFLIGHT

| شناسه | مقدار |
|---|---|
| Workflow run ID (M04) | **`41991896800`** (presence-only probe, SUCCESS) |
| Workflow run ID (پیکربندی شبیهساز، M03) | **`41951780483`** (SUCCESS) |
| Branch | `arena/aebb90b7-game` |
| Commit هنگام probe | `1ca5d6bc2c761c3555d189d5160e8f8316362fed` |
| Commit پایه قبل از M04 | `14e7fc6629d0952aed586f1603b17dd55f36a390` |
| Workflow | `.github/workflows/mimo-runtime-verification.yml` |
| پین اکشن | `reactivecircus/android-emulator-runner@b530d96654c385303d652368551fb075bc2f0b6b` (v2.35.0) |
| پیکربندی شبیهساز | API 36 / Android 16 / `google_apis` / `x86_64` / `pixel_7` / headless / `disable-animations: false` / boot timeout 900 |
| APK SHA-256 کامل | `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` |
| اندازهٔ APK | `142353499` بایت |
| Timestamp | `2026-11-05T08:02–08:06Z` |
| برچسب غالب | `OBSERVED` / `BLOCKED` |

## ۱. اسناد خواندهشده (الزام §1)

همه هفت پرونده خوانده و بررسی شدند؛ نتیجهٔ تطابق:

| پرونده | اندازه | نکتهٔ کلیدی |
|---|---|---|
| `../FINAL_REVIEW_M03.fa.md` | 8836 B | شش معیار؛ معیار ۱ محقق، ۲–۶ خیر |
| `../ENVIRONMENT_AUDIT.fa.md` | 10824 B | runner Ubuntu 26.04، KVM، ADB 37.0.1، API 36 |
| `../APK_INSTALLATION.fa.md` | 5664 B | دقیقاً همان انسداد منبع APK |
| `../APPLICATION_LAUNCH.fa.md` | 4052 B | `am start` اجرا نشد |
| `../RUNTIME_VERIFICATION.fa.md` | 7959 B | `RUNTIME VERIFIED` رفتار Mimo = ۰ |
| `../TEST_RESULTS.json` | 4119 B | ۰/۹ اجرا، ۹/۹ BLOCKED |
| `../DEVICE_PROPERTIES.json` | 1054 B | API 36، 1080×2400@420، `libndk_translation.so` |

دو پروندهٔ فنی نیز بررسی شدند: workflow (۴۸۲ خط پیش از ویرایش M04) و
`../runtime_smoke.sh`. **رفتار `script:` خطبهخط** (`parseScript()`، کشف M03) همچنان پابرجاست و
فراخوانی تکخطی `bash ANALYSIS/RUNTIME/runtime_smoke.sh` بدون تغییر حفظ شد.

## ۲. هش کامل، نه مخفف — `OBSERVED`

دستور «Do not trust the abbreviated hash» رعایت شد. هش ۶۴ رقمی کامل از دو منبع مستقل
استخراج و با هم تطبیق داده شد:

- `ANALYSIS/EVIDENCE_INDEX.json` → `EV-0001` →
  `sha256=48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`
- شمارش مجدد روی کپی مجاز workspace:
  `sha256sum '/home/user/_work/apk/Mimo_9.35 (1).apk'` → همان ۶۴ رقم،
  `stat -c %s` → `142353499`.

پیشوند `48ce1740` و پایان `7c7a` با مقدار اعلامشده در پرامپت مطابقت دارد.
همچنین ۹ هش ۶۴رقمی دیگر در اسناد M03 یافت شد که مربوط به سه_part Drive و سایر فایلها بودند؛
**هیچکدام بهعنوان هش APK پذیرفته نشدند**.

> تمایز حیاتی: این تطابق `OBSERVED` روی **کپی محلی workspace** است.
> تطابق هش **APK دریافتشده روی runner** (معیار ۳ مأموریت) انجام **نشد** ⇒ `BLOCKED`.
> ر.ک. `APK_INTEGRITY.fa.md`.

## ۳. «فرض نکن workflow قبلی هنوز درست است» — `OBSERVED`

برخلاف دستور، وضعیت فعلی workflow دوباره بررسی شد، نه فقط نتیجهٔ M03:

- پین SHA، `api-level: 36`، `target: google_apis`، `arch: x86_64`، `profile: pixel_7`،
  `disable-animations: false`، `emulator-boot-timeout: 900` و فراخوانی تکخطی `script:` همگی
  با YAML parser محلی (`js-yaml`) دوباره تأیید شدند.
- شاخهٔ فعال `arena/aebb90b7-game`، HEAD پیش از M04 پاک (clean) بود.
- **نقص امنیتی تازهای کشف شد**: `APK_URL` از `${{ inputs.apk_url }}` (یک ورودی عمومی
  `workflow_dispatch`) خوانده میشد، در حالی که §2 مأموریت صریحاً میگوید
  «A normal workflow_dispatch input is not a secret». این ورودی **حذف** و منبع به
  `${{ secrets.MIMO_APK_URL || '' }}` تغییر یافت؛ لاگ دانلود نیز URLها را redact میکند.
  جزئیات و دلیل در `APK_SOURCE_AND_AUTHORIZATION.fa.md`.

## ۴. تصمیم «عدم تکرار تنظیمات محیط» — `OBSERVED`

§1 و §13 مأموریت: «اگر APK مسدود شد، محیط را تکرار نکن». بنابراین:

- برای بررسی گزینهٔ ۲/۳ (Secrets) فقط یک **job ایزولهٔ probe** بدون شبیهساز اجرا شد
  (run `41991896800`)؛ job اصلی `runtime` با شرط روی پیام commit در آن run **skipped شد** (عدم اجرا، نه شکست).
- پیکربندی API 36 / پین اکشن / `pixel_7` / script تکخطی **دستنخورده** باقی ماند.
- هیچ `sdkmanager`، بوت AVD، `adb install` یا `am start`ـای در M04 اجرا نشد.

## ۵. عدم دستکاری شواهد قبلی — `OBSERVED`

مسیرهای محافظتشده بررسی شدند: `mimo-ui/UPGRADE`، `v12.5-fa`، ZIP/MANIFEST،
`verify_upgrade.py`، `ANALYSIS/EVIDENCE_INDEX.json`، REA/Ghidra، APK/DEX/منابع،
و پروندههای `ANALYSIS/RUNTIME/` متعلق به M03 (بهجز ویرایش هدفمند workflow و
`_DISPATCH_TRIGGER`). `git diff --stat 907d8b01 -- <protected>` خالی است.
`EVIDENCE_INDEX.json` **بهروز نشد**: هیچ شاهد تازهای دربارهٔ **رفتار برنامه** تولید نشد؛
یافتههای M04 منحصراً دربارهٔ انسداد منبعاند (توضیح در `MISSION_04_FINAL_REVIEW.fa.md` §E).

## ۶. فرمانهای دقیق preflight

```
git branch --show-current ; git rev-parse HEAD ; git status --short
python3  # read ANALYSIS/EVIDENCE_INDEX.json -> EV-0001 ; scan all 64-hex hashes
sha256sum '/home/user/_work/apk/Mimo_9.35 (1).apk'
stat -c %s '/home/user/_work/apk/Mimo_9.35 (1).apk'
sha256sum  # cross-check against prior mission reports
node -e "js-yaml.load(...mimo-runtime-verification.yml)"   # re-validate current workflow
bash -n ANALYSIS/RUNTIME/runtime_smoke.sh
```
خروجی کامل فرمانهای بررسی منبع در `LOGS/APK_SOURCE_INVESTIGATION.txt` ثبت شده است.
