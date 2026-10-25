package ir.darookhaneh.stock.feature.pharmacy.presentation.record

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.imePadding
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.AssistChip
import androidx.compose.material3.Button
import androidx.compose.material3.FilterChip
import androidx.compose.material3.MaterialTheme
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
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.text.input.ImeAction
import androidx.compose.ui.text.input.KeyboardType
import androidx.compose.ui.unit.dp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import ir.darookhaneh.stock.core.designsystem.component.AppTextField
import ir.darookhaneh.stock.core.designsystem.tokens.LocalBottomBarInset
import ir.darookhaneh.stock.core.model.pharmacy.CountingMode
import ir.darookhaneh.stock.core.model.pharmacy.DrugSummary
import ir.darookhaneh.stock.core.model.pharmacy.InventoryEventType
import ir.darookhaneh.stock.core.model.pharmacy.JalaliDate
import ir.darookhaneh.stock.core.model.pharmacy.formatJalali
import ir.darookhaneh.stock.core.presentation.component.AppDatePickerDialog
import ir.darookhaneh.stock.feature.pharmacy.R
import ir.darookhaneh.stock.feature.pharmacy.presentation.lookup.LookupSection
import org.koin.androidx.compose.koinViewModel

/**
 * ثبت سریع: یک صفحه برای ورود/خروج/ضایعات/مرجوعی/شمارش.
 * سه روش شمارش (تکی، کارتن، باز) همان چیزی است که در نسخهٔ HTML وجود داشت.
 */
@Composable
fun RecordRoute(
    onCreatedDrugNeeded: (String?) -> Unit,
    onOpenScan: () -> Unit,
) {
    val viewModel: RecordViewModel = koinViewModel()
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    RecordScreen(
        uiState = uiState,
        onAction = viewModel::onAction,
        onCreatedDrugNeeded = onCreatedDrugNeeded,
        onOpenScan = onOpenScan,
    )
}

