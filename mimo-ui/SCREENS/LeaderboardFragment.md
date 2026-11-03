# صفحه — `LeaderboardFragment`

> **خاستگاه ثبت:** `DEX UI_CLASSES.json` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.leaderboard.LeaderboardFragment$observeViewModelEvents$1$1$1` |
| نوع | `dex-ui-class` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose (unresolved per screen)` |
| تعداد لایه‌های متصل | 25 |
| ComposeView | بله |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/chapter_finished_leaderboard_fragment.xml`](../SOURCE/res/layout/chapter_finished_leaderboard_fragment.xml) → [dossier](LAYOUTS/layout_chapter_finished_leaderboard_fragment.md)
- [`res/layout/chapter_finished_leaderboard_joined.xml`](../SOURCE/res/layout/chapter_finished_leaderboard_joined.xml) → [dossier](LAYOUTS/layout_chapter_finished_leaderboard_joined.md)
- [`res/layout/chapter_finished_leaderboard_status.xml`](../SOURCE/res/layout/chapter_finished_leaderboard_status.xml) → [dossier](LAYOUTS/layout_chapter_finished_leaderboard_status.md)
- [`res/layout/fake_leaderboards_result_bottomsheet_dialog.xml`](../SOURCE/res/layout/fake_leaderboards_result_bottomsheet_dialog.xml) → [dossier](LAYOUTS/layout_fake_leaderboards_result_bottomsheet_dialog.md)
- [`res/layout/leaderboard_demotion_divider.xml`](../SOURCE/res/layout/leaderboard_demotion_divider.xml) → [dossier](LAYOUTS/layout_leaderboard_demotion_divider.md)
- [`res/layout/leaderboard_fragment.xml`](../SOURCE/res/layout/leaderboard_fragment.xml) → [dossier](LAYOUTS/layout_leaderboard_fragment.md)
- [`res/layout/leaderboard_fragment_active.xml`](../SOURCE/res/layout/leaderboard_fragment_active.xml) → [dossier](LAYOUTS/layout_leaderboard_fragment_active.md)
- [`res/layout/leaderboard_fragment_locked.xml`](../SOURCE/res/layout/leaderboard_fragment_locked.xml) → [dossier](LAYOUTS/layout_leaderboard_fragment_locked.md)
- [`res/layout/leaderboard_introduction_fragment.xml`](../SOURCE/res/layout/leaderboard_introduction_fragment.xml) → [dossier](LAYOUTS/layout_leaderboard_introduction_fragment.md)
- [`res/layout/leaderboard_item.xml`](../SOURCE/res/layout/leaderboard_item.xml) → [dossier](LAYOUTS/layout_leaderboard_item.md)
- [`res/layout/leaderboard_league_header_item.xml`](../SOURCE/res/layout/leaderboard_league_header_item.xml) → [dossier](LAYOUTS/layout_leaderboard_league_header_item.md)
- [`res/layout/leaderboard_league_header_item_highlighted.xml`](../SOURCE/res/layout/leaderboard_league_header_item_highlighted.xml) → [dossier](LAYOUTS/layout_leaderboard_league_header_item_highlighted.md)
- [`res/layout/leaderboard_league_header_view.xml`](../SOURCE/res/layout/leaderboard_league_header_view.xml) → [dossier](LAYOUTS/layout_leaderboard_league_header_view.md)
- [`res/layout/leaderboard_podium_item.xml`](../SOURCE/res/layout/leaderboard_podium_item.xml) → [dossier](LAYOUTS/layout_leaderboard_podium_item.md)
- [`res/layout/leaderboard_promotion_divider.xml`](../SOURCE/res/layout/leaderboard_promotion_divider.xml) → [dossier](LAYOUTS/layout_leaderboard_promotion_divider.md)
- [`res/layout/leaderboard_result_fragment.xml`](../SOURCE/res/layout/leaderboard_result_fragment.xml) → [dossier](LAYOUTS/layout_leaderboard_result_fragment.md)
- [`res/layout/leaderboard_result_podium_promotion_fragment.xml`](../SOURCE/res/layout/leaderboard_result_podium_promotion_fragment.xml) → [dossier](LAYOUTS/layout_leaderboard_result_podium_promotion_fragment.md)
- [`res/layout/leaderboard_result_podium_promotion_shareable_image.xml`](../SOURCE/res/layout/leaderboard_result_podium_promotion_shareable_image.xml) → [dossier](LAYOUTS/layout_leaderboard_result_podium_promotion_shareable_image.md)
- [`res/layout/leaderboard_result_share_placeholders.xml`](../SOURCE/res/layout/leaderboard_result_share_placeholders.xml) → [dossier](LAYOUTS/layout_leaderboard_result_share_placeholders.md)
- [`res/layout/leaderboard_result_standard_promotion_fragment.xml`](../SOURCE/res/layout/leaderboard_result_standard_promotion_fragment.xml) → [dossier](LAYOUTS/layout_leaderboard_result_standard_promotion_fragment.md)
- [`res/layout/leaderboard_result_standard_promotion_shareable_image.xml`](../SOURCE/res/layout/leaderboard_result_standard_promotion_shareable_image.xml) → [dossier](LAYOUTS/layout_leaderboard_result_standard_promotion_shareable_image.md)
- [`res/layout/leaderboard_result_top_league_neutral_place_fragment.xml`](../SOURCE/res/layout/leaderboard_result_top_league_neutral_place_fragment.xml) → [dossier](LAYOUTS/layout_leaderboard_result_top_league_neutral_place_fragment.md)
- [`res/layout/leaderboard_result_top_league_neutral_place_shareable_image.xml`](../SOURCE/res/layout/leaderboard_result_top_league_neutral_place_shareable_image.xml) → [dossier](LAYOUTS/layout_leaderboard_result_top_league_neutral_place_shareable_image.md)
- [`res/layout/leaderboard_result_top_league_podium_promotion_fragment.xml`](../SOURCE/res/layout/leaderboard_result_top_league_podium_promotion_fragment.xml) → [dossier](LAYOUTS/layout_leaderboard_result_top_league_podium_promotion_fragment.md)
- [`res/layout/leaderboard_result_top_league_podium_promotion_shareable_image.xml`](../SOURCE/res/layout/leaderboard_result_top_league_podium_promotion_shareable_image.xml) → [dossier](LAYOUTS/layout_leaderboard_result_top_league_podium_promotion_shareable_image.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/chapter_finished_leaderboard_fragment.xml`

