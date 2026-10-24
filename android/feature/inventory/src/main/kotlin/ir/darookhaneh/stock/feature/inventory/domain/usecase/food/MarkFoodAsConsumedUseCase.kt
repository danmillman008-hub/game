package ir.darookhaneh.stock.feature.inventory.domain.usecase.food

import ir.darookhaneh.stock.core.domain.repository.FoodRepository
import ir.darookhaneh.stock.core.model.food.FoodStatus

class MarkFoodAsConsumedUseCase(
    private val foodRepository: FoodRepository
) {
    suspend operator fun invoke(foodId: String) {
        foodRepository.updateFoodStatus(id = foodId, newStatus = FoodStatus.CONSUMED)
    }

    suspend fun executeWithList(foodIds: List<String>) {
        foodRepository.updateFoodStatusList(ids = foodIds, newStatus = FoodStatus.CONSUMED)
    }
}
