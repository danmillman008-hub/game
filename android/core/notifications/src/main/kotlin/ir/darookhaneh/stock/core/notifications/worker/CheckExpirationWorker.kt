package ir.darookhaneh.stock.core.notifications.worker

import android.content.Context
import androidx.work.CoroutineWorker
import androidx.work.WorkerParameters
import ir.darookhaneh.stock.core.data.util.AppDispatchers
import ir.darookhaneh.stock.core.notifications.domain.StockNotifier
import ir.darookhaneh.stock.core.notifications.domain.NotificationFoodItem
import ir.darookhaneh.stock.core.notifications.domain.usecase.GetExpiryFoodUseCase
import ir.darookhaneh.stock.core.notifications.domain.usecase.GetNotificationPreferenceUseCase
import kotlinx.coroutines.withContext
import timber.log.Timber

class CheckExpirationWorker(
    appContext: Context,
    params: WorkerParameters,
    private val getNotificationPreferenceUseCase: GetNotificationPreferenceUseCase,
    private val getExpiryFoodUseCase: GetExpiryFoodUseCase,
    private val workerScheduler: WorkerScheduler,
    private val notifier: StockNotifier,
    private val appDispatchers: AppDispatchers,
) : CoroutineWorker(appContext = appContext, params = params) {
    override suspend fun doWork(): Result {
        return withContext(appDispatchers.io) {
            Timber.d("Expiration Worker Check!")
            try {
                if (!getNotificationPreferenceUseCase()) {
                    return@withContext Result.success()
                }

                if (runAttemptCount >= 5) {
                    return@withContext Result.failure()
                }
                val expiringFoods = getExpiryFoodUseCase()
                if (expiringFoods.isEmpty()) {
                    Timber.d("No expiry food!")
                    return@withContext Result.success()
                }

                val expiredToday = expiringFoods.filter { it.getRemainingDays() == 0 }
                val expiringSoon = expiringFoods.filter { it.getRemainingDays() > 0 }

                expiredToday.forEach { food ->
                    notifier.showActionableExpiryPrompt(
                        foodId = food.id,
                        foodName = food.name,
                        uriPath = food.imageUri
                    )
                }

                if (expiringSoon.isNotEmpty()) {
                    val notificationItems = expiringSoon.map { food ->
                        NotificationFoodItem(
                            id = food.id,
                            name = food.name,
                            daysLeft = food.getRemainingDays(),
                            imageUri = food.imageUri
                        )
                    }
                    notifier.showExpiringItemsAlert(notificationItems)
                }
                //Reschedule
                Result.success()
            } catch (e: Exception) {
                Timber.e(e)
                Result.retry()
            } finally {
                workerScheduler.scheduleCheckExpiryWorker(forceReplace = true)
            }
        }
    }
}
