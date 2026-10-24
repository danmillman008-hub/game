package ir.darookhaneh.stock.feature.scanner.presentation.scanner.viewmodel

import androidx.compose.runtime.Immutable
import ir.darookhaneh.stock.core.model.food.FoodItem
import ir.darookhaneh.stock.core.presentation.UiResult
import ir.darookhaneh.stock.core.presentation.viewmodel.UiState

@Immutable
data class ScannerUiState(
    val barCodeInput: String = "",
    val isAutoScanned: Boolean = true,
    val isFlashOn: Boolean = false,
    val scanResult: UiResult<FoodItem> = UiResult.Idle,
    val overlay: ScannerOverlay = ScannerOverlay.NONE,
    val labelEvent: LabelEvent = LabelEvent.SCANNING,
) : UiState

enum class LabelEvent {
    NONE, AUTO_OFF, SCANNING, FAILURE, ADD_MANUALLY
}

sealed interface ScannerOverlay {
    data object NONE : ScannerOverlay
    data object LoadingDialog : ScannerOverlay
    data object BarcodeScanningDialog : ScannerOverlay
    data object WarningDialog : ScannerOverlay
    data class SuccessBottomSheet(val result: FoodItem) : ScannerOverlay
}

