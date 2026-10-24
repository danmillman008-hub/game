package ir.darookhaneh.stock.core.notifications.domain.usecase

import ir.darookhaneh.stock.core.datastore.model.NotificationDataStore

class GetNotificationPreferenceUseCase(
    private val notificationDataStore: NotificationDataStore
) {
    suspend operator fun invoke(): Boolean {
        return notificationDataStore.getPreferences().enableNotification
    }

    suspend fun getNotificationEnabled(): Boolean {
        return notificationDataStore.getPreferences().enableNotification
    }

    suspend fun getWeeklyReportEnabled(): Boolean {
        return notificationDataStore.getPreferences().enableWeeklyReport
    }
}