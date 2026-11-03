# پروندهٔ لایه — `res/layout/mtrl_calendar_day_of_week.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mtrl_calendar_day_of_week.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mtrl_calendar_day_of_week.xml`](../../SOURCE/res/layout/mtrl_calendar_day_of_week.xml) |
| SHA-256 دیکد | `60f532032a0b5062f66b779014d2ccb2dc26bd7b4b559e416dd236a0e1f3c9dc` |
| ریشه | `TextView` |
| تعداد گره | 1 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 3 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ TextView
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `TextView` | `android:layout_width` | `@dimen/mtrl_calendar_day_width` |
| 2 | `TextView` | `android:layout_height` | `@dimen/mtrl_calendar_days_of_week_height` |
| 3 | `TextView` | `style` | `?attr/materialCalendarDayOfWeekLabel` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/mtrl_calendar_day_width` | `36.000000dip` / `40.000000dip` (h360dp-land) / `48.000000dip` (h480dp-land) / `40.000000dip` (w360dp-port) / `48.000000dip` (w400dp-port) |
| `@dimen/mtrl_calendar_days_of_week_height` | `24.000000dip` / `20.000000dip` (h360dp-land) / `20.000000dip` (land) / `40.000000dip` (w360dp-port) / `48.000000dip` (w400dp-port) |

## ۴. شناسه‌های `@id`

```text
(none)
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
<TextView xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="@dimen/mtrl_calendar_day_width" android:layout_height="@dimen/mtrl_calendar_days_of_week_height" style="?attr/materialCalendarDayOfWeekLabel"/>
```
