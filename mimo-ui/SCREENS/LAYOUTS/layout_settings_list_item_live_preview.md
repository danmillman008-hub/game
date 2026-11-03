# پروندهٔ لایه — `res/layout/settings_list_item_live_preview.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/settings_list_item_live_preview.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/settings_list_item_live_preview.xml`](../../SOURCE/res/layout/settings_list_item_live_preview.xml) |
| SHA-256 دیکد | `27f01602d407137db2c1c85f303d52bdc1d3769037c12b45137139d9dc7947a7` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 8 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ ImageView  #@id/iv_settings_item_icon
   ├─ TextView  #@id/tv_settings_item_title
   └─ ProgressBar  #@id/pb_settings_list_item
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:gravity` | `0x00000010` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_secondary` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingLeft` | `16.000000dip` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingRight` | `16.000000dip` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 6 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `56.000000dip` |
| 7 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:foreground` | `?attr/selectableItemBackground` |
| 8 | `ImageView` | `android:id` | `@id/iv_settings_item_icon` |
| 9 | `ImageView` | `android:layout_width` | `24.000000dip` |
| 10 | `ImageView` | `android:layout_height` | `24.000000dip` |
| 11 | `ImageView` | `android:layout_marginEnd` | `16.000000dip` |
| 12 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 13 | `ImageView` | `app:layout_constraintHorizontal_chainStyle` | `0` |
| 14 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 15 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 16 | `ImageView` | `app:tint` | `@color/icon_weak` |
| 17 | `TextView` | `android:textColor` | `@color/text_primary` |
| 18 | `TextView` | `android:id` | `@id/tv_settings_item_title` |
| 19 | `TextView` | `android:layout_width` | `0.000000dip` |
| 20 | `TextView` | `android:layout_height` | `wrap_content` |
| 21 | `TextView` | `android:layout_marginStart` | `16.000000dip` |
| 22 | `TextView` | `android:layout_marginEnd` | `32.000000dip` |
| 23 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 24 | `TextView` | `app:layout_constraintEnd_toStartOf` | `@id/pb_settings_list_item` |
| 25 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_settings_item_icon` |
| 26 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 27 | `TextView` | `style` | `@style/TextP1` |
| 28 | `ProgressBar` | `android:id` | `@id/pb_settings_list_item` |
| 29 | `ProgressBar` | `android:paddingTop` | `16.000000dip` |
| 30 | `ProgressBar` | `android:paddingBottom` | `16.000000dip` |
| 31 | `ProgressBar` | `android:visibility` | `gone` |
| 32 | `ProgressBar` | `android:layout_width` | `wrap_content` |
| 33 | `ProgressBar` | `android:layout_height` | `wrap_content` |
| 34 | `ProgressBar` | `android:indeterminate` | `false` |
| 35 | `ProgressBar` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 36 | `ProgressBar` | `app:layout_constraintEnd_toEndOf` | `0` |
| 37 | `ProgressBar` | `app:layout_constraintTop_toTopOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |
| `@color/icon_weak` | `#FFA3A5C3` / `#80FFFFFF` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@style/TextP1` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/iv_settings_item_icon
@id/pb_settings_list_item
@id/tv_settings_item_title
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
androidx.compose.ui.tooling.PreviewActivity
com.getmimo.ui.settings.SettingsActivity
com.getmimo.ui.settings.SettingsFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00000010" android:background="@color/background_secondary" android:paddingLeft="16.000000dip" android:paddingRight="16.000000dip" android:layout_width="match_parent" android:layout_height="56.000000dip" android:foreground="?attr/selectableItemBackground">
  <ImageView android:id="@id/iv_settings_item_icon" android:layout_width="24.000000dip" android:layout_height="24.000000dip" android:layout_marginEnd="16.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintHorizontal_chainStyle="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:tint="@color/icon_weak"/>
  <TextView android:textColor="@color/text_primary" android:id="@id/tv_settings_item_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginStart="16.000000dip" android:layout_marginEnd="32.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toStartOf="@id/pb_settings_list_item" app:layout_constraintStart_toEndOf="@id/iv_settings_item_icon" app:layout_constraintTop_toTopOf="0" style="@style/TextP1"/>
  <ProgressBar android:id="@id/pb_settings_list_item" android:paddingTop="16.000000dip" android:paddingBottom="16.000000dip" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:indeterminate="false" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