```text
└─ FrameLayout  #@id/cl_chapter_finished_leaderboard
   ├─ androidx.constraintlayout.widget.ConstraintLayout  #@id/cl_main_content
   │  ├─ FrameLayout  #@id/fl_chapter_finished_leaderboard_container
   │  └─ androidx.compose.ui.platform.ComposeView  #@id/btn_chapter_finished_leaderboard_continue
   └─ ProgressBar  #@id/pb_loading
```

### `res/layout/chapter_finished_leaderboard_joined.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_later
   ├─ app.rive.runtime.kotlin.RiveAnimationView  #@id/iv_chapter_finished_leaderboard_joined_icon
   ├─ TextView  #@id/tv_chapter_finished_leaderboard_joined_title
   └─ TextView  #@id/tv_chapter_finished_leaderboard_joined_description
```

### `res/layout/chapter_finished_leaderboard_status.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ Space  #@id/s_chapter_finished_top_space
   ├─ ImageView  #@id/iv_chapter_finished_leaderboard_status_image
   ├─ TextView  #@id/tv_chapter_finished_leaderboard_status_title
   ├─ TextView  #@id/tv_chapter_finished_leaderboard_status_description
   └─ LinearLayout  #@id/chapter_finished_leaderboard_status_user_container
      ├─ FrameLayout  #@id/fl_chapter_finished_leaderboard_status_1st_place
      │  └─ include  #@id/empty_user_item_1st_place
      ├─ View  #@id/v_chapter_finished_leaderboard_status_1st_place_divider
      ├─ FrameLayout  #@id/fl_chapter_finished_leaderboard_status_2nd_place
      │  └─ include  #@id/current_user_item
      ├─ View  #@id/v_chapter_finished_leaderboard_status_3rd_place_divider
      └─ FrameLayout  #@id/fl_chapter_finished_leaderboard_status_3rd_place
         └─ include  #@id/empty_user_item_3rd_place
```

### `res/layout/fake_leaderboards_result_bottomsheet_dialog.xml`

```text
└─ LinearLayout
   ├─ TextView
   ├─ com.google.android.material.textfield.TextInputLayout
   │  └─ com.google.android.material.textfield.TextInputEditText  #@id/et_fake_leaderboards_result_rank
   ├─ com.google.android.material.textfield.TextInputLayout
   │  └─ com.google.android.material.textfield.TextInputEditText  #@id/et_fake_leaderboards_result_league
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_fake_leaderboards_result
```

### `res/layout/leaderboard_demotion_divider.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_leaderboard_demotion_divider
   ├─ View  #@id/view_leaderboard_demotion_divider_start
   └─ View  #@id/view_leaderboard_demotion_divider_end
