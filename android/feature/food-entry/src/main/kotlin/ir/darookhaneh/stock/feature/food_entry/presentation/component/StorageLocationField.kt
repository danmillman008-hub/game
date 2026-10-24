package ir.darookhaneh.stock.feature.food_entry.presentation.component

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.itemsIndexed
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import ir.darookhaneh.stock.core.designsystem.component.AppFilterButton
import ir.darookhaneh.stock.core.designsystem.icon.StockIcons
import ir.darookhaneh.stock.core.designsystem.icon.toImageVector
import ir.darookhaneh.stock.core.designsystem.tokens.LocalStockSpacing
import ir.darookhaneh.stock.core.model.food.StorageLocation
import ir.darookhaneh.stock.core.presentation.R
import ir.darookhaneh.stock.core.presentation.utils.ItemPosition
import ir.darookhaneh.stock.core.presentation.utils.animatedHorizontalShape
import ir.darookhaneh.stock.core.presentation.utils.toItemPosition
import ir.darookhaneh.stock.core.presentation.utils.toStringRes
import ir.darookhaneh.stock.core.presentation.utils.toVerticalSegmentedShape

@Composable
fun StorageLocationField(
    itemPosition: ItemPosition,
    currentLocation: StorageLocation,
    onLocationSelect: (location: StorageLocation) -> Unit
) {
    val localSpacing = LocalStockSpacing.current
    val entries = StorageLocation.entries

    ToggleListItem(
        modifier = Modifier
            .fillMaxWidth(),
        shape = itemPosition.toVerticalSegmentedShape(),
        title = stringResource(R.string.food_entry_storage_location),
        icon = StockIcons.FoodEntry.StorageLocation.toImageVector(),
    ) {
        LazyRow(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.spacedBy(localSpacing.extraSmall)
        ) {
            itemsIndexed(
                items = entries,
                key = { _, item -> item.ordinal }
            ) { index: Int, item: StorageLocation ->
                val itemPosition = index.toItemPosition(entries.size)
                val selected = item == currentLocation
                AppFilterButton(
                    selected = item == currentLocation,
                    label = stringResource(item.toStringRes()),
                    onClick = { onLocationSelect(item) },
                    shape = itemPosition.animatedHorizontalShape(selected = selected)
                )
            }
        }
    }
}