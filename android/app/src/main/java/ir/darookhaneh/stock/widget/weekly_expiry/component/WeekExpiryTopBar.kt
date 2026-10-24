package ir.darookhaneh.stock.widget.weekly_expiry.component

import androidx.compose.runtime.Composable
import androidx.compose.ui.unit.dp
import androidx.glance.ColorFilter
import androidx.glance.GlanceModifier
import androidx.glance.Image
import androidx.glance.ImageProvider
import androidx.glance.LocalContext
import androidx.glance.action.clickable
import androidx.glance.appwidget.action.actionRunCallback
import androidx.glance.appwidget.components.TitleBar
import androidx.glance.layout.padding
import ir.darookhaneh.stock.core.designsystem.icon.StockIcons
import ir.darookhaneh.stock.core.presentation.R
import ir.darookhaneh.stock.widget.utils.WidgetColors
import ir.darookhaneh.stock.widget.utils.toColorProvider
import ir.darookhaneh.stock.widget.weekly_expiry.RefreshWeeklyExpiryWidget

@Composable
fun WeeklyExpirySmallTopBar(
    modifier: GlanceModifier
) {
    TitleBar(
        modifier = modifier,
        startIcon = ImageProvider(StockIcons.Widget.WeekExpiryIcon.id),
        title = LocalContext.current.getString(R.string.widget_weekly_food_title),
        iconColor = WidgetColors.ON_BACKGROUND.toColorProvider(),
        textColor = WidgetColors.ON_BACKGROUND.toColorProvider(),
    )
}

@Composable
fun WeeklyExpiryMediumTopBar(
    modifier: GlanceModifier = GlanceModifier
) {
    TitleBar(
        modifier = modifier.padding(end = 12.dp),
        startIcon = ImageProvider(StockIcons.Widget.WeekExpiryIcon.id),
        title = LocalContext.current.getString(R.string.widget_weekly_food_title),
        iconColor = WidgetColors.ON_BACKGROUND.toColorProvider(),
        textColor = WidgetColors.ON_BACKGROUND.toColorProvider(),
    ) {
        Image(
            modifier = GlanceModifier.clickable(
                onClick = actionRunCallback<RefreshWeeklyExpiryWidget>()
            ),
            provider = ImageProvider(StockIcons.Widget.RefreshData.id),
            contentDescription = null,
            colorFilter = ColorFilter.tint(WidgetColors.ON_BACKGROUND.toColorProvider())
        )
    }
}

@Composable
fun WeeklyExpiryLargeTopBar(
    modifier: GlanceModifier = GlanceModifier
) {
    TitleBar(
        modifier = modifier.padding(end = 12.dp),
        startIcon = ImageProvider(StockIcons.Widget.WeekExpiryIcon.id),
        title = LocalContext.current.getString(R.string.widget_weekly_food_title),
        iconColor = WidgetColors.ON_BACKGROUND.toColorProvider(),
        textColor = WidgetColors.ON_BACKGROUND.toColorProvider(),
    ) {
        Image(
            provider = ImageProvider(StockIcons.Widget.RefreshData.id),
            contentDescription = null,
            colorFilter = ColorFilter.tint(WidgetColors.ON_BACKGROUND.toColorProvider())
        )
    }
}
