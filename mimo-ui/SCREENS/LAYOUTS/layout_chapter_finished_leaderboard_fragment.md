# پروندهٔ لایه — `res/layout/chapter_finished_leaderboard_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/chapter_finished_leaderboard_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/chapter_finished_leaderboard_fragment.xml`](../../SOURCE/res/layout/chapter_finished_leaderboard_fragment.xml) |
| SHA-256 دیکد | `eef75bdb17e355b0a5a69e3f05d2484e066ac1f7b786859519211675d1d81c6f` |
| ریشه | `FrameLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 10 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout  #@id/cl_chapter_finished_leaderboard
   ├─ androidx.constraintlayout.widget.ConstraintLayout  #@id/cl_main_content
   │  ├─ FrameLayout  #@id/fl_chapter_finished_leaderboard_container
   │  └─ androidx.compose.ui.platform.ComposeView  #@id/btn_chapter_finished_leaderboard_continue
   └─ ProgressBar  #@id/pb_loading
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:id` | `@id/cl_chapter_finished_leaderboard` |
| 2 | `FrameLayout` | `android:background` | `@color/background_primary` |
| 3 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 4 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/cl_main_content` |
| 6 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 7 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 8 | `FrameLayout` | `android:id` | `@id/fl_chapter_finished_leaderboard_container` |
| 9 | `FrameLayout` | `android:layout_width` | `0.000000dip` |
| 10 | `FrameLayout` | `android:layout_height` | `0.000000dip` |
| 11 | `FrameLayout` | `app:layout_constraintBottom_toTopOf` | `@id/btn_chapter_finished_leaderboard_continue` |
| 12 | `FrameLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 13 | `FrameLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 14 | `FrameLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 15 | `FrameLayout` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 16 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_chapter_finished_leaderboard_continue` |
| 17 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 18 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 19 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 20 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/chapter_end_continue_button_margin_bottom` |
| 21 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 22 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 23 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 24 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 25 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/fl_chapter_finished_leaderboard_container` |
| 26 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 27 | `ProgressBar` | `android:layout_gravity` | `0x00000011` |
| 28 | `ProgressBar` | `android:id` | `@id/pb_loading` |
| 29 | `ProgressBar` | `android:visibility` | `gone` |
| 30 | `ProgressBar` | `android:layout_width` | `wrap_content` |
| 31 | `ProgressBar` | `android:layout_height` | `wrap_content` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@dimen/chapter_end_continue_button_margin_bottom` | `16.000000dip` / `36.000000dip` (sw600dp) |
| `@dimen/general_max_width` | `480.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/btn_chapter_finished_leaderboard_continue
@id/cl_chapter_finished_leaderboard
@id/cl_main_content
@id/fl_chapter_finished_leaderboard_container
@id/pb_loading
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.chapter.ChapterActivity
com.getmimo.ui.chapter.chapterendview.leaderboard.ChapterFinishedLeaderboardFragment$setupAuthenticationObservers$2
com.getmimo.ui.chapter.chapterendview.main.ChapterFinishedFragment$onChapterFinishedContinue$1
com.getmimo.ui.chapter.chapterendview.main.ChapterFinishedFragment$showRatingBottomSheet$1$1$1
com.getmimo.ui.chapter.chapterendview.main.ChapterFinishedFragment$showRatingBottomSheet$1$2
com.getmimo.ui.leaderboard.LeaderboardFragment$observeViewModelEvents$1$1$1
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:id="@id/cl_chapter_finished_leaderboard" android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="match_parent">
  <androidx.constraintlayout.widget.ConstraintLayout android:id="@id/cl_main_content" android:layout_width="match_parent" android:layout_height="match_parent">
    <FrameLayout android:id="@id/fl_chapter_finished_leaderboard_container" android:layout_width="0.000000dip" android:layout_height="0.000000dip" app:layout_constraintBottom_toTopOf="@id/btn_chapter_finished_leaderboard_continue" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:layout_constraintWidth_max="@dimen/general_max_width"/>
    <androidx.compose.ui.platform.ComposeView android:id="@id/btn_chapter_finished_leaderboard_continue" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" android:layout_marginBottom="@dimen/chapter_end_continue_button_margin_bottom" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/fl_chapter_finished_leaderboard_container" app:layout_constraintWidth_max="@dimen/general_max_width"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
  <ProgressBar android:layout_gravity="0x00000011" android:id="@id/pb_loading" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
</FrameLayout>
```
