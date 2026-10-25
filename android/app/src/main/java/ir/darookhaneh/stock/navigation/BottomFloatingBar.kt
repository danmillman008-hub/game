@file:OptIn(ExperimentalMaterial3ExpressiveApi::class)

package ir.darookhaneh.stock.navigation

import androidx.annotation.StringRes
import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.animateContentSize
import androidx.compose.animation.expandHorizontally
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.animation.shrinkHorizontally
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.ExperimentalMaterial3ExpressiveApi
import androidx.compose.material3.FloatingToolbarDefaults
import androidx.compose.material3.HorizontalFloatingToolbar
import androidx.compose.material3.Icon
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.navigation3.runtime.NavKey
import ir.darookhaneh.stock.core.designsystem.icon.StockIcons
import ir.darookhaneh.stock.core.designsystem.icon.IconProvider
import ir.darookhaneh.stock.core.designsystem.icon.toImageVector
import ir.darookhaneh.stock.core.presentation.R
import ir.darookhaneh.stock.core.presentation.navigation.Destination
import ir.darookhaneh.stock.core.presentation.navigation.SettingDestination

enum class BottomBarItem(
    @field:StringRes val label: Int,
    val selectedIcon: IconProvider,
    val unselectedIcon: IconProvider
) {
    DASHBOARD(
        label = R.string.nav_dashboard,
        selectedIcon = StockIcons.BottomBar.SelectedDashboard,
        unselectedIcon = StockIcons.BottomBar.UnselectedDashboard
    ),

    DRUGS(
        label = R.string.nav_drugs,
        selectedIcon = StockIcons.BottomBar.SelectedDrugs,
        unselectedIcon = StockIcons.BottomBar.UnselectedDrugs
    ),

    HISTORY(
        label = R.string.nav_history,
        selectedIcon = StockIcons.BottomBar.SelectedHistory,
        unselectedIcon = StockIcons.BottomBar.UnselectedHistory
    ),

    SCAN(
        label = R.string.nav_scan,
        selectedIcon = StockIcons.BottomBar.SelectedScan,
        unselectedIcon = StockIcons.BottomBar.UnselectedScan
    ),

    SETTINGS(
        label = R.string.nav_settings,
        selectedIcon = StockIcons.BottomBar.SelectedSettings,
        unselectedIcon = StockIcons.BottomBar.UnselectedSettings
    )
}

fun NavKey.toBottomBarItem(): BottomBarItem? {
    return when (this) {
        Destination.Dashboard, is Destination.DrugDetail -> BottomBarItem.DASHBOARD
        Destination.Drugs -> BottomBarItem.DRUGS
        Destination.History -> BottomBarItem.HISTORY
        Destination.Record -> BottomBarItem.DRUGS
        Destination.Scanner -> BottomBarItem.SCAN
        is Destination.Setting -> BottomBarItem.SETTINGS
        else -> null
    }
}

fun hideBottomBar(currentDestination: NavKey?): Boolean {
    return when (currentDestination) {
        is Destination.Scanner -> true
        else -> false
    }
}

fun BottomBarItem.toDestination(): Destination {
    return when (this) {
        BottomBarItem.DASHBOARD -> Destination.Dashboard
        BottomBarItem.DRUGS -> Destination.Drugs
        BottomBarItem.HISTORY -> Destination.History
        BottomBarItem.SCAN -> Destination.Scanner
        BottomBarItem.SETTINGS -> Destination.Setting(destination = SettingDestination.Main)
    }
}

@Composable
fun BottomFloatingBar(
    selectedBottomBarItem: BottomBarItem,
    onBottomBarClick: (item: BottomBarItem) -> Unit,
    modifier: Modifier = Modifier,
) {
    val scheme = MaterialTheme.colorScheme
    HorizontalFloatingToolbar(
        modifier = modifier,
        expanded = true,
        colors = FloatingToolbarDefaults.vibrantFloatingToolbarColors(
            toolbarContainerColor = scheme.primary,
        ),
    ) {
        BottomBarItem.entries.forEach { bottomBarItem ->
            ToolBarIcon(
                selectedIcon = bottomBarItem.selectedIcon.toImageVector(),
                label = stringResource(bottomBarItem.label),
                unselectedIcon = bottomBarItem.unselectedIcon.toImageVector(),
                selected = bottomBarItem == selectedBottomBarItem,
                onClick = { onBottomBarClick(bottomBarItem) }
            )
        }
    }
}

@Composable
private fun ToolBarIcon(
    modifier: Modifier = Modifier,
    selectedIcon: ImageVector,
    label: String,
    unselectedContentColor: Color = MaterialTheme.colorScheme.onPrimary,
    unselectedContainerColor: Color = MaterialTheme.colorScheme.primary,
    selectedContentColor: Color = MaterialTheme.colorScheme.onPrimaryContainer,
    selectedContainerColor: Color = MaterialTheme.colorScheme.primaryContainer,
    unselectedIcon: ImageVector,
    selected: Boolean,
    onClick: () -> Unit
) {
    Surface(
        onClick = onClick,
        modifier = modifier.animateContentSize(),
        shape = RoundedCornerShape(32.dp),
        color = if (selected) selectedContainerColor else unselectedContainerColor
    ) {
        Row(
            modifier = Modifier.padding(16.dp),
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            Icon(
                imageVector = if (selected) selectedIcon else unselectedIcon,
                contentDescription = null,
                tint = if (selected) selectedContentColor else unselectedContentColor,
                modifier = Modifier.size(24.dp)
            )
            AnimatedVisibility(
                visible = selected,
                enter = expandHorizontally(
                    animationSpec = MaterialTheme.motionScheme.fastSpatialSpec()
                ) + fadeIn(),
                exit = shrinkHorizontally(
                    animationSpec = MaterialTheme.motionScheme.fastSpatialSpec()
                ) + fadeOut()
            ) {
                Text(
                    text = label,
                    color = selectedContentColor,
                    style = MaterialTheme.typography.bodyLarge.copy(fontWeight = FontWeight.Medium)
                )
            }

        }
    }
}