# پروندهٔ لایه — `res/layout/settings_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/settings_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/settings_fragment.xml`](../../SOURCE/res/layout/settings_fragment.xml) |
| SHA-256 دیکد | `add6b3717fd7445480841f5233d8702cc6d89140c3aad01ffd1952033546ae5b` |
| ریشه | `ScrollView` |
| تعداد گره | 33 |
| تعداد شناسه | 32 |
| تگ‌های استفاده‌شده | 11 |
| ویوهای سفارشی `com.getmimo` | 3 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 5 |
| ارجاع به منابع | 80 |

## ۱. درخت کامل مؤلفه‌ها

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

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `ScrollView` | `android:orientation` | `vertical` |
| 2 | `ScrollView` | `android:id` | `@id/sv_settings` |
| 3 | `ScrollView` | `android:layout_width` | `match_parent` |
| 4 | `ScrollView` | `android:layout_height` | `match_parent` |
| 5 | `ScrollView` | `android:fillViewport` | `true` |
| 6 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingTop` | `36.000000dip` |
| 7 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingBottom` | `24.000000dip` |
| 8 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 9 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 10 | `View` | `android:id` | `@id/settings_fragment_max_container` |
| 11 | `View` | `android:layout_width` | `0.000000dip` |
| 12 | `View` | `android:layout_height` | `100.000000dip` |
| 13 | `View` | `app:layout_constrainedWidth` | `true` |
| 14 | `View` | `app:layout_constraintEnd_toEndOf` | `0` |
| 15 | `View` | `app:layout_constraintStart_toStartOf` | `0` |
| 16 | `View` | `app:layout_constraintTop_toTopOf` | `0` |
| 17 | `View` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 18 | `include` | `android:id` | `@id/layout_user_settings` |
| 19 | `include` | `android:layout_width` | `0.000000dip` |
| 20 | `include` | `android:layout_height` | `wrap_content` |
| 21 | `include` | `app:layout_constraintEnd_toEndOf` | `@id/settings_fragment_max_container` |
| 22 | `include` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 23 | `include` | `app:layout_constraintTop_toTopOf` | `0` |
| 24 | `include` | `layout` | `@layout/settings_user_settings` |
| 25 | `TextView` | `android:textColor` | `@color/text_weak` |
| 26 | `TextView` | `android:id` | `@id/category_1_app` |
| 27 | `TextView` | `android:layout_width` | `wrap_content` |
| 28 | `TextView` | `android:layout_height` | `wrap_content` |
| 29 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 30 | `TextView` | `android:text` | `@string/settings_app` |
| 31 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 32 | `TextView` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 33 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/layout_user_settings` |
| 34 | `TextView` | `style` | `@style/TextTitle3` |
| 35 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_settings_content_language` |
| 36 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `0.000000dip` |
| 37 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 38 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 39 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintEnd_toEndOf` | `@id/settings_fragment_max_container` |
| 40 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 41 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintTop_toBottomOf` | `@id/category_1_app` |
| 42 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_flag` |
| 43 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/settings_content_language` |
| 44 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_settings_appearance` |
| 45 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `0.000000dip` |
| 46 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 47 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintLeft_toLeftOf` | `@id/settings_fragment_max_container` |
| 48 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintRight_toRightOf` | `@id/settings_fragment_max_container` |
| 49 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintTop_toBottomOf` | `@id/item_settings_content_language` |
| 50 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_goneMarginTop` | `@dimen/spacing_s` |
| 51 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_appearance` |
| 52 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/settings_appearance_title` |
| 53 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:id` | `@id/item_settings_enable_sounds` |
| 54 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_width` | `0.000000dip` |
| 55 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_height` | `wrap_content` |
| 56 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:layout_constraintEnd_toEndOf` | `@id/settings_fragment_max_container` |
| 57 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 58 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:layout_constraintTop_toBottomOf` | `@id/item_settings_appearance` |
| 59 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:layout_goneMarginTop` | `@dimen/spacing_s` |
| 60 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_icon` | `@drawable/ic_volume_max` |
| 61 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_label` | `@string/settings_enable_sound_effects` |
| 62 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_settings_app_icon` |
| 63 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `0.000000dip` |
| 64 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 65 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintLeft_toLeftOf` | `@id/settings_fragment_max_container` |
| 66 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintRight_toRightOf` | `@id/settings_fragment_max_container` |
| 67 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintTop_toBottomOf` | `@id/item_settings_enable_sounds` |
| 68 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_image` |
| 69 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/settings_app_icon` |
| 70 | `TextView` | `android:textColor` | `@color/text_weak` |
| 71 | `TextView` | `android:id` | `@id/category_2_account` |
| 72 | `TextView` | `android:layout_width` | `wrap_content` |
| 73 | `TextView` | `android:layout_height` | `wrap_content` |
| 74 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 75 | `TextView` | `android:text` | `@string/settings_account` |
| 76 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 77 | `TextView` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 78 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/item_settings_app_icon` |
| 79 | `TextView` | `style` | `@style/TextTitle3` |
| 80 | `com.getmimo.ui.settings.SettingsListItemPremium` | `android:id` | `@id/item_settings_upgrade_premium` |
| 81 | `com.getmimo.ui.settings.SettingsListItemPremium` | `android:visibility` | `gone` |
| 82 | `com.getmimo.ui.settings.SettingsListItemPremium` | `android:layout_width` | `0.000000dip` |
| 83 | `com.getmimo.ui.settings.SettingsListItemPremium` | `android:layout_height` | `wrap_content` |
| 84 | `com.getmimo.ui.settings.SettingsListItemPremium` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 85 | `com.getmimo.ui.settings.SettingsListItemPremium` | `app:layout_constraintEnd_toEndOf` | `@id/settings_fragment_max_container` |
| 86 | `com.getmimo.ui.settings.SettingsListItemPremium` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 87 | `com.getmimo.ui.settings.SettingsListItemPremium` | `app:layout_constraintTop_toBottomOf` | `@id/category_2_account` |
| 88 | `com.getmimo.ui.settings.SettingsListItemPremium` | `app:settings_icon` | `@drawable/ic_star` |
| 89 | `com.getmimo.ui.settings.SettingsListItemPremium` | `app:settings_label` | `@string/settings_upgrade_to_pro` |
| 90 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_settings_change_password` |
| 91 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `0.000000dip` |
| 92 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 93 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintEnd_toEndOf` | `@id/settings_fragment_max_container` |
| 94 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 95 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintTop_toBottomOf` | `@id/item_settings_upgrade_premium` |
| 96 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_goneMarginTop` | `@dimen/spacing_s` |
| 97 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_lock_alt_02` |
| 98 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/settings_change_password` |
| 99 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_settings_set_goal` |
| 100 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `0.000000dip` |
| 101 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 102 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintEnd_toEndOf` | `@id/settings_fragment_max_container` |
| 103 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 104 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintTop_toBottomOf` | `@id/item_settings_change_password` |
| 105 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_location_my` |
| 106 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/settings_set_goal` |
| 107 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_settings_refresh_subscription` |
| 108 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `0.000000dip` |
| 109 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 110 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintEnd_toEndOf` | `@id/settings_fragment_max_container` |
| 111 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 112 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintTop_toBottomOf` | `@id/item_settings_set_goal` |
| 113 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_redo` |
| 114 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/settings_refresh_purchases` |
| 115 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_settings_delete_account` |
| 116 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `0.000000dip` |
| 117 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 118 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 119 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintTop_toBottomOf` | `@id/item_settings_refresh_subscription` |
| 120 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_color` | `@color/error_default` |
| 121 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_trash` |
| 122 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon_color` | `@color/error_default` |
| 123 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/settings_delete_account` |
| 124 | `TextView` | `android:textColor` | `@color/text_weak` |
| 125 | `TextView` | `android:id` | `@id/category_2_notifications` |
| 126 | `TextView` | `android:layout_width` | `wrap_content` |
| 127 | `TextView` | `android:layout_height` | `wrap_content` |
| 128 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 129 | `TextView` | `android:text` | `@string/settings_notifications` |
| 130 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 131 | `TextView` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 132 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/item_settings_delete_account` |
| 133 | `TextView` | `style` | `@style/TextTitle3` |
| 134 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:id` | `@id/item_settings_enable_notifications` |
| 135 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_width` | `0.000000dip` |
| 136 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_height` | `wrap_content` |
| 137 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 138 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:layout_constraintEnd_toEndOf` | `@id/settings_fragment_max_container` |
| 139 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 140 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:layout_constraintTop_toBottomOf` | `@id/category_2_notifications` |
| 141 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_icon` | `@drawable/ic_notifications` |
| 142 | `com.getmimo.ui.settings.SettingsListSwitchItem` | `app:settings_label` | `@string/settings_enable_daily_reminder` |
| 143 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_settings_reminder_time` |
| 144 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `0.000000dip` |
| 145 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 146 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintEnd_toEndOf` | `@id/settings_fragment_max_container` |
| 147 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 148 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintTop_toBottomOf` | `@id/item_settings_enable_notifications` |
| 149 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_time` |
| 150 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/settings_reminder_time` |
| 151 | `TextView` | `android:textColor` | `@color/text_weak` |
| 152 | `TextView` | `android:id` | `@id/category_2_share` |
| 153 | `TextView` | `android:layout_width` | `wrap_content` |
| 154 | `TextView` | `android:layout_height` | `wrap_content` |
| 155 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 156 | `TextView` | `android:text` | `@string/settings_share` |
| 157 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 158 | `TextView` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 159 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/item_settings_reminder_time` |
| 160 | `TextView` | `style` | `@style/TextTitle3` |
| 161 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_settings_rate_us` |
| 162 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `0.000000dip` |
| 163 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 164 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 165 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintEnd_toEndOf` | `@id/settings_fragment_max_container` |
| 166 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 167 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintTop_toBottomOf` | `@id/category_2_share` |
| 168 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_star` |
| 169 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/settings_rate_us` |
| 170 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_follow_us_x` |
| 171 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `0.000000dip` |
| 172 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 173 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintEnd_toEndOf` | `@id/settings_fragment_max_container` |
| 174 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 175 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintTop_toBottomOf` | `@id/item_settings_rate_us` |
| 176 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_x` |
| 177 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/settings_follow_us_x` |
| 178 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_like_us_facebook` |
| 179 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `0.000000dip` |
| 180 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 181 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintEnd_toEndOf` | `@id/settings_fragment_max_container` |
| 182 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 183 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintTop_toBottomOf` | `@id/item_follow_us_x` |
| 184 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_facebook` |
| 185 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/settings_liked_us_facebook` |
| 186 | `TextView` | `android:textColor` | `@color/text_weak` |
| 187 | `TextView` | `android:id` | `@id/category_3_support` |
| 188 | `TextView` | `android:layout_width` | `wrap_content` |
| 189 | `TextView` | `android:layout_height` | `wrap_content` |
| 190 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 191 | `TextView` | `android:text` | `@string/settings_support` |
| 192 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 193 | `TextView` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 194 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/item_like_us_facebook` |
| 195 | `TextView` | `style` | `@style/TextTitle3` |
| 196 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_settings_help` |
| 197 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `0.000000dip` |
| 198 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 199 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 200 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintEnd_toEndOf` | `@id/settings_fragment_max_container` |
| 201 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 202 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintTop_toBottomOf` | `@id/category_3_support` |
| 203 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_help` |
| 204 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/settings_help` |
| 205 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_settings_terms_and_conditions` |
| 206 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `0.000000dip` |
| 207 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 208 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintEnd_toEndOf` | `@id/settings_fragment_max_container` |
| 209 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 210 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintTop_toBottomOf` | `@id/item_settings_help` |
| 211 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_file` |
| 212 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/settings_terms_and_conditions` |
| 213 | `com.getmimo.ui.settings.SettingsListItem` | `android:id` | `@id/item_settings_privacy_policy` |
| 214 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_width` | `0.000000dip` |
| 215 | `com.getmimo.ui.settings.SettingsListItem` | `android:layout_height` | `wrap_content` |
| 216 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintEnd_toEndOf` | `@id/settings_fragment_max_container` |
| 217 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 218 | `com.getmimo.ui.settings.SettingsListItem` | `app:layout_constraintTop_toBottomOf` | `@id/item_settings_terms_and_conditions` |
| 219 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_icon` | `@drawable/ic_lock_alt_02` |
| 220 | `com.getmimo.ui.settings.SettingsListItem` | `app:settings_label` | `@string/settings_privacy_policy` |
| 221 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/item_settings_create_account` |
| 222 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 223 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 224 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 225 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 226 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginEnd` | `@dimen/spacing_m` |
| 227 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `@id/settings_fragment_max_container` |
| 228 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 229 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/item_settings_privacy_policy` |
| 230 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/item_settings_log_in` |
| 231 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 232 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 233 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 234 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 235 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginEnd` | `@dimen/spacing_m` |
| 236 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `@id/settings_fragment_max_container` |
| 237 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 238 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/item_settings_create_account` |
| 239 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/item_settings_log_out` |
| 240 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 241 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 242 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 243 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 244 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginEnd` | `@dimen/spacing_m` |
| 245 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `@id/settings_fragment_max_container` |
| 246 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 247 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/item_settings_privacy_policy` |
| 248 | `androidx.constraintlayout.widget.Barrier` | `android:id` | `@id/buttons_bottom_barrier` |
| 249 | `androidx.constraintlayout.widget.Barrier` | `android:layout_width` | `wrap_content` |
| 250 | `androidx.constraintlayout.widget.Barrier` | `android:layout_height` | `wrap_content` |
| 251 | `androidx.constraintlayout.widget.Barrier` | `app:barrierDirection` | `3` |
| 252 | `androidx.constraintlayout.widget.Barrier` | `app:constraint_referenced_ids` | `item_settings_log_out,item_settings_log_in` |
| 253 | `TextView` | `android:textColor` | `@color/text_weak` |
| 254 | `TextView` | `android:gravity` | `0x00000001` |
| 255 | `TextView` | `android:id` | `@id/tv_version_info` |
| 256 | `TextView` | `android:layout_width` | `wrap_content` |
| 257 | `TextView` | `android:layout_height` | `wrap_content` |
| 258 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 259 | `TextView` | `android:layout_marginBottom` | `92.000000dip` |
| 260 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 261 | `TextView` | `app:layout_constraintEnd_toEndOf` | `@id/settings_fragment_max_container` |
| 262 | `TextView` | `app:layout_constraintStart_toStartOf` | `@id/settings_fragment_max_container` |
| 263 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/buttons_bottom_barrier` |
| 264 | `TextView` | `style` | `@style/TextP4` |
| 265 | `androidx.constraintlayout.widget.Group` | `android:id` | `@id/logged_in_user_views` |
| 266 | `androidx.constraintlayout.widget.Group` | `android:visibility` | `visible` |
| 267 | `androidx.constraintlayout.widget.Group` | `android:layout_width` | `wrap_content` |
| 268 | `androidx.constraintlayout.widget.Group` | `android:layout_height` | `wrap_content` |
| 269 | `androidx.constraintlayout.widget.Group` | `app:constraint_referenced_ids` | `item_settings_change_password,item_settings_log_out` |
| 270 | `androidx.constraintlayout.widget.Group` | `android:id` | `@id/anonymous_user_views` |
| 271 | `androidx.constraintlayout.widget.Group` | `android:visibility` | `gone` |
| 272 | `androidx.constraintlayout.widget.Group` | `android:layout_width` | `wrap_content` |
| 273 | `androidx.constraintlayout.widget.Group` | `android:layout_height` | `wrap_content` |
| 274 | `androidx.constraintlayout.widget.Group` | `app:constraint_referenced_ids` | `item_settings_log_in,item_settings_create_account` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/error_default` | `#FFF05A6E` / `#FFF97F8D` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/general_max_width` | `480.000000dip` |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@string/settings_account` | `Account` / `Account` (de) / `Cuenta` (es) / `Compte` (fr) / `Akun` (in) / `Account` (it) / `Konto` (pl) / `Conta` (pt-rBR) / `Аккаунт` (ru) / `Hesap` (tr) |
| `@string/settings_app` | `App Settings` / `App-Einstellungen` (de) / `Ajustes de la App` (es) / `Paramètres de l'appli` (fr) / `Pengaturan aplikasi` (in) / `Impostazioni app` (it) / `Ustawienia aplikacji` (pl) / `Configurações do aplicativo` (pt-rBR) / `Настройки приложения` (ru) / `Uygulama Ayarları` (tr) |
| `@string/settings_app_icon` | `App icon` / `App-Icon` (de) / `Icono de la App` (es) / `Icône de l'appli` (fr) / `Ikon aplikasi` (in) / `Icona app` (it) / `Ikona aplikacji` (pl) / `Ícone do aplicativo` (pt-rBR) / `Иконка` (ru) / `Uygulama simgesi` (tr) |
| `@string/settings_appearance_title` | `Appearance` / `Erscheinungsbild` (de) / `Apariencia` (es) / `Apparence` (fr) / `Tampilan` (in) / `Aspetto` (it) / `Wygląd` (pl) / `Aparência` (pt-rBR) / `Внешний вид` (ru) / `Görünüm` (tr) |
| `@string/settings_change_password` | `Change password` / `Passwort ändern` (de) / `Cambiar contraseña` (es) / `Modifier le mot de passe` (fr) / `Ganti kata sandi` (in) / `Cambia password` (it) / `Zmień hasło` (pl) / `Alterar senha` (pt-rBR) / `Изменить пароль` (ru) / `Şifreyi değiştir` (tr) |
| `@string/settings_content_language` | `Content language` / `Content-Sprache` (de) / `Idioma` (es) / `Langue du contenu` (fr) / `Bahasa konten` (in) / `Lingua dei contenuti` (it) / `Język treści` (pl) / `Idioma do conteúdo` (pt-rBR) / `Язык` (ru) / `İçerik dili` (tr) |
| `@string/settings_delete_account` | `Delete account` / `Account löschen` (de) / `Eliminar cuenta` (es) / `Supprimer le compte` (fr) / `Hapus akun` (in) / `Elimina account` (it) / `Usuń konto` (pl) / `Excluir conta` (pt-rBR) / `Удалить аккаунт` (ru) / `Hesabı sil` (tr) |
| `@string/settings_enable_daily_reminder` | `Daily reminder` / `Tägliche Erinnerung` (de) / `Recordatorio diario` (es) / `Rappel quotidien` (fr) / `Pengingat harian` (in) / `Promemoria giornaliero` (it) / `Codzienne przypomnienie` (pl) / `Lembrete diário` (pt-rBR) / `Ежедневные напоминания` (ru) / `Günlük hatırlatıcı` (tr) |
| `@string/settings_enable_sound_effects` | `Sound effects` / `Soundeffekte` (de) / `Efectos de sonido` (es) / `Effets sonores` (fr) / `Efek suara` (in) / `Effetti sonori` (it) / `Efekty dźwiękowe` (pl) / `Efeitos sonoros` (pt-rBR) / `Звуковые эффекты` (ru) / `Ses efektleri` (tr) |
| `@string/settings_follow_us_x` | `Follow us on X` / `Folge uns auf X` (de) / `Síguenos en X` (es) / `Suis-nous sur X` (fr) / `Ikuti kami di X` (in) / `Seguici su X` (it) / `Obserwuj nas na X` (pl) / `Siga-nos no X` (pt-rBR) / `Подпишись на нас в X` (ru) / `X'te bizi takip et` (tr) |
| `@string/settings_help` | `Help` / `Hilfe` (de) / `Ayuda` (es) / `Aide` (fr) / `Bantuan` (in) / `Aiuto` (it) / `Pomoc` (pl) / `Ajuda` (pt-rBR) / `Помощь` (ru) / `Yardım` (tr) |
| `@string/settings_liked_us_facebook` | `Like us on Facebook` / `Like uns auf Facebook` (de) / `Dale a me gusta en Facebook` (es) / `Aime-nous sur Facebook` (fr) / `Sukai kami di Facebook` (in) / `Metti mi piace su Facebook` (it) / `Polub nas na Facebooku` (pl) / `Curta-nos no Facebook` (pt-rBR) / `Подпишись на нас в Facebook` (ru) / `Facebook'ta bizi beğen` (tr) |
| `@string/settings_notifications` | `Notifications` / `Benachrichtigungen` (de) / `Notificaciones` (es) / `Notifications` (fr) / `Notifikasi` (in) / `Notifiche` (it) / `Powiadomienia` (pl) / `Notificações` (pt-rBR) / `Уведомления` (ru) / `Bildirimler` (tr) |
| `@string/settings_privacy_policy` | `Privacy policy` / `Datenschutzrichtlinien` (de) / `Política de privacidad` (es) / `Politique de confidentialité` (fr) / `Kebijakan privasi` (in) / `Privacy policy` (it) / `Polityka prywatności` (pl) / `Política de privacidade` (pt-rBR) / `Политика конфиденциальности` (ru) / `Gizlilik politikası` (tr) |
| `@string/settings_rate_us` | `Rate us on the Play Store` / `Bewerte uns im Play Store` (de) / `Valóranos en Play Store` (es) / `Évalue-nous sur Play Store` (fr) / `Beri rating di Play Store` (in) / `Valutaci sul Play Store` (it) / `Oceń nas w Play Store` (pl) / `Avalie-nos na Play Store` (pt-rBR) / `Оцени нас в Play Store` (ru) / `Play Store'da bizi değerlendir` (tr) |
| `@string/settings_refresh_purchases` | `Refresh subscriptions` / `Abonnements aktualisieren` (de) / `Renovar suscripciones` (es) / `Rafraîchir les abonnements` (fr) / `Muat ulang langganan` (in) / `Aggiorna abbonamenti` (it) / `Odśwież subskrypcje` (pl) / `Atualizar assinaturas` (pt-rBR) / `Проверить подписку` (ru) / `Abonelikleri yenile` (tr) |
| `@string/settings_reminder_time` | `Reminder time` / `Erinnerungszeit` (de) / `Hora del recordatorio` (es) / `Heure de rappel` (fr) / `Waktu pengingat` (in) / `Orario promemoria` (it) / `Godzina przypomnienia` (pl) / `Horário do lembrete` (pt-rBR) / `Время уведомлений` (ru) / `Hatırlatma saati` (tr) |
| `@string/settings_set_goal` | `Set goal` / `Ziel festlegen` (de) / `Establecer objetivo` (es) / `Définir l'objectif` (fr) / `Atur target` (in) / `Imposta obiettivo` (it) / `Ustaw cel` (pl) / `Definir meta` (pt-rBR) / `Поставить цель` (ru) / `Hedef belirle` (tr) |
| `@string/settings_share` | `Share` / `Teilen` (de) / `Compartir` (es) / `Partager` (fr) / `Bagikan` (in) / `Condividi` (it) / `Udostępnij` (pl) / `Compartilhar` (pt-rBR) / `Поделиться` (ru) / `Paylaş` (tr) |
| `@string/settings_support` | `Contact us` / `Kontaktiere uns` (de) / `Contacta con nuestro equipo` (es) / `Nous contacter` (fr) / `Hubungi kami` (in) / `Contattaci` (it) / `Napisz do nas` (pl) / `Fale conosco` (pt-rBR) / `Связаться с нами` (ru) / `Bize ulaş` (tr) |
| `@string/settings_terms_and_conditions` | `Terms and conditions` / `AGB` (de) / `Términos y condiciones` (es) / `Termes et conditions` (fr) / `Ketentuan layanan` (in) / `Termini e condizioni` (it) / `Regulamin` (pl) / `Termos e condições` (pt-rBR) / `Условия оказываемых услуг` (ru) / `Şartlar ve koşullar` (tr) |
| `@string/settings_upgrade_to_pro` | `Get Pro` / `Pro nutzen` (de) / `Obtener Pro` (es) / `Passer en Pro` (fr) / `Dapatkan Pro` (in) / `Passa a Pro` (it) / `Przejdź na Pro` (pl) / `Seja Pro` (pt-rBR) / `Стать Pro` (ru) / `Pro'ya geç` (tr) |
| `@style/TextP4` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '12.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '15.599977sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.199982sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextTitle3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '12.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '15.599977sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/anonymous_user_views
@id/buttons_bottom_barrier
@id/category_1_app
@id/category_2_account
@id/category_2_notifications
@id/category_2_share
@id/category_3_support
@id/item_follow_us_x
@id/item_like_us_facebook
@id/item_settings_app_icon
@id/item_settings_appearance
@id/item_settings_change_password
@id/item_settings_content_language
@id/item_settings_create_account
@id/item_settings_delete_account
@id/item_settings_enable_notifications
@id/item_settings_enable_sounds
@id/item_settings_help
@id/item_settings_log_in
@id/item_settings_log_out
@id/item_settings_privacy_policy
@id/item_settings_rate_us
@id/item_settings_refresh_subscription
@id/item_settings_reminder_time
@id/item_settings_set_goal
@id/item_settings_terms_and_conditions
@id/item_settings_upgrade_premium
@id/layout_user_settings
@id/logged_in_user_views
@id/settings_fragment_max_container
@id/sv_settings
@id/tv_version_info
```

## ۵. ارجاع به لایه‌های دیگر

```text
0
0.000000dip
@id/settings_fragment_max_container
@layout/settings_user_settings
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.settings.SettingsActivity
com.getmimo.ui.settings.SettingsFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<ScrollView xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:orientation="vertical" android:id="@id/sv_settings" android:layout_width="match_parent" android:layout_height="match_parent" android:fillViewport="true">
  <androidx.constraintlayout.widget.ConstraintLayout android:paddingTop="36.000000dip" android:paddingBottom="24.000000dip" android:layout_width="match_parent" android:layout_height="wrap_content">
    <View android:id="@id/settings_fragment_max_container" android:layout_width="0.000000dip" android:layout_height="100.000000dip" app:layout_constrainedWidth="true" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:layout_constraintWidth_max="@dimen/general_max_width"/>
    <include android:id="@id/layout_user_settings" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="@id/settings_fragment_max_container" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toTopOf="0" layout="@layout/settings_user_settings"/>
    <TextView android:textColor="@color/text_weak" android:id="@id/category_1_app" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xl" android:text="@string/settings_app" android:layout_marginStart="@dimen/spacing_m" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/layout_user_settings" style="@style/TextTitle3"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_settings_content_language" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" app:layout_constraintEnd_toEndOf="@id/settings_fragment_max_container" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/category_1_app" app:settings_icon="@drawable/ic_flag" app:settings_label="@string/settings_content_language"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_settings_appearance" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintLeft_toLeftOf="@id/settings_fragment_max_container" app:layout_constraintRight_toRightOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/item_settings_content_language" app:layout_goneMarginTop="@dimen/spacing_s" app:settings_icon="@drawable/ic_appearance" app:settings_label="@string/settings_appearance_title"/>
    <com.getmimo.ui.settings.SettingsListSwitchItem android:id="@id/item_settings_enable_sounds" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="@id/settings_fragment_max_container" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/item_settings_appearance" app:layout_goneMarginTop="@dimen/spacing_s" app:settings_icon="@drawable/ic_volume_max" app:settings_label="@string/settings_enable_sound_effects"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_settings_app_icon" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintLeft_toLeftOf="@id/settings_fragment_max_container" app:layout_constraintRight_toRightOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/item_settings_enable_sounds" app:settings_icon="@drawable/ic_image" app:settings_label="@string/settings_app_icon"/>
    <TextView android:textColor="@color/text_weak" android:id="@id/category_2_account" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xl" android:text="@string/settings_account" android:layout_marginStart="@dimen/spacing_m" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/item_settings_app_icon" style="@style/TextTitle3"/>
    <com.getmimo.ui.settings.SettingsListItemPremium android:id="@id/item_settings_upgrade_premium" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" app:layout_constraintEnd_toEndOf="@id/settings_fragment_max_container" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/category_2_account" app:settings_icon="@drawable/ic_star" app:settings_label="@string/settings_upgrade_to_pro"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_settings_change_password" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="@id/settings_fragment_max_container" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/item_settings_upgrade_premium" app:layout_goneMarginTop="@dimen/spacing_s" app:settings_icon="@drawable/ic_lock_alt_02" app:settings_label="@string/settings_change_password"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_settings_set_goal" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="@id/settings_fragment_max_container" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/item_settings_change_password" app:settings_icon="@drawable/ic_location_my" app:settings_label="@string/settings_set_goal"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_settings_refresh_subscription" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="@id/settings_fragment_max_container" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/item_settings_set_goal" app:settings_icon="@drawable/ic_redo" app:settings_label="@string/settings_refresh_purchases"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_settings_delete_account" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/item_settings_refresh_subscription" app:settings_color="@color/error_default" app:settings_icon="@drawable/ic_trash" app:settings_icon_color="@color/error_default" app:settings_label="@string/settings_delete_account"/>
    <TextView android:textColor="@color/text_weak" android:id="@id/category_2_notifications" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xl" android:text="@string/settings_notifications" android:layout_marginStart="@dimen/spacing_m" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/item_settings_delete_account" style="@style/TextTitle3"/>
    <com.getmimo.ui.settings.SettingsListSwitchItem android:id="@id/item_settings_enable_notifications" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" app:layout_constraintEnd_toEndOf="@id/settings_fragment_max_container" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/category_2_notifications" app:settings_icon="@drawable/ic_notifications" app:settings_label="@string/settings_enable_daily_reminder"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_settings_reminder_time" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="@id/settings_fragment_max_container" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/item_settings_enable_notifications" app:settings_icon="@drawable/ic_time" app:settings_label="@string/settings_reminder_time"/>
    <TextView android:textColor="@color/text_weak" android:id="@id/category_2_share" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xl" android:text="@string/settings_share" android:layout_marginStart="@dimen/spacing_m" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/item_settings_reminder_time" style="@style/TextTitle3"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_settings_rate_us" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" app:layout_constraintEnd_toEndOf="@id/settings_fragment_max_container" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/category_2_share" app:settings_icon="@drawable/ic_star" app:settings_label="@string/settings_rate_us"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_follow_us_x" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="@id/settings_fragment_max_container" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/item_settings_rate_us" app:settings_icon="@drawable/ic_x" app:settings_label="@string/settings_follow_us_x"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_like_us_facebook" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="@id/settings_fragment_max_container" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/item_follow_us_x" app:settings_icon="@drawable/ic_facebook" app:settings_label="@string/settings_liked_us_facebook"/>
    <TextView android:textColor="@color/text_weak" android:id="@id/category_3_support" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xl" android:text="@string/settings_support" android:layout_marginStart="@dimen/spacing_m" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/item_like_us_facebook" style="@style/TextTitle3"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_settings_help" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" app:layout_constraintEnd_toEndOf="@id/settings_fragment_max_container" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/category_3_support" app:settings_icon="@drawable/ic_help" app:settings_label="@string/settings_help"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_settings_terms_and_conditions" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="@id/settings_fragment_max_container" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/item_settings_help" app:settings_icon="@drawable/ic_file" app:settings_label="@string/settings_terms_and_conditions"/>
    <com.getmimo.ui.settings.SettingsListItem android:id="@id/item_settings_privacy_policy" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="@id/settings_fragment_max_container" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/item_settings_terms_and_conditions" app:settings_icon="@drawable/ic_lock_alt_02" app:settings_label="@string/settings_privacy_policy"/>
    <androidx.compose.ui.platform.ComposeView android:id="@id/item_settings_create_account" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" android:layout_marginStart="@dimen/spacing_m" android:layout_marginEnd="@dimen/spacing_m" app:layout_constraintEnd_toEndOf="@id/settings_fragment_max_container" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/item_settings_privacy_policy"/>
    <androidx.compose.ui.platform.ComposeView android:id="@id/item_settings_log_in" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xs" android:layout_marginStart="@dimen/spacing_m" android:layout_marginEnd="@dimen/spacing_m" app:layout_constraintEnd_toEndOf="@id/settings_fragment_max_container" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/item_settings_create_account"/>
    <androidx.compose.ui.platform.ComposeView android:id="@id/item_settings_log_out" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" android:layout_marginStart="@dimen/spacing_m" android:layout_marginEnd="@dimen/spacing_m" app:layout_constraintEnd_toEndOf="@id/settings_fragment_max_container" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/item_settings_privacy_policy"/>
    <androidx.constraintlayout.widget.Barrier android:id="@id/buttons_bottom_barrier" android:layout_width="wrap_content" android:layout_height="wrap_content" app:barrierDirection="3" app:constraint_referenced_ids="item_settings_log_out,item_settings_log_in"/>
    <TextView android:textColor="@color/text_weak" android:gravity="0x00000001" android:id="@id/tv_version_info" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xl" android:layout_marginBottom="92.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="@id/settings_fragment_max_container" app:layout_constraintStart_toStartOf="@id/settings_fragment_max_container" app:layout_constraintTop_toBottomOf="@id/buttons_bottom_barrier" style="@style/TextP4"/>
    <androidx.constraintlayout.widget.Group android:id="@id/logged_in_user_views" android:visibility="visible" android:layout_width="wrap_content" android:layout_height="wrap_content" app:constraint_referenced_ids="item_settings_change_password,item_settings_log_out"/>
    <androidx.constraintlayout.widget.Group android:id="@id/anonymous_user_views" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" app:constraint_referenced_ids="item_settings_log_in,item_settings_create_account"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
</ScrollView>
```
