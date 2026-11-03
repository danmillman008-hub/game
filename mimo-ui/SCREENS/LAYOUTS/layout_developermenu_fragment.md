# پروندهٔ لایه — `res/layout/developermenu_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/developermenu_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/developermenu_fragment.xml`](../../SOURCE/res/layout/developermenu_fragment.xml) |
| SHA-256 دیکد | `72364dda640413a1b581db1d050c361f35d8699cbeff2d0e0ae6a98de1f9e428` |
| ریشه | `ScrollView` |
| تعداد گره | 58 |
| تعداد شناسه | 53 |
| تگ‌های استفاده‌شده | 8 |
| ویوهای سفارشی `com.getmimo` | 3 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 107 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ ScrollView  #@id/sv_developermenu
   └─ LinearLayout  #@id/settings_fragment_max_container
      ├─ TextView
      ├─ View
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_ab_test
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_content_experiment
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_firebase_remote_config_override
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_remote_config_refresh
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_campaign
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_discount
      ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/item_developer_menu_disable_premium
      ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/item_developer_menu_use_test_server
      ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/item_developer_menu_preload_images
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_clear_image_cache
      ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/item_developer_menu_god_mode
      ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/item_developer_menu_send_lesson_progress_when_swiping
      ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/item_developer_menu_force_reactivation_prompt_on_app_launch
      ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/item_developer_menu_force_path_overview_eta_enabled
      ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/item_developer_menu_force_chapter_end_progress_eta_enabled
      ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/item_developer_menu_disable_leak_canary
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_reset_push_token
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_reset_global_share_prefs
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_reset_user_properties
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_reset_dev_menu_options
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_reset_user_messages_counter
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_reset_reactivation_flow
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_crash_app
      ├─ LinearLayout  #@id/section_learning_companions
      │  ├─ TextView
      │  ├─ View
      │  ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_companions_restart
      │  ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_companions_advance
      │  └─ com.getmimo.ui.settings.SettingsListItem  #@id/item_companions_intro
      ├─ TextView  #@id/category_previews
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_preview_console
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_modal_dialog_test
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_max_upsell_flow_example
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_pro_upsell_flow_example
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_anniversary_upsell_flow_example
      ├─ TextView  #@id/category_mock_data
      ├─ View
      ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/item_developer_menu_use_mocked_trial_reminder_dates
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_add_test_reward
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_fake_leaderboards_result
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_fake_streak_data
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_fake_subscription
      ├─ TextView  #@id/category_live_publishing
      ├─ View  #@id/separator_settings_3
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_search_tracks
      ├─ com.getmimo.ui.settings.SettingsListLivePreview  #@id/item_developer_menu_download
      ├─ com.getmimo.ui.settings.SettingsListSwitchItem  #@id/item_developer_menu_use_unpublished
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_menu_awesome_mode
      ├─ com.getmimo.ui.settings.SettingsListItem  #@id/item_developer_lessons_variations_chapter
      ├─ TextView  #@id/tv_push_notification_token
      ├─ TextView  #@id/tv_in_app_messaging_token
      ├─ TextView  #@id/tv_authentication_method_info
      ├─ TextView  #@id/tv_version_info
      └─ androidx.compose.ui.platform.ComposeView  #@id/cv_tutorial_dialog
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `ScrollView` | `android:orientation` | `vertical` |
| 2 | `ScrollView` | `android:id` | `@id/sv_developermenu` |
| 3 | `ScrollView` | `android:layout_width` | `match_parent` |
| 4 | `ScrollView` | `android:layout_height` | `match_parent` |
| 5 | `ScrollView` | `android:fillViewport` | `true` |
| 6 | `LinearLayout` | `android:orientation` | `vertical` |
| 7 | `LinearLayout` | `android:id` | `@id/settings_fragment_max_container` |
| 8 | `LinearLayout` | `android:paddingBottom` | `24.000000dip` |
| 9 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 10 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 11 | `LinearLayout` | `android:maxWidth` | `@dimen/general_max_width` |
| 12 | `TextView` | `android:layout_width` | `wrap_content` |
| 13 | `TextView` | `android:layout_height` | `wrap_content` |
| 14 | `TextView` | `android:layout_marginTop` | `16.000000dip` |
| 15 | `TextView` | `android:text` | `General` |
| 16 | `TextView` | `android:paddingStart` | `16.000000dip` |
| 17 | `TextView` | `android:paddingEnd` | `16.000000dip` |
| 18 | `TextView` | `style` | `@style/TextP3` |
| 19 | `View` | `android:background` | `@color/line_primary` |
| 20 | `View` | `android:layout_width` | `wrap_content` |
| 21 | `View` | `android:layout_height` | `1.000000dip` |
| 22 | `View` | `android:layout_marginTop` | `12.000000dip` |
| 23 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_ab_test` |
| 24 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 25 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 26 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_chapter_type_experiment` |
| 27 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/developer_menu_ab_test` |
| 28 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_content_experiment` |
| 29 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 30 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 31 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_chapter_type_experiment` |
| 32 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/developer_menu_content_experiment` |
| 33 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_firebase_remote_config_override` |
| 34 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 35 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 36 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_code` |
| 37 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/developer_menu_override_remote_config` |
| 38 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_remote_config_refresh` |
| 39 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 40 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 41 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_refresh_cw` |
| 42 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/developer_menu_refresh_firebase_remote` |
| 43 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_campaign` |
| 44 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 45 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 46 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_star` |
| 47 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/developer_menu_campaign` |
| 48 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_discount` |
| 49 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 50 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 51 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_chapter_type_experiment` |
| 52 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/developer_menu_discount` |
| 53 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:id` | `@id/item_developer_menu_disable_premium` |
| 54 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_width` | `match_parent` |
| 55 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_height` | `wrap_content` |
| 56 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_icon` | `@drawable/ic_star` |
| 57 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_label` | `@string/developer_menu_disable_pro` |
| 58 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:id` | `@id/item_developer_menu_use_test_server` |
| 59 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_width` | `match_parent` |
| 60 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_height` | `wrap_content` |
| 61 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_icon` | `@drawable/ic_code` |
| 62 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_label` | `@string/developer_menu_use_test_server` |
| 63 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:id` | `@id/item_developer_menu_preload_images` |
| 64 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_width` | `match_parent` |
| 65 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_height` | `wrap_content` |
| 66 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_icon` | `@drawable/ic_download` |
| 67 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_label` | `@string/developer_menu_enable_preload_images` |
| 68 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_clear_image_cache` |
| 69 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 70 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 71 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_close_circle_filled` |
| 72 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/developer_menu_clear_image_cache` |
| 73 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:id` | `@id/item_developer_menu_god_mode` |
| 74 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_width` | `match_parent` |
| 75 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_height` | `wrap_content` |
| 76 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_icon` | `@drawable/ic_challenge` |
| 77 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_label` | `@string/developer_menu_god_mode` |
| 78 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:id` | `@id/item_developer_menu_send_lesson_progress_when_swiping` |
| 79 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_width` | `match_parent` |
| 80 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_height` | `wrap_content` |
| 81 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_icon` | `@drawable/ic_cap` |
| 82 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_label` | `@string/developer_menu_send_lesson_progress_when_swiping` |
| 83 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:id` | `@id/item_developer_menu_force_reactivation_prompt_on_app_launch` |
| 84 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_width` | `match_parent` |
| 85 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_height` | `wrap_content` |
| 86 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_icon` | `@drawable/ic_star` |
| 87 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_label` | `@string/developer_menu_force_reactivation_prompt_on_app_launch` |
| 88 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:id` | `@id/item_developer_menu_force_path_overview_eta_enabled` |
| 89 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_width` | `match_parent` |
| 90 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_height` | `wrap_content` |
| 91 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_icon` | `@drawable/ic_ai_task_eye` |
| 92 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_label` | `@string/developer_menu_force_path_overview_eta_enabled` |
| 93 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:id` | `@id/item_developer_menu_force_chapter_end_progress_eta_enabled` |
| 94 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_width` | `match_parent` |
| 95 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_height` | `wrap_content` |
| 96 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_icon` | `@drawable/ic_ai_task_eye` |
| 97 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_label` | `@string/developer_menu_force_chapter_end_progress_eta_enabled` |
| 98 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:id` | `@id/item_developer_menu_disable_leak_canary` |
| 99 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_width` | `match_parent` |
| 100 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_height` | `wrap_content` |
| 101 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_icon` | `@drawable/onboarding_fun` |
| 102 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_label` | `@string/developer_menu_disable_leak_canary` |
| 103 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_reset_push_token` |
| 104 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 105 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 106 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_close_circle_filled` |
| 107 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/developer_menu_reset_push_token` |
| 108 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_reset_global_share_prefs` |
| 109 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 110 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 111 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_close_circle_filled` |
| 112 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `Reset global shared prefs` |
| 113 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_reset_user_properties` |
| 114 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 115 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 116 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_close_circle_filled` |
| 117 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `Reset User Properties` |
| 118 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_reset_dev_menu_options` |
| 119 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 120 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 121 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_close_circle_filled` |
| 122 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `Reset dev menu` |
| 123 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_reset_user_messages_counter` |
| 124 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 125 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 126 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_close_circle_filled` |
| 127 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/developer_menu_reset_user_messages_counter` |
| 128 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_reset_reactivation_flow` |
| 129 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 130 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 131 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_close_circle_filled` |
| 132 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/developer_menu_reset_reactivation_flow` |
| 133 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_crash_app` |
| 134 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 135 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 136 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_bug` |
| 137 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/developer_menu_crash_app` |
| 138 | `LinearLayout` | `android:orientation` | `vertical` |
| 139 | `LinearLayout` | `android:id` | `@id/section_learning_companions` |
| 140 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 141 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 142 | `TextView` | `android:layout_width` | `wrap_content` |
| 143 | `TextView` | `android:layout_height` | `wrap_content` |
| 144 | `TextView` | `android:layout_marginTop` | `36.000000dip` |
| 145 | `TextView` | `android:text` | `Learning companions` |
| 146 | `TextView` | `android:paddingStart` | `16.000000dip` |
| 147 | `TextView` | `android:paddingEnd` | `16.000000dip` |
| 148 | `TextView` | `style` | `@style/TextP3` |
| 149 | `View` | `android:background` | `@color/line_primary` |
| 150 | `View` | `android:layout_width` | `wrap_content` |
| 151 | `View` | `android:layout_height` | `1.000000dip` |
| 152 | `View` | `android:layout_marginTop` | `12.000000dip` |
| 153 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_companions_restart` |
| 154 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 155 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 156 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `Restart companion week` |
| 157 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_companions_advance` |
| 158 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 159 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 160 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `Advance companion week by one day` |
| 161 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_companions_intro` |
| 162 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 163 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 164 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `Open companions intro` |
| 165 | `TextView` | `android:id` | `@id/category_previews` |
| 166 | `TextView` | `android:layout_width` | `wrap_content` |
| 167 | `TextView` | `android:layout_height` | `wrap_content` |
| 168 | `TextView` | `android:layout_marginTop` | `36.000000dip` |
| 169 | `TextView` | `android:text` | `@string/developer_menu_category_previews` |
| 170 | `TextView` | `android:paddingStart` | `16.000000dip` |
| 171 | `TextView` | `android:paddingEnd` | `16.000000dip` |
| 172 | `TextView` | `style` | `@style/TextP3` |
| 173 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_preview_console` |
| 174 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 175 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 176 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_code` |
| 177 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `Input Console` |
| 178 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_modal_dialog_test` |
| 179 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 180 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 181 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_chapter_type_experiment` |
| 182 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `Modal Dialog Test` |
| 183 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_max_upsell_flow_example` |
| 184 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 185 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 186 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_chapter_type_experiment` |
| 187 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/developer_menu_max_upsell_flow_example` |
| 188 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_pro_upsell_flow_example` |
| 189 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 190 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 191 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_chapter_type_experiment` |
| 192 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/developer_menu_pro_upsell_flow_example` |
| 193 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_anniversary_upsell_flow_example` |
| 194 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 195 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 196 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_chapter_type_experiment` |
| 197 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/developer_menu_anniversary_upsell_flow_example` |
| 198 | `TextView` | `android:id` | `@id/category_mock_data` |
| 199 | `TextView` | `android:layout_width` | `wrap_content` |
| 200 | `TextView` | `android:layout_height` | `wrap_content` |
| 201 | `TextView` | `android:layout_marginTop` | `36.000000dip` |
| 202 | `TextView` | `android:text` | `@string/developer_menu_category_mock_data` |
| 203 | `TextView` | `android:paddingStart` | `16.000000dip` |
| 204 | `TextView` | `android:paddingEnd` | `16.000000dip` |
| 205 | `TextView` | `style` | `@style/TextP3` |
| 206 | `View` | `android:background` | `@color/line_primary` |
| 207 | `View` | `android:layout_width` | `wrap_content` |
| 208 | `View` | `android:layout_height` | `1.000000dip` |
| 209 | `View` | `android:layout_marginTop` | `12.000000dip` |
| 210 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:id` | `@id/item_developer_menu_use_mocked_trial_reminder_dates` |
| 211 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_width` | `match_parent` |
| 212 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_height` | `wrap_content` |
| 213 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_icon` | `@drawable/ic_notification` |
| 214 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_label` | `@string/developer_menu_use_mocked_trial_reminder_dates` |
| 215 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_add_test_reward` |
| 216 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 217 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 218 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_coins` |
| 219 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/developer_menu_add_test_reward` |
| 220 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_fake_leaderboards_result` |
| 221 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 222 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 223 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_tab_leaderboard` |
| 224 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/developer_menu_fake_leaderboards_result` |
| 225 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_fake_streak_data` |
| 226 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 227 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 228 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_streak_active` |
| 229 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `Fake streak data` |
| 230 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_fake_subscription` |
| 231 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 232 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 233 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_tab_leaderboard` |
| 234 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/developer_menu_fake_subscription` |
| 235 | `TextView` | `android:id` | `@id/category_live_publishing` |
| 236 | `TextView` | `android:layout_width` | `wrap_content` |
| 237 | `TextView` | `android:layout_height` | `wrap_content` |
| 238 | `TextView` | `android:layout_marginTop` | `36.000000dip` |
| 239 | `TextView` | `android:text` | `@string/developer_menu_category_content` |
| 240 | `TextView` | `android:paddingStart` | `16.000000dip` |
| 241 | `TextView` | `android:paddingEnd` | `16.000000dip` |
| 242 | `TextView` | `style` | `@style/TextP3` |
| 243 | `View` | `android:id` | `@id/separator_settings_3` |
| 244 | `View` | `android:background` | `@color/line_primary` |
| 245 | `View` | `android:layout_width` | `wrap_content` |
| 246 | `View` | `android:layout_height` | `1.000000dip` |
| 247 | `View` | `android:layout_marginTop` | `12.000000dip` |
| 248 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_search_tracks` |
| 249 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 250 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 251 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_search` |
| 252 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/search_tracks` |
| 253 | `com.getmimo.ui.settings.SettingsListLivePreview` | `android:id` | `@id/item_developer_menu_download` |
| 254 | `com.getmimo.ui.settings.SettingsListLivePreview` | `android:layout_width` | `match_parent` |
| 255 | `com.getmimo.ui.settings.SettingsListLivePreview` | `android:layout_height` | `wrap_content` |
| 256 | `com.getmimo.ui.settings.SettingsListLivePreview` | `app:settings_icon` | `@drawable/ic_download` |
| 257 | `com.getmimo.ui.settings.SettingsListLivePreview` | `app:settings_label` | `@string/developer_menu_category_live_deployment_download` |
| 258 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:id` | `@id/item_developer_menu_use_unpublished` |
| 259 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_width` | `match_parent` |
| 260 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_height` | `wrap_content` |
| 261 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_icon` | `@drawable/ic_code` |
| 262 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_label` | `@string/developer_menu_category_live_deployment_use_unpublished` |
| 263 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_menu_awesome_mode` |
| 264 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 265 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 266 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/onboarding_fun` |
| 267 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/developer_menu_awesome_mode` |
| 268 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_developer_lessons_variations_chapter` |
| 269 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `match_parent` |
| 270 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 271 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_cap` |
| 272 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/developer_menu_lessons_variation_track` |
| 273 | `TextView` | `android:gravity` | `0x00000001` |
| 274 | `TextView` | `android:layout_gravity` | `0x00000001` |
| 275 | `TextView` | `android:id` | `@id/tv_push_notification_token` |
| 276 | `TextView` | `android:layout_width` | `match_parent` |
| 277 | `TextView` | `android:layout_height` | `wrap_content` |
| 278 | `TextView` | `android:layout_marginTop` | `16.000000dip` |
| 279 | `TextView` | `android:layout_marginStart` | `16.000000dip` |
| 280 | `TextView` | `android:layout_marginEnd` | `16.000000dip` |
| 281 | `TextView` | `style` | `@style/TextP3` |
| 282 | `TextView` | `android:gravity` | `0x00000001` |
| 283 | `TextView` | `android:layout_gravity` | `0x00000001` |
| 284 | `TextView` | `android:id` | `@id/tv_in_app_messaging_token` |
| 285 | `TextView` | `android:layout_width` | `match_parent` |
| 286 | `TextView` | `android:layout_height` | `wrap_content` |
| 287 | `TextView` | `android:layout_marginTop` | `16.000000dip` |
| 288 | `TextView` | `android:layout_marginStart` | `16.000000dip` |
| 289 | `TextView` | `android:layout_marginEnd` | `16.000000dip` |
| 290 | `TextView` | `style` | `@style/TextP3` |
| 291 | `TextView` | `android:gravity` | `0x00000001` |
| 292 | `TextView` | `android:layout_gravity` | `0x00000001` |
| 293 | `TextView` | `android:id` | `@id/tv_authentication_method_info` |
| 294 | `TextView` | `android:layout_width` | `match_parent` |
| 295 | `TextView` | `android:layout_height` | `wrap_content` |
| 296 | `TextView` | `android:layout_marginTop` | `16.000000dip` |
| 297 | `TextView` | `android:layout_marginStart` | `16.000000dip` |
| 298 | `TextView` | `android:layout_marginEnd` | `16.000000dip` |
| 299 | `TextView` | `style` | `@style/TextP3` |
| 300 | `TextView` | `android:gravity` | `0x00000001` |
| 301 | `TextView` | `android:layout_gravity` | `0x00000001` |
| 302 | `TextView` | `android:id` | `@id/tv_version_info` |
| 303 | `TextView` | `android:layout_width` | `wrap_content` |
| 304 | `TextView` | `android:layout_height` | `wrap_content` |
| 305 | `TextView` | `android:layout_marginTop` | `16.000000dip` |
| 306 | `TextView` | `style` | `@style/TextP3` |
| 307 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/cv_tutorial_dialog` |
| 308 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `match_parent` |
| 309 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `match_parent` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/line_primary` | `#FFEDEEF6` / `#FF3F4273` (night) |
| `@dimen/general_max_width` | `480.000000dip` |
| `@string/developer_menu_ab_test` | `Ab test` |
| `@string/developer_menu_add_test_reward` | `Add test reward` |
| `@string/developer_menu_anniversary_upsell_flow_example` | `Anniversary Upsell Flow` |
| `@string/developer_menu_awesome_mode` | `Awesome Mode` |
| `@string/developer_menu_campaign` | `Campaign` |
| `@string/developer_menu_category_content` | `Content goodies` |
| `@string/developer_menu_category_live_deployment_download` | `Download latest tracks package` |
| `@string/developer_menu_category_live_deployment_use_unpublished` | `Use unpublished Tracks Package` |
| `@string/developer_menu_category_mock_data` | `Mock data` |
| `@string/developer_menu_category_previews` | `Previews` |
| `@string/developer_menu_clear_image_cache` | `Clear image cache` |
| `@string/developer_menu_content_experiment` | `Content experiment` |
| `@string/developer_menu_crash_app` | `Force app to crash` |
| `@string/developer_menu_disable_leak_canary` | `Disable LeakCanary` |
| `@string/developer_menu_disable_pro` | `Disable pro` |
| `@string/developer_menu_discount` | `Discounts` |
| `@string/developer_menu_enable_preload_images` | `Enable preloading of images` |
| `@string/developer_menu_fake_leaderboards_result` | `Fake leaderboards result` |
| `@string/developer_menu_fake_subscription` | `Fake subscription` |
| `@string/developer_menu_force_chapter_end_progress_eta_enabled` | `Show Progress ETA screen on Chapter End` |
| `@string/developer_menu_force_path_overview_eta_enabled` | `Enable ETA (after first chapter)` |
| `@string/developer_menu_force_reactivation_prompt_on_app_launch` | `Force reactivation flow on app launch` |
| `@string/developer_menu_god_mode` | `God mode` |
| `@string/developer_menu_lessons_variation_track` | `Open lessons variations chapter` |
| `@string/developer_menu_max_upsell_flow_example` | `Max Upsell Flow` |
| `@string/developer_menu_override_remote_config` | `Override remote config` |
| `@string/developer_menu_pro_upsell_flow_example` | `Pro Upsell Flow` |
| `@string/developer_menu_refresh_firebase_remote` | `Refresh firebase remote config` |
| `@string/developer_menu_reset_push_token` | `Reset push token` |
| `@string/developer_menu_reset_reactivation_flow` | `Reset reactivation flow` |
| `@string/developer_menu_reset_user_messages_counter` | `Reset user messages counter` |
| `@string/developer_menu_send_lesson_progress_when_swiping` | `Auto send lesson progress` |
| `@string/developer_menu_use_mocked_trial_reminder_dates` | `Use mocked dates for trial reminder` |
| `@string/developer_menu_use_test_server` | `Use test server` |
| `@string/search_tracks` | `Search tracks` |
| `@style/TextP3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.199982sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/category_live_publishing
@id/category_mock_data
@id/category_previews
@id/cv_tutorial_dialog
@id/item_companions_advance
@id/item_companions_intro
@id/item_companions_restart
@id/item_developer_lessons_variations_chapter
@id/item_developer_menu_ab_test
@id/item_developer_menu_add_test_reward
@id/item_developer_menu_anniversary_upsell_flow_example
@id/item_developer_menu_awesome_mode
@id/item_developer_menu_campaign
@id/item_developer_menu_clear_image_cache
@id/item_developer_menu_content_experiment
@id/item_developer_menu_crash_app
@id/item_developer_menu_disable_leak_canary
@id/item_developer_menu_disable_premium
@id/item_developer_menu_discount
@id/item_developer_menu_download
@id/item_developer_menu_fake_leaderboards_result
@id/item_developer_menu_fake_streak_data
@id/item_developer_menu_fake_subscription
@id/item_developer_menu_firebase_remote_config_override
@id/item_developer_menu_force_chapter_end_progress_eta_enabled
@id/item_developer_menu_force_path_overview_eta_enabled
@id/item_developer_menu_force_reactivation_prompt_on_app_launch
@id/item_developer_menu_god_mode
@id/item_developer_menu_max_upsell_flow_example
@id/item_developer_menu_modal_dialog_test
@id/item_developer_menu_preload_images
@id/item_developer_menu_preview_console
@id/item_developer_menu_pro_upsell_flow_example
@id/item_developer_menu_remote_config_refresh
@id/item_developer_menu_reset_dev_menu_options
@id/item_developer_menu_reset_global_share_prefs
@id/item_developer_menu_reset_push_token
@id/item_developer_menu_reset_reactivation_flow
@id/item_developer_menu_reset_user_messages_counter
@id/item_developer_menu_reset_user_properties
@id/item_developer_menu_search_tracks
@id/item_developer_menu_send_lesson_progress_when_swiping
@id/item_developer_menu_use_mocked_trial_reminder_dates
@id/item_developer_menu_use_test_server
@id/item_developer_menu_use_unpublished
@id/section_learning_companions
@id/separator_settings_3
@id/settings_fragment_max_container
@id/sv_developermenu
@id/tv_authentication_method_info
@id/tv_in_app_messaging_token
@id/tv_push_notification_token
@id/tv_version_info
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.developermenu.DeveloperMenuFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:orientation="vertical" android:id="@id/sv_developermenu" android:layout_width="match_parent" android:layout_height="match_parent" android:fillViewport="true">
  <LinearLayout android:orientation="vertical" android:id="@id/settings_fragment_max_container" android:paddingBottom="24.000000dip" android:layout_width="match_parent" android:layout_height="wrap_content" android:maxWidth="@dimen/general_max_width">
    <TextView android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="16.000000dip" android:text="General" android:paddingStart="16.000000dip" android:paddingEnd="16.000000dip" style="@style/TextP3"/>
    <View android:background="@color/line_primary" android:layout_width="wrap_content" android:layout_height="1.000000dip" android:layout_marginTop="12.000000dip"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_ab_test" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_chapter_type_experiment" app:settings_label="@string/developer_menu_ab_test"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_content_experiment" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_chapter_type_experiment" app:settings_label="@string/developer_menu_content_experiment"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_firebase_remote_config_override" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_code" app:settings_label="@string/developer_menu_override_remote_config"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_remote_config_refresh" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_refresh_cw" app:settings_label="@string/developer_menu_refresh_firebase_remote"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_campaign" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_star" app:settings_label="@string/developer_menu_campaign"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_discount" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_chapter_type_experiment" app:settings_label="@string/developer_menu_discount"/>
    <com.getmimo.ui.settings.SettingsListSwitchItem android:id="@id/item_developer_menu_disable_premium" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_star" app:settings_label="@string/developer_menu_disable_pro"/>
    <com.getmimo.ui.settings.SettingsListSwitchItem android:id="@id/item_developer_menu_use_test_server" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_code" app:settings_label="@string/developer_menu_use_test_server"/>
    <com.getmimo.ui.settings.SettingsListSwitchItem android:id="@id/item_developer_menu_preload_images" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_download" app:settings_label="@string/developer_menu_enable_preload_images"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_clear_image_cache" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_close_circle_filled" app:settings_label="@string/developer_menu_clear_image_cache"/>
    <com.getmimo.ui.settings.SettingsListSwitchItem android:id="@id/item_developer_menu_god_mode" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_challenge" app:settings_label="@string/developer_menu_god_mode"/>
    <com.getmimo.ui.settings.SettingsListSwitchItem android:id="@id/item_developer_menu_send_lesson_progress_when_swiping" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_cap" app:settings_label="@string/developer_menu_send_lesson_progress_when_swiping"/>
    <com.getmimo.ui.settings.SettingsListSwitchItem android:id="@id/item_developer_menu_force_reactivation_prompt_on_app_launch" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_star" app:settings_label="@string/developer_menu_force_reactivation_prompt_on_app_launch"/>
    <com.getmimo.ui.settings.SettingsListSwitchItem android:id="@id/item_developer_menu_force_path_overview_eta_enabled" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_ai_task_eye" app:settings_label="@string/developer_menu_force_path_overview_eta_enabled"/>
    <com.getmimo.ui.settings.SettingsListSwitchItem android:id="@id/item_developer_menu_force_chapter_end_progress_eta_enabled" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_ai_task_eye" app:settings_label="@string/developer_menu_force_chapter_end_progress_eta_enabled"/>
    <com.getmimo.ui.settings.SettingsListSwitchItem android:id="@id/item_developer_menu_disable_leak_canary" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/onboarding_fun" app:settings_label="@string/developer_menu_disable_leak_canary"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_reset_push_token" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_close_circle_filled" app:settings_label="@string/developer_menu_reset_push_token"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_reset_global_share_prefs" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_close_circle_filled" app:settings_label="Reset global shared prefs"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_reset_user_properties" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_close_circle_filled" app:settings_label="Reset User Properties"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_reset_dev_menu_options" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_close_circle_filled" app:settings_label="Reset dev menu"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_reset_user_messages_counter" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_close_circle_filled" app:settings_label="@string/developer_menu_reset_user_messages_counter"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_reset_reactivation_flow" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_close_circle_filled" app:settings_label="@string/developer_menu_reset_reactivation_flow"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_crash_app" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_bug" app:settings_label="@string/developer_menu_crash_app"/>
    <LinearLayout android:orientation="vertical" android:id="@id/section_learning_companions" android:layout_width="match_parent" android:layout_height="wrap_content">
      <TextView android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="36.000000dip" android:text="Learning companions" android:paddingStart="16.000000dip" android:paddingEnd="16.000000dip" style="@style/TextP3"/>
      <View android:background="@color/line_primary" android:layout_width="wrap_content" android:layout_height="1.000000dip" android:layout_marginTop="12.000000dip"/>
      <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_companions_restart" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_label="Restart companion week"/>
      <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_companions_advance" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_label="Advance companion week by one day"/>
      <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_companions_intro" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_label="Open companions intro"/>
    </LinearLayout>
    <TextView android:id="@id/category_previews" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="36.000000dip" android:text="@string/developer_menu_category_previews" android:paddingStart="16.000000dip" android:paddingEnd="16.000000dip" style="@style/TextP3"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_preview_console" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_code" app:settings_label="Input Console"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_modal_dialog_test" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_chapter_type_experiment" app:settings_label="Modal Dialog Test"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_max_upsell_flow_example" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_chapter_type_experiment" app:settings_label="@string/developer_menu_max_upsell_flow_example"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_pro_upsell_flow_example" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_chapter_type_experiment" app:settings_label="@string/developer_menu_pro_upsell_flow_example"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_anniversary_upsell_flow_example" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_chapter_type_experiment" app:settings_label="@string/developer_menu_anniversary_upsell_flow_example"/>
    <TextView android:id="@id/category_mock_data" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="36.000000dip" android:text="@string/developer_menu_category_mock_data" android:paddingStart="16.000000dip" android:paddingEnd="16.000000dip" style="@style/TextP3"/>
    <View android:background="@color/line_primary" android:layout_width="wrap_content" android:layout_height="1.000000dip" android:layout_marginTop="12.000000dip"/>
    <com.getmimo.ui.settings.SettingsListSwitchItem android:id="@id/item_developer_menu_use_mocked_trial_reminder_dates" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_notification" app:settings_label="@string/developer_menu_use_mocked_trial_reminder_dates"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_add_test_reward" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_coins" app:settings_label="@string/developer_menu_add_test_reward"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_fake_leaderboards_result" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_tab_leaderboard" app:settings_label="@string/developer_menu_fake_leaderboards_result"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_fake_streak_data" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_streak_active" app:settings_label="Fake streak data"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_fake_subscription" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_tab_leaderboard" app:settings_label="@string/developer_menu_fake_subscription"/>
    <TextView android:id="@id/category_live_publishing" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="36.000000dip" android:text="@string/developer_menu_category_content" android:paddingStart="16.000000dip" android:paddingEnd="16.000000dip" style="@style/TextP3"/>
    <View android:id="@id/separator_settings_3" android:background="@color/line_primary" android:layout_width="wrap_content" android:layout_height="1.000000dip" android:layout_marginTop="12.000000dip"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_search_tracks" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_search" app:settings_label="@string/search_tracks"/>
    <com.getmimo.ui.settings.SettingsListLivePreview android:id="@id/item_developer_menu_download" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_download" app:settings_label="@string/developer_menu_category_live_deployment_download"/>
    <com.getmimo.ui.settings.SettingsListSwitchItem android:id="@id/item_developer_menu_use_unpublished" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_code" app:settings_label="@string/developer_menu_category_live_deployment_use_unpublished"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_menu_awesome_mode" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/onboarding_fun" app:settings_label="@string/developer_menu_awesome_mode"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_developer_lessons_variations_chapter" android:layout_width="match_parent" android:layout_height="wrap_content" app:settings_icon="@drawable/ic_cap" app:settings_label="@string/developer_menu_lessons_variation_track"/>
    <TextView android:gravity="0x00000001" android:layout_gravity="0x00000001" android:id="@id/tv_push_notification_token" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="16.000000dip" android:layout_marginStart="16.000000dip" android:layout_marginEnd="16.000000dip" style="@style/TextP3"/>
    <TextView android:gravity="0x00000001" android:layout_gravity="0x00000001" android:id="@id/tv_in_app_messaging_token" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="16.000000dip" android:layout_marginStart="16.000000dip" android:layout_marginEnd="16.000000dip" style="@style/TextP3"/>
    <TextView android:gravity="0x00000001" android:layout_gravity="0x00000001" android:id="@id/tv_authentication_method_info" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="16.000000dip" android:layout_marginStart="16.000000dip" android:layout_marginEnd="16.000000dip" style="@style/TextP3"/>
    <TextView android:gravity="0x00000001" android:layout_gravity="0x00000001" android:id="@id/tv_version_info" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="16.000000dip" style="@style/TextP3"/>
    <androidx.compose.ui.platform.ComposeView android:id="@id/cv_tutorial_dialog" android:layout_width="match_parent" android:layout_height="match_parent"/>
  </LinearLayout>
</ScrollView>
```
