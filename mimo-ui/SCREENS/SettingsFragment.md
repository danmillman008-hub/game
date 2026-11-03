# صفحه — `SettingsFragment`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.settings.SettingsFragment` |
| نوع | `fragment` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view binding` |
| تعداد لایه‌های متصل | 7 |
| ComposeView | بله |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/settings_activity.xml`](../SOURCE/res/layout/settings_activity.xml) → [dossier](LAYOUTS/layout_settings_activity.md)
- [`res/layout/settings_fragment.xml`](../SOURCE/res/layout/settings_fragment.xml) → [dossier](LAYOUTS/layout_settings_fragment.md)
- [`res/layout/settings_list_item.xml`](../SOURCE/res/layout/settings_list_item.xml) → [dossier](LAYOUTS/layout_settings_list_item.md)
- [`res/layout/settings_list_item_live_preview.xml`](../SOURCE/res/layout/settings_list_item_live_preview.xml) → [dossier](LAYOUTS/layout_settings_list_item_live_preview.md)
- [`res/layout/settings_list_item_radio_group.xml`](../SOURCE/res/layout/settings_list_item_radio_group.xml) → [dossier](LAYOUTS/layout_settings_list_item_radio_group.md)
- [`res/layout/settings_list_item_switcher.xml`](../SOURCE/res/layout/settings_list_item_switcher.xml) → [dossier](LAYOUTS/layout_settings_list_item_switcher.md)
- [`res/layout/settings_user_settings.xml`](../SOURCE/res/layout/settings_user_settings.xml) → [dossier](LAYOUTS/layout_settings_user_settings.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/settings_activity.xml`

```text
└─ androidx.coordinatorlayout.widget.CoordinatorLayout
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_settings
   │  └─ include  #@id/layout_toolbar
   └─ fragment  #@id/fragment_settings
```

### `res/layout/settings_fragment.xml`

```text
└─ ScrollView  #@id/sv_settings
   └─ androidx.constraintlayout.widget.ConstraintLayout
      ├─ View  #@id/settings_fragment_max_container
      ├─ include  #@id/layout_user_settings
      ├─ TextView  #@id/category_1_app
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_settings_content_language
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_settings_appearance
      ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/item_settings_enable_sounds
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_settings_app_icon
      ├─ TextView  #@id/category_2_account
      ├─ com.getmimo.ui.settings.SettingsListItemPremium  #@id/item_settings_upgrade_premium
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_settings_change_password
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_settings_set_goal
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_settings_refresh_subscription
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_settings_delete_account
      ├─ TextView  #@id/category_2_notifications
      ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/item_settings_enable_notifications
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_settings_reminder_time
      ├─ TextView  #@id/category_2_share
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_settings_rate_us
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_follow_us_x
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_like_us_facebook
      ├─ TextView  #@id/category_3_support
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_settings_help
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_settings_terms_and_conditions
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_settings_privacy_policy
      ├─ androidx.compose.ui.platform.ComposeView  #@id/item_settings_create_account
      ├─ androidx.compose.ui.platform.ComposeView  #@id/item_settings_log_in
      ├─ androidx.compose.ui.platform.ComposeView  #@id/item_settings_log_out
      ├─ androidx.constraintlayout.widget.Barrier  #@id/buttons_bottom_barrier
      ├─ TextView  #@id/tv_version_info
      ├─ androidx.constraintlayout.widget.Group  #@id/logged_in_user_views
      └─ androidx.constraintlayout.widget.Group  #@id/anonymous_user_views
```

### `res/layout/settings_list_item.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ View
   ├─ ImageView  #@id/iv_settings_item_icon
   ├─ TextView  #@id/tv_settings_item_title
   └─ TextView  #@id/tv_settings_item_value
```

### `res/layout/settings_list_item_live_preview.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ ImageView  #@id/iv_settings_item_icon
   ├─ TextView  #@id/tv_settings_item_title
   └─ ProgressBar  #@id/pb_settings_list_item
```

### `res/layout/settings_list_item_radio_group.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ ImageView  #@id/iv_settings_item_radio_group_group_icon
   ├─ TextView  #@id/tv_settings_item_radio_group_group_title
   └─ RadioGroup  #@id/tv_settings_item_radio_group_group
```

### `res/layout/settings_list_item_switcher.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_settings_list_item_switcher
   ├─ View
   ├─ ImageView  #@id/iv_settings_item_switcher_icon
   ├─ TextView  #@id/tv_settings_item_switcher_title
   └─ androidx.appcompat.widget.SwitchCompat  #@id/sw_settings_item_switcher
```

### `res/layout/settings_user_settings.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ com.google.android.material.imageview.ShapeableImageView  #@id/iv_settings_profile
   ├─ com.google.android.material.imageview.ShapeableImageView  #@id/iv_settings_profile_edit_avatar
   ├─ TextView  #@id/tv_settings_profile_name_header
   ├─ com.google.android.material.textfield.TextInputLayout  #@id/til_settings_profile_name
   │  └─ com.google.android.material.textfield.TextInputEditText  #@id/et_settings_profile_name
   ├─ TextView  #@id/tv_settings_profile_bio_header
   ├─ com.google.android.material.textfield.TextInputLayout  #@id/til_settings_profile_bio
   │  └─ com.google.android.material.textfield.TextInputEditText  #@id/et_settings_profile_bio
   ├─ TextView  #@id/tv_settings_profile_email_header
   ├─ com.google.android.material.textfield.TextInputLayout  #@id/til_settings_profile_email
   │  └─ com.google.android.material.textfield.TextInputEditText  #@id/et_settings_profile_email
   └─ androidx.constraintlayout.widget.Group  #@id/group_anonymous
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
notifications_settings_dialog_description
notifications_settings_dialog_primary_button
notifications_settings_dialog_secondary_button
notifications_settings_dialog_title
settings
settings_account
settings_app
settings_app_icon
settings_app_icon_change_needs_restart_dialog_cta
settings_app_icon_change_needs_restart_dialog_description
settings_app_icon_change_needs_restart_dialog_title
settings_app_icon_locked
settings_app_icon_subtitle
settings_appearance_dark
settings_appearance_light
settings_appearance_subitle
settings_appearance_system
settings_appearance_title
settings_change_email
settings_change_email_confirm
settings_change_email_current
settings_change_email_dialog_button
settings_change_email_dialog_message
settings_change_email_dialog_title
settings_change_email_error_same
settings_change_email_mismatch
settings_change_email_new
settings_change_email_note
settings_change_email_success
settings_change_password
settings_content_language
settings_content_language_english
settings_content_language_french
settings_content_language_german
settings_content_language_indonesian
settings_content_language_italian
settings_content_language_polish
settings_content_language_portuguese
settings_content_language_russian
settings_content_language_spanish
settings_content_language_turkish
settings_create_account_dialog_message
settings_create_account_dialog_title
settings_delete_account
settings_delete_account_dialog_button
settings_delete_account_dialog_message
settings_delete_account_dialog_title
settings_enable_daily_reminder
settings_enable_sound_effects
settings_follow_us_x
settings_help
settings_language_download_error
settings_liked_us_facebook
settings_log_in_anonymous
settings_log_out
settings_notifications
settings_privacy_policy
settings_rate_us
settings_refresh_purchases
settings_refresh_purchases_dropdown
settings_refresh_purchases_error
settings_reminder_time
settings_set_goal
settings_share
settings_support
settings_terms_and_conditions
settings_upgrade_to_pro
settings_user_about_you
settings_user_about_you_hint
settings_user_display_name
settings_user_email
settings_version_info_prefix
```

## ۴. رنگ‌های مرتبط (فهرست کامل)

(none)

## ۵. دایمنشن‌های مرتبط (فهرست کامل)

(none)

## ۶. استایل‌های مرتبط (فهرست کامل)

(none)

## ۷. شواهد حالت‌ها (رشته‌های منبع)

```text
settings_app_icon_locked
settings_change_email_error_same
settings_language_download_error
settings_refresh_purchases_error
settings_upgrade_to_pro
```

## ۸. ناوبری / deep link

(هیچ intent-filter/data برای این سطح اعلان نشده)
