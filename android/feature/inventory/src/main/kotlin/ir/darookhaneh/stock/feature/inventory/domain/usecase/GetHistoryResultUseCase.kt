package ir.darookhaneh.stock.feature.inventory.domain.usecase

import ir.darookhaneh.stock.feature.inventory.domain.model.SearchHistory
import ir.darookhaneh.stock.feature.inventory.domain.repository.SearchRepository

class GetHistoryResultUseCase(
    private val searchRepository: SearchRepository,
) {
    suspend operator fun invoke(): List<SearchHistory> {
        return searchRepository.getHistoryResultList()
    }
}