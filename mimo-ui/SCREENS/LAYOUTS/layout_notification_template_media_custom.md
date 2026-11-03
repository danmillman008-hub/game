# پروندهٔ لایه — `res/layout/notification_template_media_custom.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/notification_template_media_custom.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/notification_template_media_custom.xml`](../../SOURCE/res/layout/notification_template_media_custom.xml) |
| SHA-256 دیکد | `2f411a23c0f6be09d0dcc0c43a73d1ee65ff7aa9c8382710abbf46056a6f86d2` |
| ریشه | `LinearLayout` |
| تعداد گره | 11 |
| تعداد شناسه | 9 |
| تگ‌های استفاده‌شده | 7 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 7 |
| ارجاع به منابع | 19 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/status_bar_latest_event_content
   ├─ include
   ├─ LinearLayout  #@id/notification_main_column_container
   │  ├─ FrameLayout  #@id/notification_main_column
   │  └─ FrameLayout  #@id/right_side
   │     ├─ DateTimeView  #@id/time
   │     ├─ Chronometer  #@id/chronometer
   │     └─ TextView  #@id/info
   ├─ LinearLayout  #@id/media_actions
   ├─ include
   └─ ImageView  #@id/end_padder
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `horizontal` |
| 2 | `LinearLayout` | `android:id` | `@id/status_bar_latest_event_content` |
| 3 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 4 | `LinearLayout` | `android:layout_height` | `64.000000dip` |
| 5 | `include` | `android:layout_width` | `@dimen/notification_large_icon_width` |
| 6 | `include` | `android:layout_height` | `@dimen/notification_large_icon_height` |
| 7 | `include` | `layout` | `@layout/notification_template_icon_group` |
| 8 | `LinearLayout` | `android:orientation` | `horizontal` |
| 9 | `LinearLayout` | `android:id` | `@id/notification_main_column_container` |
| 10 | `LinearLayout` | `android:paddingTop` | `@dimen/notification_main_column_padding_top` |
| 11 | `LinearLayout` | `android:layout_width` | `0.000000dip` |
| 12 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 13 | `LinearLayout` | `android:minHeight` | `@dimen/notification_large_icon_height` |
| 14 | `LinearLayout` | `android:layout_weight` | `1.000000` |
| 15 | `LinearLayout` | `android:layout_toLeftOf` | `@id/cancel_action` |
| 16 | `LinearLayout` | `android:layout_toStartOf` | `@id/cancel_action` |
| 17 | `FrameLayout` | `android:id` | `@id/notification_main_column` |
| 18 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 19 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 20 | `FrameLayout` | `android:layout_marginLeft` | `@dimen/notification_content_margin_start` |
| 21 | `FrameLayout` | `android:layout_marginRight` | `8.000000dip` |
| 22 | `FrameLayout` | `android:layout_marginBottom` | `8.000000dip` |
| 23 | `FrameLayout` | `android:layout_weight` | `1.000000` |
| 24 | `FrameLayout` | `android:layout_marginStart` | `@dimen/notification_content_margin_start` |
| 25 | `FrameLayout` | `android:layout_marginEnd` | `8.000000dip` |
| 26 | `FrameLayout` | `android:id` | `@id/right_side` |
| 27 | `FrameLayout` | `android:paddingTop` | `@dimen/notification_right_side_padding_top` |
| 28 | `FrameLayout` | `android:layout_width` | `wrap_content` |
| 29 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 30 | `FrameLayout` | `android:layout_marginRight` | `8.000000dip` |
| 31 | `FrameLayout` | `android:layout_marginEnd` | `8.000000dip` |
| 32 | `DateTimeView` | `android:textAppearance` | `@style/TextAppearance.Compat.Notification.Time.Media` |
| 33 | `DateTimeView` | `android:layout_gravity` | `0x00800035` |
| 34 | `DateTimeView` | `android:id` | `@id/time` |
| 35 | `DateTimeView` | `android:visibility` | `gone` |
| 36 | `DateTimeView` | `android:layout_width` | `wrap_content` |
| 37 | `DateTimeView` | `android:layout_height` | `wrap_content` |
| 38 | `DateTimeView` | `android:singleLine` | `true` |
| 39 | `Chronometer` | `android:textAppearance` | `@style/TextAppearance.Compat.Notification.Time.Media` |
| 40 | `Chronometer` | `android:layout_gravity` | `0x00800035` |
| 41 | `Chronometer` | `android:id` | `@id/chronometer` |
| 42 | `Chronometer` | `android:visibility` | `gone` |
| 43 | `Chronometer` | `android:layout_width` | `wrap_content` |
| 44 | `Chronometer` | `android:layout_height` | `wrap_content` |
| 45 | `Chronometer` | `android:singleLine` | `true` |
| 46 | `TextView` | `android:textAppearance` | `@style/TextAppearance.Compat.Notification.Info.Media` |
| 47 | `TextView` | `android:layout_gravity` | `0x00800055` |
| 48 | `TextView` | `android:id` | `@id/info` |
| 49 | `TextView` | `android:layout_width` | `wrap_content` |
| 50 | `TextView` | `android:layout_height` | `wrap_content` |
| 51 | `TextView` | `android:layout_marginTop` | `20.000000dip` |
| 52 | `TextView` | `android:singleLine` | `true` |
| 53 | `LinearLayout` | `android:layout_gravity` | `0x00800015` |
| 54 | `LinearLayout` | `android:orientation` | `horizontal` |
| 55 | `LinearLayout` | `android:id` | `@id/media_actions` |
| 56 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 57 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 58 | `LinearLayout` | `android:layoutDirection` | `ltr` |
| 59 | `include` | `android:layout_width` | `48.000000dip` |
| 60 | `include` | `android:layout_height` | `match_parent` |
| 61 | `include` | `android:layout_marginRight` | `6.000000dip` |
| 62 | `include` | `android:layout_marginEnd` | `6.000000dip` |
| 63 | `include` | `layout` | `@layout/notification_media_cancel_action` |
| 64 | `ImageView` | `android:id` | `@id/end_padder` |
| 65 | `ImageView` | `android:layout_width` | `6.000000dip` |
| 66 | `ImageView` | `android:layout_height` | `match_parent` |

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
@id/chronometer
@id/end_padder
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
48.000000dip
6.000000dip
@dimen/notification_large_icon_height
@dimen/notification_large_icon_width
@layout/notification_media_cancel_action
@layout/notification_template_icon_group
match_parent
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="horizontal" android:id="@id/status_bar_latest_event_content" android:layout_width="match_parent" android:layout_height="64.000000dip">
  <include android:layout_width="@dimen/notification_large_icon_width" android:layout_height="@dimen/notification_large_icon_height" layout="@layout/notification_template_icon_group"/>
  <LinearLayout android:orientation="horizontal" android:id="@id/notification_main_column_container" android:paddingTop="@dimen/notification_main_column_padding_top" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:minHeight="@dimen/notification_large_icon_height" android:layout_weight="1.000000" android:layout_toLeftOf="@id/cancel_action" android:layout_toStartOf="@id/cancel_action">
    <FrameLayout android:id="@id/notification_main_column" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginLeft="@dimen/notification_content_margin_start" android:layout_marginRight="8.000000dip" android:layout_marginBottom="8.000000dip" android:layout_weight="1.000000" android:layout_marginStart="@dimen/notification_content_margin_start" android:layout_marginEnd="8.000000dip"/>
    <FrameLayout android:id="@id/right_side" android:paddingTop="@dimen/notification_right_side_padding_top" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginRight="8.000000dip" android:layout_marginEnd="8.000000dip">
      <DateTimeView android:textAppearance="@style/TextAppearance.Compat.Notification.Time.Media" android:layout_gravity="0x00800035" android:id="@id/time" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:singleLine="true"/>
      <Chronometer android:textAppearance="@style/TextAppearance.Compat.Notification.Time.Media" android:layout_gravity="0x00800035" android:id="@id/chronometer" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:singleLine="true"/>
      <TextView android:textAppearance="@style/TextAppearance.Compat.Notification.Info.Media" android:layout_gravity="0x00800055" android:id="@id/info" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="20.000000dip" android:singleLine="true"/>
    </FrameLayout>
  </LinearLayout>
  <LinearLayout android:layout_gravity="0x00800015" android:orientation="horizontal" android:id="@id/media_actions" android:layout_width="wrap_content" android:layout_height="match_parent" android:layoutDirection="ltr"/>
  <include android:layout_width="48.000000dip" android:layout_height="match_parent" android:layout_marginRight="6.000000dip" android:layout_marginEnd="6.000000dip" layout="@layout/notification_media_cancel_action"/>
  <ImageView android:id="@id/end_padder" android:layout_width="6.000000dip" android:layout_height="match_parent"/>
</LinearLayout>
```
