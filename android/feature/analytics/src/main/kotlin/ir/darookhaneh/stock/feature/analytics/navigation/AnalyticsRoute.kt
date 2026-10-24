package ir.darookhaneh.stock.feature.analytics.navigation

import androidx.compose.material3.ExperimentalMaterial3ExpressiveApi
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import ir.darookhaneh.stock.feature.analytics.presentation.AnalyticsScreen
import ir.darookhaneh.stock.feature.analytics.presentation.viewmodel.AnalyticsViewModel
import org.koin.androidx.compose.koinViewModel

@OptIn(ExperimentalMaterial3ExpressiveApi::class)
@Composable
fun AnalyticsRoute() {
    val viewModel: AnalyticsViewModel = koinViewModel()
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
    val onAction = viewModel::onAction

    AnalyticsScreen(
        uiState = uiState,
        onAction = onAction
    )
}
