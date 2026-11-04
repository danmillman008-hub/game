# نصب `storytold/craft-anything` روی عامل — گزارش صادقانه
<!-- v8-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v8](20_DESIGN_ROUND_8.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.
<!-- v7-banner -->
> ⚠️ **بایگانی / superseded:** طراحی فعلی **[DESIGN v7](18_DESIGN_ROUND_7.md)** است. همچنان فقط پلن/دیزاین؛ هیچ کد محصولی نوشته نشده.

> ⚠️ **بایگانی / superseded:** این سند مربوط به دورهای قبل است. طراحی فعلی **[DESIGN v6](17_DESIGN_ROUND_6.md)** است؛ صفحهٔ ورود حذف، یادگیری بازسازی و زیرصفحات «انتخاب مسیر / نمای مسیر / داخل مبحث» از کد اضافه شدند. لاگهای قدیمی صرفاً ردپای حسابرسیاند.

درخواست: «الان همینم نصب کن روی خودت» (`https://github.com/storytold/craft-anything.git`).

## آنچه واقعاً نصب شد

| لایه | وضعیت | مسیر |
|---|---|---|
| سورس v0.3.0 (shallow clone) | ✅ | `/home/user/_work/craft-anything` (خارج از ریپو، scratch) |
| مستندات رسمی + `AGENTS.md` + `CLAUDE.md` + ۴ اسکیمای JSON + `tools.md` (فهرست ۳۲۰ ابزار) + لایسنسها | ✅ وندور شده | `UPGRADE/CRAFT_ANYTHING/upstream_docs/` |
| **لایهٔ عاملی قابلاجرا** (همان شناسههای ابزار، همان قرارداد شواهد، چرخهٔ Study → Build → Check → Ready) | ✅ نصب و اجرا شده | `UPGRADE/CRAFT_ANYTHING/craft_adapter.py` |
| workspace با `craft.json` / `investigation.cany.json` / `plan.json` / `unknowns.json` / `brief.md` | ✅ ساخته و پُر شده | `UPGRADE/CRAFT_ANYTHING/workspace/` |
| خروجی شواهد صادرشده | ✅ | `UPGRADE/CATALOGS/EVIDENCE_LEDGER.json` |
| باینری Rust CLI/AppImage/deb v0.3.0 | ❌ نصب نشد | دلیل در ادامه |
| سرور MCP / دسکتاپ egui / کدینگإیجنت خارجی | ❌ | نیاز به باینری و GTK/agent CLI؛ در این محیط موجود نیست |

## چرا باینری native نصب نشد (و دوباره امتحان نشد)

- `gh release download v0.3.0 --pattern 'craft-anything-0.3.0-linux-x86_64.tar.gz'`, الگوی `SHA256SUMS.txt`، `gh api .../releases/assets/702372637 -H 'Accept: application/octet-stream'` و `curl -L` مستقیم، همگی با `TLS EOF` / `SSL_ERROR_SYSCALL` شکست خوردند: داراییهای release روی `release-assets.githubusercontent.com` و `objects.githubusercontent.com` هستند که **خارج از allowlist خروجی این سندباکس** قرار دارند (`github.com`, `codeload.github.com`, `api.github.com`, `registry.npmjs.org`, `pypi.org`, `files.pythonhosted.org` مجازاند).
- `cargo`, `rustc`, `rustup` وجود ندارند؛ `apt-cache policy rustc cargo` هیچ بستهای برنگرداند؛ ساخت از سورس نیاز به Rust 1.97+ و کتابخانههای GTK dev دارد.
- بستهٔ npm به نام `craft-anything` وجود ندارد (`npm view` → 404)؛ پکیج PyPI معادل هم نیست.
- بنابراین **همان مسیر unchanged دوباره امتحان نشد**؛ بهجای آن لایهای نصب شد که عامل واقعاً بتواند فراخوانی کند.

## چگونه از آن استفاده شد (قابل تکرار)

```
python3 UPGRADE/CRAFT_ANYTHING/craft_adapter.py commands
python3 UPGRADE/CRAFT_ANYTHING/craft_adapter.py doctor
python3 ... core-target-open --path <apk> --label <name>
python3 ... core-finding-record --text <...> --confidence VERIFIED_STATIC
python3 ... core-unknown-add --text <...>
python3 ... core-plan-update --phase P0 --status PLANNED
python3 ... core-evidence-show
python3 ... core-evidence-export --out UPGRADE/CATALOGS/EVIDENCE_LEDGER.json
```

نتیجهٔ `doctor`: `READY (agent adapter)`، حالت `deep` (چون داخل APKها را خواندهایم)، ۳ target، ۱۳ رکورد شواهد، ۸ فاز، ۵ ناشناخته.

قرارداد شواهد رعایت شده است: هر رکورد `evidence_id`, `operation`, `toolset`, `subject`/`content`, `confidence`, `authority`, `coverage`, `limitations`, `locations`, `created_ms` دارد. قواعد طلایی upstream که در این دور اعمال شدند: «Evidence is the result»، «Never crash»، «Clean room vs Deep»، «Effects are honest»، «No secrets»، «Thin UI / theme tokens».

## نسبت با REA

`morluto/rea` (الزام قبلی شما) همچنان منبع **انضباط شواهد** و استخراج جاوااسکریپت/WebView میمو است؛ `craft-anything` در این دور بهعنوان **چارچوب مطالعه/ساخت/بررسی و دفتر شواهد** روی همان دادهها سوار شد. هر دو در `11_EVIDENCE_AND_CROSSWALK.md` با سطح اطمینان مشخص شدهاند. تولید اپ همچنان **clean-room** است: هیچ دارایی، کد، نام یا متنی از Mimo/همدرس/هدفپلاس به محصول کپی نمیشود؛ فقط قراردادها و الگوهای رفتاری مستند میشوند.

## محدودیت صریح

این آداپتور **جایگزین موتور ۳۲۰ ابزاری Rust نیست**؛ فقط لایهای است که عامل بتواند همان روش را در این محیط اجرا کند. ابزارهایی که در upstream به باینری وابستهاند (`android_dart_snapshot_show` عمیق، `core_disasm_*`, Ghidra/adb/CDP) اینجا اجرا نشدند؛ معادل استاتیک آنها (`extract_source_apps.py` + androguard + استخراج رشتهها) استفاده شد و در ستون `limitations` ثبت گردید.
