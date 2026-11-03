# پروندهٔ لایه — `res/layout/notification_template_custom_big.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/notification_template_custom_big.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/notification_template_custom_big.xml`](../../SOURCE/res/layout/notification_template_custom_big.xml) |
| SHA-256 دیکد | `af001661a7e1709e32565bb978564457150c96defbbb3428cec5d0e69eb2710c` |
| ریشه | `FrameLayout` |
| تعداد گره | 11 |
| تعداد شناسه | 9 |
| تگ‌های استفاده‌شده | 6 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 7 |
| ارجاع به منابع | 16 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout  #@id/notification_background
   ├─ include
   └─ LinearLayout
      ├─ LinearLayout  #@id/notification_main_column_container
      │  ├─ FrameLayout  #@id/notification_main_column
      │  └─ FrameLayout  #@id/right_side
      │     ├─ ViewStub  #@id/time
      │     ├─ ViewStub  #@id/chronometer
      │     └─ TextView  #@id/info
      ├─ ImageView  #@id/action_divider
      └─ LinearLayout  #@id/actions
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:id` | `@id/notification_background` |
| 2 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 3 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 4 | `include` | `android:layout_width` | `@dimen/notification_large_icon_width` |
| 5 | `include` | `android:layout_height` | `@dimen/notification_large_icon_height` |
| 6 | `include` | `layout` | `@layout/notification_template_icon_group` |
| 7 | `LinearLayout` | `android:layout_gravity` | `0x00000030` |
| 8 | `LinearLayout` | `android:orientation` | `vertical` |
| 9 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 10 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 11 | `LinearLayout` | `android:layout_marginStart` | `@dimen/notification_large_icon_width` |
| 12 | `LinearLayout` | `android:orientation` | `horizontal` |
| 13 | `LinearLayout` | `android:id` | `@id/notification_main_column_container` |
| 14 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 15 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 16 | `LinearLayout` | `android:minHeight` | `@dimen/notification_large_icon_height` |
| 17 | `FrameLayout` | `android:id` | `@id/notification_main_column` |
| 18 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 19 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 20 | `FrameLayout` | `android:layout_marginBottom` | `8.000000dip` |
| 21 | `FrameLayout` | `android:layout_weight` | `1.000000` |
| 22 | `FrameLayout` | `android:layout_marginEnd` | `8.000000dip` |
| 23 | `FrameLayout` | `android:id` | `@id/right_side` |
| 24 | `FrameLayout` | `android:paddingTop` | `@dimen/notification_right_side_padding_top` |
| 25 | `FrameLayout` | `android:layout_width` | `wrap_content` |
| 26 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 27 | `FrameLayout` | `android:layout_marginEnd` | `8.000000dip` |
| 28 | `ViewStub` | `android:layout_gravity` | `0x00800035` |
| 29 | `ViewStub` | `android:id` | `@id/time` |
| 30 | `ViewStub` | `android:visibility` | `gone` |
| 31 | `ViewStub` | `android:layout` | `@layout/notification_template_part_time` |
| 32 | `ViewStub` | `android:layout_width` | `wrap_content` |
| 33 | `ViewStub` | `android:layout_height` | `wrap_content` |
| 34 | `ViewStub` | `android:layout_gravity` | `0x00800035` |
| 35 | `ViewStub` | `android:id` | `@id/chronometer` |
| 36 | `ViewStub` | `android:visibility` | `gone` |
| 37 | `ViewStub` | `android:layout` | `@layout/notification_template_part_chronometer` |
| 38 | `ViewStub` | `android:layout_width` | `wrap_content` |
| 39 | `ViewStub` | `android:layout_height` | `wrap_content` |
| 40 | `TextView` | `android:textAppearance` | `@style/TextAppearance.Compat.Notification.Info` |
| 41 | `TextView` | `android:layout_gravity` | `0x00800055` |
| 42 | `TextView` | `android:id` | `@id/info` |
| 43 | `TextView` | `android:layout_width` | `wrap_content` |
| 44 | `TextView` | `android:layout_height` | `wrap_content` |
| 45 | `TextView` | `android:layout_marginTop` | `20.000000dip` |
| 46 | `TextView` | `android:singleLine` | `true` |
| 47 | `ImageView` | `android:id` | `@id/action_divider` |
| 48 | `ImageView` | `android:background` | `#29000000` |
| 49 | `ImageView` | `android:visibility` | `gone` |
| 50 | `ImageView` | `android:layout_width` | `match_parent` |
| 51 | `ImageView` | `android:layout_height` | `1.000000dip` |
| 52 | `LinearLayout` | `android:orientation` | `horizontal` |
| 53 | `LinearLayout` | `android:id` | `@id/actions` |
| 54 | `LinearLayout` | `android:visibility` | `gone` |
| 55 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 56 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 57 | `LinearLayout` | `android:layout_marginStart` | `16777208.000000dip` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/notification_large_icon_height` | `64.000000dip` |
| `@dimen/notification_large_icon_width` | `64.000000dip` |
| `@dimen/notification_right_side_padding_top` | `4.000000dip` |
| `@style/TextAppearance.Compat.Notification.Info` | `[]` |

## ۴. شناسه‌های `@id`

```text
@id/action_divider
@id/actions
@id/chronometer
@id/info
@id/notification_background
@id/notification_main_column
@id/notification_main_column_container
@id/right_side
@id/time
```

## ۵. ارجاع به لایه‌های دیگر

```text
0x00800035
@dimen/notification_large_icon_height
@dimen/notification_large_icon_width
@layout/notification_template_icon_group
@layout/notification_template_part_chronometer
@layout/notification_template_part_time
wrap_content
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/notification_background" android:layout_width="match_parent" android:layout_height="wrap_content">
  <include android:layout_width="@dimen/notification_large_icon_width" android:layout_height="@dimen/notification_large_icon_height" layout="@layout/notification_template_icon_group"/>
  <LinearLayout android:layout_gravity="0x00000030" android:orientation="vertical" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginStart="@dimen/notification_large_icon_width">
    <LinearLayout android:orientation="horizontal" android:id="@id/notification_main_column_container" android:layout_width="match_parent" android:layout_height="wrap_content" android:minHeight="@dimen/notification_large_icon_height">
      <FrameLayout android:id="@id/notification_main_column" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginBottom="8.000000dip" android:layout_weight="1.000000" android:layout_marginEnd="8.000000dip"/>
      <FrameLayout android:id="@id/right_side" android:paddingTop="@dimen/notification_right_side_padding_top" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginEnd="8.000000dip">
        <ViewStub android:layout_gravity="0x00800035" android:id="@id/time" android:visibility="gone" android:layout="@layout/notification_template_part_time" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
        <ViewStub android:layout_gravity="0x00800035" android:id="@id/chronometer" android:visibility="gone" android:layout="@layout/notification_template_part_chronometer" android:layout_width="wrap_content" android:layout_height="wrap_content"/>
        <TextView android:textAppearance="@style/TextAppearance.Compat.Notification.Info" android:layout_gravity="0x00800055" android:id="@id/info" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="20.000000dip" android:singleLine="true"/>
      </FrameLayout>
    </LinearLayout>
    <ImageView android:id="@id/action_divider" android:background="#29000000" android:visibility="gone" android:layout_width="match_parent" android:layout_height="1.000000dip"/>
    <LinearLayout android:orientation="horizontal" android:id="@id/actions" android:visibility="gone" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginStart="16777208.000000dip"/>
  </LinearLayout>
</FrameLayout>
```
