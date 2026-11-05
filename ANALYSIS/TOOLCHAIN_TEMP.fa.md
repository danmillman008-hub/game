# نصب ابزارهای تحلیل — صورت وضعیت دقیق (بهروزشده بعد از تصحیح شما)

> **REVIEW / موقت ولی کاملاً نصبشده.**
> تصحیح شما پذیرفته شد: «بیرون خط لولهٔ اصلی بودن» **بههیچوجه** بهمعنی «نصب نکردن» نبود.
> هر دو ریپو **کامل** در یک پوشهٔ جداگانه در گیتهاب (`TOOLS/`) قرار دارند، Ghidra **کامل نصب و اجرا شد**،
> و فایل اورجینال Drive دانلود/بازسازی/دیکامپایل شد.
> همچنان هیچکدام وارد `mimo-ui/UPGRADE`، ZIP، MANIFEST، وریفایر، طرح v12 در Drive،
> یا `U/DESIGN/index.html` **نشدند**. `verify_upgrade.py` بعد از همهٔ کارها همچنان **PASS ۲۵۹/۲۵۹ / ۱٬۹۵۴ فایل** است.

---

## ۱. پوشهٔ جداگانه در گیتهاب — هر دو ریپو، کامل

| پوشه | ریپو / شاخه | کامیت قفلشده | فایلها | حجم درخت |
|---|---|---|---|---|
| `TOOLS/ghidra/` | `NationalSecurityAgency/ghidra` @ `master` | `4cfb27ded8c4d62ccf177e08fa7a3699cc672072` | ۲۰٬۶۵۵ | ~۳۵۹ MB |
| `TOOLS/rea/` | `morluto/rea` @ `main` | `71f680d7c1aa7a45ba0325fe87b104744b0c105f` | ۱۱٬۸۵۷ (بعد از `--recursive`) | ~۱۰۱ MB |

- بهصورت **git submodule** پینشدهاند؛ روی گیتهاب دو پوشه به ریپوهای کامل لینک میشوند.
- `./TOOLS/install.sh` **اجرا شد و موفق شد**: `git submodule update --init --recursive` پنج سابماژول تو در توی REA
  (`binwalk`, `ghidra-nativeaot`, `jadx-headless-mcp`, `unblob`, `wakaru`) را هم پر کرد،
  `rea-agents@6.7.0` + `jadx-mcp@1.4.1` + `apktool-jar@2.4.1` + `@mishguru/jadx-node@3.1.0` را از npm،
  و `jdk4py==25.0.2.1` + `androguard==4.1.4` را از PyPI نصب کرد.
  خروجی واقعی: `Ghidra source files 20655` · `REA source files 11857` ·
  `java 25.0.2` · `JADX MCP jar 43756715 bytes` · `apktool jar 17661172 bytes` · `REA CLI present`.
- همهٔ چیزهای تولیدشده زیر `TOOLS/_*/` هستند و توسط `.gitignore` از گیتهاب/ZIP/MANIFEST حذف میشوند.

---

## ۲. «پروکسی گیتهاب» — دقیقاً همان روشی که خواستید

سندباکس فقط به `github.com`, `api.github.com`, `codeload.github.com`, `registry.npmjs.org`,
`pypi.org`, `files.pythonhosted.org` دسترسی دارد. ریلیزها روی
`release-assets.githubusercontent.com` مسدوداند. سه دورزنندهٔ مجاز بهکار رفت:

### ۲٫۱ GitHub Actions بهعنوان محاسبه/پروکسی (Ghidra کامل)

`.github/workflows/mimo-re-toolchain.yml` → **run `41936300913`، تمام ۹ گام ✓، ۴۳ ثانیه**.
شواهد در `ANALYSIS/GHIDRA/`:

