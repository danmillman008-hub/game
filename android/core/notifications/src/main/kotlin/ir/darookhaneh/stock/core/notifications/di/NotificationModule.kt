package ir.darookhaneh.stock.core.notifications.di

import coil3.ImageLoader
import ir.darookhaneh.stock.core.notifications.data.StockNotificationFactory
import ir.darookhaneh.stock.core.notifications.data.StockNotifierImp
import ir.darookhaneh.stock.core.notifications.domain.StockNotifier
import ir.darookhaneh.stock.core.notifications.domain.usecase.DeleteOldFoodUseCase
import ir.darookhaneh.stock.core.notifications.domain.usecase.GetExpiryFoodUseCase
import ir.darookhaneh.stock.core.notifications.domain.usecase.GetNotificationPreferenceUseCase
import ir.darookhaneh.stock.core.notifications.domain.usecase.GetWeeklySummaryUseCase
import ir.darookhaneh.stock.core.notifications.domain.usecase.UpdateFoodStatusUseCase
import ir.darookhaneh.stock.core.notifications.worker.CheckExpirationWorker
import ir.darookhaneh.stock.core.notifications.worker.CheckUpdateVersionWorker
import ir.darookhaneh.stock.core.notifications.worker.CleanUpFileWorker
import ir.darookhaneh.stock.core.notifications.worker.DeleteOldFoodWorker
import ir.darookhaneh.stock.core.notifications.worker.WeeklyReportWorker
import ir.darookhaneh.stock.core.notifications.worker.WorkerScheduler
import ir.darookhaneh.stock.core.notifications.worker.WorkerSchedulerImp
import org.koin.androidx.workmanager.dsl.workerOf
import org.koin.core.module.dsl.bind
import org.koin.core.module.dsl.factoryOf
import org.koin.core.module.dsl.singleOf
import org.koin.dsl.module

val notificationModule = module {
    singleOf(::WorkerSchedulerImp) { bind<WorkerScheduler>() }
    singleOf(::StockNotifierImp) { bind<StockNotifier>() }
    singleOf(::StockNotificationFactory)
    single<ImageLoader> {
        ImageLoader(context = get())
    }


    // UseCase
    factoryOf(::GetNotificationPreferenceUseCase)
    factoryOf(::GetExpiryFoodUseCase)
    factoryOf(::UpdateFoodStatusUseCase)
    factoryOf(::GetWeeklySummaryUseCase)
    factoryOf(::DeleteOldFoodUseCase)

    // Workers
    workerOf(::CheckExpirationWorker)
    workerOf(::WeeklyReportWorker)
    workerOf(::CleanUpFileWorker)
    workerOf(::DeleteOldFoodWorker)
    workerOf(::CheckUpdateVersionWorker)
}
