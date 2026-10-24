package ir.darookhaneh.stock.widget.usecase

import ir.darookhaneh.stock.core.domain.repository.FoodRepository
import ir.darookhaneh.stock.core.model.food.FoodItem
import ir.darookhaneh.stock.core.model.food.FoodStatus
import ir.darookhaneh.stock.toLocalDate
import java.time.DayOfWeek
import java.time.LocalDate

class GetFoodsUseCase(
    private val foodRepository: FoodRepository
) {

    suspend operator fun invoke(): List<FoodItem> {
        return foodRepository.getAllFoodItems()
    }

    suspend fun getThisWeek(): List<FoodItem> {
        val today = LocalDate.now()
        val startOfWeek = today.with(DayOfWeek.MONDAY)
        val endOfWeek = today.with(DayOfWeek.SUNDAY)

        return foodRepository.getAllFoodItems()
            .filter { food ->
                food.expiryDate.toLocalDate() in startOfWeek..endOfWeek && food.status == FoodStatus.ACTIVE
            }
            .sortedBy { it.expiryDate }
    }
}