package ir.darookhaneh.stock.feature.settings.di

import ir.darookhaneh.stock.core.datastore.SettingsDataStore
import ir.darookhaneh.stock.core.datastore.SettingsDataStoreImpl
import ir.darookhaneh.stock.feature.settings.data.DataBackUpManger
import ir.darookhaneh.stock.feature.settings.data.DatabaseBackUpManager
import ir.darookhaneh.stock.feature.settings.data.DatabaseBackUpManagerImpl
import ir.darookhaneh.stock.feature.settings.data.ImageBackUpManager
import ir.darookhaneh.stock.feature.settings.data.ImageBackUpManagerImpl
import ir.darookhaneh.stock.feature.settings.domain.usecase.CheckCapabilityUseCase
import ir.darookhaneh.stock.feature.settings.domain.usecase.DeleteAllDataUseCase
import ir.darookhaneh.stock.feature.settings.domain.usecase.ImportDataUseCase
import ir.darookhaneh.stock.feature.settings.domain.usecase.ManageDataUseCase
import ir.darookhaneh.stock.feature.settings.domain.usecase.ObserveSettingStateUseCase
import ir.darookhaneh.stock.feature.settings.domain.usecase.UpdatePreferencesUseCase
import ir.darookhaneh.stock.feature.settings.presentation.viewmodel.SettingsViewModel
import org.koin.android.ext.koin.androidContext
import org.koin.core.module.dsl.bind
import org.koin.core.module.dsl.factoryOf
import org.koin.core.module.dsl.singleOf
import org.koin.core.module.dsl.viewModelOf
import org.koin.dsl.module

val settingModule = module {
    single<SettingsDataStore> { SettingsDataStoreImpl(context = androidContext()) }
    singleOf(::DatabaseBackUpManagerImpl) { bind<DatabaseBackUpManager>() }
    singleOf(::ImageBackUpManagerImpl) { bind<ImageBackUpManager>() }
    singleOf(::DataBackUpManger)


    factoryOf(::ObserveSettingStateUseCase)
    factoryOf(::ManageDataUseCase)
    factoryOf(::ImportDataUseCase)
    factoryOf(::DeleteAllDataUseCase)
    factoryOf(::CheckCapabilityUseCase)
    factoryOf(::UpdatePreferencesUseCase)

    viewModelOf(::SettingsViewModel)
}