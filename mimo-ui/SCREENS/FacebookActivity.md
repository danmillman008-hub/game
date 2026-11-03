# صفحه — `FacebookActivity`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.facebook.FacebookActivity` |
| نوع | `activity` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `@style/MaterialDarkModeTheme.TranslucentStatusBar.NoAnim` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `False` |
| فناوری | `third-party` |
| تعداد لایه‌های متصل | 7 |
| ComposeView | خیر |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/com_facebook_activity_layout.xml`](../SOURCE/res/layout/com_facebook_activity_layout.xml) → [dossier](LAYOUTS/layout_com_facebook_activity_layout.md)
- [`res/layout/com_facebook_device_auth_dialog_fragment.xml`](../SOURCE/res/layout/com_facebook_device_auth_dialog_fragment.xml) → [dossier](LAYOUTS/layout_com_facebook_device_auth_dialog_fragment.md)
- [`res/layout/com_facebook_login_fragment.xml`](../SOURCE/res/layout/com_facebook_login_fragment.xml) → [dossier](LAYOUTS/layout_com_facebook_login_fragment.md)
- [`res/layout/com_facebook_smart_device_dialog_fragment.xml`](../SOURCE/res/layout/com_facebook_smart_device_dialog_fragment.xml) → [dossier](LAYOUTS/layout_com_facebook_smart_device_dialog_fragment.md)
- [`res/layout-land/com_facebook_sso_noapp_dialog.xml`](../SOURCE/res/layout-land/com_facebook_sso_noapp_dialog.xml) → [dossier](LAYOUTS/layout-land_com_facebook_sso_noapp_dialog.md)
- [`res/layout/com_facebook_sso_noapp_dialog.xml`](../SOURCE/res/layout/com_facebook_sso_noapp_dialog.xml) → [dossier](LAYOUTS/layout_com_facebook_sso_noapp_dialog.md)
- [`res/layout/com_facebook_tooltip_bubble.xml`](../SOURCE/res/layout/com_facebook_tooltip_bubble.xml) → [dossier](LAYOUTS/layout_com_facebook_tooltip_bubble.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/com_facebook_activity_layout.xml`

```text
└─ FrameLayout  #@id/com_facebook_fragment_container
```

### `res/layout/com_facebook_device_auth_dialog_fragment.xml`

```text
└─ androidx.cardview.widget.CardView
   └─ LinearLayout
      ├─ RelativeLayout
      │  ├─ FrameLayout
      │  │  └─ androidx.appcompat.widget.AppCompatImageView
      │  ├─ TextView  #@id/confirmation_code
      │  └─ ProgressBar  #@id/progress_bar
      ├─ TextView  #@id/com_facebook_device_auth_instructions
      └─ FrameLayout
         └─ Button  #@id/cancel_button
            └─ requestFocus
```

### `res/layout/com_facebook_login_fragment.xml`

```text
└─ RelativeLayout
   └─ ProgressBar  #@id/com_facebook_login_fragment_progress_bar
```

### `res/layout/com_facebook_smart_device_dialog_fragment.xml`

```text
└─ androidx.cardview.widget.CardView
   └─ LinearLayout
      ├─ RelativeLayout
      │  ├─ FrameLayout
      │  │  └─ androidx.appcompat.widget.AppCompatImageView
      │  ├─ TextView  #@id/confirmation_code
      │  └─ ProgressBar  #@id/progress_bar
      ├─ TextView  #@id/com_facebook_smart_instructions_0
      ├─ TextView  #@id/com_facebook_smart_instructions_or
      ├─ TextView  #@id/com_facebook_device_auth_instructions
      └─ FrameLayout
         └─ Button  #@id/cancel_button
```

### `res/layout-land/com_facebook_sso_noapp_dialog.xml`

```text
└─ LinearLayout
   ├─ LinearLayout
   │  ├─ ImageView
   │  ├─ TextView  #@id/com_facebook_sso_noapp_title
   │  └─ ImageButton  #@id/com_facebook_sso_noapp_close
   ├─ TextView  #@id/com_facebook_sso_noapp_body
   └─ LinearLayout
      ├─ Button  #@id/com_facebook_sso_noapp_not_now
      └─ Button  #@id/com_facebook_sso_noapp_continue
```

### `res/layout/com_facebook_sso_noapp_dialog.xml`

