# پروندهٔ لایه — `res/layout/notification_template_big_media_narrow.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/notification_template_big_media_narrow.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/notification_template_big_media_narrow.xml`](../../SOURCE/res/layout/notification_template_big_media_narrow.xml) |
| SHA-256 دیکد | `eef61bf5d5dfe65aff03adb495896196628fb300777063af2ea5e34f73cadb70` |
| ریشه | `RelativeLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 9 |
| ارجاع به منابع | 8 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ RelativeLayout  #@id/status_bar_latest_event_content
   ├─ ImageView  #@id/icon
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
| 15 | `include` | `android:layout_width` | `match_parent` |
| 16 | `include` | `android:layout_height` | `wrap_content` |
| 17 | `include` | `android:layout_marginLeft` | `128.000000dip` |
| 18 | `include` | `android:layout_toLeftOf` | `@id/cancel_action` |
| 19 | `include` | `android:layout_marginStart` | `128.000000dip` |
| 20 | `include` | `android:layout_toStartOf` | `@id/cancel_action` |
| 21 | `include` | `layout` | `@layout/notification_template_lines_media` |
| 22 | `LinearLayout` | `android:orientation` | `horizontal` |
| 23 | `LinearLayout` | `android:id` | `@id/media_actions` |
| 24 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 25 | `LinearLayout` | `android:layout_height` | `48.000000dip` |
| 26 | `LinearLayout` | `android:layout_marginLeft` | `12.000000dip` |
| 27 | `LinearLayout` | `android:layout_marginRight` | `12.000000dip` |
| 28 | `LinearLayout` | `android:layout_toRightOf` | `@id/icon` |
| 29 | `LinearLayout` | `android:layout_alignParentBottom` | `true` |
| 30 | `LinearLayout` | `android:layoutDirection` | `ltr` |
| 31 | `LinearLayout` | `android:layout_toEndOf` | `@id/icon` |
| 32 | `ImageView` | `android:id` | `@id/action_divider` |
| 33 | `ImageView` | `android:background` | `?0x0101032C` |
| 34 | `ImageView` | `android:layout_width` | `match_parent` |
| 35 | `ImageView` | `android:layout_height` | `1.000000dip` |
| 36 | `ImageView` | `android:layout_toRightOf` | `@id/icon` |
| 37 | `ImageView` | `android:layout_above` | `@id/media_actions` |
| 38 | `ImageView` | `android:layout_toEndOf` | `@id/icon` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/action_divider
@id/icon
@id/media_actions
@id/status_bar_latest_event_content
```

## ۵. ارجاع به لایه‌های دیگر

```text
128.000000dip
2.000000dip
48.000000dip
@id/cancel_action
@layout/notification_media_cancel_action
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
  <ImageView android:id="@id/icon" android:layout_width="128.000000dip" android:layout_height="128.000000dip" android:scaleType="centerCrop"/>
  <include android:layout_width="48.000000dip" android:layout_height="48.000000dip" android:layout_marginLeft="2.000000dip" android:layout_marginRight="2.000000dip" android:layout_alignParentRight="true" android:layout_alignParentEnd="true" layout="@layout/notification_media_cancel_action"/>
  <include android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginLeft="128.000000dip" android:layout_toLeftOf="@id/cancel_action" android:layout_marginStart="128.000000dip" android:layout_toStartOf="@id/cancel_action" layout="@layout/notification_template_lines_media"/>
  <LinearLayout android:orientation="horizontal" android:id="@id/media_actions" android:layout_width="match_parent" android:layout_height="48.000000dip" android:layout_marginLeft="12.000000dip" android:layout_marginRight="12.000000dip" android:layout_toRightOf="@id/icon" android:layout_alignParentBottom="true" android:layoutDirection="ltr" android:layout_toEndOf="@id/icon"/>
  <ImageView android:id="@id/action_divider" android:background="?0x0101032C" android:layout_width="match_parent" android:layout_height="1.000000dip" android:layout_toRightOf="@id/icon" android:layout_above="@id/media_actions" android:layout_toEndOf="@id/icon"/>
</RelativeLayout>
```
