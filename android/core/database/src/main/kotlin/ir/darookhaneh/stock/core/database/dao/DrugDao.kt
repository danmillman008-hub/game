package ir.darookhaneh.stock.core.database.dao

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import androidx.room.Update
import ir.darookhaneh.stock.core.database.entity.DrugEntity
import ir.darookhaneh.stock.core.database.entity.DrugSummaryRow
import kotlinx.coroutines.flow.Flow

@Dao
interface DrugDao {

    @Insert(onConflict = OnConflictStrategy.ABORT)
    suspend fun insert(drug: DrugEntity): Long

    @Update
    suspend fun update(drug: DrugEntity)

    @Query("DELETE FROM drug WHERE id = :drugId")
    suspend fun deleteById(drugId: Long)

    @Query("SELECT * FROM drug WHERE id = :drugId LIMIT 1")
    suspend fun getById(drugId: Long): DrugEntity?

    @Query("SELECT * FROM drug WHERE id = :drugId LIMIT 1")
    fun observeById(drugId: Long): Flow<DrugEntity?>

    /** دقیق‌ترین یافته برای اسکن: بارکد تجاری. */
    @Query("SELECT * FROM drug WHERE gtin = :gtin ORDER BY id LIMIT 1")
    suspend fun findByGtin(gtin: String): DrugEntity?

    /** IRC کمکی است، نه کلید؛ پس اولین تطابق کافی است. */
    @Query("SELECT * FROM drug WHERE irc = :irc ORDER BY id LIMIT 1")
    suspend fun findByIrc(irc: String): DrugEntity?

    @Query(
        """
        SELECT * FROM drug
        WHERE name LIKE '%' || :query || '%'
           OR IFNULL(genericName, '') LIKE '%' || :query || '%'
           OR IFNULL(gtin, '') LIKE '%' || :query || '%'
           OR IFNULL(irc, '') LIKE '%' || :query || '%'
        ORDER BY name COLLATE NOCASE ASC
        LIMIT :limit
        """
    )
    suspend fun search(query: String, limit: Int = 100): List<DrugEntity>

    /**
     * فهرست داروها با جمع موجودی.
     * LEFT JOIN تا داروی بدون بچ هم نمایش داده شود.
     */
    @Query(
        """
        SELECT d.id AS id,
               d.name AS name,
               d.genericName AS genericName,
               d.strength AS strength,
               d.dosageForm AS dosageForm,
               d.gtin AS gtin,
               d.irc AS irc,
               IFNULL(SUM(b.quantity), 0) AS totalQuantity,
               COUNT(b.id) AS batchCount,
               MIN(b.expiryDate) AS nearestExpiry
        FROM drug d
        LEFT JOIN batch b ON b.drugId = d.id
        GROUP BY d.id
        ORDER BY d.name COLLATE NOCASE ASC
        """
    )
    fun observeSummaries(): Flow<List<DrugSummaryRow>>

    @Query(
        """
        SELECT d.id AS id,
               d.name AS name,
               d.genericName AS genericName,
               d.strength AS strength,
               d.dosageForm AS dosageForm,
               d.gtin AS gtin,
               d.irc AS irc,
               IFNULL(SUM(b.quantity), 0) AS totalQuantity,
               COUNT(b.id) AS batchCount,
               MIN(b.expiryDate) AS nearestExpiry
        FROM drug d
        LEFT JOIN batch b ON b.drugId = d.id
        WHERE d.name LIKE '%' || :query || '%'
           OR IFNULL(d.genericName, '') LIKE '%' || :query || '%'
           OR IFNULL(d.gtin, '') LIKE '%' || :query || '%'
           OR IFNULL(d.irc, '') LIKE '%' || :query || '%'
        GROUP BY d.id
        ORDER BY d.name COLLATE NOCASE ASC
        """
    )
    fun observeSummariesFiltered(query: String): Flow<List<DrugSummaryRow>>

    @Query("SELECT COUNT(*) FROM drug")
    fun observeDrugCount(): Flow<Int>

    @Query("SELECT IFNULL(SUM(quantity), 0) FROM batch")
    fun observeTotalUnits(): Flow<Int>
}
