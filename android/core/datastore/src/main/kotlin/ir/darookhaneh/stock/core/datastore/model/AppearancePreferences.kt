package ir.darookhaneh.stock.core.datastore.model

import androidx.datastore.core.DataStore
import androidx.datastore.preferences.core.Preferences
import androidx.datastore.preferences.core.stringPreferencesKey
import ir.darookhaneh.stock.core.datastore.utils.BaseDataStore
import ir.darookhaneh.stock.core.datastore.utils.decodeFromFlow
import ir.darookhaneh.stock.core.datastore.utils.encodeToDataStore
import ir.darookhaneh.stock.core.model.setting.AppLanguage
import ir.darookhaneh.stock.core.model.setting.SeedColor
import ir.darookhaneh.stock.core.model.setting.ThemeMode
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.first
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.Json

@Serializable
data class AppearancePreferences(
    val themeMode: ThemeMode = ThemeMode.SYSTEM,
    val appLanguage: AppLanguage = AppLanguage.DEFAULT,
    val enableDynamicColor: Boolean = false,
    val enableCategoryGroup: Boolean = false,
    val seedColor: SeedColor = SeedColor.EMERALD,
) {
    companion object {
        val preferencesKey = stringPreferencesKey("appearance_prefs")
    }
}

class AppearanceDataStore(
    private val json: Json,
    private val dataStore: DataStore<Preferences>
) : BaseDataStore<AppearancePreferences> {
    override val preferencesFlow: Flow<AppearancePreferences>
        get() = dataStore.data.decodeFromFlow(
            json = json,
            key = AppearancePreferences.preferencesKey,
            defaultValue = AppearancePreferences()
        )

    override suspend fun getPreferences(): AppearancePreferences {
        return preferencesFlow.first()
    }

    override suspend fun setPreference(preferences: AppearancePreferences) {
        dataStore.encodeToDataStore(
            json = json,
            key = AppearancePreferences.preferencesKey,
            value = preferences
        )
    }

}
