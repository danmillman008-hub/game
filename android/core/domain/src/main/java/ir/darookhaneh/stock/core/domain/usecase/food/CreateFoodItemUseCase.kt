package ir.darookhaneh.stock.core.domain.usecase.food

import ir.darookhaneh.stock.core.domain.repository.FoodRepository
import ir.darookhaneh.stock.core.domain.repository.LocalMediaStorage
import ir.darookhaneh.stock.core.model.error_handling.Resource
import ir.darookhaneh.stock.core.model.error_handling.getDataOrNull
import ir.darookhaneh.stock.core.model.food.FoodItem

class CreateFoodItemUseCase(
    private val foodRepository: FoodRepository,
    private val localMediaStorage: LocalMediaStorage,
) {
    suspend operator fun invoke(
        foodItem: FoodItem
    ): Resource<FoodItem> {
        val itemToSave = foodItem.imageUri?.let { uri ->
            val newUri = localMediaStorage.copyImageToInternalStorage(uri).getDataOrNull()
            foodItem.copy(imageUri = newUri)
        } ?: foodItem

        return foodRepository.addFoodItem(itemToSave)
    }
}