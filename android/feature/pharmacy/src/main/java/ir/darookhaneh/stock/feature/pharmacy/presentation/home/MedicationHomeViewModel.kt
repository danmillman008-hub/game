package ir.darookhaneh.stock.feature.pharmacy.presentation.home

import androidx.compose.runtime.Immutable
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.ObserveDrugSummariesUseCase
import ir.darookhaneh.stock.core.model.pharmacy.DrugSummary
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.combine
import kotlinx.coroutines.flow.flatMapLatest
import kotlinx.coroutines.flow.stateIn

@Immutable
data class MedicationHomeUiState(
    val query: String = "",
    val drugs: List<DrugSummary> = emptyList(),
    val isLoading: Boolean = true,
) {
    val isEmpty: Boolean get() = !isLoading && drugs.isEmpty() && query.isBlank()
    val isNoResult: Boolean get() = !isLoading && drugs.isEmpty() && query.isNotBlank()
}

sealed interface MedicationHomeAction {
    data class OnQueryChange(val query: String) : MedicationHomeAction
    data object ClearQuery : MedicationHomeAction
}

/**
 * داشبورد داروها — داده از Room، بدون mock.
 * آستانهٔ موجودی کم در لایهٔ دامنه اعمال می‌شود (پیش‌فرض ۱۰ برای مجموع موجودی هر دارو).
 */
@OptIn(ExperimentalCoroutinesApi::class)
class MedicationHomeViewModel(
    private val observeDrugSummaries: ObserveDrugSummariesUseCase,
) : ViewModel() {

    private val query = MutableStateFlow("")
    val uiState: StateFlow<MedicationHomeUiState> = combine(
        query.flatMapLatest { observeDrugSummaries(it) },
        query,
    ) { drugs, currentQuery ->
        MedicationHomeUiState(query = currentQuery, drugs = drugs, isLoading = false)
    }.stateIn(
        scope = viewModelScope,
        started = SharingStarted.WhileSubscribed(5_000),
        initialValue = MedicationHomeUiState(),
    )

    private val _lastSavedDrugId = MutableStateFlow<Long?>(null)
    val lastSavedDrugId: StateFlow<Long?> = _lastSavedDrugId.asStateFlow()

    fun onAction(action: MedicationHomeAction) {
        when (action) {
            is MedicationHomeAction.OnQueryChange -> query.value = action.query
            MedicationHomeAction.ClearQuery -> query.value = ""
        }
    }
}
