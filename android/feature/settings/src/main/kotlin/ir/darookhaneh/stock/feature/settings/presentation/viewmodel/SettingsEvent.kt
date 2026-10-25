package ir.darookhaneh.stock.feature.settings.presentation.viewmodel

import ir.darookhaneh.stock.core.presentation.viewmodel.UiEvent

sealed interface SettingsEvent : UiEvent {
    data object NavigateBack : SettingsEvent
    data object OpenSourceClick : SettingsEvent
    data object SendFeedBackEmail : SettingsEvent
    data class ShowSnackBar(val message: String) : SettingsEvent
    data object NavigateToGithub : SettingsEvent
}
