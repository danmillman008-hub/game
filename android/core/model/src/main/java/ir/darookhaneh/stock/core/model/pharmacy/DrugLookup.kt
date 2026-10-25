package ir.darookhaneh.stock.core.model.pharmacy

/**
 * نتیجهٔ استعلام کد دارو از سامانهٔ تیتک (یا حافظهٔ محلی همان استعلام‌ها).
 *
 * چرا در مدل است: هم لایهٔ شبکه، هم لایهٔ داده (کش) و هم UI به همین شکل واحد
 * کار می‌کنند و هیچ‌کدام به JSON خام سرور وابسته نیستند.
 */
data class DrugLookupResult(
    /** کدی که استعلام شد (نرمال‌شده: فقط رقم). */
    val code: String,
    val name: String,
    val englishName: String? = null,
    val gtin: String? = null,
    val irc: String? = null,
    val company: String? = null,
    val price: Long? = null,
    /** کد وضعیت اصالت تیتک؛ تفسیرش در [DrugLookupStatus] است. */
    val statusCode: Int? = null,
    val statusMessage: String? = null,
    val source: LookupSource = LookupSource.NETWORK,
    val fetchedAt: Long = 0L,
) {
    /** آیا وضعیت اصالت را می‌دانیم و «تأییدشده» است؟ */
    val isAuthentic: Boolean? get() = when (statusCode) {
        null -> null
        0 -> null
        in 1..99 -> true
        else -> false
    }
}

/**
 * منبع آنلاین استعلام.
 *
 * چرا رابط و نه کلاس مشخص: لایهٔ داده باید بدون شبکه هم تست شود (فیک در تست‌ها)،
 * و ماژول شبکه نباید مجبور شود به لایهٔ دامنه وابسته باشد.
 */
interface DrugLookupRemote {
    /** @throws LookupException در صورت شکست شبکه/سرور/پیدا نشدن. */
    suspend fun lookup(code: String): DrugLookupResult
}

enum class LookupSource {
    /** تازه از سرور تیتک گرفته شد. */
    NETWORK,

    /** از حافظهٔ محلی؛ بدون هیچ درخواست شبکه‌ای. */
    CACHE,
}

/** دلیل شکست استعلام — برای پیام فارسی و تصمیم UI. */
enum class LookupFailure {
    /** کد از نظر شکل معتبر نیست (مثلاً کمتر از ۸ رقم). */
    INVALID_CODE,

    /** دستگاه به اینترنت/سرور دسترسی نداشت. */
    NO_CONNECTION,

    /** سرور پاسخ نداد در زمان مجاز. */
    TIMEOUT,

    /** کد در سامانه پیدا نشد. */
    NOT_FOUND,

    /** سرور خطا داد یا پاسخ قابل‌فهم نبود. */
    SERVER_ERROR,
}

/** خطای استعلام با پیام آمادهٔ نمایش. */
class LookupException(
    val failure: LookupFailure,
    override val message: String,
) : Exception(message)
