package ir.darookhaneh.stock.di

import ir.darookhaneh.stock.AppViewModel
import ir.darookhaneh.stock.core.data.AppCapabilityManager
import ir.darookhaneh.stock.core.datastore.DeviceCapableDataStore
import ir.darookhaneh.stock.core.datastore.DeviceCapableDataStoreImpl
import ir.darookhaneh.stock.core.presentation.navigation.Navigator
import ir.darookhaneh.stock.core.presentation.navigation.NavigatorImpl
import ir.darookhaneh.stock.feature.settings.data.WidgetExceptionLogger
import ir.darookhaneh.stock.feature.settings.data.WidgetExceptionLoggerImpl
import ir.darookhaneh.stock.utils.AppInitializer
import ir.darookhaneh.stock.utils.DefaultAppCapabilityManager
import ir.darookhaneh.stock.widget.usecase.GetFoodsUseCase
import ir.darookhaneh.stock.widget.worker.ConsumeFoodWorker
import ir.darookhaneh.stock.widget.worker.WasteWeeklyAllFoodsWorker
import org.koin.androidx.workmanager.dsl.workerOf
import org.koin.core.module.dsl.bind
import org.koin.core.module.dsl.factoryOf
import org.koin.core.module.dsl.singleOf
import org.koin.core.module.dsl.viewModelOf
import org.koin.dsl.bind
import org.koin.dsl.module

val appModule = module {

    singleOf(::DefaultAppCapabilityManager) { bind<AppCapabilityManager>() }
    singleOf(::DeviceCapableDataStoreImpl) { bind<DeviceCapableDataStore>() }
    singleOf(::NavigatorImpl) { bind<Navigator>() }
    singleOf(::AppInitializer)
    viewModelOf(::AppViewModel)

    //UseCase
    factoryOf(::GetFoodsUseCase)
    factoryOf(::WidgetExceptionLoggerImpl) bind WidgetExceptionLogger::class

    //Worker
    workerOf(::ConsumeFoodWorker)
    workerOf(::WasteWeeklyAllFoodsWorker)
}