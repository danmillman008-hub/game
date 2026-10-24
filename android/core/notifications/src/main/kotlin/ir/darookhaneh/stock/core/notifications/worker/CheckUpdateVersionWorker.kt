package ir.darookhaneh.stock.core.notifications.worker

import android.content.Context
import androidx.work.CoroutineWorker
import androidx.work.WorkerParameters
import ir.darookhaneh.stock.core.data.AppNewFeaturesReader
import ir.darookhaneh.stock.core.data.util.AppDispatchers
import ir.darookhaneh.stock.core.data.util.onSuccess
import ir.darookhaneh.stock.core.domain.usecase.CheckUpdateUseCase
import ir.darookhaneh.stock.core.notifications.domain.StockNotifier
import kotlinx.coroutines.withContext

class CheckUpdateVersionWorker(
    context: Context,
    workerParams: WorkerParameters,
    private val checkUpdateUseCase: CheckUpdateUseCase,
    private val appNewFeaturesReader: AppNewFeaturesReader,
    private val appDispatchers: AppDispatchers,
    private val notifier: StockNotifier,
) : CoroutineWorker(context, workerParams) {
    override suspend fun doWork(): Result {
        return withContext(appDispatchers.io) {
            try {
                val currentVersion = appNewFeaturesReader.currentVersionName
                checkUpdateUseCase()
                    .onSuccess { newVersion ->
                        if (newVersion != null && newVersion != currentVersion) {
                            notifier.showNewUpdateVersion()
                        }
                    }
                Result.success()
            } catch (e: Exception) {
                Result.failure()
            }
        }
    }
}