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
            "stock-database"
        )
            .addMigrations(
                AppDatabase.MIGRATION_12_13,
                AppDatabase.MIGRATION_13_14,
                AppDatabase.MIGRATION_14_15
            )
            .build()
    } bind AppDatabase::class
    single { get<AppDatabase>().foodDao() }
    single { get<AppDatabase>().searchDao() }
    single { get<AppDatabase>().categoryDao() }
    single<TransactionRunner> { RoomTransactionRunner(get<AppDatabase>()) }
}
