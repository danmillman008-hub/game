# ۱۲ — بازتولید گامبهگام (دقیقاً همان کاری که کردیم)

همهٔ مراحل ایستا، بیهیچ اجرای اپ و بیهیچ تغییر در APK.

```bash
# ۰) پیشنیاز
python3 -m venv /tmp/venv && /tmp/venv/bin/pip install androguard==4.1.4
# (اختیاری) node/npm برای شواهد رسمی REA: npx -y rea-agents@6.8.0

# ۱) سه بخش آرشیو را از Google Drive → پوشهٔ mimo بگیرید
#    Mimo_9.35 (1).z01 / .z02 / .zip  (۵۲٬۴۲۸٬۸۰۰ + ۵۲٬۴۲۸٬۸۰۰ + ۳۱٬۰۶۹٬۳۶۸ بایت)
sha256sum Mimo_9.35\ \(1\).z01 Mimo_9.35\ \(1\).z02 Mimo_9.35\ \(1\).zip
# 1e3a4115…93b18   1ac22ab2…4f539   91c67086…2b7

# ٢) بازسازی APK (دستور دقیق)
cat 'Mimo_9.35 (1).z01' 'Mimo_9.35 (1).z02' 'Mimo_9.35 (1).zip' > /tmp/mimo_full.zip
unzip -o /tmp/mimo_full.zip -d /tmp/apk
sha256sum '/tmp/apk/Mimo_9.35 (1).apk'
# 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a

# ٣) استخراج کامل
/tmp/venv/bin/python tools/extract_ui.py --apk '/tmp/apk/Mimo_9.35 (1).apk' --out .
# خروجی: SOURCE/, CATALOGS/, MANIFEST.json  (۲۱ ثانیه)

# ۴) پروندهها، کد بازسازیشده، اطلس
/tmp/venv/bin/python tools/build_dossiers.py
/tmp/venv/bin/python tools/build_atlas.py
/tmp/venv/bin/python tools/write_docs.py
gzip -9 -c ATLAS/data.json > ATLAS/data.json.gz && rm ATLAS/data.json

# ۵) راستیآزمایی fail-closed
/tmp/venv/bin/python tools/verify_ui.py
# → {"status": "PASS", "checks": 18, "failed": [], ...}

# ۶) مشاهدهٔ اطلس (اختیاری؛ فایل بهتنهایی هم باز میشود)
python3 -m http.server 8080 --bind 0.0.0.0 -d ATLAS
```

## شواهد رسمی REA (همان ریپوی که معرفی کردید)

```bash
npx -y rea-agents@6.8.0 analyze-javascript-application SOURCE/assets/ui \
  --source-path lesson-webview.js --source-path lesson-webview-fonts.js \
  --source-path spieglein/index.html --source-path prettier/index.html \
  --source-path testdata/127-0-1.html … (۱۵ فایل) \
  --analysis-timeout-ms 120000 --max-semantic-nodes-per-file 4000 --format json \
  > REFERENCE/REA_EVIDENCE/JS_EVIDENCE.json
```

> تحلیل **همهٔ** ۳۳ فایل JS/HTML با `provider_timeout` شکست خورد (باندل `standalone.js`
> ۱٫۰MB و `editor.bundle.js` ۲٫۴MB). نسخهٔ کامل همان تلاش ناموفق هم به عنوان شاهد
> محدودیت محیط در `11` ثبت شده؛ انتخاب ۱۵ فایلِ نوشتهشده توسط Mimo موفق شد.

## خروجی قابل انتظار

| فایل | مقدار |
|---|---|
| `MANIFEST.json` | هش، نسخه، ۱۴٬۳۹۸ عضو، ۵۰٬۴۷۷ ردیف منبع، شمارشها |
| `CATALOGS/APK_ENTRY_CENSUS.csv` | ۱۴٬۳۹۸ ردیف |
| `SOURCE/res/layout*/` | ۱٬۲۹۹ فایل XML |
| `SCREENS/` | ۱٬۵۷۷ فایل Markdown |
| `ATLAS/index.html` | اطلس آفلاین ~۱۹MB |
| `CATALOGS/VERIFICATION_REPORT.json` | `PASS` |
