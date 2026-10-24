package ir.darookhaneh.stock.core.domain.usecase.category

import ir.darookhaneh.stock.core.domain.repository.CategoryRepository
import ir.darookhaneh.stock.core.model.food.FoodCategory

class EditCategoryUseCase(
    private val categoryRepository: CategoryRepository
) {
    suspend operator fun invoke(category: FoodCategory){
        categoryRepository.updateCategory(category = category)
    }
}