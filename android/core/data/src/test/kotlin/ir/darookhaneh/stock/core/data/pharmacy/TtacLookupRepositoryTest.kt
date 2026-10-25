package ir.darookhaneh.stock.core.data.pharmacy

import ir.darookhaneh.stock.core.database.dao.LookupCacheDao
import ir.darookhaneh.stock.core.database.entity.LookupCacheEntity
import ir.darookhaneh.stock.core.model.pharmacy.DrugLookupRemote
import ir.darookhaneh.stock.core.model.pharmacy.DrugLookupResult
import ir.darookhaneh.stock.core.model.pharmacy.LookupException
import ir.darookhaneh.stock.core.model.pharmacy.LookupFailure
import ir.darookhaneh.stock.core.model.pharmacy.LookupSource
import ir.darookhaneh.stock.core.model.pharmacy.TimeProvider
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.flowOf
import kotlinx.coroutines.runBlocking
import org.junit.Assert.assertEquals
import org.junit.Assert.assertNull
import org.junit.Assert.assertTrue
import org.junit.Test

/**
 * تست رفتار «استعلام + حافظهٔ محلی» بدون شبکه و بدون Room واقعی.
 *
 * چرا مهم است: این لایه تصمیم می‌گیرد کِی به اینترنت برود. اگر اشتباه کند، یا اپ در
 * حالت آفلاین از کار می‌افتد یا بی‌اجازه به شبکه وصل می‌شود — هر دو خلاف قاعدهٔ محصول.
 */
class TtacLookupRepositoryTest {

    private class FakeDao : LookupCacheDao {
        val rows = mutableMapOf<String, LookupCacheEntity>()
        var upsertCount = 0

        override suspend fun get(code: String): LookupCacheEntity? = rows[code]
        override suspend fun upsert(entry: LookupCacheEntity) {
            rows[entry.code] = entry
            upsertCount++
        }
        override fun observeCount(): Flow<Int> = flowOf(rows.size)
        override suspend fun clear() = rows.clear()
        override suspend fun deleteOlderThan(olderThan: Long): Int {
            val before = rows.size
            rows.entries.removeAll { it.value.fetchedAt < olderThan }
            return before - rows.size
        }
    }

    private class FakeRemote(
        private val handler: (String) -> DrugLookupResult,
    ) : DrugLookupRemote {
        var calls = 0
        override suspend fun lookup(code: String): DrugLookupResult {
            calls++
            return handler(code)
        }
    }

    private var now = 1_700_000_000_000L

    private fun repo(dao: FakeDao, remote: FakeRemote) =
        TtacLookupRepositoryImpl(remote = remote, cacheDao = dao, timeProvider = { now })

    private fun fresh(code: String = "62600000000001") = DrugLookupResult(
        code = code,
        name = "استامینوفن",
        gtin = code,
        irc = "1234567890123456",
        company = "شرکت نمونه",
        price = 12000,
        statusCode = 1,
        fetchedAt = now,
    )

    @Test
    fun `اولین استعلام از شبکه می‌آید و در حافظه ذخیره می‌شود`() = runBlocking {
        val dao = FakeDao()
        val remote = FakeRemote { fresh(it) }

        val result = repo(dao, remote).lookup("62600000000001")

        assertEquals(1, remote.calls)
        assertEquals(LookupSource.NETWORK, result.source)
        assertEquals("استامینوفن", result.name)
        assertEquals(1, dao.upsertCount)
        assertEquals("استامینوفن", dao.rows["62600000000001"]?.name)
    }

    @Test
    fun `استعلام دوم از حافظه می‌آید و شبکه صدا زده نمی‌شود`() = runBlocking {
        val dao = FakeDao()
        val remote = FakeRemote { fresh(it) }
        val repository = repo(dao, remote)

        repository.lookup("62600000000001")
        now += 60 * 60 * 1000 // یک ساعت بعد
        val second = repository.lookup("62600000000001")

        assertEquals(1, remote.calls)
        assertEquals(LookupSource.CACHE, second.source)
        assertEquals("استامینوفن", second.name)
    }

    @Test
    fun `حافظهٔ کهنه دوباره از شبکه خوانده می‌شود`() = runBlocking {
        val dao = FakeDao()
        val remote = FakeRemote { fresh(it) }
        val repository = repo(dao, remote)

        repository.lookup("62600000000001")
        now += TtacLookupRepositoryImpl.CACHE_TTL_MILLIS + 1
        repository.lookup("62600000000001")

        assertEquals(2, remote.calls)
    }

    @Test
    fun `آفلاین با وجود حافظه، نتیجهٔ قبلی برمی‌گردد`() = runBlocking {
        val dao = FakeDao()
        dao.upsert(
            LookupCacheEntity(
                code = "62600000000001",
                name = "آموکسی‌سیلین",
                gtin = "62600000000001",
                fetchedAt = now - TtacLookupRepositoryImpl.CACHE_TTL_MILLIS - 1,
            )
        )
        val remote = FakeRemote {
            throw LookupException(LookupFailure.NO_CONNECTION, "اینترنت نیست")
        }

        val result = repo(dao, remote).lookup("62600000000001")

        assertEquals(LookupSource.CACHE, result.source)
        assertEquals("آموکسی‌سیلین", result.name)
    }

    @Test
    fun `آفلاین بدون حافظه خطا می‌دهد`() = runBlocking {
        val remote = FakeRemote {
            throw LookupException(LookupFailure.NO_CONNECTION, "اینترنت نیست")
        }

        val error = runCatching { repo(FakeDao(), remote).lookup("62600000000001") }
            .exceptionOrNull()

        assertTrue(error is LookupException)
        assertEquals(LookupFailure.NO_CONNECTION, (error as LookupException).failure)
    }

    @Test
    fun `پیدا نشدن کد در حافظه ذخیره نمی‌شود`() = runBlocking {
        val dao = FakeDao()
        val remote = FakeRemote {
            throw LookupException(LookupFailure.NOT_FOUND, "پیدا نشد")
        }

        runCatching { repo(dao, remote).lookup("99999999999999") }

        assertNull(dao.rows["99999999999999"])
        assertEquals(0, dao.upsertCount)
    }

    @Test
    fun `کد کوتاه‌تر از ۸ رقم بدون شبکه رد می‌شود`() = runBlocking {
        val dao = FakeDao()
        val remote = FakeRemote { fresh(it) }

        val error = runCatching { repo(dao, remote).lookup("12345") }.exceptionOrNull()

        assertEquals(LookupFailure.INVALID_CODE, (error as LookupException).failure)
        assertEquals(0, remote.calls)
    }

    @Test
    fun `کش را می‌توان بدون شبکه خواند`() = runBlocking {
        val dao = FakeDao()
        val remote = FakeRemote { fresh(it) }
        val repository = repo(dao, remote)
        repository.lookup("62600000000001")

        val cached = repository.cached("62600000000001")

        assertEquals(LookupSource.CACHE, cached?.source)
        assertEquals(1, remote.calls)
    }
}
