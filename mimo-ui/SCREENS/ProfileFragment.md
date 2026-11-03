# صفحه — `ProfileFragment`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.profile.main.ProfileFragment` |
| نوع | `fragment` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view binding` |
| تعداد لایه‌های متصل | 21 |
| ComposeView | بله |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/card_reactivate_pro.xml`](../SOURCE/res/layout/card_reactivate_pro.xml) → [dossier](LAYOUTS/layout_card_reactivate_pro.md)
- [`res/layout/profile_certificate_view.xml`](../SOURCE/res/layout/profile_certificate_view.xml) → [dossier](LAYOUTS/layout_profile_certificate_view.md)
- [`res/layout/profile_certificates_item.xml`](../SOURCE/res/layout/profile_certificates_item.xml) → [dossier](LAYOUTS/layout_profile_certificates_item.md)
- [`res/layout/profile_certificates_max_item.xml`](../SOURCE/res/layout/profile_certificates_max_item.xml) → [dossier](LAYOUTS/layout_profile_certificates_max_item.md)
- [`res/layout/profile_certificates_view.xml`](../SOURCE/res/layout/profile_certificates_view.xml) → [dossier](LAYOUTS/layout_profile_certificates_view.md)
- [`res/layout/profile_empty_trophies_item.xml`](../SOURCE/res/layout/profile_empty_trophies_item.xml) → [dossier](LAYOUTS/layout_profile_empty_trophies_item.md)
- [`res/layout/profile_fragment.xml`](../SOURCE/res/layout/profile_fragment.xml) → [dossier](LAYOUTS/layout_profile_fragment.md)
- [`res/layout/profile_friend_item.xml`](../SOURCE/res/layout/profile_friend_item.xml) → [dossier](LAYOUTS/layout_profile_friend_item.md)
- [`res/layout/profile_friends_empty.xml`](../SOURCE/res/layout/profile_friends_empty.xml) → [dossier](LAYOUTS/layout_profile_friends_empty.md)
- [`res/layout/profile_friends_header.xml`](../SOURCE/res/layout/profile_friends_header.xml) → [dossier](LAYOUTS/layout_profile_friends_header.md)
- [`res/layout/profile_friends_invite_card.xml`](../SOURCE/res/layout/profile_friends_invite_card.xml) → [dossier](LAYOUTS/layout_profile_friends_invite_card.md)
- [`res/layout/profile_friends_offline.xml`](../SOURCE/res/layout/profile_friends_offline.xml) → [dossier](LAYOUTS/layout_profile_friends_offline.md)
- [`res/layout/profile_friends_placeholder.xml`](../SOURCE/res/layout/profile_friends_placeholder.xml) → [dossier](LAYOUTS/layout_profile_friends_placeholder.md)
- [`res/layout/profile_header.xml`](../SOURCE/res/layout/profile_header.xml) → [dossier](LAYOUTS/layout_profile_header.md)
- [`res/layout/profile_header_unlocked.xml`](../SOURCE/res/layout/profile_header_unlocked.xml) → [dossier](LAYOUTS/layout_profile_header_unlocked.md)
- [`res/layout/profile_header_view.xml`](../SOURCE/res/layout/profile_header_view.xml) → [dossier](LAYOUTS/layout_profile_header_view.md)
- [`res/layout/profile_info_card_view.xml`](../SOURCE/res/layout/profile_info_card_view.xml) → [dossier](LAYOUTS/layout_profile_info_card_view.md)
- [`res/layout/profile_trophies_item.xml`](../SOURCE/res/layout/profile_trophies_item.xml) → [dossier](LAYOUTS/layout_profile_trophies_item.md)
- [`res/layout/public_profile_activity.xml`](../SOURCE/res/layout/public_profile_activity.xml) → [dossier](LAYOUTS/layout_public_profile_activity.md)
- [`res/layout/public_profile_code_header_view.xml`](../SOURCE/res/layout/public_profile_code_header_view.xml) → [dossier](LAYOUTS/layout_public_profile_code_header_view.md)
- [`res/layout/public_profile_fragment.xml`](../SOURCE/res/layout/public_profile_fragment.xml) → [dossier](LAYOUTS/layout_public_profile_fragment.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/card_reactivate_pro.xml`

```text
└─ androidx.cardview.widget.CardView  #@id/cv_partnership_card_strive
   └─ androidx.constraintlayout.widget.ConstraintLayout
      ├─ ImageView  #@id/iv_reactivate_pro
      ├─ TextView  #@id/tv_reactivate_pro_title
      ├─ TextView  #@id/tv_reactivate_pro_description
      └─ TextView  #@id/btn_claim
```

### `res/layout/profile_certificate_view.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ ImageView  #@id/iv_certificate_icon
   ├─ TextView  #@id/tv_certificate_title
   ├─ com.google.android.material.progressindicator.CircularProgressIndicator  #@id/certificate_progress
   ├─ TextView  #@id/tv_certificate_progress_text
   ├─ ImageView  #@id/iv_certificate_download
   └─ View  #@id/v_separator
```

### `res/layout/profile_certificates_item.xml`

```text
└─ LinearLayout
   ├─ TextView
   └─ com.getmimo.ui.profile.view.ProfileCertificatesView  #@id/profile_paths_progress_view
```

### `res/layout/profile_certificates_max_item.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_certificate_title
   ├─ ImageView  #@id/iv_certificate_info_icon
   └─ com.getmimo.ui.profile.view.ProfileCertificatesView  #@id/profile_paths_progress_view
```

### `res/layout/profile_certificates_view.xml`

```text
└─ merge
   └─ LinearLayout  #@id/profile_paths_container
```

### `res/layout/profile_empty_trophies_item.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_trophies_title
   └─ LinearLayout  #@id/layout_no_trophies
      ├─ ImageView
      ├─ TextView
      └─ TextView
```

### `res/layout/profile_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_profile_root
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_profile
   │  └─ include  #@id/layout_toolbar
   ├─ androidx.recyclerview.widget.RecyclerView  #@id/rv_profile
   ├─ com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView  #@id/anonymous_user_lock_view
   └─ com.getmimo.ui.components.common.OfflineView  #@id/profile_offline_view
```

### `res/layout/profile_friend_item.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/root_friend_item
   ├─ ImageView  #@id/iv_avatar
   ├─ TextView  #@id/tv_username_friend_podium_item
   ├─ TextView  #@id/tv_sparks
   ├─ ImageView  #@id/iv_sparks
   ├─ TextView  #@id/tv_streak
   ├─ ImageView  #@id/iv_streak
   └─ View  #@id/v_separator
```

### `res/layout/profile_friends_empty.xml`

```text
└─ LinearLayout
   ├─ ImageView
   ├─ TextView
   └─ TextView
```

### `res/layout/profile_friends_header.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_friends_title
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_add_friends
```

### `res/layout/profile_friends_invite_card.xml`

```text
└─ androidx.cardview.widget.CardView  #@id/cv_profile_invite_card
   └─ androidx.constraintlayout.widget.ConstraintLayout
      ├─ ImageView  #@id/iv_friends_banner
      ├─ TextView  #@id/tv_friends_banner_description
      └─ androidx.compose.ui.platform.ComposeView  #@id/btn_friends_banner_invite
```

### `res/layout/profile_friends_offline.xml`

```text
└─ LinearLayout
   ├─ ImageView
   └─ TextView  #@id/layout_saved_code_empty_view_description
```

### `res/layout/profile_friends_placeholder.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/root_friend_item
   ├─ com.getmimo.ui.components.placeholder.PlaceholderView  #@id/iv_avatar
   ├─ com.getmimo.ui.components.placeholder.PlaceholderView  #@id/tv_username_friend_podium_item
   └─ com.getmimo.ui.components.placeholder.PlaceholderView
```

### `res/layout/profile_header.xml`

```text
└─ FrameLayout
   └─ com.getmimo.ui.profile.view.ProfileHeaderView  #@id/profile_header_view
```

### `res/layout/profile_header_unlocked.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ com.getmimo.ui.components.placeholder.TextPlaceholderView  #@id/tv_settings_user_name
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_profile_header_add_bio
   ├─ com.getmimo.ui.components.placeholder.TextPlaceholderView  #@id/tv_profile_header_bio
   ├─ androidx.constraintlayout.widget.Barrier  #@id/barrier_bio_bottom
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_profile_header_upgrade
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_follow
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_unfollow
```

### `res/layout/profile_header_view.xml`

```text
└─ merge
   ├─ com.google.android.material.imageview.ShapeableImageView  #@id/iv_settings_user_picture
   ├─ TextView  #@id/tv_settings_premium_badge
   ├─ TextView  #@id/tv_settings_max_badge
   ├─ include  #@id/profile_header_unlocked
   ├─ com.getmimo.ui.profile.view.ProfileInfoCard  #@id/profile_info_card_streak
   ├─ com.getmimo.ui.profile.view.ProfileInfoCard  #@id/profile_info_card_xp
   ├─ com.getmimo.ui.profile.view.ProfileInfoCard  #@id/profile_info_card_league
   ├─ androidx.compose.ui.platform.ComposeView  #@id/profile_info_card_longest_streak
   └─ androidx.compose.ui.platform.ComposeView  #@id/cw_share_my_progress
```

### `res/layout/profile_info_card_view.xml`

```text
└─ merge
   └─ androidx.constraintlayout.widget.ConstraintLayout
      ├─ ImageView  #@id/iv_profile_card_icon
      ├─ TextView  #@id/tv_profile_card_value
      ├─ TextView  #@id/tv_profile_card_label
      └─ com.getmimo.ui.components.placeholder.PlaceholderView  #@id/profile_card_placeholder
```

### `res/layout/profile_trophies_item.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_trophies_title
   └─ LinearLayout  #@id/layout_trophies_rows
```

### `res/layout/public_profile_activity.xml`

```text
└─ FrameLayout  #@id/layout_public_profile_activity
```

### `res/layout/public_profile_code_header_view.xml`

```text
└─ TextView  #@id/tv_playgrounds_header
```

### `res/layout/public_profile_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_profile_root
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_profile
   │  └─ include  #@id/layout_toolbar
   ├─ androidx.recyclerview.widget.RecyclerView  #@id/rv_profile
   └─ com.getmimo.ui.components.common.OfflineView  #@id/profile_offline_view
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
create_profile
friends_profile_empty
friends_profile_empty_add_friends
navigation_profile
profile_add_bio
profile_add_name_and_bio
profile_anonymous_lock_message
profile_anonymous_lock_title
profile_certificates
profile_certificates_completion_description
profile_certificates_completion_title
profile_certificates_professional_description
profile_certificates_professional_title
profile_error
profile_friends_invite_friends_banner_description_offering_pro
profile_friends_offline
profile_offline_description
profile_share_code_learning
profile_share_my_progress
profile_share_stats_title
profile_upgrade
profile_upgrade_try_pro
public_profile_report_user
public_profile_report_user_dialog_content
public_profile_report_user_dialog_header
public_profile_successfully_followed_profile
public_profile_successfully_reported
user_profile
```

## ۴. رنگ‌های مرتبط (فهرست کامل)

(none)

## ۵. دایمنشن‌های مرتبط (فهرست کامل)

```text
com_facebook_profilepictureview_preset_size_large
com_facebook_profilepictureview_preset_size_normal
com_facebook_profilepictureview_preset_size_small
profile_header_avatar_size
```

## ۶. استایل‌های مرتبط (فهرست کامل)

(none)

## ۷. شواهد حالت‌ها (رشته‌های منبع)

```text
friends_profile_empty
friends_profile_empty_add_friends
profile_error
profile_friends_offline
profile_offline_description
profile_upgrade
profile_upgrade_try_pro
```

## ۸. ناوبری / deep link

(هیچ intent-filter/data برای این سطح اعلان نشده)
