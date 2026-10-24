package ir.darookhaneh.stock.widget.total_food.component

import androidx.compose.runtime.Composable
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.times
import androidx.glance.ColorFilter
import androidx.glance.GlanceModifier
import androidx.glance.ImageProvider
import androidx.glance.background
import androidx.glance.layout.Alignment
import androidx.glance.layout.Column
import androidx.glance.layout.height
import androidx.glance.layout.padding
import androidx.glance.layout.width
import androidx.glance.text.Text
import ir.darookhaneh.stock.R
import ir.darookhaneh.stock.core.model.food.Freshness
import ir.darookhaneh.stock.widget.total_food.utils.TotalFoodWidgetUtils
import ir.darookhaneh.stock.widget.total_food.utils.toColor
import ir.darookhaneh.stock.widget.total_food.utils.toContainerColor
import ir.darookhaneh.stock.widget.utils.WidgetTypography

@Composable
fun TotalFoodItem(
    freshness: Freshness,
    value: Int,
    percent: Float,
) {
    val maxHeight = 160.dp
    val safeHeight = (percent * maxHeight)
        .coerceAtLeast(TotalFoodWidgetUtils.MIN_HEIGHT)


    Column(
        modifier = GlanceModifier
            .height(safeHeight)
            .width(24.dp)
            .background(
                imageProvider = ImageProvider(resId = R.drawable.total_food_item_shape),
                colorFilter = ColorFilter.tint(freshness.toContainerColor())
            )
            .padding(vertical = 4.dp, horizontal = 4.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalAlignment = Alignment.Top
    ) {
        Text(
            text = "$value",
            style = WidgetTypography.label.copy(
                color = freshness.toColor()
            )
        )
    }
}