# اندپوینت‌های واقعی سامانهٔ تیتک — استخراج‌شده از خود اپلیکیشن

منبع: فایل `ttac-4.3.6.apk` (بستهٔ `ir.ttac.irfdamobile`، نسخهٔ نمایشی `6.9.1`، `versionCode 60031`، `compileSdk 30`) — همان فایلی که در همین ریپو آپلود شد.
روش: باز کردن APK → استخراج `resources.arsc` → خواندن `res/values/strings.xml` با `androguard` → دی‌کامپایل کلاس‌های شبکه (`Lu6/*`) و مدل‌های پاسخ (`ir/ttac/irfdamobile/model/**`) با `androguard`.

نتیجهٔ مهم: **اپ موبایل تیتک برای استعلام کد اصالت / UID / بارکد، هیچ کلید API نمی‌خواهد** و درخواست را با `GET` ساده به دامنهٔ خودش می‌فرستد.

---

## ۱) استعلام کد (همان چیزی که در اپ «بررسی بارکد و UID» است)

کلاس `Lu6/t` — سه حالت دارد و آدرس را از `R.string.wrapperV2URL` می‌سازد:

| نوع کد | متد و مسیر | پارامتر |
|---|---|---|
| کد اصالت ۱۶ رقمی | `GET /api/WrapperV2/CheckSixteenCode` | `sixteenCode` |
| شناسهٔ رهگیری UID (۲۰ رقم) | `GET /api/WrapperV2/CheckUid` | `uidCode` |
| بارکد / GTIN | `GET /api/WrapperV2/CheckBarcode` | `barcode` |

آدرس پایه: `https://irfdamobile.ttac.ir/api/`

### نمونهٔ کامل درخواست

```
GET https://irfdamobile.ttac.ir/api/WrapperV2/CheckSixteenCode?sixteenCode=1234567890123456
    &latitude=0.0
    &longitude=0.0
    &device=2
    &deviceIdentifier=<شناسهٔ دستگاه>
    &Platform=1
    &PlatformVersion=30
    &VersionCode=60031
    &AppVersion=6.9.1
```

- `Platform=1` یعنی Android (`DeviceType.ANDROID.getValue()` در کلاس `ir/ttac/irfdamobile/model/general/DeviceType`).
- `PlatformVersion` = `Build.VERSION.SDK_INT`، `VersionCode`/`AppVersion` از `PackageInfo` خوانده می‌شوند.
- هدرها: فقط `User-Agent: ""` (بدون هیچ کلید یا توکن). تایم‌اوت هر دو سو ۳۰ ثانیه.
- کد با `URLEncoder.encode(code,"UTF-8")` فرستاده می‌شود.

### ساختار پاسخ (Gson → `ProductCatalogWebModel`)

```json
{
  "Success": true,
  "ErrorCode": 0,
  "Result": {
    "PersianName": "…",
    "EnglishName": "…",
    "Irc": "7310432273664919",
    "GTIN": "06260152410148",
    "UID": "…",
    "BatchCode": "…",
    "Expiration": "…",
    "Manufacturing": "…",
    "Price": "…",
    "Manufacturer": "…",
    "Importer": "…",
    "Distributer": "…",
    "StatusCode": 1,
    "StatusMessage": "کالا اصل است",
    "ErrorCode": "…",
    "ErrorMessage": "…"
  }
}
```

### معنی `StatusCode` (دقیقاً از enum `Code16Status` در APK)

| کد | نام در اپ | معنی |
|---|---|---|
| 0 | `NO_RESULT_AVAILABLE` | اطلاعاتی پیدا نشد |
| 1 | `GENUINE` | اصلی |
| 2 | `RECHECKED` | استعلام چندباره (چند شخص/سامانه) |
| 3 | `COUNTERFEIT` | تقلبی |
| 4 | `EXPIRED` | تاریخ گذشته |
| 5 | `RECALL` | ریکال (فراخوان) |
| 6 | `DOUBLE_CHECK` | استعلام دوباره (یک شخص/سامانه) |
| 7 | `NOT_RELEASED` | آزاد نشده |

