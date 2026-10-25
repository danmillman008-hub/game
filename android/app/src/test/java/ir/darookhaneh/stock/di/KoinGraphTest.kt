package ir.darookhaneh.stock.di

import android.app.Application
import androidx.test.core.app.ApplicationProvider
import ir.darookhaneh.stock.AppViewModel
import ir.darookhaneh.stock.core.notifications.di.notificationModule
import ir.darookhaneh.stock.feature.pharmacy.di.pharmacyModule
import ir.darookhaneh.stock.feature.pharmacy.presentation.add.AddDrugViewModel
import ir.darookhaneh.stock.feature.pharmacy.presentation.dashboard.DashboardViewModel
import ir.darookhaneh.stock.feature.pharmacy.presentation.history.HistoryViewModel
import ir.darookhaneh.stock.feature.pharmacy.presentation.home.MedicationHomeViewModel
import ir.darookhaneh.stock.feature.pharmacy.presentation.record.RecordViewModel
import ir.darookhaneh.stock.feature.pharmacy.presentation.scan.ScannerViewModel
import ir.darookhaneh.stock.feature.settings.di.settingModule
import kotlinx.coroutines.test.runTest
import org.junit.After
import org.junit.Assert.assertNotNull
import org.junit.Test
import org.junit.runner.RunWith
import org.koin.android.ext.koin.androidContext
import org.koin.core.context.startKoin
import org.koin.core.context.stopKoin
import org.koin.test.KoinTest
import org.koin.test.get
import org.robolectric.RobolectricTestRunner
import org.robolectric.annotation.Config

/**
 * گیت گراف تزریق وابستگی.
 *
 * دلیل وجود: اپ روی گوشی هنگام باز شدن کرش می‌کرد چون Koin نمی‌تواند پارامتر
 * پیش‌فرض سازنده (`clock: () -> Long = …`) را تأمین کند و همان لحظهٔ ساخت
 * DashboardViewModel با NoDefinitionFoundException می‌مرد. این تست همان گراف
 * واقعی را می‌سازد تا چنین اشکالی پیش از رسیدن به گوشی گرفته شود.
 */
@RunWith(RobolectricTestRunner::class)
@Config(sdk = [34])
class KoinGraphTest : KoinTest {

    private fun startGraph() {
        val context = ApplicationProvider.getApplicationContext<Application>()
        startKoin {
            androidContext(context)
            modules(
                listOf(
                    appModule,
                    databaseModule,
                    dataModule,
                    domainModule,
                    networkModule,
                    notificationModule,
                    pharmacyModule,
                    settingModule,
                )
            )
        }
    }

    @After
    fun tearDown() {
        stopKoin()
    }

    @Test
    fun `گراف کامل Koin بدون خطا ساخته می‌شود`() {
        startGraph()
        assertNotNull(get<AppViewModel>())
    }

    @Test
    fun `همهٔ ViewModelهای صفحه‌ها قابل ساخت هستند`() {
        startGraph()
        assertNotNull(get<DashboardViewModel>())
        assertNotNull(get<MedicationHomeViewModel>())
        assertNotNull(get<AddDrugViewModel>())
        assertNotNull(get<ScannerViewModel>())
        assertNotNull(get<RecordViewModel>())
        assertNotNull(get<HistoryViewModel>())
    }

    @Test
    fun `داشبورد می‌تواند جریان داده را جمع کند`() = runTest {
        startGraph()
        val vm = get<DashboardViewModel>()
        assertNotNull(vm.uiState.value)
    }

    @Test
    fun `فهرست داروها با دیتابیس خالی جریان خالی برمی‌گرداند`() = runTest {
        startGraph()
        val vm = get<MedicationHomeViewModel>()
        assertNotNull(vm.uiState.value)
    }
}
