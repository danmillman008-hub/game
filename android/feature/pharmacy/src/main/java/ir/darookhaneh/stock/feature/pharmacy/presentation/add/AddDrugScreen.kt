package ir.darookhaneh.stock.feature.pharmacy.presentation.add

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Button
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import ir.darookhaneh.stock.core.designsystem.component.AppTextField
import ir.darookhaneh.stock.core.presentation.component.AppDatePickerDialog
import ir.darookhaneh.stock.feature.pharmacy.R
import org.koin.androidx.compose.koinViewModel
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

@Composable
fun AddDrugRoute(
    initialGtin: String? = null,
    onSaved: (Long) -> Unit,
    onCancel: () -> Unit,
) {
    val viewModel: AddDrugViewModel = koinViewModel()
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    // کد اسکن‌شدهٔ ناشناخته مستقیم به همین فرم می‌آید.
    LaunchedEffect(initialGtin) {
        if (!initialGtin.isNullOrBlank() && uiState.gtin.isBlank()) {
            viewModel.onAction(AddDrugAction.OnGtinChange(initialGtin))
        }
    }

    LaunchedEffect(uiState.savedDrugId) {
        uiState.savedDrugId?.let(onSaved)
    }

    AddDrugScreen(
        uiState = uiState,
        onAction = viewModel::onAction,
        onCancel = onCancel,
    )
}

@Composable
fun AddDrugScreen(
    uiState: AddDrugUiState,
    onAction: (AddDrugAction) -> Unit,
    onCancel: () -> Unit,
) {
    var showDatePicker by remember { mutableStateOf(false) }

    Scaffold { padding ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(padding)
                .verticalScroll(rememberScrollState())
                .padding(horizontal = 16.dp, vertical = 12.dp),
            verticalArrangement = Arrangement.spacedBy(10.dp),
        ) {
            Text(
                text = stringResource(R.string.pharmacy_add_title),
                style = MaterialTheme.typography.headlineSmall,
            )
            Text(
                text = stringResource(R.string.pharmacy_add_hint),
                style = MaterialTheme.typography.bodySmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
            )

            AppTextField(
                value = uiState.name,
                onValueChange = { onAction(AddDrugAction.OnNameChange(it)) },
                label = stringResource(R.string.pharmacy_field_name),
                isError = uiState.name.isNotBlank() && uiState.name.trim().length < 2,
                errorMessage = stringResource(R.string.pharmacy_field_name_error),
                keyboardOptions = KeyboardOptions(imeAction = ImeAction.Next),
            )
            AppTextField(
                value = uiState.genericName,
                onValueChange = { onAction(AddDrugAction.OnGenericNameChange(it)) },
                label = stringResource(R.string.pharmacy_field_generic),
            )
            AppTextField(
                value = uiState.strength,
                onValueChange = { onAction(AddDrugAction.OnStrengthChange(it)) },
                label = stringResource(R.string.pharmacy_field_strength),
            )
            AppTextField(
                value = uiState.dosageForm,
                onValueChange = { onAction(AddDrugAction.OnDosageFormChange(it)) },
                label = stringResource(R.string.pharmacy_field_form),
            )
            AppTextField(
                value = uiState.gtin,
                onValueChange = { onAction(AddDrugAction.OnGtinChange(it)) },
                label = stringResource(R.string.pharmacy_field_gtin),
                keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
            )
            AppTextField(
                value = uiState.irc,
                onValueChange = { onAction(AddDrugAction.OnIrcChange(it)) },
                label = stringResource(R.string.pharmacy_field_irc),
                keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
            )

            Text(
                text = stringResource(R.string.pharmacy_section_batch),
                style = MaterialTheme.typography.titleSmall,
                modifier = Modifier.padding(top = 8.dp),
            )
            AppTextField(
                value = uiState.batchNumber,
                onValueChange = { onAction(AddDrugAction.OnBatchNumberChange(it)) },
                label = stringResource(R.string.pharmacy_field_batch_number),
            )
            AppTextField(
                value = uiState.expiryDate?.let { formatDate(it) } ?: "",
                onValueChange = {},
                label = stringResource(R.string.pharmacy_field_expiry),
                readOnly = true,
                trailingIcon = {
                    TextButton(onClick = { showDatePicker = true }) {
                        Text(stringResource(R.string.pharmacy_pick_date))
                    }
                },
            )
            AppTextField(
                value = uiState.quantity,
                onValueChange = { onAction(AddDrugAction.OnQuantityChange(it)) },
                label = stringResource(R.string.pharmacy_field_quantity),
                keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
            )
            AppTextField(
                value = uiState.location,
                onValueChange = { onAction(AddDrugAction.OnLocationChange(it)) },
                label = stringResource(R.string.pharmacy_field_location),
            )

            uiState.errorMessage?.let { message ->
                Row(modifier = Modifier.fillMaxWidth()) {
                    Text(
                        text = message,
                        color = MaterialTheme.colorScheme.error,
                        style = MaterialTheme.typography.bodySmall,
                    )
                }
            }

            Row(
                modifier = Modifier
                    .fillMaxWidth()
                    .padding(top = 8.dp),
                horizontalArrangement = Arrangement.spacedBy(8.dp),
            ) {
                TextButton(onClick = onCancel, modifier = Modifier.weight(1f)) {
                    Text(stringResource(R.string.pharmacy_cancel))
                }
                Button(
                    onClick = { onAction(AddDrugAction.Save) },
                    enabled = uiState.canSave,
                    modifier = Modifier.weight(1f),
                ) {
                    if (uiState.isSaving) {
                        CircularProgressIndicator(modifier = Modifier.padding(4.dp))
                    } else {
                        Text(stringResource(R.string.pharmacy_save))
                    }
                }
            }
        }
    }

    if (showDatePicker) {
        AppDatePickerDialog(
            initialDateMillis = uiState.expiryDate,
            title = stringResource(R.string.pharmacy_field_expiry),
            onDateSelected = { onAction(AddDrugAction.OnExpiryDateChange(it)) },
            onDismiss = { showDatePicker = false },
        )
    }
}

private fun formatDate(millis: Long): String =
    SimpleDateFormat("yyyy/MM/dd", Locale.US).format(Date(millis))
