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
    /** تعداد واحد در هر بسته (قرص در جعبه، عدد در کارتن…). برای تبدیل کارتن/بسته به واحد. */
    val packSize: Int? = null,
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

    /** انبارگردانی: مقدار شمارش‌شده جای موجودی را می‌گیرد (جای‌گذاری، نه جمع). */
    COUNT,

    /** ضایعات: داروی دورریز/شکسته/منقضی که از انبار خارج می‌شود. مثل خروج، اما با دلیل. */
    DAMAGE,

    /** مرجوعی: برگشت از مراجع (بیمار/داروخانهٔ دیگر). مثل ورود، اما با دلیل. */
    RETURN,
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
    /** تعداد واحد در هر بسته؛ null یعنی نامشخص. */
    val packSize: Int? = null,
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

/**
 * روش شمارش — همان سه حالتی که در نسخهٔ HTML وجود داشت.
 * ورودی کاربر همیشه به **واحد** تبدیل می‌شود تا موجودی یک عدد واحد داشته باشد.
 */
enum class CountingMode {
    /** تکی: تعداد بسته/عدد. */
    SINGLE,

    /** کارتن × تعداد در کارتن + بستهٔ خارج از کارتن. */
    CARTON,

    /** باز/نیمه‌مصرف: تعداد بستهٔ سالم + واحد باقی‌مانده در بسته‌های باز. */
    OPEN,
}

/**
 * ورودی خام شمارش.
 *
 * @param packs تعداد بسته (یا عدد در حالت تکی)
 * @param cartons تعداد کارتن (حالت CARTON)
 * @param unitsPerCarton تعداد بسته در هر کارتن؛ اگر صفر باشد از `packSize` دارو/کارتنِ ذخیره‌شده استفاده می‌شود
 * @param loosePacks بسته‌های خارج از کارتن (حالت CARTON)
 * @param openUnits واحدهای باقی‌مانده در بسته‌های باز (حالت OPEN)
 */
data class QuantityInput(
    val mode: CountingMode = CountingMode.SINGLE,
    val packs: Int = 0,
    val cartons: Int = 0,
    val unitsPerCarton: Int = 0,
    val loosePacks: Int = 0,
    val openUnits: Int = 0,
) {
    /**
     * تبدیل به واحد.
     * قاعده‌ها (هم‌ارز نسخهٔ HTML):
     * - SINGLE: packs + openUnits
     * - CARTON: cartons * per + loosePacks، سپس + openUnits
     * - OPEN: packs + openUnits
     */
    fun toUnits(packSize: Int? = null): Int {
        val per = if (unitsPerCarton > 0) unitsPerCarton else (packSize ?: 1)
        val base = when (mode) {
            CountingMode.SINGLE -> packs
            CountingMode.CARTON -> cartons * per + loosePacks
            CountingMode.OPEN -> packs
        }
        return (base + openUnits).coerceAtLeast(0)
    }

    /** توضیح خوانا برای ثبت در تاریخچه؛ null یعنی توضیح لازم نیست. */
    fun describe(): String? = when (mode) {
        CountingMode.SINGLE -> null
        CountingMode.CARTON ->
            "$cartons کارتن × ${if (unitsPerCarton > 0) unitsPerCarton else "?"}" +
                if (loosePacks > 0) " + $loosePacks بسته" else ""

        CountingMode.OPEN -> "باز/نیمه‌مصرف"
    }

    val isEmpty: Boolean
        get() = packs == 0 && cartons == 0 && loosePacks == 0 && openUnits == 0
}

/** یک ردیف تاریخچهٔ سراسری برای نمایش در صفحهٔ «تاریخچه». */
data class HistoryEntry(
    val eventId: Long,
    val batchId: Long,
    val drugId: Long,
    val drugName: String,
    val batchNumber: String?,
    val expiryDate: Long?,
    val type: InventoryEventType,
    val quantityDelta: Int,
    val note: String?,
    val createdAt: Long,
    val batchQuantity: Int,
    /** تغییر معادل بسته — برای نمایش «چند جعبه کم/زیاد شد». */
    val packSize: Int? = null,
) {
    val packEquivalent: Double?
        get() = packSize?.takeIf { it > 0 }?.let { quantityDelta.toDouble() / it }
}
