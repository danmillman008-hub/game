# پروندهٔ لایه — `res/layout/abc_list_menu_item_layout.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/abc_list_menu_item_layout.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/abc_list_menu_item_layout.xml`](../../SOURCE/res/layout/abc_list_menu_item_layout.xml) |
| SHA-256 دیکد | `93bde258558d96d049ae187ca41b0b414435bc1ffa4df642214c0bcbc07bc273` |
| ریشه | `androidx.appcompat.view.menu.ListMenuItemView` |
| تعداد گره | 4 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.appcompat.view.menu.ListMenuItemView
   └─ RelativeLayout
      ├─ TextView  #@id/title
      └─ TextView  #@id/shortcut
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.appcompat.view.menu.ListMenuItemView` | `android:layout_width` | `match_parent` |
| 2 | `androidx.appcompat.view.menu.ListMenuItemView` | `android:layout_height` | `?attr/listPreferredItemHeightSmall` |
| 3 | `RelativeLayout` | `android:layout_gravity` | `0x00000010` |
| 4 | `RelativeLayout` | `android:duplicateParentState` | `true` |
| 5 | `RelativeLayout` | `android:layout_width` | `0.000000dip` |
| 6 | `RelativeLayout` | `android:layout_height` | `wrap_content` |
| 7 | `RelativeLayout` | `android:layout_marginLeft` | `?attr/listPreferredItemPaddingLeft` |
| 8 | `RelativeLayout` | `android:layout_marginRight` | `?attr/listPreferredItemPaddingRight` |
| 9 | `RelativeLayout` | `android:layout_weight` | `1.000000` |
| 10 | `TextView` | `android:textAppearance` | `?attr/textAppearanceListItemSmall` |
| 11 | `TextView` | `android:ellipsize` | `marquee` |
| 12 | `TextView` | `android:id` | `@id/title` |
| 13 | `TextView` | `android:fadingEdge` | `0x00001000` |
| 14 | `TextView` | `android:duplicateParentState` | `true` |
| 15 | `TextView` | `android:layout_width` | `match_parent` |
| 16 | `TextView` | `android:layout_height` | `wrap_content` |
| 17 | `TextView` | `android:singleLine` | `true` |
| 18 | `TextView` | `android:layout_alignParentLeft` | `true` |
| 19 | `TextView` | `android:layout_alignParentTop` | `true` |
| 20 | `TextView` | `android:textAppearance` | `?0x01010042` |
| 21 | `TextView` | `android:id` | `@id/shortcut` |
| 22 | `TextView` | `android:duplicateParentState` | `true` |
| 23 | `TextView` | `android:layout_width` | `wrap_content` |
| 24 | `TextView` | `android:layout_height` | `wrap_content` |
| 25 | `TextView` | `android:singleLine` | `true` |
| 26 | `TextView` | `android:layout_below` | `@id/title` |
| 27 | `TextView` | `android:layout_alignParentLeft` | `true` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|

## ۴. شناسه‌های `@id`

```text
@id/shortcut
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
<androidx.appcompat.view.menu.ListMenuItemView xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="?attr/listPreferredItemHeightSmall">
  <RelativeLayout android:layout_gravity="0x00000010" android:duplicateParentState="true" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginLeft="?attr/listPreferredItemPaddingLeft" android:layout_marginRight="?attr/listPreferredItemPaddingRight" android:layout_weight="1.000000">
    <TextView android:textAppearance="?attr/textAppearanceListItemSmall" android:ellipsize="marquee" android:id="@id/title" android:fadingEdge="0x00001000" android:duplicateParentState="true" android:layout_width="match_parent" android:layout_height="wrap_content" android:singleLine="true" android:layout_alignParentLeft="true" android:layout_alignParentTop="true"/>
    <TextView android:textAppearance="?0x01010042" android:id="@id/shortcut" android:duplicateParentState="true" android:layout_width="wrap_content" android:layout_height="wrap_content" android:singleLine="true" android:layout_below="@id/title" android:layout_alignParentLeft="true"/>
  </RelativeLayout>
</androidx.appcompat.view.menu.ListMenuItemView>
```
