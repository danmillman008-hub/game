package ir.darookhaneh.stock.feature.analytics.presentation.viewmodel

import ir.darookhaneh.stock.core.presentation.viewmodel.UiAction

sealed interface AnalyticsAction : UiAction {
    data class OnSpoilageChartPressed(val consumed: Int, val wasted: Int) : AnalyticsAction
    data object OnSpoilageChartHide : AnalyticsAction
}
