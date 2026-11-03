# ۱۳ — ردیابی ادعا → شاهد (Traceability)

هش بسته: `48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a`

| # | ادعا | فایل شاهد | کلاس |
|---|---|---|---|
| ۱ | بسته `com.getmimo` 9.35 / ۱۴٬۳۹۸ عضو | `MANIFEST.json`, `CATALOGS/APK_ENTRY_CENSUS.csv` | `VERIFIED_STATIC` |
| ۲ | هش بسته با تحلیل قبلی یکسان است | `REFERENCE/PRIOR_WORK/APK_HASHES.json` | `VERIFIED_STATIC` |
| ۳ | ۶۱ activity / ۶ alias / ۴۶ `<data>` | `SOURCE/manifest/AndroidManifest.xml` | `VERIFIED_STATIC` |
| ۴ | ۱٬۲۹۹ لایه در ۱۰ پوشه | `SOURCE/res/layout*/`, `CATALOGS/LAYOUT_INDEX.csv` | `VERIFIED_STATIC` |
| ۵ | ۲٬۸۵۹ فایل AXML بیهیچ خطا دیکد شد | `CATALOGS/DECODE_ERRORS.json` (خالی), `SOURCE/_raw_axml/` | `VERIFIED_STATIC` |
| ۶ | ۱۲٬۹۱۵ شناسه / ۵۰٬۴۷۷ ردیف منبع | `SOURCE/arsc/RESOURCE_TABLE.json`, `CATALOGS/RESOURCE_INDEX.csv` | `VERIFIED_STATIC` |
| ۷ | ۱٬۱۹۸ رنگ، ۱٬۴۰۱ دایمن، ۱٬۷۲۱ رشته | `CATALOGS/DESIGN_TOKENS.json`, `SOURCE/values/` | `VERIFIED_STATIC` |
| ۸ | ۲۵۴ دارایی کد WebView عیناً | `SOURCE/assets/ui/`, `CATALOGS/APK_ENTRY_CENSUS.csv` | `VERIFIED_STATIC` |
| ۹ | ۳٬۲۵۵ کلاس UI / ۱٬۹۲۳ کلاس `ui.*` / ۱۲۷ Compose | `SOURCE/dex/UI_CLASSES.json`, `CATALOGS/DEX_CENSUS.json` | `VERIFIED_STATIC` |
| ۱۰ | ۱۰۹ کلاس دقیقاً `R.layout.X` را inflate میکنند | `SOURCE/dex/LAYOUT_XREFS.csv`, operandهای `const` DEX | `VERIFIED_STATIC` |
| ۱۱ | ۷۱ لایه `ComposeView` و ۶ لایه `WebView` دارند | `CATALOGS/LAYOUT_INDEX.json` → فیلدهای `compose_views`/`webviews` | `VERIFIED_STATIC` |
| ۱۲ | ۵۳ ویوی سفارشی `com.getmimo` | همان فایل → `custom_views` | `VERIFIED_STATIC` |
| ۱۳ | ۲۷۶ سطح رابط ثبت شده | `CATALOGS/SCREEN_INDEX.csv`, `SCREENS/*.md` | `VERIFIED_STATIC` + `DERIVED` |
| ۱۴ | نگاشت صفحه → لایه | `SOURCE/dex/LAYOUT_XREFS.csv` + تطابق نام → `DERIVED` | `DERIVED` |
| ۱۵ | حالتها (offline/empty/error/…) | نام رشتهها در `SOURCE/values/values/string.xml` | `PARTIALLY_VERIFIED` |
| ۱۶ | بدنهٔ متدها / رفتار runtime | — (JADX/emulator موجود نبود) | `NOT_TESTED` / `UNKNOWN` |
| ۱۷ | بسته repack/mod شده | رشتهٔ `Smob…`, ۸ DEX پوچ, گواهی خودامضا | `VERIFIED_STATIC` |
| ۱۸ | پروتکل پیام WebView | `SOURCE/assets/ui/lesson-webview.js` + `REFERENCE/REA_EVIDENCE/JS_EVIDENCE.json` | `VERIFIED_STATIC` |
| ۱۹ | محدودیتهای تحلیل REA | `JS_EVIDENCE.json → limitations` (۸ مورد) | `VERIFIED_STATIC` |
| ۲۰ | پوشش کامل | `CATALOGS/COVERAGE_BY_AREA.csv`, `VERIFICATION_REPORT.json` | `DERIVED` |

## فهرست هش خروجیها

`CATALOGS/SHA256SUMS.txt` شامل SHA-256 تکتک فایلهای این پوشه است (بهجز خود فایل هشها)،
پس هر تغییری بعد از تحویل قابل تشخیص است.
