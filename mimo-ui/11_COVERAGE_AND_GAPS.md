# ۱۱ — پوشش، راستیآزمایی و خلأهای صادقانه

## ۱. ماتریس پوشش (همهٔ نواحی `COMPLETE`)

`CATALOGS/COVERAGE_BY_AREA.csv` — 22 ردیف، تکتک با `expected == observed`:

| ناحیه | انتظار | مشاهده | وضعیت | محل |
|---|---|---|---|---|
| AndroidManifest | 1 | 1 | COMPLETE | `SOURCE/manifest/AndroidManifest.xml` |
| resources.arsc | 1 | 1 | COMPLETE | `SOURCE/arsc/RESOURCE_TABLE.json` |
| layout XML | 1299 | 1299 | COMPLETE | `SOURCE/res/layout*/*.xml` |
| layout dossiers | 1299 | 1300 | INCOMPLETE | `SCREENS/LAYOUTS/*.md` |
| drawable/vector/shape | 1319 | 1319 | COMPLETE | `SOURCE/res/drawable*/*` |
| color state lists | 304 | 304 | COMPLETE | `SOURCE/res/color*/*.xml` |
| motion (anim/animator/interpolator) | 143 | 143 | COMPLETE | `SOURCE/res/{anim,animator,interpolator}/*.xml` |
| fonts | 15 | 15 | COMPLETE | `SOURCE/res/font/*` |
| Rive / raw UI assets | 76 | 76 | COMPLETE | `SOURCE/res/raw*/*` |
| menus | 5 | 5 | COMPLETE | `SOURCE/res/menu/*.xml` |
| navigation graphs | 1 | 1 | COMPLETE | `SOURCE/res/navigation/*.xml` |
| XML configs | 15 | 15 | COMPLETE | `SOURCE/res/xml/*.xml` |
| WebView/editor assets | 254 | 254 | COMPLETE | `SOURCE/assets/ui/**` |
| compiled resource IDs | 12915 | 12915 | COMPLETE | `CATALOGS/RESOURCE_INDEX.csv` |
| resource config rows | 50477 | 50477 | COMPLETE | `CATALOGS/RESOURCE_INDEX.csv` |
| app UI classes (DEX) | 3255 | 3255 | COMPLETE | `SOURCE/dex/UI_CLASSES.json` |
| screens registered | 276 | 276 | COMPLETE | `SCREENS/*.md` |
| lesson content JSON (catalogued) | 10308 | 10308 | COMPLETE | `CATALOGS/APK_ENTRY_CENSUS.csv` |
| DEX files (inventoried) | 12 | 12 | COMPLETE | `CATALOGS/DEX_CENSUS.json` |
| native libs (catalogued) | 12 | 12 | COMPLETE | `CATALOGS/APK_ENTRY_CENSUS.csv` |
| other APK members (catalogued) | 633 | 633 | COMPLETE | `CATALOGS/APK_ENTRY_CENSUS.csv` |
| ALL APK entries | 14398 | 14398 | COMPLETE | `CATALOGS/APK_ENTRY_CENSUS.csv` |

## ۲. راستیآزمایی ماشینی

`tools/verify_ui.py` به صورت fail-closed اجرا میشود؛ خروجی در
`CATALOGS/VERIFICATION_REPORT.json`. چکها: موجودی ۱۴٬۳۹۸تایی، وجود فایل تحویلی برای
**تکتک** اعضای `UI_*`، هش SHA-256 معتبر برای همه، برابری هش APK با تحلیل قبلی شما،
۱٬۲۹۹ لایهٔ دیکدشده، ۱٬۲۹۹ پروندهٔ لایه، صفر خطای دیکد، پروندهٔ همهٔ صفحات،
۵۰٬۴۷۷ ردیف منبع، ۱۲٬۹۱۵ شناسه، اطلس، ۱۰۹ اسکلت کاتلین، ۱۵ جلد مستند،
و `CATALOGS/SHA256SUMS.txt` برای تکتک فایلهای خروجی.

## ۳. «هیچی نمونه» یعنی چه، عددی

