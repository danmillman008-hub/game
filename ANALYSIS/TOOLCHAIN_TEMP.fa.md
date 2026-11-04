# نصب موقت ابزارها — صورت وضعیت دقیق

> **REVIEW / موقت.** همانطور که گفتید «اکوسیستم فعلی بسیار بهتره، صرفاً موقت نصب کن». هیچکدام از این ابزارها وارد ریپو، ZIP، MANIFEST، وریفایر، درایو یا پروتوتایپ **نشدند**. همه زیر `/home/user/_work/_tmp_tools/` و `/home/user/_work/_analysis/` هستند و با یک `rm -rf` پاک میشوند؛ خط لولهٔ استخراجِ خود ریپو جایگزین نشد.

## ۱. `morluto/rea` — ✅ نصب و استفاده شد

| مورد | مقدار |
|---|---|
| کلون | `/home/user/_work/_tmp_tools/rea` (شالو، ۱۲۴ MB، `main`) |
| بستهٔ CLI | `npm install rea-agents` → `/home/user/_work/_tmp_tools/rea-npm` — نسخهٔ `rea@6.7.0`، ۱۴۸ پکیج |
| `rea doctor` | ناسالم صرفاً بهدلیل نبود engineها: `ghidra` → `GHIDRA_INSTALL_DIR` تنظیم نشده، `jadx` → `REA_JADX_MCP_JAR` تنظیم نشده، `hopper`/`ida`/`kuna` → absent. خود Node/هاست سالم (`node 22.22.3`, `debian 12`). |
| `rea capabilities` | `rea-artifact-graph` provider **در دسترس**؛ `native-macos` بهدلیل هاست غیرفعال |
| **خروجی واقعی** | `rea inspect-artifact '<APK>' --format json` → `/home/user/_work/_analysis/evidence/rea_artifact.json` (۱۶٬۲۹۵٬۰۴۵ بایت) |
| Evidence ID | `ev_cbbbefbf1ed8230551034c3f9d5ab72b9f19ad938841639ec19fe0a9ceef11b2` |
| مشاهدات | `node_count=14063`, `occurrence_count=14399`, `edge_count=14398`, `integrity_contradictions=0`, `confidence=observed`, `authority=shipped-artifact`، SHA‑256 ریشه = `48ce1740aa…` (منطبق با ریپو) |
| Limitations (عیناً) | «bounded static hypotheses; does not execute the artifact» · «ZIP inventory lists central‑directory entries only; APK Signing Block / ZIP comment not occurrences» |
| ابزاری که کار **نکرد** | `inspect-android-package`, `search-android-classes`, `inspect-android-class`, `inspect-android-method`, `trace-android-references`, `decode-android-resources`, `rea analyze` → همگی `capability_unavailable / unsupported_provider`. دلیل: provider `jadx` به `jadx-headless-mcp 0.7.1` JAR نیاز دارد و `apktool` هم نصب نیست. |
| متدولوژی بهکاررفته | `.agents/skills/reverse-engineer-anything/SKILL.md`, `references/evidence-workflows.md`, `references/android-applications.md`, `references/runtime-observation.md`, `references/environments.md` — اصل «شاهد، حدود پوشش، ناشناختههای باقیمانده، عدم ادعای اجرا» در سند اصلی رعایت شد. |

**چرا JAR نیامد**: `docs/android-analysis.md` آن را از `github.com/1013503897/jadx-headless-mcp/releases/download/v0.7.1/jadx-headless-mcp-0.7.1-all.jar` میگیرد. `api.github.com` شناسهٔ asset را برگرداند (`571963366`، ۴۲٫۶ MB) ولی دانلود به `release-assets.githubusercontent.com` ریدایرکت میشود که در allowlist شبکهٔ این سندباکس نیست. بستهٔ npm همنام (`jadx-headless-mcp@0.7.0`) فقط ۴۶ KB کد JS دارد و **هیچ JARــی** درونش نیست. جستجوی کد گیتهاب برای JAR وندورشده هم ۰ نتیجه داد.

## ۲. `NationalSecurityAgency/ghidra` — ⚠️ سورس + JDK نصب شد، headless اجرا نشد

