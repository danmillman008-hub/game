package ir.darookhaneh.stock.feature.pharmacy.presentation.dashboard

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.unit.dp
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import ir.darookhaneh.stock.core.model.pharmacy.BatchAlert
import ir.darookhaneh.stock.core.model.pharmacy.DashboardSnapshot
import ir.darookhaneh.stock.core.model.pharmacy.DrugSummary
import ir.darookhaneh.stock.feature.pharmacy.R
import org.koin.androidx.compose.koinViewModel

@Composable
fun DashboardRoute(
    onAddDrug: () -> Unit,
    onScan: () -> Unit,
    onOpenDrug: (Long) -> Unit,
    onOpenDrugs: () -> Unit,
) {
    val viewModel: DashboardViewModel = koinViewModel()
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    DashboardScreen(
        snapshot = uiState,
        onAddDrug = onAddDrug,
        onScan = onScan,
        onOpenDrug = onOpenDrug,
        onOpenDrugs = onOpenDrugs,
    )
}

@Composable
fun DashboardScreen(
    snapshot: DashboardSnapshot,
    onAddDrug: () -> Unit,
    onScan: () -> Unit,
    onOpenDrug: (Long) -> Unit,
    onOpenDrugs: () -> Unit,
) {
    Scaffold { padding ->
        LazyColumn(
            modifier = Modifier
                .fillMaxSize()
                .padding(padding)
                .padding(horizontal = 16.dp),
            verticalArrangement = Arrangement.spacedBy(10.dp),
        ) {
            item {
                Column(modifier = Modifier.padding(top = 16.dp)) {
                    Text(
                        text = stringResource(R.string.pharmacy_dashboard_title),
                        style = MaterialTheme.typography.headlineSmall,
                    )
                    Text(
                        text = stringResource(
                            R.string.pharmacy_dashboard_summary,
                            snapshot.drugCount,
                            snapshot.unitCount,
                        ),
                        style = MaterialTheme.typography.bodySmall,
                        color = MaterialTheme.colorScheme.onSurfaceVariant,
                    )
                }
            }

            item {
                Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                    StatCard(
                        label = stringResource(R.string.pharmacy_dashboard_low_stock),
                        value = snapshot.lowStockDrugs.size,
                        modifier = Modifier.weight(1f),
                    )
                    StatCard(
                        label = stringResource(R.string.pharmacy_dashboard_expiring),
                        value = snapshot.expiringSoon.size,
                        modifier = Modifier.weight(1f),
                    )
                    StatCard(
                        label = stringResource(R.string.pharmacy_dashboard_expired),
                        value = snapshot.expired.size,
                        modifier = Modifier.weight(1f),
                    )
                }
            }

            item {
                Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                    OutlinedButton(onClick = onScan, modifier = Modifier.weight(1f)) {
                        Text(stringResource(R.string.pharmacy_scan_barcode))
                    }
                    OutlinedButton(onClick = onAddDrug, modifier = Modifier.weight(1f)) {
                        Text(stringResource(R.string.pharmacy_add_manual))
                    }
                }
            }

            if (snapshot.expired.isNotEmpty()) {
                item { SectionTitle(stringResource(R.string.pharmacy_dashboard_expired)) }
                items(items = snapshot.expired, key = { "e-${it.batchId}" }) { alert ->
                    AlertRow(alert = alert, onClick = { onOpenDrug(alert.drugId) })
                }
            }

            if (snapshot.expiringSoon.isNotEmpty()) {
                item { SectionTitle(stringResource(R.string.pharmacy_dashboard_expiring)) }
                items(items = snapshot.expiringSoon, key = { "s-${it.batchId}" }) { alert ->
                    AlertRow(alert = alert, onClick = { onOpenDrug(alert.drugId) })
                }
            }

            if (snapshot.lowStockDrugs.isNotEmpty()) {
                item { SectionTitle(stringResource(R.string.pharmacy_dashboard_low_stock)) }
                items(items = snapshot.lowStockDrugs, key = { "l-${it.id}" }) { drug ->
                    LowStockRow(drug = drug, onClick = { onOpenDrug(drug.id) })
                }
            }

            if (
                snapshot.drugCount == 0 &&
                snapshot.expired.isEmpty() &&
                snapshot.expiringSoon.isEmpty()
            ) {
                item {
                    Text(
                        text = stringResource(R.string.pharmacy_empty_state),
                        style = MaterialTheme.typography.bodyLarge,
                        color = MaterialTheme.colorScheme.onSurfaceVariant,
                        modifier = Modifier.padding(vertical = 32.dp),
                    )
                }
            }

            item {
                OutlinedButton(onClick = onOpenDrugs, modifier = Modifier.fillMaxWidth()) {
                    Text(stringResource(R.string.pharmacy_dashboard_all_drugs))
                }
            }

            item { Column(modifier = Modifier.padding(bottom = 24.dp)) {} }
        }
    }
}

@Composable
private fun SectionTitle(text: String) {
    Text(
        text = text,
        style = MaterialTheme.typography.titleSmall,
        modifier = Modifier.padding(top = 8.dp),
    )
}

@Composable
private fun StatCard(label: String, value: Int, modifier: Modifier = Modifier) {
    Surface(
        modifier = modifier,
        shape = RoundedCornerShape(12.dp),
        color = MaterialTheme.colorScheme.surfaceContainerLow,
    ) {
        Column(
            modifier = Modifier.padding(12.dp),
            horizontalAlignment = Alignment.CenterHorizontally,
        ) {
            Text(text = value.toString(), style = MaterialTheme.typography.headlineSmall)
            Text(
                text = label,
                style = MaterialTheme.typography.labelSmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
            )
        }
    }
}

@Composable
private fun AlertRow(alert: BatchAlert, onClick: () -> Unit) {
    Surface(
        onClick = onClick,
        shape = RoundedCornerShape(12.dp),
        color = MaterialTheme.colorScheme.surfaceContainerLow,
        modifier = Modifier.fillMaxWidth(),
    ) {
        Row(
            modifier = Modifier.padding(12.dp),
            horizontalArrangement = Arrangement.SpaceBetween,
        ) {
            Column(modifier = Modifier.weight(1f)) {
                Text(text = alert.drugName, style = MaterialTheme.typography.titleSmall)
                Text(
                    text = stringResource(
                        R.string.pharmacy_dashboard_days_left,
                        alert.daysToExpiry ?: 0,
                    ),
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                )
            }
            Text(
                text = stringResource(R.string.pharmacy_quantity_short, alert.quantity),
                style = MaterialTheme.typography.labelLarge,
            )
        }
    }
}

@Composable
private fun LowStockRow(drug: DrugSummary, onClick: () -> Unit) {
    Surface(
        onClick = onClick,
        shape = RoundedCornerShape(12.dp),
        color = MaterialTheme.colorScheme.surfaceContainerLow,
        modifier = Modifier.fillMaxWidth(),
    ) {
        Row(
            modifier = Modifier.padding(12.dp),
            horizontalArrangement = Arrangement.SpaceBetween,
        ) {
            Text(text = drug.name, style = MaterialTheme.typography.titleSmall)
            Text(
                text = stringResource(R.string.pharmacy_quantity_short, drug.totalQuantity),
                style = MaterialTheme.typography.labelLarge,
                color = MaterialTheme.colorScheme.error,
            )
        }
    }
}
