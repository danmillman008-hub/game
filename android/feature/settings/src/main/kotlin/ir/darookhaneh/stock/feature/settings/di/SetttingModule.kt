package ir.darookhaneh.stock.feature.settings.di

import ir.darookhaneh.stock.core.datastore.SettingsDataStore
import ir.darookhaneh.stock.core.datastore.SettingsDataStoreImpl
import ir.darookhaneh.stock.feature.settings.data.WidgetExceptionLogger
import ir.darookhaneh.stock.feature.settings.data.WidgetExceptionLoggerImpl
import ir.darookhaneh.stock.feature.settings.domain.usecase.CheckCapabilityUseCase
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
    singleOf(::WidgetExceptionLoggerImpl) { bind<WidgetExceptionLogger>() }

    factoryOf(::ObserveSettingStateUseCase)
    factoryOf(::CheckCapabilityUseCase)
    factoryOf(::UpdatePreferencesUseCase)

    viewModelOf(::SettingsViewModel)
}
