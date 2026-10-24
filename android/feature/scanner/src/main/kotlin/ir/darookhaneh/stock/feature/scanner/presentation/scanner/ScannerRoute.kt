package ir.darookhaneh.stock.feature.scanner.presentation.scanner

import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.hapticfeedback.HapticFeedbackType
import androidx.compose.ui.platform.LocalHapticFeedback
import androidx.compose.ui.res.stringResource
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import ir.darookhaneh.stock.core.designsystem.component.StockAlertDialog
import ir.darookhaneh.stock.core.designsystem.component.BoxLayout
import ir.darookhaneh.stock.core.presentation.ObserveEffect
import ir.darookhaneh.stock.core.presentation.R
import ir.darookhaneh.stock.core.presentation.component.TextFieldDialog
import ir.darookhaneh.stock.feature.food_entry.navigation.FoodEntryRoute
import ir.darookhaneh.stock.feature.food_entry.presentation.model.toEntryUiModel
import ir.darookhaneh.stock.feature.scanner.presentation.scanner.component.dialog.ScannerLoadingDialog
import ir.darookhaneh.stock.feature.scanner.presentation.scanner.viewmodel.AddBarcodeDialogAction.OnConfirm
import ir.darookhaneh.stock.feature.scanner.presentation.scanner.viewmodel.AddBarcodeDialogAction.OnValueChange
import ir.darookhaneh.stock.feature.scanner.presentation.scanner.viewmodel.ScannerAction.OnDismissRequest
import ir.darookhaneh.stock.feature.scanner.presentation.scanner.viewmodel.ScannerEvent
import ir.darookhaneh.stock.feature.scanner.presentation.scanner.viewmodel.ScannerOverlay
import ir.darookhaneh.stock.feature.scanner.presentation.scanner.viewmodel.ScannerUiState
import ir.darookhaneh.stock.feature.scanner.presentation.scanner.viewmodel.ScannerViewModel
import ir.darookhaneh.stock.feature.scanner.presentation.scanner.viewmodel.WarningDialogAction
import org.koin.androidx.compose.koinViewModel

@Composable
fun ScannerRoute(
    onNavigateBack: () -> Unit,
) {
    val localHapticFeedback = LocalHapticFeedback.current
    val viewModel: ScannerViewModel = koinViewModel()
    val uiState: ScannerUiState by viewModel.uiState.collectAsStateWithLifecycle()
    val onAction = viewModel::onAction
    ObserveEffect(viewModel.uiEvent) { event ->
        when (event) {
            is ScannerEvent.OnSuccess -> {
                localHapticFeedback.performHapticFeedback(HapticFeedbackType.LongPress)
            }

            is ScannerEvent.OnFailure -> {
                localHapticFeedback.performHapticFeedback(HapticFeedbackType.Reject)
            }
        }
    }

    BoxLayout {
        ScannerScreen(
            uiState = uiState,
            onClosePress = onNavigateBack,
            onAction = onAction
        )

        when (val overlay = uiState.overlay) {
            ScannerOverlay.NONE -> Unit
            ScannerOverlay.LoadingDialog -> {
                ScannerLoadingDialog(onDismissRequest = { onAction(OnDismissRequest) })
            }

            ScannerOverlay.BarcodeScanningDialog -> TextFieldDialog(
                value = uiState.barCodeInput,
                title = stringResource(R.string.scanner_barcode_dialog_title),
                confirmText = stringResource(R.string.scanner_barcode_confirm),
                onValueChange = { value -> onAction(OnValueChange(value)) },
                onDismiss = { onAction(OnDismissRequest) },
                onConfirm = { onAction(OnConfirm) }
            )

            ScannerOverlay.WarningDialog -> StockAlertDialog(
                onConfirm = { onAction(WarningDialogAction.Confirm) },
                onDismissRequest = { onAction(OnDismissRequest) },
                title = stringResource(R.string.scanner_warning_dialog_title),
                text = stringResource(R.string.scanner_warning_dialog_content),
                dismissText = stringResource(R.string.scanner_warning_dialog_dismiss),
                confirmText = stringResource(R.string.scanner_warning_dialog_confirm)
            )

            is ScannerOverlay.SuccessBottomSheet -> {
                FoodEntryRoute(
                    onDismiss = { onAction(OnDismissRequest) },
                    currentFoodModel = overlay.result.toEntryUiModel(),
                )
            }
        }
    }
}
