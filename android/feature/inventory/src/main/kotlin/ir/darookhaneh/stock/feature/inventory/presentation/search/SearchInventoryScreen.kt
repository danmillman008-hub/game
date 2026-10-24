package ir.darookhaneh.stock.feature.inventory.presentation.search

import androidx.compose.animation.AnimatedVisibility
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.heightIn
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.ExperimentalMaterial3ExpressiveApi
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.remember
import androidx.compose.ui.Modifier
import androidx.compose.ui.focus.FocusRequester
import androidx.compose.ui.unit.dp
import ir.darookhaneh.stock.core.designsystem.tokens.LocalStockSpacing
import ir.darookhaneh.stock.core.presentation.component.CategoryFilterGroup
import ir.darookhaneh.stock.core.presentation.model.CategoryUiModel
import ir.darookhaneh.stock.feature.inventory.presentation.model.FoodUiModel
import ir.darookhaneh.stock.feature.inventory.presentation.search.component.RecentSearchContent
import ir.darookhaneh.stock.feature.inventory.presentation.search.component.SearchEmpty
import ir.darookhaneh.stock.feature.inventory.presentation.search.component.SearchResultContent
import ir.darookhaneh.stock.feature.inventory.presentation.search.component.SearchTopBar
import ir.darookhaneh.stock.feature.inventory.presentation.search.viewmodel.SearchAction
import ir.darookhaneh.stock.feature.inventory.presentation.search.viewmodel.SearchUiState
import kotlinx.collections.immutable.ImmutableList

@OptIn(ExperimentalMaterial3Api::class, ExperimentalMaterial3ExpressiveApi::class)
@Composable
fun SearchInventoryScreen(
    foodItems: ImmutableList<FoodUiModel>,
    uiState: SearchUiState,
    onAction: (SearchAction) -> Unit,
) {
    val focusRequester = remember { FocusRequester() }
    val localSpacing = LocalStockSpacing.current
    LaunchedEffect(Unit) { focusRequester.requestFocus() }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(top = localSpacing.large),
    ) {
        SearchTopBar(
            modifier = Modifier.fillMaxWidth(),
            query = uiState.query,
            onBackClick = { onAction(SearchAction.OnBack) },
            onQueryChange = { query -> onAction(SearchAction.OnQueryChange(query)) },
            onClearQuery = { onAction(SearchAction.OnClearQuery) }
        )

        Spacer(modifier = Modifier.height(localSpacing.medium))

        CategoryFilterGroup(
            modifier = Modifier
                .fillMaxWidth()
                .padding(horizontal = localSpacing.large),
            selectedCategory = uiState.currentCategory,
            categories = uiState.categories,
            onCategoryClick = { category -> onAction(SearchAction.OnCategorySelect(category)) }
        )

        AnimatedVisibility(
            visible = uiState.query.isBlank() && uiState.currentCategory == CategoryUiModel.All,
            modifier = Modifier
                .fillMaxWidth()
                .padding(horizontal = localSpacing.large)
                .padding(top = localSpacing.medium)
        ) {
            RecentSearchContent(
                modifier = Modifier
                    .fillMaxWidth()
                    .heightIn(max = 240.dp),
                searchHistories = uiState.searchHistories,
                onItemClick = { item ->
                    onAction(SearchAction.OnHistoryClick(item.name))
                }
            )
        }

        Spacer(modifier = Modifier.height(localSpacing.extraLarge))

        if (foodItems.isEmpty()) {
            SearchEmpty(modifier = Modifier.fillMaxSize())
        } else {
            SearchResultContent(
                modifier = Modifier
                    .weight(1f)
                    .padding(horizontal = localSpacing.large),
                searchResults = foodItems,
                onItemClick = { item ->
                    onAction(SearchAction.OnSearchResultClick(item))
                }
            )
        }
    }
}
