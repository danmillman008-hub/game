package ir.darookhaneh.stock.feature.pharmacy.presentation.detail

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.Button
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import ir.darookhaneh.stock.core.designsystem.component.AppTextField
import ir.darookhaneh.stock.core.model.pharmacy.Batch
import ir.darookhaneh.stock.core.model.pharmacy.InventoryEvent
import ir.darookhaneh.stock.core.model.pharmacy.InventoryEventType
import ir.darookhaneh.stock.core.presentation.component.AppDatePickerDialog
import ir.darookhaneh.stock.feature.pharmacy.R
import org.koin.androidx.compose.koinViewModel
import org.koin.core.parameter.parametersOf
import java.text.SimpleDateFormat
import java.util.Date
import java.util.Locale

@Composable
fun DrugDetailRoute(drugId: Long) {
    val viewModel: DrugDetailViewModel = koinViewModel { parametersOf(drugId) }
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    DrugDetailScreen(uiState = uiState, onAction = viewModel::onAction)
}

@Composable
fun DrugDetailScreen(
    uiState: DrugDetailUiState,
    onAction: (DrugDetailAction) -> Unit,
) {
    var showDatePicker by remember { mutableStateOf(false) }

    Scaffold { padding ->
        LazyColumn(
            modifier = Modifier
                .fillMaxSize()
                .padding(padding)
                .padding(horizontal = 16.dp),
            verticalArrangement = Arrangement.spacedBy(10.dp),
        ) {
            item {
                Text(
                    text = uiState.drug?.name ?: stringResource(R.string.pharmacy_detail_loading),
                    style = MaterialTheme.typography.headlineSmall,
                    modifier = Modifier.padding(top = 16.dp),
                )
            }

            item {
                val subtitle = listOfNotNull(
                    uiState.drug?.genericName,
                    uiState.drug?.strength,
                    uiState.drug?.dosageForm,
                ).joinToString(" · ")
                Text(
                    text = if (subtitle.isBlank()) "—" else subtitle,
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                )
                Text(
                    text = stringResource(R.string.pharmacy_detail_total, uiState.totalQuantity),
                    style = MaterialTheme.typography.titleMedium,
                    modifier = Modifier.padding(top = 6.dp),
                )
            }

            item {
                Row(
                    modifier = Modifier.fillMaxWidth(),
                    horizontalArrangement = Arrangement.spacedBy(8.dp),
                ) {
                    Text(
                        text = stringResource(R.string.pharmacy_detail_batches),
                        style = MaterialTheme.typography.titleSmall,
                        modifier = Modifier.weight(1f),
                    )
                    TextButton(onClick = { onAction(DrugDetailAction.OpenAddBatch) }) {
                        Text(stringResource(R.string.pharmacy_detail_add_batch))
                    }
                }
            }

            if (uiState.batches.isEmpty()) {
                item {
                    Text(
                        text = stringResource(R.string.pharmacy_detail_no_batch),
                        style = MaterialTheme.typography.bodyMedium,
                        color = MaterialTheme.colorScheme.onSurfaceVariant,
                    )
                }
            }

            items(items = uiState.batches, key = { it.id }) { batch ->
                BatchRow(
                    batch = batch,
                    selected = batch.id == uiState.selectedBatchId,
                    onClick = { onAction(DrugDetailAction.SelectBatch(batch.id)) },
                )
            }

            uiState.selectedBatch?.let { batch ->
                item { InventoryActionsCard(uiState = uiState, onAction = onAction) }
                item {
                    Text(
                        text = stringResource(R.string.pharmacy_detail_events),
                        style = MaterialTheme.typography.titleSmall,
                        modifier = Modifier.padding(top = 8.dp),
                    )
                }
                if (uiState.events.isEmpty()) {
                    item {
                        Text(
                            text = stringResource(R.string.pharmacy_detail_no_event),
                            style = MaterialTheme.typography.bodySmall,
                            color = MaterialTheme.colorScheme.onSurfaceVariant,
                        )
                    }
                }
                items(items = uiState.events, key = { it.id }) { event ->
                    EventRow(event = event)
                }
            }

            item { Column(modifier = Modifier.padding(bottom = 24.dp)) {} }
        }
    }

    uiState.message?.let { message ->
        androidx.compose.material3.AlertDialog(
            onDismissRequest = { onAction(DrugDetailAction.DismissMessage) },
            confirmButton = {
                TextButton(onClick = { onAction(DrugDetailAction.DismissMessage) }) { Text("باشه") }
            },
            text = { Text(message) },
        )
    }

    if (uiState.showAddBatch) {
        AddBatchDialog(
            uiState = uiState,
            onAction = onAction,
            onPickDate = { showDatePicker = true },
        )
    }

    if (showDatePicker) {
        AppDatePickerDialog(
            initialDateMillis = uiState.newBatchExpiry,
            title = stringResource(R.string.pharmacy_field_expiry),
            onDateSelected = { onAction(DrugDetailAction.OnNewBatchExpiryChange(it)) },
            onDismiss = { showDatePicker = false },
        )
    }
}

