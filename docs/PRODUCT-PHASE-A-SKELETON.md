# فاز A — اسکلت محصول (پاک‌سازی کامل + مدل دادهٔ دارویی)

تاریخ: ۲۵ اکتبر ۲۰۲۶ · برنچ: `arena/dd2b6beb-game` · وضعیت بیلد: **سبز** (workflow `product-build`)

> نکته: شما «حذف در یک برنچ جدا» را خواسته بودید. در این محیط، برنچ نشست
> (`arena/dd2b6beb-game`) قابل تغییر یا ساخت برنچ جدید نیست. بنابراین حذف به‌صورت
> **یک سری کامیت مستقل و پیوسته** انجام شد و در انتهای کار، بیلد و تست واحد
> **سبز** است — همان تضمینی که از برنچ جدا انتظار داشتید. اگر لازم شد، بازگردانی
> فقط با `git revert` همان کامیت‌ها یک‌مرحله‌ای است.

## ۱) چه چیزی حذف شد (کامل، نه موقت)

| مورد | وضعیت |
|---|---|
| `feature:food-entry` | حذف کامل |
| `feature:inventory` (فهرست/جست‌وجو/جزئیات غذا) | حذف کامل |
| `feature:scanner` (اسکنر غذا + OCR تاریخ) | حذف کامل |
| `feature:analytics` (ضایعات/تازگی/آمار غذایی) | حذف کامل |
| ویجت‌های Glance (`total_food`, `weekly_expiry`) + receiverها + وابستگی Glance | حذف کامل |
| `core:model/food` (`FoodItem`, `FoodCategory`, `StorageStatus`, `ItemUnit`, …) | حذف کامل |
| `core:database` (جدول‌های غذا/دسته/جست‌وجو/FTS + DAOها + مایگریشن‌های ۱۲→۱۵) | حذف کامل، اسکیما از صفر |
| `core:domain` (FoodRepository/CategoryRepository + use caseهای غذا) | حذف کامل |
| `core:data` (FoodRepositoryImpl, CategoryRepositoryImpl, mapperها) | حذف کامل |
| `core:network` (`FoodApi`, `FoodRemoteDataSource`, مدل پاسخ غذا) | حذف کامل |
| `core:notifications` (workerهای انقضای غذا، notifier غذا، receiver اکشن غذا) | حذف؛ کانال‌ها و زیرساخت WorkManager/Koin مانده |
| `feature:settings` — بخش‌های «اعلان‌های غذا» و «داده‌های من» (export/import غذا) | حذف؛ بازسازی روی مدل دارو در فاز بعد |

## ۲) چه چیزی نگه داشته شد (زیرساخت)

- DI (Koin) و ماژول‌بندی، `MainActivity`، ناوبری Navigation3، ترنزیشن‌ها.
- Design system، تم/رنگ، RTL، **فونت وزیرمتن** (اکنون فونت پیش‌فرض تایپوگرافی).
- دوربین/CameraX و مسیر **ML Kit bundled** (بدون Play Services) طبق نتیجهٔ تست GMS-free.
- کانال‌های اعلان، WorkManager + `KoinWorkerFactory`.
- تنظیمات عمومی: ظاهر (تم/رنگ/زبان)، بیومتریک، دربارهٔ برنامه، بررسی نسخه، متن‌های open-source.
- CI: `product-build` (assembleDebug + unit tests، با انتشار خطاها در Issue).

## ۳) مدل دادهٔ نسخهٔ ۱ (Room، schema = 1)

```
drug(id, name, genericName?, strength?, dosageForm?, gtin?, irc?, createdAt, updatedAt)
batch(id, drugId→drug.id CASCADE, batchNumber?, expiryDate?, quantity, location?, createdAt, updatedAt)
inventory_event(id, batchId→batch.id CASCADE, type, quantityDelta, note?, createdAt)
```

- ایندکس‌ها: `gtin`, `irc`, `name`, `genericName`؛ روی بچ: `drugId`, `expiryDate` و
  **یکتایی `(drugId, batchNumber, expiryDate)`**؛ روی رخداد: `batchId`, `createdAt`.
- `irc` **اختیاری، غیر UNIQUE**؛ ساخت دارو هیچ وابستگی شبکه‌ای ندارد.
- تغییر موجودی به‌صورت **اتمیک و شرطی** است:
  `UPDATE batch SET quantity = quantity + :delta WHERE id = :id AND quantity + :delta >= 0`
  → موجودی منفی در سطح SQLite هم غیرممکن می‌شود (نه فقط در UI).
- هر تغییر موجودی یک ردیف `inventory_event` می‌نویسد؛ حذف بچ/دارو آبشاری است.

## ۴) ناوبری فعلی

`داشبورد` · `داروها` · `اسکن` · `تنظیمات` — هر چهار مسیر با صفحهٔ موقت
(`PlaceholderScreen`) وصل شده‌اند تا اپ اجرا شود؛ صفحه‌های واقعی با دادهٔ Room
در گام بعد جای آن‌ها می‌نشیند. نوار پایین روی صفحهٔ اسکن پنهان می‌شود.

## ۵) تصمیم‌های ثبت‌شده

1. **پاک‌کردن اسکیما، نه مهاجرت** — محصول منتشر نشده و داده‌ی مشتری وجود ندارد؛
   `fallbackToDestructiveMigration(dropAllTables = true)` تنها در نسخهٔ ۱ مجاز است.
   از این پس هر تغییر اسکیما نسخه +۱ و Migration واقعی + تست مهاجرت لازم دارد.
2. **حذف کامل، نه انبار کردن کد** — برای پرهیز از «دو مدل ذهنی» (غذا و دارو).
3. زبان پیش‌فرض محصول **فارسی** است؛ رشته‌های انگلیسی فعلی به‌تدریج با
   `values-fa/string.xml` جایگزین می‌شوند (کلیدهای ناوبری و نام برنامه انجام شد).

## ۶) گام بعدی (فاز B و C)

- لایهٔ دامنه/داده: `DrugRepository`, `BatchRepository`, `InventoryRepository` + use caseها.
- شش تست هستهٔ الزامی: مقدار منفی، RECEIVE، DISPENSE/ADJUSTMENT، داروی بدون IRC،
  اسکن ناشناخته بدون شبکه، ثبت event هنگام حذف/اصلاح بچ.
- چهار صفحهٔ واقعی: داشبورد، فهرست داروها، اسکن/ثبت، جزئیات دارو و بچ.
