package ir.darookhaneh.stock.core.network.ttac

import ir.darookhaneh.stock.core.model.pharmacy.DrugLookupResult
import ir.darookhaneh.stock.core.model.pharmacy.LookupFailure
import ir.darookhaneh.stock.core.model.pharmacy.LookupException
import kotlinx.serialization.json.Json
import kotlinx.serialization.json.JsonArray
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.JsonObject
import kotlinx.serialization.json.JsonPrimitive

/**
 * ساخت آدرس و پارس پاسخ «اپ موبایل تیتک».
 *
 * منبع این جزئیات: فایل `pharmacy-inventory (3).html` که خودِ کارفرما داشت و در آن
 * اندپوینت‌ها با مهندسی معکوس `ttac-4.3.6.apk` پیدا شده بودند
 * (`WrapperV2/CheckBarcode`، `WrapperV2/CheckSixteenCode`، `WrapperV2/CheckUid`).
 *
 * این فایل **خالص** است: نه شبکه، نه اندروید، نه زمان. فقط رشته می‌گیرد و رشته/مدل
 * می‌دهد؛ به همین دلیل با تست پوشش داده می‌شود.
 */
object TtacParser {

    const val BASE_URL = "https://irfdamobile.ttac.ir/api/"

    /** همان مقادیر اپ رسمی تیتک نسخهٔ ۶.۹.۱ (نسخهٔ ۶۰۰۳۱). */
    private const val VERSION_CODE = "60031"
    private const val APP_VERSION = "6.9.1"
    private const val PLATFORM_VERSION = "30"

    /** نرمال‌سازی رقم‌ها: ارقام فارسی/عربی → لاتین، و حذف هر چیز غیررقم. */
    fun digits(raw: String?): String {
        if (raw.isNullOrEmpty()) return ""
        val out = StringBuilder(raw.length)
        for (ch in raw) {
            when (ch) {
                in '۰'..'۹' -> out.append('0' + (ch - '۰'))
                in '٠'..'٩' -> out.append('0' + (ch - '٠'))
                in '0'..'9' -> out.append(ch)
            }
        }
        return out.toString()
    }

    /** GTIN به ۱۴ رقم با صفر پیشرو. */
    fun gtin14(raw: String?): String {
        val d = digits(raw)
        if (d.isEmpty()) return ""
        return if (d.length >= 14) d.takeLast(14) else d.padStart(14, '0')
    }

    /** نوع کد بر اساس طول رقم‌ها — همان قاعدهٔ نسخهٔ HTML. */
    fun kindOf(code: String): TtacKind {
        val d = digits(code)
        return when {
            d.length >= 21 -> TtacKind.GS1
            d.length == 20 -> TtacKind.UID
            d.length == 16 -> TtacKind.AUTH_16
            d.length in 8..15 -> TtacKind.GTIN
            else -> TtacKind.UNKNOWN
        }
    }

    /** آیا این کد ارزش استعلام دارد؟ (۸ رقم یا بیشتر) */
    fun isLookupCandidate(code: String?): Boolean = digits(code).length >= 8

    /**
     * آدرس کامل استعلام.
     *
     * @param deviceId شناسهٔ ساختگی دستگاه؛ اپ رسمی هم یک رشتهٔ تصادفی می‌فرستد و
     *   برای این اندپوینت‌ها احراز هویتی لازم نیست.
     */
    fun buildLookupUrl(
        code: String,
        deviceId: String = "a-stock-android",
        baseUrl: String = BASE_URL,
    ): String {
        val d = digits(code)
        val encoded = java.net.URLEncoder.encode(d, "UTF-8")
        val path = when (kindOf(d)) {
            TtacKind.UID -> "WrapperV2/CheckUid?uidCode=$encoded"
            TtacKind.AUTH_16 -> "WrapperV2/CheckSixteenCode?sixteenCode=$encoded"
            else -> "WrapperV2/CheckBarcode?barcode=$encoded"
        }
        val safeBase = if (baseUrl.endsWith("/")) baseUrl else "$baseUrl/"
        return safeBase + path +
            "&latitude=0.0&longitude=0.0&device=2" +
            "&deviceIdentifier=" + java.net.URLEncoder.encode(deviceId, "UTF-8") +
            "&Platform=1&PlatformVersion=$PLATFORM_VERSION" +
            "&VersionCode=$VERSION_CODE&AppVersion=$APP_VERSION"
    }

