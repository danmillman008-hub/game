package ir.darookhaneh.stock.widget.total_food.component

import androidx.compose.runtime.Composable
import androidx.glance.ImageProvider
import androidx.glance.LocalContext
import androidx.glance.appwidget.components.TitleBar
import ir.darookhaneh.stock.core.designsystem.icon.StockIcons
import ir.darookhaneh.stock.widget.utils.WidgetColors
import ir.darookhaneh.stock.widget.utils.toColorProvider

@Composable
fun TotalFoodTopBar() {
    TitleBar(
        startIcon = ImageProvider(StockIcons.Widget.TotalFood.id),
        title = LocalContext.current.getString(ir.darookhaneh.stock.core.presentation.R.string.widget_weekly_freshness_title),
        iconColor = WidgetColors.ON_BACKGROUND.toColorProvider(),
        textColor = WidgetColors.ON_BACKGROUND.toColorProvider(),
    )
}


/*
fun TotalFoodMediumTopBar(){
    TitleBar(
        startIcon = ImageProvider(StockIcons.Widget.TotalFood.id),
        title = "Total Food",
        textColor = WidgetColors.ON_BACKGROUND.toColorProvider(),
        iconColor = WidgetColors.ON_BACKGROUND.toColorProvider()
    )
}

@Composable
fun TotalFoodLargeTopBar(){
    TitleBar(
        startIcon = ImageProvider(StockIcons.Widget.TotalFood.id),
        title = "Total Food",
        textColor = WidgetColors.ON_BACKGROUND.toColorProvider(),
        iconColor = WidgetColors.ON_BACKGROUND.toColorProvider()
    )
}*/
