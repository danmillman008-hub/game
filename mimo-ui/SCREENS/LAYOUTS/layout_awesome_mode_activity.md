# پروندهٔ لایه — `res/layout/awesome_mode_activity.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/awesome_mode_activity.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/awesome_mode_activity.xml`](../../SOURCE/res/layout/awesome_mode_activity.xml) |
| SHA-256 دیکد | `3ae8b8fa6bec65331641f3eb19c11a53aa13af217b79e9912bfcac88786a760f` |
| ریشه | `androidx.coordinatorlayout.widget.CoordinatorLayout` |
| تعداد گره | 8 |
| تعداد شناسه | 7 |
| تگ‌های استفاده‌شده | 6 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 12 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.coordinatorlayout.widget.CoordinatorLayout
   ├─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_awesome_mode_intro_screen
   │  ├─ TextView  #@id/tv_awesome_mode_title
   │  └─ TextView  #@id/tv_awesome_mode_explanation
   └─ androidx.coordinatorlayout.widget.CoordinatorLayout  #@id/layout_awesome_mode_content_screen
      ├─ androidx.viewpager2.widget.ViewPager2  #@id/vp_lessons
      └─ com.google.android.material.appbar.AppBarLayout  #@id/appbar_awesome_mode
         └─ com.getmimo.ui.chapter.view.ChapterToolbar  #@id/toolbar_awesome_mode
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:fitsSystemWindows` | `false` |
| 2 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:clipChildren` | `false` |
| 3 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:clipToPadding` | `false` |
| 4 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:layout_width` | `match_parent` |
| 5 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:layout_height` | `match_parent` |
| 6 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:animateLayoutChanges` | `false` |
| 7 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/layout_awesome_mode_intro_screen` |
| 8 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 9 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 10 | `TextView` | `android:id` | `@id/tv_awesome_mode_title` |
| 11 | `TextView` | `android:layout_width` | `wrap_content` |
| 12 | `TextView` | `android:layout_height` | `wrap_content` |
| 13 | `TextView` | `android:layout_marginTop` | `104.000000dip` |
| 14 | `TextView` | `android:text` | `@string/developer_menu_awesome_mode_title` |
| 15 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 16 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 17 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 18 | `TextView` | `style` | `@style/TextH1` |
| 19 | `TextView` | `android:gravity` | `0x00000011` |
| 20 | `TextView` | `android:id` | `@id/tv_awesome_mode_explanation` |
| 21 | `TextView` | `android:layout_width` | `0.000000dip` |
| 22 | `TextView` | `android:layout_height` | `wrap_content` |
| 23 | `TextView` | `android:layout_marginTop` | `32.000000dip` |
| 24 | `TextView` | `android:text` | `@string/developer_menu_awesome_mode_instructions` |
| 25 | `TextView` | `android:layout_marginStart` | `32.000000dip` |
| 26 | `TextView` | `android:layout_marginEnd` | `32.000000dip` |
| 27 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 28 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 29 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_awesome_mode_title` |
| 30 | `TextView` | `style` | `@style/TextLabel2` |
| 31 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:id` | `@id/layout_awesome_mode_content_screen` |
| 32 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:visibility` | `gone` |
| 33 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:layout_width` | `match_parent` |
| 34 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:layout_height` | `match_parent` |
| 35 | `androidx.viewpager2.widget.ViewPager2` | `android:id` | `@id/vp_lessons` |
| 36 | `androidx.viewpager2.widget.ViewPager2` | `android:layout_width` | `match_parent` |
| 37 | `androidx.viewpager2.widget.ViewPager2` | `android:layout_height` | `match_parent` |
| 38 | `com.google.android.material.appbar.AppBarLayout` | `android:id` | `@id/appbar_awesome_mode` |
| 39 | `com.google.android.material.appbar.AppBarLayout` | `android:focusable` | `false` |
| 40 | `com.google.android.material.appbar.AppBarLayout` | `android:focusableInTouchMode` | `false` |
| 41 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_width` | `match_parent` |
| 42 | `com.google.android.material.appbar.AppBarLayout` | `android:layout_height` | `wrap_content` |
| 43 | `com.google.android.material.appbar.AppBarLayout` | `android:elevation` | `0.000000dip` |
| 44 | `com.getmimo.ui.chapter.view.ChapterToolbar` | `android:id` | `@id/toolbar_awesome_mode` |
| 45 | `com.getmimo.ui.chapter.view.ChapterToolbar` | `android:layout_width` | `match_parent` |
| 46 | `com.getmimo.ui.chapter.view.ChapterToolbar` | `android:layout_height` | `@dimen/lesson_progress_navbar_height` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/lesson_progress_navbar_height` | `52.000000dip` / `68.000000dip` (sw600dp) |
| `@string/developer_menu_awesome_mode_instructions` | `Refresh the current lesson or open a new one to view it. Press back to close awesome mode.` |
| `@string/developer_menu_awesome_mode_title` | `Awesome Mode` |
| `@style/TextH1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '24.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '31.199984sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.199983sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextLabel2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/appbar_awesome_mode
@id/layout_awesome_mode_content_screen
@id/layout_awesome_mode_intro_screen
@id/toolbar_awesome_mode
@id/tv_awesome_mode_explanation
@id/tv_awesome_mode_title
@id/vp_lessons
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.awesome.AwesomeModeActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.coordinatorlayout.widget.CoordinatorLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:fitsSystemWindows="false" android:clipChildren="false" android:clipToPadding="false" android:layout_width="match_parent" android:layout_height="match_parent" android:animateLayoutChanges="false">
  <androidx.constraintlayout.widget.ConstraintLayout android:id="@id/layout_awesome_mode_intro_screen" android:layout_width="match_parent" android:layout_height="match_parent">
    <TextView android:id="@id/tv_awesome_mode_title" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="104.000000dip" android:text="@string/developer_menu_awesome_mode_title" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextH1"/>
    <TextView android:gravity="0x00000011" android:id="@id/tv_awesome_mode_explanation" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="32.000000dip" android:text="@string/developer_menu_awesome_mode_instructions" android:layout_marginStart="32.000000dip" android:layout_marginEnd="32.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_awesome_mode_title" style="@style/TextLabel2"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
  <androidx.coordinatorlayout.widget.CoordinatorLayout android:id="@id/layout_awesome_mode_content_screen" android:visibility="gone" android:layout_width="match_parent" android:layout_height="match_parent">
    <androidx.viewpager2.widget.ViewPager2 android:id="@id/vp_lessons" android:layout_width="match_parent" android:layout_height="match_parent"/>
    <com.google.android.material.appbar.AppBarLayout android:id="@id/appbar_awesome_mode" android:focusable="false" android:focusableInTouchMode="false" android:layout_width="match_parent" android:layout_height="wrap_content" android:elevation="0.000000dip">
      <com.getmimo.ui.chapter.view.ChapterToolbar android:id="@id/toolbar_awesome_mode" android:layout_width="match_parent" android:layout_height="@dimen/lesson_progress_navbar_height"/>
    </com.google.android.material.appbar.AppBarLayout>
  </androidx.coordinatorlayout.widget.CoordinatorLayout>
</androidx.coordinatorlayout.widget.CoordinatorLayout>
```
