package ir.darookhaneh.stock.feature.food_entry.presentation.component

import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material3.ExperimentalMaterial3ExpressiveApi
import androidx.compose.material3.FilledTonalIconButton
import androidx.compose.material3.IconButtonDefaults
import androidx.compose.material3.ListItem
import androidx.compose.material3.ListItemDefaults
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.font.FontWeight
import ir.darookhaneh.stock.core.designsystem.icon.StockIcons
import ir.darookhaneh.stock.core.designsystem.icon.AppIcon
import ir.darookhaneh.stock.core.designsystem.tokens.LocalStockShapes
import ir.darookhaneh.stock.core.presentation.R
import ir.darookhaneh.stock.core.presentation.utils.ItemPosition
import ir.darookhaneh.stock.core.presentation.utils.toVerticalSegmentedShape
import ir.darookhaneh.stock.toReadableText

@OptIn(ExperimentalMaterial3ExpressiveApi::class)
@Composable
fun ExpiryDateField(
    modifier: Modifier = Modifier,
    itemPosition: ItemPosition,
    expiryDate: Long?,
    errorMessage: String? = null,
    onEditClick: () -> Unit,
) {
    val scheme = MaterialTheme.colorScheme
    val stockIcon = StockIcons.FoodEntry
    LocalStockShapes.current
    ListItem(
        shapes = ListItemDefaults.shapes(
            shape = itemPosition.toVerticalSegmentedShape()
        ),
        modifier = modifier,
        colors = ListItemDefaults.colors(
            containerColor = scheme.surface,
            headlineColor = scheme.onSurface,
            overlineColor = scheme.onSurface,
        ),
        onClick = onEditClick,
        leadingContent = {
            AppIcon(
                tint = scheme.onSecondaryContainer,
                iconProvider = stockIcon.ExpiryDate,
            )
        },
        trailingContent = {
            FilledTonalIconButton(
                onClick = onEditClick,
                shape = CircleShape,
                colors = IconButtonDefaults.iconButtonColors(
                    containerColor = scheme.primary,
                    contentColor = scheme.onPrimary
                )
            ) {
                AppIcon(
                    iconProvider = StockIcons.FoodEntry.EditFood,
                )
            }
        },
        supportingContent = {
            errorMessage?.let {
                Text(
                    text = errorMessage,
                    color = MaterialTheme.colorScheme.error,
                    style = MaterialTheme.typography.labelLarge
                )
            }
        },
        verticalAlignment = Alignment.CenterVertically,
        overlineContent = {
            Text(
                text = stringResource(R.string.food_entry_expiry_date),
                fontWeight = FontWeight.SemiBold,
                style = MaterialTheme.typography.bodyMedium
            )
        }
    ) {
        Text(
            text = expiryDate?.toReadableText()
                ?.ifBlank { stringResource(R.string.food_entry_expiry_date_placeholder) }
                ?: stringResource(R.string.food_entry_expiry_date_placeholder),
            style = MaterialTheme.typography.titleMedium,
            fontWeight = FontWeight.SemiBold
        )
    }
}