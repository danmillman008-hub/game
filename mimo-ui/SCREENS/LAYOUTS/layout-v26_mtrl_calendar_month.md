# پروندهٔ لایه — `res/layout-v26/mtrl_calendar_month.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-v26/mtrl_calendar_month.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-v26/mtrl_calendar_month.xml`](../../SOURCE/res/layout-v26/mtrl_calendar_month.xml) |
| SHA-256 دیکد | `2bd101552edf0ff42e518bfca11aa59e76a7d78f5e9f99ffa8f478bb16068a7e` |
| ریشه | `com.google.android.material.datepicker.MaterialCalendarGridView` |
| تعداد گره | 1 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 4 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ com.google.android.material.datepicker.MaterialCalendarGridView  #@id/month_grid
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `com.google.android.material.datepicker.MaterialCalendarGridView` | `android:gravity` | `0x00000011` |
| 2 | `com.google.android.material.datepicker.MaterialCalendarGridView` | `android:id` | `@id/month_grid` |
| 3 | `com.google.android.material.datepicker.MaterialCalendarGridView` | `android:addStatesFromChildren` | `false` |
| 4 | `com.google.android.material.datepicker.MaterialCalendarGridView` | `android:descendantFocusability` | `1` |
| 5 | `com.google.android.material.datepicker.MaterialCalendarGridView` | `android:layout_width` | `match_parent` |
| 6 | `com.google.android.material.datepicker.MaterialCalendarGridView` | `android:layout_height` | `match_parent` |
| 7 | `com.google.android.material.datepicker.MaterialCalendarGridView` | `android:listSelector` | `@0x0106000D` |
| 8 | `com.google.android.material.datepicker.MaterialCalendarGridView` | `android:horizontalSpacing` | `@dimen/mtrl_calendar_month_horizontal_padding` |
| 9 | `com.google.android.material.datepicker.MaterialCalendarGridView` | `android:verticalSpacing` | `@dimen/mtrl_calendar_month_vertical_padding` |
| 10 | `com.google.android.material.datepicker.MaterialCalendarGridView` | `android:defaultFocusHighlightEnabled` | `false` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/mtrl_calendar_month_horizontal_padding` | `2.000000dip` / `4.000000dip` (h360dp-land) / `0.000000dip` (h480dp-land) / `4.000000dip` (w360dp-port) / `0.000000dip` (w400dp-port) |
| `@dimen/mtrl_calendar_month_vertical_padding` | `0.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/month_grid
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/mtrl_calendar_month_labeled.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<com.google.android.material.datepicker.MaterialCalendarGridView xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00000011" android:id="@id/month_grid" android:addStatesFromChildren="false" android:descendantFocusability="1" android:layout_width="match_parent" android:layout_height="match_parent" android:listSelector="@0x0106000D" android:horizontalSpacing="@dimen/mtrl_calendar_month_horizontal_padding" android:verticalSpacing="@dimen/mtrl_calendar_month_vertical_padding" android:defaultFocusHighlightEnabled="false"/>
```
