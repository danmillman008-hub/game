package ir.darookhaneh.stock.core.domain.usecase.category

import ir.darookhaneh.stock.core.domain.repository.CategoryRepository

class DeleteCategoryUseCase(
    private val categoryRepository: CategoryRepository
) {
    suspend operator fun invoke(categoryId: String){
        categoryRepository.deleteCategory(categoryId)
    }
}