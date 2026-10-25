package ir.darookhaneh.stock.feature.settings.navigation

import android.content.Intent
import android.os.Build
import androidx.compose.material3.SnackbarDuration
import androidx.compose.material3.SnackbarHostState
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.remember
import androidx.compose.ui.platform.LocalContext
import androidx.core.net.toUri
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import ir.darookhaneh.stock.core.designsystem.component.BoxLayout
import ir.darookhaneh.stock.core.presentation.ObserveEffect
import ir.darookhaneh.stock.core.presentation.navigation.Destination.Setting
import ir.darookhaneh.stock.core.presentation.navigation.SettingDestination
import ir.darookhaneh.stock.feature.settings.presentation.component.open_source.OpenSourceContent
import ir.darookhaneh.stock.feature.settings.presentation.screen.AboutAppScreen
import ir.darookhaneh.stock.feature.settings.presentation.screen.AppearanceScreen
import ir.darookhaneh.stock.feature.settings.presentation.screen.MainSettingsScreen
import ir.darookhaneh.stock.feature.settings.presentation.screen.OtherSettingsScreen
import ir.darookhaneh.stock.feature.settings.presentation.viewmodel.SettingsAction
import ir.darookhaneh.stock.feature.settings.presentation.viewmodel.SettingsEvent
import ir.darookhaneh.stock.feature.settings.presentation.viewmodel.SettingsViewModel
import org.koin.androidx.compose.koinViewModel

@Composable
fun SettingRoute(
    destination: SettingDestination,
    onNavigateToSettingRoute: (Setting) -> Unit,
    onNavigateBack: () -> Unit,
) = BoxLayout {
    val viewModel: SettingsViewModel = koinViewModel()
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
    val combineState by viewModel.combineState.collectAsStateWithLifecycle()
    val onAction = viewModel::onAction
    val snackBarHostState = remember { SnackbarHostState() }
    val context = LocalContext.current

    ObserveEffect(viewModel.uiEvent) { event ->
        when (event) {
            SettingsEvent.NavigateBack -> onNavigateBack()

            is SettingsEvent.ShowSnackBar -> {
                snackBarHostState.showSnackbar(
                    message = event.message,
                    duration = SnackbarDuration.Short
                )
            }

            SettingsEvent.SendFeedBackEmail -> {
                val intent = Intent(Intent.ACTION_SENDTO).apply {
                    data = "mailto:".toUri()
                    putExtra(Intent.EXTRA_SUBJECT, "[Stock Feedback] Bug Report & Suggestions")
                    val emailBody = """
                        --- Device Info (Do not delete) ---
                        App Version: ${uiState.versionName}
                        Android OS: API ${Build.VERSION.SDK_INT} (${Build.VERSION.RELEASE})
                        Device Model: ${Build.MANUFACTURER} ${Build.MODEL}
                        -----------------------------------
                    """.trimIndent()
                    putExtra(Intent.EXTRA_TEXT, emailBody)
                }
                runCatching { context.startActivity(intent) }
            }

            SettingsEvent.OpenSourceClick -> onNavigateToSettingRoute(
                Setting(SettingDestination.OpenSource)
            )

            SettingsEvent.NavigateToGithub ->
                runCatching {
                    context.startActivity(Intent(Intent.ACTION_VIEW, "https://github.com".toUri()))
                }
        }
    }

    when (destination) {
        SettingDestination.Appearance -> AppearanceScreen(
            combineState = combineState,
            onAction = onAction
        )

        SettingDestination.Main -> MainSettingsScreen(
            onAction = onAction,
            onBackClick = onNavigateBack
        )

        SettingDestination.OtherSettings -> OtherSettingsScreen(
            combineState = combineState,
            onAction = onAction
        )

        SettingDestination.AboutApp -> AboutAppScreen(
            uiState = uiState,
            onAction = onAction
        )

        SettingDestination.OpenSource -> OpenSourceContent(onBack = onNavigateBack)

        // این صفحات در فازهای بعدی برمی‌گردند (اعلان انقضا / پشتیبان‌گیری دارو).
        SettingDestination.Notification,
        SettingDestination.YourData -> MainSettingsScreen(
            onAction = onAction,
            onBackClick = onNavigateBack
        )
    }
}