    /**
     * پارس پاسخ استعلام.
     *
     * ساختار واقعی: `{ "Result": { persianname, irc, gtin, … }, "ErrorCode": 0 }`
     * ولی سرور گاهی `Result` را آرایه می‌دهد و گاهی خطا را با HTTP 500 و بدنهٔ JSON
     * برمی‌گرداند؛ برای همین پارس تحمل‌پذیر است و روی بدنهٔ HTTP هم کار می‌کند.
     *
     * @throws LookupException اگر پاسخ «پیدا نشد» یا «خطای سرور» باشد.
     */
    fun parseLookup(body: String?, term: String): DrugLookupResult {
        val text = body?.trim().orEmpty()
        if (text.isEmpty() || (text.first() != '{' && text.first() != '[')) {
            throw LookupException(LookupFailure.SERVER_ERROR, "پاسخ سامانه قابل خواندن نبود.")
        }
        val root = runCatching { Json.parseToJsonElement(text) }.getOrNull()
            ?: throw LookupException(LookupFailure.SERVER_ERROR, "پاسخ سامانه JSON معتبر نبود.")

        val top = root.asObjectOrNull()
        val errorCode = top?.get("ErrorCode")?.asIntOrNull() ?: top?.get("errorcode")?.asIntOrNull()

        val resultElement = top?.get("Result") ?: top?.get("result") ?: root
        val result = when {
            resultElement is JsonArray -> resultElement.firstOrNull()?.asObjectOrNull()?.let(::lowercaseKeys)
            resultElement is JsonObject -> lowercaseKeys(resultElement)
            else -> null
        }

        if (result == null) {
            val message = top?.get("Message")?.asStringOrNull()
                ?: top?.get("message")?.asStringOrNull()
            throw if (errorCode == null || errorCode == 0) {
                LookupException(
                    LookupFailure.NOT_FOUND,
                    message?.takeIf { it.isNotBlank() } ?: "این کد در سامانهٔ تیتک پیدا نشد.",
                )
            } else {
                LookupException(
                    LookupFailure.SERVER_ERROR,
                    message?.takeIf { it.isNotBlank() } ?: "سامانه خطا داد (کد $errorCode).",
                )
            }
        }

        val name = result.str("persianname") ?: result.str("englishname")
            ?: throw LookupException(LookupFailure.NOT_FOUND, "این کد در سامانهٔ تیتک پیدا نشد.")

        val codeDigits = digits(term)
        return DrugLookupResult(
            code = codeDigits,
            name = name,
            englishName = result.str("englishname"),
            gtin = result.str("gtin")?.let { value -> gtin14(value).ifBlank { null } }
                ?: if (codeDigits.length in 8..14) gtin14(codeDigits) else null,
            irc = result.str("irc"),
            company = result.str("manufacturer")
                ?: result.str("importer")
                ?: result.str("distributer"),
            price = result.str("price")?.filter { it.isDigit() }?.toLongOrNull(),
            statusCode = result.int("statuscode"),
            statusMessage = result.str("statusmessage"),
            fetchedAt = System.currentTimeMillis(),
        )
    }

    private fun JsonElement.asObjectOrNull(): JsonObject? = this as? JsonObject

    private fun JsonElement.asIntOrNull(): Int? =
        (this as? JsonPrimitive)?.content?.trim()?.toIntOrNull()

    private fun JsonElement.asStringOrNull(): String? =
        (this as? JsonPrimitive)?.content

    private fun JsonObject.str(key: String): String? =
        // نیم‌فاصله (U+200C) حذف نمی‌شود: در فارسی درست است و حذفش نام دارو را خراب می‌کند.
        this[key]?.asStringOrNull()?.trim()?.takeIf { it.isNotEmpty() }

    private fun JsonObject.int(key: String): Int? = this[key]?.asIntOrNull()

    /** کلیدها را کوچک می‌کند تا تفاوت حروف بزرگ/کوچک سرور مهم نباشد. */
    private fun lowercaseKeys(obj: JsonObject): JsonObject =
        JsonObject(obj.entries.associate { (k, v) -> k.lowercase() to v })
}

enum class TtacKind {
    GS1,
    UID,
    AUTH_16,
    GTIN,
    UNKNOWN,
}
