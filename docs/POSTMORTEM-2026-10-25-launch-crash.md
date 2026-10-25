# رفع باگ: «اپ بعد از نصب باز نمی‌شود» — ۲۵ اکتبر ۲۰۲۶

## نشانه

کاربر نسخهٔ `stock-arm64-release-*.apk` را نصب کرد و اپ با crash بسته شد
(«the app keeps stopping»).

## علت ریشه‌ای

`Koin` پارامترهای **پیش‌فرض سازنده** را تزریق نمی‌کند. کد ما این‌طور بود:

```kotlin
class DrugRepositoryImpl(
    private val drugDao: DrugDao,
    private val clock: () -> Long = System::currentTimeMillis,   // ← این
) : DrugRepository
```

و در گراف:

```kotlin
singleOf(::DrugRepositoryImpl) { bind<DrugRepository>() }
```

Koin برای پارامتر `clock` دنبال تعریفی از نوع `kotlin.Function0<kotlin.Long>`
می‌گشت که وجود ندارد → `NoDefinitionFoundException`.

چون صفحهٔ شروع، **داشبورد** است و `DashboardViewModel` برای اولین قالب‌بندی به
`ObserveDashboardUseCase → DrugRepository` نیاز دارد، خطا **همان لحظهٔ باز شدن اپ**
رخ می‌داد: اسپلش نمایش داده می‌شد و بلافاصله کرش. همین الگو در سه کلاس دیگر هم بود:

- `BatchRepositoryImpl(batchDao, clock = …)`
- `InventoryRepositoryImpl(batchDao, eventDao, txRunner, clock = …)`
- `ObserveDashboardUseCase(drugRepo, batchRepo, clock = …, lowStockThreshold = 10, expiringSoonDays = 90)`

## اصلاح

جای پارامترهای پیش‌فرض، چیزهای واقعی به گراف اضافه شدند:

```kotlin
// core:model
fun interface TimeProvider { fun now(): Long }
val SystemTimeProvider = TimeProvider { System.currentTimeMillis() }
data class PharmacyConfig(
    val lowStockThreshold: Int = 10,
    val expiringSoonDays: Long = 90,
)

// DI
single<TimeProvider> { SystemTimeProvider }
single { PharmacyConfig() }
singleOf(::DrugRepositoryImpl) { bind<DrugRepository>() }
```

مزیت جانبی: زمان و آستانه‌ها حالا **تزریق‌پذیر** هستند — تست‌ها زمان ثابت می‌دهند و
در فاز H همین `PharmacyConfig` از تنظیمات کاربر پر می‌شود (بدون دست‌زدن به سازنده‌ها).

## چرا تست‌ها نگرفته بودند؟

تست‌های واحد و لایهٔ داده گراف Koin را نمی‌ساختند؛ آن‌ها کلاس‌ها را دستی
(with پارامترهای پیش‌فرض) می‌ساختند. باگ فقط در **ترکیب واقعی DI + UI** ظاهر می‌شد.

## دو گیت جدید (تا تکرار نشود)

1. **`KoinGraphTest`** (`app/src/test`) — گراف کامل Koin را با Robolectric می‌سازد و
   `AppViewModel` + همهٔ ViewModelهای صفحه‌ها را resolve می‌کند. هر پارامتر
   غیرقابل‌تأمین در آینده این تست را قرمز می‌کند. (۴ تست)
2. **workflow `app-smoke`** — روی امولاتور AOSP واقعی: نصب APK، `am start`,
   بررسی اینکه پروسه زنده مانده، و انتشار crash buffer + اسکرین‌شات در Issue.

## نتیجهٔ تأیید

| گیت | نتیجه |
|---|---|
| `product-build` (run `40184073015`) | ✅ **۳۱ تست، ۰ شکست** (شامل ۴ تست گراف Koin) |
| `app-smoke` (run `40184068809`، Issue #44) | ✅ `VERDICT_release=APP_RUNNING` · `VERDICT_debug=APP_RUNNING` |

لاگ دستگاه در همان Issue نشان می‌دهد Koin اکنون `TimeProvider` و `PharmacyConfig` را
resolve می‌کند و `DashboardViewModel` بدون خطا ساخته می‌شود؛ سپس
`Displayed ir.darookhaneh.stock/.MainActivity: +1s589ms`.

## درس‌ها

- در Koin هر پارامتر سازنده باید در گراف باشد؛ **هیچ‌وقت** روی مقدار پیش‌فرض حساب نکن.
- بیلد سبز + تست واحد سبز به‌معنای «اپ باز می‌شود» نیست؛ باید یک تست **باز شدن اپ**
  وجود داشته باشد.
- از این پس هر تغییر در DI فقط با `KoinGraphTest` سبز merge می‌شود.