---

## ۲) جزئیات فرآورده با IRC (تعداد در بسته، صاحب پروانه، قیمت)

کلاس `Lu6/d` → `DrugDetailInfo{ Result:{ …DrugLicense:{…} } }`

```
GET https://irfdamobile.ttac.ir/api/Wrapper/NfiDetailIrc?irc=7310432273664919
```

فیلدهای مهم `DrugLicense` (`DrugLicenseInfoVM`):
`FaBrandName`, `EnBrandName`, `GTIN`, `IRC`, `LicenseOwnerCompanyName`, `BrandOwnerCompanyName`,
`ProducerCompanyName`, `UnitOfUsePackaging` (مثل `20 in 1` = تعداد در بسته), `PackageConsumerPrice`,
`PersianExpirationDate`, `DrugGenericFaName`, `DrugGenericCode`, `IndexFaName`, `StatusStr`.

---

## ۳) جست‌وجوی نامی در کاتالوگ

کلاس `Lu6/e` و `Lu6/b` → `DrugGeneralInfo`

```
GET https://irfdamobile.ttac.ir/api/wrapper/NfiSearch?term=استامینوفن&pageNumber=1&pageSize=10
GET https://irfdamobile.ttac.ir/api/wrapper/NfiSearchByAtc?term=<ATC>&pageNumber=1&pageSize=10
```

پاسخ: `{Success, Count, PageNumber, PageSize, ErrorCode, Message, Result:{DrugLicenses:[…]}}`
که هر آیتم همان `DrugLicenseInfoVM` بالا است (نام، GTIN، IRC، شرکت، تعداد در بسته، قیمت).

---

## ۴) بقیهٔ اندپوینت‌های اپ (برای مرجع)

| کاربرد | آدرس |
|---|---|
| تنظیمات از سرور | `https://irfdamobile.ttac.ir/api/General/GetAndroidConfig` |
| موجودی‌های داروخانه | `https://irfdamobile.ttac.ir/api/MobilePerson/GetPharmacyInventories` |
| موجودی خانواده | `…/api/MobilePerson/GetPharmacyFamilyInventories` |
| فروش اخیر با بارکد | `…/Api/MobilePharmacy/GetRecentlySoldDrugPharmacyByBarcode` |
| فروش اخیر با UID | `…/Api/MobilePharmacy/GetRecentlySoldDrugPharmacyByUID` |
| فروش اخیر (فهرست) | `…/Api/MobilePharmacy/GetRecentlySoldDrugPharmacy` |
| جست‌وجوی داروخانه | `…/api/General/SearchPharmacy_V2` |
| داروخانه‌های نزدیک | `…/api/General/GetNearbyPharmacies_V2` |
| نظر داروخانه | `…/api/General/LoadPharmacyV2Comments` |
| ثبت نظر | `…/api/MobilePharmacyComments/AddPharmacyComment` |
| امتیاز داروخانه | `…/api/MobilePharmacyComments/UpdatePharmacyScore` |
| ورود/ثبت‌نام | `…/api/MobilePerson/LoginVerification`, `RegisterVerification`, `UpdatePersonData`, `UpdateSetting` |
| شیر خشک (newapi) | `https://newapi.ttac.ir/irfdamobile/v1/temporaryparticularfoodlicense?terms=…&pageNumber=…&pageSize=…&ClientIp=…` + هدر `X-SSP-Api-Key` |
| فروش اخیر شیر خشک | `https://newapi.ttac.ir/irfdamobile/v1/recentlysoldparticularfoodpharmacy` |
| گزارش عوارض (ADR) | `https://adr.ttac.ir/api/…` |

> هدر `X-SSP-Api-Key` فقط در سرویس‌های `newapi.ttac.ir` استفاده می‌شود (مقدار داخل خود APK: `f2f22843-2222-4371-8791-45c4fd14dee7`)؛ مسیرهای `irfdamobile.ttac.ir/api/Wrapper*` هیچ کلیدی نمی‌خواهند.

