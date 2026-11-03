# پروندهٔ لایه — `res/layout/fake_streak_bottomsheet_dialog.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/fake_streak_bottomsheet_dialog.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/fake_streak_bottomsheet_dialog.xml`](../../SOURCE/res/layout/fake_streak_bottomsheet_dialog.xml) |
| SHA-256 دیکد | `f4f9979e2d67f782253bef5ecae098508d1cb0e3a173cf296d1fecb52a19fd96` |
| ریشه | `LinearLayout` |
| تعداد گره | 8 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ TextView
   ├─ com.google.android.material.textfield.TextInputLayout
   │  └─ com.google.android.material.textfield.TextInputEditText  #@id/et_fake_current_streak
   ├─ com.google.android.material.textfield.TextInputLayout
   │  └─ com.google.android.material.textfield.TextInputEditText  #@id/et_fake_best_streak
   ├─ androidx.compose.ui.platform.ComposeView  #@id/btn_fake_streak_data
   └─ androidx.compose.ui.platform.ComposeView  #@id/btn_clear
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 3 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 4 | `TextView` | `android:gravity` | `0x00000011` |
| 5 | `TextView` | `android:layout_width` | `match_parent` |
| 6 | `TextView` | `android:layout_height` | `wrap_content` |
| 7 | `TextView` | `android:layout_marginTop` | `16.000000dip` |
| 8 | `TextView` | `android:text` | `Current streak: 0 - Int.MAXVALUE
Best streak >= Current Streak` |
| 9 | `TextView` | `style` | `@style/TextLabel3` |
| 10 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_gravity` | `0x00000011` |
| 11 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_width` | `200.000000dip` |
| 12 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_height` | `wrap_content` |
| 13 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_marginTop` | `16.000000dip` |
| 14 | `com.google.android.material.textfield.TextInputLayout` | `style` | `@style/Widget.MaterialComponents.TextInputLayout.OutlinedBox` |
| 15 | `com.google.android.material.textfield.TextInputEditText` | `android:id` | `@id/et_fake_current_streak` |
| 16 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_width` | `match_parent` |
| 17 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_height` | `match_parent` |
| 18 | `com.google.android.material.textfield.TextInputEditText` | `android:hint` | `Current streak` |
| 19 | `com.google.android.material.textfield.TextInputEditText` | `android:inputType` | `0x00000002` |
| 20 | `com.google.android.material.textfield.TextInputEditText` | `style` | `@style/TextLabel2` |
| 21 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_gravity` | `0x00000011` |
| 22 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_width` | `200.000000dip` |
| 23 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_height` | `wrap_content` |
| 24 | `com.google.android.material.textfield.TextInputLayout` | `android:layout_marginTop` | `16.000000dip` |
| 25 | `com.google.android.material.textfield.TextInputLayout` | `style` | `@style/Widget.MaterialComponents.TextInputLayout.OutlinedBox` |
| 26 | `com.google.android.material.textfield.TextInputEditText` | `android:id` | `@id/et_fake_best_streak` |
| 27 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_width` | `match_parent` |
| 28 | `com.google.android.material.textfield.TextInputEditText` | `android:layout_height` | `match_parent` |
| 29 | `com.google.android.material.textfield.TextInputEditText` | `android:hint` | `Best streak` |
| 30 | `com.google.android.material.textfield.TextInputEditText` | `android:inputType` | `0x00000002` |
| 31 | `com.google.android.material.textfield.TextInputEditText` | `style` | `@style/TextLabel2` |
| 32 | `androidx.compose.ui.platform.ComposeView` | `android:layout_gravity` | `0x00000011` |
| 33 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_fake_streak_data` |
| 34 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 35 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 36 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `16.000000dip` |
| 37 | `androidx.compose.ui.platform.ComposeView` | `android:layout_gravity` | `0x00000011` |
| 38 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/btn_clear` |
| 39 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `wrap_content` |
| 40 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 41 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginTop` | `8.000000dip` |
| 42 | `androidx.compose.ui.platform.ComposeView` | `android:layout_marginBottom` | `24.000000dip` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/TextLabel2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextLabel3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '12.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '15.599977sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_bold', 'value_type': 'reference'}]` (sw600dp) |
| `@style/Widget.MaterialComponents.TextInputLayout.OutlinedBox` | `[{'attr': 'attr.boxCollapsedPaddingTop', 'attr_id': '0x7F04009B', 'value': '0.000000dip', 'value_type': 'dimension'}, {'attr': 'attr.materialThemeOverlay', 'attr_id': '0x7F040411', 'value': '@style/ThemeOverlay.MaterialComponents.TextInputEditText.OutlinedBox', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/btn_clear
@id/btn_fake_streak_data
@id/et_fake_best_streak
@id/et_fake_current_streak
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:layout_width="match_parent" android:layout_height="wrap_content">
  <TextView android:gravity="0x00000011" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="16.000000dip" android:text="Current streak: 0 - Int.MAXVALUE&#10;Best streak &gt;= Current Streak" style="@style/TextLabel3"/>
  <com.google.android.material.textfield.TextInputLayout android:layout_gravity="0x00000011" android:layout_width="200.000000dip" android:layout_height="wrap_content" android:layout_marginTop="16.000000dip" style="@style/Widget.MaterialComponents.TextInputLayout.OutlinedBox">
    <com.google.android.material.textfield.TextInputEditText android:id="@id/et_fake_current_streak" android:layout_width="match_parent" android:layout_height="match_parent" android:hint="Current streak" android:inputType="0x00000002" style="@style/TextLabel2"/>
  </com.google.android.material.textfield.TextInputLayout>
  <com.google.android.material.textfield.TextInputLayout android:layout_gravity="0x00000011" android:layout_width="200.000000dip" android:layout_height="wrap_content" android:layout_marginTop="16.000000dip" style="@style/Widget.MaterialComponents.TextInputLayout.OutlinedBox">
    <com.google.android.material.textfield.TextInputEditText android:id="@id/et_fake_best_streak" android:layout_width="match_parent" android:layout_height="match_parent" android:hint="Best streak" android:inputType="0x00000002" style="@style/TextLabel2"/>
  </com.google.android.material.textfield.TextInputLayout>
  <androidx.compose.ui.platform.ComposeView android:layout_gravity="0x00000011" android:id="@id/btn_fake_streak_data" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="16.000000dip"/>
  <androidx.compose.ui.platform.ComposeView android:layout_gravity="0x00000011" android:id="@id/btn_clear" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="8.000000dip" android:layout_marginBottom="24.000000dip"/>
</LinearLayout>
```
