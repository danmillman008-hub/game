package ir.darookhaneh.stock.feature.inventory.domain.usecase

import ir.darookhaneh.stock.core.datastore.model.GeneralDataStore
import ir.darookhaneh.stock.core.datastore.model.GeneralPreferences
import kotlinx.coroutines.flow.Flow

class GetInventoryPreferenceUseCase(
    private val generalDataStore: GeneralDataStore
) {
    fun observe(): Flow<GeneralPreferences> {
        return generalDataStore.preferencesFlow
    }

    suspend fun updatePreferences(generalPreferences: GeneralPreferences) {
        generalDataStore.setPreference(generalPreferences)
    }

}