package ir.darookhaneh.stock.feature.analytics.domain.model

import java.time.LocalDate

data class WeeklyExpiryStatistic(
    val date: LocalDate,
    val count: Int
)
