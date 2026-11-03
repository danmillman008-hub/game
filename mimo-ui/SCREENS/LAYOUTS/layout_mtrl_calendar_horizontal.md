# پروندهٔ لایه — `res/layout/mtrl_calendar_horizontal.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mtrl_calendar_horizontal.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mtrl_calendar_horizontal.xml`](../../SOURCE/res/layout/mtrl_calendar_horizontal.xml) |
| SHA-256 دیکد | `aedb95a52be33a48bc68b5f6691c605d7c02ee9842a50aa09f5c0fa45ede3fb2` |
| ریشه | `LinearLayout` |
| تعداد گره | 7 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 3 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ include
   └─ FrameLayout  #@id/mtrl_calendar_selection_frame
      ├─ androidx.recyclerview.widget.RecyclerView  #@id/mtrl_calendar_year_selector_frame
      └─ LinearLayout  #@id/mtrl_calendar_day_selector_frame
         ├─ include
         └─ include
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 3 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 4 | `include` | `layout` | `@layout/mtrl_calendar_month_navigation` |
| 5 | `FrameLayout` | `android:id` | `@id/mtrl_calendar_selection_frame` |
| 6 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 7 | `FrameLayout` | `android:layout_height` | `match_parent` |
| 8 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_gravity` | `0x00000001` |
| 9 | `androidx.recyclerview.widget.RecyclerView` | `android:id` | `@id/mtrl_calendar_year_selector_frame` |
| 10 | `androidx.recyclerview.widget.RecyclerView` | `android:scrollbars` | `0x00000000` |
| 11 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_width` | `wrap_content` |
| 12 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_height` | `match_parent` |
| 13 | `LinearLayout` | `android:orientation` | `vertical` |
| 14 | `LinearLayout` | `android:id` | `@id/mtrl_calendar_day_selector_frame` |
| 15 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 16 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 17 | `include` | `layout` | `@layout/mtrl_calendar_days_of_week` |
| 18 | `include` | `layout` | `@layout/mtrl_calendar_months` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/mtrl_calendar_day_selector_frame
@id/mtrl_calendar_selection_frame
@id/mtrl_calendar_year_selector_frame
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/mtrl_calendar_days_of_week
@layout/mtrl_calendar_month_navigation
@layout/mtrl_calendar_months
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:layout_width="match_parent" android:layout_height="match_parent">
  <include layout="@layout/mtrl_calendar_month_navigation"/>
  <FrameLayout android:id="@id/mtrl_calendar_selection_frame" android:layout_width="match_parent" android:layout_height="match_parent">
    <androidx.recyclerview.widget.RecyclerView android:layout_gravity="0x00000001" android:id="@id/mtrl_calendar_year_selector_frame" android:scrollbars="0x00000000" android:layout_width="wrap_content" android:layout_height="match_parent"/>
    <LinearLayout android:orientation="vertical" android:id="@id/mtrl_calendar_day_selector_frame" android:layout_width="wrap_content" android:layout_height="match_parent">
      <include layout="@layout/mtrl_calendar_days_of_week"/>
      <include layout="@layout/mtrl_calendar_months"/>
    </LinearLayout>
  </FrameLayout>
</LinearLayout>
```
