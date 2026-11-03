# پروندهٔ لایه — `res/layout/chapter_activity.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/chapter_activity.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/chapter_activity.xml`](../../SOURCE/res/layout/chapter_activity.xml) |
| SHA-256 دیکد | `fa894dde239543504a21388e03a90ec63341b6dbc5f0cff36c3f7478318d8052` |
| ریشه | `FrameLayout` |
| تعداد گره | 7 |
| تعداد شناسه | 6 |
| تگ‌های استفاده‌شده | 7 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 8 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout  #@id/chapter_activity_root
   ├─ androidx.compose.ui.platform.ComposeView  #@id/compose_view
   └─ androidx.coordinatorlayout.widget.CoordinatorLayout
      ├─ androidx.viewpager2.widget.ViewPager2  #@id/vp_lessons
      ├─ androidx.fragment.app.FragmentContainerView  #@id/layout_chapter_finished_share_fragment
      └─ com.google.android.material.appbar.AppBarLayout  #@id/chapter_appbarlayout
         └─ com.getmimo.ui.chapter.view.ChapterToolbar  #@id/chapter_toolbar
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:id` | `@id/chapter_activity_root` |
| 2 | `FrameLayout` | `android:clipChildren` | `false` |
| 3 | `FrameLayout` | `android:clipToPadding` | `false` |
| 4 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 5 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 6 | `FrameLayout` | `android:animateLayoutChanges` | `false` |
| 7 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/compose_view` |
| 8 | `androidx.compose.ui.platform.ComposeView` | `android:fitsSystemWindows` | `false` |
| 9 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `match_parent` |
| 10 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `match_parent` |
| 11 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:fitsSystemWindows` | `true` |
| 12 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:clipChildren` | `false` |
| 13 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:clipToPadding` | `false` |
| 14 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:layout_width` | `match_parent` |
| 15 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:layout_height` | `match_parent` |
| 16 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:animateLayoutChanges` | `false` |
| 17 | `androidx.viewpager2.widget.ViewPager2` | `android:id` | `@id/vp_lessons` |
| 18 | `androidx.viewpager2.widget.ViewPager2` | `android:layout_width` | `match_parent` |
| 19 | `androidx.viewpager2.widget.ViewPager2` | `android:layout_height` | `match_parent` |
| 20 | `androidx.fragment.app.FragmentContainerView` | `android:id` | `@id/layout_chapter_finished_share_fragment` |
| 21 | `androidx.fragment.app.FragmentContainerView` | `android:layout_width` | `match_parent` |
| 22 | `androidx.fragment.app.FragmentContainerView` | `android:layout_height` | `match_parent` |
| 23 | `com.google.android.material.appbar.AppBarLayout` | `android:id` | `@id/chapter_appbarlayout` |
| 24 | `com.google.android.material.appbar.AppBarLayout` | `android:background` | `@color/navbar_background` |
| 25 | `com.google.android.material.appbar.AppBarLayout` | `android:focusable` | `false` |
| 26 | `com.google.android.material.appbar.AppBarLayout` | `android:focusableInTouchMode` | `false` |
| 27 | `com.google.android.material.appbar.AppBarLayout` | `android:fitsSystemWindows` | `true` |
| 28 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_width` | `match_parent` |
| 29 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_height` | `wrap_content` |
| 30 | `com.google.android.material.appbar.AppBarLayout` | `android:elevation` | `0.000000dip` |
| 31 | `com.google.android.material.appbar.AppBarLayout` | `app:elevation` | `0.000000dip` |
| 32 | `com.getmimo.ui.chapter.view.ChapterToolbar` | `android:id` | `@id/chapter_toolbar` |
| 33 | `com.getmimo.ui.chapter.view.ChapterToolbar` | `android:layout_width` | `match_parent` |
| 34 | `com.getmimo.ui.chapter.view.ChapterToolbar` | `android:layout_height` | `@dimen/lesson_progress_navbar_height` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/navbar_background` | `#FFFFFFFF` / `#FF333661` (night) |
| `@dimen/lesson_progress_navbar_height` | `52.000000dip` / `68.000000dip` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/chapter_activity_root
@id/chapter_appbarlayout
@id/chapter_toolbar
@id/compose_view
@id/layout_chapter_finished_share_fragment
@id/vp_lessons
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.chapter.ChapterActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/chapter_activity_root" android:clipChildren="false" android:clipToPadding="false" android:layout_width="match_parent" android:layout_height="match_parent" android:animateLayoutChanges="false">
  <androidx.compose.ui.platform.ComposeView android:id="@id/compose_view" android:fitsSystemWindows="false" android:layout_width="match_parent" android:layout_height="match_parent"/>
  <androidx.coordinatorlayout.widget.CoordinatorLayout android:fitsSystemWindows="true" android:clipChildren="false" android:clipToPadding="false" android:layout_width="match_parent" android:layout_height="match_parent" android:animateLayoutChanges="false">
    <androidx.viewpager2.widget.ViewPager2 android:id="@id/vp_lessons" android:layout_width="match_parent" android:layout_height="match_parent"/>
    <androidx.fragment.app.FragmentContainerView android:id="@id/layout_chapter_finished_share_fragment" android:layout_width="match_parent" android:layout_height="match_parent"/>
    <com.google.android.material.appbar.AppBarLayout android:id="@id/chapter_appbarlayout" android:background="@color/navbar_background" android:focusable="false" android:focusableInTouchMode="false" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="wrap_content" android:elevation="0.000000dip" app:elevation="0.000000dip">
      <com.getmimo.ui.chapter.view.ChapterToolbar android:id="@id/chapter_toolbar" android:layout_width="match_parent" android:layout_height="@dimen/lesson_progress_navbar_height"/>
    </com.google.android.material.appbar.AppBarLayout>
  </androidx.coordinatorlayout.widget.CoordinatorLayout>
</FrameLayout>
```
