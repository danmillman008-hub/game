package ir.darookhaneh.stock.di

import ir.darookhaneh.stock.core.data.AppNewFeaturesReader
import ir.darookhaneh.stock.core.data.pharmacy.BatchRepositoryImpl
import ir.darookhaneh.stock.core.data.pharmacy.DrugRepositoryImpl
import ir.darookhaneh.stock.core.data.pharmacy.InventoryRepositoryImpl
import ir.darookhaneh.stock.core.data.pharmacy.TtacLookupRepositoryImpl
import ir.darookhaneh.stock.core.data.repository.LocalMediaStorageImpl
import ir.darookhaneh.stock.core.data.repository.UpdateRepositoryImpl
import ir.darookhaneh.stock.core.data.util.AppDispatchers
import ir.darookhaneh.stock.core.data.util.DefaultAppDispatchers
import ir.darookhaneh.stock.core.datastore.dataStore
import ir.darookhaneh.stock.core.datastore.migration.AppearanceMigrator
import ir.darookhaneh.stock.core.datastore.migration.BaseMigrator
import ir.darookhaneh.stock.core.datastore.migration.GeneralMigrator
import ir.darookhaneh.stock.core.datastore.migration.NotificationMigrator
import ir.darookhaneh.stock.core.datastore.model.AppearanceDataStore
import ir.darookhaneh.stock.core.datastore.model.AppearancePreferences
import ir.darookhaneh.stock.core.datastore.model.GeneralDataStore
import ir.darookhaneh.stock.core.datastore.model.GeneralPreferences
import ir.darookhaneh.stock.core.datastore.model.NotificationDataStore
import ir.darookhaneh.stock.core.datastore.model.NotificationPreferences
import ir.darookhaneh.stock.core.datastore.utils.BaseDataStore
import ir.darookhaneh.stock.core.domain.pharmacy.repository.BatchRepository
import ir.darookhaneh.stock.core.domain.pharmacy.repository.DrugRepository
import ir.darookhaneh.stock.core.domain.pharmacy.repository.DrugLookupRepository
import ir.darookhaneh.stock.core.domain.pharmacy.repository.InventoryRepository
import ir.darookhaneh.stock.core.domain.repository.LocalMediaStorage
import ir.darookhaneh.stock.core.model.pharmacy.PharmacyConfig
import ir.darookhaneh.stock.core.model.pharmacy.SystemTimeProvider
import ir.darookhaneh.stock.core.model.pharmacy.TimeProvider
import ir.darookhaneh.stock.core.domain.repository.UpdateRepository
import ir.darookhaneh.stock.core.network.ttac.TtacApi
import kotlinx.serialization.ExperimentalSerializationApi
import kotlinx.serialization.json.Json
import org.koin.android.ext.koin.androidApplication
import org.koin.core.module.dsl.bind
import org.koin.core.module.dsl.singleOf
import org.koin.dsl.module

@OptIn(ExperimentalSerializationApi::class)
val dataModule = module {
    singleOf(::AppNewFeaturesReader)

    // داروخانه — همه محلی، بدون شبکه
    single<TimeProvider> { SystemTimeProvider }
    single { PharmacyConfig() }
    singleOf(::DrugRepositoryImpl) { bind<DrugRepository>() }
    singleOf(::BatchRepositoryImpl) { bind<BatchRepository>() }
    singleOf(::InventoryRepositoryImpl) { bind<InventoryRepository>() }

    // استعلام تیتک: فقط با دکمهٔ کاربر؛ نتیجه در دیتابیس کش می‌شود.
    single { TtacApi(client = TtacApi.defaultClient()) }
    singleOf(::TtacLookupRepositoryImpl) { bind<DrugLookupRepository>() }
    singleOf(::DefaultAppDispatchers) { bind<AppDispatchers>() }
    singleOf(::LocalMediaStorageImpl) { bind<LocalMediaStorage>() }
    singleOf(::UpdateRepositoryImpl) { bind<UpdateRepository>() }

    // Datastore
    single { androidApplication().dataStore }
    single {
        Json {
            decodeEnumsCaseInsensitive = true
            encodeDefaults = true
            ignoreUnknownKeys = true
        }
    }

    singleOf(::NotificationDataStore) { bind<BaseDataStore<NotificationPreferences>>() }
    singleOf(::AppearanceDataStore) { bind<BaseDataStore<AppearancePreferences>>() }
    singleOf(::GeneralDataStore) { bind<BaseDataStore<GeneralPreferences>>() }

    // Datastore - Migration
    singleOf(::NotificationMigrator) { bind<BaseMigrator>() }
    singleOf(::AppearanceMigrator) { bind<BaseMigrator>() }
    singleOf(::GeneralMigrator) { bind<BaseMigrator>() }
}
