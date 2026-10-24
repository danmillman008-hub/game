package ir.darookhaneh.stock.feature.scanner.presentation.scanner.viewmodel

import ir.darookhaneh.stock.core.model.food.FoodItem
import ir.darookhaneh.stock.core.presentation.UiError

import ir.darookhaneh.stock.core.presentation.viewmodel.UiEvent

sealed interface ScannerEvent : UiEvent {
    data class OnSuccess(val foodItem: FoodItem) : ScannerEvent
    data class OnFailure(val error: UiError) : ScannerEvent
}