package ir.darookhaneh.stock.core.data.repository

import ir.darookhaneh.stock.core.data.util.AppDispatchers
import ir.darookhaneh.stock.core.data.util.safeCall
import ir.darookhaneh.stock.core.domain.repository.UpdateRepository
import ir.darookhaneh.stock.core.model.error_handling.Resource
import ir.darookhaneh.stock.core.network.api.GithubApi

class UpdateRepositoryImpl(
    private val githubApi: GithubApi,
    private val appDispatchers: AppDispatchers
) : UpdateRepository {
    override suspend fun getTagName(): Resource<String?> {
        return safeCall(appDispatchers.io) {
            githubApi.fetchTagName().tagName?.removePrefix("v")
        }
    }
}