package ir.darookhaneh.stock.core.database.dao

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.Query
import ir.darookhaneh.stock.core.database.entity.HistoryRow
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

    /**
     * تاریخچهٔ سراسری با نام دارو و اطلاعات بچ.
     * ORDER BY createdAt DESC تا جدیدترین رخداد اول باشد (همان رفتار نسخهٔ HTML).
     */
    @Query(
        """
        SELECT e.id AS eventId,
               e.batchId AS batchId,
               d.id AS drugId,
               d.name AS drugName,
               b.batchNumber AS batchNumber,
               b.expiryDate AS expiryDate,
               e.type AS type,
               e.quantityDelta AS quantityDelta,
               e.note AS note,
               e.createdAt AS createdAt,
               b.quantity AS batchQuantity,
               d.packSize AS packSize
        FROM inventory_event e
        JOIN batch b ON b.id = e.batchId
        JOIN drug d ON d.id = b.drugId
        ORDER BY e.createdAt DESC, e.id DESC
        LIMIT :limit
        """
    )
    fun observeHistory(limit: Int = 500): Flow<List<HistoryRow>>

    @Query(
        """
        SELECT e.id AS eventId,
               e.batchId AS batchId,
               d.id AS drugId,
               d.name AS drugName,
               b.batchNumber AS batchNumber,
               b.expiryDate AS expiryDate,
               e.type AS type,
               e.quantityDelta AS quantityDelta,
               e.note AS note,
               e.createdAt AS createdAt,
               b.quantity AS batchQuantity,
               d.packSize AS packSize
        FROM inventory_event e
        JOIN batch b ON b.id = e.batchId
        JOIN drug d ON d.id = b.drugId
        WHERE d.name LIKE '%' || :query || '%'
           OR IFNULL(b.batchNumber, '') LIKE '%' || :query || '%'
           OR IFNULL(e.note, '') LIKE '%' || :query || '%'
        ORDER BY e.createdAt DESC, e.id DESC
        LIMIT :limit
        """
    )
    fun observeHistoryFiltered(query: String, limit: Int = 500): Flow<List<HistoryRow>>

    @Query("SELECT IFNULL(SUM(quantityDelta), 0) FROM inventory_event WHERE batchId = :batchId")
    suspend fun netDeltaForBatch(batchId: Long): Int
}
