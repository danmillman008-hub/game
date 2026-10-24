package ir.darookhaneh.stock.feature.food_entry.domain.usecase

import ir.darookhaneh.stock.core.data.util.getDataOrNull
import ir.darookhaneh.stock.core.domain.repository.CategoryRepository
import ir.darookhaneh.stock.core.domain.repository.FoodRepository
import ir.darookhaneh.stock.core.domain.repository.LocalMediaStorage
import ir.darookhaneh.stock.core.model.food.FoodCategory
import ir.darookhaneh.stock.core.model.food.FoodItem
import kotlinx.coroutines.flow.Flow

class ObserveCategoriesUseCase(
    private val categoryRepository: CategoryRepository
) {
    operator fun invoke(): Flow<List<FoodCategory>> = categoryRepository.observeAllCategories()
}

class GetCategoriesUseCase(
    private val categoryRepository: CategoryRepository
) {
    suspend operator fun invoke(): List<FoodCategory> = categoryRepository.getAllCategories()
}

class AddCategoryUseCase(
    private val categoryRepository: CategoryRepository
) {
    suspend operator fun invoke(category: FoodCategory) = categoryRepository.addCategory(category)

    suspend fun getCurrentCategory(categoryId: String): FoodCategory? {
        return categoryRepository.getCategoryById(categoryId)
    }
}

class SaveFoodItemUseCase(
    private val foodRepository: FoodRepository,
    private val localMediaStorage: LocalMediaStorage
) {
    suspend operator fun invoke(foodItem: FoodItem) {
        val newUri = foodItem.imageUri?.let {
            localMediaStorage.copyImageToInternalStorage(uriPath = it).getDataOrNull()
                ?: foodItem.imageUri
        } ?: foodItem.imageUri


        if (foodRepository.getFoodById(foodItem.id) != null) {
            foodRepository.updateFoodItem(
                foodItem.copy(
                    imageUri = newUri
                )
            )
        } else {
            foodRepository.addFoodItem(
                foodItem.copy(
                    imageUri = newUri
                )
            )
        }
    }
}
