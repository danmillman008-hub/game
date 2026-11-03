# پروندهٔ لایه — `res/layout/lesson_interactive_fillthegap_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/lesson_interactive_fillthegap_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/lesson_interactive_fillthegap_fragment.xml`](../../SOURCE/res/layout/lesson_interactive_fillthegap_fragment.xml) |
| SHA-256 دیکد | `aa217b7615cda1b1815f4ed84602d04ca13636584b53827031a1e858f88c2273` |
| ریشه | `LinearLayout` |
| تعداد گره | 11 |
| تعداد شناسه | 10 |
| تگ‌های استفاده‌شده | 11 |
| ویوهای سفارشی `com.getmimo` | 6 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 20 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ ScrollView  #@id/sv_lesson
   │  └─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_lesson_content
   │     ├─ androidx.compose.ui.platform.ComposeView  #@id/cv_lesson_hard_mode_label
   │     ├─ com.getmimo.ui.lesson.interactive.view.LessonDescriptionView  #@id/layout_lesson_description
   │     ├─ TextView  #@id/tv_ftg_hint
   │     ├─ com.getmimo.ui.lesson.view.database.DatabaseView  #@id/database_view
   │     ├─ com.getmimo.ui.lesson.view.code.header.CodeHeaderView  #@id/codeheaderview
   │     ├─ com.getmimo.ui.lesson.view.code.CodeBodyView  #@id/codebodyview
   │     └─ com.getmimo.ui.lesson.interactive.view.LessonOutputView  #@id/lesson_output_layout
   └─ com.getmimo.ui.lesson.view.InteractionKeyboardContainerView  #@id/interaction_keyboard_fillthegap
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
| 10 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/layout_lesson_content` |
| 11 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 12 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 13 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginTop` | `@dimen/lesson_content_margin_top` |
| 14 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginBottom` | `@dimen/lesson_content_margin_bottom` |
| 15 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/cv_lesson_hard_mode_label` |
| 16 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `gone` |
| 17 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `match_parent` |
| 18 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 19 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toTopOf` | `0` |
| 20 | `com.getmimo.ui.lesson.interactive.view.LessonDescriptionView` | `android:id` | `@id/layout_lesson_description` |
| 21 | `com.getmimo.ui.lesson.interactive.view.LessonDescriptionView` | `android:layout_width` | `0.000000dip` |
| 22 | `com.getmimo.ui.lesson.interactive.view.LessonDescriptionView` | `android:layout_height` | `wrap_content` |
| 23 | `com.getmimo.ui.lesson.interactive.view.LessonDescriptionView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 24 | `com.getmimo.ui.lesson.interactive.view.LessonDescriptionView` | `app:layout_constraintStart_toStartOf` | `0` |
| 25 | `com.getmimo.ui.lesson.interactive.view.LessonDescriptionView` | `app:layout_constraintTop_toBottomOf` | `@id/cv_lesson_hard_mode_label` |
| 26 | `com.getmimo.ui.lesson.interactive.view.LessonDescriptionView` | `app:layout_constraintWidth_max` | `@dimen/lessonview_content_maxwidth` |
| 27 | `TextView` | `android:id` | `@id/tv_ftg_hint` |
| 28 | `TextView` | `android:layout_width` | `0.000000dip` |
| 29 | `TextView` | `android:layout_height` | `wrap_content` |
| 30 | `TextView` | `android:text` | `@string/interaction_hint_ftg` |
| 31 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 32 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 33 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/layout_lesson_description` |
| 34 | `TextView` | `app:layout_constraintWidth_max` | `@dimen/lessonview_content_maxwidth` |
| 35 | `TextView` | `style` | `@style/TextInteractionHint` |
| 36 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `android:id` | `@id/database_view` |
| 37 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `android:visibility` | `gone` |
| 38 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `android:layout_width` | `0.000000dip` |
| 39 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `android:layout_height` | `wrap_content` |
| 40 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 41 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 42 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `app:layout_constraintStart_toStartOf` | `0` |
| 43 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_ftg_hint` |
| 44 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `app:layout_goneMarginTop` | `@dimen/spacing_m_expandable` |
| 45 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `android:id` | `@id/codeheaderview` |
| 46 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `android:visibility` | `gone` |
| 47 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `android:layout_width` | `0.000000dip` |
| 48 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `android:layout_height` | `wrap_content` |
| 49 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `android:layout_marginBottom` | `@dimen/spacing_m_expandable` |
| 50 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `android:layout_marginStart` | `@dimen/lesson_codeview_margin_start` |
| 51 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `android:layout_marginEnd` | `@dimen/lesson_codeview_margin_end` |
| 52 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 53 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `app:layout_constraintStart_toStartOf` | `0` |
| 54 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `app:layout_constraintTop_toBottomOf` | `@id/database_view` |
| 55 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `app:layout_goneMarginTop` | `@dimen/spacing_m_expandable` |
| 56 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `android:id` | `@id/codebodyview` |
| 57 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `android:visibility` | `gone` |
| 58 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `android:layout_width` | `0.000000dip` |
| 59 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `android:layout_height` | `wrap_content` |
| 60 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `android:layout_marginBottom` | `@dimen/spacing_m_expandable` |
| 61 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `android:layout_marginStart` | `@dimen/lesson_codeview_margin_start` |
| 62 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `android:layout_marginEnd` | `@dimen/lesson_codeview_margin_end` |
| 63 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 64 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `app:layout_constraintStart_toStartOf` | `0` |
| 65 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `app:layout_constraintTop_toBottomOf` | `@id/codeheaderview` |
| 66 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `app:layout_goneMarginTop` | `@dimen/spacing_m_expandable` |
| 67 | `com.getmimo.ui.lesson.interactive.view.LessonOutputView` | `android:id` | `@id/lesson_output_layout` |
| 68 | `com.getmimo.ui.lesson.interactive.view.LessonOutputView` | `android:layout_width` | `0.000000dip` |
| 69 | `com.getmimo.ui.lesson.interactive.view.LessonOutputView` | `android:layout_height` | `wrap_content` |
| 70 | `com.getmimo.ui.lesson.interactive.view.LessonOutputView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 71 | `com.getmimo.ui.lesson.interactive.view.LessonOutputView` | `app:layout_constraintStart_toStartOf` | `0` |
| 72 | `com.getmimo.ui.lesson.interactive.view.LessonOutputView` | `app:layout_constraintTop_toBottomOf` | `@id/codebodyview` |
| 73 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `android:id` | `@id/interaction_keyboard_fillthegap` |
| 74 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `android:clipChildren` | `false` |
| 75 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `android:clipToPadding` | `false` |
| 76 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `android:layout_width` | `match_parent` |
| 77 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `android:layout_height` | `wrap_content` |
| 78 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `app:contains_ftg` | `true` |

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
| `@dimen/spacing_s` | `12.000000dip` |
| `@string/interaction_hint_ftg` | `Tap the snippets below` / `Tippe unten auf die Snippets` (de) / `Toca el código abajo` (es) / `Appuie sur les extraits ci-dessous` (fr) / `Ketuk snippet di bawah` (in) / `Tocca gli snippet qui sotto` (it) / `Dotknij fragmentów poniżej` (pl) / `Toque nos trechos de código abaixo` (pt-rBR) / `Нажми на фрагменты ниже` (ru) / `Aşağıdaki parçalara dokun` (tr) |
| `@style/TextInteractionHint` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_weak', 'value_type': 'reference'}, {'attr': 'android:gravity', 'attr_id': '0x010100AF', 'value': '0x00000010', 'value_type': 'int_hex'}, {'attr': 'android:layout_marginTop', 'attr_id': '0x010100F8', 'value': '@dimen/spacing_l', 'value_type': 'reference'}, {'attr': 'android:drawablePadding', 'attr_id': '0x01010171', 'value': '@dimen/spacing_xxs', 'value_type': 'reference'}, {'attr': 'android:layout_marginStart', 'attr_id': '0x010103B5', 'value': '@dimen/spacing_m', 'value_type': 'reference'}, {'attr': 'android:layout_marginEnd', 'attr_id': '0x010103B6', 'value': '@dimen/spacing_m', 'value_type': 'reference'}, {'attr': 'attr.drawableStartCompat', 'attr_id': '0x7F040217', 'value': '@drawable/ic_info_circle', 'value_type': 'reference'}, {'attr': 'attr.drawableTint', 'attr_id': '0x7F040218', 'value': '@color/text_weak', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/codebodyview
@id/codeheaderview
@id/cv_lesson_hard_mode_label
@id/database_view
@id/interaction_keyboard_fillthegap
@id/layout_lesson_content
@id/layout_lesson_description
@id/lesson_output_layout
@id/sv_lesson
@id/tv_ftg_hint
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
  <ScrollView android:id="@id/sv_lesson" android:layout_width="match_parent" android:layout_height="0.000000dip" android:layout_weight="1.000000">
    <androidx.constraintlayout.widget.ConstraintLayout android:layout_gravity="0x00000031" android:id="@id/layout_lesson_content" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/lesson_content_margin_top" android:layout_marginBottom="@dimen/lesson_content_margin_bottom">
      <androidx.compose.ui.platform.ComposeView android:id="@id/cv_lesson_hard_mode_label" android:visibility="gone" android:layout_width="match_parent" android:layout_height="wrap_content" app:layout_constraintTop_toTopOf="0"/>
      <com.getmimo.ui.lesson.interactive.view.LessonDescriptionView android:id="@id/layout_lesson_description" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/cv_lesson_hard_mode_label" app:layout_constraintWidth_max="@dimen/lessonview_content_maxwidth"/>
      <TextView android:id="@id/tv_ftg_hint" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:text="@string/interaction_hint_ftg" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/layout_lesson_description" app:layout_constraintWidth_max="@dimen/lessonview_content_maxwidth" style="@style/TextInteractionHint"/>
      <com.getmimo.ui.lesson.view.database.DatabaseView android:id="@id/database_view" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_ftg_hint" app:layout_goneMarginTop="@dimen/spacing_m_expandable"/>
      <com.getmimo.ui.lesson.view.code.header.CodeHeaderView android:id="@id/codeheaderview" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_m_expandable" android:layout_marginStart="@dimen/lesson_codeview_margin_start" android:layout_marginEnd="@dimen/lesson_codeview_margin_end" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/database_view" app:layout_goneMarginTop="@dimen/spacing_m_expandable"/>
      <com.getmimo.ui.lesson.view.code.CodeBodyView android:id="@id/codebodyview" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_m_expandable" android:layout_marginStart="@dimen/lesson_codeview_margin_start" android:layout_marginEnd="@dimen/lesson_codeview_margin_end" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/codeheaderview" app:layout_goneMarginTop="@dimen/spacing_m_expandable"/>
      <com.getmimo.ui.lesson.interactive.view.LessonOutputView android:id="@id/lesson_output_layout" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/codebodyview"/>
    </androidx.constraintlayout.widget.ConstraintLayout>
  </ScrollView>
  <com.getmimo.ui.lesson.view.InteractionKeyboardContainerView android:id="@id/interaction_keyboard_fillthegap" android:clipChildren="false" android:clipToPadding="false" android:layout_width="match_parent" android:layout_height="wrap_content" app:contains_ftg="true"/>
</LinearLayout>
```
