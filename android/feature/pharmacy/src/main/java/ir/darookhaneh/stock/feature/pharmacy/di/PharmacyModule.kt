package ir.darookhaneh.stock.feature.pharmacy.di

import ir.darookhaneh.stock.feature.pharmacy.presentation.add.AddDrugViewModel
import ir.darookhaneh.stock.feature.pharmacy.presentation.detail.DrugDetailViewModel
import ir.darookhaneh.stock.feature.pharmacy.presentation.home.MedicationHomeViewModel
import org.koin.core.module.dsl.viewModelOf
import org.koin.dsl.module

val pharmacyModule = module {
    viewModelOf(::MedicationHomeViewModel)
    viewModelOf(::AddDrugViewModel)

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