```text
└─ LinearLayout
   ├─ RelativeLayout
   │  ├─ ImageButton  #@id/com_facebook_sso_noapp_close
   │  └─ LinearLayout
   │     ├─ ImageView
   │     └─ TextView  #@id/com_facebook_sso_noapp_title
   ├─ TextView  #@id/com_facebook_sso_noapp_body
   ├─ Button  #@id/com_facebook_sso_noapp_continue
   └─ Button  #@id/com_facebook_sso_noapp_not_now
```

### `res/layout/com_facebook_tooltip_bubble.xml`

```text
└─ RelativeLayout
   ├─ RelativeLayout  #@id/com_facebook_body_frame
   │  ├─ ImageView  #@id/com_facebook_button_xout
   │  └─ TextView  #@id/com_facebook_tooltip_bubble_view_text_body
   ├─ ImageView  #@id/com_facebook_tooltip_bubble_view_top_pointer
   └─ ImageView  #@id/com_facebook_tooltip_bubble_view_bottom_pointer
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
com_facebook_device_auth_instructions
com_facebook_image_download_unknown_error
com_facebook_internet_permission_error_message
com_facebook_internet_permission_error_title
com_facebook_like_button_liked
com_facebook_like_button_not_liked
com_facebook_loading
com_facebook_loginview_cancel_action
com_facebook_loginview_log_in_button
com_facebook_loginview_log_in_button_continue
com_facebook_loginview_log_in_button_long
com_facebook_loginview_log_out_action
com_facebook_loginview_log_out_button
com_facebook_loginview_logged_in_as
com_facebook_loginview_logged_in_using_facebook
com_facebook_send_button_text
com_facebook_share_button_text
com_facebook_smart_device_instructions
com_facebook_smart_device_instructions_or
com_facebook_smart_login_confirmation_cancel
com_facebook_smart_login_confirmation_continue_as
com_facebook_smart_login_confirmation_title
com_facebook_sso_noapp_body
com_facebook_sso_noapp_not_now
com_facebook_sso_noapp_title
com_facebook_sso_outdated_body
com_facebook_sso_outdated_title
com_facebook_tooltip_default
facebook_app_id
facebook_client_token
settings_liked_us_facebook
streak_chapter_end_sharing_stories_error_facebook
```

## ۴. رنگ‌های مرتبط (فهرست کامل)

```text
com_facebook_blue
com_facebook_button_background_color
com_facebook_button_background_color_disabled
com_facebook_button_background_color_pressed
com_facebook_button_text_color
com_facebook_device_auth_text
com_facebook_likeboxcountview_border_color
com_facebook_likeboxcountview_text_color
com_facebook_likeview_text_color
com_facebook_primary_button_disabled_text_color
com_facebook_primary_button_pressed_text_color
com_facebook_primary_button_text_color
support_facebook
```

## ۵. دایمنشن‌های مرتبط (فهرست کامل)

```text
com_facebook_auth_dialog_corner_radius
com_facebook_auth_dialog_corner_radius_oversized
com_facebook_button_corner_radius
com_facebook_button_login_corner_radius
com_facebook_likeboxcountview_border_radius
com_facebook_likeboxcountview_border_width
com_facebook_likeboxcountview_caret_height
com_facebook_likeboxcountview_caret_width
com_facebook_likeboxcountview_text_padding
com_facebook_likeboxcountview_text_size
com_facebook_likeview_edge_padding
com_facebook_likeview_internal_padding
com_facebook_likeview_text_size
com_facebook_profilepictureview_preset_size_large
com_facebook_profilepictureview_preset_size_normal
com_facebook_profilepictureview_preset_size_small
```

## ۶. استایل‌های مرتبط (فهرست کامل)

```text
com_facebook_activity_theme
com_facebook_auth_dialog
com_facebook_auth_dialog_instructions_textview
com_facebook_button
com_facebook_button_like
com_facebook_loginview_default_style
com_facebook_sso_noapp_dialog
```

## ۷. شواهد حالت‌ها (رشته‌های منبع)

```text
com_facebook_image_download_unknown_error
com_facebook_internet_permission_error_message
com_facebook_internet_permission_error_title
com_facebook_loading
streak_chapter_end_sharing_stories_error_facebook
```

## ۸. ناوبری / deep link

(هیچ intent-filter/data برای این سطح اعلان نشده)
