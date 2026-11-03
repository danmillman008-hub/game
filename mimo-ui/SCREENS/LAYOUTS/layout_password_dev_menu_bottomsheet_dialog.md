# پروندهٔ لایه — `res/layout/password_dev_menu_bottomsheet_dialog.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/password_dev_menu_bottomsheet_dialog.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/password_dev_menu_bottomsheet_dialog.xml`](../../SOURCE/res/layout/password_dev_menu_bottomsheet_dialog.xml) |
| SHA-256 دیکد | `3fb53b3a0e0ec702a1af887607abcb508588d8a400a5e8b7e2c6cd033cc2d1dc` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 10 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ com.google.android.material.textfield.TextInputLayout  #@id/til_name_code
   │  └─ com.google.android.material.textfield.TextInputEditText  #@id/et_name_code
   └─ LinearLayout
      ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_continue
      └─ androidx.compose.ui.platform.ComposeView  #@id/btn_cancel
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_secondary` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:padding` | `@dimen/spacing_m` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 5 | `com.google.android.material.textfield.TextInputLayout` | `android:id` | `@id/til_name_code` |
| 6 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_width` | `match_parent` |
| 7 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_height` | `wrap_content` |
| 8 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 9 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 10 | `com.google.android.material.textfield.TextInputLayout` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 11 | `com.google.android.material.textfield.TextInputLayout` | `style` | `@style/MaterialEditTextLayout` |
| 12 | `com.google.android.material.textfield.TextInputEditText` | `android:id` | `@id/et_name_code` |
| 13 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_width` | `match_parent` |
| 14 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_height` | `wrap_content` |
| 15 | `com.google.android.material.textfield.TextInputEditText` | `android:hint` | `@string/password` |
| 16 | `com.google.android.material.textfield.TextInputEditText` | `android:ems` | `10` |
| 17 | `com.google.android.material.textfield.TextInputEditText` | `android:inputType` | `0x00000061` |
| 18 | `com.google.android.material.textfield.TextInputEditText` | `android:imeOptions` | `0x00000006` |
| 19 | `com.google.android.material.textfield.TextInputEditText` | `style` | `@style/MaterialEditText` |
| 20 | `LinearLayout` | `android:orientation` | `horizontal` |
| 21 | `LinearLayout` | `android:layout_width` | `0.000000dip` |
| 22 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 23 | `LinearLayout` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 24 | `LinearLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 25 | `LinearLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 26 | `LinearLayout` | `app:layout_constraintTop_toBottomOf` | `@id/til_name_code` |
| 27 | `LinearLayout` | `app:layout_constraintWidth_max` | `@dimen/general_max_width` |
| 28 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_continue` |
| 29 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 30 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 31 | `androidx.compose.ui.platform.ComposeView` | `android:layout_weight` | `1.000000` |
| 32 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_cancel` |
| 33 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 34 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 35 | `androidx.compose.ui.platform.ComposeView` | `android:layout_weight` | `1.000000` |
| 36 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginStart` | `@dimen/spacing_m` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |
| `@dimen/general_max_width` | `480.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@string/password` | `Password` / `Passwort` (de) / `Contraseña` (es) / `Mot de passe` (fr) / `Kata sandi` (in) / `Password` (it) / `Hasło` (pl) / `Senha` (pt-rBR) / `Пароль` (ru) / `Şifre` (tr) |
| `@style/MaterialEditText` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_primary', 'value_type': 'reference'}, {'attr': 'android:textColorHint', 'attr_id': '0x0101009A', 'value': '@color/text_weak', 'value_type': 'reference'}, {'attr': 'android:padding', 'attr_id': '0x010100D5', 'value': '@dimen/spacing_s', 'value_type': 'reference'}]` |
| `@style/MaterialEditTextLayout` | `[{'attr': 'android:textColorHint', 'attr_id': '0x0101009A', 'value': '@color/text_disabled', 'value_type': 'reference'}, {'attr': 'android:imeOptions', 'attr_id': '0x01010264', 'value': '0x00000006', 'value_type': 'int_hex'}, {'attr': 'attr.boxBackgroundColor', 'attr_id': '0x7F040099', 'value': '@color/background_secondary', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusBottomEnd', 'attr_id': '0x7F04009C', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusBottomStart', 'attr_id': '0x7F04009D', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusTopEnd', 'attr_id': '0x7F04009E', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxCornerRadiusTopStart', 'attr_id': '0x7F04009F', 'value': '@dimen/spacing_xs', 'value_type': 'reference'}, {'attr': 'attr.boxStrokeColor', 'attr_id': '0x7F0400A0', 'value': '@color/material_edittext_border', 'value_type': 'reference'}, {'attr': 'attr.endIconTint', 'attr_id': '0x7F040236', 'value': '@color/icon_weak', 'value_type': 'reference'}, {'attr': 'attr.hintEnabled', 'attr_id': '0x7F0402E7', 'value': 'false', 'value_type': 'int_boolean'}, {'attr': 'attr.strokeColor', 'attr_id': '0x7F040586', 'value': '@color/material_edittext_border', 'value_type': 'reference'}, {'attr': 'attr.strokeWidth', 'attr_id': '0x7F040587', 'value': '1.000000dip', 'value_type': 'dimension'}]` |

## ۴. شناسه‌های `@id`

```text
@id/btn_cancel
@id/btn_continue
@id/et_name_code
@id/til_name_code
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:background="@color/background_secondary" android:padding="@dimen/spacing_m" android:layout_width="match_parent" android:layout_height="wrap_content">
  <com.google.android.material.textfield.TextInputLayout android:id="@id/til_name_code" android:layout_width="match_parent" android:layout_height="wrap_content" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:layout_constraintWidth_max="@dimen/general_max_width" style="@style/MaterialEditTextLayout">
    <com.google.android.material.textfield.TextInputEditText android:id="@id/et_name_code" android:layout_width="match_parent" android:layout_height="wrap_content" android:hint="@string/password" android:ems="10" android:inputType="0x00000061" android:imeOptions="0x00000006" style="@style/MaterialEditText"/>
  </com.google.android.material.textfield.TextInputLayout>
  <LinearLayout android:orientation="horizontal" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/til_name_code" app:layout_constraintWidth_max="@dimen/general_max_width">
    <androidx.compose.ui.platform.ComposeView android:id="@id/btn_continue" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_weight="1.000000"/>
    <androidx.compose.ui.platform.ComposeView android:id="@id/btn_cancel" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_weight="1.000000" android:layout_marginStart="@dimen/spacing_m"/>
  </LinearLayout>
</androidx.constraintlayout.widget.ConstraintLayout>
```
