# پوشهٔ جداگانهٔ ابزارهای تحلیل (موقت)

> **این پوشه کاملاً جدای خط لولهٔ اصلی `mimo-ui/UPGRADE` است.**
> هیچ فایلی از `TOOLS/` وارد ZIP نهایی، MANIFEST، `verify_upgrade.py`،
> پوشهٔ طرح v12 در Drive، یا `U/DESIGN/index.html` نمی‌شود.
> هدف فقط «درک دقیق Mimo 9.35» است، نه ساختن ساختار/محصول تازه.

## چه چیزی اینجا نصب است؟

دو ریپوی کامل، بهصورت **submodule** قفلشده روی کامیت مشخص، داخل یک پوشهٔ جداگانه در همان ریپوی گیتهاب:

| پوشه | ریپو | کامیت قفلشده | محتوا |
|---|---|---|---|
| `TOOLS/ghidra/` | `NationalSecurityAgency/ghidra` (`master`) | `4cfb27ded8c4d62ccf177e08fa7a3699cc672072` | سورس کامل Ghidra، ۲۰٬۶۵۵ فایل، ~۳۵۹ MB |
| `TOOLS/rea/` | `morluto/rea` (`main`) | `71f680d7c1aa7a45ba0325fe87b104744b0c105f` | سورس کامل REA، ۷٬۱۵۲ فایل، ~۱۰۱ MB |

روی گیتهاب، این دو پوشه بهصورت لینک به همان ریپوهای کامل دیده میشوند؛
با یک دستور `./TOOLS/install.sh` هر دو بهصورت کامل روی هر ماشینی پر میشوند.

## چرا «پروکسی گیتهاب»؟

سندباکس فقط به `github.com`، `api.github.com`، `codeload.github.com`،
`registry.npmjs.org`، `pypi.org` و `files.pythonhosted.org` دسترسی دارد؛
`release-assets.githubusercontent.com` (جایی که فایل ریلیز Ghidra و JADX هست)،
`objects.githubusercontent.com`، `services.gradle.org`، `repo1.maven.org`،
`drive.google.com` و باقی هاستها بستهاند.

دور زدن این محدودیت، دقیقاً همان کاری است که خواستید، با **سه مسیر مجاز**:

1. **GitHub Actions بهعنوان محاسبه/پروکسی:**
   `.github/workflows/mimo-re-toolchain.yml` روی رانر گیتهاب اجرا میشود،
   ریلیز رسمی `ghidra_12.2_PUBLIC_20261016.zip` (۵۶۹ MB) و
   `jadx-headless-mcp-0.7.1-all.jar` را دانلود میکند، Ghidra را **کامل نصب** میکند،
   `analyzeHeadless` را روی DEX اصلی Mimo اجرا میکند و فقط خروجی متنی
   (گزارش، sha256، لاگ) را با `git push` به همین برنچ برمیگرداند.
   خروجی در `ANALYSIS/GHIDRA/`.
2. **npm registry بهعنوان حامل باینری:** چند پکیج npm، JARهای واقعی را داخل
   tarball خود دارند و از `registry.npmjs.org` (مجاز) میآیند:
   - `jadx-mcp@1.4.1` → `jadx-mcp.jar` (۴۳٬۷۵۶٬۷۱۵ B) شامل JADX مدرن
     (`jadx/api`, `jadx/core`) + سرور MCP با ۲۱ ابزار؛
   - `apktool-jar@2.4.1` → `apktool_2.4.1.jar`؛
   - `@mishguru/jadx-node@3.1.0` → JADX CLI 1.1.0 کامل.
   به این ترتیب موتور دیکامپایل بدون هیچ دانلود مستقیمی نصب و اجرا شد.
3. **PyPI بهعنوان حامل JDK:** `jdk4py==25.0.2.1` و `androguard==4.1.4`.
   (نکتهٔ صادقانه: بیلد `jdk4py` فقط `java.compiler` دارد، ماژول
   `jdk.compiler`/`javac` را ندارد؛ بنابراین REA که پل جاوای خود را کامپایل
   میکند، روی همین JRE سلامت کامل نمیگیرد. JADX و apktool به javac نیاز ندارند.)

## نصب کامل (یک دستور)

```bash
cd /home/user/game
./TOOLS/install.sh
```

این اسکریپت: سابماژولها را کامل میکند، `rea-agents@6.7.0` و ابزارهای JADX/apktool
را از npm، و JDK/androguard را از PyPI نصب میکند، سپس وضعیت را چاپ میکند.
همهٔ چیزهای تولیدشده داخل `TOOLS/_*` هستند و توسط `.gitignore` رد میشوند
(یعنی وارد گیتهاب/ZIP/MANIFEST نمیشوند).

برای نصب **باینری ریلیز Ghidra** روی ماشینی که اینترنت آزاد دارد:

```bash
GHIDRA_ZIP_URL='https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_12.2_build/ghidra_12.2_PUBLIC_20261016.zip' \
  ./TOOLS/install.sh --with-ghidra-release
```

در سندباکس فعلی این URL بسته است؛ همان کار را ورکفلو `mimo-re-toolchain`
روی رانر گیتهاب انجام میدهد (مسیر ۱).

## چهچیزی عمداً اینجا نیست

- هیچ ساختار/کامپوننت/صفحهای برای پروتوتایپ ساخته نشد.
- هیچ تغییری در `mimo-ui/UPGRADE`، ZIP، MANIFEST، verifier، یا طرح v12 در Drive.
- هیچ ادعای اجرای زنده / رفتار رانشدهٔ اپ / VPN واقعی / تأیید کاربر.
