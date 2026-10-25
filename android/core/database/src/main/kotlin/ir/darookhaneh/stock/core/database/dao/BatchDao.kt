package ir.darookhaneh.stock.core.database.dao

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import androidx.room.Update
import ir.darookhaneh.stock.core.database.entity.BatchEntity
import kotlinx.coroutines.flow.Flow

@Dao
interface BatchDao {

    @Insert(onConflict = OnConflictStrategy.ABORT)
    suspend fun insert(batch: BatchEntity): Long

    @Update
    suspend fun update(batch: BatchEntity)

    @Query("DELETE FROM batch WHERE id = :batchId")
    suspend fun deleteById(batchId: Long)

    @Query("SELECT * FROM batch WHERE id = :batchId LIMIT 1")
    suspend fun getById(batchId: Long): BatchEntity?

    @Query("SELECT * FROM batch WHERE id = :batchId LIMIT 1")
    fun observeById(batchId: Long): Flow<BatchEntity?>

    @Query("SELECT * FROM batch WHERE drugId = :drugId ORDER BY expiryDate IS NULL, expiryDate ASC, id ASC")
    fun observeByDrug(drugId: Long): Flow<List<BatchEntity>>

    @Query("SELECT * FROM batch WHERE drugId = :drugId ORDER BY expiryDate IS NULL, expiryDate ASC, id ASC")
    suspend fun getByDrug(drugId: Long): List<BatchEntity>

    /** برای تشخیص تکرار بچ: همان دارو + شماره بچ + تاریخ انقضا. */
    @Query(
        """
        SELECT * FROM batch
        WHERE drugId = :drugId
          AND IFNULL(batchNumber, '') = IFNULL(:batchNumber, '')
          AND IFNULL(expiryDate, -1) = IFNULL(:expiryDate, -1)
        LIMIT 1
        """
    )
    suspend fun findMatching(drugId: Long, batchNumber: String?, expiryDate: Long?): BatchEntity?

    /**
     * تغییر اتمی موجودی.
     * شرط `quantity + :delta >= 0` تضمین می‌کند هیچ‌گاه مقدار منفی ذخیره نشود؛
     * اگر صفر ردیف تغییر کند یعنی عملیات مجاز نبوده است.
     */
    @Query(
        """
        UPDATE batch
        SET quantity = quantity + :delta,
            updatedAt = :now
        WHERE id = :batchId AND quantity + :delta >= 0
        """
    )
    suspend fun applyDelta(batchId: Long, delta: Int, now: Long): Int

    @Query("SELECT COUNT(*) FROM batch WHERE expiryDate IS NOT NULL AND expiryDate < :now")
    fun observeExpiredCount(now: Long): Flow<Int>

    @Query(
        """
        SELECT COUNT(*) FROM batch
        WHERE expiryDate IS NOT NULL AND expiryDate >= :now AND expiryDate <= :until
        """
    )
    fun observeExpiringSoonCount(now: Long, until: Long): Flow<Int>

    @Query("SELECT COUNT(*) FROM batch WHERE quantity <= :threshold")
    fun observeLowStockCount(threshold: Int): Flow<Int>
}
