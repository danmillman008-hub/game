# پروندهٔ لایه — `res/layout/notification_action.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/notification_action.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/notification_action.xml`](../../SOURCE/res/layout/notification_action.xml) |
| SHA-256 دیکد | `afe4a5b62bb67b309d1f16488a9c019f423ce291083f2ce1a34c2170f822baba` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/action_container
   ├─ ImageView  #@id/action_image
   └─ TextView  #@id/action_text
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `horizontal` |
| 2 | `LinearLayout` | `android:id` | `@id/action_container` |
| 3 | `LinearLayout` | `android:layout_width` | `0.000000dip` |
| 4 | `LinearLayout` | `android:layout_height` | `48.000000dip` |
| 5 | `LinearLayout` | `android:layout_weight` | `1.000000` |
| 6 | `LinearLayout` | `android:paddingStart` | `4.000000dip` |
| 7 | `LinearLayout` | `style` | `@style/Widget.Compat.NotificationActionContainer` |
| 8 | `ImageView` | `android:layout_gravity` | `0x00800013` |
| 9 | `ImageView` | `android:id` | `@id/action_image` |
| 10 | `ImageView` | `android:layout_width` | `@dimen/notification_action_icon_size` |
| 11 | `ImageView` | `android:layout_height` | `@dimen/notification_action_icon_size` |
| 12 | `ImageView` | `android:scaleType` | `centerInside` |
| 13 | `TextView` | `android:ellipsize` | `end` |
| 14 | `TextView` | `android:layout_gravity` | `0x00800013` |
| 15 | `TextView` | `android:id` | `@id/action_text` |
| 16 | `TextView` | `android:clickable` | `false` |
| 17 | `TextView` | `android:layout_width` | `wrap_content` |
| 18 | `TextView` | `android:layout_height` | `wrap_content` |
| 19 | `TextView` | `android:singleLine` | `true` |
| 20 | `TextView` | `android:paddingStart` | `4.000000dip` |
| 21 | `TextView` | `style` | `@style/Widget.Compat.NotificationActionText` |

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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="horizontal" android:id="@id/action_container" android:layout_width="0.000000dip" android:layout_height="48.000000dip" android:layout_weight="1.000000" android:paddingStart="4.000000dip" style="@style/Widget.Compat.NotificationActionContainer">
  <ImageView android:layout_gravity="0x00800013" android:id="@id/action_image" android:layout_width="@dimen/notification_action_icon_size" android:layout_height="@dimen/notification_action_icon_size" android:scaleType="centerInside"/>
  <TextView android:ellipsize="end" android:layout_gravity="0x00800013" android:id="@id/action_text" android:clickable="false" android:layout_width="wrap_content" android:layout_height="wrap_content" android:singleLine="true" android:paddingStart="4.000000dip" style="@style/Widget.Compat.NotificationActionText"/>
</LinearLayout>
```
