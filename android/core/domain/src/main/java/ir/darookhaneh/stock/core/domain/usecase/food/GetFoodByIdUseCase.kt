package ir.darookhaneh.stock.core.domain.usecase.food

import ir.darookhaneh.stock.core.domain.repository.FoodRepository
import ir.darookhaneh.stock.core.model.food.FoodItem

class GetFoodByIdUseCase(
    private val foodRepository: FoodRepository
) {
    suspend operator fun invoke(id: String): FoodItem? {
        return foodRepository.getFoodById(id)
    }
}