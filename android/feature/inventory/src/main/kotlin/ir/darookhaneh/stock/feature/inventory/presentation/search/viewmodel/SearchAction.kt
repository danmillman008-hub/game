package ir.darookhaneh.stock.feature.inventory.presentation.search.viewmodel

import ir.darookhaneh.stock.core.presentation.model.CategoryUiModel
import ir.darookhaneh.stock.core.presentation.viewmodel.UiAction
import ir.darookhaneh.stock.feature.inventory.presentation.model.FoodUiModel


sealed interface SearchAction : UiAction {
    data object OnDismiss : SearchAction
    data class OnQueryChange(val newQuery: String) : SearchAction
    data class OnEditSheetOpen(val food: FoodUiModel) : SearchAction
    data object OnClearQuery : SearchAction
    data object OnBack : SearchAction
    data class OnHistoryClick(val history: String) : SearchAction
    data class OnSearchResultClick(val searchResult: FoodUiModel) : SearchAction
    data class OnCategorySelect(val category: CategoryUiModel) : SearchAction
}