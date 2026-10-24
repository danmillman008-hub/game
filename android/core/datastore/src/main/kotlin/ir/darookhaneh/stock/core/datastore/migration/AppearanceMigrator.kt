package ir.darookhaneh.stock.core.datastore.migration

import androidx.datastore.core.DataStore
import androidx.datastore.preferences.core.Preferences
import androidx.datastore.preferences.core.edit
import ir.darookhaneh.stock.core.datastore.UserPreferencesKeys
import ir.darookhaneh.stock.core.datastore.model.AppearanceDataStore
import ir.darookhaneh.stock.core.datastore.model.AppearancePreferences
import ir.darookhaneh.stock.core.model.setting.toAppLanguage
import ir.darookhaneh.stock.core.model.setting.toDarkMode
import kotlinx.coroutines.flow.first

class AppearanceMigrator(
    private val dataStore: DataStore<Preferences>,
    private val appearanceDataStore: AppearanceDataStore,
) : BaseMigrator {
    override suspend fun shouldMigrate(): Boolean {
        val prefs = dataStore.data.first()

        return prefs.run {
            contains(UserPreferencesKeys.DYNAMIC_COLOR) ||
                    contains(UserPreferencesKeys.DARK_MODE) ||
                    contains(UserPreferencesKeys.LANGUAGE) ||
                    contains(UserPreferencesKeys.CATEGORY)
        }
    }

    override suspend fun migrate() {
        val oldPrefs = dataStore.data.first()
        val currentData = appearanceDataStore.getPreferences()
        val newData = AppearancePreferences(
            themeMode = oldPrefs[UserPreferencesKeys.DARK_MODE].toDarkMode(),
            enableDynamicColor = oldPrefs[UserPreferencesKeys.DYNAMIC_COLOR]
                ?: currentData.enableDynamicColor,
            appLanguage = oldPrefs[UserPreferencesKeys.LANGUAGE].toAppLanguage(),
            enableCategoryGroup = oldPrefs[UserPreferencesKeys.CATEGORY]
                ?: currentData.enableCategoryGroup
        )
        appearanceDataStore.setPreference(newData)
    }

    override suspend fun cleanUp() {
        dataStore.edit {
            it.remove(UserPreferencesKeys.DARK_MODE)
            it.remove(UserPreferencesKeys.CATEGORY)
            it.remove(UserPreferencesKeys.DYNAMIC_COLOR)
            it.remove(UserPreferencesKeys.LANGUAGE)
        }
    }

}