# MISSION 04 — منبع APK و مجوز دسترسی (APK SOURCE AND AUTHORIZATION)

| شناسه | مقدار |
|---|---|
| Workflow run ID | **`41991896800`** (presence-only probe) |
| Branch / commit | `arena/aebb90b7-game` / `1ca5d6bc2c761c3555d189d5160e8f8316362fed` |
| پیکربندی شبیهساز | API 36 / Android 16 / `pixel_7` / `google_apis` / `x86_64` (مرجع run `41951780483`) |
| APK SHA-256 | `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` |
| Timestamp | `2026-11-05T08:02–08:06Z` |
| نتیجه | **`BLOCKED`** — هیچ منبع مجاز قابلدسترس برای runner یافت نشد |

## ۱. ممنوعیتهای رعایتشده — `OBSERVED`

| ممنوعیت §2 | وضعیت |
|---|---|
| Commit کردن APK | انجام نشد؛ `git ls-files` فاقد APK اصلی است |
| آپلود به release عمومی | انجام نشد؛ تنها release موجود `apk-latest` همان ۸ فایل `stock-*` قدیمی است |
| عمومی کردن فایلهای خصوصی Drive | انجام نشد؛ مجوزها دستنخورده (owner-only) |
| نمایش URL خصوصی Drive در لاگ workflow | انجام نشد؛ هیچ URL خصوصی تولید/ثبت نشد |
| چاپ token / credential | انجام نشد؛ `gh auth status` با `<REDACTED>` و فقط نام متغیرها چاپ شد |
| دورزدن محدودیتهای دسترسی | انجام نشد |
| APK غیرمرتبط بهعنوان جایگزین | انجام نشد؛ workflow بدون تطابق SHA نصب را رد میکند |
| ساختن APK از روی DEX | انجام نشد |
| درخواست مجوز برای عمومی کردن فایلها | انجام نشد (REVIEW، نه درخواست تأیید) |

## ۲. بررسی گزینهها به ترتیب ارجحیت §2

### گزینهٔ ۱ — «Existing authorized private download endpoint» ⇒ `BLOCKED`

- جستوجو در تمام شاخهها و تاریخچه: `git grep -iInE 'drive\.usercontent|drive\.google\.com/(uc|file)|signed.?url|sas.?token|presigned|apk[_-]?url'` —
  تنها ارجاعات یافتشده مربوط به **ورودی قدیمی `apk_url` خود workflow** و اسناد M03 بود؛
  هیچ endpoint خصوصیِ ازپیشموجودی یافت نشد.
- `gh release list --limit 100` → فقط `apk-latest` (پیشتر بررسی شده، فایلهای `stock-*`).
- **هیچ URLـای اختراع نشد.**

### گزینهٔ ۲ — «Actions Secrets containing an authorized URL» ⇒ `BLOCKED`

دو مانع مستقل:

1. **enumeration ناممکن**: `gh secret list`،
   `gh api repos/danmillman008-hub/game/actions/secrets` و `/actions/variables`
   همگی → `HTTP 403: Resource not accessible by integration`.
   `GH_TOKEN` و `GITHUB_TOKEN` یک توکناند؛ هیچ PAT جداگانهای در
   `~/.config/gh/hosts.yml` / `~/.git-credentials` / `.git/config` وجود ندارد.
2. **نوشتن secret ناممکن**: `gh secret set M04_WRITE_PROBE --body 'probe-only-no-credential'`
   → `failed to fetch public key: HTTP 403 ... /actions/secrets/public-key`.
   بنابراین حتی نمیتوان URL خصوصی کوتاهمدت را در secret ذخیره کرد.

برای رفع ابهام «شاید secretـای با نام دیگر وجود دارد»، یک **probe فقط حضور/عدمحضور**
بدون چاپ هیچ مقداری روی runner اجرا شد (`LOGS/SECRET_PRESENCE_PROBE.txt`):

```
run_id=41991896800   trigger=push   candidate_names=37
PRESENT=0    ABSENT=37
```
نامهای بررسیشده: ۲۲ نام URLمانند (`MIMO_APK_URL`, `APK_URL`, `MIMO_APK`,
`ORIGINAL_APK_URL`, `APK_DOWNLOAD_URL`, `MIMO_APK_DOWNLOAD_URL`, `MIMO_935_APK_URL`,
`MIMO935_APK_URL`, `ANDROID_APK_URL`, `PRIVATE_APK_URL`, `APK_SOURCE_URL`,
`MIMO_APK_SIGNED_URL`, `MIMO_DOWNLOAD_URL`, `MIMO_PRIVATE_URL`, `APK_PRIVATE_URL`,
`DRIVE_APK_URL`, `GDRIVE_APK_URL`, `GOOGLE_DRIVE_APK_URL`, `MIMO_DRIVE_URL`,
`APK_ARTIFACT_URL`, `MIMO_ARTIFACT_URL`, `PRIVATE_ARTIFACT_URL`)؛
۱۳ نام credentialمانند (`GDRIVE_TOKEN`, `GOOGLE_DRIVE_TOKEN`, `DRIVE_ACCESS_TOKEN`,
`DRIVE_CREDENTIALS`, `GOOGLE_SERVICE_ACCOUNT`, `GCP_SA_KEY`, `GCS_CREDENTIALS`,
`AWS_ACCESS_KEY_ID`, `AZURE_STORAGE_CONNECTION_STRING`, `BLOB_SAS_URL`,
`MIMO_ARTIFACT_TOKEN`, `PRIVATE_ARTIFACT_TOKEN`, `APK_DOWNLOAD_TOKEN`)؛
و ۲ متغیر `vars.*`.

