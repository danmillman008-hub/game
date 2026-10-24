package ir.darookhaneh.stock.core.domain.usecase

import ir.darookhaneh.stock.core.domain.repository.UpdateRepository
import ir.darookhaneh.stock.core.model.error_handling.Resource

class CheckUpdateUseCase(
    private val updateRepository: UpdateRepository
) {
    suspend operator fun invoke(): Resource<String?> {
        return updateRepository.getTagName()
    }
}