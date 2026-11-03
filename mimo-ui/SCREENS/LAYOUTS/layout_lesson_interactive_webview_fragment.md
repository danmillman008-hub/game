# پروندهٔ لایه — `res/layout/lesson_interactive_webview_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/lesson_interactive_webview_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/lesson_interactive_webview_fragment.xml`](../../SOURCE/res/layout/lesson_interactive_webview_fragment.xml) |
| SHA-256 دیکد | `6bec986f7569bd7db5069868d1538a06c49edcda4cad1a04f0ccc2710c5a3dd1` |
| ریشه | `LinearLayout` |
| تعداد گره | 12 |
| تعداد شناسه | 11 |
| تگ‌های استفاده‌شده | 12 |
| ویوهای سفارشی `com.getmimo` | 7 |
| `ComposeView` | 1 |
| `WebView` | 1 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 18 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ com.getmimo.ui.lesson.interactive.webview.WebViewLessonScrollView  #@id/sv_lesson_noninteractive
   │  └─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_lesson_content
   │     ├─ androidx.compose.ui.platform.ComposeView  #@id/cv_lesson_hard_mode_label
   │     ├─ com.getmimo.ui.lesson.interactive.view.LessonDescriptionView  #@id/layout_lesson_description
   │     ├─ com.getmimo.ui.lesson.view.database.DatabaseView  #@id/database_view
   │     ├─ com.getmimo.ui.lesson.view.code.header.CodeHeaderView  #@id/codeheaderview
   │     ├─ com.getmimo.ui.lesson.view.code.CodeBodyView  #@id/codebodyview
   │     └─ com.getmimo.ui.lesson.interactive.view.LessonOutputView  #@id/lesson_output_layout
   ├─ androidx.coordinatorlayout.widget.CoordinatorLayout  #@id/feedback_sheet
   │  └─ androidx.fragment.app.FragmentContainerView  #@id/feedback_container
   └─ com.getmimo.ui.lesson.view.InteractionKeyboardContainerView  #@id/interaction_keyboard_noninteractive
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:background` | `@color/background_primary` |
| 3 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 4 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 5 | `com.getmimo.ui.lesson.interactive.webview.WebViewLessonScrollView` | `android:id` | `@id/sv_lesson_noninteractive` |
| 6 | `com.getmimo.ui.lesson.interactive.webview.WebViewLessonScrollView` | `android:layout_width` | `match_parent` |
| 7 | `com.getmimo.ui.lesson.interactive.webview.WebViewLessonScrollView` | `android:layout_height` | `0.000000dip` |
| 8 | `com.getmimo.ui.lesson.interactive.webview.WebViewLessonScrollView` | `android:layout_weight` | `1.000000` |
| 9 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_gravity` | `0x00000031` |
| 10 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:orientation` | `vertical` |
| 11 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/layout_lesson_content` |
| 12 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingTop` | `@dimen/lesson_content_margin_top` |
| 13 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingBottom` | `@dimen/lesson_content_margin_bottom` |
| 14 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 15 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 16 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/cv_lesson_hard_mode_label` |
| 17 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `gone` |
| 18 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `match_parent` |
| 19 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 20 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toTopOf` | `0` |
| 21 | `com.getmimo.ui.lesson.interactive.view.LessonDescriptionView` | `android:id` | `@id/layout_lesson_description` |
| 22 | `com.getmimo.ui.lesson.interactive.view.LessonDescriptionView` | `android:layout_width` | `0.000000dip` |
| 23 | `com.getmimo.ui.lesson.interactive.view.LessonDescriptionView` | `android:layout_height` | `wrap_content` |
| 24 | `com.getmimo.ui.lesson.interactive.view.LessonDescriptionView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 25 | `com.getmimo.ui.lesson.interactive.view.LessonDescriptionView` | `app:layout_constraintStart_toStartOf` | `0` |
| 26 | `com.getmimo.ui.lesson.interactive.view.LessonDescriptionView` | `app:layout_constraintTop_toBottomOf` | `@id/cv_lesson_hard_mode_label` |
| 27 | `com.getmimo.ui.lesson.interactive.view.LessonDescriptionView` | `app:layout_constraintWidth_max` | `@dimen/lessonview_content_maxwidth` |
| 28 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `android:id` | `@id/database_view` |
| 29 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `android:visibility` | `gone` |
| 30 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `android:layout_width` | `0.000000dip` |
| 31 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `android:layout_height` | `wrap_content` |
| 32 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `android:layout_marginTop` | `@dimen/spacing_m_expandable` |
| 33 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 34 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `app:layout_constraintStart_toStartOf` | `0` |
| 35 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `app:layout_constraintTop_toBottomOf` | `@id/layout_lesson_description` |
| 36 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `android:id` | `@id/codeheaderview` |
| 37 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `android:visibility` | `gone` |
| 38 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `android:layout_width` | `0.000000dip` |
| 39 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `android:layout_height` | `wrap_content` |
| 40 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `android:layout_marginBottom` | `@dimen/spacing_m_expandable` |
| 41 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `android:layout_marginStart` | `@dimen/lesson_codeview_margin_start` |
| 42 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `android:layout_marginEnd` | `@dimen/lesson_codeview_margin_end` |
| 43 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 44 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `app:layout_constraintStart_toStartOf` | `0` |
| 45 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `app:layout_constraintTop_toBottomOf` | `@id/database_view` |
| 46 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `app:layout_goneMarginTop` | `@dimen/spacing_m_expandable` |
| 47 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `android:id` | `@id/codebodyview` |
| 48 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `android:visibility` | `gone` |
| 49 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `android:layout_width` | `0.000000dip` |
| 50 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `android:layout_height` | `wrap_content` |
| 51 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `android:layout_marginBottom` | `@dimen/spacing_m_expandable` |
| 52 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `android:layout_marginStart` | `@dimen/lesson_codeview_margin_start` |
| 53 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `android:layout_marginEnd` | `@dimen/lesson_codeview_margin_end` |
| 54 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 55 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `app:layout_constraintStart_toStartOf` | `0` |
| 56 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `app:layout_constraintTop_toBottomOf` | `@id/codeheaderview` |
| 57 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `app:layout_goneMarginTop` | `@dimen/spacing_m_expandable` |
| 58 | `com.getmimo.ui.lesson.interactive.view.LessonOutputView` | `android:id` | `@id/lesson_output_layout` |
| 59 | `com.getmimo.ui.lesson.interactive.view.LessonOutputView` | `android:layout_width` | `0.000000dip` |
| 60 | `com.getmimo.ui.lesson.interactive.view.LessonOutputView` | `android:layout_height` | `wrap_content` |
| 61 | `com.getmimo.ui.lesson.interactive.view.LessonOutputView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 62 | `com.getmimo.ui.lesson.interactive.view.LessonOutputView` | `app:layout_constraintStart_toStartOf` | `0` |
| 63 | `com.getmimo.ui.lesson.interactive.view.LessonOutputView` | `app:layout_constraintTop_toBottomOf` | `@id/codebodyview` |
| 64 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:id` | `@id/feedback_sheet` |
| 65 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:visibility` | `gone` |
| 66 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:layout_width` | `match_parent` |
| 67 | `androidx.coordinatorlayout.widget.CoordinatorLayout` | `android:layout_height` | `wrap_content` |
| 68 | `androidx.fragment.app.FragmentContainerView` | `android:id` | `@id/feedback_container` |
| 69 | `androidx.fragment.app.FragmentContainerView` | `android:layout_width` | `match_parent` |
| 70 | `androidx.fragment.app.FragmentContainerView` | `android:layout_height` | `wrap_content` |
| 71 | `androidx.fragment.app.FragmentContainerView` | `app:behavior_hideable` | `true` |
| 72 | `androidx.fragment.app.FragmentContainerView` | `app:behavior_skipCollapsed` | `true` |
| 73 | `androidx.fragment.app.FragmentContainerView` | `app:layout_behavior` | `com.google.android.material.bottomsheet.BottomSheetBehavior` |
| 74 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `android:id` | `@id/interaction_keyboard_noninteractive` |
| 75 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `android:clipChildren` | `false` |
| 76 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `android:clipToPadding` | `false` |
| 77 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `android:layout_width` | `match_parent` |
| 78 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `android:layout_height` | `wrap_content` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@dimen/lesson_codeview_margin_end` | `0.000000dip` |
| `@dimen/lesson_codeview_margin_start` | `0.000000dip` |
| `@dimen/lesson_content_margin_bottom` | `16.000000dip` |
| `@dimen/lesson_content_margin_top` | `8.000000dip` |
| `@dimen/lessonview_content_maxwidth` | `@dimen/content_max_width` |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/codebodyview
@id/codeheaderview
@id/cv_lesson_hard_mode_label
@id/database_view
@id/feedback_container
@id/feedback_sheet
@id/interaction_keyboard_noninteractive
@id/layout_lesson_content
@id/layout_lesson_description
@id/lesson_output_layout
@id/sv_lesson_noninteractive
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="match_parent">
  <com.getmimo.ui.lesson.interactive.webview.WebViewLessonScrollView android:id="@id/sv_lesson_noninteractive" android:layout_width="match_parent" android:layout_height="0.000000dip" android:layout_weight="1.000000">
    <androidx.constraintlayout.widget.ConstraintLayout android:layout_gravity="0x00000031" android:orientation="vertical" android:id="@id/layout_lesson_content" android:paddingTop="@dimen/lesson_content_margin_top" android:paddingBottom="@dimen/lesson_content_margin_bottom" android:layout_width="match_parent" android:layout_height="wrap_content">
      <androidx.compose.ui.platform.ComposeView android:id="@id/cv_lesson_hard_mode_label" android:visibility="gone" android:layout_width="match_parent" android:layout_height="wrap_content" app:layout_constraintTop_toTopOf="0"/>
      <com.getmimo.ui.lesson.interactive.view.LessonDescriptionView android:id="@id/layout_lesson_description" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/cv_lesson_hard_mode_label" app:layout_constraintWidth_max="@dimen/lessonview_content_maxwidth"/>
      <com.getmimo.ui.lesson.view.database.DatabaseView android:id="@id/database_view" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m_expandable" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/layout_lesson_description"/>
      <com.getmimo.ui.lesson.view.code.header.CodeHeaderView android:id="@id/codeheaderview" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_m_expandable" android:layout_marginStart="@dimen/lesson_codeview_margin_start" android:layout_marginEnd="@dimen/lesson_codeview_margin_end" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/database_view" app:layout_goneMarginTop="@dimen/spacing_m_expandable"/>
      <com.getmimo.ui.lesson.view.code.CodeBodyView android:id="@id/codebodyview" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_m_expandable" android:layout_marginStart="@dimen/lesson_codeview_margin_start" android:layout_marginEnd="@dimen/lesson_codeview_margin_end" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/codeheaderview" app:layout_goneMarginTop="@dimen/spacing_m_expandable"/>
      <com.getmimo.ui.lesson.interactive.view.LessonOutputView android:id="@id/lesson_output_layout" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/codebodyview"/>
    </androidx.constraintlayout.widget.ConstraintLayout>
  </com.getmimo.ui.lesson.interactive.webview.WebViewLessonScrollView>
  <androidx.coordinatorlayout.widget.CoordinatorLayout android:id="@id/feedback_sheet" android:visibility="gone" android:layout_width="match_parent" android:layout_height="wrap_content">
    <androidx.fragment.app.FragmentContainerView android:id="@id/feedback_container" android:layout_width="match_parent" android:layout_height="wrap_content" app:behavior_hideable="true" app:behavior_skipCollapsed="true" app:layout_behavior="com.google.android.material.bottomsheet.BottomSheetBehavior"/>
  </androidx.coordinatorlayout.widget.CoordinatorLayout>
  <com.getmimo.ui.lesson.view.InteractionKeyboardContainerView android:id="@id/interaction_keyboard_noninteractive" android:clipChildren="false" android:clipToPadding="false" android:layout_width="match_parent" android:layout_height="wrap_content"/>
</LinearLayout>
```
