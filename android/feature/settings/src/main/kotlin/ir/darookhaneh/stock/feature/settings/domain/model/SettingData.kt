package ir.darookhaneh.stock.feature.settings.domain.model

import ir.darookhaneh.stock.core.datastore.model.AppearancePreferences
import ir.darookhaneh.stock.core.datastore.model.GeneralPreferences
import ir.darookhaneh.stock.core.datastore.model.NotificationPreferences

data class SettingDataPreferences(
    val enableBiometric: Boolean = false,
    val appearancePreferences: AppearancePreferences = AppearancePreferences(),
    val generalPreferences: GeneralPreferences = GeneralPreferences(),
    val notificationPreferences: NotificationPreferences = NotificationPreferences()
)
