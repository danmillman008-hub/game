package ir.darookhaneh.stock.core.data.pharmacy

import android.database.sqlite.SQLiteConstraintException
import ir.darookhaneh.stock.core.database.dao.BatchDao
import ir.darookhaneh.stock.core.database.dao.InventoryEventDao
import ir.darookhaneh.stock.core.database.entity.BatchEntity
import ir.darookhaneh.stock.core.database.entity.InventoryEventEntity
import ir.darookhaneh.stock.core.database.TransactionRunner
import ir.darookhaneh.stock.core.domain.pharmacy.InventoryRules
import ir.darookhaneh.stock.core.domain.pharmacy.PharmacyError
import ir.darookhaneh.stock.core.domain.pharmacy.PharmacyException
import ir.darookhaneh.stock.core.domain.pharmacy.repository.BatchRepository
import ir.darookhaneh.stock.core.domain.pharmacy.repository.InventoryRepository
import ir.darookhaneh.stock.core.model.pharmacy.Batch
import ir.darookhaneh.stock.core.model.pharmacy.InventoryEvent
import ir.darookhaneh.stock.core.model.pharmacy.InventoryEventType
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

class BatchRepositoryImpl(
    private val batchDao: BatchDao,
    private val clock: () -> Long = System::currentTimeMillis,
) : BatchRepository {

    override suspend fun create(
        drugId: Long,
        batchNumber: String?,
        expiryDate: Long?,
        initialQuantity: Int,
        location: String?,
    ): Long {
        if (initialQuantity < 0) throw PharmacyException(PharmacyError.NegativeQuantity)

        // جلوگیری از بچ تکراری، علاوه بر قید یکتای دیتابیس.
        if (batchDao.findMatching(drugId, batchNumber, expiryDate) != null) {
            throw PharmacyException(PharmacyError.DuplicateBatch)
        }

        val now = clock()
        return try {
            batchDao.insert(
                BatchEntity(
                    drugId = drugId,
                    batchNumber = batchNumber,
                    expiryDate = expiryDate,
                    quantity = initialQuantity,
                    location = location,
                    createdAt = now,
                    updatedAt = now,
                )
            )
        } catch (e: SQLiteConstraintException) {
            throw PharmacyException(PharmacyError.DuplicateBatch)
        }
    }

    override suspend fun getById(batchId: Long): Batch? =
        batchDao.getById(batchId)?.toDomain()

    override fun observeByDrug(drugId: Long): Flow<List<Batch>> =
        batchDao.observeByDrug(drugId).map { list -> list.map { it.toDomain() } }
}

/**
 * ثبت رخداد موجودی به‌صورت **اتمیک**:
 * 1) بچ خوانده می‌شود، 2) مقدار جدید با قواعد دامنه محاسبه می‌شود،
 * 3) UPDATE شرطی اجرا می‌شود (پایین‌ترین لایه هم اجازهٔ منفی‌شدن نمی‌دهد)،
 * 4) رخداد ثبت می‌شود — همه در یک تراکنش؛ هر خطا کل تراکنش را rollback می‌کند.
 */
class InventoryRepositoryImpl(
    private val batchDao: BatchDao,
    private val inventoryEventDao: InventoryEventDao,
    private val transactionRunner: TransactionRunner,
    private val clock: () -> Long = System::currentTimeMillis,
) : InventoryRepository {

    override suspend fun record(
        batchId: Long,
        type: InventoryEventType,
        amount: Int,
        note: String?,
    ): Long = transactionRunner.runWithResult {
        val batch = batchDao.getById(batchId)
            ?: throw PharmacyException(PharmacyError.BatchNotFound)

        val nextQuantity = InventoryRules.quantityAfter(
            current = batch.quantity,
            type = type,
            amount = amount,
        ).getOrElse { throw it }

        val delta = InventoryRules.delta(batch.quantity, nextQuantity)
        if (delta == 0) {
            throw PharmacyException(PharmacyError.InvalidAmount)
        }

        val updated = batchDao.applyDelta(batchId = batchId, delta = delta, now = clock())
        if (updated != 1) {
            // ممنوعیت موجودی منفی در سطح SQL: هیچ تغییری اعمال نشد.
            throw PharmacyException(
                if (delta < 0) PharmacyError.InsufficientStock else PharmacyError.StorageFailure
            )
        }

        inventoryEventDao.insert(
            InventoryEventEntity(
                batchId = batchId,
                type = type.toStorage(),
                quantityDelta = delta,
                note = note,
                createdAt = clock(),
            )
        )
    }

    override fun observeEvents(batchId: Long): Flow<List<InventoryEvent>> =
        inventoryEventDao.observeByBatch(batchId).map { list -> list.map { it.toDomain() } }
}
