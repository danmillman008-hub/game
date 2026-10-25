package ir.darookhaneh.stock.pharmacy

import android.app.Application
import androidx.room.Room
import androidx.test.core.app.ApplicationProvider
import ir.darookhaneh.stock.core.data.pharmacy.BatchRepositoryImpl
import ir.darookhaneh.stock.core.data.pharmacy.DrugRepositoryImpl
import ir.darookhaneh.stock.core.data.pharmacy.InventoryRepositoryImpl
import ir.darookhaneh.stock.core.database.AppDatabase
import ir.darookhaneh.stock.core.database.RoomTransactionRunner
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.AddBatchUseCase
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.CreateDrugWithStockUseCase
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.RecordInventoryEventUseCase
import ir.darookhaneh.stock.core.model.pharmacy.InventoryEventType
import ir.darookhaneh.stock.core.model.pharmacy.PharmacyConfig
import ir.darookhaneh.stock.core.model.pharmacy.TimeProvider
import ir.darookhaneh.stock.feature.pharmacy.presentation.detail.DrugDetailAction
import ir.darookhaneh.stock.feature.pharmacy.presentation.detail.DrugDetailViewModel
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.ExperimentalCoroutinesApi
import kotlinx.coroutines.flow.first
import kotlinx.coroutines.test.UnconfinedTestDispatcher
import kotlinx.coroutines.test.resetMain
import kotlinx.coroutines.runBlocking
import kotlinx.coroutines.withTimeout
import kotlinx.coroutines.test.setMain
import org.junit.After
import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotNull
import org.junit.Before
import org.junit.Test
import org.junit.runner.RunWith
import org.robolectric.RobolectricTestRunner
import org.robolectric.annotation.Config

/**
 * بازسازی همان مسیری که کاربر روی گوشی رفت و اپ کرش کرد:
 * «ثبت اولین دارو» → باز شدن جزئیات دارو → ثبت خروج.
 *
 * این تست با Room واقعی (in-memory) و همان Repository/UseCase/ViewModel تولیدی اجرا
 * می‌شود، نه mock. اگر جایی از این زنجیره استثنا بدهد، اینجا قرمز می‌شود.
 */
@OptIn(ExperimentalCoroutinesApi::class)
@RunWith(RobolectricTestRunner::class)
@Config(sdk = [34], application = Application::class)
class PharmacySaveFlowTest {

    private lateinit var db: AppDatabase
    private lateinit var drugRepository: DrugRepositoryImpl
    private lateinit var batchRepository: BatchRepositoryImpl
    private lateinit var inventoryRepository: InventoryRepositoryImpl
    private lateinit var createDrugWithStock: CreateDrugWithStockUseCase

    private val now = 1_772_000_000_000L
    private val day = 86_400_000L

    @Before
    fun setUp() {
        Dispatchers.setMain(UnconfinedTestDispatcher())
        val context = ApplicationProvider.getApplicationContext<Application>()
        db = Room.inMemoryDatabaseBuilder(context, AppDatabase::class.java)
            .allowMainThreadQueries()
            .build()

        val timeProvider = TimeProvider { now }
        drugRepository = DrugRepositoryImpl(db.drugDao(), timeProvider, PharmacyConfig())
        batchRepository = BatchRepositoryImpl(db.batchDao(), timeProvider)
        inventoryRepository = InventoryRepositoryImpl(
            batchDao = db.batchDao(),
            inventoryEventDao = db.inventoryEventDao(),
            transactionRunner = RoomTransactionRunner(db),
            timeProvider = timeProvider,
        )
        createDrugWithStock = CreateDrugWithStockUseCase(
            drugRepository = drugRepository,
            batchRepository = batchRepository,
            inventoryRepository = inventoryRepository,
        )
    }

    @After
    fun tearDown() {
        db.close()
        Dispatchers.resetMain()
    }

    @Test
    fun `ثبت اولین دارو و باز شدن جزئیات بدون استثنا انجام می‌شود`() = runBlocking {
        val drugId = createDrugWithStock(
            name = "استامینوفن ۵۰۰",
            packSize = 20,
            batchNumber = "A-12",
            expiryDate = now + 60 * day,
            initialQuantity = 20,
        )

        // ۱) فهرست داروها (همان چیزی که بعد از ثبت باید رندر شود)
        val summaries = drugRepository.observeSummaries().first()
        assertEquals(1, summaries.size)
        assertEquals("استامینوفن ۵۰۰", summaries.first().name)
        assertEquals(20, summaries.first().totalQuantity)
        assertEquals(1, summaries.first().batchCount)
        assertEquals(20, summaries.first().packSize)

        // ۲) جزئیات دارو (صفحه‌ای که بلافاصله بعد از ذخیره باز می‌شود)
        val viewModel = DrugDetailViewModel(
            drugId = drugId,
            drugRepository = drugRepository,
            batchRepository = batchRepository,
            inventoryRepository = inventoryRepository,
            addBatch = AddBatchUseCase(drugRepository, batchRepository),
            recordInventoryEvent = RecordInventoryEventUseCase(batchRepository, inventoryRepository),
        )

        // جریان‌های Room غیرهمگام منتشر می‌شوند؛ تا رسیدن داده صبر می‌کنیم (نه sleep ثابت).
        val ready = withTimeout(10_000) {
            viewModel.uiState.first { it.drug != null && it.selectedBatchId != null }
        }
        assertEquals("استامینوفن ۵۰۰", ready.drug?.name)
        assertNotNull(ready.selectedBatchId)

        // ۳) خروج ۵ عدد → ۱۵
        val batchId = requireNotNull(ready.selectedBatchId)
        viewModel.onAction(DrugDetailAction.SelectBatch(batchId))
        viewModel.onAction(DrugDetailAction.OnAmountChange("5"))
        viewModel.onAction(DrugDetailAction.Record(InventoryEventType.DISPENSE))

        val after = withTimeout(10_000) {
            viewModel.uiState.first { state -> state.batches.firstOrNull()?.quantity == 15 }
        }
        assertEquals(15, after.batches.first().quantity)
        assertEquals(15, drugRepository.observeSummaries().first().first().totalQuantity)
    }

    @Test
    fun `ثبت سریع با روش کارتن و ضایعات درست کار می‌کند`() = runBlocking {
        val drugId = createDrugWithStock(
            name = "آموکسی‌سیلین",
            packSize = 24,
            batchNumber = "B-1",
            expiryDate = now + 90 * day,
            initialQuantity = 100,
        )
        val batchId = batchRepository.observeByDrug(drugId).first().first().id

        val record = RecordInventoryEventUseCase(batchRepository, inventoryRepository)

        // ضایعات ۵ عدد
        record(batchId = batchId, type = InventoryEventType.DAMAGE, amount = 5)
        assertEquals(95, batchRepository.getById(batchId)?.quantity)

        // مرجوعی ۳ عدد
        record(batchId = batchId, type = InventoryEventType.RETURN, amount = 3)
        assertEquals(98, batchRepository.getById(batchId)?.quantity)

        // تاریخچهٔ سراسری هر سه رخداد (ورود اولیه + ضایعات + مرجوعی) را دارد
        val history = inventoryRepository.observeHistory().first()
        assertEquals(3, history.size)
        assertEquals("آموکسی‌سیلین", history.first().drugName)
    }
}
