# پروندهٔ لایه — `res/layout/notification_template_big_media.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/notification_template_big_media.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/notification_template_big_media.xml`](../../SOURCE/res/layout/notification_template_big_media.xml) |
| SHA-256 دیکد | `ae4d18dcd361143c86f40e308e328ff5fe38d96bbb0b0463691dfa9408e204c2` |
| ریشه | `RelativeLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 12 |
| ارجاع به منابع | 10 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ RelativeLayout  #@id/status_bar_latest_event_content
   ├─ include
   ├─ include
   ├─ include
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
| 14 | `include` | `android:layout_gravity` | `0x00000070` |
| 15 | `include` | `android:layout_width` | `match_parent` |
| 16 | `include` | `android:layout_height` | `wrap_content` |
| 17 | `include` | `android:layout_marginLeft` | `@dimen/notification_large_icon_width` |
| 18 | `include` | `android:layout_toLeftOf` | `@id/cancel_action` |
| 19 | `include` | `android:layout_marginStart` | `@dimen/notification_large_icon_width` |
| 20 | `include` | `android:layout_toStartOf` | `@id/cancel_action` |
| 21 | `include` | `layout` | `@layout/notification_template_lines_media` |
| 22 | `LinearLayout` | `android:orientation` | `horizontal` |
| 23 | `LinearLayout` | `android:id` | `@id/media_actions` |
| 24 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 25 | `LinearLayout` | `android:layout_height` | `48.000000dip` |
| 26 | `LinearLayout` | `android:layout_marginLeft` | `12.000000dip` |
| 27 | `LinearLayout` | `android:layout_marginRight` | `12.000000dip` |
| 28 | `LinearLayout` | `android:layout_alignParentBottom` | `true` |
| 29 | `LinearLayout` | `android:layoutDirection` | `ltr` |
| 30 | `ImageView` | `android:id` | `@id/action_divider` |
| 31 | `ImageView` | `android:background` | `?0x0101032C` |
| 32 | `ImageView` | `android:layout_width` | `match_parent` |
| 33 | `ImageView` | `android:layout_height` | `1.000000dip` |
| 34 | `ImageView` | `android:layout_above` | `@id/media_actions` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/notification_large_icon_height` | `64.000000dip` |
| `@dimen/notification_large_icon_width` | `64.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/action_divider
@id/media_actions
@id/status_bar_latest_event_content
```

## ۵. ارجاع به لایه‌های دیگر

```text
0x00000070
2.000000dip
48.000000dip
@dimen/notification_large_icon_height
@dimen/notification_large_icon_width
@id/cancel_action
@layout/notification_media_cancel_action
@layout/notification_template_icon_group
@layout/notification_template_lines_media
match_parent
true
wrap_content
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
  <include android:layout_gravity="0x00000070" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginLeft="@dimen/notification_large_icon_width" android:layout_toLeftOf="@id/cancel_action" android:layout_marginStart="@dimen/notification_large_icon_width" android:layout_toStartOf="@id/cancel_action" layout="@layout/notification_template_lines_media"/>
  <LinearLayout android:orientation="horizontal" android:id="@id/media_actions" android:layout_width="match_parent" android:layout_height="48.000000dip" android:layout_marginLeft="12.000000dip" android:layout_marginRight="12.000000dip" android:layout_alignParentBottom="true" android:layoutDirection="ltr"/>
  <ImageView android:id="@id/action_divider" android:background="?0x0101032C" android:layout_width="match_parent" android:layout_height="1.000000dip" android:layout_above="@id/media_actions"/>
</RelativeLayout>
```
