package ir.darookhaneh.stock.core.data.pharmacy

import ir.darookhaneh.stock.core.model.pharmacy.LookupException
import ir.darookhaneh.stock.core.model.pharmacy.LookupFailure
import ir.darookhaneh.stock.core.network.ttac.TtacKind
import ir.darookhaneh.stock.core.network.ttac.TtacParser
import org.junit.Assert.assertEquals
import org.junit.Assert.assertFalse
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

/**
 * تست پارس پاسخ تیتک — بدون هیچ درخواست شبکه‌ای.
 *
 * چرا جدا از شبکه: منطق «کدام اندپوینت، چه فیلدی، چه خطایی» جایی است که واقعاً
 * خراب می‌شود؛ خودِ HTTP را سرور تست می‌کند.
 */
class TtacParserTest {

    private val realisticBody = """
        {
          "ErrorCode": 0,
          "Message": "",
          "Result": {
            "PersianName": "استامینوفن ۵۰۰ میلی‌گرم",
            "EnglishName": "ACETAMINOPHEN 500MG",
            "Gtin": "06260000000001",
            "Irc": "1234567890123456",
            "Price": "12500",
            "Manufacturer": "شرکت داروسازی نمونه",
            "StatusCode": 0,
            "StatusMessage": ""
          }
        }
    """.trimIndent()

    @Test
    fun `کد ۱۴ رقمی به اندپوینت بارکد می‌رود`() {
        val url = TtacParser.buildLookupUrl("62600000000001", deviceId = "dev-1")
        assertTrue(url.contains("WrapperV2/CheckBarcode?barcode=62600000000001"))
        assertTrue(url.contains("deviceIdentifier=dev-1"))
        assertTrue(url.contains("VersionCode=60031"))
    }

    @Test
    fun `کد ۱۶ رقمی به اندپوینت کد اصالت می‌رود`() {
        val url = TtacParser.buildLookupUrl("1234567890123456")
        assertTrue(url.contains("WrapperV2/CheckSixteenCode?sixteenCode=1234567890123456"))
    }

    @Test
    fun `کد ۲۰ رقمی به اندپوینت UID می‌رود`() {
        val url = TtacParser.buildLookupUrl("12345678901234567890")
        assertTrue(url.contains("WrapperV2/CheckUid?uidCode=12345678901234567890"))
    }

    @Test
    fun `ارقام فارسی و فاصله‌ها نرمال می‌شوند`() {
        // ارقام فارسی با جداکننده → لاتین بدون جداکننده.
        // رشتهٔ فارسی را از همان عدد لاتین می‌سازیم تا شمارش رقم‌ها دستی و خطاپذیر نباشد.
        val persian = "62600000000001".map { digit ->
            if (digit.isDigit()) '۰' + (digit - '0') else ' '
        }.joinToString("")
        assertEquals("62600000000001", TtacParser.digits(persian))
        assertEquals(TtacKind.GTIN, TtacParser.kindOf("۶۲۶۰۰۰۰۰۰۰۰۰۰۱"))
    }

    @Test
    fun `کد کوتاهتر از ۸ رقم ارزش استعلام ندارد`() {
        assertFalse(TtacParser.isLookupCandidate("1234567"))
        assertTrue(TtacParser.isLookupCandidate("62600000000001"))
    }

    @Test
    fun `پاسخ واقعی سرور به مدل تبدیل می‌شود`() {
        val result = TtacParser.parseLookup(realisticBody, "62600000000001")

        assertEquals("استامینوفن ۵۰۰ میلی‌گرم", result.name)
        assertEquals("ACETAMINOPHEN 500MG", result.englishName)
        // GTIN از خود پاسخ سرور خوانده می‌شود (با صفر پیشرو)، نه از کد پرسیده‌شده.
        assertEquals("06260000000001", result.gtin)
        assertEquals("1234567890123456", result.irc)
        assertEquals("شرکت داروسازی نمونه", result.company)
        assertEquals(12500L, result.price)
        assertEquals(0, result.statusCode)
        assertNull(result.isAuthentic)
    }

    @Test
    fun `Result به شکل آرایه هم پذیرفته می‌شود`() {
        val body = """
            {"ErrorCode":0,"Result":[{"persianname":"آموکسی‌سیلین","gtin":"62600000000002"}]}
        """.trimIndent()

        val result = TtacParser.parseLookup(body, "62600000000002")
        assertEquals("آموکسی‌سیلین", result.name)
        assertEquals("62600000000002", result.gtin)
    }

    @Test
    fun `خطای ۱۳۰۱ سرور به پیام روشن تبدیل می‌شود`() {
        val body = """{"ErrorCode":1301,"Message":"ساختار بارکد ارسالی نامعتبر است"}"""

        val error = runCatching { TtacParser.parseLookup(body, "12345678") }.exceptionOrNull()

        assertTrue(error is LookupException)
        assertEquals(LookupFailure.SERVER_ERROR, (error as LookupException).failure)
        assertTrue(error.message.contains("نامعتبر"))
    }

    @Test
    fun `پیدا نشدن کد با پیام مخصوص خودش برمی‌گردد`() {
        val body = """{"ErrorCode":0,"Result":null,"Message":"اطلاعاتی یافت نشد"}"""

        val error = runCatching { TtacParser.parseLookup(body, "99999999999999") }.exceptionOrNull()

        assertEquals(LookupFailure.NOT_FOUND, (error as LookupException).failure)
        assertTrue(error.message.contains("یافت نشد"))
    }

    @Test
    fun `پاسخ غیر JSON خطای سرور است، نه کرش`() {
        val error = runCatching { TtacParser.parseLookup("<html>500</html>", "12345678") }
            .exceptionOrNull()

        assertEquals(LookupFailure.SERVER_ERROR, (error as LookupException).failure)
    }

    @Test
    fun `کد بدون نتیجه و بدون نام خطای پیدا نشدن می‌دهد`() {
        val body = """{"ErrorCode":0,"Result":{"Gtin":"62600000000003"}}"""
        val error = runCatching { TtacParser.parseLookup(body, "62600000000003") }.exceptionOrNull()
        assertEquals(LookupFailure.NOT_FOUND, (error as LookupException).failure)
    }
}
