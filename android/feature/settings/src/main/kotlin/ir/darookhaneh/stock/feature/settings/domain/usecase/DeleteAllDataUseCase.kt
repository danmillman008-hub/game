package ir.darookhaneh.stock.feature.settings.domain.usecase

import ir.darookhaneh.stock.core.data.util.onSuccess
import ir.darookhaneh.stock.core.domain.repository.FoodRepository
import ir.darookhaneh.stock.core.domain.repository.LocalMediaStorage
import ir.darookhaneh.stock.core.model.error_handling.Resource

class DeleteAllDataUseCase(
    private val foodRepository: FoodRepository,
    private val localMediaStorage: LocalMediaStorage,
) {
    suspend operator fun invoke(): Resource<Unit> {
        return foodRepository.deleteAllFoodItems()
            .onSuccess {
                localMediaStorage.deleteAllFromInternalStorage()
            }
    }
}