```

### `res/layout/leaderboard_fragment.xml`

```text
└─ androidx.coordinatorlayout.widget.CoordinatorLayout  #@id/root_leaderboard_fragment
   ├─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_leaderboard
   │  └─ include  #@id/layout_toolbar
   └─ FrameLayout
      ├─ com.getmimo.ui.components.common.OfflineView  #@id/layout_leaderboard_offline
      ├─ ProgressBar  #@id/pb_leaderboard_loading_progress
      ├─ include  #@id/layout_leaderboard_locked
      ├─ include  #@id/layout_leaderboard_active
      └─ com.getmimo.ui.authentication.lock.AnonymousUserFeatureLockedView  #@id/anonymous_user_lock_view
```

### `res/layout/leaderboard_fragment_active.xml`

```text
└─ LinearLayout
   ├─ com.getmimo.ui.leaderboard.LeaderboardLeagueHeaderView  #@id/leaderboard_league_header_view
   └─ androidx.swiperefreshlayout.widget.SwipeRefreshLayout  #@id/srl_leaderboard_refresh_layout
      └─ androidx.recyclerview.widget.RecyclerView  #@id/rv_leaderboard
```

### `res/layout/leaderboard_fragment_locked.xml`

```text
└─ LinearLayout
   ├─ com.getmimo.ui.leaderboard.LeaderboardLeagueHeaderView  #@id/leaderboard_league_header_view_locked
   ├─ Space
   ├─ ImageView  #@id/iv_leaderboard_fragment_locked_illustration
   ├─ TextView  #@id/tv_leaderboard_fragment_locked_header
   ├─ TextView  #@id/tv_leaderboard_fragment_locked_message
   ├─ Space
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_leaderboard_fragment_locked_jump_into_lesson
```

### `res/layout/leaderboard_introduction_fragment.xml`

```text
└─ FrameLayout
   └─ androidx.constraintlayout.widget.ConstraintLayout
      ├─ ImageView  #@id/iv_leaderboard_intro_image
      ├─ TextView  #@id/iv_leaderboard_intro_title
      ├─ TextView  #@id/iv_leaderboard_intro_subtitle
      ├─ androidx.constraintlayout.widget.ConstraintLayout  #@id/cl_leaderboard_intro_details_container
      │  ├─ ImageView  #@id/iv_leaderboard_into_league_image
      │  ├─ TextView  #@id/tv_leaderboard_into_league_title
      │  ├─ TextView  #@id/tv_leaderboard_into_league_subtitle
      │  ├─ ImageView  #@id/iv_leaderboard_into_time_image
      │  ├─ TextView  #@id/tv_leaderboard_into_time_title
      │  └─ TextView
      └─ androidx.compose.ui.platform.ComposeView  #@id/mb_leaderboard_into_got_it
```

### `res/layout/leaderboard_item.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/root_leaderboard_podium_item
   ├─ TextView  #@id/tv_rank_leaderboard_item
   ├─ ImageView  #@id/iv_avatar_leaderboard_item
   ├─ TextView  #@id/tv_username_leaderboard_item
   ├─ TextView  #@id/tv_sparks_leaderboard_item
   └─ ImageView  #@id/iv_sparks_leaderboard_item
```

### `res/layout/leaderboard_league_header_item.xml`

```text
└─ FrameLayout
   └─ ImageView  #@id/iv_leaderboard_league_header_item
```

### `res/layout/leaderboard_league_header_item_highlighted.xml`

```text
└─ FrameLayout
   └─ ImageView  #@id/iv_leaderboard_league_header_item_highlighted
```

### `res/layout/leaderboard_league_header_view.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ FrameLayout  #@id/frameLayout
   │  └─ androidx.recyclerview.widget.RecyclerView  #@id/rv_leaderboard_result_leagues
   ├─ TextView  #@id/tv_leaderboard_results_league_label
   └─ TextView  #@id/tv_leaderboard_header_results_available_timer
```

### `res/layout/leaderboard_podium_item.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/root_leaderboard_podium_item
   ├─ ImageView  #@id/iv_medal_leaderboard_podium_item
   ├─ ImageView  #@id/iv_avatar_leaderboard_podium_item
   ├─ TextView  #@id/tv_username_leaderboard_podium_item
   ├─ TextView  #@id/tv_sparks_leaderboard_podium_item
   └─ ImageView  #@id/iv_sparks_leaderboard_podium_item
