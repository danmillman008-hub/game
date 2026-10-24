package ir.darookhaneh.stock.core.notifications.domain.usecase

import ir.darookhaneh.stock.core.domain.repository.FoodRepository
import ir.darookhaneh.stock.core.model.food.FoodStatus
import java.time.DayOfWeek
import java.time.LocalDate
import java.time.ZoneId

class GetWeeklySummaryUseCase(
    private val foodRepository: FoodRepository
) {
    suspend operator fun invoke(): Pair<Int, Int> {
        val allFoods = foodRepository.getAllFoodItems()
        val startOfWeek = LocalDate.now()
            .with(DayOfWeek.MONDAY)
            .atStartOfDay(ZoneId.systemDefault())
            .toInstant()
            .toEpochMilli()

        val weeklyResolvedFoods = allFoods.filter { food ->
            val resolvedAt = food.resolvedDate ?: 0L
            resolvedAt >= startOfWeek
        }

        val consumedInWeek = weeklyResolvedFoods.count { it.status == FoodStatus.CONSUMED }
        val wastedInWeek = weeklyResolvedFoods.count { it.status == FoodStatus.WASTED }

        return Pair(consumedInWeek, wastedInWeek)
    }
}
