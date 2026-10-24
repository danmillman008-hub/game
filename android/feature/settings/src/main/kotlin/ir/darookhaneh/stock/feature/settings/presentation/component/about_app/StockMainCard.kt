package ir.darookhaneh.stock.feature.settings.presentation.component.about_app

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Row
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxHeight
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.layout.width
import androidx.compose.material3.Card
import androidx.compose.material3.CardDefaults
import androidx.compose.material3.ExperimentalMaterial3ExpressiveApi
import androidx.compose.material3.FilledTonalIconButton
import androidx.compose.material3.IconButtonDefaults
import androidx.compose.material3.MaterialShapes
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.material3.toShape
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import ir.darookhaneh.stock.core.designsystem.icon.StockIcons
import ir.darookhaneh.stock.core.designsystem.icon.AppIcon
import ir.darookhaneh.stock.core.presentation.R
import ir.darookhaneh.stock.core.presentation.utils.ItemPosition
import ir.darookhaneh.stock.core.presentation.utils.toVerticalSegmentedShape

@Composable
fun StockMainContent(
    modifier: Modifier,
    itemPosition: ItemPosition,
    appVersion: String,
    onGithubClick: () -> Unit,
    onDiscordClick: () -> Unit,
) {
    Card(
        modifier = modifier,
        shape = itemPosition.toVerticalSegmentedShape(),
        colors = CardDefaults.cardColors(
            containerColor = MaterialTheme.colorScheme.surfaceContainerHighest,
            contentColor = MaterialTheme.colorScheme.onSurface
        )
    ) {
        StockMainContent(
            modifier = Modifier
                .fillMaxSize()
                .padding(16.dp),
            appVersion = appVersion,
            onGithubClick = onGithubClick,
            onDiscordClick = onDiscordClick
        )
    }
}

@OptIn(ExperimentalMaterial3ExpressiveApi::class)
@Composable
fun StockMainContent(
    modifier: Modifier = Modifier,
    appVersion: String,
    onGithubClick: () -> Unit,
    onDiscordClick: () -> Unit = {},
) {
    Row(
        modifier = modifier,
        verticalAlignment = Alignment.CenterVertically
    ) {
        Box(
            modifier = Modifier
                .size(64.dp)
                .background(
                    color = MaterialTheme.colorScheme.primary,
                    shape = MaterialShapes.Cookie12Sided.toShape()
                ),
            contentAlignment = Alignment.Center
        ) {
            AppIcon(
                iconProvider = StockIcons.Settings.Stock,
                tint = MaterialTheme.colorScheme.primaryContainer,
                modifier = Modifier.size(32.dp)
            )
        }

        Spacer(modifier = Modifier.width(16.dp))

        TextContent(
            modifier = Modifier.weight(1f),
            title = stringResource(R.string.app_name),
            content = appVersion
        )

        TrailingContent(
            modifier = Modifier.fillMaxHeight(),
            onGithubClick = onGithubClick,
            onDiscordClick = onDiscordClick
        )

    }
}

@Composable
private fun TextContent(
    modifier: Modifier = Modifier,
    title: String,
    content: String
) {
    Column(
        modifier = modifier,
        verticalArrangement = Arrangement.Center,
    ) {
        Text(
            text = title,
            style = MaterialTheme.typography.headlineSmall,
            fontWeight = FontWeight.SemiBold,
            color = MaterialTheme.colorScheme.onSurface
        )

        Spacer(modifier = Modifier.height(4.dp))

        Text(
            text = content,
            style = MaterialTheme.typography.bodyLarge,
            fontWeight = FontWeight.Medium,
            color = MaterialTheme.colorScheme.primary
        )
    }

}

@Composable
private fun TrailingContent(
    modifier: Modifier,
    onGithubClick: () -> Unit,
    onDiscordClick: () -> Unit = {}
) {
    Row(
        modifier = modifier,
        verticalAlignment = Alignment.CenterVertically,
        horizontalArrangement = Arrangement.spacedBy(8.dp)
    ) {
        FilledTonalIconButton(
            onClick = onGithubClick,
            colors = IconButtonDefaults.iconButtonColors(
                containerColor = MaterialTheme.colorScheme.secondary,
                contentColor = MaterialTheme.colorScheme.onSecondary
            )
        ) {
            AppIcon(
                iconProvider = StockIcons.Settings.Github,
                modifier = Modifier.size(20.dp)
            )
        }
    }
}

