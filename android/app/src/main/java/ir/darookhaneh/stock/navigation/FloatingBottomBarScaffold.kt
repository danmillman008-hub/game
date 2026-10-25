package ir.darookhaneh.stock.navigation

import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.animation.slideInVertically
import androidx.compose.animation.slideOutVertically
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.navigationBarsPadding
import androidx.compose.foundation.layout.padding
import androidx.compose.runtime.Composable
import androidx.compose.runtime.CompositionLocalProvider
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import ir.darookhaneh.stock.core.designsystem.tokens.BottomBarReservedHeight
import ir.darookhaneh.stock.core.designsystem.tokens.LocalBottomBarInset

/**
 * چیدمان پایهٔ اپ: محتوا + نوار پایین شناور.
 *
 * نکتهٔ مهم (رفع باگ ۲.۰.۰): محتوا **بیرون از محدودهٔ نوار** قرار می‌گیرد
 * (`padding(bottom = …)`) و مقدار همان فاصله با [LocalBottomBarInset] به صفحه‌ها می‌رسد.
 * قبلاً نوار روی محتوا شناور بود و دکمه‌های پایین صفحه را می‌پوشاند.
 */
@Composable
fun FloatingBottomBarScaffold(
    modifier: Modifier = Modifier,
    bottomBarVisible: Boolean = true,
    bottomBar: @Composable () -> Unit,
    content: @Composable () -> Unit,
) {
    val reserved = if (bottomBarVisible) BottomBarReservedHeight else 0.dp
    CompositionLocalProvider(LocalBottomBarInset provides reserved) {
        Box(modifier = modifier.fillMaxSize()) {
            Box(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(bottom = reserved)
            ) {
                content()
            }

            AnimatedVisibility(
                visible = bottomBarVisible,
                modifier = Modifier
                    .align(Alignment.BottomCenter)
                    .navigationBarsPadding()
                    .padding(start = 16.dp, end = 16.dp, bottom = 16.dp),
                enter = fadeIn() + slideInVertically { it / 2 },
                exit = fadeOut() + slideOutVertically { it / 2 },
            ) {
                bottomBar()
            }
        }
    }
}
