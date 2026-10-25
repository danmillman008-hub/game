package ir.darookhaneh.stock.core.model.pharmacy

/**
 * منبع زمان — به‌جای `System.currentTimeMillis()` مستقیم.
 * دلیل وجود: وابستگی به زمان باید تزریق شود تا هم تست‌پذیر باشد و هم
 * Koin بتواند آن را از گراف بگیرد (پارامتر پیش‌فرض سازنده در Koin حل نمی‌شود).
 */
fun interface TimeProvider {
    fun now(): Long
}

/** پیاده‌سازی تولیدی. */
val SystemTimeProvider = TimeProvider { System.currentTimeMillis() }

/** آستانه‌های نمایشی؛ قابل تغییر از تنظیمات در فازهای بعد. */
object PharmacyThresholds {
    /** موجودی کم برای مجموع بچ‌های فعال یک دارو، نه برای هر بچ. */
    const val DEFAULT_LOW_STOCK_THRESHOLD = 10

    /** «بچ نزدیک انقضا» بر حسب روز. */
    const val DEFAULT_EXPIRING_SOON_DAYS = 90L

    const val MILLIS_PER_DAY = 24L * 60 * 60 * 1000
}

/**
 * پیکربندی قابل تنظیم داروخانه.
 * جای پارامترهای پیش‌فرض سازنده را گرفت تا در DI صریح و قابل‌تغییر باشد.
 */
data class PharmacyConfig(
    val lowStockThreshold: Int = PharmacyThresholds.DEFAULT_LOW_STOCK_THRESHOLD,
    val expiringSoonDays: Long = PharmacyThresholds.DEFAULT_EXPIRING_SOON_DAYS,
)
