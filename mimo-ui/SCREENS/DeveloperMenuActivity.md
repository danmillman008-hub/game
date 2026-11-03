# صفحه — `DeveloperMenuActivity`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.developermenu.DeveloperMenuActivity` |
| نوع | `activity` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `@style/MaterialDarkModeTheme` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose (unresolved per screen)` |
| تعداد لایه‌های متصل | 6 |
| ComposeView | بله |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/developer_menu_campaign_activity.xml`](../SOURCE/res/layout/developer_menu_campaign_activity.xml) → [dossier](LAYOUTS/layout_developer_menu_campaign_activity.md)
- [`res/layout/developer_menu_content_experiment_activity.xml`](../SOURCE/res/layout/developer_menu_content_experiment_activity.xml) → [dossier](LAYOUTS/layout_developer_menu_content_experiment_activity.md)
- [`res/layout/developer_menu_discount_activity.xml`](../SOURCE/res/layout/developer_menu_discount_activity.xml) → [dossier](LAYOUTS/layout_developer_menu_discount_activity.md)
- [`res/layout/developer_menu_remote_config_activity.xml`](../SOURCE/res/layout/developer_menu_remote_config_activity.xml) → [dossier](LAYOUTS/layout_developer_menu_remote_config_activity.md)
- [`res/layout/developer_menu_remote_config_item.xml`](../SOURCE/res/layout/developer_menu_remote_config_item.xml) → [dossier](LAYOUTS/layout_developer_menu_remote_config_item.md)
- [`res/layout/developermenu_activity.xml`](../SOURCE/res/layout/developermenu_activity.xml) → [dossier](LAYOUTS/layout_developermenu_activity.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/developer_menu_campaign_activity.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_abtest__config
   │  └─ include  #@id/layout_toolbar
   └─ ScrollView
      └─ androidx.constraintlayout.widget.ConstraintLayout
         ├─ TextView  #@id/tv_dev_menu_campaign
         ├─ TextView  #@id/tv_dev_menu_campaign_parameter
         ├─ TextView  #@id/tv_dev_menu_campaign_value
         ├─ com.getmimo.ui.settings.SettingsListItemRadioGroup  #@id/rg_dev_menu_campaign
         ├─ TextView  #@id/tv_dev_menu_campaign_allows_free_trial
         ├─ TextView  #@id/tv_dev_menu_campaign_allows_free_trial_value
         └─ com.getmimo.ui.settings.SettingsListItemRadioGroup  #@id/rg_dev_menu_campaign_allows_free_trial
```

### `res/layout/developer_menu_content_experiment_activity.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ include  #@id/layout_toolbar
   ├─ CheckBox  #@id/cb_override_content_experiment
   ├─ TextView  #@id/tv_content_experiment_label
   ├─ EditText  #@id/et_content_experiment_content
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_use_template
```

### `res/layout/developer_menu_discount_activity.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_discount_config
   │  └─ include  #@id/layout_toolbar
   └─ ScrollView  #@id/sv_developermenu_discount
      └─ LinearLayout
         ├─ TextView  #@id/tv_smart_discount_chapter_completed
         ├─ TextView  #@id/tv_smart_discount
         ├─ TextView  #@id/tv_discount_theme
         ├─ com.getmimo.ui.settings.SettingsListItemRadioGroup  #@id/rg_override_subscription_reactivate_discount
         ├─ TextView  #@id/tv_external_subscription
         ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/item_developer_menu_fake_remote_discount
         ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/item_developer_menu_fake_remote_discount_image
         ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/item_developer_menu_force_last_call_discount
         ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_reset_smart_discount
         └─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_smart_discount_send_push_notification
```

### `res/layout/developer_menu_remote_config_activity.xml`

```text
└─ androidx.coordinatorlayout.widget.CoordinatorLayout
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_developermenu
   │  └─ include  #@id/layout_toolbar
   └─ androidx.constraintlayout.widget.ConstraintLayout
      ├─ EditText  #@id/et_remote_config_id
      ├─ EditText  #@id/et_remote_config_value
      ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_remote_config_add
      └─ androidx.recyclerview.widget.RecyclerView  #@id/rv_remote_config
```

### `res/layout/developer_menu_remote_config_item.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ ImageView  #@id/iv_remove
   ├─ TextView  #@id/tv_item_id
   └─ TextView  #@id/tv_item_value
```

### `res/layout/developermenu_activity.xml`

```text
└─ androidx.coordinatorlayout.widget.CoordinatorLayout  #@id/developer_menu_root
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_developermenu
   │  └─ include  #@id/layout_toolbar
   └─ fragment  #@id/fragment_developermenu
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
developer_menu_ab_test
developer_menu_add_test_reward
developer_menu_anniversary_upsell_flow_example
developer_menu_awesome_mode
developer_menu_awesome_mode_instructions
developer_menu_awesome_mode_title
developer_menu_campaign
developer_menu_campaign_allows_free_trial
developer_menu_campaign_parameter
developer_menu_campaign_user_coming_from_campaign
developer_menu_category_content
developer_menu_category_live_deployment_download
developer_menu_category_live_deployment_use_unpublished
developer_menu_category_mock_data
developer_menu_category_previews
developer_menu_clear_image_cache
developer_menu_content_experiment
developer_menu_content_experiment_label
developer_menu_content_experiment_override
developer_menu_content_experiment_use_template
developer_menu_crash_app
developer_menu_create_test_reward
developer_menu_disable_leak_canary
developer_menu_disable_override_coming_from_campaign
developer_menu_disable_override_motive_variant
developer_menu_disable_pro
developer_menu_discount
developer_menu_discount_chapter_completed
developer_menu_discount_current_discount
developer_menu_discount_current_subscription
developer_menu_discount_fake_remote_discount
developer_menu_discount_fake_remote_discount_image
developer_menu_discount_force_last_call_discount
developer_menu_discount_local_discount_theme
developer_menu_discount_override_subscription
developer_menu_discount_reset_local_discount
developer_menu_discount_send_push_notification
developer_menu_enable_preload_images
developer_menu_fake_leaderboards_result
developer_menu_fake_subscription
developer_menu_force_chapter_end_progress_eta_enabled
developer_menu_force_path_overview_eta_enabled
developer_menu_force_reactivation_prompt_on_app_launch
developer_menu_god_mode
developer_menu_god_mode_toast
developer_menu_inapp_messaging_token
developer_menu_lessons_variation_track
developer_menu_max_upsell_flow_example
developer_menu_override_remote_config
developer_menu_override_remote_config_add
developer_menu_override_remote_config_hint_id
developer_menu_override_remote_config_hint_value
developer_menu_override_remote_config_id
developer_menu_override_remote_config_value
developer_menu_preview_live_content_failure_title
developer_menu_preview_live_content_file_not_found
developer_menu_preview_live_content_success_description
developer_menu_preview_live_content_success_title
developer_menu_pro_upsell_flow_example
developer_menu_push_notification_token
developer_menu_refresh_firebase_remote
developer_menu_reset_push_token
developer_menu_reset_reactivation_flow
developer_menu_reset_user_messages_counter
developer_menu_send_lesson_progress_when_swiping
developer_menu_use_mocked_trial_reminder_dates
developer_menu_use_test_server
```

## ۴. رنگ‌های مرتبط (فهرست کامل)

(none)

## ۵. دایمنشن‌های مرتبط (فهرست کامل)

```text
developer_menu_item_height
```

## ۶. استایل‌های مرتبط (فهرست کامل)

(none)

## ۷. شواهد حالت‌ها (رشته‌های منبع)

(none)

## ۸. ناوبری / deep link

(هیچ intent-filter/data برای این سطح اعلان نشده)
