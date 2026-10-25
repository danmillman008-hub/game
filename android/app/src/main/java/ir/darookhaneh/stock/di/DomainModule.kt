package ir.darookhaneh.stock.di

import ir.darookhaneh.stock.core.domain.pharmacy.usecase.AddBatchUseCase
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.CreateDrugWithStockUseCase
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.ObserveDashboardUseCase
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.ObserveDrugSummariesUseCase
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.LookupDrugCodeUseCase
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.ObserveAutoLookupUseCase
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.SetAutoLookupUseCase
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.RecordInventoryEventUseCase
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.ResolveScannedCodeUseCase
import ir.darookhaneh.stock.core.domain.usecase.CheckUpdateUseCase
import org.koin.core.module.dsl.factoryOf
import org.koin.dsl.module

val domainModule = module {
    factoryOf(::CheckUpdateUseCase)

    // داروخانه
    factoryOf(::CreateDrugWithStockUseCase)
    factoryOf(::AddBatchUseCase)
    factoryOf(::RecordInventoryEventUseCase)
    factoryOf(::ResolveScannedCodeUseCase)
    factoryOf(::ObserveDrugSummariesUseCase)
    factoryOf(::ObserveDashboardUseCase)
    factoryOf(::LookupDrugCodeUseCase)
    factoryOf(::ObserveAutoLookupUseCase)
    factoryOf(::SetAutoLookupUseCase)
}
