package ir.darookhaneh.stock.core.network.ttac

import ir.darookhaneh.stock.core.model.pharmacy.DrugLookupRemote
import ir.darookhaneh.stock.core.model.pharmacy.DrugLookupResult
import ir.darookhaneh.stock.core.model.pharmacy.LookupException
import ir.darookhaneh.stock.core.model.pharmacy.LookupFailure
import kotlinx.coroutines.CoroutineDispatcher
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import okhttp3.OkHttpClient
import okhttp3.Request
import java.io.IOException
import java.net.SocketTimeoutException
import java.net.UnknownHostException

/**
 * کلاینت استعلام تیتک.
 *
 * قواعد مهم:
 * - **هیچ فراخوانی خودکاری وجود ندارد.** این کلاس فقط وقتی صدا زده می‌شود که کاربر
 *   در UI دکمهٔ «استعلام از تیتک» را بزند؛ اپ آفلاین کامل کار می‌کند.
 * - خطاها به [LookupException] با پیام فارسی تبدیل می‌شوند تا UI تصمیم بگیرد.
 * - سرور تیتک خطا را با HTTP 500 و بدنهٔ JSON می‌فرستد؛ پس بدنه حتی روی کد خطا
 *   پارس می‌شود.
 */
class TtacApi(
    private val client: OkHttpClient,
    private val dispatcher: CoroutineDispatcher = Dispatchers.IO,
    private val baseUrl: String = TtacParser.BASE_URL,
) : DrugLookupRemote {

    override suspend fun lookup(code: String): DrugLookupResult = withContext(dispatcher) {
        if (!TtacParser.isLookupCandidate(code)) {
            throw LookupException(LookupFailure.INVALID_CODE, "کد معتبر نیست؛ حداقل ۸ رقم لازم است.")
        }

        val request = Request.Builder()
            .url(TtacParser.buildLookupUrl(code = code, baseUrl = baseUrl))
            .header("Accept", "application/json, text/plain, */*")
            .get()
            .build()

        val body: String
        try {
            client.newCall(request).execute().use { response ->
                body = response.body?.string().orEmpty()
            }
        } catch (e: SocketTimeoutException) {
            throw LookupException(
                LookupFailure.TIMEOUT,
                "سامانهٔ تیتک در زمان مجاز پاسخ نداد. کمی بعد دوباره امتحان کنید.",
            )
        } catch (e: UnknownHostException) {
            throw LookupException(
                LookupFailure.NO_CONNECTION,
                "اتصال به سامانهٔ تیتک برقرار نشد. اینترنت گوشی را بررسی کنید.",
            )
        } catch (e: IOException) {
            throw LookupException(
                LookupFailure.NO_CONNECTION,
                "ارتباط با سامانهٔ تیتک قطع شد. بدون اینترنت هم ثبت دستی کار می‌کند.",
            )
        }

        TtacParser.parseLookup(body, code)
    }

    companion object {
        /** کلاینت اختصاصی: تایم‌اوت کوتاه، بدون کش HTTP. */
        fun defaultClient(): OkHttpClient = OkHttpClient.Builder()
            .connectTimeout(12, java.util.concurrent.TimeUnit.SECONDS)
            .readTimeout(12, java.util.concurrent.TimeUnit.SECONDS)
            .callTimeout(20, java.util.concurrent.TimeUnit.SECONDS)
            .retryOnConnectionFailure(true)
            .build()
    }
}
