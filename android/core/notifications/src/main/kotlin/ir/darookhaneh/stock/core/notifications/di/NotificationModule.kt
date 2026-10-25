package ir.darookhaneh.stock.core.notifications.di

import coil3.ImageLoader
import org.koin.dsl.module

/**
 * زیرساخت اعلان.
 *
 * کانال‌ها در [ir.darookhaneh.stock.core.notifications.data.NotificationChannelManager] ساخته می‌شوند.
 * Workerهای هشدار انقضا در فاز «هشدار موجودی» بر اساس جدول `batch` برمی‌گردند.
 */
val notificationModule = module {
    single<ImageLoader> { ImageLoader(context = get()) }
}
