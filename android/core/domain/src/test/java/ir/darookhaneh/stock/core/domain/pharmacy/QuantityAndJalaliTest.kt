package ir.darookhaneh.stock.core.domain.pharmacy

import ir.darookhaneh.stock.core.model.pharmacy.CountingMode
import ir.darookhaneh.stock.core.model.pharmacy.InventoryEventType
import ir.darookhaneh.stock.core.model.pharmacy.JalaliDate
import ir.darookhaneh.stock.core.model.pharmacy.QuantityInput
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test
import java.time.LocalDate
import java.time.ZoneId

/**
 * تست هم‌ارزی با نسخهٔ HTML: سه روش شمارش و پنج نوع عملیات، به‌علاوهٔ تقویم شمسی.
 */
class QuantityAndJalaliTest {

    // ---------- روش شمارش ----------

    @Test
    fun `ورودی تکی تعداد بسته است و در تعداد هر بسته ضرب می‌شود`() {
        // ۷ جعبهٔ ۲۰ تایی = ۱۴۰ واحد (هم‌ارز نسخهٔ HTML؛ پیش‌تر ۷ واحد حساب می‌شد)
        val input = QuantityInput(mode = CountingMode.SINGLE, packs = 7)
        assertEquals(140, input.toUnits(packSize = 20))
    }

    @Test
    fun `بدون packSize هر بسته یک واحد حساب می‌شود`() {
        val input = QuantityInput(mode = CountingMode.SINGLE, packs = 7)
        assertEquals(7, input.toUnits(packSize = null))
    }

    @Test
    fun `کارتن ضرب در تعداد بسته در کارتن به‌علاوهٔ بستهٔ خارج`() {
        // ۳ کارتن × ۲۴ بسته + ۵ بسته = ۷۷ بسته = ۱۵۴۰ واحد (هر بسته ۲۰ عدد)
        val input = QuantityInput(
            mode = CountingMode.CARTON,
            cartons = 3,
            unitsPerCarton = 24,
            loosePacks = 5,
        )
        assertEquals(1540, input.toUnits(packSize = 20))
    }

    @Test
    fun `اگر تعداد بسته در کارتن وارد نشود هر کارتن یک بسته حساب می‌شود`() {
        val input = QuantityInput(mode = CountingMode.CARTON, cartons = 2)
        assertEquals(40, input.toUnits(packSize = 20))
    }

    @Test
    fun `باز و نیمه‌مصرف بسته‌های سالم به‌علاوهٔ واحدهای باز`() {
        // ۴ بستهٔ سالم × ۲۰ + ۱۲ واحد باز = ۹۲
        val input = QuantityInput(mode = CountingMode.OPEN, packs = 4, openUnits = 12)
        assertEquals(92, input.toUnits(packSize = 20))
    }

    @Test
    fun `مقدار منفی هرگز تولید نمی‌شود`() {
        val input = QuantityInput(mode = CountingMode.OPEN, packs = 0, openUnits = -5)
        assertEquals(0, input.toUnits())
    }

    @Test
    fun `ورودی خالی تشخیص داده می‌شود`() {
        assertTrue(QuantityInput().isEmpty)
        assertFalse(QuantityInput(packs = 1).isEmpty)
    }

    @Test
    fun `توضیح روش کارتن شامل تعداد کارتن است`() {
        val text = QuantityInput(mode = CountingMode.CARTON, cartons = 2, unitsPerCarton = 10).describe()
        assertEquals("2 کارتن × 10", text)
        assertNull(QuantityInput().describe())
    }

    // ---------- عملیات ----------

    @Test
    fun `ضایعات مثل خروج موجودی را کم می‌کند`() {
        val result = InventoryRules.quantityAfter(current = 10, type = InventoryEventType.DAMAGE, amount = 4)
        assertEquals(6, result.getOrThrow())
    }

    @Test
    fun `ضایعات بیش از موجودی رد می‌شود`() {
        val result = InventoryRules.quantityAfter(current = 3, type = InventoryEventType.DAMAGE, amount = 4)
        assertTrue(result.isFailure)
    }

    @Test
    fun `مرجوعی مثل ورود موجودی را زیاد می‌کند`() {
        val result = InventoryRules.quantityAfter(current = 5, type = InventoryEventType.RETURN, amount = 3)
        assertEquals(8, result.getOrThrow())
    }

    @Test
    fun `شمارش مقدار را جای‌گذاری می‌کند نه جمع`() {
        val result = InventoryRules.quantityAfter(current = 50, type = InventoryEventType.COUNT, amount = 12)
        assertEquals(12, result.getOrThrow())
    }

    // ---------- تقویم شمسی ----------

    @Test
    fun `نوروز ۱۴۰۳ برابر ۲۰ مارس ۲۰۲۴ است`() {
        val jalali = JalaliDate.from(LocalDate.of(2024, 3, 20))
        assertEquals(JalaliDate(1403, 1, 1), jalali)
        assertEquals(LocalDate.of(2024, 3, 20), jalali.toGregorian())
    }

    @Test
    fun `آخرین روز سال ۱۴۰۳ برابر ۲۰ مارس ۲۰۲۵ است`() {
        val jalali = JalaliDate.from(LocalDate.of(2025, 3, 20))
        assertEquals(JalaliDate(1403, 12, 30), jalali)
        assertEquals(LocalDate.of(2025, 3, 20), jalali.toGregorian())
    }

    @Test
    fun `تبدیل رفت و برگشت برای ۳۰ روز متوالی پایدار است`() {
        var date = LocalDate.of(2024, 1, 1)
        repeat(30) {
            val jalali = JalaliDate.from(date)
            assertEquals(date, jalali.toGregorian())
            date = date.plusDays(1)
        }
    }

    @Test
    fun `پارس ورودی فارسی و دو رقمی`() {
        assertEquals(JalaliDate(1404, 6, 31), JalaliDate.parse("۱۴۰۴/۰۶/۳۱"))
        assertEquals(JalaliDate(1404, 6, 31), JalaliDate.parse("1404-6-31"))
        assertEquals(JalaliDate(1404, 6, 31), JalaliDate.parse("14040631"))
        // سال دو رقمی
        assertEquals(1404, JalaliDate.parse("04/06/31")?.year)
        // روز خالی = آخرین روز ماه
        assertEquals(31, JalaliDate.parse("1404/6")?.day)
        assertNull(JalaliDate.parse("نامعتبر"))
        assertNull(JalaliDate.parse("1404/13/01"))
    }

    @Test
    fun `طول ماه‌های شمسی درست است`() {
        assertEquals(31, JalaliDate.monthLength(1403, 1))
        assertEquals(30, JalaliDate.monthLength(1403, 7))
        assertEquals(30, JalaliDate.monthLength(1403, 12)) // ۱۴۰۳ کبیسه است
        assertEquals(29, JalaliDate.monthLength(1402, 12))
    }

    @Test
    fun `میلی‌ثانیه تبدیل به تاریخ شمسی و برعکس`() {
        val millis = JalaliDate(1403, 1, 1).toEpochMillis(ZoneId.of("Asia/Tehran"))
        val back = JalaliDate.fromEpochMillis(millis, ZoneId.of("Asia/Tehran"))
        assertEquals(JalaliDate(1403, 1, 1), back)
    }
}
