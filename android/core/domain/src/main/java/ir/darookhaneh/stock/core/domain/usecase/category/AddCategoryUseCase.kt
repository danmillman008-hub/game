package ir.darookhaneh.stock.core.domain.usecase.category

import ir.darookhaneh.stock.core.domain.repository.CategoryRepository
import ir.darookhaneh.stock.core.model.food.FoodCategory

class AddCategoryUseCase(
    private val categoryRepository: CategoryRepository
) {
    suspend operator fun invoke(name: String): FoodCategory {
        val newCategory = FoodCategory(name = name)
        categoryRepository.addCategory(newCategory)
        return newCategory
    }
}