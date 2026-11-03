# پروندهٔ لایه — `res/layout/notification_template_big_media_narrow_custom.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/notification_template_big_media_narrow_custom.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/notification_template_big_media_narrow_custom.xml`](../../SOURCE/res/layout/notification_template_big_media_narrow_custom.xml) |
| SHA-256 دیکد | `75baf988e4e988a60facf5beda35864442d1735375fc3f7a579356f15cd3a535` |
| ریشه | `RelativeLayout` |
| تعداد گره | 11 |
| تعداد شناسه | 10 |
| تگ‌های استفاده‌شده | 8 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 4 |
| ارجاع به منابع | 19 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ RelativeLayout  #@id/status_bar_latest_event_content
   ├─ ImageView  #@id/icon
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
| 4 | `ImageView` | `android:id` | `@id/icon` |
| 5 | `ImageView` | `android:layout_width` | `128.000000dip` |
| 6 | `ImageView` | `android:layout_height` | `128.000000dip` |
| 7 | `ImageView` | `android:scaleType` | `centerCrop` |
| 8 | `include` | `android:layout_width` | `48.000000dip` |
| 9 | `include` | `android:layout_height` | `48.000000dip` |
| 10 | `include` | `android:layout_marginLeft` | `2.000000dip` |
| 11 | `include` | `android:layout_marginRight` | `2.000000dip` |
| 12 | `include` | `android:layout_alignParentRight` | `true` |
| 13 | `include` | `android:layout_alignParentEnd` | `true` |
| 14 | `include` | `layout` | `@layout/notification_media_cancel_action` |
| 15 | `LinearLayout` | `android:orientation` | `horizontal` |
| 16 | `LinearLayout` | `android:id` | `@id/notification_main_column_container` |
| 17 | `LinearLayout` | `android:paddingTop` | `@dimen/notification_main_column_padding_top` |
| 18 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 19 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 20 | `LinearLayout` | `android:layout_marginLeft` | `128.000000dip` |
| 21 | `LinearLayout` | `android:minHeight` | `@dimen/notification_large_icon_height` |
| 22 | `LinearLayout` | `android:layout_toLeftOf` | `@id/cancel_action` |
| 23 | `LinearLayout` | `android:layout_marginStart` | `128.000000dip` |
| 24 | `LinearLayout` | `android:layout_toStartOf` | `@id/cancel_action` |
| 25 | `FrameLayout` | `android:id` | `@id/notification_main_column` |
| 26 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 27 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 28 | `FrameLayout` | `android:layout_marginLeft` | `@dimen/notification_media_narrow_margin` |
| 29 | `FrameLayout` | `android:layout_marginRight` | `8.000000dip` |
| 30 | `FrameLayout` | `android:layout_marginBottom` | `8.000000dip` |
| 31 | `FrameLayout` | `android:layout_weight` | `1.000000` |
| 32 | `FrameLayout` | `android:layout_marginStart` | `@dimen/notification_media_narrow_margin` |
| 33 | `FrameLayout` | `android:layout_marginEnd` | `8.000000dip` |
| 34 | `FrameLayout` | `android:id` | `@id/right_side` |
| 35 | `FrameLayout` | `android:paddingTop` | `@dimen/notification_right_side_padding_top` |
| 36 | `FrameLayout` | `android:layout_width` | `wrap_content` |
| 37 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 38 | `FrameLayout` | `android:layout_marginRight` | `8.000000dip` |
| 39 | `FrameLayout` | `android:layout_marginEnd` | `8.000000dip` |
| 40 | `DateTimeView` | `android:textAppearance` | `@style/TextAppearance.Compat.Notification.Time.Media` |
| 41 | `DateTimeView` | `android:layout_gravity` | `0x00800035` |
| 42 | `DateTimeView` | `android:id` | `@id/time` |
| 43 | `DateTimeView` | `android:visibility` | `gone` |
| 44 | `DateTimeView` | `android:layout_width` | `wrap_content` |
| 45 | `DateTimeView` | `android:layout_height` | `wrap_content` |
| 46 | `DateTimeView` | `android:singleLine` | `true` |
| 47 | `Chronometer` | `android:textAppearance` | `@style/TextAppearance.Compat.Notification.Time.Media` |
| 48 | `Chronometer` | `android:layout_gravity` | `0x00800035` |
| 49 | `Chronometer` | `android:id` | `@id/chronometer` |
| 50 | `Chronometer` | `android:visibility` | `gone` |
| 51 | `Chronometer` | `android:layout_width` | `wrap_content` |
| 52 | `Chronometer` | `android:layout_height` | `wrap_content` |
| 53 | `Chronometer` | `android:singleLine` | `true` |
| 54 | `TextView` | `android:textAppearance` | `@style/TextAppearance.Compat.Notification.Info.Media` |
| 55 | `TextView` | `android:layout_gravity` | `0x00800055` |
| 56 | `TextView` | `android:id` | `@id/info` |
| 57 | `TextView` | `android:layout_width` | `wrap_content` |
| 58 | `TextView` | `android:layout_height` | `wrap_content` |
| 59 | `TextView` | `android:layout_marginTop` | `20.000000dip` |
| 60 | `TextView` | `android:singleLine` | `true` |
| 61 | `LinearLayout` | `android:orientation` | `horizontal` |
| 62 | `LinearLayout` | `android:id` | `@id/media_actions` |
| 63 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 64 | `LinearLayout` | `android:layout_height` | `48.000000dip` |
| 65 | `LinearLayout` | `android:layout_marginLeft` | `12.000000dip` |
| 66 | `LinearLayout` | `android:layout_marginRight` | `12.000000dip` |
| 67 | `LinearLayout` | `android:layout_toRightOf` | `@id/icon` |
| 68 | `LinearLayout` | `android:layout_alignParentBottom` | `true` |
| 69 | `LinearLayout` | `android:layoutDirection` | `ltr` |
| 70 | `LinearLayout` | `android:layout_toEndOf` | `@id/icon` |
| 71 | `ImageView` | `android:id` | `@id/action_divider` |
| 72 | `ImageView` | `android:background` | `?0x0101032C` |
| 73 | `ImageView` | `android:layout_width` | `match_parent` |
| 74 | `ImageView` | `android:layout_height` | `1.000000dip` |
| 75 | `ImageView` | `android:layout_toRightOf` | `@id/icon` |
| 76 | `ImageView` | `android:layout_above` | `@id/media_actions` |
| 77 | `ImageView` | `android:layout_toEndOf` | `@id/icon` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/notification_large_icon_height` | `64.000000dip` |
| `@dimen/notification_main_column_padding_top` | `0.000000dip` |
| `@dimen/notification_media_narrow_margin` | `12.000000dip` |
| `@dimen/notification_right_side_padding_top` | `4.000000dip` |
| `@style/TextAppearance.Compat.Notification.Info.Media` | `[]` |
| `@style/TextAppearance.Compat.Notification.Time.Media` | `[]` |

## ۴. شناسه‌های `@id`

```text
@id/action_divider
@id/chronometer
@id/icon
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
@layout/notification_media_cancel_action
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
  <ImageView android:id="@id/icon" android:layout_width="128.000000dip" android:layout_height="128.000000dip" android:scaleType="centerCrop"/>
  <include android:layout_width="48.000000dip" android:layout_height="48.000000dip" android:layout_marginLeft="2.000000dip" android:layout_marginRight="2.000000dip" android:layout_alignParentRight="true" android:layout_alignParentEnd="true" layout="@layout/notification_media_cancel_action"/>
  <LinearLayout android:orientation="horizontal" android:id="@id/notification_main_column_container" android:paddingTop="@dimen/notification_main_column_padding_top" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginLeft="128.000000dip" android:minHeight="@dimen/notification_large_icon_height" android:layout_toLeftOf="@id/cancel_action" android:layout_marginStart="128.000000dip" android:layout_toStartOf="@id/cancel_action">
    <FrameLayout android:id="@id/notification_main_column" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginLeft="@dimen/notification_media_narrow_margin" android:layout_marginRight="8.000000dip" android:layout_marginBottom="8.000000dip" android:layout_weight="1.000000" android:layout_marginStart="@dimen/notification_media_narrow_margin" android:layout_marginEnd="8.000000dip"/>
    <FrameLayout android:id="@id/right_side" android:paddingTop="@dimen/notification_right_side_padding_top" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginRight="8.000000dip" android:layout_marginEnd="8.000000dip">
      <DateTimeView android:textAppearance="@style/TextAppearance.Compat.Notification.Time.Media" android:layout_gravity="0x00800035" android:id="@id/time" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:singleLine="true"/>
      <Chronometer android:textAppearance="@style/TextAppearance.Compat.Notification.Time.Media" android:layout_gravity="0x00800035" android:id="@id/chronometer" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:singleLine="true"/>
      <TextView android:textAppearance="@style/TextAppearance.Compat.Notification.Info.Media" android:layout_gravity="0x00800055" android:id="@id/info" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="20.000000dip" android:singleLine="true"/>
    </FrameLayout>
  </LinearLayout>
  <LinearLayout android:orientation="horizontal" android:id="@id/media_actions" android:layout_width="match_parent" android:layout_height="48.000000dip" android:layout_marginLeft="12.000000dip" android:layout_marginRight="12.000000dip" android:layout_toRightOf="@id/icon" android:layout_alignParentBottom="true" android:layoutDirection="ltr" android:layout_toEndOf="@id/icon"/>
  <ImageView android:id="@id/action_divider" android:background="?0x0101032C" android:layout_width="match_parent" android:layout_height="1.000000dip" android:layout_toRightOf="@id/icon" android:layout_above="@id/media_actions" android:layout_toEndOf="@id/icon"/>
</RelativeLayout>
```
