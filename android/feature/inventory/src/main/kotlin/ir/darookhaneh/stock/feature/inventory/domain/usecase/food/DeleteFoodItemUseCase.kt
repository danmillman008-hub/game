package ir.darookhaneh.stock.feature.inventory.domain.usecase.food

import ir.darookhaneh.stock.core.domain.repository.FoodRepository

class DeleteFoodItemUseCase(
    private val foodRepository: FoodRepository
) {
    suspend operator fun invoke(id: String) {
        return foodRepository.removeFoodItem(id)
    }
}