package ir.darookhaneh.stock.core.database

import androidx.room.Database
import androidx.room.RoomDatabase
import ir.darookhaneh.stock.core.database.dao.BatchDao
import ir.darookhaneh.stock.core.database.dao.DrugDao
import ir.darookhaneh.stock.core.database.dao.InventoryEventDao
import ir.darookhaneh.stock.core.database.entity.BatchEntity
import ir.darookhaneh.stock.core.database.entity.DrugEntity
import ir.darookhaneh.stock.core.database.entity.InventoryEventEntity

@Database(
    entities = [
        DrugEntity::class,
        BatchEntity::class,
        InventoryEventEntity::class,
    ],
    version = DatabaseConstant.SCHEMA_VERSION,
    exportSchema = true,
)
abstract class AppDatabase : RoomDatabase() {
    abstract fun drugDao(): DrugDao
    abstract fun batchDao(): BatchDao
    abstract fun inventoryEventDao(): InventoryEventDao
}

object DatabaseConstant {
    /**
     * نسخهٔ ۱ = شروع تمیز محصول داروخانه‌ای.
     *
     * محصول قبلی (مدل غذایی) هرگز منتشر نشده؛ بنابراین هیچ مهاجرت داده‌ای لازم نیست
     * و اسکیمای قدیمی دور ریخته شده است (پاک‌کردن، نه مهاجرت).
     *
     * از این پس هر تغییر اسکیما: نسخه +۱ و Migration واقعی + تست مهاجرت.
     */
    const val SCHEMA_VERSION = 1
}
