package ir.darookhaneh.stock.core.data.pharmacy

import ir.darookhaneh.stock.core.database.dao.LookupCacheDao
import ir.darookhaneh.stock.core.database.entity.LookupCacheEntity
import ir.darookhaneh.stock.core.domain.pharmacy.repository.DrugLookupRepository
import ir.darookhaneh.stock.core.model.pharmacy.DrugLookupRemote
import ir.darookhaneh.stock.core.model.pharmacy.DrugLookupResult
import ir.darookhaneh.stock.core.model.pharmacy.LookupException
import ir.darookhaneh.stock.core.model.pharmacy.LookupFailure
import ir.darookhaneh.stock.core.model.pharmacy.LookupSource
import ir.darookhaneh.stock.core.model.pharmacy.TimeProvider

/**
 * استعلام تیتک با حافظهٔ محلی.
 *
 * رفتار:
 * 1) اگر نتیجهٔ تازه‌تر از [CACHE_TTL_MILLIS] در دیتابیس باشد، **بدون شبکه** برگردانده می‌شود.
 * 2) وگرنه یک درخواست می‌رود؛ در صورت موفقیت، نتیجه ذخیره می‌شود.
 * 3) در صورت شکست، اگر نسخهٔ کهنه در حافظه باشد همان برگردانده می‌شود (آفلاین بهتر از هیچ).
 */
class TtacLookupRepositoryImpl(
    private val remote: DrugLookupRemote,
    private val cacheDao: LookupCacheDao,
    private val timeProvider: TimeProvider,
) : DrugLookupRepository {

    override suspend fun lookup(code: String): DrugLookupResult {
        val normalized = code.filter(Char::isDigit)
        if (normalized.length < 8) {
            throw LookupException(LookupFailure.INVALID_CODE, "کد معتبر نیست؛ حداقل ۸ رقم لازم است.")
        }

        val cached = cacheDao.get(normalized)
        val now = timeProvider.now()
        if (cached != null && now - cached.fetchedAt <= CACHE_TTL_MILLIS) {
            return cached.toResult(LookupSource.CACHE)
        }

        val fresh = try {
            remote.lookup(normalized)
        } catch (e: LookupException) {
            // آفلاین: اگر نتیجهٔ قبلی داریم، همان را با برچسب «حافظه» بده.
            if (cached != null && e.failure == LookupFailure.NO_CONNECTION) {
                return cached.toResult(LookupSource.CACHE)
            }
            throw e
        }

        cacheDao.upsert(fresh.toEntity(fetchedAt = if (fresh.fetchedAt > 0) fresh.fetchedAt else now))
        return fresh.copy(source = LookupSource.NETWORK)
    }

    override suspend fun cached(code: String): DrugLookupResult? {
        val normalized = code.filter(Char::isDigit)
        return cacheDao.get(normalized)?.toResult(LookupSource.CACHE)
    }

    private fun LookupCacheEntity.toResult(source: LookupSource) = DrugLookupResult(
        code = code,
        name = name,
        englishName = englishName,
        gtin = gtin,
        irc = irc,
        company = company,
        price = price,
        statusCode = statusCode,
        statusMessage = statusMessage,
        source = source,
        fetchedAt = fetchedAt,
    )

    private fun DrugLookupResult.toEntity(fetchedAt: Long) = LookupCacheEntity(
        code = code,
        name = name,
        englishName = englishName,
        gtin = gtin,
        irc = irc,
        company = company,
        price = price,
        statusCode = statusCode,
        statusMessage = statusMessage,
        fetchedAt = fetchedAt,
    )

    companion object {
        /** ۳۰ روز: اطلاعات کاتالوگ به‌ندرت عوض می‌شود؛ اصالت با هر بار اسکن دوباره پرسیده می‌شود. */
        const val CACHE_TTL_MILLIS = 30L * 24 * 60 * 60 * 1000
    }
}
