package ir.darookhaneh.stock.navigation

import androidx.compose.animation.AnimatedVisibility
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.animation.slideInVertically
import androidx.compose.animation.slideOutVertically
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.WindowInsets
import androidx.compose.foundation.layout.asPaddingValues
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.imePadding
import androidx.compose.foundation.layout.navigationBars
import androidx.compose.foundation.layout.navigationBarsPadding
import androidx.compose.foundation.layout.padding
import androidx.compose.runtime.Composable
import androidx.compose.runtime.CompositionLocalProvider
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.remember
import androidx.compose.runtime.setValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.layout.onSizeChanged
import androidx.compose.ui.platform.LocalDensity
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp
import ir.darookhaneh.stock.core.designsystem.tokens.BottomBarReservedHeight
import ir.darookhaneh.stock.core.designsystem.tokens.LocalBottomBarInset

/**
 * چیدمان پایهٔ اپ: محتوا + نوار پایین شناور.
 *
 * **چرا اندازه‌گیری واقعی (نسخهٔ ۲.۱.۱):** مقدار ثابت ۹۶dp برای نوار کافی نبود؛
 * ارتفاع نوار = ارتفاع داخلی + حاشیهٔ ۱۶dp بالا/پایین + ارتفاع نوار ناوبری سیستم.
 * روی گوشی‌های با ناوبری سه‌دکمه‌ای و با فونت بزرگ (وزیرمتن + fontScale) نوار
 * بلندتر می‌شد و روی دکمه‌های پایین صفحه (مثل «ثبت دارو») می‌افتاد و کلیک را
 * می‌گرفت. اکنون ارتفاع واقعی نوار با [onSizeChanged] اندازه‌گیری و همان مقدار
 * از محتوا کنار گذاشته می‌شود؛ پس هرگز همپوشانی رخ نمی‌دهد.
 *
 * [LocalBottomBarInset] عمداً صفر است: فاصله یک‌بار و در همین‌جا از محتوا گرفته
 * می‌شود؛ صفحه‌ها نباید دوباره اضافه کنند (قبلاً دوبار اضافه می‌شد و فضای خالی
 * عجیب می‌ساخت).
 */
@Composable
fun FloatingBottomBarScaffold(
    modifier: Modifier = Modifier,
    bottomBarVisible: Boolean = true,
    bottomBar: @Composable () -> Unit,
    content: @Composable () -> Unit,
) {
    val density = LocalDensity.current
    val navigationBarBottom: Dp = WindowInsets.navigationBars
        .asPaddingValues()
        .calculateBottomPadding()

    var barHeightPx by remember { mutableStateOf(0) }

    val measuredBarHeight = with(density) { barHeightPx.toDp() }
    // حاشیهٔ بالای نوار هم باید کنار گذاشته شود؛ پایین‌تر از نوار ناوبری سیستم
    // می‌نشیند و آن هم ارتفاع واقعی گرفته‌شده است.
    val reserved: Dp = if (bottomBarVisible && barHeightPx > 0) {
        maxOf(BottomBarReservedHeight, measuredBarHeight + navigationBarBottom + 8.dp)
    } else {
        0.dp
    }

    CompositionLocalProvider(LocalBottomBarInset provides 0.dp) {
        Box(modifier = modifier.fillMaxSize()) {
            Box(
                modifier = Modifier
                    .fillMaxSize()
                    // صفحه‌کلید مجازی: بدون این، دکمهٔ پایین فرم‌ها زیر کیبورد می‌ماند
                    // و کاربر فکر می‌کند «دکمه کار نمی‌کند».
                    .imePadding()
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
                Box(modifier = Modifier.onSizeChanged { barHeightPx = it.height }) {
                    bottomBar()
                }
            }
        }
    }
}
