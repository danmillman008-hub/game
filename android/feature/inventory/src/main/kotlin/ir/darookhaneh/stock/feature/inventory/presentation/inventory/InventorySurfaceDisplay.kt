package ir.darookhaneh.stock.feature.inventory.presentation.inventory

import androidx.compose.runtime.Composable
import androidx.compose.ui.res.stringResource
import ir.darookhaneh.stock.core.designsystem.component.StockAlertDialog
import ir.darookhaneh.stock.core.designsystem.icon.StockIcons
import ir.darookhaneh.stock.core.designsystem.icon.toImageVector
import ir.darookhaneh.stock.core.presentation.R
import ir.darookhaneh.stock.core.presentation.component.AppNewFeatureBottomSheet
import ir.darookhaneh.stock.core.presentation.component.TextFieldDialog
import ir.darookhaneh.stock.feature.food_entry.navigation.FoodEntryRoute
import ir.darookhaneh.stock.feature.inventory.presentation.inventory.viewmodel.InventoryAction
import ir.darookhaneh.stock.feature.inventory.presentation.inventory.viewmodel.InventoryAction.OnEditCategorySheet.OnInputChange
import ir.darookhaneh.stock.feature.inventory.presentation.inventory.viewmodel.InventoryAction.OnEditCategorySheet.Save
import ir.darookhaneh.stock.feature.inventory.presentation.inventory.viewmodel.InventoryOverlay
import ir.darookhaneh.stock.feature.inventory.presentation.inventory.viewmodel.InventoryUiState
import ir.darookhaneh.stock.feature.inventory.presentation.model.toEntryUiModel
import ir.darookhaneh.stock.feature.inventory.presentation.shared.DetailBottomSheetRoute

@Composable
internal fun InventoryOverlayContainer(
    uiState: InventoryUiState,
    onAction: (InventoryAction) -> Unit
) {
    val onDismiss = { onAction(InventoryAction.OnDismiss) }
    when (val overlay = uiState.overlay) {
        InventoryOverlay.None -> Unit

        InventoryOverlay.CategoryEdit -> TextFieldDialog(
            title = stringResource(R.string.category_edit_dialog_title),
            value = uiState.categoryInput,
            confirmText = stringResource(R.string.inventory_category_edit_btn),
            onValueChange = { category -> onAction(OnInputChange(category)) },
            onDismiss = onDismiss,
            onConfirm = { onAction(Save) }
        )

        InventoryOverlay.CategoryDelete -> StockAlertDialog(
            icon = StockIcons.Inventory.DeleteCategory.toImageVector(),
            onDismissRequest = onDismiss,
            onConfirm = { onAction(InventoryAction.OnDeleteAlertConfirm) },
            title = stringResource(R.string.delete_category_dialog_title),
            text = stringResource(R.string.delete_category_dialog_content),
            confirmText = stringResource(R.string.delete_category_dialog_confirm)
        )

        InventoryOverlay.ItemDetail -> DetailBottomSheetRoute(
            foodItem = uiState.currentFoodItem,
            onDismiss = onDismiss,
            onNavigateToEdit = { foodUiModel ->
                onAction(
                    InventoryAction.OnEditFoodSheetOpen(foodUiModel)
                )
            }
        )

        InventoryOverlay.CategoryAdd -> TextFieldDialog(
            value = uiState.categoryInput,
            title = stringResource(R.string.inventory_category_add),
            confirmText = stringResource(R.string.inventory_category_add_btn),
            onValueChange = {
                onAction(InventoryAction.OnAddCategory.OnInputChange(it))
            },
            onDismiss = onDismiss,
            onConfirm = { onAction(InventoryAction.OnAddCategory.Save) }
        )

        is InventoryOverlay.NewFeatureSheet -> AppNewFeatureBottomSheet(
            versionFeatures = overlay.versionFeature,
            onDismiss = onDismiss
        )

        InventoryOverlay.ConsumeConfirm -> StockAlertDialog(
            icon = StockIcons.ConsumeFood.toImageVector(),
            onDismissRequest = onDismiss,
            onConfirm = { onAction(InventoryAction.OnConsumeConfirm) },
            title = stringResource(R.string.detail_dialog_consume_title),
            text = stringResource(R.string.detail_dialog_consume_content),
            confirmText = stringResource(R.string.detail_fab_consume_this)
        )

        InventoryOverlay.WasteConfirm -> StockAlertDialog(
            icon = StockIcons.WasteFood.toImageVector(),
            onDismissRequest = onDismiss,
            onConfirm = { onAction(InventoryAction.OnWasteConfirm) },
            title = stringResource(R.string.detail_dialog_waste_title),
            text = stringResource(R.string.detail_dialog_waste_content),
            confirmText = stringResource(R.string.detail_fab_mark_as_wasted),
            isDestructive = true
        )

        InventoryOverlay.CameraPolicySheet -> StockAlertDialog(
            icon = StockIcons.Inventory.ScanFood.toImageVector(),
            onDismissRequest = onDismiss,
            onConfirm = { onAction(InventoryAction.OnConfirmCameraPolicy) },
            title = stringResource(R.string.camera_permission_title),
            text = stringResource(R.string.camera_permission_description),
            confirmText = stringResource(R.string.camera_permission_confirm_btn),
        )

        is InventoryOverlay.AddFoodBottomSheet -> FoodEntryRoute(
            currentFoodModel = overlay.food?.toEntryUiModel(),
            onDismiss = onDismiss
        )

        is InventoryOverlay.EditFoodSheet -> FoodEntryRoute(
            currentFoodModel = overlay.food.toEntryUiModel(),
            onDismiss = onDismiss
        )
    }
}