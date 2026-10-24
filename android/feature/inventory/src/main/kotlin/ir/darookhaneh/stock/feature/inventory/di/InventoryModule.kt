package ir.darookhaneh.stock.feature.inventory.di

import ir.darookhaneh.stock.core.domain.usecase.category.AddCategoryUseCase
import ir.darookhaneh.stock.core.domain.usecase.category.DeleteCategoryUseCase
import ir.darookhaneh.stock.core.domain.usecase.category.EditCategoryUseCase
import ir.darookhaneh.stock.core.domain.usecase.category.ObserveCategoriesUseCase
import ir.darookhaneh.stock.core.domain.usecase.food.CreateFoodItemUseCase
import ir.darookhaneh.stock.feature.inventory.data.repository.SearchRepositoryImp
import ir.darookhaneh.stock.feature.inventory.domain.repository.SearchRepository
import ir.darookhaneh.stock.feature.inventory.domain.usecase.GetHistoryResultUseCase
import ir.darookhaneh.stock.feature.inventory.domain.usecase.GetInventoryPreferenceUseCase
import ir.darookhaneh.stock.feature.inventory.domain.usecase.ObserveSettingDataUseCase
import ir.darookhaneh.stock.feature.inventory.domain.usecase.food.DeleteFoodItemUseCase
import ir.darookhaneh.stock.feature.inventory.domain.usecase.food.MarkFoodAsConsumedUseCase
import ir.darookhaneh.stock.feature.inventory.domain.usecase.food.MarkFoodAsWastedUseCase
import ir.darookhaneh.stock.feature.inventory.domain.usecase.food.ObserveFoodItemsUseCase
import ir.darookhaneh.stock.feature.inventory.domain.usecase.food.UpdateSearchHistoryUseCase
import ir.darookhaneh.stock.feature.inventory.presentation.inventory.viewmodel.InventoryViewModel
import ir.darookhaneh.stock.feature.inventory.presentation.model.FoodUiModel
import ir.darookhaneh.stock.feature.inventory.presentation.search.viewmodel.SearchViewModel
import ir.darookhaneh.stock.feature.inventory.presentation.shared.DetailBottomSheetViewModel
import org.koin.core.module.dsl.bind
import org.koin.core.module.dsl.factoryOf
import org.koin.core.module.dsl.singleOf
import org.koin.core.module.dsl.viewModel
import org.koin.core.module.dsl.viewModelOf
import org.koin.dsl.module

val inventoryModule = module {
    //repository
    singleOf(::SearchRepositoryImp) { bind<SearchRepository>() }
    //usecase
    factoryOf(::GetInventoryPreferenceUseCase)
    factoryOf(::DeleteCategoryUseCase)
    factoryOf(::EditCategoryUseCase)
    factoryOf(::GetHistoryResultUseCase)
    factoryOf(::UpdateSearchHistoryUseCase)
    factoryOf(::CreateFoodItemUseCase)
    factoryOf(::AddCategoryUseCase)
    factoryOf(::DeleteFoodItemUseCase)
    factoryOf(::ObserveFoodItemsUseCase)
    factoryOf(::ObserveCategoriesUseCase)
    factoryOf(::ObserveSettingDataUseCase)
    factoryOf(::MarkFoodAsConsumedUseCase)
    factoryOf(::MarkFoodAsWastedUseCase)
    //viewModel
    viewModelOf(::InventoryViewModel)
    viewModelOf(::SearchViewModel)
    viewModel { (foodItem: FoodUiModel) ->
        DetailBottomSheetViewModel(
            foodItem = foodItem,
            markFoodAsConsumedUseCase = get(),
            markFoodAsWastedUseCase = get()
        )
    }
}
