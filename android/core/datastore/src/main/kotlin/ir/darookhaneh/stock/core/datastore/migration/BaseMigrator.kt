package ir.darookhaneh.stock.core.datastore.migration

interface BaseMigrator {
    suspend fun shouldMigrate(): Boolean
    suspend fun migrate()
    suspend fun cleanUp()
}