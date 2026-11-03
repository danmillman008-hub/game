# پروندهٔ لایه — `res/layout/streak_bottom_sheet_content.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/streak_bottom_sheet_content.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/streak_bottom_sheet_content.xml`](../../SOURCE/res/layout/streak_bottom_sheet_content.xml) |
| SHA-256 دیکد | `158907b85ca7942889b3455460f4fe83fd757ea362212500c05ec3ac43338286` |
| ریشه | `merge` |
| تعداد گره | 17 |
| تعداد شناسه | 14 |
| تگ‌های استفاده‌شده | 14 |
| ویوهای سفارشی `com.getmimo` | 3 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 34 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   ├─ com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView  #@id/anonymous_user_lock_view
   ├─ com.getmimo.ui.components.common.OfflineView  #@id/offline_view
   └─ androidx.core.widget.NestedScrollView  #@id/calendar_content_scroll_view
      └─ androidx.constraintlayout.widget.ConstraintLayout
         ├─ ImageView  #@id/ib_calendar_previous_month
         ├─ TextView  #@id/tv_calendar_month_name
         ├─ ImageButton  #@id/ib_calendar_next_month
         ├─ GridView  #@id/gv_calendar_header
         ├─ androidx.recyclerview.widget.RecyclerView  #@id/rv_calendar
         ├─ androidx.constraintlayout.widget.Guideline  #@id/guideline_layout_vertical_middle
         ├─ View
         ├─ androidx.compose.ui.platform.ComposeView  #@id/info_card_streak_challenge
         ├─ com.getmimo.ui.profile.view.ProfileInfoCard  #@id/info_card_streak
         ├─ com.getmimo.ui.profile.view.ProfileInfoCard  #@id/info_card_xp
         ├─ com.getmimo.ui.profile.view.ProfileInfoCard  #@id/info_card_league
         └─ androidx.compose.ui.platform.ComposeView  #@id/info_card_longest_streak
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `android:id` | `@id/anonymous_user_lock_view` |
| 2 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `android:visibility` | `gone` |
| 3 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `android:layout_width` | `match_parent` |
| 4 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `android:layout_height` | `match_parent` |
| 5 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 6 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 7 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `app:layout_constraintStart_toStartOf` | `0` |
| 8 | `com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView` | `app:layout_constraintTop_toBottomOf` | `@id/cv_bottom_sheet_header` |
| 9 | `com.getmimo.ui.components.common.OfflineView` | `android:id` | `@id/offline_view` |
| 10 | `com.getmimo.ui.components.common.OfflineView` | `android:visibility` | `gone` |
| 11 | `com.getmimo.ui.components.common.OfflineView` | `android:layout_width` | `match_parent` |
| 12 | `com.getmimo.ui.components.common.OfflineView` | `android:layout_height` | `match_parent` |
| 13 | `com.getmimo.ui.components.common.OfflineView` | `android:layout_marginTop` | `@dimen/spacing_xl` |
| 14 | `com.getmimo.ui.components.common.OfflineView` | `android:layout_marginBottom` | `@dimen/spacing_xl` |
| 15 | `com.getmimo.ui.components.common.OfflineView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 16 | `com.getmimo.ui.components.common.OfflineView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 17 | `com.getmimo.ui.components.common.OfflineView` | `app:layout_constraintStart_toStartOf` | `0` |
| 18 | `com.getmimo.ui.components.common.OfflineView` | `app:layout_constraintTop_toBottomOf` | `@id/cv_bottom_sheet_header` |
| 19 | `com.getmimo.ui.components.common.OfflineView` | `app:offline_description` | `@string/activity_offline_description` |
| 20 | `androidx.core.widget.NestedScrollView` | `android:id` | `@id/calendar_content_scroll_view` |
| 21 | `androidx.core.widget.NestedScrollView` | `android:layout_width` | `0.000000dip` |
| 22 | `androidx.core.widget.NestedScrollView` | `android:layout_height` | `wrap_content` |
| 23 | `androidx.core.widget.NestedScrollView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 24 | `androidx.core.widget.NestedScrollView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 25 | `androidx.core.widget.NestedScrollView` | `app:layout_constraintStart_toStartOf` | `0` |
| 26 | `androidx.core.widget.NestedScrollView` | `app:layout_constraintTop_toBottomOf` | `@id/cv_bottom_sheet_header` |
| 27 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 28 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 29 | `ImageView` | `android:id` | `@id/ib_calendar_previous_month` |
| 30 | `ImageView` | `android:background` | `?attr/selectableItemBackgroundBorderless` |
| 31 | `ImageView` | `android:layout_width` | `@dimen/icon_size_large_expandable` |
| 32 | `ImageView` | `android:layout_height` | `@dimen/icon_size_large_expandable` |
| 33 | `ImageView` | `android:layout_marginTop` | `@dimen/spacing_l_expandable` |
| 34 | `ImageView` | `android:src` | `@drawable/ic_chevron_left` |
| 35 | `ImageView` | `android:layout_marginStart` | `@dimen/spacing_s_expandable` |
| 36 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 37 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 38 | `ImageView` | `app:tint` | `@color/calendar_button_tint_selector` |
| 39 | `TextView` | `android:textColor` | `@color/text_primary` |
| 40 | `TextView` | `android:gravity` | `0x00000001` |
| 41 | `TextView` | `android:layout_gravity` | `0x00000010` |
| 42 | `TextView` | `android:id` | `@id/tv_calendar_month_name` |
| 43 | `TextView` | `android:layout_width` | `0.000000dip` |
| 44 | `TextView` | `android:layout_height` | `wrap_content` |
| 45 | `TextView` | `android:layout_weight` | `1.000000` |
| 46 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `@id/ib_calendar_previous_month` |
| 47 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 48 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 49 | `TextView` | `app:layout_constraintTop_toTopOf` | `@id/ib_calendar_previous_month` |
| 50 | `TextView` | `style` | `@style/TextH3` |
| 51 | `ImageButton` | `android:enabled` | `false` |
| 52 | `ImageButton` | `android:id` | `@id/ib_calendar_next_month` |
| 53 | `ImageButton` | `android:background` | `?0x0101045C` |
| 54 | `ImageButton` | `android:layout_width` | `@dimen/icon_size_large_expandable` |
| 55 | `ImageButton` | `android:layout_height` | `@dimen/icon_size_large_expandable` |
| 56 | `ImageButton` | `android:src` | `@drawable/ic_chevron_right` |
| 57 | `ImageButton` | `android:layout_marginEnd` | `@dimen/spacing_s_expandable` |
| 58 | `ImageButton` | `app:layout_constraintEnd_toEndOf` | `0` |
| 59 | `ImageButton` | `app:layout_constraintTop_toTopOf` | `@id/ib_calendar_previous_month` |
| 60 | `ImageButton` | `app:tint` | `@color/calendar_button_tint_selector` |
| 61 | `GridView` | `android:gravity` | `0x00000011` |
| 62 | `GridView` | `android:id` | `@id/gv_calendar_header` |
| 63 | `GridView` | `android:layout_width` | `0.000000dip` |
| 64 | `GridView` | `android:layout_height` | `wrap_content` |
| 65 | `GridView` | `android:layout_marginTop` | `@dimen/spacing_m_expandable` |
| 66 | `GridView` | `android:stretchMode` | `2` |
| 67 | `GridView` | `android:numColumns` | `7` |
| 68 | `GridView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 69 | `GridView` | `app:layout_constraintStart_toStartOf` | `0` |
| 70 | `GridView` | `app:layout_constraintTop_toBottomOf` | `@id/ib_calendar_previous_month` |
| 71 | `androidx.recyclerview.widget.RecyclerView` | `android:id` | `@id/rv_calendar` |
| 72 | `androidx.recyclerview.widget.RecyclerView` | `android:paddingBottom` | `@dimen/spacing_s_expandable` |
| 73 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_width` | `0.000000dip` |
| 74 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_height` | `wrap_content` |
| 75 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 76 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintStart_toStartOf` | `0` |
| 77 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintTop_toBottomOf` | `@id/gv_calendar_header` |
| 78 | `androidx.constraintlayout.widget.Guideline` | `android:orientation` | `vertical` |
| 79 | `androidx.constraintlayout.widget.Guideline` | `android:id` | `@id/guideline_layout_vertical_middle` |
| 80 | `androidx.constraintlayout.widget.Guideline` | `android:layout_width` | `wrap_content` |
| 81 | `androidx.constraintlayout.widget.Guideline` | `android:layout_height` | `wrap_content` |
| 82 | `androidx.constraintlayout.widget.Guideline` | `app:layout_constraintGuide_percent` | `0.500000` |
| 83 | `View` | `android:background` | `@color/background_primary` |
| 84 | `View` | `android:layout_width` | `match_parent` |
| 85 | `View` | `android:layout_height` | `0.000000dip` |
| 86 | `View` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 87 | `View` | `app:layout_constraintTop_toBottomOf` | `@id/rv_calendar` |
| 88 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/info_card_streak_challenge` |
| 89 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 90 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 91 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 92 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 93 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 94 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 95 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/rv_calendar` |
| 96 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:id` | `@id/info_card_streak` |
| 97 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_width` | `0.000000dip` |
| 98 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_height` | `wrap_content` |
| 99 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 100 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 101 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_marginEnd` | `@dimen/spacing_xs` |
| 102 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `app:layout_constraintEnd_toStartOf` | `@id/info_card_xp` |
| 103 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `app:layout_constraintHorizontal_chainStyle` | `2` |
| 104 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `app:layout_constraintStart_toStartOf` | `0` |
| 105 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `app:layout_constraintTop_toBottomOf` | `@id/info_card_streak_challenge` |
| 106 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `app:layout_goneMarginTop` | `@dimen/spacing_m` |
| 107 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:id` | `@id/info_card_xp` |
| 108 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_width` | `0.000000dip` |
| 109 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_height` | `wrap_content` |
| 110 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 111 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_marginHorizontal` | `@dimen/spacing_xxs` |
| 112 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `app:layout_constraintEnd_toStartOf` | `@id/info_card_league` |
| 113 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `app:layout_constraintStart_toEndOf` | `@id/info_card_streak` |
| 114 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `app:layout_constraintTop_toBottomOf` | `@id/info_card_streak_challenge` |
| 115 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `app:layout_goneMarginTop` | `@dimen/spacing_m` |
| 116 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:id` | `@id/info_card_league` |
| 117 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_width` | `0.000000dip` |
| 118 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_height` | `wrap_content` |
| 119 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 120 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_marginStart` | `@dimen/spacing_xs` |
| 121 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `android:layout_marginEnd` | `@dimen/spacing_m` |
| 122 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `app:layout_constraintEnd_toEndOf` | `0` |
| 123 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `app:layout_constraintStart_toEndOf` | `@id/info_card_xp` |
| 124 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `app:layout_constraintTop_toBottomOf` | `@id/info_card_streak_challenge` |
| 125 | `com.getmimo.ui.profile.view.ProfileInfoCard` | `app:layout_goneMarginTop` | `@dimen/spacing_m` |
| 126 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/info_card_longest_streak` |
| 127 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 128 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 129 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 130 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/spacing_l` |
| 131 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 132 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 133 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 134 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 135 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/info_card_streak` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/calendar_button_tint_selector` | `res/color/calendar_button_tint_selector.xml` |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/icon_size_large_expandable` | `24.000000dip` / `32.000000dip` (sw600dp) |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_l_expandable` | `24.000000dip` / `36.000000dip` (sw600dp) |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_s_expandable` | `12.000000dip` / `16.000000dip` (sw600dp) |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@dimen/spacing_xxs` | `4.000000dip` |
| `@string/activity_offline_description` | `Connect to the internet to see your activity` / `Verbinde dich mit dem Internet, um deine Aktivität zu sehen` (de) / `Conéctate a internet para ver tu actividad` (es) / `Connecte-toi à internet pour voir ta progression` (fr) / `Sambungkan ke internet untuk melihat aktivitasmu` (in) / `Connettiti a internet per vedere la tua attività` (it) / `Połącz się z internetem, aby zobaczyć swoją aktywność` (pl) / `Conecte-se à Internet para ver sua atividade` (pt-rBR) / `Подключись к интернету, чтобы посмотреть активность` (ru) / `Etkinliğini görmek için internete bağlan` (tr) |
| `@style/TextH3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/anonymous_user_lock_view
@id/calendar_content_scroll_view
@id/guideline_layout_vertical_middle
@id/gv_calendar_header
@id/ib_calendar_next_month
@id/ib_calendar_previous_month
@id/info_card_league
@id/info_card_longest_streak
@id/info_card_streak
@id/info_card_streak_challenge
@id/info_card_xp
@id/offline_view
@id/rv_calendar
@id/tv_calendar_month_name
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.streaks.bottomsheet.StreakBottomSheetFragment$configureRecyclerView$2
com.getmimo.ui.streaks.bottomsheet.StreakBottomSheetFragment$configureRecyclerView$3
com.getmimo.ui.streaks.bottomsheet.StreakBottomSheetFragment$configureRecyclerView$4
com.getmimo.ui.streaks.bottomsheet.StreakBottomSheetFragment$configureRecyclerView$5
com.getmimo.ui.streaks.bottomsheet.StreakBottomSheetFragment$configureRecyclerView$streakMonthAdapter$1
com.getmimo.ui.streaks.bottomsheet.StreakBottomSheetFragment$onViewCreated$1
com.getmimo.ui.streaks.bottomsheet.StreakBottomSheetFragment$onViewCreated$1$1
com.getmimo.ui.streaks.bottomsheet.StreakBottomSheetFragment$onViewCreated$2
com.getmimo.ui.streaks.bottomsheet.StreakBottomSheetFragment$onViewCreated$2$1
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<merge xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto">
  <com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView android:id="@id/anonymous_user_lock_view" android:visibility="gone" android:layout_width="match_parent" android:layout_height="match_parent" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/cv_bottom_sheet_header"/>
  <com.getmimo.ui.components.common.OfflineView android:id="@id/offline_view" android:visibility="gone" android:layout_width="match_parent" android:layout_height="match_parent" android:layout_marginTop="@dimen/spacing_xl" android:layout_marginBottom="@dimen/spacing_xl" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/cv_bottom_sheet_header" app:offline_description="@string/activity_offline_description"/>
  <androidx.core.widget.NestedScrollView android:id="@id/calendar_content_scroll_view" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/cv_bottom_sheet_header">
    <androidx.constraintlayout.widget.ConstraintLayout android:layout_width="match_parent" android:layout_height="wrap_content">
      <ImageView android:id="@id/ib_calendar_previous_month" android:background="?attr/selectableItemBackgroundBorderless" android:layout_width="@dimen/icon_size_large_expandable" android:layout_height="@dimen/icon_size_large_expandable" android:layout_marginTop="@dimen/spacing_l_expandable" android:src="@drawable/ic_chevron_left" android:layout_marginStart="@dimen/spacing_s_expandable" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:tint="@color/calendar_button_tint_selector"/>
      <TextView android:textColor="@color/text_primary" android:gravity="0x00000001" android:layout_gravity="0x00000010" android:id="@id/tv_calendar_month_name" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_weight="1.000000" app:layout_constraintBottom_toBottomOf="@id/ib_calendar_previous_month" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="@id/ib_calendar_previous_month" style="@style/TextH3"/>
      <ImageButton android:enabled="false" android:id="@id/ib_calendar_next_month" android:background="?0x0101045C" android:layout_width="@dimen/icon_size_large_expandable" android:layout_height="@dimen/icon_size_large_expandable" android:src="@drawable/ic_chevron_right" android:layout_marginEnd="@dimen/spacing_s_expandable" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="@id/ib_calendar_previous_month" app:tint="@color/calendar_button_tint_selector"/>
      <GridView android:gravity="0x00000011" android:id="@id/gv_calendar_header" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m_expandable" android:stretchMode="2" android:numColumns="7" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/ib_calendar_previous_month"/>
      <androidx.recyclerview.widget.RecyclerView android:id="@id/rv_calendar" android:paddingBottom="@dimen/spacing_s_expandable" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/gv_calendar_header"/>
      <androidx.constraintlayout.widget.Guideline android:orientation="vertical" android:id="@id/guideline_layout_vertical_middle" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintGuide_percent="0.500000"/>
      <View android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="0.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintTop_toBottomOf="@id/rv_calendar"/>
      <androidx.compose.ui.platform.ComposeView android:id="@id/info_card_streak_challenge" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/rv_calendar"/>
      <com.getmimo.ui.profile.view.ProfileInfoCard android:id="@id/info_card_streak" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" android:layout_marginStart="@dimen/spacing_m" android:layout_marginEnd="@dimen/spacing_xs" app:layout_constraintEnd_toStartOf="@id/info_card_xp" app:layout_constraintHorizontal_chainStyle="2" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/info_card_streak_challenge" app:layout_goneMarginTop="@dimen/spacing_m"/>
      <com.getmimo.ui.profile.view.ProfileInfoCard android:id="@id/info_card_xp" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" android:layout_marginHorizontal="@dimen/spacing_xxs" app:layout_constraintEnd_toStartOf="@id/info_card_league" app:layout_constraintStart_toEndOf="@id/info_card_streak" app:layout_constraintTop_toBottomOf="@id/info_card_streak_challenge" app:layout_goneMarginTop="@dimen/spacing_m"/>
      <com.getmimo.ui.profile.view.ProfileInfoCard android:id="@id/info_card_league" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" android:layout_marginStart="@dimen/spacing_xs" android:layout_marginEnd="@dimen/spacing_m" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toEndOf="@id/info_card_xp" app:layout_constraintTop_toBottomOf="@id/info_card_streak_challenge" app:layout_goneMarginTop="@dimen/spacing_m"/>
      <androidx.compose.ui.platform.ComposeView android:id="@id/info_card_longest_streak" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" android:layout_marginBottom="@dimen/spacing_l" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/info_card_streak"/>
    </androidx.constraintlayout.widget.ConstraintLayout>
  </androidx.core.widget.NestedScrollView>
</merge>
```
