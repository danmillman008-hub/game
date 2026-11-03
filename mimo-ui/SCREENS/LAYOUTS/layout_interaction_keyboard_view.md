# پروندهٔ لایه — `res/layout/interaction_keyboard_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/interaction_keyboard_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/interaction_keyboard_view.xml`](../../SOURCE/res/layout/interaction_keyboard_view.xml) |
| SHA-256 دیکد | `a35a1609312c179dd5768233e2d5c93b05b1d1a371a16c4719d3a216f550431b` |
| ریشه | `merge` |
| تعداد گره | 6 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 9 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   ├─ View  #@id/border_top
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_reset
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_undo
   ├─ com.getmimo.ui.common.runbutton.RunButton  #@id/btn_run
   └─ androidx.compose.ui.platform.ComposeView  #@id/fab_code_playground
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `View` | `android:id` | `@id/border_top` |
| 2 | `View` | `android:background` | `@color/line_primary` |
| 3 | `View` | `android:layout_width` | `match_parent` |
| 4 | `View` | `android:layout_height` | `1.000000dip` |
| 5 | `View` | `app:layout_constraintTop_toTopOf` | `0` |
| 6 | `androidx.compose.ui.platform.ComposeView` | `android:enabled` | `false` |
| 7 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_reset` |
| 8 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `invisible` |
| 9 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `48.000000dip` |
| 10 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `48.000000dip` |
| 11 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginStart` | `@dimen/spacing_xxs_expandable` |
| 12 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 13 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 14 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/border_top` |
| 15 | `androidx.compose.ui.platform.ComposeView` | `android:enabled` | `false` |
| 16 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_undo` |
| 17 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `invisible` |
| 18 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `48.000000dip` |
| 19 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `48.000000dip` |
| 20 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 21 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toEndOf` | `@id/btn_reset` |
| 22 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toBottomOf` | `@id/border_top` |
| 23 | `com.getmimo.ui.common.runbutton.RunButton` | `android:id` | `@id/btn_run` |
| 24 | `com.getmimo.ui.common.runbutton.RunButton` | `android:clipChildren` | `false` |
| 25 | `com.getmimo.ui.common.runbutton.RunButton` | `android:clipToPadding` | `false` |
| 26 | `com.getmimo.ui.common.runbutton.RunButton` | `android:layout_width` | `0.000000dip` |
| 27 | `com.getmimo.ui.common.runbutton.RunButton` | `android:layout_height` | `wrap_content` |
| 28 | `com.getmimo.ui.common.runbutton.RunButton` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 29 | `com.getmimo.ui.common.runbutton.RunButton` | `app:layout_constraintEnd_toEndOf` | `0` |
| 30 | `com.getmimo.ui.common.runbutton.RunButton` | `app:layout_constraintStart_toEndOf` | `@id/fab_code_playground` |
| 31 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/fab_code_playground` |
| 32 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 33 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 34 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/interaction_keyboard_button_margin_bottom` |
| 35 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginStart` | `@dimen/spacing_m_expandable` |
| 36 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 37 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/line_primary` | `#FFEDEEF6` / `#FF3F4273` (night) |
| `@dimen/interaction_keyboard_button_margin_bottom` | `12.000000dip` |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@dimen/spacing_xxs_expandable` | `4.000000dip` / `6.000000dip` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/border_top
@id/btn_reset
@id/btn_run
@id/btn_undo
@id/fab_code_playground
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
<merge xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto">
  <View android:id="@id/border_top" android:background="@color/line_primary" android:layout_width="match_parent" android:layout_height="1.000000dip" app:layout_constraintTop_toTopOf="0"/>
  <androidx.compose.ui.platform.ComposeView android:enabled="false" android:id="@id/btn_reset" android:visibility="invisible" android:layout_width="48.000000dip" android:layout_height="48.000000dip" android:layout_marginStart="@dimen/spacing_xxs_expandable" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/border_top"/>
  <androidx.compose.ui.platform.ComposeView android:enabled="false" android:id="@id/btn_undo" android:visibility="invisible" android:layout_width="48.000000dip" android:layout_height="48.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toEndOf="@id/btn_reset" app:layout_constraintTop_toBottomOf="@id/border_top"/>
  <com.getmimo.ui.common.runbutton.RunButton android:id="@id/btn_run" android:clipChildren="false" android:clipToPadding="false" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toEndOf="@id/fab_code_playground"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/fab_code_playground" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/interaction_keyboard_button_margin_bottom" android:layout_marginStart="@dimen/spacing_m_expandable" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0"/>
</merge>
```
