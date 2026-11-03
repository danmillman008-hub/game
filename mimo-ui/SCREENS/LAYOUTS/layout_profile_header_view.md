# پروندهٔ لایه — `res/layout/profile_header_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/profile_header_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/profile_header_view.xml`](../../SOURCE/res/layout/profile_header_view.xml) |
| SHA-256 دیکد | `c8b2ba5081245bfdd0ec416d51ddbed643b4990d5ee4cad75eda535543786f1d` |
| ریشه | `merge` |
| تعداد گره | 10 |
| تعداد شناسه | 9 |
| تگ‌های استفاده‌شده | 6 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 6 |
| ارجاع به منابع | 21 |

## ۱. درخت کامل مؤلفه‌ها

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

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `com.google.android.material.imageview.ShapeableImageView` | `android:id` | `@id/iv_settings_user_picture` |
| 2 | `com.google.android.material.imageview.ShapeableImageView` | `android:background` | `@color/background_primary` |
| 3 | `com.google.android.material.imageview.ShapeableImageView` | `android:layout_width` | `@dimen/profile_header_avatar_size` |
| 4 | `com.google.android.material.imageview.ShapeableImageView` | `android:layout_height` | `@dimen/profile_header_avatar_size` |
| 5 | `com.google.android.material.imageview.ShapeableImageView` | `android:layout_marginTop` | `@dimen/spacing_l_expandable` |
| 6 | `com.google.android.material.imageview.ShapeableImageView` | `android:layout_marginBottom` | `@dimen/spacing_m_expandable` |
| 7 | `com.google.android.material.imageview.ShapeableImageView` | `android:scaleType` | `centerCrop` |
| 8 | `com.google.android.material.imageview.ShapeableImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 9 | `com.google.android.material.imageview.ShapeableImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 10 | `com.google.android.material.imageview.ShapeableImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 11 | `com.google.android.material.imageview.ShapeableImageView` | `app:shapeAppearanceOverlay` | `@style/CircularImageView` |
| 12 | `TextView` | `android:id` | `@id/tv_settings_premium_badge` |
| 13 | `TextView` | `android:background` | `@drawable/bg_badge_pro_with_border` |
| 14 | `TextView` | `android:visibility` | `invisible` |
| 15 | `TextView` | `android:layout_marginBottom` | `8.000000dip` |
| 16 | `TextView` | `android:includeFontPadding` | `true` |
| 17 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `@id/iv_settings_user_picture` |
| 18 | `TextView` | `app:layout_constraintEnd_toEndOf` | `@id/iv_settings_user_picture` |
| 19 | `TextView` | `app:layout_constraintStart_toStartOf` | `@id/iv_settings_user_picture` |
| 20 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_settings_user_picture` |
| 21 | `TextView` | `style` | `@style/MimoBadge.Pro` |
| 22 | `TextView` | `android:id` | `@id/tv_settings_max_badge` |
| 23 | `TextView` | `android:visibility` | `invisible` |
| 24 | `TextView` | `android:layout_marginBottom` | `8.000000dip` |
| 25 | `TextView` | `android:includeFontPadding` | `true` |
| 26 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `@id/iv_settings_user_picture` |
| 27 | `TextView` | `app:layout_constraintEnd_toEndOf` | `@id/iv_settings_user_picture` |
| 28 | `TextView` | `app:layout_constraintStart_toStartOf` | `@id/iv_settings_user_picture` |
| 29 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/iv_settings_user_picture` |
| 30 | `TextView` | `style` | `@style/MimoBadge.Max` |
| 31 | `include` | `android:id` | `@id/profile_header_unlocked` |
| 32 | `include` | `android:layout_width` | `0.000000dip` |
| 33 | `include` | `android:layout_height` | `wrap_content` |
| 34 | `include` | `android:layout_marginTop` | `@dimen/spacing_m_expandable` |
| 35 | `include` | `app:layout_constraintEnd_toEndOf` | `0` |
| 36 | `include` | `app:layout_constraintStart_toStartOf` | `0` |
| 37 | `include` | `app:layout_constraintTop_toBottomOf` | `@id/iv_settings_user_picture` |
| 38 | `include` | `layout` | `@layout/profile_header_unlocked` |
| 39 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:id` | `@id/profile_info_card_streak` |
| 40 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_width` | `0.000000dip` |
| 41 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_height` | `wrap_content` |
| 42 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 43 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_marginStart` | `@dimen/spacing_m_expandable` |
| 44 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_marginEnd` | `@dimen/spacing_xs` |
| 45 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `app:layout_constraintEnd_toStartOf` | `@id/profile_info_card_xp` |
| 46 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `app:layout_constraintHorizontal_chainStyle` | `2` |
| 47 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `app:layout_constraintStart_toStartOf` | `0` |
| 48 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `app:layout_constraintTop_toBottomOf` | `@id/profile_header_unlocked` |
| 49 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:id` | `@id/profile_info_card_xp` |
| 50 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_width` | `0.000000dip` |
| 51 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_height` | `wrap_content` |
| 52 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 53 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_marginHorizontal` | `@dimen/spacing_xxs` |
| 54 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `app:layout_constraintEnd_toStartOf` | `@id/profile_info_card_league` |
| 55 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `app:layout_constraintStart_toEndOf` | `@id/profile_info_card_streak` |
| 56 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `app:layout_constraintTop_toBottomOf` | `@id/profile_header_unlocked` |
| 57 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:id` | `@id/profile_info_card_league` |
| 58 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_width` | `0.000000dip` |
| 59 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_height` | `wrap_content` |
| 60 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 61 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_marginStart` | `@dimen/spacing_xs` |
| 62 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_marginEnd` | `@dimen/spacing_m_expandable` |
| 63 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `app:layout_constraintEnd_toEndOf` | `0` |
| 64 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `app:layout_constraintStart_toEndOf` | `@id/profile_info_card_xp` |
| 65 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `app:layout_constraintTop_toBottomOf` | `@id/profile_header_unlocked` |
| 66 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/profile_info_card_longest_streak` |
| 67 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 68 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 69 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 70 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m_expandable` |
| 71 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 72 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 73 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/profile_info_card_streak` |
| 74 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/cw_share_my_progress` |
| 75 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `gone` |
| 76 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 77 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 78 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 79 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 80 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 81 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/profile_info_card_longest_streak` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@dimen/profile_header_avatar_size` | `88.000000dip` |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_l_expandable` | `24.000000dip` / `36.000000dip` (sw600dp) |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@dimen/spacing_xxs` | `4.000000dip` |
| `@style/CircularImageView` | `[{'attr': 'attr.cornerFamily', 'attr_id': '0x7F0401A1', 'value': '0', 'value_type': 'int_dec'}, {'attr': 'attr.cornerSize', 'attr_id': '0x7F0401A8', 'value': '50.000001%', 'value_type': 'fraction'}]` |
| `@style/MimoBadge.Max` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_reversed', 'value_type': 'reference'}, {'attr': 'android:background', 'attr_id': '0x010100D4', 'value': '@drawable/bg_badge_max', 'value_type': 'reference'}, {'attr': 'android:text', 'attr_id': '0x0101014F', 'value': '@string/max', 'value_type': 'reference'}]` |
| `@style/MimoBadge.Pro` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_reversed', 'value_type': 'reference'}, {'attr': 'android:background', 'attr_id': '0x010100D4', 'value': '@drawable/bg_badge_pro', 'value_type': 'reference'}, {'attr': 'android:text', 'attr_id': '0x0101014F', 'value': '@string/pro', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/cw_share_my_progress
@id/iv_settings_user_picture
@id/profile_header_unlocked
@id/profile_info_card_league
@id/profile_info_card_longest_streak
@id/profile_info_card_streak
@id/profile_info_card_xp
@id/tv_settings_max_badge
@id/tv_settings_premium_badge
```

## ۵. ارجاع به لایه‌های دیگر

```text
0
0.000000dip
@dimen/spacing_m_expandable
@id/iv_settings_user_picture
@layout/profile_header_unlocked
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.profile.main.ProfileFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android">
  <com.google.android.material.imageview.ShapeableImageView android:id="@id/iv_settings_user_picture" android:background="@color/background_primary" android:layout_width="@dimen/profile_header_avatar_size" android:layout_height="@dimen/profile_header_avatar_size" android:layout_marginTop="@dimen/spacing_l_expandable" android:layout_marginBottom="@dimen/spacing_m_expandable" android:scaleType="centerCrop" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:shapeAppearanceOverlay="@style/CircularImageView"/>
  <TextView android:id="@id/tv_settings_premium_badge" android:background="@drawable/bg_badge_pro_with_border" android:visibility="invisible" android:layout_marginBottom="8.000000dip" android:includeFontPadding="true" app:layout_constraintBottom_toBottomOf="@id/iv_settings_user_picture" app:layout_constraintEnd_toEndOf="@id/iv_settings_user_picture" app:layout_constraintStart_toStartOf="@id/iv_settings_user_picture" app:layout_constraintTop_toBottomOf="@id/iv_settings_user_picture" style="@style/MimoBadge.Pro"/>
  <TextView android:id="@id/tv_settings_max_badge" android:visibility="invisible" android:layout_marginBottom="8.000000dip" android:includeFontPadding="true" app:layout_constraintBottom_toBottomOf="@id/iv_settings_user_picture" app:layout_constraintEnd_toEndOf="@id/iv_settings_user_picture" app:layout_constraintStart_toStartOf="@id/iv_settings_user_picture" app:layout_constraintTop_toBottomOf="@id/iv_settings_user_picture" style="@style/MimoBadge.Max"/>
  <include android:id="@id/profile_header_unlocked" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m_expandable" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/iv_settings_user_picture" layout="@layout/profile_header_unlocked"/>
  <com.getmimo.ui.profile.view.ProfileInfoCard android:id="@id/profile_info_card_streak" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" android:layout_marginStart="@dimen/spacing_m_expandable" android:layout_marginEnd="@dimen/spacing_xs" app:layout_constraintEnd_toStartOf="@id/profile_info_card_xp" app:layout_constraintHorizontal_chainStyle="2" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/profile_header_unlocked"/>
  <com.getmimo.ui.profile.view.ProfileInfoCard android:id="@id/profile_info_card_xp" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" android:layout_marginHorizontal="@dimen/spacing_xxs" app:layout_constraintEnd_toStartOf="@id/profile_info_card_league" app:layout_constraintStart_toEndOf="@id/profile_info_card_streak" app:layout_constraintTop_toBottomOf="@id/profile_header_unlocked"/>
  <com.getmimo.ui.profile.view.ProfileInfoCard android:id="@id/profile_info_card_league" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" android:layout_marginStart="@dimen/spacing_xs" android:layout_marginEnd="@dimen/spacing_m_expandable" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toEndOf="@id/profile_info_card_xp" app:layout_constraintTop_toBottomOf="@id/profile_header_unlocked"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/profile_info_card_longest_streak" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" android:layout_marginHorizontal="@dimen/spacing_m_expandable" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/profile_info_card_streak"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/cw_share_my_progress" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/profile_info_card_longest_streak"/>
</merge>
```
