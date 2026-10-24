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
