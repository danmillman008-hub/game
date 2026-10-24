package ir.darookhaneh.stock.feature.analytics.di

import ir.darookhaneh.stock.feature.analytics.data.repository.FoodAnalyticsRepositoryImpl
import ir.darookhaneh.stock.feature.analytics.domain.repository.FoodAnalyticsRepository
import ir.darookhaneh.stock.feature.analytics.presentation.viewmodel.AnalyticsViewModel
import org.koin.core.module.dsl.bind
import org.koin.core.module.dsl.singleOf
import org.koin.core.module.dsl.viewModelOf
import org.koin.dsl.module

/**
 * Koin module for the Analytics feature.
 * Defines dependencies for repository, individual UseCases, and the ViewModel.
 */
val analyticsModule = module {
    // Repository
    singleOf(::FoodAnalyticsRepositoryImpl) { bind<FoodAnalyticsRepository>() }

    // ViewModel
    viewModelOf(::AnalyticsViewModel)
}
