# پروندهٔ لایه — `res/layout/notification_template_media.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/notification_template_media.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/notification_template_media.xml`](../../SOURCE/res/layout/notification_template_media.xml) |
| SHA-256 دیکد | `b58454797641cf27deabd2c8f6fa15e6b3372621531301686551bb6ae22640f0` |
| ریشه | `LinearLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 11 |
| ارجاع به منابع | 8 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/status_bar_latest_event_content
   ├─ include
   ├─ include
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
| 8 | `include` | `android:layout_width` | `0.000000dip` |
| 9 | `include` | `android:layout_height` | `wrap_content` |
| 10 | `include` | `android:layout_weight` | `1.000000` |
| 11 | `include` | `layout` | `@layout/notification_template_lines_media` |
| 12 | `LinearLayout` | `android:layout_gravity` | `0x00800015` |
| 13 | `LinearLayout` | `android:orientation` | `horizontal` |
| 14 | `LinearLayout` | `android:id` | `@id/media_actions` |
| 15 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 16 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 17 | `LinearLayout` | `android:layoutDirection` | `ltr` |
| 18 | `include` | `android:layout_width` | `48.000000dip` |
| 19 | `include` | `android:layout_height` | `match_parent` |
| 20 | `include` | `android:layout_marginRight` | `6.000000dip` |
| 21 | `include` | `android:layout_marginEnd` | `6.000000dip` |
| 22 | `include` | `layout` | `@layout/notification_media_cancel_action` |
| 23 | `ImageView` | `android:id` | `@id/end_padder` |
| 24 | `ImageView` | `android:layout_width` | `6.000000dip` |
| 25 | `ImageView` | `android:layout_height` | `match_parent` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/notification_large_icon_height` | `64.000000dip` |
| `@dimen/notification_large_icon_width` | `64.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/end_padder
@id/media_actions
@id/status_bar_latest_event_content
```

## ۵. ارجاع به لایه‌های دیگر

```text
0.000000dip
1.000000
48.000000dip
6.000000dip
@dimen/notification_large_icon_height
@dimen/notification_large_icon_width
@layout/notification_media_cancel_action
@layout/notification_template_icon_group
@layout/notification_template_lines_media
match_parent
wrap_content
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
  <include android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_weight="1.000000" layout="@layout/notification_template_lines_media"/>
  <LinearLayout android:layout_gravity="0x00800015" android:orientation="horizontal" android:id="@id/media_actions" android:layout_width="wrap_content" android:layout_height="match_parent" android:layoutDirection="ltr"/>
  <include android:layout_width="48.000000dip" android:layout_height="match_parent" android:layout_marginRight="6.000000dip" android:layout_marginEnd="6.000000dip" layout="@layout/notification_media_cancel_action"/>
  <ImageView android:id="@id/end_padder" android:layout_width="6.000000dip" android:layout_height="match_parent"/>
</LinearLayout>
```
