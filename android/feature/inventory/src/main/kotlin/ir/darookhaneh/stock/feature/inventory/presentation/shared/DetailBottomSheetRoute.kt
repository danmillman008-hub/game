package ir.darookhaneh.stock.feature.inventory.presentation.shared

import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.res.stringResource
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.rememberViewModelStoreOwner
import ir.darookhaneh.stock.core.designsystem.component.StockAlertDialog
import ir.darookhaneh.stock.core.designsystem.component.AppBottomSheet
import ir.darookhaneh.stock.core.designsystem.icon.StockIcons
import ir.darookhaneh.stock.core.designsystem.icon.toImageVector
import ir.darookhaneh.stock.core.presentation.ObserveEffect
import ir.darookhaneh.stock.core.presentation.R
import ir.darookhaneh.stock.feature.inventory.presentation.model.FoodUiModel
import ir.darookhaneh.stock.feature.inventory.presentation.shared.viewmodel.DetailAction
import ir.darookhaneh.stock.feature.inventory.presentation.shared.viewmodel.DetailEvent
import ir.darookhaneh.stock.feature.inventory.presentation.shared.viewmodel.DetailOverlay
import ir.darookhaneh.stock.feature.inventory.presentation.shared.viewmodel.DetailUiState
import org.koin.androidx.compose.koinViewModel
import org.koin.core.parameter.parametersOf

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun DetailBottomSheetRoute(
    foodItem: FoodUiModel,
    onDismiss: () -> Unit,
    onNavigateToEdit: (FoodUiModel) -> Unit,
) {
    val rememberViewModelStoreOwner = rememberViewModelStoreOwner()
    val viewModel: DetailBottomSheetViewModel = koinViewModel(
        viewModelStoreOwner = rememberViewModelStoreOwner
    ) { parametersOf(foodItem) }
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
    val onAction = viewModel::onAction

    ObserveEffect(viewModel.uiEvent) { event ->
        when (event) {
            DetailEvent.OnDismiss -> onDismiss()
            is DetailEvent.NavigateToEdit -> onNavigateToEdit(event.foodUiModel)
        }
    }

    AppBottomSheet(
        onDismiss = onDismiss,
    ) {
        DetailBottomSheetContent(
            uiState = uiState,
            onEditClick = { onAction(DetailAction.OnEditClick) },
            onConsumedClick = { onAction(DetailAction.OnConsumeClick) },
            onWastedClick = { onAction(DetailAction.OnWasteClick) }
        )
    }

    DetailBottomSheetOverlays(
        uiState = uiState,
        onDismissOverlay = { onAction(DetailAction.OnDismiss) },
        onConsumeConfirm = { onAction(DetailAction.OnConsumeConfirm) },
        onWasteConfirm = { onAction(DetailAction.OnWasteConfirm) }
    )
}

@Composable
fun DetailBottomSheetOverlays(
    uiState: DetailUiState,
    onDismissOverlay: () -> Unit,
    onConsumeConfirm: () -> Unit,
    onWasteConfirm: () -> Unit
) {
    when (uiState.overlay) {
        DetailOverlay.None -> Unit
        DetailOverlay.ConsumeConfirm -> StockAlertDialog(
            icon = StockIcons.ConsumeFood.toImageVector(),
            onDismissRequest = onDismissOverlay,
            onConfirm = onConsumeConfirm,
            title = stringResource(R.string.detail_dialog_consume_title),
            text = stringResource(R.string.detail_dialog_consume_content),
            confirmText = stringResource(R.string.detail_fab_consume_this)
        )

        DetailOverlay.WasteConfirm -> StockAlertDialog(
            icon = StockIcons.WasteFood.toImageVector(),
            onDismissRequest = onDismissOverlay,
            onConfirm = onWasteConfirm,
            title = stringResource(R.string.detail_dialog_waste_title),
            text = stringResource(R.string.detail_dialog_waste_content),
            confirmText = stringResource(R.string.detail_fab_mark_as_wasted),
            isDestructive = true
        )
    }
}