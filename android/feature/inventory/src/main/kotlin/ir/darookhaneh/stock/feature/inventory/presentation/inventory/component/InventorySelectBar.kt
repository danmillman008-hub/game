package ir.darookhaneh.stock.feature.inventory.presentation.inventory.component

import androidx.compose.material3.ExperimentalMaterial3Api
import androidx.compose.material3.ExperimentalMaterial3ExpressiveApi
import androidx.compose.material3.IconButton
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.MediumFlexibleTopAppBar
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.pluralStringResource
import androidx.compose.ui.text.font.FontWeight
import ir.darookhaneh.stock.core.designsystem.icon.StockIcons
import ir.darookhaneh.stock.core.designsystem.icon.AppIcon
import ir.darookhaneh.stock.core.presentation.R
import ir.darookhaneh.stock.feature.inventory.presentation.inventory.viewmodel.InventoryAction
import ir.darookhaneh.stock.feature.inventory.presentation.inventory.viewmodel.InventorySelectAction

@OptIn(ExperimentalMaterial3Api::class, ExperimentalMaterial3ExpressiveApi::class)
@Composable
fun InventorySelectBar(
    selectedCount: Int,
    modifier: Modifier = Modifier,
    onAction: (InventoryAction) -> Unit
) {
    MediumFlexibleTopAppBar(
        modifier = modifier,
        title = {
            Text(
                text = "$selectedCount",
                style = MaterialTheme.typography.displaySmall.copy(
                    fontWeight = FontWeight.Black
                )
            )
        },
        subtitle = {
            Text(text = pluralStringResource(R.plurals.inventory_selected_title, selectedCount))
        },
        navigationIcon = {
            IconButton(
                onClick = { onAction(InventorySelectAction.ClearSelection) }
            ) {
                AppIcon(iconProvider = StockIcons.Close)
            }
        },
        actions = {
            IconButton(
                onClick = { onAction(InventorySelectAction.SelectAll) }
            ) {
                AppIcon(iconProvider = StockIcons.Inventory.SelectAll)
            }

            IconButton(
                onClick = { onAction(InventorySelectAction.ConsumeAll) }
            ) {
                AppIcon(iconProvider = StockIcons.ConsumeFood)
            }

            IconButton(
                onClick = { onAction(InventorySelectAction.WasteAll) }
            ) {
                AppIcon(iconProvider = StockIcons.WasteFood)
            }
        }
    )
}