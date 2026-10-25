package ir.darookhaneh.stock.di

import androidx.room.Room
import ir.darookhaneh.stock.core.database.AppDatabase
import ir.darookhaneh.stock.core.database.RoomTransactionRunner
import ir.darookhaneh.stock.core.database.TransactionRunner
import org.koin.android.ext.koin.androidContext
import org.koin.dsl.bind
import org.koin.dsl.module

val databaseModule = module {
    single {
        Room.databaseBuilder(
            androidContext(),
            AppDatabase::class.java,
            "stock-database",
        )
            // محصول منتشرنشده: اسکیمای قدیمی دور ریخته می‌شود، نه مهاجرت داده می‌شود.
            .fallbackToDestructiveMigration(dropAllTables = true)
            .build()
    } bind AppDatabase::class
    single { get<AppDatabase>().drugDao() }
    single { get<AppDatabase>().batchDao() }
    single { get<AppDatabase>().inventoryEventDao() }
    single<TransactionRunner> { RoomTransactionRunner(get<AppDatabase>()) }
}
