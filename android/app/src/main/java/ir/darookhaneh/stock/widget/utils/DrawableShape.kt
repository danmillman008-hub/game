package ir.darookhaneh.stock.widget.utils

import androidx.annotation.DrawableRes
import ir.darookhaneh.stock.R
import ir.darookhaneh.stock.core.presentation.utils.ItemPosition

@DrawableRes
fun ItemPosition.toVerticalDrawable(): Int {
    return when (this) {
        ItemPosition.TOP -> R.drawable.item_start_shape
        ItemPosition.MIDDLE -> R.drawable.item_middle_shape
        ItemPosition.SINGLE -> R.drawable.item_single_shape
        ItemPosition.BOTTOM -> R.drawable.item_bottom_shape
    }
}