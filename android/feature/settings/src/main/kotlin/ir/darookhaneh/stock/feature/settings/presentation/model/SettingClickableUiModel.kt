package ir.darookhaneh.stock.feature.settings.presentation.model

import androidx.annotation.StringRes
import androidx.compose.runtime.Stable
import ir.darookhaneh.stock.core.designsystem.icon.StockIcons
import ir.darookhaneh.stock.core.designsystem.icon.IconProvider
import ir.darookhaneh.stock.core.presentation.R

@Stable
enum class SettingClickableUiModel(
    @param:StringRes val title: Int,
    @param:StringRes val description: Int,
    val icon: IconProvider,
) {
    APPEARANCE(
        title = R.string.appearance_title,
        description = R.string.appearance_subtitle,
        icon = StockIcons.Settings.Appearance
    ),

    NOTIFICATION(
        title = R.string.notification_settings_title,
        description = R.string.notification_settings_subtitle,
        icon = StockIcons.Settings.Notifications
    ),

    YOUR_DATA(
        title = R.string.your_data_title,
        description = R.string.your_data_subtitle,
        icon = StockIcons.Settings.YourData
    ),

    OTHER_SETTING(
        title = R.string.other_settings_title_page,
        description = R.string.other_settings_subtitle,
        icon = StockIcons.Settings.OtherSetting
    ),

    ABOUT(
        title = R.string.setting_about_app,
        description = R.string.setting_about_app_desc,
        icon = StockIcons.Settings.AboutApp
    ),

    DEBUG(
        title = R.string.setting_widget_debug,
        description = R.string.setting_widget_debug_desc,
        icon = StockIcons.Settings.WidgetDebug
    ),

    DAILY_REMINDER(
        title = R.string.setting_daily_reminder,
        description = R.string.setting_daily_reminder_desc,
        icon = StockIcons.Settings.Notifications
    ),

    EXPORT(
        title = R.string.setting_export,
        description = R.string.setting_export_desc,
        icon = StockIcons.Settings.ExportData
    ),

    IMPORT(
        title = R.string.setting_import,
        description = R.string.setting_import_desc,
        icon = StockIcons.Settings.ImportData
    ),

    LANGUAGE(
        title = R.string.setting_language_title,
        description = R.string.setting_language_desc,
        icon = StockIcons.Settings.Language
    ),

    DELETE_ALL(
        title = R.string.setting_clear_data,
        description = R.string.setting_clear_data_desc,
        icon = StockIcons.Settings.DeleteAll
    ),

    NEW_FEATURES(
        title = R.string.setting_new_features,
        description = R.string.setting_new_features_desc,
        icon = StockIcons.Settings.NewFeature
    ),

    COPYRIGHT(
        title = R.string.setting_license,
        description = R.string.setting_license_desc,
        icon = StockIcons.Settings.License
    ),

    FEEDBACK(
        title = R.string.setting_feedback,
        description = R.string.setting_feedback_desc,
        icon = StockIcons.Settings.Feedback
    ),

    PRIVACY_POLICY(
        title = R.string.setting_privacy_policy,
        description = R.string.setting_privacy_policy_desc,
        icon = StockIcons.Settings.PrivatePolicy
    ),

    OPEN_SOURCE(
        title = R.string.setting_open_source,
        description = R.string.setting_open_source_desc,
        icon = StockIcons.Settings.OpenSource
    ),

    CHECK_UPDATE(
        title = R.string.setting_check_update_title,
        description = R.string.setting_check_update_desc,
        icon = StockIcons.Settings.CheckUpdate
    )
}
