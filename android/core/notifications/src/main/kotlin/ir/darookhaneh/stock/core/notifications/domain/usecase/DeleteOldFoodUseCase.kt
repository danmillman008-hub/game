package ir.darookhaneh.stock.core.notifications.domain.usecase

import ir.darookhaneh.stock.core.datastore.model.NotificationDataStore
import ir.darookhaneh.stock.core.domain.repository.FoodRepository
import ir.darookhaneh.stock.core.model.error_handling.Resource
import java.util.Calendar

class DeleteOldFoodUseCase(
    private val foodRepository: FoodRepository,
    private val notificationDataStore: NotificationDataStore
) {
    suspend operator fun invoke(): Resource<Unit> {
        val daysThreshold = notificationDataStore.getPreferences().deleteFoodThresholdDayInWeek

        if (daysThreshold <= 0) return Resource.Success(Unit)

        val calendar = Calendar.getInstance().apply {
            timeInMillis = System.currentTimeMillis()
            add(Calendar.DAY_OF_YEAR, -daysThreshold)
            set(Calendar.HOUR_OF_DAY, 0)
            set(Calendar.MINUTE, 0)
            set(Calendar.SECOND, 0)
            set(Calendar.MILLISECOND, 0)
        }

        val thresholdTimestamp = calendar.timeInMillis

        return foodRepository.deleteFoodAfterDay(thresholdTimestamp)
    }
}