| مورد | مقدار واقعی |
|---|---|
| ریلیز رسمی | `ghidra_12.2_PUBLIC_20261016.zip` |
| SHA‑256 ریلیز | `2c2cd776db3c1f6a097ba418922378ac3649cadd5e844a6f5f088ae628a7be67` |
| نصب کامل | `ghidra_12.2_PUBLIC` · **۵٬۳۲۴ فایل** · **۸۸۵M** · `analyzeHeadless=EXECUTABLE` · `ghidraRun=EXECUTABLE` |
| JDK رانر | `Temurin-25.0.5+8-LTS` (همان `application.java.min=25` ریلیز) |
| `application.version` | `12.2` · build `2026‑Oct‑16` |
| اجرا | `analyzeHeadless ... -import classes.dex classes2.dex classes3.dex -noanalysis -postScript MimoGhidraReport.java -deleteProject` |
| خروجی Ghidra | ۳ برنامهٔ `Dalvik:LE:32:DEX_KitKat`، ۳ بلوک حافظه، **۳۶٬۷۰۷ + ۴۱٬۳۷۱ + ۱۲٬۱۷۰ = ۹۰٬۲۴۸ نماد**، لاگ کامل `Import succeeded` |
| JADX engine REA | `jadx-headless-mcp-0.7.1-all.jar` دانلود و هش شد: `6e5eacf500b64292bfb73c49797c1958f6ee44646e43e868039ae7feb573ff75` — **دقیقاً** همان هش مستند REA |

یعنی Ghidra دیگر «سورس صرفاً بهعنوان مرجع فرمت» نیست؛ **باینری رسمی، نصب کامل، و headless اجرا شده است**.

### ۲٫۲ npm registry بهعنوان حامل باینری (موتور دیکامپایل محلی)

| پکیج (از `registry.npmjs.org`) | باینری داخل tarball |
|---|---|
| `jadx-mcp@1.4.1` | `jadx-mcp.jar` · ۴۳٬۷۵۶٬۷۱۵ B · JADX مدرن (`jadx/api`, `jadx/core`) + سرور MCP با ۲۱ ابزار |
| `apktool-jar@2.4.1` | `apktool_2.4.1.jar` · ۱۷٬۶۶۱٬۱۷۲ B |
| `@mishguru/jadx-node@3.1.0` | JADX CLI 1.1.0 کامل |

موتور JADX MCP روی **همان APK اورجینال** بالا آمد:
`Loaded classes: 29476, methods: 129071, instructions: 7426450` →
`Engine ready. Total classes: 24022` → `Decompiler Stats: classes=24022, errors=0, warnings=0`
(خطای سطح کلاس صفر؛ خطاها در سطح متد — بند ۵).

### ۲٫۳ GitHub Actions بهعنوان پروکسی دیکامپایل (JADX 1.5.6)

`.github/workflows/mimo-jadx-proxy.yml` → **run `41937805854`، تمام گامها ✓**.
`jadx-1.5.6.zip` (SHA‑256 `545ea2be9c242511bc145755cf4bda2485ade42966e096f8b4d3da2a230e8974`)
روی رانر دانلود/نصب شد و `classes.dex` اورجینال (۱۶٬۲۳۷٬۹۲۰ B) را دیکامپایل کرد.
خروجی در `ANALYSIS/DECOMPILED/`:

- **۲٬۲۱۱ فایل Java** مربوط به `com.getmimo` · **۳۸۱٬۴۵۵ خط**
- بستهٔ فشرده `getmimo_sources.tar.gz` (۱٬۲۱۶٬۵۸۷ B، SHA‑256 `ec7af3a740b349b3ec74bb90141b52e64636bed72f911fd12c41360b1c63774c`)
- `REPORT.md`, `JADX_VERSION.txt`, `JADX_HELP.txt`, `JADX_ZIP.sha256`, `SOURCES.sha256`, `jadx.log`
- JADX 1.1.0 محلی هم ۱۱٬۸۴۴ فایل Java (۱۳۵ MB) تولید کرد — از همین خروجی **۵۳ تعریف Retrofit** استخراج شد
  (`ANALYSIS/MIMO_RETROFIT_ENDPOINTS.json`).

