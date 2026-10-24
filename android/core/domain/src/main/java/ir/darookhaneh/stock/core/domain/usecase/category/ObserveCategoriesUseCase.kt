package ir.darookhaneh.stock.core.domain.usecase.category

import ir.darookhaneh.stock.core.domain.repository.CategoryRepository
import ir.darookhaneh.stock.core.model.food.FoodCategory
import kotlinx.coroutines.flow.Flow

class ObserveCategoriesUseCase(
    private val categoryRepository: CategoryRepository
) {
    operator fun invoke(): Flow<List<FoodCategory>> {
        return categoryRepository.observeAllCategories()
    }
}