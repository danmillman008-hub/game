package ir.darookhaneh.stock.feature.food_entry.presentation.component

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.itemsIndexed
import androidx.compose.material3.FilledTonalIconButton
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import ir.darookhaneh.stock.core.designsystem.component.AppFilterButton
import ir.darookhaneh.stock.core.designsystem.icon.StockIcons
import ir.darookhaneh.stock.core.designsystem.icon.AppIcon
import ir.darookhaneh.stock.core.designsystem.icon.toImageVector
import ir.darookhaneh.stock.core.designsystem.tokens.LocalStockSpacing
import ir.darookhaneh.stock.core.presentation.R
import ir.darookhaneh.stock.core.presentation.model.CategoryUiModel
import ir.darookhaneh.stock.core.presentation.utils.ItemPosition
import ir.darookhaneh.stock.core.presentation.utils.animatedHorizontalShape
import ir.darookhaneh.stock.core.presentation.utils.toItemPosition
import ir.darookhaneh.stock.core.presentation.utils.toVerticalSegmentedShape
import kotlinx.collections.immutable.ImmutableList

@Composable
fun CategoryField(
    itemPosition: ItemPosition,
    currentCategory: CategoryUiModel,
    categories: ImmutableList<CategoryUiModel.ByCategory>,
    onCategorySelect: (category: CategoryUiModel.ByCategory) -> Unit,
    onNewCategoryAdd: () -> Unit
) {
    val localSpacing = LocalStockSpacing.current
    ToggleListItem(
        modifier = Modifier.fillMaxWidth(),
        shape = itemPosition.toVerticalSegmentedShape(),
        title = stringResource(R.string.food_entry_category),
        icon = StockIcons.Inventory.Category.toImageVector(),
    ) {
        Row(
            modifier = Modifier.fillMaxWidth(),
            verticalAlignment = Alignment.CenterVertically,
        ) {
            LazyRow(
                modifier = Modifier.weight(1f),
                horizontalArrangement = Arrangement.spacedBy(
                    localSpacing.extraSmall
                ),
                contentPadding = PaddingValues(end = localSpacing.extraSmall),
            ) {
                itemsIndexed(
                    items = categories,
                    key = { _, category -> category.data.id }
                ) { index, category ->

                    val itemPosition = index.toItemPosition(categories.size)
                    val selected = category == currentCategory

                    AppFilterButton(
                        selected = selected,
                        label = category.data.name,
                        onClick = {
                            onCategorySelect(category)
                        },
                        shape = itemPosition.animatedHorizontalShape(
                            selected = selected
                        )
                    )
                }
            }

            FilledTonalIconButton(
                onClick = onNewCategoryAdd,
            ) {
                AppIcon(
                    iconProvider = StockIcons.FoodEntry.AddCategory
                )
            }
        }
    }
}