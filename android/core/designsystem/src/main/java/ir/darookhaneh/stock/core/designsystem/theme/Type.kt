package ir.darookhaneh.stock.core.designsystem.theme

import androidx.compose.material3.Typography
import androidx.compose.ui.text.ExperimentalTextApi
import androidx.compose.ui.text.font.Font
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.text.font.FontVariation
import androidx.compose.ui.text.font.FontWeight
import ir.darookhaneh.stock.core.designsystem.R

/**
 * Google Sans Flex
 *
 * The font is a variable font, so we can control:
 *
 * - Weight (wght)
 * - Width (wdth)
 * - Roundness (ROND)
 *
 * These axes allow the typography to feel more expressive
 * without needing multiple font files.
 */

@OptIn(ExperimentalTextApi::class)
private val GoogleSansFlexFontFamily = FontFamily(

    // 400 - Regular
    Font(
        resId = R.font.google_sans_flex_font,
        weight = FontWeight.Normal,
        variationSettings = FontVariation.Settings(
            FontVariation.weight(400),
            FontVariation.width(100f),
            FontVariation.Setting("ROND", 20f),
        ),
    ),

    // 500 - Medium
    Font(
        resId = R.font.google_sans_flex_font,
        weight = FontWeight.Medium,
        variationSettings = FontVariation.Settings(
            FontVariation.weight(500),
            FontVariation.width(102.5f),
            FontVariation.Setting("ROND", 35f),
        ),
    ),

    // 600 - SemiBold
    Font(
        resId = R.font.google_sans_flex_font,
        weight = FontWeight.SemiBold,
        variationSettings = FontVariation.Settings(
            FontVariation.weight(600),
            FontVariation.width(105f),
            FontVariation.Setting("ROND", 50f),
        ),
    ),

    // 700 - Bold
    Font(
        resId = R.font.google_sans_flex_font,
        weight = FontWeight.Bold,
        variationSettings = FontVariation.Settings(
            FontVariation.weight(700),
            FontVariation.width(105f),
            FontVariation.Setting("ROND", 50f),
        ),
    ),
)

/**
 * فونت اصلی محصول: وزیرمتن.
 * برای متن فارسی/عربی تنها این خانواده استفاده می‌شود تا شکل حروف و اعداد درست بماند.
 */
private val VazirmatnFontFamily = FontFamily(
    Font(resId = R.font.vazirmatn, weight = FontWeight.Normal),
    Font(resId = R.font.vazirmatn, weight = FontWeight.Medium),
    Font(resId = R.font.vazirmatn, weight = FontWeight.SemiBold),
    Font(resId = R.font.vazirmatn, weight = FontWeight.Bold),
)

fun getTypographyForFont(): Typography {

    val defaultTypography = Typography()

    return defaultTypography.copy(
        // وزیرمتن به عنوان فونت پایهٔ همهٔ استایل‌ها
    

        // -----------------------------------------------------------------
        // Display
        // -----------------------------------------------------------------

        displayLarge = defaultTypography.displayLarge.copy(
            fontFamily = VazirmatnFontFamily,
        ),

        displayMedium = defaultTypography.displayMedium.copy(
            fontFamily = VazirmatnFontFamily,
        ),

        displaySmall = defaultTypography.displaySmall.copy(
            fontFamily = VazirmatnFontFamily,
        ),

        // -----------------------------------------------------------------
        // Headline
        // -----------------------------------------------------------------

        headlineLarge = defaultTypography.headlineLarge.copy(
            fontFamily = VazirmatnFontFamily,
        ),

        headlineMedium = defaultTypography.headlineMedium.copy(
            fontFamily = VazirmatnFontFamily,
        ),

        headlineSmall = defaultTypography.headlineSmall.copy(
            fontFamily = VazirmatnFontFamily,
        ),

        // -----------------------------------------------------------------
        // Title
        // -----------------------------------------------------------------

        titleLarge = defaultTypography.titleLarge.copy(
            fontFamily = VazirmatnFontFamily,
        ),

        titleMedium = defaultTypography.titleMedium.copy(
            fontFamily = VazirmatnFontFamily,
        ),

        titleSmall = defaultTypography.titleSmall.copy(
            fontFamily = VazirmatnFontFamily,
        ),

        // -----------------------------------------------------------------
        // Body
        // -----------------------------------------------------------------

        bodyLarge = defaultTypography.bodyLarge.copy(
            fontFamily = VazirmatnFontFamily,
        ),

        bodyMedium = defaultTypography.bodyMedium.copy(
            fontFamily = VazirmatnFontFamily,
        ),

        bodySmall = defaultTypography.bodySmall.copy(
            fontFamily = VazirmatnFontFamily,
        ),

        labelLarge = defaultTypography.labelLarge.copy(
            fontFamily = VazirmatnFontFamily,
        ),

        labelMedium = defaultTypography.labelMedium.copy(
            fontFamily = VazirmatnFontFamily,
        ),

        labelSmall = defaultTypography.labelSmall.copy(
            fontFamily = VazirmatnFontFamily,
        ),
    )
}