package ir.darookhaneh.stock.feature.pharmacy.presentation.lookup

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.imePadding
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.text.KeyboardActions
import androidx.compose.foundation.text.KeyboardOptions
import androidx.compose.material3.Button
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
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
import ir.darookhaneh.stock.core.model.pharmacy.DrugLookupResult
import ir.darookhaneh.stock.core.model.pharmacy.LookupSource
import ir.darookhaneh.stock.core.model.pharmacy.formatJalali
import ir.darookhaneh.stock.feature.pharmacy.R
import org.koin.androidx.compose.koinViewModel

/**
 * صفحهٔ «استعلام از سامانهٔ تیتک».
 *
 * این صفحه پاسخ مستقیم به این ایراد کارفرماست: «نه دکمهٔ مشخصی گذاشتی نه روش
 * مشخصی». اینجا یک ورودی کد، یک دکمهٔ اصلی بزرگ، نوع کدِ تشخیص‌داده‌شده، و
 * توضیح شفاف اینکه چه چیزی و کجا فرستاده می‌شود وجود دارد.
 */
@Composable
fun LookupRoute(
    initialCode: String? = null,
    onOpenDrug: (Long) -> Unit,
    onManualAdd: () -> Unit,
) {
    val viewModel: LookupViewModel = koinViewModel()
    val uiState by viewModel.uiState.collectAsStateWithLifecycle()

    // اگر از اسکن یا از صفحهٔ ثبت با کد آمده‌ایم، همان کد از قبل پر است.
    LaunchedEffect(initialCode) {
        if (!initialCode.isNullOrBlank() && uiState.input.isBlank()) {
            viewModel.onAction(LookupScreenAction.OnInputChange(initialCode))
        }
    }

    LaunchedEffect(uiState.openDrugId) {
        uiState.openDrugId?.let { drugId ->
            viewModel.onAction(LookupScreenAction.ConsumeOpenDrug)
            onOpenDrug(drugId)
        }
    }

    LookupScreen(
        uiState = uiState,
        onAction = viewModel::onAction,
        onManualAdd = onManualAdd,
    )
}