```

### `res/layout/leaderboard_promotion_divider.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_leaderboard_promotion_divider
   ├─ View  #@id/view_leaderboard_promotion_divider_start
   └─ View  #@id/view_leaderboard_promotion_divider_end
```

### `res/layout/leaderboard_result_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ FrameLayout  #@id/iv_leaderboard_result_illustration_header
   │  ├─ ImageView  #@id/iv_leaderboard_result_illustration_neutral
   │  └─ androidx.constraintlayout.widget.ConstraintLayout  #@id/container_leaderboard_result_illustration_demotion
   │     ├─ ImageView  #@id/iv_leaderboard_result_illustration_demotion_league
   │     └─ ImageView  #@id/iv_leaderboard_result_illustration_demotion_indicator
   ├─ TextView  #@id/tv_leaderboard_result_time
   ├─ TextView  #@id/tv_leaderboard_result_header
   ├─ TextView  #@id/tv_leaderboard_result_message
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_leaderboard_result_continue
```

### `res/layout/leaderboard_result_podium_promotion_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_leaderboard_result_time
   ├─ androidx.constraintlayout.widget.ConstraintLayout  #@id/container_leaderboard_result_illustration_podium
   │  ├─ ImageView  #@id/iv_leaderboard_result_illustration_podium
   │  └─ ImageView  #@id/iv_leaderboard_result_illustration_podium_league
   ├─ TextView  #@id/tv_leaderboard_result_header
   ├─ TextView  #@id/tv_leaderboard_result_message
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_share
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_leaderboard_result_continue
```

### `res/layout/leaderboard_result_podium_promotion_shareable_image.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_shareable_image
   ├─ ImageView  #@id/iv_mimo_logo
   ├─ TextView  #@id/tv_leaderboard_result_time
   ├─ androidx.constraintlayout.widget.ConstraintLayout  #@id/container_leaderboard_result_illustration_podium
   │  ├─ ImageView  #@id/iv_leaderboard_result_illustration_podium
   │  └─ ImageView  #@id/iv_leaderboard_result_illustration_podium_league
   ├─ TextView  #@id/tv_leaderboard_result_header
   ├─ TextView  #@id/tv_leaderboard_result_message
   └─ TextView  #@id/tv_mimo_app_link
```

### `res/layout/leaderboard_result_share_placeholders.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ View  #@id/placeholder_3
   ├─ View  #@id/placeholder_4
   ├─ View  #@id/placeholder_5
   ├─ View  #@id/placeholder_6
   ├─ View  #@id/placeholder_7
   ├─ View  #@id/placeholder_8
   ├─ View  #@id/placeholder_1
   └─ View  #@id/placeholder_2
```

### `res/layout/leaderboard_result_standard_promotion_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_leaderboard_result_time
   ├─ androidx.constraintlayout.widget.ConstraintLayout  #@id/constraintLayout
   │  ├─ ImageView  #@id/iv_leaderboard_result_illustration_promotion_league
   │  ├─ ImageView  #@id/iv_leaderboard_result_illustration_promotion_indicator
   │  ├─ TextView  #@id/tv_leaderboard_result_header
   │  └─ TextView  #@id/tv_leaderboard_result_message
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_share
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_leaderboard_result_continue
```

### `res/layout/leaderboard_result_standard_promotion_shareable_image.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_shareable_image
   ├─ ImageView  #@id/iv_mimo_logo
   ├─ TextView  #@id/tv_leaderboard_result_time
   ├─ ImageView  #@id/iv_leaderboard_result_illustration_promotion_league
   ├─ ImageView  #@id/iv_leaderboard_result_illustration_promotion_indicator
   ├─ TextView  #@id/tv_leaderboard_result_header
   ├─ TextView  #@id/tv_leaderboard_result_message
   └─ TextView  #@id/tv_mimo_app_link
```

### `res/layout/leaderboard_result_top_league_neutral_place_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_leaderboard_result_time
   ├─ ImageView  #@id/iv_leaderboard_result_illustration_neutral
   ├─ TextView  #@id/tv_leaderboard_result_header
   ├─ TextView  #@id/tv_leaderboard_result_message
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_share
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_leaderboard_result_continue
```

### `res/layout/leaderboard_result_top_league_neutral_place_shareable_image.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_shareable_image
   ├─ ImageView  #@id/iv_mimo_logo
   ├─ TextView  #@id/tv_leaderboard_result_time
   ├─ ImageView  #@id/iv_leaderboard_result_illustration_neutral
   ├─ TextView  #@id/tv_leaderboard_result_header
   ├─ TextView  #@id/tv_leaderboard_result_message
   └─ TextView  #@id/tv_mimo_app_link
