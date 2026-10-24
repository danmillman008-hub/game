package ir.darookhaneh.stock.feature.settings.domain.usecase

import ir.darookhaneh.stock.core.model.error_handling.Resource
import ir.darookhaneh.stock.feature.settings.data.DataBackUpManger

class ManageDataUseCase(
    private val dataBackUpManger: DataBackUpManger
) {
    suspend operator fun invoke() {
        dataBackUpManger.exportDataToZip()
    }

    suspend fun exportData(): Resource<String> {
        return dataBackUpManger.exportDataToZip()
    }

    suspend fun importData(uriPath: String): Resource<Unit> {
        return dataBackUpManger.restoreEverythingFromZip(uriPath)
    }
}