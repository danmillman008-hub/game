# بازتولید تحلیل (Reproduce)

این پوشه، ابزارهای مرحله‌به‌مرحله‌ای است که برای ساخت `MIMO-REPORT.md` استفاده شد. ترتیب اجرا:

## ۰) بازسازی APK از ZIP چندپاره
فایل‌های `Mimo_9.35 (1).zip` + `.z01` + `.z02` یک آرشیو ZIP چندپاره هستند که **بخش `.zip` آخرین قطعه است** (central directory در آن قرار دارد). ترتیب درست اتصال:

```bash
cat "Mimo_9.35 (1).z01" "Mimo_9.35 (1).z02" "Mimo_9.35 (1).zip" > mimo_full.zip
unzip mimo_full.zip          # → Mimo_9.35 (1).apk
sha256sum "Mimo_9.35 (1).apk"
# 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
```

> اگر `unzip` هشدار «extra bytes at beginning» داد، طبیعی است (unzip از multi-part پشتیبانی کامل ندارد) ولی استخراج درست انجام می‌شود.

## ۱) موجودی ایستا (بدون Java)
```bash
python3 -m venv .venv
.venv/bin/pip install androguard
.venv/bin/python tools/analyze_apk.py "Mimo_9.35 (1).apk" out/
```
خروجی: `manifest.json`, `all-classes.txt`, `all-dex-strings.txt`, `apk.sha256`.
این مرحله معادل `inspect_android_package` + `search_android_classes` در REA است، با پارسر DEX پایتونی (بدون JVM).

## ۲) تحلیل محتوا (پداگوژی)
```bash
unzip "Mimo_9.35 (1).apk" 'assets/lessons-en/*' -d extracted/
python3 tools/analyze_content.py extracted out/ en
```
خروجی: `content_stats.json` (واژگان DSL، آمار تعامل‌ها، Hard Mode…) و `curriculum-map.json`.
برای مقایسهٔ زبان‌ها: `de`, `fr`, `es`, `it`, `pt`, `pl`, `ru`, `tr`, `id`.

## ۳) بازیابی مدل‌های داده از `const-string` (بدون دی‌کامپایلر)
الگو: هر کلاس Kotlin با `data class` یک `toString()` دارد که نام فیلدها را به‌صورت رشته ثابت نگه می‌دارد. پس با اسکن `const-string` می‌توان قرارداد داده را بازسازی کرد، حتی وقتی نام کلاس‌ها مبهم شده‌اند:

```python
from androguard.core.dex import DEX
# برای هر کلاس/متد، دستورهای const-string را جمع کن و الگوی "Name(field=" را جست‌وجو کن
```
نمونهٔ نتایج این تکنیک در گزارش:
```
ExecuteFilesResponse(hasPassed=, consoleOutput=, error=, tests=, hostedProjectUrl=)
ExecuteLessonTestCase(hasPassed=, description=, error=)
ChallengeTestCase(hasPassed=, requirement=, description=)
RunSuccessful(hasPassed=, consoleOutput=, browserOutput=, tests=, showRewardBadge=, rewardedSparksForCorrectAnswer=)
SystemMessage$Executable(instructions=, expectedAnswer=, pathName=)
```

## ۴) گام بعدی (نیازمند Java)
```bash
# JDK 17 + JADX-MCP headless، سپس طبق REA:
rea doctor --provider jadx --json
# inspect_android_method روی:
#   com.getmimo.ui.lesson.interactive.validatedinput.*
#   com.getmimo.ui.lesson.executable.*        (منطق مقایسه/تست)
#   com.getmimo.analytics.*                   (تاکسونومی رویدادها)
```
برای ترافیک واقعی: `mitmproxy` + `Frida` (bpinning) روی شبیه‌ساز، و مشاهدهٔ payloadهای
`/runFiles`, `/v2/client-config`, `/v2/purchase`.

## چارچوب مرجع
- REA — Reverse engineer anything with agents: <https://github.com/morluto/rea>
  - `.agents/skills/reverse-engineer-anything/references/android-applications.md`
  - `docs/android-analysis.md`
