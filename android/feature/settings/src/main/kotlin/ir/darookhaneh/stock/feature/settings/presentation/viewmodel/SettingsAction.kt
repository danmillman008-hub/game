package ir.darookhaneh.stock.feature.settings.presentation.viewmodel

import ir.darookhaneh.stock.core.model.setting.AppFont
import ir.darookhaneh.stock.core.model.setting.AppLanguage
import ir.darookhaneh.stock.core.model.setting.SeedColor
import ir.darookhaneh.stock.core.model.setting.ThemeMode
import ir.darookhaneh.stock.core.presentation.viewmodel.UiAction
import ir.darookhaneh.stock.feature.settings.presentation.model.SettingClickableUiModel
import ir.darookhaneh.stock.feature.settings.presentation.model.SettingToggleType

sealed interface SettingsAction : UiAction {
    data object OnDismiss : SettingsAction
    data class SetDarkMode(val themeMode: ThemeMode) : SettingsAction
    data class ChangeLanguage(val language: AppLanguage) : SettingsAction
    data class ChangeFont(val font: AppFont) : SettingsAction
    data class SetSeedColorPreset(val seedColor: SeedColor) : SettingsAction

    data object OnGithubClick : SettingsAction
    data object OnBackClick : SettingsAction

    data class ClickableAction(val type: SettingClickableUiModel) : SettingsAction

    data class ToggleAction(
        val type: SettingToggleType,
        val enabled: Boolean
    ) : SettingsAction

    data object ClearLog : SettingsAction
}
