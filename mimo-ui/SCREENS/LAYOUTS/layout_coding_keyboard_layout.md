# پروندهٔ لایه — `res/layout/coding_keyboard_layout.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/coding_keyboard_layout.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/coding_keyboard_layout.xml`](../../SOURCE/res/layout/coding_keyboard_layout.xml) |
| SHA-256 دیکد | `eb009846f5ed56faf4ad513e4a1bc1ed393228bde1f8fd9ce463063396a2bb0e` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 8 |
| تعداد شناسه | 7 |
| تگ‌های استفاده‌شده | 7 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 19 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ View  #@id/background
   ├─ ImageView  #@id/iv_ai_tutor_pulse
   ├─ com.google.android.material.button.MaterialButton  #@id/btn_ai_tutor
   ├─ androidx.recyclerview.widget.RecyclerView  #@id/rv_coding_keyboard
   ├─ View  #@id/view_coding_keyboard_gradient
   ├─ com.getmimo.ui.common.runbutton.AnimatedRunButton  #@id/btn_run_code_coding_keyboard
   └─ androidx.constraintlayout.widget.Group  #@id/group_coding_keyboard_aware
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:focusable` | `true` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:clickable` | `true` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:clipChildren` | `false` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:clipToPadding` | `false` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 6 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `@dimen/coding_keyboard_height` |
| 7 | `View` | `android:id` | `@id/background` |
| 8 | `View` | `android:background` | `@color/codingkeyboard_background` |
| 9 | `View` | `android:layout_width` | `0.000000dip` |
| 10 | `View` | `android:layout_height` | `0.000000dip` |
| 11 | `View` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 12 | `View` | `app:layout_constraintEnd_toEndOf` | `0` |
| 13 | `View` | `app:layout_constraintStart_toStartOf` | `0` |
| 14 | `View` | `app:layout_constraintTop_toTopOf` | `@id/rv_coding_keyboard` |
| 15 | `ImageView` | `android:id` | `@id/iv_ai_tutor_pulse` |
| 16 | `ImageView` | `android:visibility` | `gone` |
| 17 | `ImageView` | `android:layout_width` | `1.000000dip` |
| 18 | `ImageView` | `android:layout_height` | `1.000000dip` |
| 19 | `ImageView` | `android:src` | `@drawable/ai_tutor_pulse` |
| 20 | `ImageView` | `android:elevation` | `10.000000dip` |
| 21 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `@id/btn_ai_tutor` |
| 22 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `@id/btn_ai_tutor` |
| 23 | `ImageView` | `app:layout_constraintStart_toStartOf` | `@id/btn_ai_tutor` |
| 24 | `ImageView` | `app:layout_constraintTop_toTopOf` | `@id/btn_ai_tutor` |
| 25 | `com.google.android.material.button.MaterialButton` | `android:id` | `@id/btn_ai_tutor` |
| 26 | `com.google.android.material.button.MaterialButton` | `android:visibility` | `gone` |
| 27 | `com.google.android.material.button.MaterialButton` | `android:clipChildren` | `false` |
| 28 | `com.google.android.material.button.MaterialButton` | `android:clipToPadding` | `false` |
| 29 | `com.google.android.material.button.MaterialButton` | `android:layout_width` | `wrap_content` |
| 30 | `com.google.android.material.button.MaterialButton` | `android:layout_height` | `0.000000dip` |
| 31 | `com.google.android.material.button.MaterialButton` | `android:layout_margin` | `@dimen/spacing_xxs` |
| 32 | `com.google.android.material.button.MaterialButton` | `android:layout_marginVertical` | `@dimen/spacing_xxs` |
| 33 | `com.google.android.material.button.MaterialButton` | `android:paddingHorizontal` | `@dimen/spacing_xs` |
| 34 | `com.google.android.material.button.MaterialButton` | `app:backgroundTint` | `@color/selection_enabled` |
| 35 | `com.google.android.material.button.MaterialButton` | `app:cornerRadius` | `@dimen/spacing_xs` |
| 36 | `com.google.android.material.button.MaterialButton` | `app:icon` | `@drawable/ic_ai_tutor` |
| 37 | `com.google.android.material.button.MaterialButton` | `app:iconSize` | `24.000000dip` |
| 38 | `com.google.android.material.button.MaterialButton` | `app:iconTint` | `@color/icon_primary` |
| 39 | `com.google.android.material.button.MaterialButton` | `app:layout_constraintBottom_toBottomOf` | `@id/rv_coding_keyboard` |
| 40 | `com.google.android.material.button.MaterialButton` | `app:layout_constraintStart_toStartOf` | `0` |
| 41 | `com.google.android.material.button.MaterialButton` | `app:layout_constraintTop_toTopOf` | `@id/rv_coding_keyboard` |
| 42 | `com.google.android.material.button.MaterialButton` | `style` | `@style/MaterialIconOnlyFilledButton` |
| 43 | `androidx.recyclerview.widget.RecyclerView` | `android:orientation` | `horizontal` |
| 44 | `androidx.recyclerview.widget.RecyclerView` | `android:id` | `@id/rv_coding_keyboard` |
| 45 | `androidx.recyclerview.widget.RecyclerView` | `android:clipChildren` | `false` |
| 46 | `androidx.recyclerview.widget.RecyclerView` | `android:clipToPadding` | `false` |
| 47 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_width` | `0.000000dip` |
| 48 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_height` | `@dimen/coding_keyboard_snippet_height` |
| 49 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_marginStart` | `@dimen/spacing_xxs` |
| 50 | `androidx.recyclerview.widget.RecyclerView` | `app:layoutManager` | `androidx.recyclerview.widget.LinearLayoutManager` |
| 51 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 52 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintEnd_toStartOf` | `@id/btn_run_code_coding_keyboard` |
| 53 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintHorizontal_weight` | `1.000000` |
| 54 | `androidx.recyclerview.widget.RecyclerView` | `app:layout_constraintStart_toEndOf` | `@id/btn_ai_tutor` |
| 55 | `View` | `android:id` | `@id/view_coding_keyboard_gradient` |
| 56 | `View` | `android:background` | `@drawable/bg_coding_keyboard_gradient` |
| 57 | `View` | `android:layout_width` | `100.000000dip` |
| 58 | `View` | `android:layout_height` | `0.000000dip` |
| 59 | `View` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 60 | `View` | `app:layout_constraintEnd_toEndOf` | `0` |
| 61 | `View` | `app:layout_constraintTop_toTopOf` | `@id/rv_coding_keyboard` |
| 62 | `com.getmimo.ui.common.runbutton.AnimatedRunButton` | `android:gravity` | `0x00000011` |
| 63 | `com.getmimo.ui.common.runbutton.AnimatedRunButton` | `android:id` | `@id/btn_run_code_coding_keyboard` |
| 64 | `com.getmimo.ui.common.runbutton.AnimatedRunButton` | `android:layout_width` | `0.000000dip` |
| 65 | `com.getmimo.ui.common.runbutton.AnimatedRunButton` | `android:layout_height` | `0.000000dip` |
| 66 | `com.getmimo.ui.common.runbutton.AnimatedRunButton` | `android:layout_marginEnd` | `@dimen/spacing_s` |
| 67 | `com.getmimo.ui.common.runbutton.AnimatedRunButton` | `android:layout_marginVertical` | `@dimen/spacing_xs` |
| 68 | `com.getmimo.ui.common.runbutton.AnimatedRunButton` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 69 | `com.getmimo.ui.common.runbutton.AnimatedRunButton` | `app:layout_constraintDimensionRatio` | `H,1:1` |
| 70 | `com.getmimo.ui.common.runbutton.AnimatedRunButton` | `app:layout_constraintEnd_toEndOf` | `0` |
| 71 | `com.getmimo.ui.common.runbutton.AnimatedRunButton` | `app:layout_constraintTop_toTopOf` | `0` |
| 72 | `androidx.constraintlayout.widget.Group` | `android:id` | `@id/group_coding_keyboard_aware` |
| 73 | `androidx.constraintlayout.widget.Group` | `android:layout_width` | `0.000000dip` |
| 74 | `androidx.constraintlayout.widget.Group` | `android:layout_height` | `0.000000dip` |
| 75 | `androidx.constraintlayout.widget.Group` | `app:constraint_referenced_ids` | `rv_coding_keyboard,background` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/codingkeyboard_background` | `#FFF6F7FB` / `#FF333661` (night) |
| `@color/icon_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/selection_enabled` | `#FFFFFFFF` / `#FF3F4273` (night) |
| `@dimen/coding_keyboard_height` | `64.000000dip` |
| `@dimen/coding_keyboard_snippet_height` | `44.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@dimen/spacing_xxs` | `4.000000dip` |
| `@style/MaterialIconOnlyFilledButton` | `[{'attr': 'android:paddingLeft', 'attr_id': '0x010100D6', 'value': '8.000000dip', 'value_type': 'dimension'}, {'attr': 'android:paddingRight', 'attr_id': '0x010100D8', 'value': '8.000000dip', 'value_type': 'dimension'}, {'attr': 'android:minWidth', 'attr_id': '0x0101013F', 'value': '48.000000dip', 'value_type': 'dimension'}, {'attr': 'android:minHeight', 'attr_id': '0x01010140', 'value': '48.000000dip', 'value_type': 'dimension'}, {'attr': 'android:insetTop', 'attr_id': '0x010101B9', 'value': '0.000000dip', 'value_type': 'dimension'}, {'attr': 'android:insetBottom', 'attr_id': '0x010101BA', 'value': '0.000000dip', 'value_type': 'dimension'}, {'attr': 'attr.iconGravity', 'attr_id': '0x7F0402F5', 'value': '0x00000002', 'value_type': 'int_hex'}, {'attr': 'attr.iconPadding', 'attr_id': '0x7F0402F7', 'value': '0.000000dip', 'value_type': 'dimension'}, {'attr': 'attr.shapeAppearance', 'attr_id': '0x7F040521', 'value': '@style/MaterialButtonShape', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/background
@id/btn_ai_tutor
@id/btn_run_code_coding_keyboard
@id/group_coding_keyboard_aware
@id/iv_ai_tutor_pulse
@id/rv_coding_keyboard
@id/view_coding_keyboard_gradient
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:focusable="true" android:clickable="true" android:clipChildren="false" android:clipToPadding="false" android:layout_width="match_parent" android:layout_height="@dimen/coding_keyboard_height">
  <View android:id="@id/background" android:background="@color/codingkeyboard_background" android:layout_width="0.000000dip" android:layout_height="0.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="@id/rv_coding_keyboard"/>
  <ImageView android:id="@id/iv_ai_tutor_pulse" android:visibility="gone" android:layout_width="1.000000dip" android:layout_height="1.000000dip" android:src="@drawable/ai_tutor_pulse" android:elevation="10.000000dip" app:layout_constraintBottom_toBottomOf="@id/btn_ai_tutor" app:layout_constraintEnd_toEndOf="@id/btn_ai_tutor" app:layout_constraintStart_toStartOf="@id/btn_ai_tutor" app:layout_constraintTop_toTopOf="@id/btn_ai_tutor"/>
  <com.google.android.material.button.MaterialButton android:id="@id/btn_ai_tutor" android:visibility="gone" android:clipChildren="false" android:clipToPadding="false" android:layout_width="wrap_content" android:layout_height="0.000000dip" android:layout_margin="@dimen/spacing_xxs" android:layout_marginVertical="@dimen/spacing_xxs" android:paddingHorizontal="@dimen/spacing_xs" app:backgroundTint="@color/selection_enabled" app:cornerRadius="@dimen/spacing_xs" app:icon="@drawable/ic_ai_tutor" app:iconSize="24.000000dip" app:iconTint="@color/icon_primary" app:layout_constraintBottom_toBottomOf="@id/rv_coding_keyboard" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="@id/rv_coding_keyboard" style="@style/MaterialIconOnlyFilledButton"/>
  <androidx.recyclerview.widget.RecyclerView android:orientation="horizontal" android:id="@id/rv_coding_keyboard" android:clipChildren="false" android:clipToPadding="false" android:layout_width="0.000000dip" android:layout_height="@dimen/coding_keyboard_snippet_height" android:layout_marginStart="@dimen/spacing_xxs" app:layoutManager="androidx.recyclerview.widget.LinearLayoutManager" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toStartOf="@id/btn_run_code_coding_keyboard" app:layout_constraintHorizontal_weight="1.000000" app:layout_constraintStart_toEndOf="@id/btn_ai_tutor"/>
  <View android:id="@id/view_coding_keyboard_gradient" android:background="@drawable/bg_coding_keyboard_gradient" android:layout_width="100.000000dip" android:layout_height="0.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="@id/rv_coding_keyboard"/>
  <com.getmimo.ui.common.runbutton.AnimatedRunButton android:gravity="0x00000011" android:id="@id/btn_run_code_coding_keyboard" android:layout_width="0.000000dip" android:layout_height="0.000000dip" android:layout_marginEnd="@dimen/spacing_s" android:layout_marginVertical="@dimen/spacing_xs" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintDimensionRatio="H,1:1" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0"/>
  <androidx.constraintlayout.widget.Group android:id="@id/group_coding_keyboard_aware" android:layout_width="0.000000dip" android:layout_height="0.000000dip" app:constraint_referenced_ids="rv_coding_keyboard,background"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
