package ir.darookhaneh.stock.core.database

import androidx.room.RoomDatabase
import androidx.room.withTransaction

/**
 * اجرای چند عملیات در یک تراکنش.
 * هر عملیاتی که در [runWithResult] پرتاب استثنا کند، کل تراکنش را rollback می‌کند.
 */
interface TransactionRunner {
    suspend fun run(onTransaction: suspend () -> Unit)

    suspend fun <T> runWithResult(onTransaction: suspend () -> T): T
}

class RoomTransactionRunner(
    private val db: RoomDatabase,
) : TransactionRunner {
    override suspend fun run(onTransaction: suspend () -> Unit) {
        db.withTransaction { onTransaction() }
    }

    override suspend fun <T> runWithResult(onTransaction: suspend () -> T): T =
        db.withTransaction { onTransaction() }
}
