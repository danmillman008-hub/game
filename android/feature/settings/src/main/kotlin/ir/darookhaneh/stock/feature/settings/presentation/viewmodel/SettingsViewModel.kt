package ir.darookhaneh.stock.feature.settings.presentation.viewmodel

import androidx.lifecycle.viewModelScope
import ir.darookhaneh.stock.core.data.AppNewFeaturesReader
import ir.darookhaneh.stock.core.data.util.product
import ir.darookhaneh.stock.core.domain.usecase.CheckUpdateUseCase
import ir.darookhaneh.stock.core.presentation.UiResult
import ir.darookhaneh.stock.core.presentation.navigation.Destination.Setting
import ir.darookhaneh.stock.core.presentation.navigation.Navigator
import ir.darookhaneh.stock.core.presentation.navigation.SettingDestination
import ir.darookhaneh.stock.core.presentation.toUiResult
import ir.darookhaneh.stock.core.presentation.viewmodel.BaseViewModel
import ir.darookhaneh.stock.feature.settings.data.WidgetExceptionLogger
import ir.darookhaneh.stock.feature.settings.domain.usecase.CheckCapabilityUseCase
import ir.darookhaneh.stock.feature.settings.domain.usecase.ObserveSettingStateUseCase
import ir.darookhaneh.stock.feature.settings.domain.usecase.UpdatePreferencesUseCase
import ir.darookhaneh.stock.feature.settings.presentation.model.SettingClickableUiModel
import ir.darookhaneh.stock.feature.settings.presentation.model.SettingToggleType
import ir.darookhaneh.stock.feature.settings.presentation.viewmodel.SettingsEvent.ShowSnackBar
import ir.darookhaneh.stock.feature.settings.presentation.viewmodel.SettingsOverlay.LanguageSheet
import ir.darookhaneh.stock.feature.settings.presentation.viewmodel.SettingsOverlay.NewFeatureSheet
import ir.darookhaneh.stock.feature.settings.presentation.viewmodel.SettingsOverlay.None
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.combine
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.launch