---

## ۳. فایل اورجینال Drive — دانلود، بازسازی، اثبات بایت به بایت

پوشهٔ `mimo` در Drive (`1yU1PN1GhTZlDeu91H4FSS0JsOT5MjpxB`) یک **آرشیو ۳ تکهای** است، نه یک APK ساده:

| قطعه | بایت | SHA‑256 (مطابق متاداتای Drive) |
|---|---|---|
| `Mimo_9.35 (1).z01` | ۵۲٬۴۲۸٬۸۰۰ | `1e3a41159ebe531121f0b04f146791fe900605c7ac15cc9cf54b1501d3b93b18` |
| `Mimo_9.35 (1).z02` | ۵۲٬۴۲۸٬۸۰۰ | `1ac22ab2c916f302d8ba0fd42317f1cb79ea53eb6045061d0a174993a634f539` |
| `Mimo_9.35 (1).zip` | ۳۱٬۰۶۹٬۳۶۸ | `91c670864fc66d852b371ed83c1f6d260ab4075c078030f74b29620807ffa2b7` |

- هر سه قطعه از طریق کانکتور Drive در دسترساند و سه SHA‑256 **یکبهیک با متاداتای Drive جور شد**.
- الحاق `.z01 + .z02 + .zip` = ۱۳۵٬۹۲۶٬۹۶۸ B؛ ZIP دقیقاً **یک عضو** دارد: `Mimo_9.35 (1).apk` به اندازهٔ ۱۴۲٬۳۵۳٬۴۹۹ B و `CRC32 = 0x94bc6bf2`.
- `CRC32` همان APK محلی = `0x94bc6bf2` ✔ و `SHA‑256` = `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a` ✔
  (همان هش ۱۴٬۳۹۸ entry در `APK_ENTRY_CENSUS.csv` و ریشهٔ Evidence REA).
- بنابراین «فایل اصلی» **همان فایلی است که تحلیل شد** — هیچ نسخهٔ متفاوت/گمشدهٔ دیگری وجود ندارد. «پیچ و مهرهها» =
  ۳ قطعهٔ آرشیو + APK + ۱۲ DEX + ۱۴٬۳۹۸ entry + ۱۰٬۳۵۲ فایل محتوای `assets/` + ARSC + Manifest.

---

## ۴. وضعیت REA (صادقانه)

| مورد | وضعیت |
|---|---|
| ریپو کامل + ۵ سابماژول تو در تو | ✅ نصب شد |
| `rea inspect-artifact` روی APK | ✅ Evidence `ev_cbbbefbf…f11b2` / ۱۴٬۰۶۳ گره / ۱۴٬۳۹۸ یال / ۰ تناقض |
| `REA_JADX_MCP_JAR` | ✅ مسیر `jadx-mcp.jar` تنظیم شد؛ همان JARی که Ghidra workflow دانلود کرد هم هششد |
| `rea doctor` | ⚠️ همچنان `environment_healthy=false`: بیلد `jdk4py` فقط ماژول `java.compiler` دارد و **`jdk.compiler`/`javac` را ندارد**؛ REA برای کامپایل «پل سورس جاوا» به یک JDK کامل نیاز دارد. `GHIDRA_INSTALL_DIR` محلی هم تنظیم نیست (باینری ریلیز ۸۸۵M روی رانر گیتهاب نصب است، در سندباکس قابل دانلود مستقیم نیست). |
| نتیجه | JADX و apktool **بدون javac** اجرا شدند و خروجی دادند؛ ولی provider رسمی JADX/Ghidraی REA در همین سندباکس سلامت کامل نمیگیرد. **ادعای «REA کاملاً سالم» نمیشود.** |

