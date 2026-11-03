# پروندهٔ لایه — `res/layout/mtrl_calendar_month_labeled.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mtrl_calendar_month_labeled.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mtrl_calendar_month_labeled.xml`](../../SOURCE/res/layout/mtrl_calendar_month_labeled.xml) |
| SHA-256 دیکد | `ad4e334a6ea8658dd85590b0b24702857fb457b961028681f93d1d5fe5a8f757` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 1 |
| ارجاع به منابع | 4 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ TextView  #@id/month_title
   └─ include
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 3 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 4 | `TextView` | `android:gravity` | `0x00800013` |
| 5 | `TextView` | `android:id` | `@id/month_title` |
| 6 | `TextView` | `android:focusable` | `true` |
| 7 | `TextView` | `android:layout_width` | `match_parent` |
| 8 | `TextView` | `android:layout_height` | `@dimen/mtrl_calendar_day_height` |
| 9 | `TextView` | `style` | `?attr/materialCalendarMonth` |
| 10 | `include` | `layout` | `@layout/mtrl_calendar_month` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/mtrl_calendar_day_height` | `32.000000dip` / `40.000000dip` (h360dp-land) / `48.000000dip` (h480dp-land) / `40.000000dip` (w360dp-port) / `48.000000dip` (w400dp-port) |

## ۴. شناسه‌های `@id`

```text
@id/month_title
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/mtrl_calendar_month
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:layout_width="match_parent" android:layout_height="wrap_content">
  <TextView android:gravity="0x00800013" android:id="@id/month_title" android:focusable="true" android:layout_width="match_parent" android:layout_height="@dimen/mtrl_calendar_day_height" style="?attr/materialCalendarMonth"/>
  <include layout="@layout/mtrl_calendar_month"/>
</LinearLayout>
```
