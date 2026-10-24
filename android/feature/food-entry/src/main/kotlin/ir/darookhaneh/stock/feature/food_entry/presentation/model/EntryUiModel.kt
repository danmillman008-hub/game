package ir.darookhaneh.stock.feature.food_entry.presentation.model

import androidx.compose.runtime.Immutable
import ir.darookhaneh.stock.core.model.food.FoodItem
import ir.darookhaneh.stock.core.model.food.StorageLocation
import ir.darookhaneh.stock.core.presentation.model.CategoryUiModel
import ir.darookhaneh.stock.core.presentation.model.toFoodCategory
import ir.darookhaneh.stock.core.presentation.model.toUiModel
import java.util.UUID

@Immutable
data class EntryUiModel(
    val id: String = UUID.randomUUID().toString(),
    val name: String = "",
    val categoryUiModel: CategoryUiModel = CategoryUiModel.Uncategorized,
    val location: StorageLocation = StorageLocation.FRIDGE,
    val purchaseDate: Long = System.currentTimeMillis(),
    val expiryDate: Long? = null,
    val imageUri: String? = null,
    val notes: String = "",
)

fun FoodItem.toEntryUiModel(): EntryUiModel {
    return EntryUiModel(
        id = id,
        name = name,
        categoryUiModel = category.toUiModel(),
        location = location,
        purchaseDate = purchaseDate,
        expiryDate = expiryDate,
        imageUri = imageUri,
        notes = note
    )
}

fun EntryUiModel.toFoodItem(): FoodItem {
    return FoodItem(
        id = id,
        name = name,
        location = location,
        category = categoryUiModel.toFoodCategory(),
        categoryId = categoryUiModel.toFoodCategory()?.id,
        purchaseDate = purchaseDate,
        expiryDate = expiryDate ?: -1,
        imageUri = imageUri,
        note = notes
    )
}
