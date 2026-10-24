package ir.darookhaneh.stock.feature.settings.mapper

import ir.darookhaneh.stock.core.database.entity.CategoryEntity
import ir.darookhaneh.stock.core.database.entity.FoodItemEntity
import ir.darookhaneh.stock.core.database.entity.FoodItemWithCategory
import ir.darookhaneh.stock.feature.settings.data.FlattenCategoryData
import ir.darookhaneh.stock.feature.settings.data.FlattenFoodData

fun FoodItemWithCategory.toFlattenFood(): FlattenFoodData {
    return FlattenFoodData(
        id = foodItem.id,
        name = foodItem.name,
        normalizedName = foodItem.normalizedName,
        categoryId = category?.id,
        location = foodItem.location,
        purchaseDate = foodItem.purchaseDate,
        expiryDate = foodItem.expiryDate,
        imageUri = foodItem.imageUri,
        notes = foodItem.notes,
        status = foodItem.status,
        resolvedDate = foodItem.resolvedDate
    )
}


fun FlattenFoodData.toFoodItemEntity(): FoodItemEntity {
    return FoodItemEntity(
        id = id,
        name = name,
        normalizedName = normalizedName,
        categoryId = categoryId,
        location = location,
        purchaseDate = purchaseDate,
        expiryDate = expiryDate,
        imageUri = imageUri,
        notes = notes,
        status = status,
        resolvedDate = resolvedDate,
    )
}

fun FlattenCategoryData.toCategoryEntity() = CategoryEntity(
    id = id,
    name = name,
    description = description
)

fun CategoryEntity.toFlattenCategoryData() = FlattenCategoryData(
    id = id,
    name = name,
    description = description
)
