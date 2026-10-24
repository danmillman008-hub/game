package ir.darookhaneh.stock.feature.inventory.presentation.shared

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.ExperimentalMaterial3ExpressiveApi
import androidx.compose.material3.MaterialShapes
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.toShape
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import ir.darookhaneh.stock.core.designsystem.icon.StockIcons
import ir.darookhaneh.stock.core.designsystem.icon.AppIcon
import ir.darookhaneh.stock.core.designsystem.tokens.LocalStockSpacing

@OptIn(ExperimentalMaterial3ExpressiveApi::class)
@Composable
fun DetailTopBar(
    modifier: Modifier = Modifier,
) {
    val localSpacing = LocalStockSpacing.current

    Row(
        modifier = modifier,
        verticalAlignment = Alignment.CenterVertically,
        horizontalArrangement = Arrangement.spacedBy(localSpacing.medium)
    ) {
        Surface(
            modifier = Modifier,
            color = MaterialTheme.colorScheme.primary,
            shape = MaterialShapes.Pill.toShape()
        ) {
            AppIcon(
                modifier = Modifier.padding(localSpacing.small),
                iconProvider = StockIcons.Inventory.DetailFood,
                tint = MaterialTheme.colorScheme.onPrimary
            )
        }


        Text(
            modifier = Modifier.weight(1f),
            text = "Food Detail",
            style = MaterialTheme.typography.titleLarge.copy(
                fontWeight = FontWeight.Black
            )
        )
    }
}