@Composable
fun LookupScreen(
    uiState: LookupScreenState,
    onAction: (LookupScreenAction) -> Unit,
    onManualAdd: () -> Unit,
) {
    val bottomInset = LocalBottomBarInset.current
    var showHowItWorks by remember { mutableStateOf(false) }

    LazyColumn(
        modifier = Modifier
            .fillMaxSize()
            .imePadding()
            .padding(horizontal = 16.dp),
        verticalArrangement = Arrangement.spacedBy(12.dp),
        contentPadding = androidx.compose.foundation.layout.PaddingValues(
            top = 16.dp,
            bottom = bottomInset + 24.dp,
        ),
    ) {
        item {
            Column {
                Text(
                    text = stringResource(R.string.pharmacy_lookup_screen_title),
                    style = MaterialTheme.typography.headlineSmall,
                    fontWeight = FontWeight.Bold,
                )
                Text(
                    text = stringResource(R.string.pharmacy_lookup_screen_subtitle),
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                )
            }
        }

        // ---------- مرحله ۱: کد ----------
        item {
            Surface(
                shape = RoundedCornerShape(16.dp),
                color = MaterialTheme.colorScheme.surfaceContainerLow,
                modifier = Modifier.fillMaxWidth(),
            ) {
                Column(
                    modifier = Modifier.padding(14.dp),
                    verticalArrangement = Arrangement.spacedBy(10.dp),
                ) {
                    Text(
                        text = stringResource(R.string.pharmacy_lookup_step_code),
                        style = MaterialTheme.typography.titleSmall,
                        fontWeight = FontWeight.Bold,
                    )
                    AppTextField(
                        value = uiState.input,
                        onValueChange = { onAction(LookupScreenAction.OnInputChange(it)) },
                        label = stringResource(R.string.pharmacy_lookup_code_label),
                        keyboardOptions = KeyboardOptions(
                            keyboardType = KeyboardType.Number,
                            imeAction = ImeAction.Search,
                        ),
                        keyboardActions = KeyboardActions(
                            onSearch = { if (uiState.canLookup) onAction(LookupScreenAction.Start) },
                        ),
                    )
                    Text(
                        text = uiState.kind.label,
                        style = MaterialTheme.typography.labelMedium,
                        color = if (uiState.kind == LookupCodeKind.UNKNOWN) {
                            MaterialTheme.colorScheme.error
                        } else {
                            MaterialTheme.colorScheme.primary
                        },
                    )

                    // دکمهٔ اصلی و بزرگ: همین چیزی که «مشخص نبود».
                    Button(
                        onClick = { onAction(LookupScreenAction.Start) },
                        enabled = uiState.canLookup,
                        modifier = Modifier
                            .fillMaxWidth()
                            .height(52.dp),
                        shape = RoundedCornerShape(14.dp),
                    ) {
                        if (uiState.isLoading) {
                            CircularProgressIndicator(
                                modifier = Modifier.size(20.dp),
                                strokeWidth = 2.dp,
                                color = MaterialTheme.colorScheme.onPrimary,
                            )
                            Text(
                                text = stringResource(R.string.pharmacy_lookup_running),
                                modifier = Modifier.padding(start = 10.dp),
                            )
                        } else {
                            Text(
                                text = stringResource(R.string.pharmacy_lookup_start),
                                style = MaterialTheme.typography.titleMedium,
                            )
                        }
                    }

                    Row(
                        modifier = Modifier.fillMaxWidth(),
                        horizontalArrangement = Arrangement.spacedBy(8.dp),
                    ) {
                        OutlinedButton(
                            onClick = onManualAdd,
                            modifier = Modifier.weight(1f),
                        ) {
                            Text(stringResource(R.string.pharmacy_lookup_manual_instead))
                        }
                        TextButton(
                            onClick = { showHowItWorks = !showHowItWorks },
                            modifier = Modifier.weight(1f),
                        ) {
                            Text(
                                stringResource(
                                    if (showHowItWorks) R.string.pharmacy_lookup_how_hide
                                    else R.string.pharmacy_lookup_how_show
                                )
                            )
                        }
                    }

                    if (showHowItWorks) {
                        Surface(
                            shape = RoundedCornerShape(12.dp),
                            color = MaterialTheme.colorScheme.surfaceContainerHigh,
                            modifier = Modifier.fillMaxWidth(),
                        ) {
                            Column(
                                modifier = Modifier.padding(12.dp),
                                verticalArrangement = Arrangement.spacedBy(6.dp),
                            ) {
                                Text(
                                    text = stringResource(R.string.pharmacy_lookup_how_what),
                                    style = MaterialTheme.typography.bodySmall,
                                )
                                Text(
                                    text = stringResource(R.string.pharmacy_lookup_how_where),
                                    style = MaterialTheme.typography.bodySmall,
                                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                                )
                                Text(
                                    text = stringResource(R.string.pharmacy_lookup_how_offline),
                                    style = MaterialTheme.typography.bodySmall,
                                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                                )
                            }
                        }
                    }
                }
            }
        }

        // ---------- مرحله ۲: نتیجه ----------
        uiState.error?.let { message ->
            item {
                Surface(
                    shape = RoundedCornerShape(14.dp),
                    color = MaterialTheme.colorScheme.errorContainer,
                    modifier = Modifier.fillMaxWidth(),
                ) {
                    Column(
                        modifier = Modifier.padding(14.dp),
                        verticalArrangement = Arrangement.spacedBy(8.dp),
                    ) {
                        Text(
                            text = stringResource(R.string.pharmacy_lookup_error_title),
                            style = MaterialTheme.typography.titleSmall,
                            fontWeight = FontWeight.Bold,
                            color = MaterialTheme.colorScheme.onErrorContainer,
                        )
                        Text(
                            text = message,
                            style = MaterialTheme.typography.bodySmall,
                            color = MaterialTheme.colorScheme.onErrorContainer,
                        )
                        if (uiState.canLookup) {
                            TextButton(onClick = { onAction(LookupScreenAction.Start) }) {
                                Text(stringResource(R.string.pharmacy_lookup_retry))
                            }
                        }
                    }
                }
            }
        }

        uiState.result?.let { result ->
            item { LookupResultCard(result = result, uiState = uiState, onAction = onAction) }
        }

        uiState.notice?.let { notice ->
            item {
                Text(
                    text = notice,
                    style = MaterialTheme.typography.bodySmall,
                    color = MaterialTheme.colorScheme.primary,
                )
            }
        }
    }
}

