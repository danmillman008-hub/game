# صفحه — `ChapterActivity`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.chapter.ChapterActivity` |
| نوع | `activity` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `@style/MaterialDarkModeTheme` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose (unresolved per screen)` |
| تعداد لایه‌های متصل | 11 |
| ComposeView | بله |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/chapter_activity.xml`](../SOURCE/res/layout/chapter_activity.xml) → [dossier](LAYOUTS/layout_chapter_activity.md)
- [`res/layout/chapter_end_native_ads_fragment.xml`](../SOURCE/res/layout/chapter_end_native_ads_fragment.xml) → [dossier](LAYOUTS/layout_chapter_end_native_ads_fragment.md)
- [`res/layout/chapter_end_set_reminder_time_fragment.xml`](../SOURCE/res/layout/chapter_end_set_reminder_time_fragment.xml) → [dossier](LAYOUTS/layout_chapter_end_set_reminder_time_fragment.md)
- [`res/layout/chapter_finished_fragment.xml`](../SOURCE/res/layout/chapter_finished_fragment.xml) → [dossier](LAYOUTS/layout_chapter_finished_fragment.md)
- [`res/layout/chapter_finished_leaderboard_fragment.xml`](../SOURCE/res/layout/chapter_finished_leaderboard_fragment.xml) → [dossier](LAYOUTS/layout_chapter_finished_leaderboard_fragment.md)
- [`res/layout/chapter_finished_leaderboard_joined.xml`](../SOURCE/res/layout/chapter_finished_leaderboard_joined.xml) → [dossier](LAYOUTS/layout_chapter_finished_leaderboard_joined.md)
- [`res/layout/chapter_finished_leaderboard_status.xml`](../SOURCE/res/layout/chapter_finished_leaderboard_status.xml) → [dossier](LAYOUTS/layout_chapter_finished_leaderboard_status.md)
- [`res/layout/chapter_finished_share_streak_layout_shareable_image.xml`](../SOURCE/res/layout/chapter_finished_share_streak_layout_shareable_image.xml) → [dossier](LAYOUTS/layout_chapter_finished_share_streak_layout_shareable_image.md)
- [`res/layout/chapter_finished_streak_fragment.xml`](../SOURCE/res/layout/chapter_finished_streak_fragment.xml) → [dossier](LAYOUTS/layout_chapter_finished_streak_fragment.md)
- [`res/layout/chapter_finished_widget_intro_fragment.xml`](../SOURCE/res/layout/chapter_finished_widget_intro_fragment.xml) → [dossier](LAYOUTS/layout_chapter_finished_widget_intro_fragment.md)
- [`res/layout/chapter_toolbar.xml`](../SOURCE/res/layout/chapter_toolbar.xml) → [dossier](LAYOUTS/layout_chapter_toolbar.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/chapter_activity.xml`

```text
└─ FrameLayout  #@id/chapter_activity_root
   ├─ androidx.compose.ui.platform.ComposeView  #@id/compose_view
   └─ androidx.coordinatorlayout.widget.CoordinatorLayout
      ├─ androidx.viewpager2.widget.ViewPager2  #@id/vp_lessons
      ├─ androidx.fragment.app.FragmentContainerView  #@id/layout_chapter_finished_share_fragment
      └─ com.google.android.material.appbar.AppBarLayout  #@id/chapter_appbarlayout
         └─ com.getmimo.ui.chapter.view.ChapterToolbar  #@id/chapter_toolbar
```

### `res/layout/chapter_end_native_ads_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_ads_modal_title
   ├─ com.google.android.material.progressindicator.CircularProgressIndicator  #@id/cpi_countdown_timer
   ├─ TextView  #@id/tv_seconds_timer_close
   ├─ ImageButton  #@id/iv_ads_modal_close
   ├─ TextView  #@id/tv_ads_keep_mimo_free
   ├─ TextView  #@id/tv_subscribe_to_mimo_pro
   ├─ androidx.cardview.widget.CardView  #@id/card_view_ads_modal_content
   │  └─ com.google.android.gms.ads.nativead.NativeAdView  #@id/layout_adview
   │     └─ androidx.constraintlayout.widget.ConstraintLayout
   │        ├─ com.google.android.gms.ads.nativead.MediaView  #@id/mv_ads_modal_content
   │        ├─ ImageView  #@id/iv_ads_modal_content
   │        ├─ ImageView  #@id/iv_ads_modal_content_app_icon
   │        ├─ TextView  #@id/tv_ads_modal_content_title
   │        ├─ TextView  #@id/tv_ads_modal_content_description
   │        └─ com.google.android.material.button.MaterialButton  #@id/btn_cta
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_ads_modal_remove_ads
   └─ FrameLayout  #@id/layout_loading_ad
      └─ ProgressBar  #@id/progress_bar_loading_ads
```

### `res/layout/chapter_end_set_reminder_time_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_set_reminder_time_title
   ├─ TextView  #@id/tv_set_reminder_time
   ├─ TextView  #@id/tv_onboarding_step_header
   ├─ app.rive.runtime.kotlin.RiveAnimationView  #@id/iv_set_reminder_time
   ├─ TextView  #@id/tv_reminder_time
   └─ androidx.compose.ui.platform.ComposeView  #@id/compose_footer_content
```

### `res/layout/chapter_finished_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_chapter_finished_fragment
   ├─ androidx.constraintlayout.widget.Group  #@id/group_chapter_finished_success_state
   ├─ androidx.compose.ui.platform.ComposeView  #@id/rav_chapter_finished
   ├─ TextView  #@id/tv_chapter_finished_success_title
   ├─ TextView  #@id/tv_chapter_finished_success_subtitle
   ├─ androidx.compose.ui.platform.ComposeView  #@id/cv_chapter_finished_stats
   ├─ androidx.cardview.widget.CardView  #@id/cv_double_gain
   │  └─ TextView  #@id/tv_profile_card_value
   ├─ androidx.compose.ui.platform.ComposeView  #@id/cv_chapter_finished_daily_goal_progress
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_chapter_finished_continue
   ├─ LinearLayout  #@id/layout_chapter_finished_loading_state
   │  ├─ app.rive.runtime.kotlin.RiveAnimationView
   │  └─ TextView
   ├─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_chapter_finished_offline_state
   │  ├─ ImageView  #@id/iv_connection_error
   │  ├─ TextView  #@id/tv_offline_state_headline
   │  ├─ TextView  #@id/tv_offline_state_description
   │  └─ androidx.compose.ui.platform.ComposeView  #@id/btn_chapter_finished_offline_state_continue
   ├─ androidx.compose.ui.platform.ComposeView  #@id/cv_coins
   └─ androidx.fragment.app.FragmentContainerView  #@id/fcv_chapter_finished_fragment_container
```

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

### `res/layout/chapter_finished_share_streak_layout_shareable_image.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_shareable_image
   ├─ ImageView
   ├─ ImageView  #@id/iv_mimo_logo
   ├─ TextView  #@id/tv_100days_of_code
   ├─ TextView  #@id/tv_nb_days_of_code
   ├─ TextView  #@id/tv_days_of_code
   ├─ com.google.android.material.progressindicator.CircularProgressIndicator  #@id/cpi_day_of_code
   ├─ TextView  #@id/tv_description
   ├─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_profile
   │  ├─ com.google.android.material.imageview.ShapeableImageView  #@id/iv_user_picture
   │  └─ TextView  #@id/tv_get_to_one_hundred
   └─ TextView  #@id/tv_mimo_app_link
```

### `res/layout/chapter_finished_streak_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/cl_chapter_finished_streak_fragment
   └─ androidx.compose.ui.platform.ComposeView  #@id/cv_chapter_finished_streak_content
```

### `res/layout/chapter_finished_widget_intro_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/cl_chapter_finished_widget_intro_fragment
   ├─ ImageView  #@id/img_widget
   ├─ TextView  #@id/widget_intro_header
   └─ androidx.compose.ui.platform.ComposeView  #@id/buttons_view
```

### `res/layout/chapter_toolbar.xml`

```text
└─ merge
   ├─ ImageView  #@id/btn_lesson_close
   ├─ TextView  #@id/tv_lesson_streak_chapter_toolbar
   ├─ TextView  #@id/tv_chapter_toolbar_label
   ├─ com.getmimo.ui.common.SpringAnimatingProgressBar  #@id/pb_chapter
   ├─ ImageView  #@id/btn_lesson_report
   └─ View  #@id/v_line
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
chapter
chapter_end_free_streak_goal_booting_up
chapter_end_free_streak_goal_commit
chapter_end_free_streak_goal_going_strong
chapter_end_free_streak_goal_habit_forming
chapter_end_free_streak_goal_headline
chapter_end_free_streak_goal_how_many_days
chapter_end_native_ads_learn_more
chapter_end_native_ads_remove_ads
chapter_end_native_ads_title
chapter_end_progress_eta_half_body
chapter_end_progress_eta_half_title
chapter_end_progress_eta_quarter_body
chapter_end_progress_eta_quarter_title
chapter_end_progress_eta_three_left_body
chapter_end_progress_eta_three_left_title
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
chapter_end_screen_sign_up_subtitle
chapter_end_screen_sign_up_title
chapter_end_streak_close_subtitle
chapter_end_streak_close_title
chapter_end_streak_free_challenge_completed_subtitle
chapter_end_streak_free_challenge_completed_title
chapter_end_streak_free_challenge_started_subtitle
chapter_end_streak_free_challenge_started_title
chapter_end_streak_multiple_subtitle
chapter_end_streak_one_more_subtitle
chapter_end_streak_one_more_title
chapter_end_streak_record_subtitle
chapter_end_streak_started_subtitle
chapter_end_streak_started_title
chapter_end_widget_intro_add_widget
chapter_end_widget_intro_title
chapter_finished_loading
chapter_finished_offline_state_description
developer_menu_discount_chapter_completed
developer_menu_force_chapter_end_progress_eta_enabled
streak_chapter_end_sharing_stories_error_facebook
streak_chapter_end_sharing_stories_error_instagram
streak_chapter_end_sharing_stories_repost_story
streak_chapter_end_sharing_stories_repost_story_highlight
streak_chapter_end_sharing_stories_share_layout_days_of_code_get_to_100
streak_chapter_end_sharing_stories_share_layout_days_of_code_get_to_100_more_than_100
streak_chapter_end_sharing_stories_share_layout_days_of_code_hashtag
streak_chapter_end_sharing_stories_share_layout_days_of_code_mimo_app_link
streak_chapter_end_sharing_stories_share_to
streak_chapter_end_sharing_stories_title
```

## ۴. رنگ‌های مرتبط (فهرست کامل)

```text
progress_chapter_background
progress_chapter_background_hard_mode
progress_chapter_primary
progress_chapter_primary_hard_mode
progress_chapter_weak
```

## ۵. دایمنشن‌های مرتبط (فهرست کامل)

```text
chapter_end_animation_width
chapter_end_continue_button_margin_bottom
```

## ۶. استایل‌های مرتبط (فهرست کامل)

(none)

## ۷. شواهد حالت‌ها (رشته‌های منبع)

```text
chapter_finished_loading
chapter_finished_offline_state_description
streak_chapter_end_sharing_stories_error_facebook
streak_chapter_end_sharing_stories_error_instagram
```

## ۸. ناوبری / deep link

(هیچ intent-filter/data برای این سطح اعلان نشده)
