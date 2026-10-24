package ir.darookhaneh.stock.feature.food_entry.di

import ir.darookhaneh.stock.core.domain.usecase.food.GetFoodByIdUseCase
import ir.darookhaneh.stock.feature.food_entry.data.FoodEntryDataStore
import ir.darookhaneh.stock.feature.food_entry.domain.usecase.AddCategoryUseCase
import ir.darookhaneh.stock.feature.food_entry.domain.usecase.FoodEntryPreferencesUseCase
import ir.darookhaneh.stock.feature.food_entry.domain.usecase.GetCategoriesUseCase
import ir.darookhaneh.stock.feature.food_entry.domain.usecase.ObserveCategoriesUseCase
import ir.darookhaneh.stock.feature.food_entry.domain.usecase.SaveFoodItemUseCase
import ir.darookhaneh.stock.feature.food_entry.presentation.model.EntryUiModel
import ir.darookhaneh.stock.feature.food_entry.presentation.viewmodel.FoodEntryViewModel
import org.koin.android.ext.koin.androidContext
import org.koin.core.module.dsl.factoryOf
import org.koin.core.module.dsl.viewModel
import org.koin.dsl.module

val foodEntryModule = module {
    //data
    single { FoodEntryDataStore(androidContext()) }

    //usecase
    factoryOf(::ObserveCategoriesUseCase)
    factoryOf(::AddCategoryUseCase)
    factoryOf(::GetCategoriesUseCase)
    factoryOf(::SaveFoodItemUseCase)
    factoryOf(::FoodEntryPreferencesUseCase)
    factoryOf(::GetFoodByIdUseCase)

    //viewModel
    viewModel { (food: EntryUiModel) ->
        FoodEntryViewModel(
            entryUiModel = food,
            addCategoryUseCase = get(),
            saveFoodItemUseCase = get(),
            foodEntryPreferencesUseCase = get(),
            observeCategoriesUseCase = get(),
        )
    }
}