---

## ۵) کاربرد در برنامهٔ «انبارگردانی داروخانه»

فایل `pharmacy-inventory (3).html` حالا اول از همین API استفاده می‌کند:

1. کد اسکن‌شده اگر ۲۰ رقمی باشد → `CheckUid`، اگر ۱۶ رقمی باشد → `CheckSixteenCode`، در غیر این صورت → `CheckBarcode`.
2. پاسخ که آمد، نام/شرکت/GTIN/IRC/بچ/انقضا/قیمت در فرم پر می‌شود (بدون پاپ‌آپ و بدون تب جدید).
3. برای «تعداد در بسته» یک درخواست دوم با `NfiDetailIrc` زده می‌شود.
4. اگر `StatusCode=0` بود («اطلاعاتی پیدا نشد») هیچ رکوردی ساخته نمی‌شود و پیام روشن نمایش داده می‌شود.

---

## ۶) نتیجهٔ تست دسترسی (مهم)

با اجرای یک workflow در GitHub Actions (از IP خارج از ایران، سرور آمریکا) تست شد:

```
getent hosts irfdamobile.ttac.ir
10.19.62.200    irfdamobile.ttac.ir
curl: (28) Connection timed out after 30000 ms
```

یعنی دامنهٔ `irfdamobile.ttac.ir` به یک **IP داخلی (10.19.62.200)** resolve می‌شود و فقط از **داخل شبکهٔ ایران** قابل دسترسی است.
نتیجه:
- روی اینترنت ایران (بدون VPN)، اپ/مرورگر این آدرس را می‌بیند و درخواست انجام می‌شود.
- با فیلترشکن/VPN خارجی، این آدرس جواب نمی‌دهد (timeout).
- مسیرهای کمکی (پروکسی‌های عمومی خارج از ایران) هم برای همین دامنه فایده‌ای ندارند؛ فقط برای دامنه‌های عمومی مثل `irc.fda.gov.ir` کاربرد دارند.

فایل `.github/workflows/probe-ttac.yml` همان ابزار تست است (نتیجه را به‌صورت annotation روی check-run می‌گذارد).

---

## ۷) نتایج تست واقعی — ۲۴ اکتبر ۲۰۲۶ (مهم: چند تصحیح)

تست با مرورگر واقعی از **Europe/Berlin** انجام شد و اندپوینت‌ها **کار کردند**؛ پس نتیجهٔ قبلی («فقط از داخل ایران») درست نبود — فقط IPهای مرکز داده (مثل runnerهای GitHub Actions) بسته‌اند.

### الف) دسترسی و CORS

| موضوع | نتیجه |
|---|---|
| رسیدن به دامنه (no-cors) | ✅ ~۱۰۰–۹۸۰ms |
| خواندن پاسخ (cors، فقط هدرهای ساده) | ✅ کار می‌کند |
| هدر سفارشی (مثل `X-Test`) → preflight | ⛔ `Failed to fetch` (سرور `OPTIONS` را جواب نمی‌دهد) |

نتیجه: درخواست‌ها باید **فقط GET با هدرهای ساده** باشند (بدون کلید/هدر سفارشی). `Accept` مشکلی ندارد.

### ب) پارامترها

بدون `latitude/longitude/device/...` سرور **HTTP 404** می‌دهد؛ با مجموعهٔ کامل پارامترها کار می‌کند. پس همان پارامترهای اپ (شامل `VersionCode`/`AppVersion`) را همیشه بفرست.

### ج) `barcode` چه چیزی می‌خواهد؟ (مهم‌ترین یافته)

| ورودی | نتیجه |
|---|---|
| `barcode=6260152410148` (فقط GTIN) | ❌ HTTP 500 — `ErrorCode 1301` — «ساختار بارکد ارسالی نامعتبر است. پیشنهاد می کنیم برای دسترسی به اطلاعات کاتالوگ محصول کدUID آن را امتحان کنید» |
| `barcode=010626262040134421171980002061282275001727010010082` (کل رشتهٔ DataMatrix برچسب) | ✅ HTTP 200 + اطلاعات کامل محصول |

