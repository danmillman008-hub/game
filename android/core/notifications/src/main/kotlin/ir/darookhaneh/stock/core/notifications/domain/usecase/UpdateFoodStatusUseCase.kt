package ir.darookhaneh.stock.core.notifications.domain.usecase

import ir.darookhaneh.stock.core.domain.repository.FoodRepository
import ir.darookhaneh.stock.core.model.food.FoodStatus

class UpdateFoodStatusUseCase(
    private val foodRepository: FoodRepository
) {
    suspend operator fun invoke(foodId: String, status: FoodStatus) {
        foodRepository.updateFoodStatus(foodId, status)
    }
}
