package ir.darookhaneh.stock.feature.inventory.presentation.inventory.component.grid_list

import androidx.compose.foundation.Image
import androidx.compose.foundation.background
import androidx.compose.foundation.combinedClickable
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.lazy.staggeredgrid.LazyVerticalStaggeredGrid
import androidx.compose.foundation.lazy.staggeredgrid.StaggeredGridCells
import androidx.compose.foundation.lazy.staggeredgrid.items
import androidx.compose.foundation.lazy.staggeredgrid.rememberLazyStaggeredGridState
import androidx.compose.material3.CircularWavyProgressIndicator
import androidx.compose.material3.ExperimentalMaterial3ExpressiveApi
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.snapshotFlow
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.res.painterResource
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.unit.dp
import ir.darookhaneh.stock.core.designsystem.R
import ir.darookhaneh.stock.core.designsystem.icon.StockIcons
import ir.darookhaneh.stock.core.designsystem.icon.AppIcon
import ir.darookhaneh.stock.core.designsystem.theme.StockTheme
import ir.darookhaneh.stock.core.designsystem.tokens.LocalStockShapes
import ir.darookhaneh.stock.core.designsystem.tokens.LocalStockSpacing
import ir.darookhaneh.stock.feature.inventory.presentation.inventory.viewmodel.InventoryResultState
import ir.darookhaneh.stock.feature.inventory.presentation.model.FoodUiModel
import kotlinx.collections.immutable.ImmutableList
import kotlinx.collections.immutable.ImmutableSet

@Composable
internal fun InventoryGridContent(
    inventoryResultState: InventoryResultState,
    selectedIds: ImmutableSet<String>,
    onItemClick: (FoodUiModel) -> Unit,
    onItemLongClick: (FoodUiModel) -> Unit,
    onAddManuallyClick: () -> Unit,
    onScroll: (Boolean) -> Unit,
    itemProvider: () -> ImmutableList<FoodUiModel>,
) {
    when (inventoryResultState) {
        InventoryResultState.Loading -> LoadingPage(modifier = Modifier.fillMaxSize())

        is InventoryResultState.Empty -> EmptyScreen(
            modifier = Modifier
                .fillMaxWidth()
                .fillMaxHeight(0.8f)
        )

        is InventoryResultState.Success -> {
            val items = itemProvider()
            if (items.isNotEmpty()) {
                InventoryGridList(
                    items = items,
                    selectedIds = selectedIds,
                    onItemClick = onItemClick,
                    onItemLongClick = onItemLongClick,
                    onScroll = onScroll
                )
            } else {
                EmptyScreen(
                    modifier = Modifier
                        .fillMaxWidth()
                        .fillMaxHeight(0.8f)
                )
            }
        }
    }
}

@Composable
private fun InventoryGridList(
    modifier: Modifier = Modifier,
    items: ImmutableList<FoodUiModel>,
    selectedIds: ImmutableSet<String>,
    onItemClick: (FoodUiModel) -> Unit,
    onItemLongClick: (FoodUiModel) -> Unit = {},
    onScroll: (Boolean) -> Unit = {},
    contentPadding: PaddingValues = PaddingValues(
        start = 16.dp,
        top = 16.dp,
        end = 16.dp,
        bottom = 120.dp
    )
) {
    val staggeredGridState = rememberLazyStaggeredGridState()

    LaunchedEffect(staggeredGridState) {
        snapshotFlow { staggeredGridState.firstVisibleItemIndex < 1 }
            .collect { visible -> onScroll(visible) }
    }

    LazyVerticalStaggeredGrid(
        state = staggeredGridState,
        columns = StaggeredGridCells.Fixed(2),
        modifier = modifier.fillMaxSize(),
        contentPadding = contentPadding,
        horizontalArrangement = Arrangement.spacedBy(16.dp),
        verticalItemSpacing = 16.dp
    ) {
        items(
            items = items,
            key = { it.id }
        ) { foodItem ->
            val localShape = LocalStockShapes.current
            InventoryFoodGridItem(
                item = foodItem,
                isSelected = foodItem.id in selectedIds,
                modifier = Modifier
                    .animateItem()
                    .clip(localShape.large)
                    .combinedClickable(
                        enabled = true,
                        onClick = { onItemClick(foodItem) },
                        onLongClick = { onItemLongClick(foodItem) }
                    )
            )
        }
    }
}

@Composable
private fun EmptyScreen(
    modifier: Modifier = Modifier,
) {
    val localSpacing = LocalStockSpacing.current
    Column(
        modifier = modifier,
        verticalArrangement = Arrangement.Center,
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        AppIcon(
            iconProvider = StockIcons.Inventory.EmptyState,
            modifier = Modifier.size(56.dp),
            tint = MaterialTheme.colorScheme.secondary
        )

        Spacer(modifier = Modifier.height(localSpacing.small))

        Text(
            text = stringResource(ir.darookhaneh.stock.core.presentation.R.string.inventory_empty_content),
            style = MaterialTheme.typography.bodyLarge,
            fontWeight = FontWeight.Medium,
            color = MaterialTheme.colorScheme.secondary
        )
    }
}

@Composable
private fun EmptyPage(
    modifier: Modifier = Modifier,
    onClick: () -> Unit = {},
) {
    val spacing = StockTheme.spacing
    val scheme = MaterialTheme.colorScheme
    Column(
        modifier = modifier
            .background(color = scheme.background)
            .padding(horizontal = spacing.medium),
        verticalArrangement = Arrangement.spacedBy(
            space = spacing.small,
            alignment = Alignment.CenterVertically
        ),
        horizontalAlignment = Alignment.CenterHorizontally
    ) {
        Image(
            painter = painterResource(R.drawable.img_empty),
            contentDescription = "empty",
            modifier = Modifier.size(200.dp)
        )

        Text(
            text = stringResource(ir.darookhaneh.stock.core.presentation.R.string.inventory_empty_title),
            style = MaterialTheme.typography.bodyLarge.copy(
                fontWeight = FontWeight.Medium,
            ),
            color = scheme.onBackground,
        )

        Text(
            text = stringResource(ir.darookhaneh.stock.core.presentation.R.string.inventory_empty_content),
            style = MaterialTheme.typography.bodyMedium,
            textAlign = TextAlign.Center,
            color = scheme.onBackground
        )

        TextButton(
            onClick = onClick
        ) {
            Text(
                text = stringResource(ir.darookhaneh.stock.core.presentation.R.string.inventory_manually_btn),
                style = MaterialTheme.typography.bodyLarge,
                color = MaterialTheme.colorScheme.primary,
                fontWeight = FontWeight.Medium
            )
        }
    }
}

@OptIn(ExperimentalMaterial3ExpressiveApi::class)
@Composable
private fun LoadingPage(
    modifier: Modifier = Modifier,
) {
    Box(
        modifier = modifier,
        contentAlignment = Alignment.Center
    ) {
        CircularWavyProgressIndicator()
    }
}