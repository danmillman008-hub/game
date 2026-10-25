package ir.darookhaneh.stock.core.domain.pharmacy.usecase

import ir.darookhaneh.stock.core.domain.pharmacy.BatchRules
import ir.darookhaneh.stock.core.domain.pharmacy.DrugRules
import ir.darookhaneh.stock.core.domain.pharmacy.InventoryRules
import ir.darookhaneh.stock.core.domain.pharmacy.PharmacyError
import ir.darookhaneh.stock.core.domain.pharmacy.PharmacyException
import ir.darookhaneh.stock.core.domain.pharmacy.repository.BatchRepository
import ir.darookhaneh.stock.core.domain.pharmacy.repository.DrugRepository
import ir.darookhaneh.stock.core.domain.pharmacy.repository.InventoryRepository
import ir.darookhaneh.stock.core.model.pharmacy.Drug
import ir.darookhaneh.stock.core.model.pharmacy.InventoryEventType

/**
 * ثبت دارو + بچ + ورود اولیهٔ موجودی، یا فقط دارو.
 * برای جریان «ثبت دستی دارو» استفاده می‌شود و هیچ ورودی شبکه‌ای ندارد.
 */
class CreateDrugWithStockUseCase(
    private val drugRepository: DrugRepository,
    private val batchRepository: BatchRepository,
    private val inventoryRepository: InventoryRepository,
) {
    /**
     * @param initialQuantity اگر > 0 باشد، یک بچ ساخته و رخداد RECEIVE ثبت می‌شود.
     * @return شناسهٔ دارو
     */
    suspend operator fun invoke(
        name: String,
        genericName: String? = null,
        strength: String? = null,
        dosageForm: String? = null,
        gtin: String? = null,
        irc: String? = null,
        batchNumber: String? = null,
        expiryDate: Long? = null,
        initialQuantity: Int = 0,
        location: String? = null,
    ): Long {
        DrugRules.validateName(name)?.let { throw PharmacyException(it) }

        if (initialQuantity < 0) {
            throw PharmacyException(PharmacyError.NegativeQuantity)
        }

        val wantsBatch = !batchNumber.isNullOrBlank() || expiryDate != null || initialQuantity > 0
        if (wantsBatch) {
            BatchRules.validateIdentity(batchNumber, expiryDate)?.let { throw PharmacyException(it) }
        }

        val drugId = drugRepository.create(
            name = name.trim(),
            genericName = genericName?.trim()?.takeIf { it.isNotEmpty() },
            strength = strength?.trim()?.takeIf { it.isNotEmpty() },
            dosageForm = dosageForm?.trim()?.takeIf { it.isNotEmpty() },
            gtin = DrugRules.normalizeGtin(gtin),
            irc = DrugRules.normalizeIrc(irc),
        )

        if (wantsBatch) {
            val batchId = batchRepository.create(
                drugId = drugId,
                batchNumber = batchNumber?.trim()?.takeIf { it.isNotEmpty() },
                expiryDate = expiryDate,
                initialQuantity = 0,
                location = location?.trim()?.takeIf { it.isNotEmpty() },
            )
            if (initialQuantity > 0) {
                inventoryRepository.record(
                    batchId = batchId,
                    type = InventoryEventType.RECEIVE,
                    amount = initialQuantity,
                    note = "ورود اولیه هنگام ثبت دارو",
                )
            }
        }

        return drugId
    }
}

/** افزودن بچ جدید به داروی موجود. */
class AddBatchUseCase(
    private val drugRepository: DrugRepository,
    private val batchRepository: BatchRepository,
) {
    suspend operator fun invoke(
        drugId: Long,
        batchNumber: String? = null,
        expiryDate: Long? = null,
        location: String? = null,
    ): Long {
        drugRepository.getById(drugId) ?: throw PharmacyException(PharmacyError.DrugNotFound)
        BatchRules.validateIdentity(batchNumber, expiryDate)?.let { throw PharmacyException(it) }

        return batchRepository.create(
            drugId = drugId,
            batchNumber = batchNumber?.trim()?.takeIf { it.isNotEmpty() },
            expiryDate = expiryDate,
            location = location?.trim()?.takeIf { it.isNotEmpty() },
        )
    }
}

/**
 * ثبت رخداد موجودی. قاعده در دامنه تعیین می‌شود، اما اعمال نهایی اتمیک در لایهٔ داده است.
 */
class RecordInventoryEventUseCase(
    private val batchRepository: BatchRepository,
    private val inventoryRepository: InventoryRepository,
) {
    suspend operator fun invoke(
        batchId: Long,
        type: InventoryEventType,
        amount: Int,
        note: String? = null,
    ): Long {
        val batch = batchRepository.getById(batchId)
            ?: throw PharmacyException(PharmacyError.BatchNotFound)

        InventoryRules.quantityAfter(
            current = batch.quantity,
            type = type,
            amount = amount,
        ).getOrElse { throw it }

        return inventoryRepository.record(
            batchId = batchId,
            type = type,
            amount = amount,
            note = note?.trim()?.takeIf { it.isNotEmpty() },
        )
    }
}

/** یافتن دارو با کد اسکن‌شده — کاملاً محلی، بدون هیچ فراخوانی شبکه. */
class ResolveScannedCodeUseCase(
    private val drugRepository: DrugRepository,
) {
    suspend operator fun invoke(rawValue: String): Drug? {
        val code = rawValue.trim()
        if (code.isEmpty()) return null
        return drugRepository.findByGtin(code) ?: drugRepository.findByIrc(code)
    }
}

/** فهرست داروها با جست‌وجو. */
class ObserveDrugSummariesUseCase(
    private val drugRepository: DrugRepository,
) {
    operator fun invoke(query: String? = null) =
        drugRepository.observeSummaries(query?.trim()?.takeIf { it.isNotEmpty() })
}
