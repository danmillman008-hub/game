package ir.darookhaneh.stock.feature.inventory.domain.usecase

import ir.darookhaneh.stock.feature.inventory.domain.model.SearchHistory
import ir.darookhaneh.stock.feature.inventory.domain.repository.SearchRepository
import ir.darookhaneh.stock.feature.inventory.domain.usecase.food.UpdateSearchHistoryUseCase
import io.mockk.coEvery
import io.mockk.coVerify
import io.mockk.mockk
import io.mockk.slot
import kotlinx.coroutines.test.runTest
import org.junit.Assert.assertEquals
import org.junit.Before
import org.junit.Test

class UpdateSearchHistoryUseCaseTest {

    private lateinit var searchRepository: SearchRepository
    private lateinit var updateSearchHistoryUseCase: UpdateSearchHistoryUseCase

    @Before
    fun setUp() {
        searchRepository = mockk()
        updateSearchHistoryUseCase = UpdateSearchHistoryUseCase(searchRepository)
    }

    @Test
    fun `invoke should store the query as one history entry`() = runTest {
        val captured = slot<SearchHistory>()
        coEvery { searchRepository.addHistoryResult(capture(captured)) } returns Unit

        updateSearchHistoryUseCase("Milk")

        coVerify(exactly = 1) { searchRepository.addHistoryResult(any()) }
        assertEquals("Milk", captured.captured.name)
    }

    @Test
    fun `invoke should not read the food list while writing history`() = runTest {
        coEvery { searchRepository.addHistoryResult(any()) } returns Unit

        updateSearchHistoryUseCase("Bread")

        coVerify(exactly = 0) { searchRepository.getFoodItemListByQuery(any()) }
    }
}
