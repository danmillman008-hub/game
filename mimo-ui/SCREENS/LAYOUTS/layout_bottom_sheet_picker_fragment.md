# پروندهٔ لایه — `res/layout/bottom_sheet_picker_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/bottom_sheet_picker_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/bottom_sheet_picker_fragment.xml`](../../SOURCE/res/layout/bottom_sheet_picker_fragment.xml) |
| SHA-256 دیکد | `0927a48d257ab9ae53804729fdae0671ff3c68455395fa80d53e642b30699651` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 3 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ View
   └─ androidx.recyclerview.widget.RecyclerView  #@id/rv_bottom_sheet_picker_fragment
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:background` | `@color/background_secondary` |
| 3 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 4 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 5 | `View` | `android:layout_gravity` | `0x00000001` |
| 6 | `View` | `android:background` | `@drawable/bg_handle` |
| 7 | `View` | `android:layout_width` | `32.000000dip` |
| 8 | `View` | `android:layout_height` | `4.000000dip` |
| 9 | `View` | `android:layout_marginTop` | `2.000000dip` |
| 10 | `View` | `android:layout_marginBottom` | `12.000000dip` |
| 11 | `View` | `android:layout_marginStart` | `8.000000dip` |
| 12 | `View` | `android:layout_marginEnd` | `8.000000dip` |
| 13 | `androidx.recyclerview.widget.RecyclerView` | `android:id` | `@id/rv_bottom_sheet_picker_fragment` |
| 14 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_width` | `match_parent` |
| 15 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_height` | `wrap_content` |
| 16 | `androidx.recyclerview.widget.RecyclerView` | `android:layout_marginBottom` | `16.000000dip` |
| 17 | `androidx.recyclerview.widget.RecyclerView` | `android:overScrollMode` | `2` |
| 18 | `androidx.recyclerview.widget.RecyclerView` | `android:nestedScrollingEnabled` | `false` |
| 19 | `androidx.recyclerview.widget.RecyclerView` | `app:layoutManager` | `androidx.recyclerview.widget.LinearLayoutManager` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |

## ۴. شناسه‌های `@id`

```text
@id/rv_bottom_sheet_picker_fragment
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
<LinearLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:background="@color/background_secondary" android:layout_width="match_parent" android:layout_height="wrap_content">
  <View android:layout_gravity="0x00000001" android:background="@drawable/bg_handle" android:layout_width="32.000000dip" android:layout_height="4.000000dip" android:layout_marginTop="2.000000dip" android:layout_marginBottom="12.000000dip" android:layout_marginStart="8.000000dip" android:layout_marginEnd="8.000000dip"/>
  <androidx.recyclerview.widget.RecyclerView android:id="@id/rv_bottom_sheet_picker_fragment" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginBottom="16.000000dip" android:overScrollMode="2" android:nestedScrollingEnabled="false" app:layoutManager="androidx.recyclerview.widget.LinearLayoutManager"/>
</LinearLayout>
```
