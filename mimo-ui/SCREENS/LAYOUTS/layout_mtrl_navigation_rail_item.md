# پروندهٔ لایه — `res/layout/mtrl_navigation_rail_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mtrl_navigation_rail_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mtrl_navigation_rail_item.xml`](../../SOURCE/res/layout/mtrl_navigation_rail_item.xml) |
| SHA-256 دیکد | `cf7509ad0298d52446761b4e6db37f892cc1666937927198a40ae1ed9a96b76e` |
| ریشه | `merge` |
| تعداد گره | 9 |
| تعداد شناسه | 8 |
| تگ‌های استفاده‌شده | 7 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 16 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   └─ LinearLayout  #@id/navigation_bar_item_content_container
      ├─ FrameLayout  #@id/navigation_bar_item_icon_container
      │  ├─ View  #@id/navigation_bar_item_active_indicator_view
      │  └─ LinearLayout  #@id/navigation_bar_item_inner_content_container
      │     └─ ImageView  #@id/navigation_bar_item_icon_view
      └─ com.google.android.material.internal.BaselineLayout  #@id/navigation_bar_item_labels_group
         ├─ TextView  #@id/navigation_bar_item_small_label_view
         └─ TextView  #@id/navigation_bar_item_large_label_view
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:layout_gravity` | `0x00000031` |
| 2 | `LinearLayout` | `android:orientation` | `vertical` |
| 3 | `LinearLayout` | `android:id` | `@id/navigation_bar_item_content_container` |
| 4 | `LinearLayout` | `android:duplicateParentState` | `true` |
| 5 | `LinearLayout` | `android:clipChildren` | `false` |
| 6 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 7 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 8 | `LinearLayout` | `android:layout_marginTop` | `@dimen/mtrl_navigation_rail_margin` |
| 9 | `FrameLayout` | `android:layout_gravity` | `0x00000011` |
| 10 | `FrameLayout` | `android:id` | `@id/navigation_bar_item_icon_container` |
| 11 | `FrameLayout` | `android:duplicateParentState` | `true` |
| 12 | `FrameLayout` | `android:clipChildren` | `false` |
| 13 | `FrameLayout` | `android:layout_width` | `wrap_content` |
| 14 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 15 | `View` | `android:layout_gravity` | `0x00000011` |
| 16 | `View` | `android:id` | `@id/navigation_bar_item_active_indicator_view` |
| 17 | `View` | `android:layout_width` | `0.000000dip` |
| 18 | `View` | `android:layout_height` | `0.000000dip` |
| 19 | `LinearLayout` | `android:gravity` | `0x00000011` |
| 20 | `LinearLayout` | `android:layout_gravity` | `0x00000011` |
| 21 | `LinearLayout` | `android:orientation` | `horizontal` |
| 22 | `LinearLayout` | `android:id` | `@id/navigation_bar_item_inner_content_container` |
| 23 | `LinearLayout` | `android:duplicateParentState` | `true` |
| 24 | `LinearLayout` | `android:clipChildren` | `false` |
| 25 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 26 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 27 | `ImageView` | `android:layout_gravity` | `0x00000011` |
| 28 | `ImageView` | `android:id` | `@id/navigation_bar_item_icon_view` |
| 29 | `ImageView` | `android:duplicateParentState` | `true` |
| 30 | `ImageView` | `android:layout_width` | `@dimen/mtrl_navigation_rail_icon_size` |
| 31 | `ImageView` | `android:layout_height` | `@dimen/mtrl_navigation_rail_icon_size` |
| 32 | `ImageView` | `android:contentDescription` | `@null` |
| 33 | `com.google.android.material.internal.BaselineLayout` | `android:layout_gravity` | `0x00000011` |
| 34 | `com.google.android.material.internal.BaselineLayout` | `android:id` | `@id/navigation_bar_item_labels_group` |
| 35 | `com.google.android.material.internal.BaselineLayout` | `android:paddingBottom` | `@dimen/mtrl_navigation_rail_text_bottom_margin` |
| 36 | `com.google.android.material.internal.BaselineLayout` | `android:duplicateParentState` | `true` |
| 37 | `com.google.android.material.internal.BaselineLayout` | `android:clipChildren` | `false` |
| 38 | `com.google.android.material.internal.BaselineLayout` | `android:clipToPadding` | `false` |
| 39 | `com.google.android.material.internal.BaselineLayout` | `android:layout_width` | `wrap_content` |
| 40 | `com.google.android.material.internal.BaselineLayout` | `android:layout_height` | `wrap_content` |
| 41 | `com.google.android.material.internal.BaselineLayout` | `android:layout_marginTop` | `@dimen/m3_navigation_rail_icon_label_padding` |
| 42 | `TextView` | `android:textSize` | `@dimen/mtrl_navigation_rail_text_size` |
| 43 | `TextView` | `android:ellipsize` | `end` |
| 44 | `TextView` | `android:gravity` | `0x00000010` |
| 45 | `TextView` | `android:id` | `@id/navigation_bar_item_small_label_view` |
| 46 | `TextView` | `android:duplicateParentState` | `true` |
| 47 | `TextView` | `android:layout_width` | `wrap_content` |
| 48 | `TextView` | `android:layout_height` | `wrap_content` |
| 49 | `TextView` | `android:paddingStart` | `@dimen/m3_navigation_rail_label_padding_horizontal` |
| 50 | `TextView` | `android:paddingEnd` | `@dimen/m3_navigation_rail_label_padding_horizontal` |
| 51 | `TextView` | `android:textSize` | `@dimen/mtrl_navigation_rail_active_text_size` |
| 52 | `TextView` | `android:ellipsize` | `end` |
| 53 | `TextView` | `android:gravity` | `0x00000010` |
| 54 | `TextView` | `android:id` | `@id/navigation_bar_item_large_label_view` |
| 55 | `TextView` | `android:visibility` | `invisible` |
| 56 | `TextView` | `android:duplicateParentState` | `true` |
| 57 | `TextView` | `android:layout_width` | `wrap_content` |
| 58 | `TextView` | `android:layout_height` | `wrap_content` |
| 59 | `TextView` | `android:paddingStart` | `@dimen/m3_navigation_rail_label_padding_horizontal` |
| 60 | `TextView` | `android:paddingEnd` | `@dimen/m3_navigation_rail_label_padding_horizontal` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/m3_navigation_rail_icon_label_padding` | `4.000000dip` |
| `@dimen/m3_navigation_rail_label_padding_horizontal` | `2.000000dip` |
| `@dimen/mtrl_navigation_rail_active_text_size` | `14.000000dip` |
| `@dimen/mtrl_navigation_rail_icon_size` | `24.000000dip` |
| `@dimen/mtrl_navigation_rail_margin` | `8.000000dip` |
| `@dimen/mtrl_navigation_rail_text_bottom_margin` | `16.000000dip` |
| `@dimen/mtrl_navigation_rail_text_size` | `12.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/navigation_bar_item_active_indicator_view
@id/navigation_bar_item_content_container
@id/navigation_bar_item_icon_container
@id/navigation_bar_item_icon_view
@id/navigation_bar_item_inner_content_container
@id/navigation_bar_item_labels_group
@id/navigation_bar_item_large_label_view
@id/navigation_bar_item_small_label_view
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
<merge xmlns:android="http://schemas.android.com/apk/res/android">
  <LinearLayout android:layout_gravity="0x00000031" android:orientation="vertical" android:id="@id/navigation_bar_item_content_container" android:duplicateParentState="true" android:clipChildren="false" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/mtrl_navigation_rail_margin">
    <FrameLayout android:layout_gravity="0x00000011" android:id="@id/navigation_bar_item_icon_container" android:duplicateParentState="true" android:clipChildren="false" android:layout_width="wrap_content" android:layout_height="wrap_content">
      <View android:layout_gravity="0x00000011" android:id="@id/navigation_bar_item_active_indicator_view" android:layout_width="0.000000dip" android:layout_height="0.000000dip"/>
      <LinearLayout android:gravity="0x00000011" android:layout_gravity="0x00000011" android:orientation="horizontal" android:id="@id/navigation_bar_item_inner_content_container" android:duplicateParentState="true" android:clipChildren="false" android:layout_width="wrap_content" android:layout_height="wrap_content">
        <ImageView android:layout_gravity="0x00000011" android:id="@id/navigation_bar_item_icon_view" android:duplicateParentState="true" android:layout_width="@dimen/mtrl_navigation_rail_icon_size" android:layout_height="@dimen/mtrl_navigation_rail_icon_size" android:contentDescription="@null"/>
      </LinearLayout>
    </FrameLayout>
    <com.google.android.material.internal.BaselineLayout android:layout_gravity="0x00000011" android:id="@id/navigation_bar_item_labels_group" android:paddingBottom="@dimen/mtrl_navigation_rail_text_bottom_margin" android:duplicateParentState="true" android:clipChildren="false" android:clipToPadding="false" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/m3_navigation_rail_icon_label_padding">
      <TextView android:textSize="@dimen/mtrl_navigation_rail_text_size" android:ellipsize="end" android:gravity="0x00000010" android:id="@id/navigation_bar_item_small_label_view" android:duplicateParentState="true" android:layout_width="wrap_content" android:layout_height="wrap_content" android:paddingStart="@dimen/m3_navigation_rail_label_padding_horizontal" android:paddingEnd="@dimen/m3_navigation_rail_label_padding_horizontal"/>
      <TextView android:textSize="@dimen/mtrl_navigation_rail_active_text_size" android:ellipsize="end" android:gravity="0x00000010" android:id="@id/navigation_bar_item_large_label_view" android:visibility="invisible" android:duplicateParentState="true" android:layout_width="wrap_content" android:layout_height="wrap_content" android:paddingStart="@dimen/m3_navigation_rail_label_padding_horizontal" android:paddingEnd="@dimen/m3_navigation_rail_label_padding_horizontal"/>
    </com.google.android.material.internal.BaselineLayout>
  </LinearLayout>
</merge>
```
