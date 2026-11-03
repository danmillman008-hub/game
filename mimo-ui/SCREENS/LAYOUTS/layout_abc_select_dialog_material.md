# پروندهٔ لایه — `res/layout/abc_select_dialog_material.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/abc_select_dialog_material.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/abc_select_dialog_material.xml`](../../SOURCE/res/layout/abc_select_dialog_material.xml) |
| SHA-256 دیکد | `fff6b05350fdf3642f8b8f9e3a69912c198fafe1605718227ff47044b8a552f2` |
| ریشه | `view` |
| تعداد گره | 1 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 1 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ view  #@id/select_dialog_listview
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `view` | `android:layout_gravity` | `0x00800003` |
| 2 | `view` | `android:id` | `@id/select_dialog_listview` |
| 3 | `view` | `android:scrollbars` | `0x00000200` |
| 4 | `view` | `android:fadingEdge` | `0x00000000` |
| 5 | `view` | `android:clipToPadding` | `false` |
| 6 | `view` | `android:layout_width` | `match_parent` |
| 7 | `view` | `android:layout_height` | `match_parent` |
| 8 | `view` | `android:cacheColorHint` | `@null` |
| 9 | `view` | `android:divider` | `?attr/listDividerAlertDialog` |
| 10 | `view` | `android:overScrollMode` | `1` |
| 11 | `view` | `android:textAlignment` | `viewStart` |
| 12 | `view` | `app:paddingBottomNoButtons` | `@dimen/abc_dialog_list_padding_bottom_no_buttons` |
| 13 | `view` | `app:paddingTopNoTitle` | `@dimen/abc_dialog_list_padding_top_no_title` |
| 14 | `view` | `class` | `androidx.appcompat.app.AlertController$RecycleListView` |
| 15 | `view` | `style` | `@style/Widget.AppCompat.ListView` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/abc_dialog_list_padding_bottom_no_buttons` | `8.000000dip` |
| `@dimen/abc_dialog_list_padding_top_no_title` | `8.000000dip` |
| `@style/Widget.AppCompat.ListView` | `[]` |

## ۴. شناسه‌های `@id`

```text
@id/select_dialog_listview
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
<view xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00800003" android:id="@id/select_dialog_listview" android:scrollbars="0x00000200" android:fadingEdge="0x00000000" android:clipToPadding="false" android:layout_width="match_parent" android:layout_height="match_parent" android:cacheColorHint="@null" android:divider="?attr/listDividerAlertDialog" android:overScrollMode="1" android:textAlignment="viewStart" app:paddingBottomNoButtons="@dimen/abc_dialog_list_padding_bottom_no_buttons" app:paddingTopNoTitle="@dimen/abc_dialog_list_padding_top_no_title" class="androidx.appcompat.app.AlertController$RecycleListView" style="@style/Widget.AppCompat.ListView"/>
```
