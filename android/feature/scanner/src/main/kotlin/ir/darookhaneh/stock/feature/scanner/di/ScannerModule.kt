package ir.darookhaneh.stock.feature.scanner.di

import ir.darookhaneh.stock.feature.scanner.domain.usecase.CreateFoodItemFromDateUseCase
import ir.darookhaneh.stock.feature.scanner.domain.usecase.ScanBarcodeUseCase
import ir.darookhaneh.stock.feature.scanner.domain.usecase.ScanFoodDateUseCase
import ir.darookhaneh.stock.feature.scanner.presentation.scanner.viewmodel.ScannerViewModel
import org.koin.core.module.dsl.factoryOf
import org.koin.core.module.dsl.viewModelOf
import org.koin.dsl.module

val scannerModule = module {
    //usecase
    factoryOf(::ScanBarcodeUseCase)
    factoryOf(::ScanFoodDateUseCase)
    factoryOf(::CreateFoodItemFromDateUseCase)

    //viewmodel
    viewModelOf(::ScannerViewModel)
}