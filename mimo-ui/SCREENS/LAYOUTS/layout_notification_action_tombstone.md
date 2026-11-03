# پروندهٔ لایه — `res/layout/notification_action_tombstone.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/notification_action_tombstone.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/notification_action_tombstone.xml`](../../SOURCE/res/layout/notification_action_tombstone.xml) |
| SHA-256 دیکد | `94bdc3115d68e49d40019a64729aa2625187c13ceea0d2a2ff17dd2af8d2f6e9` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/action_container
   ├─ ImageView  #@id/action_image
   └─ TextView  #@id/action_text
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:enabled` | `false` |
| 2 | `LinearLayout` | `android:orientation` | `horizontal` |
| 3 | `LinearLayout` | `android:id` | `@id/action_container` |
| 4 | `LinearLayout` | `android:background` | `@null` |
| 5 | `LinearLayout` | `android:layout_width` | `0.000000dip` |
| 6 | `LinearLayout` | `android:layout_height` | `48.000000dip` |
| 7 | `LinearLayout` | `android:layout_weight` | `1.000000` |
| 8 | `LinearLayout` | `android:paddingStart` | `4.000000dip` |
| 9 | `LinearLayout` | `style` | `@style/Widget.Compat.NotificationActionContainer` |
| 10 | `ImageView` | `android:enabled` | `false` |
| 11 | `ImageView` | `android:layout_gravity` | `0x00800013` |
| 12 | `ImageView` | `android:id` | `@id/action_image` |
| 13 | `ImageView` | `android:layout_width` | `@dimen/notification_action_icon_size` |
| 14 | `ImageView` | `android:layout_height` | `@dimen/notification_action_icon_size` |
| 15 | `ImageView` | `android:scaleType` | `centerInside` |
| 16 | `ImageView` | `android:alpha` | `0.500000` |
| 17 | `TextView` | `android:enabled` | `false` |
| 18 | `TextView` | `android:ellipsize` | `end` |
| 19 | `TextView` | `android:layout_gravity` | `0x00800013` |
| 20 | `TextView` | `android:id` | `@id/action_text` |
| 21 | `TextView` | `android:clickable` | `false` |
| 22 | `TextView` | `android:layout_width` | `wrap_content` |
| 23 | `TextView` | `android:layout_height` | `wrap_content` |
| 24 | `TextView` | `android:singleLine` | `true` |
| 25 | `TextView` | `android:alpha` | `0.500000` |
| 26 | `TextView` | `android:paddingStart` | `4.000000dip` |
| 27 | `TextView` | `style` | `@style/Widget.Compat.NotificationActionText` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/notification_action_icon_size` | `32.000000dip` |
| `@style/Widget.Compat.NotificationActionContainer` | `[{'attr': 'android:background', 'attr_id': '0x010100D4', 'value': '@drawable/notification_action_background', 'value_type': 'reference'}]` |
| `@style/Widget.Compat.NotificationActionText` | `[{'attr': 'android:textAppearance', 'attr_id': '0x01010034', 'value': '?android:01010207', 'value_type': 'attribute'}, {'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '@dimen/notification_action_text_size', 'value_type': 'reference'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/androidx_core_secondary_text_default_material_light', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/action_container
@id/action_image
@id/action_text
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:enabled="false" android:orientation="horizontal" android:id="@id/action_container" android:background="@null" android:layout_width="0.000000dip" android:layout_height="48.000000dip" android:layout_weight="1.000000" android:paddingStart="4.000000dip" style="@style/Widget.Compat.NotificationActionContainer">
  <ImageView android:enabled="false" android:layout_gravity="0x00800013" android:id="@id/action_image" android:layout_width="@dimen/notification_action_icon_size" android:layout_height="@dimen/notification_action_icon_size" android:scaleType="centerInside" android:alpha="0.500000"/>
  <TextView android:enabled="false" android:ellipsize="end" android:layout_gravity="0x00800013" android:id="@id/action_text" android:clickable="false" android:layout_width="wrap_content" android:layout_height="wrap_content" android:singleLine="true" android:alpha="0.500000" android:paddingStart="4.000000dip" style="@style/Widget.Compat.NotificationActionText"/>
</LinearLayout>
```
