package ir.darookhaneh.stock.feature.settings.domain.usecase

import ir.darookhaneh.stock.core.datastore.SettingsDataStore
import ir.darookhaneh.stock.core.datastore.model.AppearanceDataStore
import ir.darookhaneh.stock.core.datastore.model.AppearancePreferences
import ir.darookhaneh.stock.core.datastore.model.NotificationDataStore
import ir.darookhaneh.stock.core.datastore.model.NotificationPreferences

class UpdatePreferencesUseCase(
    private val settingsDataStore: SettingsDataStore,
    private val appearanceDataStore: AppearanceDataStore,
    private val notificationDataStore: NotificationDataStore
) {
    suspend fun updateAppearance(newValue: AppearancePreferences) {
        appearanceDataStore.setPreference(newValue)
    }

    suspend fun updateNotification(newValue: NotificationPreferences) {
        notificationDataStore.setPreference(newValue)
    }

    suspend fun updateBiometric(enabled: Boolean) {
        settingsDataStore.setBiometricLock(enabled)
    }
}