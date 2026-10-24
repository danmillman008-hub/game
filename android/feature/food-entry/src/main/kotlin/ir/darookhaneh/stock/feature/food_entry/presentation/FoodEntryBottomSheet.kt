package ir.darookhaneh.stock.feature.food_entry.presentation

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.ExperimentalMaterial3ExpressiveApi
import androidx.compose.material3.MaterialShapes
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.material3.toShape
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.font.FontWeight
import ir.darookhaneh.stock.core.designsystem.component.AppBottomSheet
import ir.darookhaneh.stock.core.designsystem.icon.StockIcons
import ir.darookhaneh.stock.core.designsystem.icon.AppIcon
import ir.darookhaneh.stock.core.designsystem.tokens.LocalStockSpacing
import ir.darookhaneh.stock.core.presentation.R
import ir.darookhaneh.stock.feature.food_entry.presentation.component.FoodEntryContent
import ir.darookhaneh.stock.feature.food_entry.presentation.viewmodel.FoodEntryAction
import ir.darookhaneh.stock.feature.food_entry.presentation.viewmodel.FoodEntryUiState

@OptIn(ExperimentalMaterial3Api::class, ExperimentalMaterial3ExpressiveApi::class)
@Composable
fun FoodEntryBottomSheet(
    state: FoodEntryUiState,
    onDismiss: () -> Unit,
    onAction: (FoodEntryAction) -> Unit
) {
    AppBottomSheet(
        onDismiss = onDismiss,
        modifier = Modifier
    ) {
        val localSpacing = LocalStockSpacing.current
        val scheme = MaterialTheme.colorScheme
        Row(
            modifier = Modifier
                .fillMaxWidth()
                .padding(horizontal = localSpacing.medium),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(localSpacing.medium)
        ) {
            Box(
                modifier = Modifier.background(
                    shape = MaterialShapes.Pill.toShape(),
                    color = scheme.primary
                ),
                contentAlignment = Alignment.Center
            ) {
                AppIcon(
                    modifier = Modifier.padding(localSpacing.medium),
                    iconProvider = StockIcons.FoodEntry.AddFood,
                    tint = scheme.onPrimary
                )
            }

            Text(
                text = stringResource(R.string.food_entry_title),
                style = MaterialTheme.typography.titleLarge,
                fontWeight = FontWeight.SemiBold,
                color = MaterialTheme.colorScheme.onSurface
            )
        }

        Spacer(modifier = Modifier.height(localSpacing.large))

        FoodEntryContent(
            modifier = Modifier
                .fillMaxWidth()
                .padding(horizontal = localSpacing.medium)
                .padding(bottom = localSpacing.extraExtraLarge),
            state = state,
            onAction = onAction
        )
    }
}
