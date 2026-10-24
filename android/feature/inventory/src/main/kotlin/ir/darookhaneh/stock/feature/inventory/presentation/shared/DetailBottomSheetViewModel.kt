package ir.darookhaneh.stock.feature.inventory.presentation.shared

import androidx.lifecycle.viewModelScope
import ir.darookhaneh.stock.core.data.util.product
import ir.darookhaneh.stock.core.presentation.viewmodel.BaseViewModel
import ir.darookhaneh.stock.feature.inventory.domain.usecase.food.MarkFoodAsConsumedUseCase
import ir.darookhaneh.stock.feature.inventory.domain.usecase.food.MarkFoodAsWastedUseCase
import ir.darookhaneh.stock.feature.inventory.presentation.model.FoodUiModel
import ir.darookhaneh.stock.feature.inventory.presentation.shared.viewmodel.DetailAction
import ir.darookhaneh.stock.feature.inventory.presentation.shared.viewmodel.DetailEvent
import ir.darookhaneh.stock.feature.inventory.presentation.shared.viewmodel.DetailOverlay
import ir.darookhaneh.stock.feature.inventory.presentation.shared.viewmodel.DetailUiState
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch

class DetailBottomSheetViewModel(
    private val foodItem: FoodUiModel,
    private val markFoodAsConsumedUseCase: MarkFoodAsConsumedUseCase,
    private val markFoodAsWastedUseCase: MarkFoodAsWastedUseCase
) : BaseViewModel<DetailUiState, DetailEvent, DetailAction>() {
    private val _uiState = MutableStateFlow(
        DetailUiState(
            currentFoodItem = foodItem
        )
    )
    override val uiState: StateFlow<DetailUiState>
        get() = _uiState.asStateFlow()

    override fun onAction(action: DetailAction) {
        when (action) {
            DetailAction.OnConsumeClick -> {
                _uiState.product { copy(overlay = DetailOverlay.ConsumeConfirm) }
            }

            DetailAction.OnConsumeConfirm -> {
                viewModelScope.launch {
                    markFoodAsConsumedUseCase(foodItem.id)
                    _uiState.product { copy(overlay = DetailOverlay.None) }
                    emitEvent(DetailEvent.OnDismiss)
                }
            }

            DetailAction.OnDismiss -> {
                _uiState.product { copy(overlay = DetailOverlay.None) }
            }

            DetailAction.OnEditClick -> {
                _uiState.product { copy(overlay = DetailOverlay.None) }
                emitEvent(DetailEvent.NavigateToEdit(foodItem))
            }

            DetailAction.OnWasteClick -> {
                _uiState.product { copy(overlay = DetailOverlay.WasteConfirm) }
            }

            DetailAction.OnWasteConfirm -> viewModelScope.launch {
                markFoodAsWastedUseCase(foodItem.id)
                _uiState.product { copy(overlay = DetailOverlay.None) }
                emitEvent(DetailEvent.OnDismiss)
            }
        }
    }
}
