# پروندهٔ لایه — `res/layout/abc_activity_chooser_view_list_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/abc_activity_chooser_view_list_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/abc_activity_chooser_view_list_item.xml`](../../SOURCE/res/layout/abc_activity_chooser_view_list_item.xml) |
| SHA-256 دیکد | `c8ed67f66e69eb1da33014de03fbaa8162e3ddb106753ce369bbb714cd63de2c` |
| ریشه | `LinearLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/list_item
   └─ LinearLayout
      ├─ ImageView  #@id/icon
      └─ TextView  #@id/title
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:id` | `@id/list_item` |
| 3 | `LinearLayout` | `android:background` | `?attr/selectableItemBackground` |
| 4 | `LinearLayout` | `android:paddingLeft` | `16.000000dip` |
| 5 | `LinearLayout` | `android:paddingRight` | `16.000000dip` |
| 6 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 7 | `LinearLayout` | `android:layout_height` | `?attr/dropdownListPreferredItemHeight` |
| 8 | `LinearLayout` | `android:minWidth` | `196.000000dip` |
| 9 | `LinearLayout` | `android:duplicateParentState` | `true` |
| 10 | `LinearLayout` | `android:layout_width` | `wrap_content` |
| 11 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 12 | `ImageView` | `android:layout_gravity` | `0x00000010` |
| 13 | `ImageView` | `android:id` | `@id/icon` |
| 14 | `ImageView` | `android:duplicateParentState` | `true` |
| 15 | `ImageView` | `android:layout_width` | `32.000000dip` |
| 16 | `ImageView` | `android:layout_height` | `32.000000dip` |
| 17 | `ImageView` | `android:layout_marginRight` | `8.000000dip` |
| 18 | `TextView` | `android:textAppearance` | `?attr/textAppearanceLargePopupMenu` |
| 19 | `TextView` | `android:ellipsize` | `marquee` |
| 20 | `TextView` | `android:layout_gravity` | `0x00000010` |
| 21 | `TextView` | `android:id` | `@id/title` |
| 22 | `TextView` | `android:fadingEdge` | `0x00001000` |
| 23 | `TextView` | `android:duplicateParentState` | `true` |
| 24 | `TextView` | `android:layout_width` | `wrap_content` |
| 25 | `TextView` | `android:layout_height` | `wrap_content` |
| 26 | `TextView` | `android:singleLine` | `true` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/icon
@id/list_item
@id/title
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:id="@id/list_item" android:background="?attr/selectableItemBackground" android:paddingLeft="16.000000dip" android:paddingRight="16.000000dip" android:layout_width="match_parent" android:layout_height="?attr/dropdownListPreferredItemHeight" android:minWidth="196.000000dip">
  <LinearLayout android:duplicateParentState="true" android:layout_width="wrap_content" android:layout_height="match_parent">
    <ImageView android:layout_gravity="0x00000010" android:id="@id/icon" android:duplicateParentState="true" android:layout_width="32.000000dip" android:layout_height="32.000000dip" android:layout_marginRight="8.000000dip"/>
    <TextView android:textAppearance="?attr/textAppearanceLargePopupMenu" android:ellipsize="marquee" android:layout_gravity="0x00000010" android:id="@id/title" android:fadingEdge="0x00001000" android:duplicateParentState="true" android:layout_width="wrap_content" android:layout_height="wrap_content" android:singleLine="true"/>
  </LinearLayout>
</LinearLayout>
```