```

### `res/layout/leaderboard_result_top_league_podium_promotion_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_leaderboard_result_time
   ├─ androidx.constraintlayout.widget.ConstraintLayout  #@id/container_leaderboard_result_illustration_podium
   │  ├─ ImageView  #@id/iv_leaderboard_result_illustration_podium
   │  └─ ImageView  #@id/iv_leaderboard_result_illustration_podium_league
   ├─ TextView  #@id/tv_leaderboard_result_header
   ├─ TextView  #@id/tv_leaderboard_result_message
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_share
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_leaderboard_result_continue
```

### `res/layout/leaderboard_result_top_league_podium_promotion_shareable_image.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_shareable_image
   ├─ ImageView  #@id/iv_mimo_logo
   ├─ TextView  #@id/tv_leaderboard_result_time
   ├─ androidx.constraintlayout.widget.ConstraintLayout  #@id/container_leaderboard_result_illustration_podium
   │  ├─ ImageView  #@id/iv_leaderboard_result_illustration_podium
   │  └─ ImageView  #@id/iv_leaderboard_result_illustration_podium_league
   ├─ TextView  #@id/tv_leaderboard_result_header
   ├─ TextView  #@id/tv_leaderboard_result_message
   └─ TextView  #@id/tv_mimo_app_link
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
chapter_end_screen_leaderboard_joined_description
chapter_end_screen_leaderboard_joined_title
chapter_end_screen_leaderboard_status_description_danger
chapter_end_screen_leaderboard_status_description_demotion
chapter_end_screen_leaderboard_status_description_highest_league
chapter_end_screen_leaderboard_status_description_neutral
chapter_end_screen_leaderboard_status_description_promotion
chapter_end_screen_leaderboard_status_description_protection
chapter_end_screen_leaderboard_status_description_top
chapter_end_screen_leaderboard_status_title
developer_menu_fake_leaderboards_result
leaderboard_ask_for_name_title
leaderboard_demotion_zone
leaderboard_into_league_subtitle
leaderboard_into_league_title
leaderboard_into_subtitle
leaderboard_into_time_subtitle
leaderboard_into_time_title
leaderboard_into_title
leaderboard_league_name_1
leaderboard_league_name_2
leaderboard_league_name_3
leaderboard_league_name_4
leaderboard_league_name_5
leaderboard_league_short_name_1
leaderboard_league_short_name_2
leaderboard_league_short_name_3
leaderboard_league_short_name_4
leaderboard_league_short_name_5
leaderboard_offline_message
leaderboard_promotion_zone
leaderboard_result_header_demotion
leaderboard_result_header_keep_it_up
leaderboard_result_header_protection
leaderboard_result_message
leaderboard_result_message_demotion
leaderboard_result_message_neutral_position
leaderboard_result_message_podium_top_league_promotion_share
leaderboard_result_message_promotion
leaderboard_result_message_promotion_share
leaderboard_result_message_protection
leaderboard_result_message_top_league
leaderboard_result_promotion_share_result
leaderboard_result_title_podium_promotion_share
leaderboard_result_title_promotion_share
leaderboard_trophies_title
leaderboard_unlock_header_more_lessons
leaderboard_unlock_header_signup
leaderboard_unlock_message_more_lessons
leaderboard_unlock_message_signup
navigation_leaderboard
```

## ۴. رنگ‌های مرتبط (فهرست کامل)

(none)

## ۵. دایمنشن‌های مرتبط (فهرست کامل)

```text
leaderboard_item_icon_margin_start
leaderboard_item_name_margin_start
leaderboard_item_ranking_margin_start
leaderboard_item_sparks_margin_end
leaderboard_league_header_height
leaderboard_league_header_item_height
leaderboard_league_header_item_selected_height
leaderboard_league_header_item_selected_width
leaderboard_league_header_item_width
```

## ۶. استایل‌های مرتبط (فهرست کامل)

(none)

## ۷. شواهد حالت‌ها (رشته‌های منبع)

```text
leaderboard_offline_message
```

## ۸. ناوبری / deep link

(هیچ intent-filter/data برای این سطح اعلان نشده)
