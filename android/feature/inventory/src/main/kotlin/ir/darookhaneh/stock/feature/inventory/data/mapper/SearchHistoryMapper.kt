package ir.darookhaneh.stock.feature.inventory.data.mapper

import ir.darookhaneh.stock.core.database.entity.SearchHistoryEntity
import ir.darookhaneh.stock.feature.inventory.domain.model.SearchHistory

fun SearchHistoryEntity.toDomain() = SearchHistory(
    id = id,
    name = query,
    timeStamp = timestamp
)

fun SearchHistory.toSearchHistoryEntity() = SearchHistoryEntity(
    query = name
)