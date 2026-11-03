# پروندهٔ لایه — `res/layout/code_header_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/code_header_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/code_header_view.xml`](../../SOURCE/res/layout/code_header_view.xml) |
| SHA-256 دیکد | `ee0cf86c45c34ad0e9397a2c3e807a385c536e2057a3184570b940afa8b743ea` |
| ریشه | `merge` |
| تعداد گره | 10 |
| تعداد شناسه | 9 |
| تگ‌های استفاده‌شده | 7 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 20 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   ├─ com.google.android.material.tabs.TabLayout  #@id/code_header_tablayout
   ├─ Space  #@id/tab_start_margin
   ├─ View  #@id/view_coding_keyboard_gradient_start
   ├─ View  #@id/view_coding_keyboard_gradient_end
   ├─ com.getmimo.ui.common.CodeViewActionButton  #@id/btn_action_add
   ├─ com.getmimo.ui.common.CodeViewActionButton  #@id/btn_action
   ├─ androidx.compose.ui.platform.ComposeView  #@id/code_header_run_button
   ├─ androidx.constraintlayout.widget.Barrier  #@id/barrier_end_of_header
   └─ View  #@id/code_header_separator
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `com.google.android.material.tabs.TabLayout` | `android:gravity` | `0x00800013` |
| 2 | `com.google.android.material.tabs.TabLayout` | `android:id` | `@id/code_header_tablayout` |
| 3 | `com.google.android.material.tabs.TabLayout` | `android:focusable` | `true` |
| 4 | `com.google.android.material.tabs.TabLayout` | `android:focusableInTouchMode` | `true` |
| 5 | `com.google.android.material.tabs.TabLayout` | `android:layout_width` | `0.000000dip` |
| 6 | `com.google.android.material.tabs.TabLayout` | `android:layout_height` | `48.000000dip` |
| 7 | `com.google.android.material.tabs.TabLayout` | `android:paddingStart` | `@dimen/spacing_s` |
| 8 | `com.google.android.material.tabs.TabLayout` | `app:layout_constraintEnd_toStartOf` | `@id/barrier_end_of_header` |
| 9 | `com.google.android.material.tabs.TabLayout` | `app:layout_constraintStart_toEndOf` | `@id/tab_start_margin` |
| 10 | `com.google.android.material.tabs.TabLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 11 | `com.google.android.material.tabs.TabLayout` | `style` | `@style/CodeEditorTabLayout` |
| 12 | `Space` | `android:id` | `@id/tab_start_margin` |
| 13 | `Space` | `android:visibility` | `gone` |
| 14 | `Space` | `android:layout_width` | `@dimen/spacing_xl` |
| 15 | `Space` | `android:layout_height` | `0.000000dip` |
| 16 | `Space` | `app:layout_constraintBottom_toBottomOf` | `@id/btn_action_add` |
| 17 | `Space` | `app:layout_constraintStart_toStartOf` | `@id/btn_action_add` |
| 18 | `Space` | `app:layout_constraintTop_toTopOf` | `@id/btn_action_add` |
| 19 | `View` | `android:id` | `@id/view_coding_keyboard_gradient_start` |
| 20 | `View` | `android:background` | `@drawable/bg_code_header_action_button_gradient_start` |
| 21 | `View` | `android:visibility` | `gone` |
| 22 | `View` | `android:layout_width` | `56.000000dip` |
| 23 | `View` | `android:layout_height` | `0.000000dip` |
| 24 | `View` | `app:layout_constraintBottom_toTopOf` | `@id/code_header_separator` |
| 25 | `View` | `app:layout_constraintEnd_toStartOf` | `@id/code_header_tablayout` |
| 26 | `View` | `app:layout_constraintStart_toStartOf` | `@id/code_header_tablayout` |
| 27 | `View` | `app:layout_constraintTop_toTopOf` | `0` |
| 28 | `View` | `android:id` | `@id/view_coding_keyboard_gradient_end` |
| 29 | `View` | `android:background` | `@drawable/bg_code_header_action_button_gradient` |
| 30 | `View` | `android:visibility` | `gone` |
| 31 | `View` | `android:layout_width` | `56.000000dip` |
| 32 | `View` | `android:layout_height` | `0.000000dip` |
| 33 | `View` | `app:layout_constraintBottom_toTopOf` | `@id/code_header_separator` |
| 34 | `View` | `app:layout_constraintEnd_toEndOf` | `@id/code_header_tablayout` |
| 35 | `View` | `app:layout_constraintStart_toEndOf` | `@id/code_header_tablayout` |
| 36 | `View` | `app:layout_constraintTop_toTopOf` | `0` |
| 37 | `com.getmimo.ui.common.CodeViewActionButton` | `android:layout_gravity` | `0x00800035` |
| 38 | `com.getmimo.ui.common.CodeViewActionButton` | `android:id` | `@id/btn_action_add` |
| 39 | `com.getmimo.ui.common.CodeViewActionButton` | `android:background` | `?attr/selectableItemBackground` |
| 40 | `com.getmimo.ui.common.CodeViewActionButton` | `android:visibility` | `gone` |
| 41 | `com.getmimo.ui.common.CodeViewActionButton` | `android:layout_width` | `wrap_content` |
| 42 | `com.getmimo.ui.common.CodeViewActionButton` | `android:layout_height` | `wrap_content` |
| 43 | `com.getmimo.ui.common.CodeViewActionButton` | `android:paddingStart` | `@dimen/spacing_m` |
| 44 | `com.getmimo.ui.common.CodeViewActionButton` | `android:paddingEnd` | `@dimen/spacing_m` |
| 45 | `com.getmimo.ui.common.CodeViewActionButton` | `app:layout_constraintBottom_toTopOf` | `@id/code_header_separator` |
| 46 | `com.getmimo.ui.common.CodeViewActionButton` | `app:layout_constraintStart_toStartOf` | `0` |
| 47 | `com.getmimo.ui.common.CodeViewActionButton` | `app:layout_constraintTop_toTopOf` | `0` |
| 48 | `com.getmimo.ui.common.CodeViewActionButton` | `android:layout_gravity` | `0x00800035` |
| 49 | `com.getmimo.ui.common.CodeViewActionButton` | `android:id` | `@id/btn_action` |
| 50 | `com.getmimo.ui.common.CodeViewActionButton` | `android:background` | `?attr/selectableItemBackground` |
| 51 | `com.getmimo.ui.common.CodeViewActionButton` | `android:visibility` | `gone` |
| 52 | `com.getmimo.ui.common.CodeViewActionButton` | `android:layout_width` | `wrap_content` |
| 53 | `com.getmimo.ui.common.CodeViewActionButton` | `android:layout_height` | `wrap_content` |
| 54 | `com.getmimo.ui.common.CodeViewActionButton` | `android:paddingStart` | `@dimen/code_editor_btn_expand_padding` |
| 55 | `com.getmimo.ui.common.CodeViewActionButton` | `android:paddingEnd` | `@dimen/code_editor_btn_expand_padding` |
| 56 | `com.getmimo.ui.common.CodeViewActionButton` | `app:layout_constraintBottom_toTopOf` | `@id/code_header_separator` |
| 57 | `com.getmimo.ui.common.CodeViewActionButton` | `app:layout_constraintEnd_toEndOf` | `0` |
| 58 | `com.getmimo.ui.common.CodeViewActionButton` | `app:layout_constraintTop_toTopOf` | `0` |
| 59 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/code_header_run_button` |
| 60 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `gone` |
| 61 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 62 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 63 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginStart` | `@dimen/spacing_xxs` |
| 64 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginEnd` | `@dimen/spacing_xs` |
| 65 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toTopOf` | `@id/code_header_separator` |
| 66 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 67 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toTopOf` | `0` |
| 68 | `androidx.constraintlayout.widget.Barrier` | `android:id` | `@id/barrier_end_of_header` |
| 69 | `androidx.constraintlayout.widget.Barrier` | `android:layout_width` | `0.000000dip` |
| 70 | `androidx.constraintlayout.widget.Barrier` | `android:layout_height` | `0.000000dip` |
| 71 | `androidx.constraintlayout.widget.Barrier` | `app:barrierDirection` | `5` |
| 72 | `androidx.constraintlayout.widget.Barrier` | `app:constraint_referenced_ids` | `btn_action,code_header_run_button` |
| 73 | `View` | `android:id` | `@id/code_header_separator` |
| 74 | `View` | `android:background` | `@color/line_primary` |
| 75 | `View` | `android:layout_width` | `match_parent` |
| 76 | `View` | `android:layout_height` | `1.000000dip` |
| 77 | `View` | `app:layout_constraintBottom_toBottomOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/line_primary` | `#FFEDEEF6` / `#FF3F4273` (night) |
| `@dimen/code_editor_btn_expand_padding` | `8.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@dimen/spacing_xxs` | `4.000000dip` |
| `@style/CodeEditorTabLayout` | `[{'attr': 'attr.tabBackground', 'attr_id': '0x7F04059F', 'value': '@color/transparent', 'value_type': 'reference'}, {'attr': 'attr.tabGravity', 'attr_id': '0x7F0405A1', 'value': '0', 'value_type': 'int_dec'}, {'attr': 'attr.tabIndicator', 'attr_id': '0x7F0405A4', 'value': '@drawable/tab_indicator', 'value_type': 'reference'}, {'attr': 'attr.tabIndicatorHeight', 'attr_id': '0x7F0405AA', 'value': '2.000000dip', 'value_type': 'dimension'}, {'attr': 'attr.tabMinWidth', 'attr_id': '0x7F0405AD', 'value': '0.000000dip', 'value_type': 'dimension'}, {'attr': 'attr.tabMode', 'attr_id': '0x7F0405AE', 'value': '0', 'value_type': 'int_dec'}, {'attr': 'attr.tabPadding', 'attr_id': '0x7F0405AF', 'value': '0.000000dip', 'value_type': 'dimension'}, {'attr': 'attr.tabSelectedTextColor', 'attr_id': '0x7F0405B7', 'value': '@color/text_primary', 'value_type': 'reference'}, {'attr': 'attr.tabTextAppearance', 'attr_id': '0x7F0405B9', 'value': '@style/TextCodeEditorTitleWithMultipleTabs', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/barrier_end_of_header
@id/btn_action
@id/btn_action_add
@id/code_header_run_button
@id/code_header_separator
@id/code_header_tablayout
@id/tab_start_margin
@id/view_coding_keyboard_gradient_end
@id/view_coding_keyboard_gradient_start
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
<merge xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android">
  <com.google.android.material.tabs.TabLayout android:gravity="0x00800013" android:id="@id/code_header_tablayout" android:focusable="true" android:focusableInTouchMode="true" android:layout_width="0.000000dip" android:layout_height="48.000000dip" android:paddingStart="@dimen/spacing_s" app:layout_constraintEnd_toStartOf="@id/barrier_end_of_header" app:layout_constraintStart_toEndOf="@id/tab_start_margin" app:layout_constraintTop_toTopOf="0" style="@style/CodeEditorTabLayout"/>
  <Space android:id="@id/tab_start_margin" android:visibility="gone" android:layout_width="@dimen/spacing_xl" android:layout_height="0.000000dip" app:layout_constraintBottom_toBottomOf="@id/btn_action_add" app:layout_constraintStart_toStartOf="@id/btn_action_add" app:layout_constraintTop_toTopOf="@id/btn_action_add"/>
  <View android:id="@id/view_coding_keyboard_gradient_start" android:background="@drawable/bg_code_header_action_button_gradient_start" android:visibility="gone" android:layout_width="56.000000dip" android:layout_height="0.000000dip" app:layout_constraintBottom_toTopOf="@id/code_header_separator" app:layout_constraintEnd_toStartOf="@id/code_header_tablayout" app:layout_constraintStart_toStartOf="@id/code_header_tablayout" app:layout_constraintTop_toTopOf="0"/>
  <View android:id="@id/view_coding_keyboard_gradient_end" android:background="@drawable/bg_code_header_action_button_gradient" android:visibility="gone" android:layout_width="56.000000dip" android:layout_height="0.000000dip" app:layout_constraintBottom_toTopOf="@id/code_header_separator" app:layout_constraintEnd_toEndOf="@id/code_header_tablayout" app:layout_constraintStart_toEndOf="@id/code_header_tablayout" app:layout_constraintTop_toTopOf="0"/>
  <com.getmimo.ui.common.CodeViewActionButton android:layout_gravity="0x00800035" android:id="@id/btn_action_add" android:background="?attr/selectableItemBackground" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:paddingStart="@dimen/spacing_m" android:paddingEnd="@dimen/spacing_m" app:layout_constraintBottom_toTopOf="@id/code_header_separator" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  <com.getmimo.ui.common.CodeViewActionButton android:layout_gravity="0x00800035" android:id="@id/btn_action" android:background="?attr/selectableItemBackground" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:paddingStart="@dimen/code_editor_btn_expand_padding" android:paddingEnd="@dimen/code_editor_btn_expand_padding" app:layout_constraintBottom_toTopOf="@id/code_header_separator" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/code_header_run_button" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginStart="@dimen/spacing_xxs" android:layout_marginEnd="@dimen/spacing_xs" app:layout_constraintBottom_toTopOf="@id/code_header_separator" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0"/>
  <androidx.constraintlayout.widget.Barrier android:id="@id/barrier_end_of_header" android:layout_width="0.000000dip" android:layout_height="0.000000dip" app:barrierDirection="5" app:constraint_referenced_ids="btn_action,code_header_run_button"/>
  <View android:id="@id/code_header_separator" android:background="@color/line_primary" android:layout_width="match_parent" android:layout_height="1.000000dip" app:layout_constraintBottom_toBottomOf="0"/>
</merge>
```
