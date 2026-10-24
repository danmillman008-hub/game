package ir.darookhaneh.stock.core.database

import androidx.room.Database
import androidx.room.RoomDatabase
import ir.darookhaneh.stock.core.database.dao.CategoryDao
import ir.darookhaneh.stock.core.database.dao.FoodDao
import ir.darookhaneh.stock.core.database.dao.SearchDao
import ir.darookhaneh.stock.core.database.entity.CategoryEntity
import ir.darookhaneh.stock.core.database.entity.FoodItemEntity
import ir.darookhaneh.stock.core.database.entity.InventoryItemFtsEntity
import ir.darookhaneh.stock.core.database.entity.SearchHistoryEntity

@Database(
    entities = [
        FoodItemEntity::class,
        SearchHistoryEntity::class,
        InventoryItemFtsEntity::class,
        CategoryEntity::class
    ],
    version = DatabaseConstant.SCHEMA_VERSION,
    exportSchema = true
)
abstract class AppDatabase : RoomDatabase() {
    abstract fun foodDao(): FoodDao
    abstract fun searchDao(): SearchDao
    abstract fun categoryDao(): CategoryDao
}

object DatabaseConstant {
    /**
     * نسخهٔ ۱ = شروع تمیز محصول داروخانه‌ای.
     * محصول قدیمی هرگز منتشر نشده، بنابراین هیچ مهاجرتی لازم نیست و
     * دیتابیس قدیمی در نصب تازه اصلاً وجود ندارد.
     * از این پس هر تغییر اسکیما باید نسخه را +۱ کند و Migration واقعی داشته باشد.
     */
    const val SCHEMA_VERSION = 1
}
