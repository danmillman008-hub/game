# پروندهٔ لایه — `res/layout/lesson_interactive_validatedinput_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/lesson_interactive_validatedinput_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/lesson_interactive_validatedinput_fragment.xml`](../../SOURCE/res/layout/lesson_interactive_validatedinput_fragment.xml) |
| SHA-256 دیکد | `b9d1a9b22880c43411ad1a5ff0bfecf9a6f0b296db87e46e74a85593532231f6` |
| ریشه | `LinearLayout` |
| تعداد گره | 12 |
| تعداد شناسه | 11 |
| تگ‌های استفاده‌شده | 12 |
| ویوهای سفارشی `com.getmimo` | 7 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 23 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ ScrollView  #@id/sv_lesson
   │  └─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_lesson_content
   │     ├─ androidx.compose.ui.platform.ComposeView  #@id/cv_lesson_hard_mode_label
   │     ├─ com.getmimo.ui.lesson.interactive.view.LessonDescriptionView  #@id/layout_lesson_description
   │     ├─ TextView  #@id/tv_validated_input_hint
   │     ├─ com.getmimo.ui.lesson.view.database.DatabaseView  #@id/database_view
   │     ├─ com.getmimo.ui.lesson.view.code.header.CodeHeaderView  #@id/codeheaderview
   │     ├─ com.getmimo.ui.lesson.view.code.CodeBodyView  #@id/codebodyview
   │     └─ com.getmimo.ui.lesson.interactive.view.LessonOutputView  #@id/lesson_output_layout
   ├─ com.getmimo.ui.lesson.view.InteractionKeyboardContainerView  #@id/interaction_keyboard_validatedinput
   └─ com.getmimo.ui.codeeditor.codingkeyboard.CodingKeyboardView  #@id/coding_keyboard_view_validated_input
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:background` | `@color/code_background` |
| 3 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 4 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 5 | `ScrollView` | `android:id` | `@id/sv_lesson` |
| 6 | `ScrollView` | `android:layout_width` | `match_parent` |
| 7 | `ScrollView` | `android:layout_height` | `0.000000dip` |
| 8 | `ScrollView` | `android:layout_weight` | `1.000000` |
| 9 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_gravity` | `0x00000031` |
| 10 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:orientation` | `vertical` |
| 11 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/layout_lesson_content` |
| 12 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_primary` |
| 13 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 14 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 15 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginTop` | `@dimen/lesson_content_margin_top` |
| 16 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginBottom` | `@dimen/coding_keyboard_height` |
| 17 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/cv_lesson_hard_mode_label` |
| 18 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `gone` |
| 19 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `match_parent` |
| 20 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 21 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toTopOf` | `0` |
| 22 | `com.getmimo.ui.lesson.interactive.view.LessonDescriptionView` | `android:id` | `@id/layout_lesson_description` |
| 23 | `com.getmimo.ui.lesson.interactive.view.LessonDescriptionView` | `android:layout_width` | `0.000000dip` |
| 24 | `com.getmimo.ui.lesson.interactive.view.LessonDescriptionView` | `android:layout_height` | `wrap_content` |
| 25 | `com.getmimo.ui.lesson.interactive.view.LessonDescriptionView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 26 | `com.getmimo.ui.lesson.interactive.view.LessonDescriptionView` | `app:layout_constraintStart_toStartOf` | `0` |
| 27 | `com.getmimo.ui.lesson.interactive.view.LessonDescriptionView` | `app:layout_constraintTop_toBottomOf` | `@id/cv_lesson_hard_mode_label` |
| 28 | `com.getmimo.ui.lesson.interactive.view.LessonDescriptionView` | `app:layout_constraintWidth_max` | `@dimen/lessonview_content_maxwidth` |
| 29 | `TextView` | `android:id` | `@id/tv_validated_input_hint` |
| 30 | `TextView` | `android:layout_width` | `0.000000dip` |
| 31 | `TextView` | `android:layout_height` | `wrap_content` |
| 32 | `TextView` | `android:text` | `@string/interaction_hint_validated_input` |
| 33 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 34 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 35 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/layout_lesson_description` |
| 36 | `TextView` | `app:layout_constraintWidth_max` | `@dimen/lessonview_content_maxwidth` |
| 37 | `TextView` | `style` | `@style/TextInteractionHint` |
| 38 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `android:id` | `@id/database_view` |
| 39 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `android:visibility` | `gone` |
| 40 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `android:layout_width` | `0.000000dip` |
| 41 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `android:layout_height` | `wrap_content` |
| 42 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 43 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 44 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `app:layout_constraintStart_toStartOf` | `0` |
| 45 | `com.getmimo.ui.lesson.view.database.DatabaseView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_validated_input_hint` |
| 46 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `android:id` | `@id/codeheaderview` |
| 47 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `android:visibility` | `gone` |
| 48 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `android:layout_width` | `0.000000dip` |
| 49 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `android:layout_height` | `wrap_content` |
| 50 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `android:layout_marginBottom` | `@dimen/spacing_m_expandable` |
| 51 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `android:layout_marginStart` | `@dimen/lesson_codeview_margin_start` |
| 52 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `android:layout_marginEnd` | `@dimen/lesson_codeview_margin_end` |
| 53 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 54 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `app:layout_constraintStart_toStartOf` | `0` |
| 55 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `app:layout_constraintTop_toBottomOf` | `@id/database_view` |
| 56 | `com.getmimo.ui.lesson.view.code.header.CodeHeaderView` | `app:layout_goneMarginTop` | `@dimen/spacing_m_expandable` |
| 57 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `android:id` | `@id/codebodyview` |
| 58 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `android:visibility` | `gone` |
| 59 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `android:layout_width` | `0.000000dip` |
| 60 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `android:layout_height` | `wrap_content` |
| 61 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `android:layout_marginBottom` | `@dimen/spacing_m_expandable` |
| 62 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `android:layout_marginStart` | `@dimen/lesson_codeview_margin_start` |
| 63 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `android:layout_marginEnd` | `@dimen/lesson_codeview_margin_end` |
| 64 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 65 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `app:layout_constraintStart_toStartOf` | `0` |
| 66 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `app:layout_constraintTop_toBottomOf` | `@id/codeheaderview` |
| 67 | `com.getmimo.ui.lesson.view.code.CodeBodyView` | `app:layout_goneMarginTop` | `@dimen/spacing_m_expandable` |
| 68 | `com.getmimo.ui.lesson.interactive.view.LessonOutputView` | `android:id` | `@id/lesson_output_layout` |
| 69 | `com.getmimo.ui.lesson.interactive.view.LessonOutputView` | `android:layout_width` | `0.000000dip` |
| 70 | `com.getmimo.ui.lesson.interactive.view.LessonOutputView` | `android:layout_height` | `wrap_content` |
| 71 | `com.getmimo.ui.lesson.interactive.view.LessonOutputView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 72 | `com.getmimo.ui.lesson.interactive.view.LessonOutputView` | `app:layout_constraintStart_toStartOf` | `0` |
| 73 | `com.getmimo.ui.lesson.interactive.view.LessonOutputView` | `app:layout_constraintTop_toBottomOf` | `@id/codebodyview` |
| 74 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `android:id` | `@id/interaction_keyboard_validatedinput` |
| 75 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `android:background` | `@color/transparent` |
| 76 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `android:visibility` | `gone` |
| 77 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `android:clipChildren` | `false` |
| 78 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `android:clipToPadding` | `false` |
| 79 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `android:layout_width` | `match_parent` |
| 80 | `com.getmimo.ui.lesson.view.InteractionKeyboardContainerView` | `android:layout_height` | `wrap_content` |
| 81 | `com.getmimo.ui.codeeditor.codingkeyboard.CodingKeyboardView` | `android:id` | `@id/coding_keyboard_view_validated_input` |
| 82 | `com.getmimo.ui.codeeditor.codingkeyboard.CodingKeyboardView` | `android:visibility` | `gone` |
| 83 | `com.getmimo.ui.codeeditor.codingkeyboard.CodingKeyboardView` | `android:layout_width` | `match_parent` |
| 84 | `com.getmimo.ui.codeeditor.codingkeyboard.CodingKeyboardView` | `android:layout_height` | `@dimen/coding_keyboard_height` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_primary` | `#FFF6F7FB` / `#FF252746` (night) |
| `@color/code_background` | `#FFFFFFFF` / `#FF1D1F32` (night) |
| `@color/transparent` | `#00000000` |
| `@dimen/coding_keyboard_height` | `64.000000dip` |
| `@dimen/lesson_codeview_margin_end` | `0.000000dip` |
| `@dimen/lesson_codeview_margin_start` | `0.000000dip` |
| `@dimen/lesson_content_margin_top` | `8.000000dip` |
| `@dimen/lessonview_content_maxwidth` | `@dimen/content_max_width` |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@dimen/spacing_s` | `12.000000dip` |
| `@string/interaction_hint_validated_input` | `Tap the editor below to enter your solution` / `Tippe auf den Editor unten, um deine Lösung einzugeben` (de) / `Toca el editor de abajo para ingresar tu solución` (es) / `Appuie sur l'éditeur ci-dessous pour entrer ta solution` (fr) / `Ketuk editor di bawah untuk memasukkan solusimu` (in) / `Tocca l'editor qui sotto per inserire la soluzione` (it) / `Dotknij edytora poniżej, aby wpisać rozwiązanie` (pl) / `Toque no editor abaixo para inserir sua solução` (pt-rBR) / `Нажми на редактор ниже, чтобы ввести решение` (ru) / `Çözümünü yazmak için aşağıdaki editöre dokun` (tr) |
| `@style/TextInteractionHint` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_weak', 'value_type': 'reference'}, {'attr': 'android:gravity', 'attr_id': '0x010100AF', 'value': '0x00000010', 'value_type': 'int_hex'}, {'attr': 'android:layout_marginTop', 'attr_id': '0x010100F8', 'value': '@dimen/spacing_l', 'value_type': 'reference'}, {'attr': 'android:drawablePadding', 'attr_id': '0x01010171', 'value': '@dimen/spacing_xxs', 'value_type': 'reference'}, {'attr': 'android:layout_marginStart', 'attr_id': '0x010103B5', 'value': '@dimen/spacing_m', 'value_type': 'reference'}, {'attr': 'android:layout_marginEnd', 'attr_id': '0x010103B6', 'value': '@dimen/spacing_m', 'value_type': 'reference'}, {'attr': 'attr.drawableStartCompat', 'attr_id': '0x7F040217', 'value': '@drawable/ic_info_circle', 'value_type': 'reference'}, {'attr': 'attr.drawableTint', 'attr_id': '0x7F040218', 'value': '@color/text_weak', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/codebodyview
@id/codeheaderview
@id/coding_keyboard_view_validated_input
@id/cv_lesson_hard_mode_label
@id/database_view
@id/interaction_keyboard_validatedinput
@id/layout_lesson_content
@id/layout_lesson_description
@id/lesson_output_layout
@id/sv_lesson
@id/tv_validated_input_hint
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:orientation="vertical" android:background="@color/code_background" android:layout_width="match_parent" android:layout_height="match_parent">
  <ScrollView android:id="@id/sv_lesson" android:layout_width="match_parent" android:layout_height="0.000000dip" android:layout_weight="1.000000">
    <androidx.constraintlayout.widget.ConstraintLayout android:layout_gravity="0x00000031" android:orientation="vertical" android:id="@id/layout_lesson_content" android:background="@color/background_primary" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/lesson_content_margin_top" android:layout_marginBottom="@dimen/coding_keyboard_height">
      <androidx.compose.ui.platform.ComposeView android:id="@id/cv_lesson_hard_mode_label" android:visibility="gone" android:layout_width="match_parent" android:layout_height="wrap_content" app:layout_constraintTop_toTopOf="0"/>
      <com.getmimo.ui.lesson.interactive.view.LessonDescriptionView android:id="@id/layout_lesson_description" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/cv_lesson_hard_mode_label" app:layout_constraintWidth_max="@dimen/lessonview_content_maxwidth"/>
      <TextView android:id="@id/tv_validated_input_hint" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:text="@string/interaction_hint_validated_input" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/layout_lesson_description" app:layout_constraintWidth_max="@dimen/lessonview_content_maxwidth" style="@style/TextInteractionHint"/>
      <com.getmimo.ui.lesson.view.database.DatabaseView android:id="@id/database_view" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_s" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_validated_input_hint"/>
      <com.getmimo.ui.lesson.view.code.header.CodeHeaderView android:id="@id/codeheaderview" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_m_expandable" android:layout_marginStart="@dimen/lesson_codeview_margin_start" android:layout_marginEnd="@dimen/lesson_codeview_margin_end" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/database_view" app:layout_goneMarginTop="@dimen/spacing_m_expandable"/>
      <com.getmimo.ui.lesson.view.code.CodeBodyView android:id="@id/codebodyview" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_m_expandable" android:layout_marginStart="@dimen/lesson_codeview_margin_start" android:layout_marginEnd="@dimen/lesson_codeview_margin_end" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/codeheaderview" app:layout_goneMarginTop="@dimen/spacing_m_expandable"/>
      <com.getmimo.ui.lesson.interactive.view.LessonOutputView android:id="@id/lesson_output_layout" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/codebodyview"/>
    </androidx.constraintlayout.widget.ConstraintLayout>
  </ScrollView>
  <com.getmimo.ui.lesson.view.InteractionKeyboardContainerView android:id="@id/interaction_keyboard_validatedinput" android:background="@color/transparent" android:visibility="gone" android:clipChildren="false" android:clipToPadding="false" android:layout_width="match_parent" android:layout_height="wrap_content"/>
  <com.getmimo.ui.codeeditor.codingkeyboard.CodingKeyboardView android:id="@id/coding_keyboard_view_validated_input" android:visibility="gone" android:layout_width="match_parent" android:layout_height="@dimen/coding_keyboard_height"/>
</LinearLayout>
```
