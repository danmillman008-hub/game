package ir.darookhaneh.stock.core.data.repository

import ir.darookhaneh.stock.core.data.util.AppDispatchers
import ir.darookhaneh.stock.core.database.dao.FoodDao
import ir.darookhaneh.stock.core.database.entity.FoodItemEntity
import ir.darookhaneh.stock.core.model.food.FoodItem
import ir.darookhaneh.stock.core.model.food.StorageLocation
import ir.darookhaneh.stock.core.network.data_source.FoodRemoteDataSource
import ir.darookhaneh.stock.toGenericNormalized
import io.mockk.coEvery
import io.mockk.coVerify
import io.mockk.every
import io.mockk.mockk
import io.mockk.mockkStatic
import io.mockk.unmockkAll
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.test.runTest
import org.junit.Assert.assertEquals
import org.junit.Before
import org.junit.Test

class FoodRepositoryImplTest {

    private lateinit var foodDao: FoodDao
    private lateinit var foodRemoteDataSource: FoodRemoteDataSource
    private lateinit var appDispatchers: AppDispatchers
    private lateinit var repository: FoodRepositoryImpl

    @Before
    fun setUp() {
        mockkStatic("ir.darookhaneh.stock.StringExtKt")
        every { any<String>().toGenericNormalized() } answers { firstArg() }

        foodDao = mockk()
        foodRemoteDataSource = mockk()
        appDispatchers = object : AppDispatchers {
            override val io = Dispatchers.Unconfined
            override val main = Dispatchers.Unconfined
        }
        repository = FoodRepositoryImpl(appDispatchers, foodDao, foodRemoteDataSource)
    }

    @org.junit.After
    fun tearDown() {
        unmockkAll()
    }

    @Test
    fun `getFoodById should call dao and return domain model`() = runTest {
        val foodId = "1"
        val entity = FoodItemEntity(
            id = foodId,
            name = "Milk",
            normalizedName = "milk",
            categoryId = "dairy",
            location = StorageLocation.FRIDGE,
            purchaseDate = 1000L,
            expiryDate = 2000L,
            imageUri = "uri",
            notes = ""
        )
        coEvery { foodDao.getFoodById(foodId) } returns entity

        val result = repository.getFoodById(foodId)

        assertEquals("Milk", result?.name)
        coVerify(exactly = 1) { foodDao.getFoodById(foodId) }
    }

    @Test
    fun `addFoodItem should call dao insert`() = runTest {
        val foodItem = FoodItem(id = "1", name = "Apple")
        coEvery { foodDao.insertFood(any()) } returns Unit

        repository.addFoodItem(foodItem)

        coVerify(exactly = 1) { foodDao.insertFood(any()) }
    }
}
