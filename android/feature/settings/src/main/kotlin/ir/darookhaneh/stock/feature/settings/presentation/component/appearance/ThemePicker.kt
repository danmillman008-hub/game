package ir.darookhaneh.stock.feature.settings.presentation.component.appearance

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.material3.ExperimentalMaterial3ExpressiveApi
import androidx.compose.material3.MaterialTheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import ir.darookhaneh.stock.core.designsystem.component.AppFilterButton
import ir.darookhaneh.stock.core.designsystem.icon.StockIcons
import ir.darookhaneh.stock.core.designsystem.icon.toImageVector
import ir.darookhaneh.stock.core.model.setting.ThemeMode
import ir.darookhaneh.stock.core.presentation.R
import ir.darookhaneh.stock.core.presentation.utils.ItemPosition
import ir.darookhaneh.stock.core.presentation.utils.animatedHorizontalShape
import ir.darookhaneh.stock.core.presentation.utils.toItemPosition
import ir.darookhaneh.stock.core.presentation.utils.toVerticalSegmentedShape
import ir.darookhaneh.stock.feature.settings.presentation.component.ListItemContent
import ir.darookhaneh.stock.feature.settings.utils.toStringRes

@OptIn(ExperimentalMaterial3ExpressiveApi::class)
@Composable
fun ThemePicker(
    itemPosition: ItemPosition,
    themeMode: ThemeMode,
    onThemeModeChange: (ThemeMode) -> Unit
) {
    val stockIcons = StockIcons.Settings
    val icon = when (themeMode) {
        ThemeMode.LIGHT -> stockIcons.LightTheme
        ThemeMode.DARK -> stockIcons.DarkTheme
        ThemeMode.SYSTEM -> stockIcons.SystemTheme
    }

    val entries = ThemeMode.entries

    ListItemContent(
        title = stringResource(R.string.setting_app_theme),
        modifier = Modifier.fillMaxWidth(),
        icon = icon.toImageVector(),
        shape = itemPosition.toVerticalSegmentedShape(),
    ) {
        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.spacedBy(4.dp)
        ) {
            entries.forEachIndexed { index, mode ->
                val itemPosition = index.toItemPosition(entries.size)
                val selected = themeMode == mode
                AppFilterButton(
                    modifier = Modifier.weight(1f),
                    label = stringResource(mode.toStringRes()),
                    selected = selected,
                    onClick = { onThemeModeChange(mode) },
                    shape = itemPosition.animatedHorizontalShape(selected = selected),
                    disabledContainerColor = MaterialTheme.colorScheme.surface,
                    disabledContentColor = MaterialTheme.colorScheme.onSurface,
                    activeContainerColor = MaterialTheme.colorScheme.primary,
                    activeContentColor = MaterialTheme.colorScheme.onPrimary
                )
            }
        }
    }
}