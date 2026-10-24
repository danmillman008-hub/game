package ir.darookhaneh.stock.core.data.mapper

import ir.darookhaneh.stock.core.database.entity.CategoryEntity
import ir.darookhaneh.stock.core.model.food.FoodCategory

fun CategoryEntity.toDomain(): FoodCategory {
    return FoodCategory(
        id = id,
        name = name,
        description = description
    )
}

fun FoodCategory.toEntity(): CategoryEntity {
    return CategoryEntity(
        id = id,
        name = name,
        description = description
    )
}