@Composable
private fun LookupResultCard(
    result: DrugLookupResult,
    uiState: LookupScreenState,
    onAction: (LookupScreenAction) -> Unit,
) {
    Surface(
        shape = RoundedCornerShape(16.dp),
        color = MaterialTheme.colorScheme.surfaceContainerHigh,
        modifier = Modifier.fillMaxWidth(),
    ) {
        Column(
            modifier = Modifier.padding(14.dp),
            verticalArrangement = Arrangement.spacedBy(8.dp),
        ) {
            Text(
                text = stringResource(R.string.pharmacy_lookup_result_title),
                style = MaterialTheme.typography.labelMedium,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
            )
            Text(
                text = result.name,
                style = MaterialTheme.typography.titleLarge,
                fontWeight = FontWeight.Bold,
            )
            result.englishName?.takeIf { it.isNotBlank() }?.let {
                Text(text = it, style = MaterialTheme.typography.bodySmall)
            }

            InfoRow(stringResource(R.string.pharmacy_lookup_field_company), result.company)
            InfoRow("GTIN", result.gtin)
            InfoRow("IRC", result.irc)
            InfoRow(
                stringResource(R.string.pharmacy_lookup_field_price),
                result.price?.let { formatPrice(it) },
            )
            InfoRow(
                stringResource(R.string.pharmacy_lookup_field_status),
                result.statusMessage?.takeIf { it.isNotBlank() }
                    ?: when (result.isAuthentic) {
                        true -> stringResource(R.string.pharmacy_lookup_status_ok)
                        false -> stringResource(R.string.pharmacy_lookup_status_bad)
                        null -> stringResource(R.string.pharmacy_lookup_status_unknown)
                    },
            )
            InfoRow(
                stringResource(R.string.pharmacy_lookup_field_time),
                formatJalali(if (result.fetchedAt > 0) result.fetchedAt else null),
            )
            Text(
                text = if (result.source == LookupSource.CACHE) {
                    stringResource(R.string.pharmacy_lookup_source_cache)
                } else {
                    stringResource(R.string.pharmacy_lookup_source_network)
                },
                style = MaterialTheme.typography.labelSmall,
                color = MaterialTheme.colorScheme.onSurfaceVariant,
            )

            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.spacedBy(8.dp),
            ) {
                Button(
                    onClick = { onAction(LookupScreenAction.Apply) },
                    enabled = uiState.canApply,
                    modifier = Modifier
                        .weight(1f)
                        .height(48.dp),
                    shape = RoundedCornerShape(12.dp),
                ) {
                    Text(stringResource(R.string.pharmacy_lookup_apply))
                }
                TextButton(onClick = { onAction(LookupScreenAction.DismissResult) }) {
                    Text(stringResource(R.string.pharmacy_lookup_clear))
                }
            }
        }
    }
}

@Composable
private fun InfoRow(label: String, value: String?) {
    if (value.isNullOrBlank()) return
    Row(
        modifier = Modifier.fillMaxWidth(),
        horizontalArrangement = Arrangement.SpaceBetween,
        verticalAlignment = Alignment.CenterVertically,
    ) {
        Text(
            text = label,
            style = MaterialTheme.typography.labelMedium,
            color = MaterialTheme.colorScheme.onSurfaceVariant,
        )
        Text(text = value, style = MaterialTheme.typography.bodyMedium)
    }
}

/** قیمت تیتک به ریال است؛ به‌صورت «۱۲٬۵۰۰ ریال» نمایش داده می‌شود. */
private fun formatPrice(value: Long): String {
    val grouped = value.toString().reversed().chunked(3).joinToString("٬").reversed()
    return "$grouped ریال"
}
