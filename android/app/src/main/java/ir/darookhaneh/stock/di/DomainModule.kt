package ir.darookhaneh.stock.di

import ir.darookhaneh.stock.core.domain.usecase.CheckUpdateUseCase
import org.koin.core.module.dsl.factoryOf
import org.koin.dsl.module

val domainModule = module {
    factoryOf(::CheckUpdateUseCase)
}