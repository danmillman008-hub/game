package ir.darookhaneh.stock.feature.pharmacy.presentation.history

import androidx.compose.runtime.Immutable
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import ir.darookhaneh.stock.core.domain.pharmacy.repository.InventoryRepository
import ir.darookhaneh.stock.core.model.pharmacy.HistoryEntry
import ir.darookhaneh.stock.core.model.pharmacy.InventoryEventType
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.combine
import kotlinx.coroutines.flow.flatMapLatest
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.flow.update

@Immutable
data class HistoryUiState(
    val query: String = "",
    val filter: InventoryEventType? = null,
    val entries: List<HistoryEntry> = emptyList(),
    val isLoading: Boolean = true,
) {
    val isEmpty: Boolean get() = !isLoading && entries.isEmpty()
}

sealed interface HistoryAction {
    data class OnQueryChange(val value: String) : HistoryAction
    data class OnFilterChange(val type: InventoryEventType?) : HistoryAction
}

/**
 * تاریخچهٔ سراسری همهٔ عملیات (نسخهٔ HTML همین را داشت؛ نسخهٔ ۲.۰.۰ فقط
 * تاریخچهٔ هر بچ را نشان می‌داد و عملاً پیدا کردن «چه کسی چه چیزی را خروج زد» ممکن نبود).
 */
@OptIn(ExperimentalCoroutinesApi::class)
class HistoryViewModel(
    inventoryRepository: InventoryRepository,
) : ViewModel() {

    private val query = MutableStateFlow("")
    private val filter = MutableStateFlow<InventoryEventType?>(null)

    val uiState: StateFlow<HistoryUiState> = combine(
        query,
        filter,
        query.flatMapLatest { q -> inventoryRepository.observeHistory(q, limit = 500) },
    ) { q, f, entries ->
        HistoryUiState(
            query = q,
            filter = f,
            entries = if (f == null) entries else entries.filter { it.type == f },
            isLoading = false,
        )
    }.stateIn(
        scope = viewModelScope,
        started = SharingStarted.WhileSubscribed(5_000),
        initialValue = HistoryUiState(),
    )

    fun onAction(action: HistoryAction) {
        when (action) {
            is HistoryAction.OnQueryChange -> query.update { action.value }
            is HistoryAction.OnFilterChange -> filter.update { action.type }
        }
    }
}
