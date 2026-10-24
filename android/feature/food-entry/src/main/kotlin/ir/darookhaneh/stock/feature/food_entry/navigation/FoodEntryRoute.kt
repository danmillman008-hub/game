package ir.darookhaneh.stock.feature.food_entry.navigation

import android.Manifest
import android.os.Build
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.layout.padding
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import ir.darookhaneh.stock.core.presentation.ObserveEffect
import ir.darookhaneh.stock.core.presentation.R
import ir.darookhaneh.stock.core.presentation.component.AppDatePickerDialog
import ir.darookhaneh.stock.core.presentation.component.TextFieldDialog
import ir.darookhaneh.stock.feature.food_entry.presentation.FoodEntryBottomSheet
import ir.darookhaneh.stock.feature.food_entry.presentation.model.EntryUiModel
import ir.darookhaneh.stock.feature.food_entry.presentation.viewmodel.FoodEntryAction
import ir.darookhaneh.stock.feature.food_entry.presentation.viewmodel.FoodEntryAction.OnCategoryConfirm
import ir.darookhaneh.stock.feature.food_entry.presentation.viewmodel.FoodEntryAction.OnCategoryQueryChange
import ir.darookhaneh.stock.feature.food_entry.presentation.viewmodel.FoodEntryAction.OnDismissOverlay
import ir.darookhaneh.stock.feature.food_entry.presentation.viewmodel.FoodEntryAction.OnExpiryDateChange
import ir.darookhaneh.stock.feature.food_entry.presentation.viewmodel.FoodEntryAction.OnNameChange
import ir.darookhaneh.stock.feature.food_entry.presentation.viewmodel.FoodEntryAction.OnNameConfirm
import ir.darookhaneh.stock.feature.food_entry.presentation.viewmodel.FoodEntryAction.OnNotificationGranted
import ir.darookhaneh.stock.feature.food_entry.presentation.viewmodel.FoodEntryAction.OnPurchaseDateChange
import ir.darookhaneh.stock.feature.food_entry.presentation.viewmodel.FoodEntryEvent
import ir.darookhaneh.stock.feature.food_entry.presentation.viewmodel.FoodEntryOverlay
import ir.darookhaneh.stock.feature.food_entry.presentation.viewmodel.FoodEntryUiState
import ir.darookhaneh.stock.feature.food_entry.presentation.viewmodel.FoodEntryViewModel
import org.koin.androidx.compose.koinViewModel
import org.koin.core.parameter.parametersOf

@Composable
fun FoodEntryRoute(
    currentFoodModel: EntryUiModel?,
    onDismiss: () -> Unit,
) {
    val viewModel: FoodEntryViewModel =
        koinViewModel(parameters = { parametersOf(currentFoodModel) })
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
    val onAction = viewModel::onAction

    val notificationPermissionLauncher = rememberLauncherForActivityResult(
        contract = ActivityResultContracts.RequestPermission(),
        onResult = { isGranted ->
            onAction(OnNotificationGranted(isGranted))
        }
    )

    ObserveEffect(viewModel.uiEvent) { event ->
        when (event) {
            FoodEntryEvent.AskNotificationPermission -> {
                if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.TIRAMISU) {
                    notificationPermissionLauncher.launch(Manifest.permission.POST_NOTIFICATIONS)
                }
            }

            FoodEntryEvent.OnNavigateBack -> onDismiss()
        }
    }

    FoodEntryBottomSheet(
        state = uiState,
        onAction = onAction,
        onDismiss = onDismiss
    )

    FoodEntryOverlayContainer(
        state = uiState,
        onAction = onAction
    )
}

@Composable
private fun FoodEntryOverlayContainer(
    state: FoodEntryUiState,
    onAction: (FoodEntryAction) -> Unit
) {
    val onDismiss = { onAction(OnDismissOverlay) }
    when (state.overlay) {
        FoodEntryOverlay.NONE -> Unit
        FoodEntryOverlay.PURCHASE_DATE_PICKER -> {
            AppDatePickerDialog(
                initialDateMillis = state.entry.purchaseDate,
                title = stringResource(R.string.confirm_label_purchase_date),
                onDateSelected = {
                    onAction(OnPurchaseDateChange(it))
                    onDismiss()
                },
                onDismiss = onDismiss
            )
        }

        FoodEntryOverlay.EXPIRY_DATE_PICKER -> {
            AppDatePickerDialog(
                initialDateMillis = if (state.entry.expiryDate == -1L) null else state.entry.expiryDate,
                title = stringResource(R.string.confirm_label_expiry_date),
                onDateSelected = {
                    onAction(OnExpiryDateChange(it))
                    onDismiss()
                },
                onDismiss = onDismiss
            )
        }

        FoodEntryOverlay.CATEGORY_ADD -> {
            TextFieldDialog(
                modifier = Modifier.padding(horizontal = 16.dp),
                value = state.categoryQuery,
                title = stringResource(R.string.inventory_category_add),
                confirmText = stringResource(R.string.action_add),
                onValueChange = { onAction(OnCategoryQueryChange(it)) },
                onDismiss = onDismiss,
                onConfirm = { onAction(OnCategoryConfirm) },
            )
        }

        FoodEntryOverlay.FOOD_NAME_ADD -> {
            TextFieldDialog(
                modifier = Modifier.padding(horizontal = 16.dp),
                value = state.entry.name,
                title = stringResource(R.string.food_entry_title),
                confirmText = stringResource(R.string.action_add),
                onValueChange = {
                    onAction(OnNameChange(it))
                },
                onDismiss = onDismiss,
                onConfirm = { onAction(OnNameConfirm) },
            )
        }
    }
}
