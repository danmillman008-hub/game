package ir.darookhaneh.stock.feature.pharmacy.presentation.history

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.FilterChip
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import ir.darookhaneh.stock.core.designsystem.component.AppTextField
import ir.darookhaneh.stock.core.designsystem.tokens.LocalBottomBarInset
import ir.darookhaneh.stock.core.model.pharmacy.HistoryEntry
import ir.darookhaneh.stock.core.model.pharmacy.InventoryEventType
import ir.darookhaneh.stock.core.model.pharmacy.JalaliDate
import ir.darookhaneh.stock.core.model.pharmacy.formatJalali
import ir.darookhaneh.stock.feature.pharmacy.R
import org.koin.androidx.compose.koinViewModel

@Composable
fun HistoryRoute() {
    val viewModel: HistoryViewModel = koinViewModel()
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()
    HistoryScreen(uiState = uiState, onAction = viewModel::onAction)
}

@Composable
fun HistoryScreen(
    uiState: HistoryUiState,
    onAction: (HistoryAction) -> Unit,
) {
    val bottomInset = LocalBottomBarInset.current
    LazyColumn(
        modifier = Modifier
            .fillMaxSize()
            .padding(horizontal = 16.dp),
        verticalArrangement = Arrangement.spacedBy(8.dp),
        contentPadding = PaddingValues(top = 16.dp, bottom = bottomInset + 24.dp),
    ) {
        item {
            Text(
                text = stringResource(R.string.pharmacy_history_title),
                style = MaterialTheme.typography.headlineSmall,
                fontWeight = FontWeight.Bold,
            )
        }
        item {
            AppTextField(
                value = uiState.query,
                onValueChange = { onAction(HistoryAction.OnQueryChange(it)) },
                label = stringResource(R.string.pharmacy_history_search),
            )
        }
        item {
            Row(horizontalArrangement = Arrangement.spacedBy(6.dp)) {
                FilterChip(
                    selected = uiState.filter == null,
                    onClick = { onAction(HistoryAction.OnFilterChange(null)) },
                    label = { Text("همه") },
                )
                FilterChip(
                    selected = uiState.filter == InventoryEventType.RECEIVE,
                    onClick = { onAction(HistoryAction.OnFilterChange(InventoryEventType.RECEIVE)) },
                    label = { Text(stringResource(R.string.pharmacy_action_receive)) },
                )
                FilterChip(
                    selected = uiState.filter == InventoryEventType.DISPENSE,
                    onClick = { onAction(HistoryAction.OnFilterChange(InventoryEventType.DISPENSE)) },
                    label = { Text(stringResource(R.string.pharmacy_action_dispense)) },
                )
                FilterChip(
                    selected = uiState.filter == InventoryEventType.DAMAGE,
                    onClick = { onAction(HistoryAction.OnFilterChange(InventoryEventType.DAMAGE)) },
                    label = { Text(stringResource(R.string.pharmacy_action_damage)) },
                )
            }
        }

        if (uiState.isEmpty) {
            item {
                Text(
                    text = stringResource(R.string.pharmacy_history_empty),
                    style = MaterialTheme.typography.bodyMedium,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                    modifier = Modifier.padding(vertical = 24.dp),
                )
            }
        }

        items(items = uiState.entries, key = { "h-${it.eventId}" }) { entry ->
            HistoryRowItem(entry = entry)
        }
    }
}

@Composable
private fun HistoryRowItem(entry: HistoryEntry) {
    Surface(
        shape = RoundedCornerShape(12.dp),
        color = MaterialTheme.colorScheme.surfaceContainerLow,
        modifier = Modifier.fillMaxWidth(),
    ) {
        Row(
            modifier = Modifier.padding(12.dp),
            verticalAlignment = Alignment.CenterVertically,
        ) {
            Column(modifier = Modifier.weight(1f)) {
                Text(text = entry.drugName, style = MaterialTheme.typography.titleSmall)
                Text(
                    text = listOfNotNull(
                        eventLabel(entry.type),
                        entry.batchNumber?.let { "بچ $it" },
                        entry.expiryDate?.let { "انقضا ${formatJalali(it)}" },
                        formatJalali(entry.createdAt) + " " + timeOfDay(entry.createdAt),
                    ).joinToString(" · "),
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                )
                entry.note?.takeIf { it.isNotBlank() }?.let { note ->
                    Text(
                        text = note,
                        style = MaterialTheme.typography.labelSmall,
                        color = MaterialTheme.colorScheme.onSurfaceVariant,
                    )
                }
            }
            Column(horizontalAlignment = Alignment.End) {
                Text(
                    text = signed(entry.quantityDelta),
                    style = MaterialTheme.typography.titleMedium,
                    color = if (entry.quantityDelta >= 0) {
                        MaterialTheme.colorScheme.primary
                    } else {
                        MaterialTheme.colorScheme.error
                    },
                )
                Text(
                    text = stringResource(R.string.pharmacy_history_stock_after, entry.batchQuantity),
                    style = MaterialTheme.typography.labelSmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                )
            }
        }
    }
}

@Composable
private fun eventLabel(type: InventoryEventType): String = when (type) {
    InventoryEventType.RECEIVE -> stringResource(R.string.pharmacy_action_receive)
    InventoryEventType.DISPENSE -> stringResource(R.string.pharmacy_action_dispense)
    InventoryEventType.ADJUSTMENT -> stringResource(R.string.pharmacy_action_adjust)
    InventoryEventType.COUNT -> stringResource(R.string.pharmacy_action_count)
    InventoryEventType.DAMAGE -> stringResource(R.string.pharmacy_action_damage)
    InventoryEventType.RETURN -> stringResource(R.string.pharmacy_action_return)
}

private fun signed(value: Int): String {
    val digits = JalaliDate.toPersianDigits(if (value > 0) "+$value" else value.toString())
    return digits
}

private fun timeOfDay(millis: Long): String {
    val date = java.time.Instant.ofEpochMilli(millis)
        .atZone(java.time.ZoneId.systemDefault())
    return JalaliDate.toPersianDigits(
        "%02d:%02d".format(date.hour, date.minute)
    )
}
