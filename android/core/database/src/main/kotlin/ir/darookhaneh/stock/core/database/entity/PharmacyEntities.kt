package ir.darookhaneh.stock.core.database.entity

import androidx.room.Entity
import androidx.room.ForeignKey
import androidx.room.Index
import androidx.room.PrimaryKey

/**
 * قلم دارو.
 *
 * قواعد ثابت (docs/PHASE-1-DATA-MODEL.md):
 * - `gtin` (بارکد تجاری) و `irc` (کد اصالت) هر دو اختیاری‌اند.
 * - `irc` هرگز UNIQUE نیست و ساخت دارو به اینترنت وابسته نیست.
 * - موجودی و یکتایی داخلی بر پایه `drugId` و بچ است، نه IRC.
 */
@Entity(
    tableName = "drug",
    indices = [
        Index("gtin"),
        Index("irc"),
        Index("name"),
        Index("genericName"),
    ],
)
data class DrugEntity(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val name: String,
    val genericName: String? = null,
    val strength: String? = null,
    val dosageForm: String? = null,
    val gtin: String? = null,
    val irc: String? = null,
    val createdAt: Long,
    val updatedAt: Long,
)

/**
 * بچ فیزیکی یک دارو.
 *
 * یکتایی منطقی: (drugId, batchNumber, expiryDate).
 * `quantity` هرگز منفی نمی‌شود؛ این قاعده در لایه دامنه و در DAO اعمال می‌شود.
 */
@Entity(
    tableName = "batch",
    foreignKeys = [
        ForeignKey(
            entity = DrugEntity::class,
            parentColumns = ["id"],
            childColumns = ["drugId"],
            onDelete = ForeignKey.CASCADE,
        ),
    ],
    indices = [
        Index("drugId"),
        Index("expiryDate"),
        Index(value = ["drugId", "batchNumber", "expiryDate"], unique = true),
    ],
)
data class BatchEntity(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val drugId: Long,
    val batchNumber: String? = null,
    val expiryDate: Long? = null,
    val quantity: Int = 0,
    val location: String? = null,
    val createdAt: Long,
    val updatedAt: Long,
)

/**
 * دفتر رخدادهای موجودی؛ تنها منبع حسابرسی تغییرات `quantity`.
 * `type` یکی از مقادیر [InventoryEventType] است.
 */
@Entity(
    tableName = "inventory_event",
    foreignKeys = [
        ForeignKey(
            entity = BatchEntity::class,
            parentColumns = ["id"],
            childColumns = ["batchId"],
            onDelete = ForeignKey.CASCADE,
        ),
    ],
    indices = [
        Index("batchId"),
        Index("createdAt"),
    ],
)
data class InventoryEventEntity(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val batchId: Long,
    val type: String,
    val quantityDelta: Int,
    val note: String? = null,
    val createdAt: Long,
)

enum class InventoryEventType {
    /** ورود کالا: مقدار بچ را افزایش می‌دهد. */
    RECEIVE,

    /** خروج/فروش: مقدار بچ را کاهش می‌دهد. */
    DISPENSE,

    /** اصلاح دستی با دلیل. */
    ADJUSTMENT,

    /** انبارگردانی: ثبت مقدار شمارش‌شده. */
    COUNT,
    ;

    companion object {
        fun fromStorage(value: String): InventoryEventType =
            entries.firstOrNull { it.name == value } ?: ADJUSTMENT
    }
}

/** یک ردیف خلاصه برای فهرست داروها. */
data class DrugSummaryRow(
    val id: Long,
    val name: String,
    val genericName: String?,
    val strength: String?,
    val dosageForm: String?,
    val gtin: String?,
    val irc: String?,
    val totalQuantity: Int,
    val batchCount: Int,
    val nearestExpiry: Long?,
)

/** یک ردیف خلاصه برای داشبورد. */
data class DashboardCounters(
    val drugCount: Int,
    val unitCount: Int,
    val expiredBatchCount: Int,
    val expiringSoonBatchCount: Int,
    val lowStockBatchCount: Int,
)
