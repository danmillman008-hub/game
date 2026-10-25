package ir.darookhaneh.stock.core.database.dao

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.Query
import ir.darookhaneh.stock.core.database.entity.InventoryEventEntity
import kotlinx.coroutines.flow.Flow

@Dao
interface InventoryEventDao {

    @Insert
    suspend fun insert(event: InventoryEventEntity): Long

    @Query("SELECT * FROM inventory_event WHERE batchId = :batchId ORDER BY createdAt DESC, id DESC")
    fun observeByBatch(batchId: Long): Flow<List<InventoryEventEntity>>

    @Query("SELECT * FROM inventory_event ORDER BY createdAt DESC, id DESC LIMIT :limit")
    fun observeRecent(limit: Int = 50): Flow<List<InventoryEventEntity>>

    @Query("SELECT IFNULL(SUM(quantityDelta), 0) FROM inventory_event WHERE batchId = :batchId")
    suspend fun netDeltaForBatch(batchId: Long): Int
}
