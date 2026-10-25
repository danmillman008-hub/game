package ir.darookhaneh.stock.feature.settings.presentation.model

/**
 * گروه‌بندی آیتم‌های تنظیمات.
 * بخش اعلان‌ها و پشتیبان‌گیری پس از آماده شدن مدل دارویی برمی‌گردد.
 */
object SettingItems {

    val MainScreenSection1 = listOf(
        SettingClickableUiModel.APPEARANCE,
        SettingClickableUiModel.OTHER_SETTING,
    )

    val MainScreenSection2 = listOf(
        SettingClickableUiModel.NEW_FEATURES,
        SettingClickableUiModel.ABOUT,
        SettingClickableUiModel.DEBUG,
    )

    val AboutScreen = listOf(
        SettingClickableUiModel.PRIVACY_POLICY,
        SettingClickableUiModel.COPYRIGHT,
        SettingClickableUiModel.CHECK_UPDATE,
        SettingClickableUiModel.OPEN_SOURCE
    )
}
