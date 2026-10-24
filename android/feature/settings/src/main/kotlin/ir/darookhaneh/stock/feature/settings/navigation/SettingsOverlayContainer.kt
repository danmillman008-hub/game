package ir.darookhaneh.stock.feature.settings.navigation

import android.content.ClipData
import androidx.compose.runtime.Composable
import androidx.compose.runtime.rememberCoroutineScope
import androidx.compose.ui.graphics.vector.ImageVector
import androidx.compose.ui.platform.ClipEntry
import androidx.compose.ui.platform.LocalClipboard
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.res.vectorResource
import ir.darookhaneh.stock.core.designsystem.component.StockAlertDialog
import ir.darookhaneh.stock.core.presentation.R
import ir.darookhaneh.stock.core.presentation.component.AppNewFeatureBottomSheet
import ir.darookhaneh.stock.core.presentation.component.AppTimePickerDialog
import ir.darookhaneh.stock.feature.settings.data.AuthorConstant
import ir.darookhaneh.stock.feature.settings.presentation.component.WidgetDebugBottomSheet
import ir.darookhaneh.stock.feature.settings.presentation.component.about_app.CopyrightBottomSheet
import ir.darookhaneh.stock.feature.settings.presentation.component.about_app.PolicyBottomSheet
import ir.darookhaneh.stock.feature.settings.presentation.component.main.CheckUpdateDialog
import ir.darookhaneh.stock.feature.settings.presentation.component.open_source.OpenSourceContent
import ir.darookhaneh.stock.feature.settings.presentation.component.other_setting.SelectLanguageBottomSheet
import ir.darookhaneh.stock.feature.settings.presentation.viewmodel.SettingsAction
import ir.darookhaneh.stock.feature.settings.presentation.viewmodel.SettingsCombineState
import ir.darookhaneh.stock.feature.settings.presentation.viewmodel.SettingsOverlay
import ir.darookhaneh.stock.feature.settings.presentation.viewmodel.SettingsUiState
import ir.darookhaneh.stock.feature.settings.utils.openUrl
import kotlinx.coroutines.launch

@Composable
internal fun SettingsOverlayContainer(
    uiState: SettingsUiState,
    combineState: SettingsCombineState,
    onAction: (SettingsAction) -> Unit,
) {
    val clipboardManager = LocalClipboard.current
    val scope = rememberCoroutineScope()
    val onDismiss = { onAction(SettingsAction.OnDismiss) }
    val context = LocalContext.current

    when (val overlay = uiState.overlay) {
        SettingsOverlay.None -> Unit
        SettingsOverlay.DeleteAlertDialog -> StockAlertDialog(
            icon = ImageVector.vectorResource(R.drawable.ic_delete),
            confirmText = stringResource(R.string.delete_data_dialog_confirm),
            dismissText = stringResource(R.string.delete_data_dialog_cancel),
            onDismissRequest = onDismiss,
            onConfirm = {
                onAction(SettingsAction.DeleteAlertDialog.Confirm)
            },
            title = stringResource(R.string.delete_data_dialog_title),
            text = stringResource(R.string.delete_data_dialog_content),
        )

        SettingsOverlay.TimePicker -> AppTimePickerDialog(
            hour = combineState.notificationPreferences.hour,
            minutes = combineState.notificationPreferences.minutes,
            title = stringResource(R.string.settings_set_time),
            confirmText = stringResource(R.string.settings_set_time_confirm),
            onDateSelected = { hour, min ->
                onAction(
                    SettingsAction.SetNotifyTime.SetHourAndMinutes(
                        hour = hour,
                        minutes = min
                    )
                )
            },
            onDismiss = onDismiss
        )

        is SettingsOverlay.NewFeatureSheet -> AppNewFeatureBottomSheet(
            versionFeatures = overlay.versionFeatures,
            onDismiss = { onAction(SettingsAction.OnDismiss) }
        )

        SettingsOverlay.CopyrightSheet -> CopyrightBottomSheet(
            onDismiss = onDismiss
        )

        SettingsOverlay.OpenSourceSheet -> OpenSourceContent(
            onBack = onDismiss
        )

        SettingsOverlay.PolicySheet -> PolicyBottomSheet(
            onDismiss = onDismiss
        )

        is SettingsOverlay.LanguageSheet -> SelectLanguageBottomSheet(
            currentLanguage = combineState.appearancePreferences.appLanguage,
            onLanguageSelect = { language -> onAction(SettingsAction.ChangeLanguage(language)) },
            onDismiss = onDismiss
        )

        SettingsOverlay.WidgetDebugSheet -> WidgetDebugBottomSheet(
            log = combineState.exceptionLog,
            onDismiss = onDismiss,
            onCopyToClipboard = { log ->
                scope.launch {
                    clipboardManager.setClipEntry(
                        ClipEntry(
                            ClipData.newPlainText(
                                "Widget Log",
                                log
                            )
                        )
                    )
                }
            },
            onClear = { onAction(SettingsAction.ClearLog) }
        )

        SettingsOverlay.CheckUpdateDialog -> {
            CheckUpdateDialog(
                uiState = uiState.checkUpdateResult,
                currentVersion = uiState.versionName,
                onConfirm = { context.openUrl(AuthorConstant.RELEASE_GITHUB) },
                onDismiss = onDismiss
            )
        }
    }
}