> **محدودیت صادقانه:** GitHub هیچ API یا contextـای برای **فهرست کردن نام secretها**
> در اختیار workflow نمیگذارد. بنابراین `UNKNOWN` باقی میماند که secretـای با نام
> غیر از این ۳۷ نام وجود داشتهباشد؛ «نبود مطلق» اثبات نشده است.

### گزینهٔ ۳ — «Actions Secrets containing authorized credentials» ⇒ `BLOCKED`

همان ۱۳ نام credential در probe بالا `ABSENT` بودند؛ علاوه بر آن نوشتن/خواندن
فهرست secrets با 403 مسدود است. بدون credential هیچ ارتباط مجازی با storage خصوصی
برقرار نمیشود.

### گزینهٔ ۴ — «Another explicitly authorized private artifact source» ⇒ `BLOCKED`

- **GitHub Actions artifacts** (منبع خصوصی و وابسته به مخزن) بهطور کامل بررسی شد:
  `gh api repos/.../actions/artifacts?per_page=100&page=1..3` → `total_count=268`،
  ۱۲ نام متمایز: `app-debug-apk` (بیشینه ۱۳۸٬۶۸۵٬۸۲۱ B)، `lean`، `patched`، `release`،
  `baseline`، `gms-free`، `mivi-clips`، `verify-report`، `app-smoke`، `tests`،
  `english-vo`، `voice-probe`.
  - **هیچ artifactـای دقیقاً ۱۴۲٬۳۵۳٬۴۹۹ بایت** (اندازهٔ APK اصلی) وجود ندارد.
  - نمونهگیری از `run_id`ها: `41239394025 → verify` و
    `41238745682 / 41231078525 → mivi`، همگی روی شاخهٔ دیگر `arena/e3952d18-game`.
    یعنی بیلدهای پروژهٔ دیگریاند، نه Mimo 9.35.
  - `gh release` همان ۸ فایل `stock-*` با SHAهای متفاوت است.
- **Google Drive** (کانکتور مجاز این گفتگو):
  - `search_files q="mimeType='application/vnd.android.package-archive'"` → ۶ فایل،
    هیچکدام Mimo 9.35 نیستند (`Hadaf Plus_2.0.2.apk`، `همدرس_7.4.4.apk`،
    `Mivi AI_2.37.407.apk`، سه فایل Kik MOD).
  - `search_files q="name contains 'Mimo' ..."` → ۲۱ فایل؛ APK کامل **وجود ندارد**،
    فقط سه_part آرشیو: `Mimo_9.35 (1).z01` (۵۲٬۴۲۸٬۸۰۰ B)،
    `.z02` (۵۲٬۴۲۸٬۸۰۰ B)، `.zip` (۳۱٬۰۶۹٬۳۶۸ B) = ۱۳۵٬۹۲۶٬۹۶۸ B.
  - `list_drives` → **۰ shared drive**.
  - `list_permissions` روی `1PrS5Xc71PNOVRNJl9U_iIuirCZnT73-d` (بخش `.zip`)
    → تنها ۱ مجوز: `type=user, role=owner`؛ بدون لینک عمومی. (M03 روی `.z01` همان نتیجه را داده بود.)
- **copies بومی**: کپی تأییدشده در `/home/user/_work/apk/` موجود است،
  ولی sandbox اجازهٔ خروجی به runner را ندارد و انتقال آن از طریق URL عمومی،
  ورودی عمومی workflow، commit یا لاگ دقیقاً همان چیزی است که §2 منع کرده است.

## ۳. تغییر امنیتی workflow (الزام §3: «If a workflow change is needed, explain why»)

| تغییر | دلیل |
|---|---|
| حذف ورودی `apk_url` از `workflow_dispatch` | §2: «A normal workflow_dispatch input is not a secret». ورودیهای dispatch در مخزن عمومی قابلرؤیتاند |
| `APK_URL: ${{ secrets.MIMO_APK_URL \|\| '' }}` بهجای `${{ inputs.apk_url \|\| '' }}` | منبع URL خصوصی فقط secret مجاز است |
| `curl -fL` → `curl -fsSL` و `sed -i -E 's#https?://[^[:space:]]+#<redacted-private-url>#g'` در `runtime_smoke.sh` | جلوگیری از درج URL خصوصی در لاگ/شواهد commitشده |
| افزودن job ایزولهٔ `source_probe` + شرط `if` روی job `runtime` | بررسی گزینههای ۲/۳ **بدون تکرار تنظیمات محیط M03** |

**بدون تغییر باقی ماند**: SHA پین اکشن، `api-level: 36`، `target: google_apis`،
`arch: x86_64`، `profile: pixel_7`، `disable-animations: false`،
`emulator-boot-timeout: 900`، `emulator-options`، و فراخوانی تکخطی
`script: bash ANALYSIS/RUNTIME/runtime_smoke.sh`.

## ۴. حکم

هیچ منبع مجاز شمارهٔ ۱ تا ۴ برای runner وجود ندارد؛ Secrets قابل enumeration و قابل ایجاد
نیستند؛ فایلهای Drive خصوصیاند و عمومی کردنشان ممنوع است؛ artifactها نامرتبطاند؛
و URLـای اختراع نشد. بنابراین طبق §13: **APK retrieval متوقف شد و مأموریت `BLOCKED` است**،
بدون هیچ تلاشی برای شبیهسازی نتیجه.

**ارجاع شواهد:** `LOGS/SECRET_PRESENCE_PROBE.txt`،
`LOGS/APK_SOURCE_INVESTIGATION.txt`، `.github/workflows/mimo-runtime-verification.yml`،
`../FINAL_REVIEW_M03.fa.md`، `../APK_INSTALLATION.fa.md`.
