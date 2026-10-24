package ir.darookhaneh.stock.feature.settings.domain.usecase

import ir.darookhaneh.stock.core.datastore.SettingsDataStore
import ir.darookhaneh.stock.core.datastore.model.AppearanceDataStore
import ir.darookhaneh.stock.core.datastore.model.NotificationDataStore
import ir.darookhaneh.stock.feature.settings.domain.model.SettingDataPreferences
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.combine

class ObserveSettingStateUseCase(
    private val settingsDataStore: SettingsDataStore,
    private val notificationDataStore: NotificationDataStore,
    private val appearanceDataStore: AppearanceDataStore,
) {
    fun observe(): Flow<SettingDataPreferences> {
        return combine(
            settingsDataStore.biometricLockFlow,
            notificationDataStore.preferencesFlow,
            appearanceDataStore.preferencesFlow,
        ) { enableBiometric, notification, appearance ->
            SettingDataPreferences(
                enableBiometric = enableBiometric,
                notificationPreferences = notification,
                appearancePreferences = appearance
            )
        }
    }
}