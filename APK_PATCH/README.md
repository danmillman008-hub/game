# `APK_PATCH/` — Mimo 9.35 offline-unlock patch

**هدف:** همان APK اصلی Mimo 9.35 (`com.getmimo`, `versionCode=1792759685`,
SHA-256 `48ce1740…`) با یک «ویرایش جزیی» در کد خود اپ، طوری که همهٔ درسها و
همهٔ بخشهای هر درس بدون اینترنت و بدون ترتیب قبلی باز شوند. خروجی وب
`app/dist/Mimo.html` و پروژههای Next.js داخل ریپو هدف این کار نبودهاند.

## چه چیزی عوض شد

فقط `classes.dex` (۱۶٬۲۳۷٬۹۲۰ بایت) و فقط ۱۶۹ بایت از آن:

| محل (byte offset در DEX) | کلاس / متد | تغییر |
|---|---|---|
| `0x9954c4` (148 B) | `com.getmimo.data.source.remote.keys.a.c()` | همیشه `Boolean.TRUE` برمیگرداند؛ درِ `CanOpenChapterWithKeys` و وابستگی به `/v1/user/keys` حذف میشود |
| `0x9a9582` (4 B) | `GetPathMapState$invoke$3.invokeSuspend` @`0x4aa` | `if-nez v14,+23h` → `goto +23h`: دیگر `vn/e0` (Locked) ساخته نمیشود |
| `0x9a95f2` (4 B) | همان متد @`0x51a` | `if-nez v14,+20h` → `goto +20h`: دیگر `vn/h0` (UnlockedButNoKeys) ساخته نمیشود؛ همیشه `vn/g0` (Unlocked) |
| `0x8482b0` (4 B) | `cc/b.y()` @`0xcc` | `if-eqz v7,+3h` → دو `nop`: دیگر `vn/y` (Locked section) ساخته نمیشود؛ بخشها `vn/a0` (Unlocked) میشوند |

علاوه بر این، `SHA-1` و `Adler-32` هدر DEX اصلاح شد (بقیهٔ بایتها، طول فایل،
و تعداد ۶۵٬۵۳۶ متد بدون تغییر).

برای پیدا کردن این چهار نقطه **فقط** از شواهد مهندسی معکوس داخل ریپو استفاده
شد:

- `ANALYSIS/MISSION_06/EVIDENCE/DISASM/DefaultKeysRepository.smali.txt`
- `ANALYSIS/MISSION_06/EVIDENCE/DISASM/CanOpenChapterWithKeys.smali.txt`
- `ANALYSIS/MISSION_06/EVIDENCE/DISASM/GetPathMapState_Invoke.smali.txt`
- `ANALYSIS/MISSION_06/10_LEARNING_PROGRESSION.md`
- `ANALYSIS/MISSION_09/COMPLETE_PROGRESSION_ENGINE_SPEC.md`
- `ANALYSIS/MISSION_09/COMPLETE_CLIENT_ARCHITECTURE.md`

`GetPathMapState$invoke$3` همان ماشین حالتی است که `Completed / Locked /
UnlockedButNoKeys / Unlocked` میسازد؛ `cc/b.y` همان طبقهبند وضعیت بخشهاست.
`DefaultKeysRepository.c()` همان گیت «پرو / کلید / dev override» است که
`CanOpenChapterWithKeys` قبل از باز کردن فصل صدا میزند. هیچ حدس خارج از این
اسناد وارد پچ نشده است.

## بستهبندی و امضا

تمام ۱۴٬۳۹۵ ورودی دیگر (بهجز ۳ فایل امضای قدیمی `META-INF/*`) بایتبهبایت
کپی شدند؛ فایلهای ذخیرهنشده ۴-بایته و بلوک امضا ۸-بایته aligned هستند.
APK با **Scheme v2 + v3** و یک کلید RSA-2048 تازه امضا شد. چون
`minSdkVersion=28` (Android 9+) است، امضای v1 لازم نیست.

> امضا تازه یعنی **باید نسخهٔ اصلی Mimo را قبل از نصب حذف کنید**؛ وگرنه
> اندروید بهخاطر اختلاف امضا نصب را رد میکند.

## اجرای دوباره

```bash
python3 APK_PATCH/build_patched_apk.py \
  --original /path/to/Mimo_9.35.apk \
  --out      /path/to/Mimo_9.35_unlocked_offline.apk
```

نیازمندیها: Python 3.8+ و `openssl` (هیچ پکیج پایتونی، جاوا، apktool یا
Android SDK لازم نیست). اسکریپت کلید/گواهی امضا را در پوشهٔ کاری مینویسد و
خروجی را همانجا میسازد.

## فایلهای تحویلی

در `dist/` (این پوشه در `.gitignore` است تا باینریهای ~۲۶۰ MB وارد Git نشوند):

- `Mimo_9.35_unlocked_offline.apk` — **APK اصلی پچشده و قابل نصب**
- `Mimo_9.35_unlocked_offline.zip` — همان APK داخل یک زیپ
- `split/*.z01`, `*.z02`, `*.z03`, `*.zip` — همان زیپ در ۴ قسمت
- `SHA256SUMS.txt`, `README.txt`

## صداقت دربارهٔ محدودیتها

- پچ فقط قفلهای **سمت کلاینت** را برمیدارد. محتوای درسها از قبل داخل APK
  است (`ANALYSIS/MISSION_09`: offline learning continues from shipped assets).
  قابلیتهای واقعاً سروری (لیدربورد، استریک، همگامسازی، کلیدها، تمرین ابری)
  همچنان `SERVER_DEPENDENT` هستند؛ دربارهٔ آنها ادعایی نمیشود
  (`SERVER CONFIRMED = 0`).
- امکان اجرای APK روی دستگاه/امولاتور اندروید در این محیط نبود؛ تست زندهٔ UI
  انجام **نشده است**. بررسیهای انجامشده در `APK_PATCH/VERIFICATION.md`.
