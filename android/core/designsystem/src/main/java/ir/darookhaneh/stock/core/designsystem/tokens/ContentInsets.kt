package ir.darookhaneh.stock.core.designsystem.tokens

import androidx.compose.runtime.staticCompositionLocalOf
import androidx.compose.ui.unit.Dp
import androidx.compose.ui.unit.dp

/**
 * فاصلهٔ پایینی که محتوای هر صفحه باید رعایت کند تا زیر «نوار پایین شناور» نرود.
 *
 * چرا CompositionLocal: نوار پایین در لایهٔ اپ رندر می‌شود ولی صفحه‌ها در ماژول‌های
 * feature هستند؛ این مقدار تنها راه بدون وابستگی معکوس است.
 *
 * باگ نسخهٔ ۲.۰.۰: مقدار ۰ بود و محتوا در یک `Box` می‌نشست، پس دکمه‌های پایین صفحه
 * (از جمله FAB «ثبت دارو») زیر نوار می‌رفتند و کلیک نمی‌شدند.
 */
val LocalBottomBarInset = staticCompositionLocalOf<Dp> { 0.dp }

/** ارتفاع واقعی نوار شناور + حاشیهٔ آن. منبع واحد برای هر دو طرف. */
val BottomBarReservedHeight: Dp = 96.dp