@Composable
fun RecordScreen(
    uiState: RecordUiState,
    onAction: (RecordAction) -> Unit,
    onCreatedDrugNeeded: (String?) -> Unit = {},
    onOpenScan: () -> Unit = {},
) {
    var showDatePicker by remember { mutableStateOf(false) }
    val bottomInset = LocalBottomBarInset.current

    LazyColumn(
        modifier = Modifier
            .fillMaxSize()
            .imePadding()
            .padding(horizontal = 16.dp),
        verticalArrangement = Arrangement.spacedBy(10.dp),
        contentPadding = androidx.compose.foundation.layout.PaddingValues(
            top = 16.dp,
            bottom = bottomInset + 24.dp,
        ),
    ) {
        item {
            Row(
                modifier = Modifier.fillMaxWidth(),
                verticalAlignment = Alignment.CenterVertically,
            ) {
                Column(modifier = Modifier.weight(1f)) {
                    Text(
                        text = stringResource(R.string.pharmacy_record_title),
                        style = MaterialTheme.typography.headlineSmall,
                        fontWeight = FontWeight.Bold,
                    )
                    Text(
                        text = stringResource(R.string.pharmacy_record_subtitle),
                        style = MaterialTheme.typography.bodySmall,
                        color = MaterialTheme.colorScheme.onSurfaceVariant,
                    )
                }
                TextButton(onClick = onOpenScan) { Text(stringResource(R.string.pharmacy_scan_barcode)) }
            }
        }

        val drug = uiState.selectedDrug
        if (drug == null) {
            item {
                AppTextField(
                    value = uiState.query,
                    onValueChange = { onAction(RecordAction.OnQueryChange(it)) },
                    label = stringResource(R.string.pharmacy_record_search_label),
                    keyboardOptions = KeyboardOptions(imeAction = ImeAction.Search),
                )
            }

            if (uiState.query.isBlank()) {
                item {
                    Text(
                        text = stringResource(R.string.pharmacy_record_pick_hint),
                        style = MaterialTheme.typography.bodyMedium,
                        color = MaterialTheme.colorScheme.onSurfaceVariant,
                        modifier = Modifier.padding(vertical = 12.dp),
                    )
                }
            }

            if (uiState.query.isNotBlank() && uiState.results.isEmpty()) {
                item {
                    Surface(
                        shape = RoundedCornerShape(12.dp),
                        color = MaterialTheme.colorScheme.surfaceContainerLow,
                        modifier = Modifier.fillMaxWidth(),
                    ) {
                        Column(modifier = Modifier.padding(12.dp)) {
                            Text(
                                text = stringResource(R.string.pharmacy_no_result),
                                style = MaterialTheme.typography.bodyMedium,
                            )
                            TextButton(onClick = { onCreatedDrugNeeded(uiState.query) }) {
                                Text(stringResource(R.string.pharmacy_record_create_new))
                            }
                            // استعلام آنلاین: فقط با تصمیم کاربر؛ اپ بدون اینترنت کامل کار می‌کند.
                            if (uiState.lookup == null && JalaliDate.latinDigits(uiState.query).count(Char::isDigit) >= 8) {
                                TextButton(onClick = { onAction(RecordAction.StartLookup) }) {
                                    Text(stringResource(R.string.pharmacy_lookup_button))
                                }
                            }
                        }
                    }
                }
            }

            // کارت استعلام تیتک: وقتی دارو انتخاب نشده (یعنی دنبال دارو هستیم) یا
            // وقتی کاربر خودش استعلام خواسته است.
            if (uiState.selectedDrug == null || uiState.lookup != null) {
                item {
                    LookupSection(
                        state = uiState.lookup,
                        canLookup = JalaliDate.latinDigits(uiState.query).count(Char::isDigit) >= 8,
                        onStart = { onAction(RecordAction.StartLookup) },
                        onApply = { onAction(RecordAction.CreateFromLookup) },
                        onDismiss = { onAction(RecordAction.DismissLookup) },
                        applyLabel = stringResource(R.string.pharmacy_lookup_add_drug),
                    )
                }
            }

            items(items = uiState.results, key = { "d-${it.id}" }) { item ->
                DrugPickRow(drug = item, onClick = { onAction(RecordAction.SelectDrug(item)) })
            }
        } else {
            item { SelectedDrugCard(drug = drug, onChange = { onAction(RecordAction.ClearDrug) }) }
            item { OperationChips(selected = uiState.operation, onSelect = { onAction(RecordAction.OnOperation(it)) }) }
            item {
                BatchSection(
                    uiState = uiState,
                    onAction = onAction,
                    onPickDate = { showDatePicker = true },
                )
            }
            item { CountingSection(uiState = uiState, onAction = onAction) }

            item {
                Text(
                    text = uiState.preview,
                    style = MaterialTheme.typography.titleMedium,
                    color = if (uiState.units > 0) {
                        MaterialTheme.colorScheme.primary
                    } else {
                        MaterialTheme.colorScheme.onSurfaceVariant
                    },
                )
            }

            item {
                AppTextField(
                    value = uiState.note,
                    onValueChange = { onAction(RecordAction.OnNoteChange(it)) },
                    label = stringResource(R.string.pharmacy_record_note),
                )
            }

            uiState.message?.let { message ->
                item {
                    Surface(
                        shape = RoundedCornerShape(12.dp),
                        color = if (uiState.isError) {
                            MaterialTheme.colorScheme.errorContainer
                        } else {
                            MaterialTheme.colorScheme.primaryContainer
                        },
                        modifier = Modifier.fillMaxWidth(),
                    ) {
                        Text(
                            text = message,
                            style = MaterialTheme.typography.bodyMedium,
                            modifier = Modifier.padding(12.dp),
                        )
                    }
                }
            }

            item {
                Button(
                    onClick = { onAction(RecordAction.Save) },
                    enabled = uiState.canSave,
                    modifier = Modifier
                        .fillMaxWidth()
                        .padding(top = 4.dp),
                    shape = RoundedCornerShape(14.dp),
                ) {
                    Text(
                        text = stringResource(R.string.pharmacy_record_save),
                        style = MaterialTheme.typography.titleMedium,
                        modifier = Modifier.padding(vertical = 6.dp),
                    )
                }
            }
        }
    }

    if (showDatePicker) {
        AppDatePickerDialog(
            initialDateMillis = uiState.expiryMillis,
            title = stringResource(R.string.pharmacy_field_expiry),
            onDateSelected = { onAction(RecordAction.OnExpiryPicked(it)) },
            onDismiss = { showDatePicker = false },
        )
    }
}

