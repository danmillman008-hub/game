package ir.darookhaneh.stock.feature.pharmacy.di

import ir.darookhaneh.stock.feature.pharmacy.presentation.add.AddDrugViewModel
import ir.darookhaneh.stock.feature.pharmacy.presentation.detail.DrugDetailViewModel
import ir.darookhaneh.stock.feature.pharmacy.presentation.dashboard.DashboardViewModel
import ir.darookhaneh.stock.feature.pharmacy.presentation.history.HistoryViewModel
import ir.darookhaneh.stock.feature.pharmacy.presentation.lookup.LookupViewModel
import ir.darookhaneh.stock.feature.pharmacy.presentation.record.RecordViewModel
import ir.darookhaneh.stock.feature.pharmacy.presentation.home.MedicationHomeViewModel
import ir.darookhaneh.stock.feature.pharmacy.presentation.scan.ScannerViewModel
import org.koin.androidx.viewmodel.dsl.viewModel
import org.koin.core.module.dsl.viewModelOf
import org.koin.dsl.module

val pharmacyModule = module {
    viewModelOf(::DashboardViewModel)
    viewModelOf(::MedicationHomeViewModel)
    viewModelOf(::AddDrugViewModel)
    viewModelOf(::ScannerViewModel)
    viewModelOf(::RecordViewModel)
    viewModelOf(::HistoryViewModel)
    viewModelOf(::LookupViewModel)

    viewModel { params ->
        DrugDetailViewModel(
            drugId = params.get(),
            drugRepository = get(),
            batchRepository = get(),
            inventoryRepository = get(),
            addBatch = get(),
            recordInventoryEvent = get(),
        )
    }
}
