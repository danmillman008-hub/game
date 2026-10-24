package ir.darookhaneh.stock.widget.utils

import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.glance.material3.ColorProviders
import androidx.glance.unit.ColorProvider
import ir.darookhaneh.stock.core.designsystem.theme.onPrimaryContainerDark
import ir.darookhaneh.stock.core.designsystem.theme.onPrimaryContainerLight
import ir.darookhaneh.stock.core.designsystem.theme.onSecondaryDark
import ir.darookhaneh.stock.core.designsystem.theme.onSecondaryLight
import ir.darookhaneh.stock.core.designsystem.theme.onSurfaceDark
import ir.darookhaneh.stock.core.designsystem.theme.onSurfaceLight
import ir.darookhaneh.stock.core.designsystem.theme.primaryContainerDark
import ir.darookhaneh.stock.core.designsystem.theme.primaryContainerLight
import ir.darookhaneh.stock.core.designsystem.theme.primaryDark
import ir.darookhaneh.stock.core.designsystem.theme.primaryLight
import ir.darookhaneh.stock.core.designsystem.theme.secondaryContainerDark
import ir.darookhaneh.stock.core.designsystem.theme.secondaryContainerLight
import ir.darookhaneh.stock.core.designsystem.theme.secondaryDark
import ir.darookhaneh.stock.core.designsystem.theme.secondaryLight
import ir.darookhaneh.stock.core.designsystem.theme.surfaceDark
import ir.darookhaneh.stock.core.designsystem.theme.surfaceLight

object WidgetColorScheme {
    val colors = ColorProviders(
        light = lightColorScheme(
            primary = primaryLight, // Lấy từ Color.kt của bạn
            surface = surfaceLight,
            onSurface = onSurfaceLight,
            secondaryContainer = secondaryContainerLight,
            secondary = secondaryLight,
            onSecondary = onSecondaryLight,
            primaryContainer = primaryContainerLight,
            onPrimaryContainer = onPrimaryContainerLight
        ),
        dark = darkColorScheme(
            primary = primaryDark,
            surface = surfaceDark,
            onSurface = onSurfaceDark,
            secondaryContainer = secondaryContainerDark,
            secondary = secondaryDark,
            onSecondary = onSecondaryDark,
            primaryContainer = primaryContainerDark,
            onPrimaryContainer = onPrimaryContainerDark
        )
    )
}

enum class WidgetColors {
    BACKGROUND, ON_BACKGROUND,
    LIST_ITEM_BACKGROUND, LIST_ITEM_CONTENT,
}

@Composable
fun WidgetColors.toColorProvider(): ColorProvider {
    WidgetColorScheme.colors.run {
        return when (this@toColorProvider) {
            WidgetColors.BACKGROUND -> secondary
            WidgetColors.ON_BACKGROUND -> onSecondary
            WidgetColors.LIST_ITEM_BACKGROUND -> secondaryContainer
            WidgetColors.LIST_ITEM_CONTENT -> secondary

        }
    }
}