این یک محدودیت محیطی دقیق است، نه «نصب نکردن». اگر خواستید، میشود همان `rea doctor` / `inspect-android-package`
را هم روی رانر Actions (که JDK کامل + JAR + Ghidra دارد) اجرا کرد.

---

## ۵. محدودیت فنی تازهای که کشف شد (مهم و صادقانه)

هر سه دیکامپایلر روی **بدنهٔ برخی متدها** شکست خوردند، درحالیکه امضاها/آنوتیشنها/رشتهها کامل آمدند:

| موتور | خطا |
|---|---|
| JADX 1.1.0 (npm) | `bogus element_width: 0005/000b/000d/000f` در `InsnDecoder` (دیکدر قدیمی، DEX 039) |
| JADX مدرن داخل `jadx-mcp.jar` | `newPosition > limit` / `newPosition < 0` در `MethodNode.load` |
| JADX 1.5.6 (رانر گیتهاب) | `ERROR - finished with errors, count: 243002`؛ ۲٬۱۷۹ فایل از ۲٬۲۱۱ فایل `com.getmimo` دستکم یک `Method not decompiled` دارند (۱۱٬۶۲۸ استاب) |

هدر DEX کاملاً استاندارد است (ماژیک `dex\n039\0`، ۱۸ ورودی `map_list` همگی از انواع شناختهشده،
بدون `call_site_id_item`/`method_handle_item`/`hiddenapi`). پس مشکل «خرابی فایل» نیست؛
بلکه ترکیب R8 + کروتینهای Kotlin (`SuspendLambda`/`ContinuationImpl`) بدنهٔ بایتکد را برای JADX قابل decode نمیکند.
Ghidra در عوض هر سه DEX را **با ۹۰٬۲۴۸ نماد** import کرد (`-noanalysis`) — یعنی لودر DEX Ghidra تحملپذیرتر است.

**آنچه با این وجود کامل بهدست آمد**: ۲۴٬۰۲۲ کلاس / ۱۲۹٬۰۷۱ متد / ۷٬۴۲۶٬۴۵۰ دستورالعمل،
۱۰۵٬۶۱۱ رشته، ۳۲٬۶۸۴ تایپ، **۵۳ نقطهٔ پایانی Retrofit با امضا و آنوتیشن**،
تمام `@Metadata` کاتلین (اسامی سورسlevel فیلدها/متدها)، ۱۰٬۳۵۲ فایل محتوای shipped،
ARSC، Manifest، و ۹۰٬۲۴۸ نماد Ghidra.

**آنچه همچنان ناشناخته است** (همان §۹ سند اصلی، حالا با دلیل فنی مشخص):
فرمول عددی امتیاز، هندسهٔ دقیق `com.getmimo.ui.path.map.k` (بدنهٔ کامپوزابل)،
ترتیب فراخوانیهای رانتایم، و مقادیر سروری. هیچ ادعای اجرای زنده/امولاتور/اسکرینشات رانتایم نشده است.

---

## ۶. ایزولاسیون (دوباره تأیید شد)

- `git status` بعد از همهٔ کارها: فقط `ANALYSIS/`, `TOOLS/`, `.github/workflows/`, `.gitmodules`, `.gitignore` — **هیچ فایلی زیر `mimo-ui/UPGRADE/` تغییر نکرد**.
- `python3 mimo-ui/UPGRADE/tools/verify_upgrade.py mimo-ui/UPGRADE` → `{"verdict":"PASS","checks":259,"passed":259,"failed":[],"files_hashed":1954}`.
- پیشنمایش `http://localhost:8081/DESIGN/index.html` → `200` / ۴۳۷٬۹۷۲ B (بدون تغییر).
- هیچ VPN سرویسی پیکربندی نشد؛ «VPNمانند» = انتقال از طریق رانر گیتهاب و رجیستریهای مجاز.
- هیچ تأیید نهایی/Approval ادعا نشد؛ `SAVED` پروتوتایپ فقط در حافظه است و در localStorage ذخیره نمیشود.
