# پروندهٔ لایه — `res/layout/developer_menu_remote_config_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/developer_menu_remote_config_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/developer_menu_remote_config_item.xml`](../../SOURCE/res/layout/developer_menu_remote_config_item.xml) |
| SHA-256 دیکد | `ebce344343fe8d1e82eb7eedb84b56a1eee2f6cb1653e971b3ad1b111e559b3b` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 12 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ ImageView  #@id/iv_remove
   ├─ TextView  #@id/tv_item_id
   └─ TextView  #@id/tv_item_value
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 3 | `ImageView` | `android:id` | `@id/iv_remove` |
| 4 | `ImageView` | `android:layout_width` | `16.000000dip` |
| 5 | `ImageView` | `android:layout_height` | `16.000000dip` |
| 6 | `ImageView` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 7 | `ImageView` | `android:src` | `@drawable/ic_close` |
| 8 | `ImageView` | `android:layout_marginEnd` | `@dimen/spacing_xs` |
| 9 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 10 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 11 | `ImageView` | `app:tint` | `@color/icon_weak` |
| 12 | `TextView` | `android:textAppearance` | `@style/TextP3` |
| 13 | `TextView` | `android:id` | `@id/tv_item_id` |
| 14 | `TextView` | `android:layout_width` | `wrap_content` |
| 15 | `TextView` | `android:layout_height` | `wrap_content` |
| 16 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 17 | `TextView` | `android:text` | `@string/developer_menu_override_remote_config_id` |
| 18 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_s` |
| 19 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_s` |
| 20 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 21 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 22 | `TextView` | `android:textAppearance` | `@style/TextP3` |
| 23 | `TextView` | `android:id` | `@id/tv_item_value` |
| 24 | `TextView` | `android:layout_width` | `wrap_content` |
| 25 | `TextView` | `android:layout_height` | `wrap_content` |
| 26 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 27 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_l` |
| 28 | `TextView` | `android:text` | `@string/developer_menu_override_remote_config_value` |
| 29 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_s` |
| 30 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_s` |
| 31 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 32 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 33 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_item_id` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/icon_weak` | `#FFA3A5C3` / `#80FFFFFF` (night) |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@string/developer_menu_override_remote_config_id` | `Id: %s` |
| `@string/developer_menu_override_remote_config_value` | `Value: %s` |
| `@style/TextP3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.199982sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/iv_remove
@id/tv_item_id
@id/tv_item_value
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.developermenu.DeveloperMenuActivity
com.getmimo.ui.developermenu.DeveloperMenuFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:layout_width="match_parent" android:layout_height="wrap_content">
  <ImageView android:id="@id/iv_remove" android:layout_width="16.000000dip" android:layout_height="16.000000dip" android:layout_marginTop="@dimen/spacing_xs" android:src="@drawable/ic_close" android:layout_marginEnd="@dimen/spacing_xs" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0" app:tint="@color/icon_weak"/>
  <TextView android:textAppearance="@style/TextP3" android:id="@id/tv_item_id" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l" android:text="@string/developer_menu_override_remote_config_id" android:layout_marginStart="@dimen/spacing_s" android:layout_marginEnd="@dimen/spacing_s" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  <TextView android:textAppearance="@style/TextP3" android:id="@id/tv_item_value" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" android:layout_marginBottom="@dimen/spacing_l" android:text="@string/developer_menu_override_remote_config_value" android:layout_marginStart="@dimen/spacing_s" android:layout_marginEnd="@dimen/spacing_s" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_item_id"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
