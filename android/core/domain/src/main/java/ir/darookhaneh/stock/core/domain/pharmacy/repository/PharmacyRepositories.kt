package ir.darookhaneh.stock.core.domain.pharmacy.repository

import ir.darookhaneh.stock.core.model.pharmacy.Batch
import ir.darookhaneh.stock.core.model.pharmacy.BatchAlert
import ir.darookhaneh.stock.core.model.pharmacy.Drug
import ir.darookhaneh.stock.core.model.pharmacy.DrugSummary
import ir.darookhaneh.stock.core.model.pharmacy.HistoryEntry
import ir.darookhaneh.stock.core.model.pharmacy.InventoryEvent
import ir.darookhaneh.stock.core.model.pharmacy.DrugLookupResult
import ir.darookhaneh.stock.core.model.pharmacy.InventoryEventType
import kotlinx.coroutines.flow.Flow

/**
 * قرارداد دارو.
 * هیچ‌یک از این توابع به شبکه وابسته نیست؛ جست‌وجوی بارکد کاملاً محلی است.
 */
interface DrugRepository {

    /** @return شناسهٔ داروی ساخته‌شده */
    suspend fun create(
        name: String,
        genericName: String? = null,
        strength: String? = null,
        dosageForm: String? = null,
        gtin: String? = null,
        irc: String? = null,
        packSize: Int? = null,
    ): Long

    suspend fun getById(drugId: Long): Drug?

    fun observeById(drugId: Long): Flow<Drug?>

    suspend fun findByGtin(gtin: String): Drug?

    suspend fun findByIrc(irc: String): Drug?

    fun observeSummaries(query: String? = null): Flow<List<DrugSummary>>

    fun observeDrugCount(): Flow<Int>

    fun observeTotalUnits(): Flow<Int>

    fun observeLowStockDrugCount(threshold: Int): Flow<Int>
}

interface BatchRepository {

    /** @return شناسهٔ بچ ساخته‌شده */
    suspend fun create(
        drugId: Long,
        batchNumber: String? = null,
        expiryDate: Long? = null,
        initialQuantity: Int = 0,
        location: String? = null,
    ): Long

    suspend fun getById(batchId: Long): Batch?

    fun observeByDrug(drugId: Long): Flow<List<Batch>>

    /** بچ‌هایی که تا [until] منقضی می‌شوند (شامل منقضی‌شده‌ها). */
    fun observeExpiringBefore(until: Long): Flow<List<BatchAlert>>

    fun observeExpiredBefore(now: Long): Flow<List<BatchAlert>>
}

/**
 * تنها مسیر مجاز تغییر موجودی.
 * پیاده‌سازی باید تغییر `quantity` و ثبت `InventoryEvent` را در یک تراکنش انجام دهد:
 * اگر یکی شکست بخورد، هیچ‌کدام نباید باقی بماند.
 */
interface InventoryRepository {

    /** @return شناسهٔ رخداد ثبت‌شده */
    suspend fun record(
        batchId: Long,
        type: InventoryEventType,
        amount: Int,
        note: String? = null,
    ): Long

    fun observeEvents(batchId: Long): Flow<List<InventoryEvent>>

    /** تاریخچهٔ سراسری همهٔ عملیات؛ `query` خالی یعنی همه. */
    fun observeHistory(query: String? = null, limit: Int = 500): Flow<List<HistoryEntry>>
}

/**
 * استعلام کد دارو از سامانهٔ تیتک.
 *
 * اختیاری و صریح: فقط با اقدام کاربر صدا زده می‌شود. پیاده‌سازی باید نتیجه را در
 * حافظهٔ محلی نگه دارد تا دفعهٔ بعد آفلاین هم کار کند.
 */
interface DrugLookupRepository {

    /** @throws ir.darookhaneh.stock.core.model.pharmacy.LookupException در صورت شکست */
    suspend fun lookup(code: String): DrugLookupResult

    /** فقط از حافظهٔ محلی؛ بدون شبکه. null یعنی قبلاً استعلام نشده. */
    suspend fun cached(code: String): DrugLookupResult?
}
