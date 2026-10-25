package ir.darookhaneh.stock.feature.pharmacy.presentation.dashboard

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.ObserveDashboardUseCase
import ir.darookhaneh.stock.core.model.pharmacy.DashboardSnapshot
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.stateIn

/** داشبورد: فقط دادهٔ واقعی، هیچ عدد ساختگی. */
class DashboardViewModel(
    observeDashboard: ObserveDashboardUseCase,
) : ViewModel() {

    val uiState: StateFlow<DashboardSnapshot> = observeDashboard().stateIn(
        scope = viewModelScope,
        started = SharingStarted.WhileSubscribed(5_000),
        initialValue = DashboardSnapshot(),
    )
}
