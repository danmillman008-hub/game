# فاز B — لایهٔ دامنه، شش تست هسته، و اولین قابلیت کامل end-to-end

تاریخ: ۲۵ اکتبر ۲۰۲۶ · برنچ: `arena/dd2b6beb-game`
آخرین بیلد: **سبز** — `product-build` run `40176154792`

## نتیجهٔ تست‌ها (منتشرشده در Issue «product-build status»)

```
ir.darookhaneh.stock.core.domain.pharmacy.PharmacyRulesTest        14 تست  OK
ir.darookhaneh.stock.core.data.pharmacy.PharmacyCoreTest           12 تست  OK
ir.darookhaneh.stock.ExampleUnitTest                                1 تست  OK
مجموع: 27 تست، 0 شکست
```

`PharmacyCoreTest` روی **Room واقعی (in-memory)** اجرا می‌شود (Robolectric)، نه mock؛
پس همان SQL و همان تراکنشی تست می‌شود که در اپ اجرا می‌شود.

## شش gate مورد توافق — کجا و چگونه

| # | gate | تست |
|---|---|---|
| ۱ | ثبت دارو بدون IRC و بدون اینترنت | `۱ دارو بدون IRC و بدون شبکه ثبت می‌شود` |
| ۲ | ایجاد بچ + رد `(drugId, batchNumber, expiryDate)` تکراری | `۲ بچ ساخته می‌شود و ترکیب تکراری رد می‌شود` + `بچ بی‌نام و بی‌تاریخ انقضا ساخته نمی‌شود` |
| ۳ | `RECEIVE` موجودی را زیاد و رخداد ثبت می‌کند | `۳ رویداد RECEIVE …` |
| ۴ | `DISPENSE` موجودی را کم و رخداد ثبت می‌کند | `۴ رویداد DISPENSE …` + `ADJUSTMENT …` |
| ۵ | موجودی منفی: نه `quantity` نه `event` تغییر نمی‌کند | `۵ خروج بیش از موجودی …` + `۵ اصلاح منفی …` |
| ۶ | کد ناشناخته: هیچ درخواست شبکه‌ای، مسیر ثبت دستی | `۶ کد ناشناخته …` + `جست‌وجوی کد با GTIN موجود، محلی …` |

## دو اصلاح شما که اعمال شد

1. **بچ بی‌نام/بی‌تاریخ** — در SQLite مقدار `NULL` در قید یکتایی تکرارپذیر است؛ بنابراین
   قاعده در **لایهٔ دامنه** enforce شد:
   `BatchRules.validateIdentity()` → «حداقل یکی از شمارهٔ بچ یا تاریخ انقضا».
   `batchNumber` و `expiryDate` هر دو nullable می‌مانند، اما ترکیب `(null, null)` رد می‌شود.
2. **اتمیک بودن تغییر موجودی** — `InventoryRepositoryImpl.record()` تمام کار را در یک
   تراکنش Room انجام می‌دهد:
   ```
   withTransaction {
       batch = dao.getById(batchId) ?: throw BatchNotFound
       next  = InventoryRules.quantityAfter(batch.quantity, type, amount)   // دامنه
       updated = dao.applyDelta(batchId, next - batch.quantity, now)        // WHERE quantity + delta >= 0
       if (updated != 1) throw InsufficientStock                            // rollback
       eventDao.insert(event)                                               // همین تراکنش
   }
   ```
   اگر event شکست بخورد کل تراکنش rollback می‌شود؛ اگر UPDATE صفر ردیف برگرداند، هیچ
   eventی ثبت نمی‌شود. پوشش تست: `۵ خروج بیش از موجودی …` (هم `quantity` و هم تعداد
   رخدادها قبل/بعد مقایسه می‌شوند).

## آستانه‌ها (طبق تصمیم شما)

- موجودی کم = **مجموع موجودی همهٔ بچ‌های یک دارو ≤ ۱۰** (نه هر بچ) — `PharmacyThresholds.DEFAULT_LOW_STOCK_THRESHOLD`.
- بچ نزدیک انقضا = **۹۰ روز** پیش‌فرض — `DEFAULT_EXPIRING_SOON_DAYS`.
- هر دو در `ObserveDashboardUseCase` پارامتر تزریقی‌اند تا بعداً از تنظیمات بیایند
  (صفحهٔ تنظیم آستانه هنوز ساخته نشده — در فاز H).
- `lowStockThreshold` روی خود `Drug` **اضافه نشده** (طبق خواستهٔ شما برای نسخهٔ بعد).

## معماری تحویل‌شده

```
core:model      Drug / Batch / InventoryEvent / DrugSummary / BatchAlert / DashboardSnapshot
core:domain     DrugRules · BatchRules · InventoryRules · PharmacyThresholds
                repository contracts (Drug/Batch/Inventory) + use caseها
core:database   drug · batch · inventory_event + DAOها + TransactionRunner.runWithResult
core:data       *RepositoryImpl (Room) + mapperها   ← هیچ وابستگی شبکه
feature:pharmacy  Dashboard · DrugList(search) · AddDrug · DrugDetail · Scanner
```

جریان‌های کامل‌شده:

- **A/B** قواعد + شش تست (بالا)
- **C** «افزودن دستی دارو»: نام اجباری، بقیه اختیاری؛ اگر تعداد یا بچ وارد شود،
  بچ ساخته و `RECEIVE` ثبت می‌شود (همه از `CreateDrugWithStockUseCase`).
- **D** فهرست داروها با جست‌وجوی محلی (نام/ژنریک/GTIN/IRC) + نمایش موجودی کل.
- **E** جزئیات دارو: بچ‌ها، افزودن بچ، و چهار عملیات ورود/خروج/اصلاح/شمارش + تاریخچهٔ رخدادها.
- **F** اسکن: CameraX + **ML Kit bundled**؛ `ResolveScannedCodeUseCase` فقط Room را
  می‌بیند؛ کد شناخته‌شده → جزئیات دارو، کد ناشناخته → `AddDrug(gtin=…)` با فرم پیش‌پر.
- **G** داشبورد: شمارنده‌ها + لیست منقضی/نزدیک‌انقضا/کمبود، همه از دادهٔ واقعی.

## آنچه هنوز نیست (فاز بعد)

1. **H**: Workerهای هشدار انقضا روی `batch` (زیرساخت WorkManager هست، Workerها هنوز نه)
   و صفحهٔ تنظیم آستانه‌ها.
2. تست UI/instrumentation برای صفحه‌ها (اسکن واقعی با دوربین روی دستگاه).
3. `irc` در UI فقط ورودی دستی است؛ اتصال به سرویس‌های IRC (اختیاری، آفلاین‌محور) بعداً.
