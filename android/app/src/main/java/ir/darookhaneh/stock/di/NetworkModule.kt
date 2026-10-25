package ir.darookhaneh.stock.di

import ir.darookhaneh.stock.core.network.api.GithubApi
import ir.darookhaneh.stock.core.network.api.GithubApi.Companion.GITHUB_RELEASE
import kotlinx.serialization.json.Json
import okhttp3.MediaType.Companion.toMediaType
import org.koin.core.qualifier.named
import org.koin.dsl.module
import retrofit2.Retrofit
import retrofit2.converter.kotlinx.serialization.asConverterFactory

private const val GITHUB_API = "GITHUB_API"

/**
 * تنها ارتباط شبکه‌ای محصول: بررسی نسخهٔ جدید روی GitHub.
 * عملیات دارو، بچ و موجودی هیچ وابستگی شبکه‌ای ندارد.
 */
val networkModule = module {
    single<GithubApi> {
        get<Retrofit>(qualifier = named(GITHUB_API)).create(GithubApi::class.java)
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