یعنی `CheckBarcode` **کل رشتهٔ اسکن‌شدهٔ برچسب (GS1)** را می‌خواهد، نه GTIN تنها. اگر از رشته، `AI(01)` و `AI(21)` را جدا کنیم به GTIN و UID می‌رسیم.

### د) نمونهٔ پاسخ واقعی

```json
{"Success":true,"Result":{
  "StatusCode":0,"StatusMessage":"","Barcode":"",
  "PersianName":"پلارژین® 120 م ل شربت","EnglishName":"PELARGINE® 120 ML SYRUP",
  "Irc":"9264016669304588","GTIN":"6262620401344",
  "UID":17198000206128227500.0,"UidString":"17198000206128227500",
  "Importer":"پارس گیتا دارو","Distributer":"پارس گیتا دارو","Manufacturer":"",
  "Price":null,"BatchCode":null,"Expiration":null,"Manufacturing":null,
  "LicenseCategory":86,"ImageUrls":[],"InquiryHistoryId":0,
  "ErrorCode":0,"ErrorMessage":"","NutritionalValue":null
},"ErrorCode":null,"Message":"","PageSize":0,"PageNumber":0,"Count":0}
```

نکته‌های ریز اما حیاتی:
- **`StatusCode: 0` یعنی «حکم اصالت نداد»، نه «پیدا نشد»** — دادهٔ محصول کامل برگشته است. نباید آن را «یافت نشد» تفسیر کرد.
- `UID` به‌صورت **double** می‌آید (`...500.0`) و دقتش کم است؛ باید از **`UidString`** استفاده شود.
- `Price`, `BatchCode`, `Expiration` در این مسیر معمولاً `null` هستند (بچ/انقضا جای دیگری است).

### ه) خطاها

خطاها با **HTTP 500** و بدنهٔ JSON می‌آیند؛ نباید دور انداخته شوند:

```json
{"Success":false,"Result":null,"ErrorCode":1301,"Message":"ساختار بارکد ارسالی نامعتبر است…"}
{"Success":false,"Result":null,"ErrorCode":1311,"Message":"خطا در برقراری ارتباط با سرویس دهنده!…"}
{"Success":false,"Result":null,"ErrorCode":-1,  "Message":"در حال حاضر خطایی رخ داده است…"}
```

| ErrorCode | معنی |
|---|---|
| 1301 | ساختار بارکد ارسالی نامعتبر است (GTIN تنها، یا رشتهٔ ناقص) |
| 1311 | خطا در ارتباط سرویس‌دهنده (موقت — دوباره تلاش کن) |
| -1 | خطای عمومی سمت سامانه |

### و) کارایی

- زمان پاسخ: **۷۰ms تا ۳٫۲ ثانیه** (اولین درخواست کندتر).
- در ۱۳ درخواست پشت‌سرهم/هم‌زمان **هیچ ۴۲۹ یا ۴۰۳** دیده نشد (یعنی در این حجم محدودیتی نبود؛ نه اینکه وجود ندارد).
- به همین دلیل **کش محلی** در برنامه لازم است: هر کد فقط یک بار استعلام می‌شود.

### ز) نتیجهٔ عملی برای برنامه

1. اسکن برچسب (DataMatrix) → کل رشته به `CheckBarcode` → نام/IRC/GTIN/UID/شرکت پر می‌شود.
2. اگر GTIN تنها بود → `1301` → یک بار با پیشوند `01` دوباره تلاش می‌شود.
3. اگر `StatusCode=0` بود و `UidString` داشت → همان UID به `CheckUid` می‌رود تا حکم اصالت (اصل/تقلبی/…) هم بیاید.
4. `NfiDetailIrc` برای تعداد در بسته و قیمت، و `NfiSearch` برای جست‌وجوی نامی.
