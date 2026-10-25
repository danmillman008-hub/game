package ir.darookhaneh.stock.app.pharmacy

import android.app.Application
import androidx.room.Room
import androidx.test.core.app.ApplicationProvider
import ir.darookhaneh.stock.core.data.pharmacy.BatchRepositoryImpl
import ir.darookhaneh.stock.core.data.pharmacy.DrugRepositoryImpl
import ir.darookhaneh.stock.core.data.pharmacy.InventoryRepositoryImpl
import ir.darookhaneh.stock.core.data.pharmacy.TtacLookupRepositoryImpl
import ir.darookhaneh.stock.core.database.AppDatabase
import ir.darookhaneh.stock.core.database.RoomTransactionRunner
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.CreateDrugWithStockUseCase
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.LookupDrugCodeUseCase
import ir.darookhaneh.stock.core.model.pharmacy.DrugLookupRemote
import ir.darookhaneh.stock.core.model.pharmacy.DrugLookupResult
import ir.darookhaneh.stock.core.model.pharmacy.LookupException
import ir.darookhaneh.stock.core.model.pharmacy.LookupFailure
import ir.darookhaneh.stock.core.model.pharmacy.PharmacyConfig
import ir.darookhaneh.stock.core.model.pharmacy.TimeProvider
import ir.darookhaneh.stock.feature.pharmacy.presentation.lookup.LookupCodeKind
import ir.darookhaneh.stock.feature.pharmacy.presentation.lookup.LookupScreenAction
import ir.darookhaneh.stock.feature.pharmacy.presentation.lookup.LookupViewModel
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.flow.first
import kotlinx.coroutines.runBlocking
import kotlinx.coroutines.test.UnconfinedTestDispatcher
import kotlinx.coroutines.test.resetMain
import kotlinx.coroutines.test.setMain
import kotlinx.coroutines.withTimeout
import org.junit.After
import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Before
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.RobolectricTestRunner
import org.robolectric.annotation.Config

/**
 * تست «استعلام تیتک» با دیتابیس واقعی (in-memory) و سرور تقلبی.
 *
 * چرا این تست: ایراد کارفرما این بود که روش استعلام مشخص نیست. اینجا همان مسیر
 * کاربر آزموده می‌شود: کد را بزن → دکمهٔ استعلام → نتیجه → «ثبت این دارو» →
 * دارو در انبار ساخته می‌شود، و بار دوم همان دارو باز می‌شود (بدون تکرار).
 * هیچ درخواست شبکه‌ای واقعی انجام نمی‌شود.
 */
@OptIn(ExperimentalCoroutinesApi::class)
@RunWith(RobolectricTestRunner::class)
@Config(sdk = [34], application = Application::class)
class LookupFlowTest {

    private lateinit var db: AppDatabase
    private lateinit var drugRepository: DrugRepositoryImpl
    private lateinit var viewModel: LookupViewModel

    private val now = 1_772_000_000_000L

    /** سرور تقلبی: همان شکل پاسخ واقعی تیتک. */
    private class FakeRemote(
        private val response: () -> DrugLookupResult,
    ) : DrugLookupRemote {
        var calls = 0
        override suspend fun lookup(code: String): DrugLookupResult {
            calls++
            return response()
        }
    }

    private fun buildViewModel(remote: DrugLookupRemote): LookupViewModel {
        val timeProvider = TimeProvider { now }
        val lookupRepository = TtacLookupRepositoryImpl(
            remote = remote,
            cacheDao = db.lookupCacheDao(),
            timeProvider = timeProvider,
        )
        return LookupViewModel(
            lookupDrugCode = LookupDrugCodeUseCase(lookupRepository),
            createDrugWithStock = CreateDrugWithStockUseCase(
                drugRepository = drugRepository,
                batchRepository = BatchRepositoryImpl(db.batchDao(), timeProvider),
                inventoryRepository = InventoryRepositoryImpl(
                    batchDao = db.batchDao(),
                    inventoryEventDao = db.inventoryEventDao(),
                    transactionRunner = RoomTransactionRunner(db),
                    timeProvider = timeProvider,
                ),
            ),
            drugRepository = drugRepository,
        )
    }

    @Before
    fun setUp() {
        Dispatchers.setMain(UnconfinedTestDispatcher())
        val context = ApplicationProvider.getApplicationContext<Application>()
        db = Room.inMemoryDatabaseBuilder(context, AppDatabase::class.java)
            .allowMainThreadQueries()
            .build()
        drugRepository = DrugRepositoryImpl(
            drugDao = db.drugDao(),
            timeProvider = { now },
            config = PharmacyConfig(),
        )
    }

    @After
    fun tearDown() {
        db.close()
        Dispatchers.resetMain()
    }

    private fun result(code: String) = DrugLookupResult(
        code = code,
        name = "استامینوفن ۵۰۰",
        englishName = "ACETAMINOPHEN 500",
        gtin = "06260000000001",
        irc = "1234567890123456",
        company = "شرکت نمونه",
        price = 12500,
        statusCode = 1,
        fetchedAt = now,
    )

