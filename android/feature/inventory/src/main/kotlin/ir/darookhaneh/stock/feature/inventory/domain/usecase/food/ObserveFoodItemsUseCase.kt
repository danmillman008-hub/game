package ir.darookhaneh.stock.feature.inventory.domain.usecase.food

import ir.darookhaneh.stock.core.domain.repository.FoodRepository
import ir.darookhaneh.stock.core.model.food.FoodItem
import kotlinx.coroutines.flow.Flow

class ObserveFoodItemsUseCase(
    private val foodRepository: FoodRepository
) {
    operator fun invoke(): Flow<List<FoodItem>> {
        return foodRepository.observeAllActiveFoodItems()
    }
}