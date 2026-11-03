# پروندهٔ لایه — `res/layout/run_button_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/run_button_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/run_button_view.xml`](../../SOURCE/res/layout/run_button_view.xml) |
| SHA-256 دیکد | `81a3a410835d795fc59118093352efde9a3f4fe2f2619044e56b5395b026bbce` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 9 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/run_button_root
   ├─ com.getmimo.ui.common.runbutton.AnimatedRunButton  #@id/btn_play
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_continue_big
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_submit
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/run_button_root` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:clipChildren` | `false` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:clipToPadding` | `false` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 6 | `com.getmimo.ui.common.runbutton.AnimatedRunButton` | `android:id` | `@id/btn_play` |
| 7 | `com.getmimo.ui.common.runbutton.AnimatedRunButton` | `android:clipChildren` | `false` |
| 8 | `com.getmimo.ui.common.runbutton.AnimatedRunButton` | `android:clipToPadding` | `false` |
| 9 | `com.getmimo.ui.common.runbutton.AnimatedRunButton` | `android:layout_width` | `48.000000dip` |
| 10 | `com.getmimo.ui.common.runbutton.AnimatedRunButton` | `android:layout_height` | `48.000000dip` |
| 11 | `com.getmimo.ui.common.runbutton.AnimatedRunButton` | `android:layout_marginBottom` | `@dimen/spacing_m` |
| 12 | `com.getmimo.ui.common.runbutton.AnimatedRunButton` | `android:foreground` | `?attr/selectableItemBackgroundBorderless` |
| 13 | `com.getmimo.ui.common.runbutton.AnimatedRunButton` | `android:layout_marginEnd` | `@dimen/spacing_m_expandable` |
| 14 | `com.getmimo.ui.common.runbutton.AnimatedRunButton` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 15 | `com.getmimo.ui.common.runbutton.AnimatedRunButton` | `app:layout_constraintEnd_toEndOf` | `0` |
| 16 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_continue_big` |
| 17 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `gone` |
| 18 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 19 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 20 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/interaction_keyboard_button_margin_bottom` |
| 21 | `androidx.compose.ui.platform.ComposeView` | `android:minWidth` | `@dimen/interaction_keyboard_button_width` |
| 22 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m_expandable` |
| 23 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 24 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 25 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 26 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_submit` |
| 27 | `androidx.compose.ui.platform.ComposeView` | `android:visibility` | `gone` |
| 28 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 29 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 30 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `@dimen/interaction_keyboard_button_margin_bottom` |
| 31 | `androidx.compose.ui.platform.ComposeView` | `android:minWidth` | `@dimen/interaction_keyboard_button_width` |
| 32 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginHorizontal` | `@dimen/spacing_m_expandable` |
| 33 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 34 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 35 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/interaction_keyboard_button_margin_bottom` | `12.000000dip` |
| `@dimen/interaction_keyboard_button_width` | `140.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/btn_continue_big
@id/btn_play
@id/btn_submit
@id/run_button_root
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:id="@id/run_button_root" android:clipChildren="false" android:clipToPadding="false" android:layout_width="match_parent" android:layout_height="wrap_content">
  <com.getmimo.ui.common.runbutton.AnimatedRunButton android:id="@id/btn_play" android:clipChildren="false" android:clipToPadding="false" android:layout_width="48.000000dip" android:layout_height="48.000000dip" android:layout_marginBottom="@dimen/spacing_m" android:foreground="?attr/selectableItemBackgroundBorderless" android:layout_marginEnd="@dimen/spacing_m_expandable" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_continue_big" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/interaction_keyboard_button_margin_bottom" android:minWidth="@dimen/interaction_keyboard_button_width" android:layout_marginHorizontal="@dimen/spacing_m_expandable" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0"/>
  <androidx.compose.ui.platform.ComposeView android:id="@id/btn_submit" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/interaction_keyboard_button_margin_bottom" android:minWidth="@dimen/interaction_keyboard_button_width" android:layout_marginHorizontal="@dimen/spacing_m_expandable" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
