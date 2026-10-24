package ir.darookhaneh.stock.feature.inventory.presentation.inventory.viewmodel

import ir.darookhaneh.stock.core.presentation.viewmodel.UiEvent

sealed interface InventoryEvent : UiEvent {
    data object RequestCameraPermission : InventoryEvent
    data object NavigateToScanner : InventoryEvent
}