| مورد | مقدار |
|---|---|
| کلون | `/home/user/_work/_tmp_tools/ghidra` (شالو، `--filter=blob:none`، ۴۴۴ MB، `master`، Ghidra 12.2) |
| JDK | `jdk4py==21.0.8.2` → `/home/user/_work/_tmp_tools/pylib/jdk4py/java-runtime` (OpenJDK 21.0.8) · `jdk4py==25.0.2.1` → `/home/user/_work/_tmp_tools/jdk25/jdk4py/java-runtime` (OpenJDK 25.0.2) — هر دو از PyPI، چون `java`/`javac` از قبل وجود نداشت |
| نیازمندی رسمی | `README.md`: **JDK 25** + **Gradle 9.1.0+** (+ Python، GCC/Clang، make) برای build سورس؛ برای اجرا، **release ZIP** پیشساخته لازم است (`ghidra_12.2_PUBLIC_20261016.zip`، ۵۶۹٬۷۱۲٬۷۰۸ بایت) |
| مسدودشدها | `release-assets.githubusercontent.com` / `objects.githubusercontent.com` (asset ریلیزها)، `services.gradle.org` / `downloads.gradle.org` (توزیع Gradle)، `repo1.maven.org` (وابستگیها)، `raw.githubusercontent.com`. پروب صریح: `HTTP 000` برای همه. فقط `github.com`, `codeload.github.com`, `api.github.com`, `registry.npmjs.org`, `pypi.org`, `files.pythonhosted.org` بازاند. |
| نتیجه | `analyzeHeadless` و provider Ghidra در REA **اجرا نشدند** (`GHIDRA_INSTALL_DIR` معتبری وجود ندارد). ادعای دیکامپایل نشده است. |
| استفادهای که شد | سورس بهعنوان **مرجع فرمت** بررسی شد: `Ghidra/Features/FileFormats/src/main/java/ghidra/file/formats/android/{dex,cdex,multidex,odex,vdex,wdex,oat/oatdexfile}` و `Ghidra/Processors/Dalvik/src/main/java/ghidra/dalvik/dex`. پارسر `string_ids`/`type_ids`ای که برای سرشماری DEX نوشتیم، مطابق همان ساختار هدر DEX عمل میکند. |

## ۳. موتورِ actuallyـاً اجراشده (باز هم موقت، بیرون ریپو)

| ابزار | منبع | نقش |
|---|---|---|
| `androguard==4.1.4` | PyPI → `/home/user/_work/_tmp_tools/pylib` | تأیید بسته و همراستایی با اکوسیستم RE/ریپو |
| پارسر مستقیم DEX (چند ده خط Python) | `/home/user/_work/_analysis/dex/` | خواندن `string_ids_size/off`, `type_ids_size/off` از هدر DEX، ULEB128 + MUTF‑8 → **۱۰۵٬۶۱۱ رشتهٔ یکتا، ۳۲٬۶۸۴ تایپ** در ۱۲ DEX؛ خروجی `ALL_strings.json`, `ALL_types.json`، و ۱۲ فایل `*_strings.txt` |
| `zipfile` استاندارد | `/home/user/_work/_analysis/mimo_assets/` | استخراج ۱۰٬۳۵۲ فایل JSON/JS/HTML/CSS/proto از `assets/` + `res/raw/` (۶۲۵٬۰۵۲٬۵۴۸ بایت اندازهٔ unpacked)، سپس شمارش کامل اسکیمای ۱٬۰۲۹ `tutorial-*.json` انگلیسی |
| جدول ARSC ریپو | `mimo-ui/SOURCE/values/values/string.xml` (۱٬۷۲۱ رشته) | نامها/قوانین امتیازدهی |
| jsdom از قبل | `/home/user/_work/v6check/check_v12_6.js` | فقط جهت اطمینان از سالم ماندن پروتوتایپ: ۱۶۰ تست / ۰ خطا (هیچ تغییری به پروتوتایپ داده نشد) |

**تطبیق متقابل**: شمارش تازهٔ DEX (`53730 / 50215 / 16718`) دقیقاً با `mimo-ui/CATALOGS/DEX_CENSUS.json` جور شد؛ ۱۴٬۳۹۸ entry تازه هم دقیقاً با `APK_ENTRY_CENSUS.csv`. یعنی ابزار موقت **چیزی را خراب نکرد و نتیجهٔ خط لولهٔ اصلی را تأیید کرد**.

## ۴. پاکسازی / موقتبودن

```bash
# هر زمان خواستید، کل نصب موقت پاک میشود؛ ریپو untouched میماند:
rm -rf /home/user/_work/_tmp_tools /home/user/_work/_analysis
```

- هیچ فایلی زیر `mimo-ui/UPGRADE/` تغییر نکرد؛ `verify_upgrade.py` همچنان **PASS ۲۵۹/۲۵۹** است.
- هیچ وابستگی به `package.json` / `requirements.txt` / MANIFEST / `reproduce[]` اضافه نشد.
- اسناد تحلیلی در `ANALYSIS/` (ریشهٔ ریپو، بیرون از بستهٔ تحویلی `UPGRADE/`) هستند تا زنجیرهٔ ZIP/درایو v12.5‑fa دستنخورده بماند.

## ۵. آنچه برای «مرحلهٔ بعد» لازم است (پیشنیاز محیطی)

برای اینکه تحلیل از «ایستا» به «دقیق تا بایتکد و رفتار» برسد، یکی از این دو لازم است:
1. محیطی با دسترسی به `release-assets.githubusercontent.com` (Ghidra release + `jadx-headless-mcp` JAR) و `services.gradle.org` / Maven Central، **یا**
2. تأمین همان JAR/ZIP بهصورت فایل توسط شما و تنظیم `REA_JADX_MCP_JAR` / `GHIDRA_INSTALL_DIR` / `JAVA_HOME` (JDK 25 آماده است).

بدون آن، گام «A» در نقشهٔ مرحلهٔ بعد (`00_MIMO_DEEP_ANALYSIS.fa.md` §۱۰) قابلاجرا نیست و ناشناختههای §۹ باقی میمانند.
