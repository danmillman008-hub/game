package ir.darookhaneh.stock.feature.inventory.domain.repository

import ir.darookhaneh.stock.core.model.food.FoodItem
import ir.darookhaneh.stock.feature.inventory.domain.model.SearchHistory

interface SearchRepository {
    suspend fun addHistoryResult(searchHistory: SearchHistory)
    suspend fun getHistoryResultList(): List<SearchHistory>
    suspend fun getFoodItemListByQuery(query: String): List<FoodItem>
}