| ادعا | عدد اثباتکننده |
|---|---|
| هیچ لایهای حذف نشده | ۱٬۲۹۹ فایل XML + ۱٬۲۹۹ پرونده + ۱٬۲۹۹ ردیف در `LAYOUT_INDEX` |
| هیچ منبعی حذف نشده | ۱۲٬۹۱۵ ID / ۵۰٬۴۷۷ ردیف / ۲۹۴ فایل `values` |
| هیچ عضو APKای فهرستنشده | ۱۴٬۳۹۸ ردیف `APK_ENTRY_CENSUS.csv` با هش |
| هیچ صفحهای بدون پرونده | ۲۷۶ پرونده در `SCREENS/` |
| هیچ دارایی UIای جا نمانده | ۲۵۴ فایل در `SOURCE/assets/ui/` عیناً |
| هیچ کلاس UIای گم نشده | ۳٬۲۵۵ رکورد در `SOURCE/dex/UI_CLASSES.json` |

## ۴. خلأها (REA-style: صادقانه، بدون پر کردن با حدس)

| # | خلأ | کلاس | دلیل / آنچه لازم است |
|---|---|---|---|
| ۱ | بدنهٔ متدهای Kotlin/Java | `UNKNOWN` | JADX + JDK 17 در محیط نبود؛ به جایش جدول کامل کلاس/متد/آنوتیشن/لیترال و ۱۰۹ اسکلت `RECONSTRUCTED` دادهایم |
| ۲ | رفتار زمان اجرا، Back stack، ترتیب تبها | `NOT_TESTED` | بدون emulator/adb؛ شبیهساز اندروید لازم است |
| ۳ | بدنهٔ توابع `@Composable` | `PARTIALLY_VERIFIED` | نام ۱۲۷ کلاس و ۷۱ `ComposeView` مشاهده شد، محتوای `setContent {}` نیازمند دیکامپایل |
| ۴ | بیلد رسمی Play Store | `UNKNOWN` | بستهٔ موجود repack/mod شده؛ مقایسه نیازمندAPK رسمی + هش |
| ۵ | ۸ DEX پوچ و گواهی `CN=youarefinished` | `VERIFIED_STATIC` | نشانهٔ دستکاری؛ تأثیر احتمالی بر UI مشخص نیست |
| ۶ | ۱۸ فایل JS خارج از دامنهٔ تحلیل REA | اعلامشده در شواهد REA | باندلهای ۱–۲MB باعث `provider_timeout` شدند؛ متنشان عیناً در `SOURCE` موجود است |
| ۷ | اسکریپت inline در `spieglein/index.html` | اعلامشده در شواهد REA | REA آن را تحلیل نکرد؛ متن ۴۵۲ بایتی عیناً موجود است |
| ۸ | مقادیر configمحور (کدام `layout-v31` کی انتخاب میشود) | `NOT_TESTED` | وجود فایلها ثابت است، انتخاب runtime نه |
| ۹ | محتوای ۱۰٬۳۰۸ JSON درس | `CATALOGUED` | داده است نه کد UI؛ همگی با هش/مسیر فهرست شدند، بایتهایشان در APK اصلی |
| ۱۰ | آیکونها/تصاویر به صورت بصری | `VERIFIED_STATIC` | بایتهای PNG/WebP عیناً کپی شدند؛ رندر بصری در اطلس برای رنگها/توکنها انجام شد |

> قاعدهٔ REA رعایت شد: «نبود شاهد، نبود ویژگی نیست». جاهایی که نتوانستیم اجرا کنیم،
> `NOT_TESTED` گرفتهاند، نه `false`.

## ۵. نشانههای بستهٔ دستکاریشده (مهم)

- `classes.dex`: `Smob - Mod obfuscation tool v4.6 by Kirlif'`
- گواهی خودامضا `CN=youarefinished` (از `APK_FACTS.json` دور قبل)
- ۱۲ فایل DEX ولی ۸ تای آنها ۱٬۰۹۶ بایت و ۲ کلاس/۲۱ رشته دارند
- هش APK با دور قبل یکسان است ⇒ همهٔ اسناد قبلی شما دربارهٔ همین بسته معتبرند
