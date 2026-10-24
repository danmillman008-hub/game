package ir.darookhaneh.stock.feature.inventory.presentation.inventory.component.grid_list

import androidx.compose.runtime.Composable
import ir.darookhaneh.stock.core.presentation.model.CategoryUiModel
import ir.darookhaneh.stock.feature.inventory.presentation.inventory.viewmodel.InventoryResultState
import ir.darookhaneh.stock.feature.inventory.presentation.inventory.viewmodel.InventorySortMode
import ir.darookhaneh.stock.feature.inventory.presentation.inventory.viewmodel.getDataOrEmpty
import ir.darookhaneh.stock.feature.inventory.presentation.model.FoodUiModel
import ir.darookhaneh.stock.feature.inventory.utils.getFilteredAndSortedList
import kotlinx.collections.immutable.ImmutableSet
import kotlinx.collections.immutable.toImmutableList

@Composable
fun InventoryCategoryList(
    currentCategory: CategoryUiModel,
    inventoryResultState: InventoryResultState,
    sortMode: InventorySortMode,
    showExpiredOnly: Boolean,
    selectedIds: ImmutableSet<String>,
    onItemClick: (FoodUiModel) -> Unit,
    onItemLongClick: (FoodUiModel) -> Unit,
    onAddManuallyClick: () -> Unit,
    onFabVisibilityChange: (Boolean) -> Unit,
) {
    InventoryGridContent(
        inventoryResultState = inventoryResultState,
        selectedIds = selectedIds,
        onItemClick = onItemClick,
        onItemLongClick = onItemLongClick,
        onAddManuallyClick = onAddManuallyClick,
        itemProvider = {
            inventoryResultState.getDataOrEmpty().getFilteredAndSortedList(
                category = currentCategory,
                showExpiredOnly = showExpiredOnly,
                sortMode = sortMode
            ).toImmutableList()
        },
        onScroll = onFabVisibilityChange
    )
}
