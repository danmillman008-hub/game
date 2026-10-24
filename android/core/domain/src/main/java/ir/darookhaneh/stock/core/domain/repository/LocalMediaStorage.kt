package ir.darookhaneh.stock.core.domain.repository

import ir.darookhaneh.stock.core.model.error_handling.Resource

interface LocalMediaStorage {
    suspend fun copyImageToInternalStorage(uriPath: String): Resource<String>
    suspend fun deleteImageFromInternalStorage(uriPath: String): Resource<Unit>
    fun deleteAllFromInternalStorage()
    suspend fun getAllUriPath(): Resource<List<String>>

}