package ir.darookhaneh.stock.feature.inventory.domain.usecase.food

import ir.darookhaneh.stock.feature.inventory.domain.model.SearchHistory
import ir.darookhaneh.stock.feature.inventory.domain.repository.SearchRepository

class UpdateSearchHistoryUseCase(
    private val searchRepository: SearchRepository
) {
    suspend operator fun invoke(searchQuery: String) {
        val searchHistory = SearchHistory(
            name = searchQuery,
            timeStamp = System.currentTimeMillis()
        )
        return searchRepository.addHistoryResult(searchHistory)
    }
}