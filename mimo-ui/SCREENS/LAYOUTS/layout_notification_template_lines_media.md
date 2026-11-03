# پروندهٔ لایه — `res/layout/notification_template_lines_media.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/notification_template_lines_media.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/notification_template_lines_media.xml`](../../SOURCE/res/layout/notification_template_lines_media.xml) |
| SHA-256 دیکد | `36186923c5c2fb25340998fc3e34f60dd2852400a41d472317e520cbf5e51dc8` |
| ریشه | `LinearLayout` |
| تعداد گره | 9 |
| تعداد شناسه | 8 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 14 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ LinearLayout  #@id/line1
   │  ├─ TextView  #@id/title
   │  ├─ DateTimeView  #@id/time
   │  └─ Chronometer  #@id/chronometer
   ├─ TextView  #@id/text2
   └─ LinearLayout  #@id/line3
      ├─ TextView  #@id/text
      └─ TextView  #@id/info
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:paddingTop` | `2.000000dip` |
| 3 | `LinearLayout` | `android:paddingRight` | `8.000000dip` |
| 4 | `LinearLayout` | `android:paddingBottom` | `2.000000dip` |
| 5 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 6 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 7 | `LinearLayout` | `android:paddingEnd` | `8.000000dip` |
| 8 | `LinearLayout` | `android:orientation` | `horizontal` |
| 9 | `LinearLayout` | `android:id` | `@id/line1` |
| 10 | `LinearLayout` | `android:paddingTop` | `6.000000dip` |
| 11 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 12 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 13 | `LinearLayout` | `android:layout_marginLeft` | `@dimen/notification_content_margin_start` |
| 14 | `LinearLayout` | `android:layout_marginStart` | `@dimen/notification_content_margin_start` |
| 15 | `TextView` | `android:textAppearance` | `@style/TextAppearance.Compat.Notification.Title.Media` |
| 16 | `TextView` | `android:ellipsize` | `marquee` |
| 17 | `TextView` | `android:id` | `@id/title` |
| 18 | `TextView` | `android:fadingEdge` | `0x00001000` |
| 19 | `TextView` | `android:layout_width` | `match_parent` |
| 20 | `TextView` | `android:layout_height` | `wrap_content` |
| 21 | `TextView` | `android:singleLine` | `true` |
| 22 | `TextView` | `android:layout_weight` | `1.000000` |
| 23 | `DateTimeView` | `android:textAppearance` | `@style/TextAppearance.Compat.Notification.Time.Media` |
| 24 | `DateTimeView` | `android:layout_gravity` | `0x00000011` |
| 25 | `DateTimeView` | `android:id` | `@id/time` |
| 26 | `DateTimeView` | `android:paddingLeft` | `8.000000dip` |
| 27 | `DateTimeView` | `android:visibility` | `gone` |
| 28 | `DateTimeView` | `android:layout_width` | `wrap_content` |
| 29 | `DateTimeView` | `android:layout_height` | `wrap_content` |
| 30 | `DateTimeView` | `android:singleLine` | `true` |
| 31 | `DateTimeView` | `android:layout_weight` | `0.000000` |
| 32 | `DateTimeView` | `android:paddingStart` | `8.000000dip` |
| 33 | `Chronometer` | `android:textAppearance` | `@style/TextAppearance.Compat.Notification.Time.Media` |
| 34 | `Chronometer` | `android:layout_gravity` | `0x00000011` |
| 35 | `Chronometer` | `android:id` | `@id/chronometer` |
| 36 | `Chronometer` | `android:paddingLeft` | `8.000000dip` |
| 37 | `Chronometer` | `android:visibility` | `gone` |
| 38 | `Chronometer` | `android:layout_width` | `wrap_content` |
| 39 | `Chronometer` | `android:layout_height` | `wrap_content` |
| 40 | `Chronometer` | `android:singleLine` | `true` |
| 41 | `Chronometer` | `android:layout_weight` | `0.000000` |
| 42 | `Chronometer` | `android:paddingStart` | `8.000000dip` |
| 43 | `TextView` | `android:textAppearance` | `@style/TextAppearance.Compat.Notification.Line2.Media` |
| 44 | `TextView` | `android:ellipsize` | `marquee` |
| 45 | `TextView` | `android:id` | `@id/text2` |
| 46 | `TextView` | `android:visibility` | `gone` |
| 47 | `TextView` | `android:fadingEdge` | `0x00001000` |
| 48 | `TextView` | `android:layout_width` | `match_parent` |
| 49 | `TextView` | `android:layout_height` | `wrap_content` |
| 50 | `TextView` | `android:layout_marginLeft` | `@dimen/notification_content_margin_start` |
| 51 | `TextView` | `android:layout_marginTop` | `16777214.000000dip` |
| 52 | `TextView` | `android:layout_marginBottom` | `16777214.000000dip` |
| 53 | `TextView` | `android:singleLine` | `true` |
| 54 | `TextView` | `android:layout_marginStart` | `@dimen/notification_content_margin_start` |
| 55 | `LinearLayout` | `android:gravity` | `0x00000010` |
| 56 | `LinearLayout` | `android:orientation` | `horizontal` |
| 57 | `LinearLayout` | `android:id` | `@id/line3` |
| 58 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 59 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 60 | `LinearLayout` | `android:layout_marginLeft` | `@dimen/notification_content_margin_start` |
| 61 | `LinearLayout` | `android:layout_marginStart` | `@dimen/notification_content_margin_start` |
| 62 | `TextView` | `android:textAppearance` | `@style/TextAppearance.Compat.Notification.Media` |
| 63 | `TextView` | `android:ellipsize` | `marquee` |
| 64 | `TextView` | `android:layout_gravity` | `0x00000011` |
| 65 | `TextView` | `android:id` | `@id/text` |
| 66 | `TextView` | `android:fadingEdge` | `0x00001000` |
| 67 | `TextView` | `android:layout_width` | `0.000000dip` |
| 68 | `TextView` | `android:layout_height` | `wrap_content` |
| 69 | `TextView` | `android:singleLine` | `true` |
| 70 | `TextView` | `android:layout_weight` | `1.000000` |
| 71 | `TextView` | `android:textAppearance` | `@style/TextAppearance.Compat.Notification.Info.Media` |
| 72 | `TextView` | `android:gravity` | `0x00000011` |
| 73 | `TextView` | `android:layout_gravity` | `0x00000011` |
| 74 | `TextView` | `android:id` | `@id/info` |
| 75 | `TextView` | `android:paddingLeft` | `8.000000dip` |
| 76 | `TextView` | `android:layout_width` | `wrap_content` |
| 77 | `TextView` | `android:layout_height` | `wrap_content` |
| 78 | `TextView` | `android:singleLine` | `true` |
| 79 | `TextView` | `android:layout_weight` | `0.000000` |
| 80 | `TextView` | `android:paddingStart` | `8.000000dip` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/notification_content_margin_start` | `0.000000dip` |
| `@style/TextAppearance.Compat.Notification.Info.Media` | `[]` |
| `@style/TextAppearance.Compat.Notification.Line2.Media` | `[]` |
| `@style/TextAppearance.Compat.Notification.Media` | `[]` |
| `@style/TextAppearance.Compat.Notification.Time.Media` | `[]` |
| `@style/TextAppearance.Compat.Notification.Title.Media` | `[]` |

