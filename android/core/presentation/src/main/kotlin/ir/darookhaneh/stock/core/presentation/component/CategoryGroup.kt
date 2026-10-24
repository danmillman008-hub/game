package ir.darookhaneh.stock.core.presentation.component

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.lazy.itemsIndexed
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material3.FilledTonalIconButton
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import ir.darookhaneh.stock.core.designsystem.component.AppFilterButton
import ir.darookhaneh.stock.core.designsystem.icon.StockIcons
import ir.darookhaneh.stock.core.designsystem.icon.AppIcon
import ir.darookhaneh.stock.core.designsystem.tokens.LocalStockSpacing
import ir.darookhaneh.stock.core.presentation.R
import ir.darookhaneh.stock.core.presentation.model.CategoryUiModel
import ir.darookhaneh.stock.core.presentation.utils.animatedHorizontalShape
import ir.darookhaneh.stock.core.presentation.utils.toItemPosition
import kotlinx.collections.immutable.ImmutableList

@Composable
fun CategoryGroup(
    modifier: Modifier = Modifier,
    selectedCategory: CategoryUiModel,
    categories: ImmutableList<CategoryUiModel>,
    onCategoryClick: (CategoryUiModel) -> Unit,
    onCreateCategoryClick: () -> Unit = {},
) {
    LazyRow(
        modifier = modifier,
        horizontalArrangement = Arrangement.spacedBy(4.dp)
    ) {
        items(
            items = categories,
        ) { category ->
            AppFilterButton(
                selected = selectedCategory == category,
                label = category.toUiText(),
                onClick = {
                    onCategoryClick(category)
                }
            )

        }

        item {
            FilledTonalIconButton(
                onClick = onCreateCategoryClick,
                shape = CircleShape
            ) {
                AppIcon(iconProvider = StockIcons.Inventory.AddCategory)
            }
        }
    }
}

@Composable
fun CategoryFilterGroup(
    modifier: Modifier = Modifier,
    selectedCategory: CategoryUiModel,
    categories: ImmutableList<CategoryUiModel>,
    onCategoryClick: (CategoryUiModel) -> Unit,
) {
    val localSpacing = LocalStockSpacing.current
    LazyRow(
        modifier = modifier,
        horizontalArrangement = Arrangement.spacedBy(localSpacing.extraSmall)
    ) {
        itemsIndexed(
            items = categories,
        ) { index, category ->
            val itemPosition = index.toItemPosition(categories.size)
            val selected = category == selectedCategory
            AppFilterButton(
                selected = selectedCategory == category,
                label = category.toUiText(),
                onClick = { onCategoryClick(category) },
                modifier = Modifier.animateItem(),
                shape = itemPosition.animatedHorizontalShape(selected = selected)
            )
        }
    }
}

@Composable
fun CategoryUiModel.toUiText(): String {
    return when (this) {
        CategoryUiModel.All -> stringResource(R.string.category_all)
        is CategoryUiModel.ByCategory -> this.data.name
        CategoryUiModel.Uncategorized -> stringResource(R.string.category_uncategorized)
    }
}