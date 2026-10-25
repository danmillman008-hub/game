package ir.darookhaneh.stock

import android.content.ClipData
import android.content.ClipboardManager
import android.graphics.Color
import android.os.Bundle
import android.widget.Toast
import androidx.activity.SystemBarStyle
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.app.AppCompatDelegate
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.AlertDialog
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.core.os.LocaleListCompat
import androidx.core.splashscreen.SplashScreen.Companion.installSplashScreen
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.navigation3.runtime.rememberNavBackStack
import ir.darookhaneh.stock.core.designsystem.theme.StockDynamicTheme
import ir.darookhaneh.stock.core.model.setting.ThemeMode
import ir.darookhaneh.stock.core.presentation.R
import ir.darookhaneh.stock.core.presentation.navigation.Destination
import ir.darookhaneh.stock.core.presentation.utils.toColor
import ir.darookhaneh.stock.navigation.AppGraph
import ir.darookhaneh.stock.navigation.BottomBarItem
import ir.darookhaneh.stock.navigation.BottomFloatingBar
import ir.darookhaneh.stock.navigation.FloatingBottomBarScaffold
import ir.darookhaneh.stock.navigation.hideBottomBar
import ir.darookhaneh.stock.navigation.toBottomBarItem
import ir.darookhaneh.stock.navigation.toDestination
import ir.darookhaneh.stock.utils.BiometricHandler
import ir.darookhaneh.stock.utils.CrashReporter
import ir.darookhaneh.stock.utils.BiometricResult
import org.koin.androidx.viewmodel.ext.android.viewModel

class MainActivity : AppCompatActivity() {
    private val viewModel: AppViewModel by viewModel()
    private val biometricHandler by lazy { BiometricHandler(this) }
    private val crashReporter by lazy { CrashReporter(this) }
    override fun onCreate(savedInstanceState: Bundle?) {
        val splashScreen = installSplashScreen()
        splashScreen.setKeepOnScreenCondition {
            viewModel.appUiState.value.isSplashScreen
        }
        super.onCreate(savedInstanceState)
        enableEdgeToEdge(
            navigationBarStyle = SystemBarStyle.dark(scrim = Color.TRANSPARENT)
        )
        setContent {
            val backStack = rememberNavBackStack(Destination.Dashboard)
            val uiState: AppUiState by viewModel.appUiState.collectAsStateWithLifecycle()
            val onAction = viewModel::onAction
            val isUnlocked by viewModel.isUnlocked.collectAsStateWithLifecycle()
            val biometricTriggerCount by viewModel.biometricTrigger.collectAsStateWithLifecycle()
            LaunchedEffect(uiState.isSplashScreen, biometricTriggerCount) {
                if (!uiState.isSplashScreen) {
                    if (!uiState.isBiometricLock) {
                        onAction(AppAction.UpdateAppUnlock(true))
                    } else if (!isUnlocked) {
                        biometricHandler.authenticate().collect { result ->
                            when (result) {
                                BiometricResult.Success -> {
                                    onAction(AppAction.UpdateAppUnlock(true))
                                }

                                BiometricResult.Failed -> {
                                    Toast.makeText(
                                        this@MainActivity, this@MainActivity.getString(
                                            R.string.biometric_auth_failed
                                        ), Toast.LENGTH_SHORT
                                    ).show()
                                    onAction(AppAction.UpdateAppUnlock(false))
                                }

                                is BiometricResult.Error -> {
                                    Toast.makeText(
                                        this@MainActivity, this@MainActivity.getString(
                                            R.string.biometric_auth_failed
                                        ), Toast.LENGTH_SHORT
                                    ).show()
                                    onAction(AppAction.UpdateAppUnlock(false))
                                    when (result) {
                                        BiometricResult.Error.NotSupported -> {
                                            onAction(AppAction.UpdateBiometricSupported(false))
                                        }

                                        else -> {
                                            Toast.makeText(
                                                this@MainActivity, this@MainActivity.getString(
                                                    R.string.biometric_auth_failed
                                                ), Toast.LENGTH_SHORT
                                            ).show()
                                        }
                                    }
                                }

                                BiometricResult.Idle -> Unit
                            }
                        }
                    }
                }
            }

            LaunchedEffect(uiState.language) {
                val currentLocales = AppCompatDelegate.getApplicationLocales()
                if (currentLocales.isEmpty || currentLocales[0]?.language != uiState.language.isoCode) {
                    val appLocale: LocaleListCompat =
                        LocaleListCompat.forLanguageTags(uiState.language.isoCode)
                    AppCompatDelegate.setApplicationLocales(appLocale)
                }
            }
            CrashReportDialog(
                crashReporter = crashReporter,
                onDismiss = { crashReporter.clear() },
            )

            StockDynamicTheme(
                seedColor = uiState.seedColor.toColor(),
                dynamicColor = uiState.isDynamicColors,
                darkTheme = when (uiState.themeMode) {
                    ThemeMode.DARK -> true
                    ThemeMode.LIGHT -> false
                    ThemeMode.SYSTEM -> isSystemInDarkTheme()
                }
            ) {
                val currentBottomBarItem = backStack.map { it.toBottomBarItem() }
                    .lastOrNull() ?: BottomBarItem.DASHBOARD
                FloatingBottomBarScaffold(
                    modifier = Modifier.fillMaxSize(),
                    bottomBarVisible = !hideBottomBar(currentDestination = backStack.lastOrNull()),
                    bottomBar = {
                        BottomFloatingBar(
                            modifier = Modifier,
                            selectedBottomBarItem = currentBottomBarItem,
                            onBottomBarClick = { item ->
                                val destination = item.toDestination()
                                // تب‌های اصلی جای‌گذاری می‌شوند، نه روی هم انبار.
                                backStack.add(destination)
                            }
                        )
                    },
                ) {
                    AppGraph(
                        modifier = Modifier,
                        backStack = backStack,
                    )
                }
            }
        }
    }

