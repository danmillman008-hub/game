package ir.darookhaneh.stock.core.data.mapper

import ir.darookhaneh.stock.core.database.entity.FoodItemEntity
import ir.darookhaneh.stock.core.database.entity.FoodItemWithCategory
import ir.darookhaneh.stock.core.model.food.FoodItem
import ir.darookhaneh.stock.core.model.food.StorageLocation
import ir.darookhaneh.stock.core.network.model.FoodApiResponse
import ir.darookhaneh.stock.toGenericNormalized
import java.util.UUID


fun FoodApiResponse.toDomain() = FoodItem(
    id = UUID.randomUUID().toString(),
    name = product?.productName.orEmpty(),
    categoryId = null,
    location = StorageLocation.OTHER,
    purchaseDate = System.currentTimeMillis(),
    expiryDate = -1,
    imageUri = product?.imageUrl,
    note = ""
)

fun FoodItemEntity.toDomain() = FoodItem(
    id = id,
    name = name,
    categoryId = categoryId,
    location = location,
    purchaseDate = purchaseDate,
    expiryDate = expiryDate,
    imageUri = imageUri,
    note = notes,
    status = status,
    resolvedDate = resolvedDate
)

fun FoodItemWithCategory.toDomain() = FoodItem(
    id = foodItem.id,
    name = foodItem.name,
    categoryId = foodItem.categoryId,
    location = foodItem.location,
    purchaseDate = foodItem.purchaseDate,
    expiryDate = foodItem.expiryDate,
    imageUri = foodItem.imageUri,
    note = foodItem.notes,
    status = foodItem.status,
    resolvedDate = foodItem.resolvedDate,
    category = category?.toDomain()
)

fun FoodItem.toEntity() = FoodItemEntity(
    id = id,
    name = name,
    normalizedName = name.toGenericNormalized(),
    categoryId = categoryId?.ifBlank { null },
    location = location,
    purchaseDate = purchaseDate,
    expiryDate = expiryDate,
    imageUri = imageUri,
    notes = note,
    status = status,
    resolvedDate = resolvedDate
)
