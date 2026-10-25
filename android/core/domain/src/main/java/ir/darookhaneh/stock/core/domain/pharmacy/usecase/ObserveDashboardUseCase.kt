package ir.darookhaneh.stock.core.domain.pharmacy.usecase

import ir.darookhaneh.stock.core.domain.pharmacy.repository.BatchRepository
import ir.darookhaneh.stock.core.domain.pharmacy.repository.DrugRepository
import ir.darookhaneh.stock.core.model.pharmacy.DashboardSnapshot
import ir.darookhaneh.stock.core.model.pharmacy.PharmacyConfig
import ir.darookhaneh.stock.core.model.pharmacy.PharmacyThresholds
import ir.darookhaneh.stock.core.model.pharmacy.TimeProvider
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.combine

/**
 * داشبورد واقعی از دادهٔ Room:
 * - موجودی کم = مجموع موجودی همهٔ بچ‌های یک دارو ≤ آستانه (پیش‌فرض ۱۰)
 * - بچ نزدیک انقضا = تا ۹۰ روز آینده
 * - منقضی‌شده = تاریخ انقضا گذشته
 */
class ObserveDashboardUseCase(
    private val drugRepository: DrugRepository,
    private val batchRepository: BatchRepository,
    private val timeProvider: TimeProvider,
    private val config: PharmacyConfig,
) {
    operator fun invoke(): Flow<DashboardSnapshot> {
        val now = timeProvider.now()
        val until = now + config.expiringSoonDays * PharmacyThresholds.MILLIS_PER_DAY

        return combine(
            drugRepository.observeDrugCount(),
            drugRepository.observeTotalUnits(),
            drugRepository.observeSummaries(),
            batchRepository.observeExpiringBefore(until),
            batchRepository.observeExpiredBefore(now),
        ) { drugCount, unitCount, summaries, expiring, expired ->
            DashboardSnapshot(
                drugCount = drugCount,
                unitCount = unitCount,
                lowStockDrugs = summaries.filter { it.isLowStock },
                // بچ‌هایی که واقعاً منقضی نشده‌اند فقط در «نزدیک انقضا» می‌آیند.
                expiringSoon = expiring.filter { (it.expiryDate ?: Long.MAX_VALUE) >= now },
                expired = expired,
            )
        }
    }
}
