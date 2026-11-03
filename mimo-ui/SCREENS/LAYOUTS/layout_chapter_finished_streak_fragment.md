# پروندهٔ لایه — `res/layout/chapter_finished_streak_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/chapter_finished_streak_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/chapter_finished_streak_fragment.xml`](../../SOURCE/res/layout/chapter_finished_streak_fragment.xml) |
| SHA-256 دیکد | `2871884567759bb134058f92682098247e0310b3ee2493bca5e0676f3fce45bf` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 4 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/cl_chapter_finished_streak_fragment
   └─ androidx.compose.ui.platform.ComposeView  #@id/cv_chapter_finished_streak_content
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/cl_chapter_finished_streak_fragment` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_primary` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 5 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/cv_chapter_finished_streak_content` |
| 6 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `match_parent` |
| 7 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `match_parent` |
| 8 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m_expandable` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/cl_chapter_finished_streak_fragment
@id/cv_chapter_finished_streak_content
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.chapter.ChapterActivity
com.getmimo.ui.chapter.chapterendview.main.ChapterFinishedFragment$onChapterFinishedContinue$1
com.getmimo.ui.chapter.chapterendview.main.ChapterFinishedFragment$showRatingBottomSheet$1$1$1
com.getmimo.ui.chapter.chapterendview.main.ChapterFinishedFragment$showRatingBottomSheet$1$2
com.getmimo.ui.chapter.chapterendview.streak.ChapterFinishedStreakFragment$bindView$1$2$1$1
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/cl_chapter_finished_streak_fragment" android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="match_parent">
  <androidx.compose.ui.platform.ComposeView android:id="@id/cv_chapter_finished_streak_content" android:layout_width="match_parent" android:layout_height="match_parent" android:layout_marginHorizontal="@dimen/spacing_m_expandable"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
