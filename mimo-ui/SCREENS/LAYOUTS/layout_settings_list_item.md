# پروندهٔ لایه — `res/layout/settings_list_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/settings_list_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/settings_list_item.xml`](../../SOURCE/res/layout/settings_list_item.xml) |
| SHA-256 دیکد | `afef487ae8c05ab2d9b3939d50cbca368d93664558ee1a15dc6b62c1bd0ebe9b` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 14 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ View
   ├─ ImageView  #@id/iv_settings_item_icon
   ├─ TextView  #@id/tv_settings_item_title
   └─ TextView  #@id/tv_settings_item_value
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:gravity` | `0x00000010` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_secondary` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `@dimen/developer_menu_item_height` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:foreground` | `?attr/selectableItemBackground` |
| 6 | `View` | `android:background` | `@color/line_primary` |
| 7 | `View` | `android:layout_width` | `match_parent` |
| 8 | `View` | `android:layout_height` | `1.000000dip` |
| 9 | `View` | `app:layout_constraintEnd_toEndOf` | `0` |
| 10 | `View` | `app:layout_constraintStart_toStartOf` | `0` |
| 11 | `View` | `app:layout_constraintTop_toTopOf` | `0` |
| 12 | `ImageView` | `android:id` | `@id/iv_settings_item_icon` |
| 13 | `ImageView` | `android:layout_width` | `@dimen/icon_size_large` |
| 14 | `ImageView` | `android:layout_height` | `@dimen/icon_size_large` |
| 15 | `ImageView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 16 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 17 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 18 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 19 | `ImageView` | `app:tint` | `@color/icon_weak` |
| 20 | `TextView` | `android:textColor` | `@color/text_primary` |
| 21 | `TextView` | `android:ellipsize` | `end` |
| 22 | `TextView` | `android:id` | `@id/tv_settings_item_title` |
| 23 | `TextView` | `android:layout_width` | `0.000000dip` |
| 24 | `TextView` | `android:layout_height` | `wrap_content` |
| 25 | `TextView` | `android:lines` | `1` |
| 26 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 27 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_xs` |
| 28 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `@id/iv_settings_item_icon` |
| 29 | `TextView` | `app:layout_constraintEnd_toStartOf` | `@id/tv_settings_item_value` |
| 30 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_settings_item_icon` |
| 31 | `TextView` | `app:layout_constraintTop_toTopOf` | `@id/iv_settings_item_icon` |
| 32 | `TextView` | `style` | `@style/TextP1` |
| 33 | `TextView` | `android:textColor` | `@color/text_weak` |
| 34 | `TextView` | `android:id` | `@id/tv_settings_item_value` |
| 35 | `TextView` | `android:visibility` | `gone` |
| 36 | `TextView` | `android:layout_width` | `wrap_content` |
| 37 | `TextView` | `android:layout_height` | `wrap_content` |
| 38 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_m` |
| 39 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `@id/iv_settings_item_icon` |
| 40 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 41 | `TextView` | `app:layout_constraintTop_toTopOf` | `@id/iv_settings_item_icon` |
| 42 | `TextView` | `style` | `@style/TextP1` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |
| `@color/icon_weak` | `#FFA3A5C3` / `#80FFFFFF` (night) |
| `@color/line_primary` | `#FFEDEEF6` / `#FF3F4273` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/developer_menu_item_height` | `56.000000dip` / `70.000000dip` (sw600dp) |
| `@dimen/icon_size_large` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/iv_settings_item_icon
@id/tv_settings_item_title
@id/tv_settings_item_value
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.settings.SettingsActivity
com.getmimo.ui.settings.SettingsFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00000010" android:background="@color/background_secondary" android:layout_width="match_parent" android:layout_height="@dimen/developer_menu_item_height" android:foreground="?attr/selectableItemBackground">
  <View android:background="@color/line_primary" android:layout_width="match_parent" android:layout_height="1.000000dip" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  <ImageView android:id="@id/iv_settings_item_icon" android:layout_width="@dimen/icon_size_large" android:layout_height="@dimen/icon_size_large" android:layout_marginStart="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:tint="@color/icon_weak"/>
  <TextView android:textColor="@color/text_primary" android:ellipsize="end" android:id="@id/tv_settings_item_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:lines="1" android:layout_marginStart="@dimen/spacing_m" android:layout_marginEnd="@dimen/spacing_xs" app:layout_constraintBottom_toBottomOf="@id/iv_settings_item_icon" app:layout_constraintEnd_toStartOf="@id/tv_settings_item_value" app:layout_constraintStart_toEndOf="@id/iv_settings_item_icon" app:layout_constraintTop_toTopOf="@id/iv_settings_item_icon" style="@style/TextP1"/>
  <TextView android:textColor="@color/text_weak" android:id="@id/tv_settings_item_value" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginEnd="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="@id/iv_settings_item_icon" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="@id/iv_settings_item_icon" style="@style/TextP1"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
