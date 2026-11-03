# پروندهٔ لایه — `res/layout/mtrl_calendar_days_of_week.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mtrl_calendar_days_of_week.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mtrl_calendar_days_of_week.xml`](../../SOURCE/res/layout/mtrl_calendar_days_of_week.xml) |
| SHA-256 دیکد | `4c94c829a0ba4cdbe494773b620b709ecc11685ad8d74c9ec477c5ed4e778af8` |
| ریشه | `GridView` |
| تعداد گره | 1 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 3 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ GridView  #@id/mtrl_calendar_days_of_week
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `GridView` | `android:gravity` | `0x00000001` |
| 2 | `GridView` | `android:id` | `@id/mtrl_calendar_days_of_week` |
| 3 | `GridView` | `android:layout_width` | `match_parent` |
| 4 | `GridView` | `android:layout_height` | `@dimen/mtrl_calendar_days_of_week_height` |
| 5 | `GridView` | `android:horizontalSpacing` | `@dimen/mtrl_calendar_month_horizontal_padding` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/mtrl_calendar_days_of_week_height` | `24.000000dip` / `20.000000dip` (h360dp-land) / `20.000000dip` (land) / `40.000000dip` (w360dp-port) / `48.000000dip` (w400dp-port) |
| `@dimen/mtrl_calendar_month_horizontal_padding` | `2.000000dip` / `4.000000dip` (h360dp-land) / `0.000000dip` (h480dp-land) / `4.000000dip` (w360dp-port) / `0.000000dip` (w400dp-port) |

## ۴. شناسه‌های `@id`

```text
@id/mtrl_calendar_days_of_week
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/mtrl_calendar_horizontal.xml
res/layout/mtrl_calendar_vertical.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<GridView xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00000001" android:id="@id/mtrl_calendar_days_of_week" android:layout_width="match_parent" android:layout_height="@dimen/mtrl_calendar_days_of_week_height" android:horizontalSpacing="@dimen/mtrl_calendar_month_horizontal_padding"/>
```
