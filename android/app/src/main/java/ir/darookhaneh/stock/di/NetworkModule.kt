package ir.darookhaneh.stock.di

import ir.darookhaneh.stock.core.network.api.FoodApi
import ir.darookhaneh.stock.core.network.api.FoodApi.Companion.BASE_URL
import ir.darookhaneh.stock.core.network.api.GithubApi
import ir.darookhaneh.stock.core.network.api.GithubApi.Companion.GITHUB_RELEASE
import ir.darookhaneh.stock.core.network.data_source.FoodRemoteDataSource
import ir.darookhaneh.stock.core.network.data_source.FoodRemoteDataSourceImpl
import kotlinx.serialization.json.Json
import okhttp3.MediaType.Companion.toMediaType
import org.koin.core.qualifier.named
import org.koin.dsl.module
import retrofit2.Retrofit
import retrofit2.converter.kotlinx.serialization.asConverterFactory

private const val STOCK_API = "STOCK_API"
private const val GITHUB_API = "GITHUB_API"

val networkModule = module {
    single<FoodRemoteDataSource> { FoodRemoteDataSourceImpl(get()) }
    single<FoodApi> {
        get<Retrofit>(qualifier = named(STOCK_API)).create(FoodApi::class.java)
    }

    single<GithubApi> {
        get<Retrofit>(qualifier = named(GITHUB_API)).create(GithubApi::class.java)
    }

    single(qualifier = named(STOCK_API)) {
        val json: Json = get()
        val contentType = "application/json".toMediaType()

        Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(json.asConverterFactory(contentType))
            .build()
    }

    single(qualifier = named(GITHUB_API)) {
        val json: Json = get()
        val contentType = "application/json".toMediaType()

        Retrofit.Builder()
            .baseUrl(GITHUB_RELEASE)
            .addConverterFactory(json.asConverterFactory(contentType))
            .build()
    }
    single {
        Json {
            explicitNulls = false
            ignoreUnknownKeys = true
            isLenient = true
            encodeDefaults = true
        }
    }
}
