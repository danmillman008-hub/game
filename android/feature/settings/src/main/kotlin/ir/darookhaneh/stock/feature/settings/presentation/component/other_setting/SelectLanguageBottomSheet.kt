package ir.darookhaneh.stock.feature.settings.presentation.component.other_setting

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.itemsIndexed
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import ir.darookhaneh.stock.capitalize
import ir.darookhaneh.stock.core.designsystem.component.AppBottomSheet
import ir.darookhaneh.stock.core.model.setting.AppLanguage
import ir.darookhaneh.stock.core.presentation.R
import ir.darookhaneh.stock.core.presentation.utils.toItemPosition
import ir.darookhaneh.stock.core.presentation.utils.toVerticalSegmentedShape

@Composable
fun SelectLanguageBottomSheet(
    currentLanguage: AppLanguage = AppLanguage.ENGLISH,
    onLanguageSelect: (AppLanguage) -> Unit,
    onDismiss: () -> Unit
) {
    AppBottomSheet(
        modifier = Modifier.padding(16.dp),
        onDismiss = onDismiss
    ) {
        LazyColumn(
            modifier = Modifier.fillMaxWidth(),
            verticalArrangement = Arrangement.spacedBy(4.dp),
            contentPadding = PaddingValues(16.dp)
        ) {
            item {
                Text(
                    text = stringResource(R.string.setting_language_title),
                    style = MaterialTheme.typography.titleMedium.copy(
                        fontWeight = FontWeight.Black
                    )
                )
            }

            item { Spacer(modifier = Modifier.height(16.dp)) }

            itemsIndexed(
                items = AppLanguage.entries,
                key = { _: Int, item: AppLanguage -> item.name },
            ) { index: Int, language: AppLanguage ->
                val itemPosition = index.toItemPosition(AppLanguage.entries.size)
                Surface(
                    modifier = Modifier.fillMaxWidth(),
                    color = if (language == currentLanguage) MaterialTheme.colorScheme.primary
                    else MaterialTheme.colorScheme.surfaceContainerHigh,
                    contentColor = if (language == currentLanguage) MaterialTheme.colorScheme.onPrimary
                    else MaterialTheme.colorScheme.onSurface,
                    shape = itemPosition.toVerticalSegmentedShape(),
                    onClick = { onLanguageSelect(language) },
                ) {
                    Text(
                        modifier = Modifier.padding(16.dp),
                        text = language.name.capitalize(),
                        style = MaterialTheme.typography.bodyMedium.copy(
                            fontWeight = FontWeight.Medium
                        )
                    )
                }
            }
        }
    }
}