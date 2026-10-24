package ir.darookhaneh.stock.core.domain.repository

import ir.darookhaneh.stock.core.model.error_handling.Resource

interface UpdateRepository {
    suspend fun getTagName(): Resource<String?>
}