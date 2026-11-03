# پروندهٔ لایه — `res/layout/lesson_interactive_reveal_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/lesson_interactive_reveal_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/lesson_interactive_reveal_fragment.xml`](../../SOURCE/res/layout/lesson_interactive_reveal_fragment.xml) |
| SHA-256 دیکد | `62ef293a0e5bdbaea03217580263778e0ce569b4be1dfef6c64240c4c2703398` |
| ریشه | `LinearLayout` |
| تعداد گره | 10 |
| تعداد شناسه | 9 |
| تگ‌های استفاده‌شده | 10 |
| ویوهای سفارشی `com.getmimo` | 6 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 17 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ ScrollView  #@id/sv_lesson
   │  └─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_lesson_content
   │     ├─ androidx.compose.ui.platform.ComposeView  #@id/cv_lesson_hard_mode_label
   │     ├─ com.getmimo.ui.lesson.interactive.view.LessonDescriptionView  #@id/layout_lesson_description
   │     ├─ com.getmimo.ui.lesson.view.database.DatabaseView  #@id/database_view
   │     ├─ com.getmimo.ui.lesson.view.code.header.CodeHeaderView  #@id/codeheaderview
   │     ├─ com.getmimo.ui.lesson.view.code.CodeBodyView  #@id/codebodyview
   │     └─ com.getmimo.ui.lesson.interactive.view.LessonOutputView  #@id/lesson_output_layout
   └─ com.getmimo.ui.lesson.view.InteractionKeyboardContainerView  #@id/interaction_keyboard_reveal
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:background` | `@color/background_primary` |
| 3 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 4 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 5 | `ScrollView` | `android:id` | `@id/sv_lesson` |
| 6 | `ScrollView` | `android:layout_width` | `match_parent` |
| 7 | `ScrollView` | `android:layout_height` | `0.000000dip` |
| 8 | `ScrollView` | `android:layout_weight` | `1.000000` |
| 9 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_gravity` | `0x00000031` |
| 10 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:orientation` | `vertical` |
| 11 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/layout_lesson_content` |
| 12 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 13 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 14 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginTop` | `@dimen/lesson_content_margin_top` |
| 15 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginBottom` | `@dimen/lesson_content_margin_bottom` |
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
| 64 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `android:id` | `@id/interaction_keyboard_reveal` |
| 65 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `android:background` | `@color/transparent` |
| 66 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `android:clipChildren` | `false` |
| 67 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `android:clipToPadding` | `false` |
| 68 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `android:layout_width` | `match_parent` |
| 69 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `android:layout_height` | `wrap_content` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/transparent` | `#00000000` |
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
@id/interaction_keyboard_reveal
@id/layout_lesson_content
@id/layout_lesson_description
@id/lesson_output_layout
@id/sv_lesson
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:orientation="vertical" android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="match_parent">
  <ScrollView android:id="@id/sv_lesson" android:layout_width="match_parent" android:layout_height="0.000000dip" android:layout_weight="1.000000">
    <androidx.constraintlayout.widget.ConstraintLayout android:layout_gravity="0x00000031" android:orientation="vertical" android:id="@id/layout_lesson_content" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/lesson_content_margin_top" android:layout_marginBottom="@dimen/lesson_content_margin_bottom">
      <androidx.compose.ui.platform.ComposeView android:id="@id/cv_lesson_hard_mode_label" android:visibility="gone" android:layout_width="match_parent" android:layout_height="wrap_content" app:layout_constraintTop_toTopOf="0"/>
      <com.getmimo.ui.lesson.interactive.view.LessonDescriptionView android:id="@id/layout_lesson_description" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/cv_lesson_hard_mode_label" app:layout_constraintWidth_max="@dimen/lessonview_content_maxwidth"/>
      <com.getmimo.ui.lesson.view.database.DatabaseView android:id="@id/database_view" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m_expandable" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/layout_lesson_description"/>
      <com.getmimo.ui.lesson.view.code.header.CodeHeaderView android:id="@id/codeheaderview" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_m_expandable" android:layout_marginStart="@dimen/lesson_codeview_margin_start" android:layout_marginEnd="@dimen/lesson_codeview_margin_end" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/database_view" app:layout_goneMarginTop="@dimen/spacing_m_expandable"/>
      <com.getmimo.ui.lesson.view.code.CodeBodyView android:id="@id/codebodyview" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_m_expandable" android:layout_marginStart="@dimen/lesson_codeview_margin_start" android:layout_marginEnd="@dimen/lesson_codeview_margin_end" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/codeheaderview" app:layout_goneMarginTop="@dimen/spacing_m_expandable"/>
      <com.getmimo.ui.lesson.interactive.view.LessonOutputView android:id="@id/lesson_output_layout" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/codebodyview"/>
    </androidx.constraintlayout.widget.ConstraintLayout>
  </ScrollView>
  <com.getmimo.ui.lesson.view.InteractionKeyboardContainerView android:id="@id/interaction_keyboard_reveal" android:background="@color/transparent" android:clipChildren="false" android:clipToPadding="false" android:layout_width="match_parent" android:layout_height="wrap_content"/>
</LinearLayout>
```
