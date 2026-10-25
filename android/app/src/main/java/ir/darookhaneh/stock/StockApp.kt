package ir.darookhaneh.stock

import android.app.Application
import androidx.work.Configuration
import coil3.ImageLoader
import coil3.PlatformContext
import coil3.SingletonImageLoader
import coil3.disk.DiskCache
import coil3.disk.directory
import coil3.memory.MemoryCache
import coil3.network.okhttp.OkHttpNetworkFetcherFactory
import coil3.request.crossfade
import ir.darookhaneh.stock.core.data.repository.FOLDER_IMAGE
import ir.darookhaneh.stock.core.notifications.data.NotificationChannelManager
import ir.darookhaneh.stock.core.notifications.di.notificationModule
import ir.darookhaneh.stock.di.appModule
import ir.darookhaneh.stock.di.dataModule
import ir.darookhaneh.stock.di.databaseModule
import ir.darookhaneh.stock.di.domainModule
import ir.darookhaneh.stock.di.networkModule
import ir.darookhaneh.stock.feature.pharmacy.di.pharmacyModule
import ir.darookhaneh.stock.feature.settings.di.settingModule
import ir.darookhaneh.stock.utils.CrashReporter
import org.koin.android.ext.koin.androidContext
import org.koin.android.ext.koin.androidLogger
import org.koin.androidx.workmanager.factory.KoinWorkerFactory
import org.koin.androidx.workmanager.koin.workManagerFactory
import org.koin.core.component.KoinComponent
import org.koin.core.component.inject
import org.koin.core.context.GlobalContext.startKoin
import org.koin.core.logger.Level
import timber.log.Timber

class StockApp : Application(), KoinComponent, SingletonImageLoader.Factory,
    Configuration.Provider {
    override val workManagerConfiguration: Configuration
        get() = Configuration.Builder()
            .setWorkerFactory(KoinWorkerFactory())
            .setMinimumLoggingLevel(android.util.Log.DEBUG)
            .build()

    override fun newImageLoader(context: PlatformContext): ImageLoader {
        return ImageLoader.Builder(context)
            .memoryCache {
                MemoryCache.Builder()
                    .maxSizePercent(context, 0.25)
                    .build()
            }
            .diskCache {
                DiskCache.Builder()
                    .directory(context.filesDir.resolve(FOLDER_IMAGE))
                    .maxSizeBytes(100L * 1024 * 1024) // 100MB
                    .build()
            }
            .components {
                add(OkHttpNetworkFetcherFactory())
            }
            .crossfade(true)
            .build()
    }

    override fun onCreate() {
        super.onCreate()

        // اولین کاری که انجام می‌شود: ثبت کرش تا هیچ خطایی بی‌ردپا نماند.
        CrashReporter(this).install()

        plantTimber()

        //Koin for DI
        startKoin {
            androidContext(this@StockApp)
            androidLogger(level = Level.DEBUG)
            workManagerFactory()
            modules(
                listOf(
                    appModule,
                    databaseModule,
                    dataModule,
                    domainModule,
                    networkModule,
                    notificationModule,
                    pharmacyModule,
                    settingModule
                )
            )
        }

        //Notification
        NotificationChannelManager.createAllChannels(this)

    }

    private fun plantTimber() {
        if (BuildConfig.DEBUG) {
            Timber.plant(Timber.DebugTree())
        }
    }
}
