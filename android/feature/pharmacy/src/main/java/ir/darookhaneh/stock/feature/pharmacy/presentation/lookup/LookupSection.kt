package ir.darookhaneh.stock.feature.pharmacy.presentation.lookup

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Button
import androidx.compose.material3.CircularProgressIndicator
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.runtime.Immutable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import ir.darookhaneh.stock.core.model.pharmacy.DrugLookupResult
import ir.darookhaneh.stock.core.model.pharmacy.LookupSource
import ir.darookhaneh.stock.feature.pharmacy.R

/**
 * وضعیت استعلام یک کد از سامانهٔ تیتک.
 *
 * قاعدهٔ محصول: استعلام **همیشه** با اقدام کاربر شروع می‌شود؛ هیچ فراخوانی خودکاری
 * در مسیر اسکن یا باز شدن صفحه وجود ندارد.
 */
@Immutable
data class LookupUiState(
    val code: String,
    val isLoading: Boolean = false,
    val result: DrugLookupResult? = null,
    val error: String? = null,
)

/**
 * کارت مشترک استعلام برای «ثبت سریع» و «ثبت دستی دارو».
 *
 * چرا مشترک: دو صفحه یک رفتار واحد دارند؛ تکرار UI باعث می‌شد یکی از دیگری عقب بماند
 * (همان اشکالی که در نسخهٔ HTML با دو نسخهٔ متفاوت از فرم وجود داشت).
 *
 * @param state null یعنی کاربر هنوز استعلامی نخواسته است (فقط دکمه نمایش داده می‌شود).
 * @param canLookup آیا کد فعلی شکل معتبری دارد (حداقل ۸ رقم).
 * @param onApply فقط وقتی نتیجه داریم معنا دارد؛ در ثبت سریع «ثبت این دارو» و در
 *   فرم دستی «پر کردن فیلدها» است.
 */
@Composable
fun LookupSection(
    state: LookupUiState?,
    canLookup: Boolean,
    onStart: () -> Unit,
    onApply: () -> Unit,
    onDismiss: () -> Unit,
    applyLabel: String,
    modifier: Modifier = Modifier,
) {
    if (state == null) {
        // کارت روشن با دکمهٔ بزرگ — نه یک دکمهٔ خاکستری که گم شود.
        Surface(
            shape = RoundedCornerShape(14.dp),
            color = MaterialTheme.colorScheme.surfaceContainerLow,
            modifier = modifier.fillMaxWidth(),
        ) {
            Column(
                modifier = Modifier.padding(12.dp),
                verticalArrangement = Arrangement.spacedBy(8.dp),
            ) {
                Text(
                    text = stringResource(R.string.pharmacy_lookup_button),
                    style = MaterialTheme.typography.titleSmall,
                    fontWeight = FontWeight.Bold,
                )
                Text(
                    text = stringResource(
                        if (canLookup) R.string.pharmacy_lookup_ready
                        else R.string.pharmacy_lookup_need_code
                    ),
                    style = MaterialTheme.typography.labelSmall,
                    color = MaterialTheme.colorScheme.onSurfaceVariant,
                )
                Button(
                    onClick = onStart,
                    enabled = canLookup,
                    modifier = Modifier.fillMaxWidth(),
                    shape = RoundedCornerShape(12.dp),
                ) {
                    Text(stringResource(R.string.pharmacy_lookup_start))
                }
            }
        }
        return
    }

    Surface(
        shape = RoundedCornerShape(14.dp),
        color = MaterialTheme.colorScheme.surfaceContainerHigh,
        modifier = modifier.fillMaxWidth(),
    ) {
        Column(
            modifier = Modifier.padding(12.dp),
            verticalArrangement = Arrangement.spacedBy(6.dp),
        ) {
            Text(
                text = stringResource(R.string.pharmacy_lookup_title),
                style = MaterialTheme.typography.titleSmall,
                fontWeight = FontWeight.Bold,
            )

            val result = state.result
            when {
                state.isLoading -> Row(
                    verticalAlignment = Alignment.CenterVertically,
                    horizontalArrangement = Arrangement.spacedBy(8.dp),
                ) {
                    CircularProgressIndicator(modifier = Modifier.size(18.dp), strokeWidth = 2.dp)
                    Text(
                        text = stringResource(R.string.pharmacy_lookup_loading),
                        style = MaterialTheme.typography.bodySmall,
                    )
                }

                result != null -> {
                    Text(text = result.name, style = MaterialTheme.typography.titleMedium)

                    val details = listOfNotNull(
                        result.company,
                        result.englishName,
                        result.gtin?.let { "GTIN $it" },
                        result.irc?.let { "IRC $it" },
                    ).joinToString(" · ")
                    if (details.isNotBlank()) {
                        Text(
                            text = details,
                            style = MaterialTheme.typography.bodySmall,
                            color = MaterialTheme.colorScheme.onSurfaceVariant,
                        )
                    }

                    result.statusMessage?.takeIf { it.isNotBlank() }?.let { message ->
                        Text(text = message, style = MaterialTheme.typography.labelSmall)
                    }
                    if (result.source == LookupSource.CACHE) {
                        Text(
                            text = stringResource(R.string.pharmacy_lookup_from_cache),
                            style = MaterialTheme.typography.labelSmall,
                            color = MaterialTheme.colorScheme.onSurfaceVariant,
                        )
                    }

                    Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                        Button(onClick = onApply) { Text(applyLabel) }
                        TextButton(onClick = onDismiss) {
                            Text(stringResource(R.string.pharmacy_cancel))
                        }
                    }
                }

                else -> {
                    Text(
                        text = state.error ?: stringResource(R.string.pharmacy_lookup_failed),
                        style = MaterialTheme.typography.bodySmall,
                        color = MaterialTheme.colorScheme.error,
                    )
                    TextButton(onClick = onDismiss) {
                        Text(stringResource(R.string.pharmacy_cancel))
                    }
                }
            }
        }
    }
}
