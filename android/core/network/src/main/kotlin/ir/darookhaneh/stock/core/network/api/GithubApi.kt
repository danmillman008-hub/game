package ir.darookhaneh.stock.core.network.api

import ir.darookhaneh.stock.core.network.model.GithubApiResponse
import retrofit2.http.GET

interface GithubApi {
    @GET("releases/latest")
    suspend fun fetchTagName(): GithubApiResponse

    companion object {
        const val GITHUB_RELEASE = "https://api.github.com/repos/NhuHuy-79/Stock/"
    }
}