@Composable
private fun BatchRow(batch: Batch, selected: Boolean, onClick: () -> Unit) {
    Surface(
        onClick = onClick,
        shape = RoundedCornerShape(12.dp),
        color = if (selected) {
            MaterialTheme.colorScheme.primaryContainer
        } else {
            MaterialTheme.colorScheme.surfaceContainerLow
        },
        modifier = Modifier.fillMaxWidth(),
    ) {
        Row(
            modifier = Modifier.padding(12.dp),
            horizontalArrangement = Arrangement.SpaceBetween,
            verticalAlignment = Alignment.CenterVertically,
        ) {
            Column(modifier = Modifier.weight(1f)) {
                Text(
                    text = batch.batchNumber?.takeIf { it.isNotBlank() }
                        ?: stringResource(R.string.pharmacy_detail_no_number),
                    style = MaterialTheme.typography.titleSmall,
                )
                Text(
                    text = batch.expiryDate?.let {
                        stringResource(R.string.pharmacy_detail_expiry, formatDate(it))
                    } ?: stringResource(R.string.pharmacy_detail_no_expiry),
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                )
                batch.location?.takeIf { it.isNotBlank() }?.let { location ->
                    Text(
                        text = location,
                        style = MaterialTheme.typography.labelSmall,
                        color = MaterialTheme.colorScheme.onSurfaceVariant,
                    )
                }
            }
            Text(
                text = stringResource(R.string.pharmacy_quantity_short, batch.quantity),
                style = MaterialTheme.typography.titleMedium,
            )
        }
    }
}

@Composable
private fun InventoryActionsCard(
    uiState: DrugDetailUiState,
    onAction: (DrugDetailAction) -> Unit,
) {
    Surface(
        shape = RoundedCornerShape(12.dp),
        color = MaterialTheme.colorScheme.surfaceContainerLow,
        modifier = Modifier.fillMaxWidth(),
    ) {
        Column(
            modifier = Modifier.padding(12.dp),
            verticalArrangement = Arrangement.spacedBy(8.dp),
        ) {
            Text(
                text = stringResource(R.string.pharmacy_detail_actions),
                style = MaterialTheme.typography.titleSmall,
            )
            AppTextField(
                value = uiState.amount,
                onValueChange = { onAction(DrugDetailAction.OnAmountChange(it)) },
                label = stringResource(R.string.pharmacy_detail_amount),
                keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
            )
            Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                OutlinedButton(
                    onClick = { onAction(DrugDetailAction.Record(InventoryEventType.RECEIVE)) },
                    enabled = uiState.canSubmitAmount,
                    modifier = Modifier.weight(1f),
                ) { Text(stringResource(R.string.pharmacy_action_receive)) }

                OutlinedButton(
                    onClick = { onAction(DrugDetailAction.Record(InventoryEventType.DISPENSE)) },
                    enabled = uiState.canSubmitAmount,
                    modifier = Modifier.weight(1f),
                ) { Text(stringResource(R.string.pharmacy_action_dispense)) }
            }
            Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                OutlinedButton(
                    onClick = { onAction(DrugDetailAction.Record(InventoryEventType.ADJUSTMENT)) },
                    enabled = uiState.canSubmitAmount,
                    modifier = Modifier.weight(1f),
                ) { Text(stringResource(R.string.pharmacy_action_adjust)) }

                Button(
                    onClick = { onAction(DrugDetailAction.Record(InventoryEventType.COUNT)) },
                    enabled = uiState.canSubmitAmount,
                    modifier = Modifier.weight(1f),
                ) { Text(stringResource(R.string.pharmacy_action_count)) }
            }
        }
    }
}

