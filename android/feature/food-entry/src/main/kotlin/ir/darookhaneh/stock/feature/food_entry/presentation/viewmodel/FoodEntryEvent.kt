package ir.darookhaneh.stock.feature.food_entry.presentation.viewmodel

import ir.darookhaneh.stock.core.presentation.viewmodel.UiEvent

sealed interface FoodEntryEvent : UiEvent {
    data object AskNotificationPermission : FoodEntryEvent
    data object OnNavigateBack : FoodEntryEvent
}