## ۴. شناسه‌های `@id`

```text
@id/chronometer
@id/info
@id/line1
@id/line3
@id/text
@id/text2
@id/time
@id/title
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/notification_template_big_media.xml
res/layout/notification_template_big_media_narrow.xml
res/layout/notification_template_media.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:paddingTop="2.000000dip" android:paddingRight="8.000000dip" android:paddingBottom="2.000000dip" android:layout_width="wrap_content" android:layout_height="wrap_content" android:paddingEnd="8.000000dip">
  <LinearLayout android:orientation="horizontal" android:id="@id/line1" android:paddingTop="6.000000dip" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginLeft="@dimen/notification_content_margin_start" android:layout_marginStart="@dimen/notification_content_margin_start">
    <TextView android:textAppearance="@style/TextAppearance.Compat.Notification.Title.Media" android:ellipsize="marquee" android:id="@id/title" android:fadingEdge="0x00001000" android:layout_width="match_parent" android:layout_height="wrap_content" android:singleLine="true" android:layout_weight="1.000000"/>
    <DateTimeView android:textAppearance="@style/TextAppearance.Compat.Notification.Time.Media" android:layout_gravity="0x00000011" android:id="@id/time" android:paddingLeft="8.000000dip" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:singleLine="true" android:layout_weight="0.000000" android:paddingStart="8.000000dip"/>
    <Chronometer android:textAppearance="@style/TextAppearance.Compat.Notification.Time.Media" android:layout_gravity="0x00000011" android:id="@id/chronometer" android:paddingLeft="8.000000dip" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:singleLine="true" android:layout_weight="0.000000" android:paddingStart="8.000000dip"/>
  </LinearLayout>
  <TextView android:textAppearance="@style/TextAppearance.Compat.Notification.Line2.Media" android:ellipsize="marquee" android:id="@id/text2" android:visibility="gone" android:fadingEdge="0x00001000" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginLeft="@dimen/notification_content_margin_start" android:layout_marginTop="16777214.000000dip" android:layout_marginBottom="16777214.000000dip" android:singleLine="true" android:layout_marginStart="@dimen/notification_content_margin_start"/>
  <LinearLayout android:gravity="0x00000010" android:orientation="horizontal" android:id="@id/line3" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginLeft="@dimen/notification_content_margin_start" android:layout_marginStart="@dimen/notification_content_margin_start">
    <TextView android:textAppearance="@style/TextAppearance.Compat.Notification.Media" android:ellipsize="marquee" android:layout_gravity="0x00000011" android:id="@id/text" android:fadingEdge="0x00001000" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:singleLine="true" android:layout_weight="1.000000"/>
    <TextView android:textAppearance="@style/TextAppearance.Compat.Notification.Info.Media" android:gravity="0x00000011" android:layout_gravity="0x00000011" android:id="@id/info" android:paddingLeft="8.000000dip" android:layout_width="wrap_content" android:layout_height="wrap_content" android:singleLine="true" android:layout_weight="0.000000" android:paddingStart="8.000000dip"/>
  </LinearLayout>
</LinearLayout>
```
