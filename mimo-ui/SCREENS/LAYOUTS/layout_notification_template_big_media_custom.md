# پروندهٔ لایه — `res/layout/notification_template_big_media_custom.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/notification_template_big_media_custom.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/notification_template_big_media_custom.xml`](../../SOURCE/res/layout/notification_template_big_media_custom.xml) |
| SHA-256 دیکد | `4d26da5c6f92165113f4470eaa441707c2931db6eb90fb93f6265f4557063b62` |
| ریشه | `RelativeLayout` |
| تعداد گره | 11 |
| تعداد شناسه | 9 |
| تگ‌های استفاده‌شده | 8 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 7 |
| ارجاع به منابع | 20 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ RelativeLayout  #@id/status_bar_latest_event_content
   ├─ include
   ├─ include
   ├─ LinearLayout  #@id/notification_main_column_container
   │  ├─ FrameLayout  #@id/notification_main_column
   │  └─ FrameLayout  #@id/right_side
   │     ├─ DateTimeView  #@id/time
   │     ├─ Chronometer  #@id/chronometer
   │     └─ TextView  #@id/info
   ├─ LinearLayout  #@id/media_actions
   └─ ImageView  #@id/action_divider
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `RelativeLayout` | `android:id` | `@id/status_bar_latest_event_content` |
| 2 | `RelativeLayout` | `android:layout_width` | `match_parent` |
| 3 | `RelativeLayout` | `android:layout_height` | `128.000000dip` |
| 4 | `include` | `android:layout_width` | `@dimen/notification_large_icon_width` |
| 5 | `include` | `android:layout_height` | `@dimen/notification_large_icon_height` |
| 6 | `include` | `layout` | `@layout/notification_template_icon_group` |
| 7 | `include` | `android:layout_width` | `48.000000dip` |
| 8 | `include` | `android:layout_height` | `48.000000dip` |
| 9 | `include` | `android:layout_marginLeft` | `2.000000dip` |
| 10 | `include` | `android:layout_marginRight` | `2.000000dip` |
| 11 | `include` | `android:layout_alignParentRight` | `true` |
| 12 | `include` | `android:layout_alignParentEnd` | `true` |
| 13 | `include` | `layout` | `@layout/notification_media_cancel_action` |
| 14 | `LinearLayout` | `android:orientation` | `horizontal` |
| 15 | `LinearLayout` | `android:id` | `@id/notification_main_column_container` |
| 16 | `LinearLayout` | `android:paddingTop` | `@dimen/notification_main_column_padding_top` |
| 17 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 18 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 19 | `LinearLayout` | `android:layout_marginLeft` | `@dimen/notification_large_icon_height` |
| 20 | `LinearLayout` | `android:minHeight` | `@dimen/notification_large_icon_height` |
| 21 | `LinearLayout` | `android:layout_toLeftOf` | `@id/cancel_action` |
| 22 | `LinearLayout` | `android:layout_marginStart` | `@dimen/notification_large_icon_height` |
| 23 | `LinearLayout` | `android:layout_toStartOf` | `@id/cancel_action` |
| 24 | `FrameLayout` | `android:id` | `@id/notification_main_column` |
| 25 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 26 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 27 | `FrameLayout` | `android:layout_marginLeft` | `@dimen/notification_content_margin_start` |
| 28 | `FrameLayout` | `android:layout_marginRight` | `8.000000dip` |
| 29 | `FrameLayout` | `android:layout_marginBottom` | `8.000000dip` |
| 30 | `FrameLayout` | `android:layout_weight` | `1.000000` |
| 31 | `FrameLayout` | `android:layout_marginStart` | `@dimen/notification_content_margin_start` |
| 32 | `FrameLayout` | `android:layout_marginEnd` | `8.000000dip` |
| 33 | `FrameLayout` | `android:id` | `@id/right_side` |
| 34 | `FrameLayout` | `android:paddingTop` | `@dimen/notification_right_side_padding_top` |
| 35 | `FrameLayout` | `android:layout_width` | `wrap_content` |
| 36 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 37 | `FrameLayout` | `android:layout_marginRight` | `8.000000dip` |
| 38 | `FrameLayout` | `android:layout_marginEnd` | `8.000000dip` |
| 39 | `DateTimeView` | `android:textAppearance` | `@style/TextAppearance.Compat.Notification.Time.Media` |
| 40 | `DateTimeView` | `android:layout_gravity` | `0x00800035` |
| 41 | `DateTimeView` | `android:id` | `@id/time` |
| 42 | `DateTimeView` | `android:visibility` | `gone` |
| 43 | `DateTimeView` | `android:layout_width` | `wrap_content` |
| 44 | `DateTimeView` | `android:layout_height` | `wrap_content` |
| 45 | `DateTimeView` | `android:singleLine` | `true` |
| 46 | `Chronometer` | `android:textAppearance` | `@style/TextAppearance.Compat.Notification.Time.Media` |
| 47 | `Chronometer` | `android:layout_gravity` | `0x00800035` |
| 48 | `Chronometer` | `android:id` | `@id/chronometer` |
| 49 | `Chronometer` | `android:visibility` | `gone` |
| 50 | `Chronometer` | `android:layout_width` | `wrap_content` |
| 51 | `Chronometer` | `android:layout_height` | `wrap_content` |
| 52 | `Chronometer` | `android:singleLine` | `true` |
| 53 | `TextView` | `android:textAppearance` | `@style/TextAppearance.Compat.Notification.Info.Media` |
| 54 | `TextView` | `android:layout_gravity` | `0x00800055` |
| 55 | `TextView` | `android:id` | `@id/info` |
| 56 | `TextView` | `android:layout_width` | `wrap_content` |
| 57 | `TextView` | `android:layout_height` | `wrap_content` |
| 58 | `TextView` | `android:layout_marginTop` | `20.000000dip` |
| 59 | `TextView` | `android:singleLine` | `true` |
| 60 | `LinearLayout` | `android:orientation` | `horizontal` |
| 61 | `LinearLayout` | `android:id` | `@id/media_actions` |
| 62 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 63 | `LinearLayout` | `android:layout_height` | `48.000000dip` |
| 64 | `LinearLayout` | `android:layout_marginLeft` | `12.000000dip` |
| 65 | `LinearLayout` | `android:layout_marginRight` | `12.000000dip` |
| 66 | `LinearLayout` | `android:layout_alignParentBottom` | `true` |
| 67 | `LinearLayout` | `android:layoutDirection` | `ltr` |
| 68 | `ImageView` | `android:id` | `@id/action_divider` |
| 69 | `ImageView` | `android:background` | `?0x0101032C` |
| 70 | `ImageView` | `android:layout_width` | `match_parent` |
| 71 | `ImageView` | `android:layout_height` | `1.000000dip` |
| 72 | `ImageView` | `android:layout_above` | `@id/media_actions` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/notification_content_margin_start` | `0.000000dip` |
| `@dimen/notification_large_icon_height` | `64.000000dip` |
| `@dimen/notification_large_icon_width` | `64.000000dip` |
| `@dimen/notification_main_column_padding_top` | `0.000000dip` |
| `@dimen/notification_right_side_padding_top` | `4.000000dip` |
| `@style/TextAppearance.Compat.Notification.Info.Media` | `[]` |
| `@style/TextAppearance.Compat.Notification.Time.Media` | `[]` |

## ۴. شناسه‌های `@id`

```text
@id/action_divider
@id/chronometer
@id/info
@id/media_actions
@id/notification_main_column
@id/notification_main_column_container
@id/right_side
@id/status_bar_latest_event_content
@id/time
```

## ۵. ارجاع به لایه‌های دیگر

```text
2.000000dip
48.000000dip
@dimen/notification_large_icon_height
@dimen/notification_large_icon_width
@layout/notification_media_cancel_action
@layout/notification_template_icon_group
true
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/status_bar_latest_event_content" android:layout_width="match_parent" android:layout_height="128.000000dip">
  <include android:layout_width="@dimen/notification_large_icon_width" android:layout_height="@dimen/notification_large_icon_height" layout="@layout/notification_template_icon_group"/>
  <include android:layout_width="48.000000dip" android:layout_height="48.000000dip" android:layout_marginLeft="2.000000dip" android:layout_marginRight="2.000000dip" android:layout_alignParentRight="true" android:layout_alignParentEnd="true" layout="@layout/notification_media_cancel_action"/>
  <LinearLayout android:orientation="horizontal" android:id="@id/notification_main_column_container" android:paddingTop="@dimen/notification_main_column_padding_top" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginLeft="@dimen/notification_large_icon_height" android:minHeight="@dimen/notification_large_icon_height" android:layout_toLeftOf="@id/cancel_action" android:layout_marginStart="@dimen/notification_large_icon_height" android:layout_toStartOf="@id/cancel_action">
    <FrameLayout android:id="@id/notification_main_column" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginLeft="@dimen/notification_content_margin_start" android:layout_marginRight="8.000000dip" android:layout_marginBottom="8.000000dip" android:layout_weight="1.000000" android:layout_marginStart="@dimen/notification_content_margin_start" android:layout_marginEnd="8.000000dip"/>
    <FrameLayout android:id="@id/right_side" android:paddingTop="@dimen/notification_right_side_padding_top" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginRight="8.000000dip" android:layout_marginEnd="8.000000dip">
      <DateTimeView android:textAppearance="@style/TextAppearance.Compat.Notification.Time.Media" android:layout_gravity="0x00800035" android:id="@id/time" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:singleLine="true"/>
      <Chronometer android:textAppearance="@style/TextAppearance.Compat.Notification.Time.Media" android:layout_gravity="0x00800035" android:id="@id/chronometer" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:singleLine="true"/>
      <TextView android:textAppearance="@style/TextAppearance.Compat.Notification.Info.Media" android:layout_gravity="0x00800055" android:id="@id/info" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="20.000000dip" android:singleLine="true"/>
    </FrameLayout>
  </LinearLayout>
  <LinearLayout android:orientation="horizontal" android:id="@id/media_actions" android:layout_width="match_parent" android:layout_height="48.000000dip" android:layout_marginLeft="12.000000dip" android:layout_marginRight="12.000000dip" android:layout_alignParentBottom="true" android:layoutDirection="ltr"/>
  <ImageView android:id="@id/action_divider" android:background="?0x0101032C" android:layout_width="match_parent" android:layout_height="1.000000dip" android:layout_above="@id/media_actions"/>
</RelativeLayout>
```
