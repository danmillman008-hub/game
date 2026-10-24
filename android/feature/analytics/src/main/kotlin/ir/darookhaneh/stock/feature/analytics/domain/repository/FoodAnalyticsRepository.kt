package ir.darookhaneh.stock.feature.analytics.domain.repository

import ir.darookhaneh.stock.core.model.food.FoodItem
import kotlinx.coroutines.flow.Flow

interface FoodAnalyticsRepository {
    fun observeAllFoodItems(): Flow<List<FoodItem>>
}