    @Test
    fun `نوع کد از روی طول تشخیص داده می‌شود`() {
        assertEquals(LookupCodeKind.GTIN, LookupCodeKind.of("62600000000001"))
        assertEquals(LookupCodeKind.AUTH_16, LookupCodeKind.of("1234567890123456"))
        assertEquals(LookupCodeKind.UID, LookupCodeKind.of("12345678901234567890"))
        assertEquals(LookupCodeKind.UNKNOWN, LookupCodeKind.of("123"))
    }

    @Test
    fun `کد نامعتبر بدون شبکه رد می‌شود`() = runBlocking {
        val remote = FakeRemote { result("1") }
        viewModel = buildViewModel(remote)

        viewModel.onAction(LookupScreenAction.OnInputChange("123"))
        viewModel.onAction(LookupScreenAction.Start)

        val state = viewModel.uiState.value
        assertTrue(state.error != null)
        assertEquals(0, remote.calls)
    }

    @Test
    fun `استعلام کد و ثبت دارو از نتیجه انجام می‌شود`() = runBlocking {
        val remote = FakeRemote { result("62600000000001") }
        viewModel = buildViewModel(remote)

        viewModel.onAction(LookupScreenAction.OnInputChange("۶۲۶ ۰۰۰۰۰ ۰۰۰۰۰ ۰۱".replace(" ", "")))
        viewModel.onAction(LookupScreenAction.Start)

        val withResult = withTimeout(10_000) { viewModel.uiState.first { it.result != null } }
        assertEquals("استامینوفن ۵۰۰", withResult.result?.name)
        assertEquals("06260000000001", withResult.result?.gtin)
        assertEquals(1, remote.calls)

        viewModel.onAction(LookupScreenAction.Apply)
        val applied = withTimeout(10_000) { viewModel.uiState.first { it.openDrugId != null } }
        val drugId = requireNotNull(applied.openDrugId)

        val drug = drugRepository.getById(drugId)
        assertNotNull(drug)
        assertEquals("استامینوفن ۵۰۰", drug?.name)
        assertEquals("06260000000001", drug?.gtin)
        assertEquals("1234567890123456", drug?.irc)
    }

    @Test
    fun `ثبت دوبارهٔ همان کد داروی تکراری نمی‌سازد و از حافظه پاسخ می‌دهد`() = runBlocking {
        val remote = FakeRemote { result("62600000000001") }
        viewModel = buildViewModel(remote)

        viewModel.onAction(LookupScreenAction.OnInputChange("62600000000001"))
        viewModel.onAction(LookupScreenAction.Start)
        withTimeout(10_000) { viewModel.uiState.first { it.result != null } }
        viewModel.onAction(LookupScreenAction.Apply)
        withTimeout(10_000) { viewModel.uiState.first { it.openDrugId != null } }

        // استعلام دوم برای همان کد: از کش، بدون درخواست تازه
        viewModel.onAction(LookupScreenAction.ConsumeOpenDrug)
        viewModel.onAction(LookupScreenAction.Start)
        val second = withTimeout(10_000) { viewModel.uiState.first { it.result != null } }

        assertEquals(1, remote.calls)
        assertEquals(1, drugRepository.observeDrugCount().first())

        viewModel.onAction(LookupScreenAction.Apply)
        withTimeout(10_000) { viewModel.uiState.first { it.openDrugId != null } }
        // هنوز یک دارو — نه دو
        assertEquals(1, drugRepository.observeDrugCount().first())
    }

    @Test
    fun `قطعی اینترنت پیام روشن می‌دهد و دارو ساخته نمی‌شود`() = runBlocking {
        val remote = FakeRemote {
            throw LookupException(LookupFailure.NO_CONNECTION, "اتصال برقرار نشد")
        }
        viewModel = buildViewModel(remote)

        viewModel.onAction(LookupScreenAction.OnInputChange("62600000000001"))
        viewModel.onAction(LookupScreenAction.Start)

        val state = withTimeout(10_000) { viewModel.uiState.first { it.error != null } }
        assertEquals("اتصال برقرار نشد", state.error)
        assertNull(state.result)
        assertEquals(0, drugRepository.observeDrugCount().first())
    }

    @Test
    fun `تغییر کد نتیجهٔ قبلی را پاک می‌کند`() = runBlocking {
        val remote = FakeRemote { result("62600000000001") }
        viewModel = buildViewModel(remote)

        viewModel.onAction(LookupScreenAction.OnInputChange("62600000000001"))
        viewModel.onAction(LookupScreenAction.Start)
        withTimeout(10_000) { viewModel.uiState.first { it.result != null } }

        viewModel.onAction(LookupScreenAction.OnInputChange("62600000000002"))
        assertNull(viewModel.uiState.value.result)
    }
}
