package ir.darookhaneh.stock.feature.analytics.data.repository

import ir.darookhaneh.stock.core.domain.repository.FoodRepository
import ir.darookhaneh.stock.core.model.food.FoodItem
import ir.darookhaneh.stock.feature.analytics.domain.repository.FoodAnalyticsRepository
import kotlinx.coroutines.flow.Flow

class FoodAnalyticsRepositoryImpl(
    private val foodRepository: FoodRepository,
) : FoodAnalyticsRepository {

    override fun observeAllFoodItems(): Flow<List<FoodItem>> {
        return foodRepository.observeAllFoodItems()
    }
}
