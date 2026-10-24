package ir.darookhaneh.stock.core.domain.repository

import ir.darookhaneh.stock.core.model.food.FoodCategory
import kotlinx.coroutines.flow.Flow

interface CategoryRepository {
    suspend fun getAllCategories(): List<FoodCategory>
    fun observeAllCategories(): Flow<List<FoodCategory>>
    suspend fun addCategory(category: FoodCategory)
    suspend fun updateCategory(category: FoodCategory)
    suspend fun deleteCategory(id: String)
    suspend fun getCategoryById(id: String): FoodCategory?
}
