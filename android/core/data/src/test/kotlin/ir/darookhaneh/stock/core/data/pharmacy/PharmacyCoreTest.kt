package ir.darookhaneh.stock.core.data.pharmacy

import android.content.Context
import androidx.room.Room
import androidx.test.core.app.ApplicationProvider
import ir.darookhaneh.stock.core.database.AppDatabase
import ir.darookhaneh.stock.core.database.RoomTransactionRunner
import ir.darookhaneh.stock.core.domain.pharmacy.PharmacyError
import ir.darookhaneh.stock.core.domain.pharmacy.PharmacyException
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.AddBatchUseCase
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.CreateDrugWithStockUseCase
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.RecordInventoryEventUseCase
import ir.darookhaneh.stock.core.domain.pharmacy.usecase.ResolveScannedCodeUseCase
import ir.darookhaneh.stock.core.model.pharmacy.InventoryEventType
import ir.darookhaneh.stock.core.model.pharmacy.PharmacyConfig
import ir.darookhaneh.stock.core.model.pharmacy.TimeProvider
import kotlinx.coroutines.flow.first
import kotlinx.coroutines.test.runTest
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
 * شش تست هستهٔ فاز B — روی Room واقعی (in-memory) و بدون هیچ شبکه‌ای.
 *
 * هر تست دقیقاً یکی از gateهای مورد توافق را می‌سنجد:
 * 1) ثبت دارو بدون IRC
 * 2) ایجاد بچ + رد بچ تکراری
 * 3) RECEIVE
 * 4) DISPENSE
 * 5) ممنوعیت موجودی منفی (نه quantity و نه event تغییر نمی‌کند)
 * 6) مسیر آفلاین کد ناشناخته
 */
@RunWith(RobolectricTestRunner::class)
@Config(sdk = [34])
class PharmacyCoreTest {

    private var fakeNow = 1_700_000_000_000L
    private val timeProvider = TimeProvider { fakeNow }

    private lateinit var db: AppDatabase
    private lateinit var drugRepository: DrugRepositoryImpl
    private lateinit var batchRepository: BatchRepositoryImpl
    private lateinit var inventoryRepository: InventoryRepositoryImpl
    private lateinit var createDrug: CreateDrugWithStockUseCase
    private lateinit var addBatch: AddBatchUseCase
    private lateinit var recordEvent: RecordInventoryEventUseCase
    private lateinit var resolveScannedCode: ResolveScannedCodeUseCase

    @Before
    fun setUp() {
        val context = ApplicationProvider.getApplicationContext<Context>()
        db = Room.inMemoryDatabaseBuilder(context, AppDatabase::class.java)
            .allowMainThreadQueries()
            .build()

        drugRepository = DrugRepositoryImpl(
            drugDao = db.drugDao(),
            timeProvider = timeProvider,
            config = PharmacyConfig(),
        )
        batchRepository = BatchRepositoryImpl(db.batchDao(), timeProvider)
        inventoryRepository = InventoryRepositoryImpl(
            batchDao = db.batchDao(),
            inventoryEventDao = db.inventoryEventDao(),
            transactionRunner = RoomTransactionRunner(db),
            timeProvider = timeProvider,
        )
        createDrug = CreateDrugWithStockUseCase(drugRepository, batchRepository, inventoryRepository)
        addBatch = AddBatchUseCase(drugRepository, batchRepository)
        recordEvent = RecordInventoryEventUseCase(batchRepository, inventoryRepository)
        resolveScannedCode = ResolveScannedCodeUseCase(drugRepository)
    }

    @After
    fun tearDown() {
        db.close()
    }

    // ------------------------------------------------------------ ۱) بدون IRC

    @Test
    fun `۱ دارو بدون IRC و بدون شبکه ثبت می‌شود`() = runTest {
        val drugId = createDrug(
            name = "آموکسی‌سیلین ۵۰۰",
            genericName = "آموکسی‌سیلین",
            strength = "500mg",
            dosageForm = "کپسول",
            irc = null,
        )

        val stored = drugRepository.getById(drugId)
        assertNotNull(stored)
        assertEquals("آموکسی‌سیلین ۵۰۰", stored!!.name)
        assertNull(stored.irc)

        // داروی دوم هم می‌تواند IRC نداشته باشد (بدون UNIQUE روی IRC)
        val secondId = createDrug(name = "استامینوفن")
        assertNull(drugRepository.getById(secondId)!!.irc)
        assertTrue(drugId != secondId)
    }

