package ir.darookhaneh.stock.core.data.pharmacy

import ir.darookhaneh.stock.core.database.dao.DrugDao
import ir.darookhaneh.stock.core.database.entity.DrugEntity
import ir.darookhaneh.stock.core.model.pharmacy.PharmacyConfig
import ir.darookhaneh.stock.core.model.pharmacy.TimeProvider
import ir.darookhaneh.stock.core.domain.pharmacy.repository.DrugRepository
import ir.darookhaneh.stock.core.model.pharmacy.Drug
import ir.darookhaneh.stock.core.model.pharmacy.DrugSummary
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

/**
 * پیاده‌سازی دارو روی Room.
 * هیچ وابستگی شبکه‌ای ندارد: جست‌وجوی GTIN/IRC و فهرست، همه محلی‌اند.
 */
class DrugRepositoryImpl(
    private val drugDao: DrugDao,
    private val timeProvider: TimeProvider,
    private val config: PharmacyConfig,
) : DrugRepository {

    override suspend fun create(
        name: String,
        genericName: String?,
        strength: String?,
        dosageForm: String?,
        gtin: String?,
        irc: String?,
    ): Long {
        val now = timeProvider.now()
        return drugDao.insert(
            DrugEntity(
                name = name,
                genericName = genericName,
                strength = strength,
                dosageForm = dosageForm,
                gtin = gtin,
                irc = irc,
                createdAt = now,
                updatedAt = now,
            )
        )
    }

    override suspend fun getById(drugId: Long): Drug? =
        drugDao.getById(drugId)?.toDomain()

    override fun observeById(drugId: Long): Flow<Drug?> =
        drugDao.observeById(drugId).map { it?.toDomain() }

    override suspend fun findByGtin(gtin: String): Drug? =
        drugDao.findByGtin(gtin)?.toDomain()

    override suspend fun findByIrc(irc: String): Drug? =
        drugDao.findByIrc(irc)?.toDomain()

    override fun observeDrugCount(): Flow<Int> = drugDao.observeDrugCount()

    override fun observeTotalUnits(): Flow<Int> = drugDao.observeTotalUnits()

    override fun observeLowStockDrugCount(threshold: Int): Flow<Int> =
        drugDao.observeLowStockDrugCount(threshold)

    override fun observeSummaries(query: String?): Flow<List<DrugSummary>> {
        val threshold = config.lowStockThreshold
        val source = if (query.isNullOrBlank()) {
            drugDao.observeSummaries()
        } else {
            drugDao.observeSummariesFiltered(query)
        }
        return source.map { rows -> rows.map { it.toDomain(threshold) } }
    }
}