@Composable
private fun DrugPickRow(drug: DrugSummary, onClick: () -> Unit) {
    Surface(
        onClick = onClick,
        shape = RoundedCornerShape(12.dp),
        color = MaterialTheme.colorScheme.surfaceContainerLow,
        modifier = Modifier.fillMaxWidth(),
    ) {
        Row(
            modifier = Modifier.padding(12.dp),
            verticalAlignment = Alignment.CenterVertically,
        ) {
            Column(modifier = Modifier.weight(1f)) {
                Text(text = drug.name, style = MaterialTheme.typography.titleSmall)
                Text(
                    text = listOfNotNull(
                        drug.gtin?.let { "GTIN $it" },
                        drug.packSize?.let { "${JalaliDate.toPersianDigits(it)} در بسته" },
                    ).joinToString(" · ").ifBlank { "—" },
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                )
            }
            Text(
                text = stringResource(R.string.pharmacy_quantity_short, drug.totalQuantity),
                style = MaterialTheme.typography.titleMedium,
            )
        }
    }
}

@Composable
private fun SelectedDrugCard(drug: DrugSummary, onChange: () -> Unit) {
    Surface(
        shape = RoundedCornerShape(14.dp),
        color = MaterialTheme.colorScheme.primaryContainer,
        modifier = Modifier.fillMaxWidth(),
    ) {
        Row(
            modifier = Modifier.padding(12.dp),
            verticalAlignment = Alignment.CenterVertically,
        ) {
            Column(modifier = Modifier.weight(1f)) {
                Text(
                    text = drug.name,
                    style = MaterialTheme.typography.titleMedium,
                    fontWeight = FontWeight.Bold,
                )
                Text(
                    text = stringResource(R.string.pharmacy_record_stock_now, drug.totalQuantity),
                    style = MaterialTheme.typography.bodySmall,
                )
            }
            TextButton(onClick = onChange) { Text(stringResource(R.string.pharmacy_record_change_drug)) }
        }
    }
}

@Composable
private fun OperationChips(selected: InventoryEventType, onSelect: (InventoryEventType) -> Unit) {
    val operations = listOf(
        InventoryEventType.RECEIVE to R.string.pharmacy_action_receive,
        InventoryEventType.DISPENSE to R.string.pharmacy_action_dispense,
        InventoryEventType.DAMAGE to R.string.pharmacy_action_damage,
        InventoryEventType.RETURN to R.string.pharmacy_action_return,
        InventoryEventType.COUNT to R.string.pharmacy_action_count,
    )
    Column(verticalArrangement = Arrangement.spacedBy(4.dp)) {
        Text(
            text = stringResource(R.string.pharmacy_record_operation),
            style = MaterialTheme.typography.titleSmall,
        )
        Row(horizontalArrangement = Arrangement.spacedBy(6.dp)) {
            operations.take(3).forEach { (type, label) ->
                FilterChip(
                    selected = selected == type,
                    onClick = { onSelect(type) },
                    label = { Text(stringResource(label)) },
                )
            }
        }
        Row(horizontalArrangement = Arrangement.spacedBy(6.dp)) {
            operations.drop(3).forEach { (type, label) ->
                FilterChip(
                    selected = selected == type,
                    onClick = { onSelect(type) },
                    label = { Text(stringResource(label)) },
                )
            }
        }
    }
}