    override fun onResume() {
        viewModel.onAction(AppAction.TriggerBiometric)
        super.onResume()
    }
}


/**
 * اگر دفعهٔ قبل کرشی ثبت شده باشد، متن آن یک‌بار نشان داده می‌شود.
 * هیچ اتصال شبکه‌ای در کار نیست؛ کاربر خودش متن را کپی و ارسال می‌کند.
 */
@Composable
private fun CrashReportDialog(
    crashReporter: CrashReporter,
    onDismiss: () -> Unit,
) {
    var report by remember { mutableStateOf<String?>(null) }
    var copied by remember { mutableStateOf(false) }
    LaunchedEffect(Unit) { report = crashReporter.readLast() }

    val text = report ?: return
    val context = LocalContext.current
    AlertDialog(
        onDismissRequest = {
            report = null
            onDismiss()
        },
        title = { Text(stringResource(ir.darookhaneh.stock.R.string.crash_title)) },
        text = {
            Column {
                Text(stringResource(ir.darookhaneh.stock.R.string.crash_body))
                Spacer(Modifier.height(8.dp))
                Text(
                    text = text.take(1200),
                    style = MaterialTheme.typography.bodySmall,
                    modifier = Modifier.verticalScroll(rememberScrollState()),
                )
            }
        },
        confirmButton = {
            TextButton(onClick = {
                val clipboard = context.getSystemService(ClipboardManager::class.java)
                clipboard?.setPrimaryClip(ClipData.newPlainText("crash", text))
                copied = true
            }) {
                Text(
                    stringResource(
                        if (copied) ir.darookhaneh.stock.R.string.crash_copied
                        else ir.darookhaneh.stock.R.string.crash_copy
                    )
                )
            }
        },
        dismissButton = {
            TextButton(onClick = {
                report = null
                onDismiss()
            }) { Text(stringResource(ir.darookhaneh.stock.R.string.crash_dismiss)) }
        },
    )
}
