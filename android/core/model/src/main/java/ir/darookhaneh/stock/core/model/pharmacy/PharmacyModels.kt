package ir.darookhaneh.stock.core.model.pharmacy

/**
 * مدل‌های دامنهٔ داروخانه.
 * این ماژول هیچ وابستگی به Android/Room/شبکه ندارد تا قواعد موجودی مستقل تست شوند.
 */

data class Drug(
    val id: Long,
    val name: String,
    val genericName: String? = null,
    val strength: String? = null,
    val dosageForm: String? = null,
    /** بارکد تجاری (GTIN/EAN). اختیاری. */
    val gtin: String? = null,
    /** کد اصالت (IRC). اختیاری و غیر یکتا. */
    val irc: String? = null,
    val createdAt: Long = 0L,
    val updatedAt: Long = 0L,
)

data class Batch(
    val id: Long,
    val drugId: Long,
    val batchNumber: String? = null,
    val expiryDate: Long? = null,
    val quantity: Int = 0,
    val location: String? = null,
    val createdAt: Long = 0L,
    val updatedAt: Long = 0L,
)

data class InventoryEvent(
    val id: Long = 0,
    val batchId: Long,
    val type: InventoryEventType,
    /** تغییر خالص موجودی؛ برای COUNT می‌تواند مثبت یا منفی باشد. */
    val quantityDelta: Int,
    val note: String? = null,
    val createdAt: Long = 0L,
)

enum class InventoryEventType {
    /** ورود کالا. */
    RECEIVE,

    /** خروج/فروش. */
    DISPENSE,

    /** اصلاح دستی با دلیل. */
    ADJUSTMENT,

    /** انبارگردانی: مقدار شمارش‌شده ثبت می‌شود. */
    COUNT,
    ;

    companion object {
        /** تبدیل رشتهٔ ذخیره‌شده در دیتابیس؛ مقدار ناشناخته به ADJUSTMENT نگاشت می‌شود. */
        fun fromStorage(value: String): InventoryEventType =
            entries.firstOrNull { it.name == value } ?: ADJUSTMENT
    }
}

/** خلاصهٔ هر دارو برای فهرست و داشبورد. */
data class DrugSummary(
    val id: Long,
    val name: String,
    val genericName: String? = null,
    val strength: String? = null,
    val dosageForm: String? = null,
    val gtin: String? = null,
    val irc: String? = null,
    /** مجموع موجودی همهٔ بچ‌های این دارو. */
    val totalQuantity: Int = 0,
    val batchCount: Int = 0,
    /** نزدیک‌ترین تاریخ انقضا میان بچ‌ها. */
    val nearestExpiry: Long? = null,
    val isLowStock: Boolean = false,
)

/** بچ با اطلاعات دارو برای نمایش در داشبورد/هشدارها. */
data class BatchAlert(
    val batchId: Long,
    val drugId: Long,
    val drugName: String,
    val batchNumber: String?,
    val expiryDate: Long?,
    val quantity: Int,
    val daysToExpiry: Long?,
)

/** وضعیت داشبورد: از دادهٔ واقعی ساخته می‌شود، نه mock. */
data class DashboardSnapshot(
    val drugCount: Int = 0,
    val unitCount: Int = 0,
    val lowStockDrugs: List<DrugSummary> = emptyList(),
    val expiringSoon: List<BatchAlert> = emptyList(),
    val expired: List<BatchAlert> = emptyList(),
)