    @Test
    fun `نام خالی باعث ساخته‌شدن رکورد نمی‌شود`() = runTest {
        val failure = runCatching { createDrug(name = "  ") }.exceptionOrNull()
        assertTrue(failure is PharmacyException)
        assertEquals(PharmacyError.BlankDrugName, (failure as PharmacyException).error)
        assertEquals(0, db.drugDao().observeDrugCount().first())
    }

    // --------------------------------------------------------------- ۲) بچ

    @Test
    fun `۲ بچ ساخته می‌شود و ترکیب تکراری رد می‌شود`() = runTest {
        val drugId = createDrug(name = "ایبوپروفن")
        val expiry = 1_900_000_000_000L

        val batchId = addBatch(drugId, batchNumber = "B-100", expiryDate = expiry)
        assertTrue(batchId > 0)

        val duplicate = runCatching { addBatch(drugId, batchNumber = "B-100", expiryDate = expiry) }
        assertTrue(duplicate.exceptionOrNull() is PharmacyException)
        assertEquals(
            PharmacyError.DuplicateBatch,
            (duplicate.exceptionOrNull() as PharmacyException).error,
        )
        assertEquals(1, db.batchDao().getByDrug(drugId).size)
    }

    @Test
    fun `بچ بی‌نام و بی‌تاریخ انقضا ساخته نمی‌شود`() = runTest {
        val drugId = createDrug(name = "متال‌گیر")
        val failure = runCatching { addBatch(drugId, batchNumber = null, expiryDate = null) }
        assertEquals(
            PharmacyError.MissingBatchIdentity,
            (failure.exceptionOrNull() as PharmacyException).error,
        )
        assertEquals(0, db.batchDao().getByDrug(drugId).size)
    }

    // ---------------------------------------------------------- ۳) ورود کالا

    @Test
    fun `۳ رویداد RECEIVE مقدار بچ را زیاد می‌کند و رخداد ثبت می‌شود`() = runTest {
        val drugId = createDrug(name = "سِفیکسیم")
        val batchId = addBatch(drugId, batchNumber = "R-1", expiryDate = 1_900_000_000_000L)

        recordEvent(batchId, InventoryEventType.RECEIVE, 20, note = "خرید")
        recordEvent(batchId, InventoryEventType.RECEIVE, 5)

        assertEquals(25, batchRepository.getById(batchId)!!.quantity)

        val events = inventoryRepository.observeEvents(batchId).first()
        assertEquals(2, events.size)
        assertTrue(events.all { it.type == InventoryEventType.RECEIVE })
        assertEquals(25, events.sumOf { it.quantityDelta })
    }

    // --------------------------------------------------------- ۴) خروج کالا

    @Test
    fun `۴ رویداد DISPENSE مقدار را درست کم می‌کند`() = runTest {
        val drugId = createDrug(name = "دیازپام")
        val batchId = addBatch(drugId, batchNumber = "D-1", expiryDate = 1_900_000_000_000L)
        recordEvent(batchId, InventoryEventType.RECEIVE, 30)

        recordEvent(batchId, InventoryEventType.DISPENSE, 12, note = "نسخه")

        assertEquals(18, batchRepository.getById(batchId)!!.quantity)
        val events = inventoryRepository.observeEvents(batchId).first()
        assertEquals(-12, events.first().quantityDelta)
        assertEquals(18, events.sumOf { it.quantityDelta })
    }