@Composable
private fun EventRow(event: InventoryEvent) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .padding(vertical = 2.dp),
        horizontalArrangement = Arrangement.SpaceBetween,
    ) {
        Text(
            text = eventTypeLabel(event.type),
            style = MaterialTheme.typography.bodySmall,
        )
        Text(
            text = if (event.quantityDelta > 0) "+${event.quantityDelta}" else "${event.quantityDelta}",
            style = MaterialTheme.typography.bodySmall,
            color = if (event.quantityDelta >= 0) {
                MaterialTheme.colorScheme.primary
            } else {
                MaterialTheme.colorScheme.error
            },
        )
    }
}

@Composable
private fun AddBatchDialog(
    uiState: DrugDetailUiState,
    onAction: (DrugDetailAction) -> Unit,
    onPickDate: () -> Unit,
) {
    androidx.compose.material3.AlertDialog(
        onDismissRequest = { onAction(DrugDetailAction.DismissAddBatch) },
        title = { Text(stringResource(R.string.pharmacy_detail_add_batch)) },
        text = {
            Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                AppTextField(
                    value = uiState.newBatchNumber,
                    onValueChange = { onAction(DrugDetailAction.OnNewBatchNumberChange(it)) },
                    label = stringResource(R.string.pharmacy_field_batch_number),
                )
                AppTextField(
                    value = uiState.newBatchExpiry?.let { formatDate(it) } ?: "",
                    onValueChange = {},
                    label = stringResource(R.string.pharmacy_field_expiry),
                    readOnly = true,
                    trailingIcon = {
                        TextButton(onClick = onPickDate) {
                            Text(stringResource(R.string.pharmacy_pick_date))
                        }
                    },
                )
                AppTextField(
                    value = uiState.newBatchLocation,
                    onValueChange = { onAction(DrugDetailAction.OnNewBatchLocationChange(it)) },
                    label = stringResource(R.string.pharmacy_field_location),
                )
            }
        },
        confirmButton = {
            TextButton(
                onClick = { onAction(DrugDetailAction.SaveBatch) },
                enabled = uiState.canSaveBatch,
            ) { Text(stringResource(R.string.pharmacy_save)) }
        },
        dismissButton = {
            TextButton(onClick = { onAction(DrugDetailAction.DismissAddBatch) }) {
                Text(stringResource(R.string.pharmacy_cancel))
            }
        },
    )
}

@Composable
private fun eventTypeLabel(type: InventoryEventType): String = when (type) {
    InventoryEventType.RECEIVE -> stringResource(R.string.pharmacy_event_receive)
    InventoryEventType.DISPENSE -> stringResource(R.string.pharmacy_event_dispense)
    InventoryEventType.ADJUSTMENT -> stringResource(R.string.pharmacy_event_adjust)
    InventoryEventType.COUNT -> stringResource(R.string.pharmacy_event_count)
}

private fun formatDate(millis: Long): String =
    SimpleDateFormat("yyyy/MM/dd", Locale.US).format(Date(millis))
