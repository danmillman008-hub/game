# صفحه — `ChapterFinishedFragment$showRatingBottomSheet$1$1$1`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.chapter.chapterendview.main.ChapterFinishedFragment$showRatingBottomSheet$1$1$1` |
| نوع | `bottom_sheet` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose` |
| تعداد لایه‌های متصل | 7 |
| ComposeView | بله |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/chapter_finished_fragment.xml`](../SOURCE/res/layout/chapter_finished_fragment.xml) → [dossier](LAYOUTS/layout_chapter_finished_fragment.md)
- [`res/layout/chapter_finished_leaderboard_fragment.xml`](../SOURCE/res/layout/chapter_finished_leaderboard_fragment.xml) → [dossier](LAYOUTS/layout_chapter_finished_leaderboard_fragment.md)
- [`res/layout/chapter_finished_leaderboard_joined.xml`](../SOURCE/res/layout/chapter_finished_leaderboard_joined.xml) → [dossier](LAYOUTS/layout_chapter_finished_leaderboard_joined.md)
- [`res/layout/chapter_finished_leaderboard_status.xml`](../SOURCE/res/layout/chapter_finished_leaderboard_status.xml) → [dossier](LAYOUTS/layout_chapter_finished_leaderboard_status.md)
- [`res/layout/chapter_finished_share_streak_layout_shareable_image.xml`](../SOURCE/res/layout/chapter_finished_share_streak_layout_shareable_image.xml) → [dossier](LAYOUTS/layout_chapter_finished_share_streak_layout_shareable_image.md)
- [`res/layout/chapter_finished_streak_fragment.xml`](../SOURCE/res/layout/chapter_finished_streak_fragment.xml) → [dossier](LAYOUTS/layout_chapter_finished_streak_fragment.md)
- [`res/layout/chapter_finished_widget_intro_fragment.xml`](../SOURCE/res/layout/chapter_finished_widget_intro_fragment.xml) → [dossier](LAYOUTS/layout_chapter_finished_widget_intro_fragment.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

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

## ۳. رشته‌های مرتبط (فهرست کامل)

(none)

## ۴. رنگ‌های مرتبط (فهرست کامل)

(none)

## ۵. دایمنشن‌های مرتبط (فهرست کامل)

(none)

## ۶. استایل‌های مرتبط (فهرست کامل)

(none)

## ۷. شواهد حالت‌ها (رشته‌های منبع)

(none)

## ۸. ناوبری / deep link

(هیچ intent-filter/data برای این سطح اعلان نشده)
