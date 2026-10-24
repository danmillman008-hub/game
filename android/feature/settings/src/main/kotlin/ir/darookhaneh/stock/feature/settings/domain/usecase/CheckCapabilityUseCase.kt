package ir.darookhaneh.stock.feature.settings.domain.usecase

import ir.darookhaneh.stock.core.data.AppCapabilityManager
import ir.darookhaneh.stock.core.datastore.DeviceCapableDataStore
import ir.darookhaneh.stock.feature.settings.domain.model.Capability
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.combine

class CheckCapabilityUseCase(
    private val deviceCapableDataStore: DeviceCapableDataStore,
    private val appCapabilityManager: AppCapabilityManager
) {
    suspend fun init() {
        deviceCapableDataStore.setDynamicColorSupported(appCapabilityManager.isDynamicColorSupported())
        deviceCapableDataStore.setNotificationGranted(appCapabilityManager.isNotificationGranted())
        deviceCapableDataStore.setBiometricSupported(appCapabilityManager.isBiometricSupported())
    }

    suspend fun updateNotification(granted: Boolean) {
        deviceCapableDataStore.setNotificationGranted(granted)
    }

    suspend fun updateBiometric(value: Boolean) {
        deviceCapableDataStore.setBiometricSupported(value)
    }

    fun observe(): Flow<Capability> {
        return combine(
            deviceCapableDataStore.dynamicColorSupported,
            deviceCapableDataStore.notificationGranted,
            deviceCapableDataStore.biometricSupported
        ) { dynamicColorSupported, notificationGranted, biometricSupported ->
            Capability(
                dynamicColorSupported = dynamicColorSupported,
                notificationGranted = notificationGranted,
                biometricSupported = biometricSupported
            )
        }
    }
}