@Composable
private fun BatchSection(
    uiState: RecordUiState,
    onAction: (RecordAction) -> Unit,
    onPickDate: () -> Unit,
) {
    Column(verticalArrangement = Arrangement.spacedBy(6.dp)) {
        Text(
            text = stringResource(R.string.pharmacy_record_batch),
            style = MaterialTheme.typography.titleSmall,
        )
        Row(horizontalArrangement = Arrangement.spacedBy(6.dp)) {
            uiState.batches.take(3).forEach { batch ->
                val label = batch.batchNumber ?: batch.expiryDate?.let {
                    formatJalali(it)
                } ?: "بچ ${batch.id}"
                FilterChip(
                    selected = !uiState.creatingBatch && uiState.selectedBatchId == batch.id,
                    onClick = { onAction(RecordAction.SelectBatch(batch.id)) },
                    label = { Text("$label · ${JalaliDate.toPersianDigits(batch.quantity)}") },
                )
            }
            AssistChip(
                onClick = { onAction(RecordAction.StartNewBatch) },
                label = { Text(stringResource(R.string.pharmacy_record_new_batch)) },
            )
        }

        if (uiState.needsBatchIdentity) {
            AppTextField(
                value = uiState.batchNumber,
                onValueChange = { onAction(RecordAction.OnBatchNumberChange(it)) },
                label = stringResource(R.string.pharmacy_field_batch_number),
            )
            AppTextField(
                value = uiState.expiryText,
                onValueChange = { onAction(RecordAction.OnExpiryTextChange(JalaliDate.latinDigits(it))) },
                label = stringResource(R.string.pharmacy_field_expiry_jalali),
                trailingIcon = {
                    TextButton(onClick = onPickDate) {
                        Text(stringResource(R.string.pharmacy_pick_date))
                    }
                },
            )
        }
    }
}

@Composable
private fun CountingSection(uiState: RecordUiState, onAction: (RecordAction) -> Unit) {
    Column(verticalArrangement = Arrangement.spacedBy(6.dp)) {
        Row(horizontalArrangement = Arrangement.spacedBy(6.dp)) {
            FilterChip(
                selected = uiState.mode == CountingMode.SINGLE,
                onClick = { onAction(RecordAction.OnMode(CountingMode.SINGLE)) },
                label = { Text(stringResource(R.string.pharmacy_mode_single)) },
            )
            FilterChip(
                selected = uiState.mode == CountingMode.CARTON,
                onClick = { onAction(RecordAction.OnMode(CountingMode.CARTON)) },
                label = { Text(stringResource(R.string.pharmacy_mode_carton)) },
            )
            FilterChip(
                selected = uiState.mode == CountingMode.OPEN,
                onClick = { onAction(RecordAction.OnMode(CountingMode.OPEN)) },
                label = { Text(stringResource(R.string.pharmacy_mode_open)) },
            )
        }

        when (uiState.mode) {
            CountingMode.SINGLE -> AppTextField(
                value = uiState.packs,
                onValueChange = { onAction(RecordAction.OnPacksChange(it)) },
                label = stringResource(R.string.pharmacy_field_packs),
                keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
            )

            CountingMode.CARTON -> {
                Row(horizontalArrangement = Arrangement.spacedBy(6.dp)) {
                    AppTextField(
                        value = uiState.cartons,
                        onValueChange = { onAction(RecordAction.OnCartonsChange(it)) },
                        label = stringResource(R.string.pharmacy_field_cartons),
                        keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
                        modifier = Modifier.weight(1f),
                    )
                    AppTextField(
                        value = uiState.unitsPerCarton.ifBlank {
                            uiState.packSize?.toString().orEmpty()
                        },
                        onValueChange = { onAction(RecordAction.OnUnitsPerCartonChange(it)) },
                        label = stringResource(R.string.pharmacy_field_per_carton),
                        keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
                        modifier = Modifier.weight(1f),
                    )
                }
                AppTextField(
                    value = uiState.loosePacks,
                    onValueChange = { onAction(RecordAction.OnLoosePacksChange(it)) },
                    label = stringResource(R.string.pharmacy_field_loose_packs),
                    keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
                )
            }

            CountingMode.OPEN -> {
                AppTextField(
                    value = uiState.packs,
                    onValueChange = { onAction(RecordAction.OnPacksChange(it)) },
                    label = stringResource(R.string.pharmacy_field_full_packs),
                    keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
                )
                AppTextField(
                    value = uiState.openUnits,
                    onValueChange = { onAction(RecordAction.OnOpenUnitsChange(it)) },
                    label = stringResource(R.string.pharmacy_field_open_units),
                    keyboardOptions = KeyboardOptions(keyboardType = KeyboardType.Number),
                )
            }
        }
    }
}