class SettingsViewModel(
    appNewFeaturesReader: AppNewFeaturesReader,
    observeSettingStateUseCase: ObserveSettingStateUseCase,
    private val widgetExceptionLogger: WidgetExceptionLogger,
    private val navigator: Navigator,
    private val checkCapabilityUseCase: CheckCapabilityUseCase,
    private val updatePreferencesUseCase: UpdatePreferencesUseCase,
    private val checkUpdateUseCase: CheckUpdateUseCase,
) : BaseViewModel<SettingsUiState, SettingsEvent, SettingsAction>() {
    private val _uiState = MutableStateFlow(
        SettingsUiState(
            versionFeatures = appNewFeaturesReader.getWhatsNewContent(),
            versionName = appNewFeaturesReader.currentVersionName
        )
    )
    override val uiState: StateFlow<SettingsUiState> = _uiState.asStateFlow()

    val combineState: StateFlow<SettingsCombineState> = combine(
        observeSettingStateUseCase.observe(),
        checkCapabilityUseCase.observe(),
        widgetExceptionLogger.latestLog(),
    ) { settingPrefs, capabilities, log ->
        SettingsCombineState(
            notificationGranted = capabilities.notificationGranted,
            biometricSupported = capabilities.biometricSupported,
            biometricEnabled = settingPrefs.enableBiometric,
            dynamicColorSupported = capabilities.dynamicColorSupported,
            appearancePreferences = settingPrefs.appearancePreferences,
            notificationPreferences = settingPrefs.notificationPreferences,
            generalPreferences = settingPrefs.generalPreferences,
            exceptionLog = log
        )
    }
        .stateIn(
            scope = viewModelScope,
            started = SharingStarted.WhileSubscribed(5000),
            initialValue = SettingsCombineState()
        )

    val currentCombineState get() = combineState.value

    override fun onAction(action: SettingsAction) {
        when (action) {
            SettingsAction.OnDismiss -> _uiState.product {
                copy(overlay = None, checkUpdateResult = UiResult.Idle)
            }

            SettingsAction.OnBackClick -> navigator.navigateBack()

            is SettingsAction.SetDarkMode -> viewModelScope.launch {
                updatePreferencesUseCase.updateAppearance(
                    currentCombineState.appearancePreferences.copy(
                        themeMode = action.themeMode
                    )
                )
            }

            is SettingsAction.ChangeLanguage -> viewModelScope.launch {
                updatePreferencesUseCase.updateAppearance(
                    currentCombineState.appearancePreferences.copy(
                        appLanguage = action.language
                    )
                )
                navigator.navigateBack()
            }

            is SettingsAction.ChangeFont -> viewModelScope.launch {
            }

            is SettingsAction.ToggleAction -> onToggleAction(action)
            is SettingsAction.ClickableAction -> onClickableAction(action)

            is SettingsAction.SetSeedColorPreset -> viewModelScope.launch {
                updatePreferencesUseCase.updateAppearance(
                    currentCombineState.appearancePreferences.copy(
                        seedColor = action.seedColor
                    )
                )
            }

            SettingsAction.ClearLog -> viewModelScope.launch {
                widgetExceptionLogger.clear()
            }

            SettingsAction.OnGithubClick -> emitEvent(SettingsEvent.NavigateToGithub)
        }
    }

    private fun onClickableAction(action: SettingsAction.ClickableAction) {
        viewModelScope.launch {
            when (action.type) {
                SettingClickableUiModel.EXPORT,
                SettingClickableUiModel.IMPORT,
                SettingClickableUiModel.DELETE_ALL,
                SettingClickableUiModel.YOUR_DATA,
                SettingClickableUiModel.DAILY_REMINDER,
                SettingClickableUiModel.NOTIFICATION -> emitEvent(
                    SettingsEvent.ShowSnackBar("این بخش در نسخه‌های بعدی فعال می‌شود.")
                )

                SettingClickableUiModel.ABOUT -> {
                    navigator.navigateTo(Setting(SettingDestination.AboutApp))
                }

                SettingClickableUiModel.NEW_FEATURES -> {
                    currentState.versionFeatures?.let {
                        _uiState.product {
                            copy(overlay = NewFeatureSheet(it))
                        }
                    }
                }

                SettingClickableUiModel.COPYRIGHT -> _uiState.product {
                    copy(overlay = SettingsOverlay.CopyrightSheet)
                }

                SettingClickableUiModel.FEEDBACK -> {
                    emitEvent(SettingsEvent.SendFeedBackEmail)
                }

                SettingClickableUiModel.OPEN_SOURCE -> navigator.navigateTo(
                    Setting(
                        SettingDestination.OpenSource
                    )
                )

                SettingClickableUiModel.PRIVACY_POLICY -> _uiState.product {
                    copy(overlay = SettingsOverlay.PolicySheet)
                }

                SettingClickableUiModel.LANGUAGE -> _uiState.product {
                    copy(
                        overlay = LanguageSheet(currentLanguage = currentCombineState.appearancePreferences.appLanguage)
                    )
                }

                SettingClickableUiModel.DEBUG -> emitEvent(
                    SettingsEvent.ShowSnackBar("لاگ خطا در نسخه بعدی نمایش داده می‌شود.")
                )

                SettingClickableUiModel.APPEARANCE -> navigator.navigateTo(
                    Setting(
                        SettingDestination.Appearance
                    )
                )

                SettingClickableUiModel.OTHER_SETTING -> navigator.navigateTo(
                    Setting(
                        SettingDestination.OtherSettings
                    )
                )

                SettingClickableUiModel.CHECK_UPDATE -> {
                    _uiState.product {
                        copy(
                            overlay = SettingsOverlay.CheckUpdateDialog,
                            checkUpdateResult = UiResult.Loading
                        )
                    }
                    val uiResult = checkUpdateUseCase()
                    _uiState.product {
                        copy(checkUpdateResult = uiResult.toUiResult())
                    }
                }
            }
        }
    }

    private fun onToggleAction(action: SettingsAction.ToggleAction) {
        viewModelScope.launch {
            when (action.type) {
                SettingToggleType.BIOMETRIC_AUTH -> {
                    updatePreferencesUseCase.updateBiometric(action.enabled)
                }

                SettingToggleType.DYNAMIC_COLOR -> {
                    updatePreferencesUseCase.updateAppearance(
                        currentCombineState.appearancePreferences.copy(
                            enableDynamicColor = action.enabled
                        )
                    )
                }

                SettingToggleType.CATEGORY_GROUP -> {
                    updatePreferencesUseCase.updateAppearance(
                        currentCombineState.appearancePreferences.copy(
                            enableCategoryGroup = action.enabled
                        )
                    )
                }

                SettingToggleType.NOTIFICATION -> updatePreferencesUseCase.updateNotification(
                    currentCombineState.notificationPreferences.copy(
                        enableNotification = action.enabled
                    )
                )

                SettingToggleType.WEEKLY_REPORT -> {
                    updatePreferencesUseCase.updateNotification(
                        currentCombineState.notificationPreferences.copy(
                            enableWeeklyReport = action.enabled
                        )
                    )
                }
            }
        }
    }

}
