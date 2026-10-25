package ir.darookhaneh.stock.core.domain.pharmacy

import ir.darookhaneh.stock.core.model.pharmacy.InventoryEventType
import org.junit.Assert.assertEquals
import org.junit.Assert.assertNotNull
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

/**
 * تست قواعد خالص دامنه — بدون Android، بدون Room، بدون شبکه.
 * این‌ها همان قواعدی هستند که لایهٔ داده و UI روی آن‌ها تکیه می‌کنند.
 */
class PharmacyRulesTest {

    // ---------------------------------------------------------------- دارو

    @Test
    fun `دارو با نام معتبر و بدون IRC پذیرفته می‌شود`() {
        assertNull(DrugRules.validateName("آموکسی‌سیلین"))
        assertNull(DrugRules.normalizeIrc(null))
    }

    @Test
    fun `نام خالی یا تک‌حرفی رد می‌شود`() {
        assertEquals(PharmacyError.BlankDrugName, DrugRules.validateName(""))
        assertEquals(PharmacyError.BlankDrugName, DrugRules.validateName("   "))
        assertEquals(PharmacyError.BlankDrugName, DrugRules.validateName("آ"))
    }

    @Test
    fun `IRC خالی به null تبدیل می‌شود و اجباری نیست`() {
        assertNull(DrugRules.normalizeIrc(""))
        assertNull(DrugRules.normalizeIrc("   "))
        assertNull(DrugRules.normalizeIrc(null))
        assertEquals("1234567890", DrugRules.normalizeIrc(" 1234567890 "))
    }

    // ---------------------------------------------------------------- بچ

    @Test
    fun `بچ بدون شماره و بدون تاریخ انقضا رد می‌شود`() {
        assertEquals(
            PharmacyError.MissingBatchIdentity,
            BatchRules.validateIdentity(batchNumber = null, expiryDate = null),
        )
        assertEquals(
            PharmacyError.MissingBatchIdentity,
            BatchRules.validateIdentity(batchNumber = "   ", expiryDate = null),
        )
    }

    @Test
    fun `بچ با شماره یا با تاریخ انقضا پذیرفته می‌شود`() {
        assertNull(BatchRules.validateIdentity(batchNumber = "B-11", expiryDate = null))
        assertNull(BatchRules.validateIdentity(batchNumber = null, expiryDate = 1_800_000_000_000L))
    }

    @Test
    fun `کلید یکتایی بچ برای حالت‌های تهی هم پایدار است`() {
        assertEquals("B-11|-1", BatchRules.identityKey(" B-11 ", null))
        assertEquals("|-1", BatchRules.identityKey(null, null))
        assertTrue(BatchRules.identityKey("B-11", 5L) != BatchRules.identityKey("B-11", 6L))
    }

    // ------------------------------------------------------------ موجودی

    @Test
    fun `RECEIVE مقدار را افزایش می‌دهد`() {
        val result = InventoryRules.quantityAfter(10, InventoryEventType.RECEIVE, 5)
        assertEquals(15, result.getOrThrow())
    }

    @Test
    fun `DISPENSE مقدار را کاهش می‌دهد`() {
        val result = InventoryRules.quantityAfter(10, InventoryEventType.DISPENSE, 4)
        assertEquals(6, result.getOrThrow())
    }

    @Test
    fun `DISPENSE بیش از موجودی رد می‌شود`() {
        val result = InventoryRules.quantityAfter(3, InventoryEventType.DISPENSE, 4)
        assertTrue(result.isFailure)
        assertEquals(
            PharmacyError.InsufficientStock,
            (result.exceptionOrNull() as PharmacyException).error,
        )
    }

    @Test
    fun `ADJUSTMENT منفی که موجودی را زیر صفر ببرد رد می‌شود`() {
        val result = InventoryRules.quantityAfter(2, InventoryEventType.ADJUSTMENT, -3)
        assertTrue(result.isFailure)
        assertEquals(
            PharmacyError.NegativeQuantity,
            (result.exceptionOrNull() as PharmacyException).error,
        )
    }

    @Test
    fun `COUNT مقدار شمارش‌شده را جایگزین می‌کند`() {
        assertEquals(7, InventoryRules.quantityAfter(10, InventoryEventType.COUNT, 7).getOrThrow())
        assertTrue(InventoryRules.quantityAfter(10, InventoryEventType.COUNT, -1).isFailure)
    }

    @Test
    fun `مقدار صفر یا منفی برای ورود و خروج نامعتبر است`() {
        assertTrue(InventoryRules.quantityAfter(5, InventoryEventType.RECEIVE, 0).isFailure)
        assertTrue(InventoryRules.quantityAfter(5, InventoryEventType.DISPENSE, -2).isFailure)
        assertTrue(InventoryRules.quantityAfter(5, InventoryEventType.ADJUSTMENT, 0).isFailure)
    }

    @Test
    fun `تغییر خالص برای ثبت رخداد درست محاسبه می‌شود`() {
        assertEquals(5, InventoryRules.delta(10, 15))
        assertEquals(-4, InventoryRules.delta(10, 6))
        assertEquals(-3, InventoryRules.delta(10, 7))
    }

    @Test
    fun `موجودی منفی فعلی هرگز مبنای عملیات نیست`() {
        val result = InventoryRules.quantityAfter(-1, InventoryEventType.RECEIVE, 5)
        assertTrue(result.isFailure)
        assertNotNull(result.exceptionOrNull())
    }
}
