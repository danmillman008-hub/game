package ir.darookhaneh.stock.core.data.repository

import ir.darookhaneh.stock.core.data.mapper.toDomain
import ir.darookhaneh.stock.core.data.mapper.toEntity
import ir.darookhaneh.stock.core.data.util.AppDispatchers
import ir.darookhaneh.stock.core.data.util.safeCall
import ir.darookhaneh.stock.core.database.TransactionRunner
import ir.darookhaneh.stock.core.database.dao.CategoryDao
import ir.darookhaneh.stock.core.database.dao.FoodDao
import ir.darookhaneh.stock.core.database.dao.SearchDao
import ir.darookhaneh.stock.core.domain.repository.FoodRepository
import ir.darookhaneh.stock.core.model.error_handling.Resource
import ir.darookhaneh.stock.core.model.food.FoodItem
import ir.darookhaneh.stock.core.model.food.FoodStatus
import ir.darookhaneh.stock.core.network.data_source.FoodRemoteDataSource
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.flowOn
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.withContext

class FoodRepositoryImpl(
    private val appDispatchers: AppDispatchers,
    private val transactionRunner: TransactionRunner,
    private val foodDao: FoodDao,
    private val categoryDao: CategoryDao,
    private val searchDao: SearchDao,
    private val foodRemoteDataSource: FoodRemoteDataSource
) : FoodRepository {
    override suspend fun scanFoodBarcode(barcodeString: String): Resource<FoodItem> {
        return safeCall(dispatcher = appDispatchers.io) {
            foodRemoteDataSource.fetchFoodApiResponse(barcodeString).toDomain()
        }
    }

    override suspend fun getAllFoodItems(): List<FoodItem> {
        return withContext(appDispatchers.io) {
            foodDao.getAllFoodItems().map { foodItemEntity ->
                foodItemEntity.toDomain()
            }
        }
    }

    override fun observeAllActiveFoodItems(): Flow<List<FoodItem>> {
        return foodDao.observeAllFoodItemsByStatus(status = FoodStatus.ACTIVE).map { entities ->
            entities.map { it.toDomain() }
        }
    }

    override fun observeAllFoodItems(): Flow<List<FoodItem>> {
        return foodDao.observeAllFoodItems().map { entities ->
            entities.map { it.toDomain() }
        }
    }

    override suspend fun updateFoodItem(item: FoodItem): Resource<Unit> {
        return safeCall(dispatcher = appDispatchers.io) {
            foodDao.updateFood(newFood = item.toEntity())
        }
    }

    override suspend fun updateFoodStatus(
        id: String,
        newStatus: FoodStatus
    ): Resource<String> {
        return safeCall(dispatcher = appDispatchers.io) {
            foodDao.updateFoodStatus(id, newStatus, System.currentTimeMillis())
            id
        }
    }

    override suspend fun updateFoodStatusList(
        ids: List<String>,
        newStatus: FoodStatus
    ): Resource<Unit> {
        return safeCall(dispatcher = appDispatchers.io) {
            foodDao.updateFoodStatusList(ids, newStatus, System.currentTimeMillis())
        }
    }

    override suspend fun getFoodById(id: String): FoodItem? {
        return foodDao.getFoodById(id)?.toDomain()
    }

    override suspend fun addFoodItem(item: FoodItem): Resource<FoodItem> {
        return safeCall(dispatcher = appDispatchers.io) {
            foodDao.insertFood(item.toEntity())
            item
        }
    }

    override suspend fun getFoodUriList(): List<String> {
        return getAllFoodItems().mapNotNull { foodItem ->
            foodItem.imageUri
        }
    }

    override fun observeFoodItemById(id: String): Flow<FoodItem> {
        return foodDao.observeFoodItem(id).map { entity -> entity.toDomain() }
    }

    override fun observeFoodItemBeforeTime(beforeTime: Long): Flow<List<FoodItem>> {
        return foodDao.observeAllFoodItemsBeforeTime(beforeTime).map { entities ->
            entities.map { it.toDomain() }
        }.flowOn(appDispatchers.io)
    }


    override suspend fun removeFoodItem(id: String) {
        foodDao.deleteFoodById(id)
    }

    override suspend fun deleteAllFoodItems(): Resource<Unit> {
        return safeCall(dispatcher = appDispatchers.io) {
            transactionRunner.run {
                categoryDao.deleteAllCategories()
                foodDao.deleteAllFoods()
                searchDao.clearAllSearchHistory()
            }
        }
    }

    override suspend fun deleteFoodAfterDay(day: Long): Resource<Unit> {
        return safeCall(dispatcher = appDispatchers.io) {
            foodDao.deleteFoodBeforeTimestamp(day)
        }
    }
}
