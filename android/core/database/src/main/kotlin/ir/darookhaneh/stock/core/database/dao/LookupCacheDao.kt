package ir.darookhaneh.stock.core.database.dao

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import ir.darookhaneh.stock.core.database.entity.LookupCacheEntity
import kotlinx.coroutines.flow.Flow

@Dao
interface LookupCacheDao {

    @Query("SELECT * FROM lookup_cache WHERE code = :code LIMIT 1")
    suspend fun get(code: String): LookupCacheEntity?

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun upsert(entry: LookupCacheEntity)

    @Query("SELECT COUNT(*) FROM lookup_cache")
    fun observeCount(): Flow<Int>

    @Query("DELETE FROM lookup_cache")
    suspend fun clear()

    @Query("DELETE FROM lookup_cache WHERE fetchedAt < :olderThan")
    suspend fun deleteOlderThan(olderThan: Long): Int
}
