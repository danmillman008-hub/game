package ir.darookhaneh.stock.feature.analytics.presentation.viewmodel

import androidx.compose.runtime.Immutable
import ir.darookhaneh.stock.core.presentation.viewmodel.UiState
import ir.darookhaneh.stock.feature.analytics.domain.model.AnalyticsPeriod
import ir.darookhaneh.stock.feature.analytics.domain.model.FreshnessStatistic
import ir.darookhaneh.stock.feature.analytics.presentation.model.SpoilagePointUiModel
import ir.darookhaneh.stock.feature.analytics.presentation.model.WeeklyExpiryStatisticUiModel

@Immutable
data class AnalyticsUiState(
    val period: AnalyticsPeriod = AnalyticsPeriod.WEEK,
    val expiryCount: Int = 0,
    val expiringSoon: Int = 0,
    val spoilageStatisticByMonth: List<SpoilagePointUiModel> = emptyList(),
    val freshnessStatisticByMonth: FreshnessStatistic = FreshnessStatistic(),
    val weeklyExpiryStatistic: List<WeeklyExpiryStatisticUiModel> = emptyList(),

    //
    val consumedValue: Int = 0,
    val wastedValue: Int = 0,
) : UiState