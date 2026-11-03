# پروندهٔ لایه — `res/layout/com_facebook_tooltip_bubble.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/com_facebook_tooltip_bubble.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/com_facebook_tooltip_bubble.xml`](../../SOURCE/res/layout/com_facebook_tooltip_bubble.xml) |
| SHA-256 دیکد | `4485d9300014895aeb026a8ef710c7f76ca9e550856e438908881e4a2c36fb1f` |
| ریشه | `RelativeLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 10 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ RelativeLayout
   ├─ RelativeLayout  #@id/com_facebook_body_frame
   │  ├─ ImageView  #@id/com_facebook_button_xout
   │  └─ TextView  #@id/com_facebook_tooltip_bubble_view_text_body
   ├─ ImageView  #@id/com_facebook_tooltip_bubble_view_top_pointer
   └─ ImageView  #@id/com_facebook_tooltip_bubble_view_bottom_pointer
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `RelativeLayout` | `android:paddingLeft` | `20.000000dip` |
| 2 | `RelativeLayout` | `android:paddingRight` | `20.000000dip` |
| 3 | `RelativeLayout` | `android:layout_width` | `wrap_content` |
| 4 | `RelativeLayout` | `android:layout_height` | `wrap_content` |
| 5 | `RelativeLayout` | `android:id` | `@id/com_facebook_body_frame` |
| 6 | `RelativeLayout` | `android:background` | `@drawable/com_facebook_tooltip_blue_background` |
| 7 | `RelativeLayout` | `android:layout_width` | `wrap_content` |
| 8 | `RelativeLayout` | `android:layout_height` | `wrap_content` |
| 9 | `RelativeLayout` | `android:layout_below` | `@id/com_facebook_tooltip_bubble_view_top_pointer` |
| 10 | `RelativeLayout` | `android:layout_centerHorizontal` | `true` |
| 11 | `ImageView` | `android:id` | `@id/com_facebook_button_xout` |
| 12 | `ImageView` | `android:padding` | `10.000000dip` |
| 13 | `ImageView` | `android:layout_width` | `wrap_content` |
| 14 | `ImageView` | `android:layout_height` | `wrap_content` |
| 15 | `ImageView` | `android:src` | `@drawable/com_facebook_tooltip_blue_xout` |
| 16 | `ImageView` | `android:layout_alignParentTop` | `true` |
| 17 | `ImageView` | `android:layout_alignParentRight` | `true` |
| 18 | `TextView` | `android:id` | `@id/com_facebook_tooltip_bubble_view_text_body` |
| 19 | `TextView` | `android:padding` | `10.000000dip` |
| 20 | `TextView` | `android:layout_width` | `wrap_content` |
| 21 | `TextView` | `android:layout_height` | `wrap_content` |
| 22 | `TextView` | `android:layout_toLeftOf` | `@id/com_facebook_button_xout` |
| 23 | `TextView` | `android:layout_alignParentLeft` | `true` |
| 24 | `TextView` | `android:layout_alignParentTop` | `true` |
| 25 | `TextView` | `style` | `@style/tooltip_bubble_text` |
| 26 | `ImageView` | `android:id` | `@id/com_facebook_tooltip_bubble_view_top_pointer` |
| 27 | `ImageView` | `android:layout_width` | `wrap_content` |
| 28 | `ImageView` | `android:layout_height` | `wrap_content` |
| 29 | `ImageView` | `android:layout_marginBottom` | `16777206.000000dip` |
| 30 | `ImageView` | `android:src` | `@drawable/com_facebook_tooltip_blue_topnub` |
| 31 | `ImageView` | `android:layout_alignParentTop` | `true` |
| 32 | `ImageView` | `android:layout_centerHorizontal` | `true` |
| 33 | `ImageView` | `android:layout_gravity` | `0x00000051` |
| 34 | `ImageView` | `android:id` | `@id/com_facebook_tooltip_bubble_view_bottom_pointer` |
| 35 | `ImageView` | `android:layout_width` | `wrap_content` |
| 36 | `ImageView` | `android:layout_height` | `wrap_content` |
| 37 | `ImageView` | `android:layout_marginTop` | `16777203.000000dip` |
| 38 | `ImageView` | `android:src` | `@drawable/com_facebook_tooltip_blue_bottomnub` |
| 39 | `ImageView` | `android:layout_below` | `@id/com_facebook_body_frame` |
| 40 | `ImageView` | `android:layout_centerHorizontal` | `true` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/tooltip_bubble_text` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '12.000000sp', 'value_type': 'dimension'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@android:0106000B', 'value_type': 'reference'}, {'attr': 'android:gravity', 'attr_id': '0x010100AF', 'value': '0x00000003', 'value_type': 'int_hex'}, {'attr': 'android:shadowColor', 'attr_id': '0x01010161', 'value': '#40000000', 'value_type': 'int_color_argb8'}, {'attr': 'android:shadowDy', 'attr_id': '0x01010163', 'value': '-1.000000', 'value_type': 'float'}, {'attr': 'android:shadowRadius', 'attr_id': '0x01010164', 'value': '0.250000', 'value_type': 'float'}]` |

## ۴. شناسه‌های `@id`

```text
@id/com_facebook_body_frame
@id/com_facebook_button_xout
@id/com_facebook_tooltip_bubble_view_bottom_pointer
@id/com_facebook_tooltip_bubble_view_text_body
@id/com_facebook_tooltip_bubble_view_top_pointer
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.facebook.FacebookActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android" android:paddingLeft="20.000000dip" android:paddingRight="20.000000dip" android:layout_width="wrap_content" android:layout_height="wrap_content">
  <RelativeLayout android:id="@id/com_facebook_body_frame" android:background="@drawable/com_facebook_tooltip_blue_background" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_below="@id/com_facebook_tooltip_bubble_view_top_pointer" android:layout_centerHorizontal="true">
    <ImageView android:id="@id/com_facebook_button_xout" android:padding="10.000000dip" android:layout_width="wrap_content" android:layout_height="wrap_content" android:src="@drawable/com_facebook_tooltip_blue_xout" android:layout_alignParentTop="true" android:layout_alignParentRight="true"/>
    <TextView android:id="@id/com_facebook_tooltip_bubble_view_text_body" android:padding="10.000000dip" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_toLeftOf="@id/com_facebook_button_xout" android:layout_alignParentLeft="true" android:layout_alignParentTop="true" style="@style/tooltip_bubble_text"/>
  </RelativeLayout>
  <ImageView android:id="@id/com_facebook_tooltip_bubble_view_top_pointer" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="16777206.000000dip" android:src="@drawable/com_facebook_tooltip_blue_topnub" android:layout_alignParentTop="true" android:layout_centerHorizontal="true"/>
  <ImageView android:layout_gravity="0x00000051" android:id="@id/com_facebook_tooltip_bubble_view_bottom_pointer" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="16777203.000000dip" android:src="@drawable/com_facebook_tooltip_blue_bottomnub" android:layout_below="@id/com_facebook_body_frame" android:layout_centerHorizontal="true"/>
</RelativeLayout>
```
