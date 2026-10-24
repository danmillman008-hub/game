package ir.darookhaneh.stock.feature.inventory.data.repository

import ir.darookhaneh.stock.core.data.mapper.toDomain
import ir.darookhaneh.stock.core.data.util.AppDispatchers
import ir.darookhaneh.stock.core.database.dao.SearchDao
import ir.darookhaneh.stock.core.model.food.FoodItem
import ir.darookhaneh.stock.core.model.food.FoodStatus
import ir.darookhaneh.stock.feature.inventory.data.mapper.toDomain
import ir.darookhaneh.stock.feature.inventory.data.mapper.toSearchHistoryEntity
import ir.darookhaneh.stock.feature.inventory.domain.model.SearchHistory
import ir.darookhaneh.stock.feature.inventory.domain.repository.SearchRepository
import ir.darookhaneh.stock.toGenericNormalized
import kotlinx.coroutines.withContext

class SearchRepositoryImp(
    private val appDispatchers: AppDispatchers,
    private val searchDao: SearchDao
) : SearchRepository {
    override suspend fun addHistoryResult(searchHistory: SearchHistory) {
        return withContext(appDispatchers.io) {
            searchDao.insertSearchHistory(searchHistory.toSearchHistoryEntity())
        }
    }

    override suspend fun getHistoryResultList(): List<SearchHistory> {
        return withContext(appDispatchers.io) {
            searchDao.getRecentSearchHistory().map { historyEntity ->
                historyEntity.toDomain()
            }
        }
    }

    override suspend fun getFoodItemListByQuery(query: String): List<FoodItem> {
        if (query.isBlank()) return emptyList()
        val normalizedQuery = query.toGenericNormalized()
        val sanitizedQuery = normalizedQuery.trim().replace(Regex("[^a-zA-Z0-9\\s]"), "")
        if (sanitizedQuery.isEmpty()) return emptyList()

        val ftsQuery = sanitizedQuery.split(Regex("\\s+"))
            .filter { it.isNotEmpty() }
            .joinToString(" ") { "$it*" }

        return withContext(appDispatchers.io) {
            searchDao.searchInventory(ftsQuery).map { foodItemEntity ->
                foodItemEntity.toDomain()
            }.filter { it.status == FoodStatus.ACTIVE }
        }
    }

}