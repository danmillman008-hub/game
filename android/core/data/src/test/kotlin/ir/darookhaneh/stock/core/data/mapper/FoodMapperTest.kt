package ir.darookhaneh.stock.core.data.mapper

import ir.darookhaneh.stock.core.database.entity.FoodItemEntity
import ir.darookhaneh.stock.core.model.food.FoodItem
import ir.darookhaneh.stock.core.model.food.FoodStatus
import ir.darookhaneh.stock.core.model.food.StorageLocation
import ir.darookhaneh.stock.toGenericNormalized
import io.mockk.every
import io.mockk.mockkStatic
import io.mockk.unmockkAll
import org.junit.Assert.assertEquals
import org.junit.Before
import org.junit.Test

class FoodMapperTest {

    @Before
    fun setUp() {
        mockkStatic("ir.darookhaneh.stock.StringExtKt")
        every { any<String>().toGenericNormalized() } answers { firstArg() }
    }

    @org.junit.After
    fun tearDown() {
        unmockkAll()
    }

    @Test
    fun `toDomain should correctly map entity to domain model`() {
        val entity = FoodItemEntity(
            id = "1",
            name = "Milk",
            normalizedName = "milk",
            categoryId = "dairy",
            location = StorageLocation.FRIDGE,
            purchaseDate = 1000L,
            expiryDate = 2000L,
            imageUri = "uri",
            notes = "note",
            status = FoodStatus.ACTIVE,
            resolvedDate = null
        )

        val domain = entity.toDomain()

        assertEquals(entity.id, domain.id)
        assertEquals(entity.name, domain.name)
        assertEquals(entity.location, domain.location)
        assertEquals(entity.purchaseDate, domain.purchaseDate)
        assertEquals(entity.expiryDate, domain.expiryDate)
        assertEquals(entity.imageUri, domain.imageUri)
        assertEquals(entity.notes, domain.note)
        assertEquals(entity.status, domain.status)
    }

    @Test
    fun `toEntity should correctly map domain to entity model`() {
        val domain = FoodItem(
            id = "1",
            name = "Milk",
            categoryId = "dairy",
            location = StorageLocation.FRIDGE,
            purchaseDate = 1000L,
            expiryDate = 2000L,
            imageUri = "uri",
            note = "note",
            status = FoodStatus.ACTIVE,
            resolvedDate = null
        )

        val entity = domain.toEntity()

        assertEquals(domain.id, entity.id)
        assertEquals(domain.name, entity.name)
        assertEquals(domain.location, entity.location)
        assertEquals(domain.purchaseDate, entity.purchaseDate)
        assertEquals(domain.expiryDate, entity.expiryDate)
        assertEquals(domain.imageUri, entity.imageUri)
        assertEquals(domain.note, entity.notes)
        assertEquals(domain.status, entity.status)
    }
}