    @Test
    fun `ADJUSTMENT اصلاح دستی را درست اعمال می‌کند`() = runTest {
        val drugId = createDrug(name = "پنتوپرازول")
        val batchId = addBatch(drugId, batchNumber = "A-1", expiryDate = 1_900_000_000_000L)
        recordEvent(batchId, InventoryEventType.RECEIVE, 50)

        recordEvent(batchId, InventoryEventType.ADJUSTMENT, -3, note = "شکسته")
        assertEquals(47, batchRepository.getById(batchId)!!.quantity)

        recordEvent(batchId, InventoryEventType.ADJUSTMENT, 2, note = "اصلاح شمارش")
        assertEquals(49, batchRepository.getById(batchId)!!.quantity)
    }

    // ------------------------------------------------- ۵) ممنوعیت موجودی منفی

    @Test
    fun `۵ خروج بیش از موجودی نه quantity و نه event را تغییر نمی‌دهد`() = runTest {
        val drugId = createDrug(name = "انسولین")
        val batchId = addBatch(drugId, batchNumber = "I-1", expiryDate = 1_900_000_000_000L)
        recordEvent(batchId, InventoryEventType.RECEIVE, 4)

        val before = batchRepository.getById(batchId)!!.quantity
        val eventsBefore = inventoryRepository.observeEvents(batchId).first().size

        val failure = runCatching { recordEvent(batchId, InventoryEventType.DISPENSE, 5) }
        assertTrue(failure.exceptionOrNull() is PharmacyException)
        assertEquals(
            PharmacyError.InsufficientStock,
            (failure.exceptionOrNull() as PharmacyException).error,
        )

        assertEquals(before, batchRepository.getById(batchId)!!.quantity)
        assertEquals(eventsBefore, inventoryRepository.observeEvents(batchId).first().size)
    }

    @Test
    fun `۵ اصلاح منفی که موجودی را زیر صفر ببرد انجام نمی‌شود`() = runTest {
        val drugId = createDrug(name = "وارفارین")
        val batchId = addBatch(drugId, batchNumber = "W-1", expiryDate = 1_900_000_000_000L)
        recordEvent(batchId, InventoryEventType.RECEIVE, 2)
        val eventsBefore = inventoryRepository.observeEvents(batchId).first().size

        val failure = runCatching { recordEvent(batchId, InventoryEventType.ADJUSTMENT, -3) }
        assertEquals(
            PharmacyError.NegativeQuantity,
            (failure.exceptionOrNull() as PharmacyException).error,
        )

        assertEquals(2, batchRepository.getById(batchId)!!.quantity)
        assertEquals(eventsBefore, inventoryRepository.observeEvents(batchId).first().size)
    }

    @Test
    fun `رخداد برای بچ ناموجود ثبت نمی‌شود`() = runTest {
        val failure = runCatching {
            recordEvent(batchId = 9999, type = InventoryEventType.RECEIVE, amount = 1)
        }
        assertEquals(
            PharmacyError.BatchNotFound,
            (failure.exceptionOrNull() as PharmacyException).error,
        )
    }

    // -------------------------------------------------- ۶) مسیر آفلاین اسکن

    @Test
    fun `۶ کد ناشناخته هیچ دارویی برنمی‌گرداند و ثبت دستی کار می‌کند`() = runTest {
        val unknown = "6260000000000"

        assertNull(resolveScannedCode(unknown))

        // مسیر جایگزین: ثبت دستی — بدون هیچ فراخوانی شبکه‌ای.
        val drugId = createDrug(
            name = "داروی دستی",
            gtin = unknown,
            batchNumber = "M-1",
            expiryDate = 1_900_000_000_000L,
            initialQuantity = 3,
        )

        val found = resolveScannedCode(unknown)
        assertNotNull(found)
        assertEquals(drugId, found!!.id)

        val batches = batchRepository.observeByDrug(drugId).first()
        assertEquals(1, batches.size)
        assertEquals(3, batches.first().quantity)
    }

    @Test
    fun `جست‌وجوی کد با GTIN موجود، محلی و بدون شبکه نتیجه می‌دهد`() = runTest {
        val gtin = "6260000000017"
        val drugId = createDrug(name = "قطره چشمی", gtin = gtin)

        assertEquals(drugId, resolveScannedCode(gtin)!!.id)
        assertEquals(drugId, drugRepository.findByGtin(gtin)!!.id)
    }
}
