package ir.darookhaneh.stock

import android.graphics.Color
import android.os.Bundle
import android.widget.Toast
import androidx.activity.SystemBarStyle
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.appcompat.app.AppCompatActivity
import androidx.appcompat.app.AppCompatDelegate
import androidx.compose.animation.AnimatedVisibility
import androidx.compose.foundation.isSystemInDarkTheme
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
import ir.darookhaneh.stock.utils.BiometricResult
import org.koin.androidx.viewmodel.ext.android.viewModel

class MainActivity : AppCompatActivity() {
    private val viewModel: AppViewModel by viewModel()
    private val biometricHandler by lazy { BiometricHandler(this) }
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
            val backStack = rememberNavBackStack(Destination.Inventory.Home)
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
            StockDynamicTheme(
                seedColor = uiState.seedColor.toColor(),
                dynamicColor = uiState.isDynamicColors,
                darkTheme = when (uiState.themeMode) {
                    ThemeMode.DARK -> true
                    ThemeMode.LIGHT -> false
                    ThemeMode.SYSTEM -> isSystemInDarkTheme()
                }
            ) {
                FloatingBottomBarScaffold(
                    modifier = Modifier.fillMaxSize(),
                    bottomBar = {
                        val currentBottomBarItem = backStack.map { it.toBottomBarItem() }
                            .lastOrNull() ?: BottomBarItem.HOME
                        AnimatedVisibility(
                            visible = !hideBottomBar(currentDestination = backStack.lastOrNull()),
                        ) {
                            BottomFloatingBar(
                                modifier = Modifier,
                                selectedBottomBarItem = currentBottomBarItem,
                                onBottomBarClick = { item ->
                                    val destination = item.toDestination()
                                    backStack.add(destination)
                                }
                            )
                        }
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

