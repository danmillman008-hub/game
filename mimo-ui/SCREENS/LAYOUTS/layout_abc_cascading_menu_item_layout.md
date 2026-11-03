# پروندهٔ لایه — `res/layout/abc_cascading_menu_item_layout.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/abc_cascading_menu_item_layout.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/abc_cascading_menu_item_layout.xml`](../../SOURCE/res/layout/abc_cascading_menu_item_layout.xml) |
| SHA-256 دیکد | `28c6f74650566fd7e88b89559a16a9c2717c2aa52802f2b3fc4d124edc5fcef7` |
| ریشه | `androidx.appcompat.view.menu.ListMenuItemView` |
| تعداد گره | 7 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 13 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.appcompat.view.menu.ListMenuItemView
   ├─ ImageView  #@id/group_divider
   └─ LinearLayout  #@id/content
      ├─ TextView  #@id/title
      ├─ Space
      ├─ TextView  #@id/shortcut
      └─ ImageView  #@id/submenuarrow
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.appcompat.view.menu.ListMenuItemView` | `android:orientation` | `vertical` |
| 2 | `androidx.appcompat.view.menu.ListMenuItemView` | `android:layout_width` | `match_parent` |
| 3 | `androidx.appcompat.view.menu.ListMenuItemView` | `android:layout_height` | `wrap_content` |
| 4 | `androidx.appcompat.view.menu.ListMenuItemView` | `android:minWidth` | `196.000000dip` |
| 5 | `ImageView` | `android:id` | `@id/group_divider` |
| 6 | `ImageView` | `android:background` | `@drawable/abc_list_divider_material` |
| 7 | `ImageView` | `android:layout_width` | `match_parent` |
| 8 | `ImageView` | `android:layout_height` | `1.000000dip` |
| 9 | `ImageView` | `android:layout_marginTop` | `4.000000dip` |
| 10 | `ImageView` | `android:layout_marginBottom` | `4.000000dip` |
| 11 | `LinearLayout` | `android:id` | `@id/content` |
| 12 | `LinearLayout` | `android:duplicateParentState` | `true` |
| 13 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 14 | `LinearLayout` | `android:layout_height` | `?attr/dropdownListPreferredItemHeight` |
| 15 | `LinearLayout` | `style` | `@style/RtlOverlay.Widget.AppCompat.PopupMenuItem` |
| 16 | `TextView` | `android:textAppearance` | `?attr/textAppearanceLargePopupMenu` |
| 17 | `TextView` | `android:layout_gravity` | `0x00000010` |
| 18 | `TextView` | `android:id` | `@id/title` |
| 19 | `TextView` | `android:duplicateParentState` | `true` |
| 20 | `TextView` | `android:layout_width` | `wrap_content` |
| 21 | `TextView` | `android:layout_height` | `wrap_content` |
| 22 | `TextView` | `android:singleLine` | `true` |
| 23 | `TextView` | `style` | `@style/RtlOverlay.Widget.AppCompat.PopupMenuItem.Title` |
| 24 | `Space` | `android:layout_width` | `0.000000dip` |
| 25 | `Space` | `android:layout_height` | `1.000000dip` |
| 26 | `Space` | `android:layout_weight` | `1.000000` |
| 27 | `TextView` | `android:textAppearance` | `?attr/textAppearanceSmallPopupMenu` |
| 28 | `TextView` | `android:layout_gravity` | `0x00000010` |
| 29 | `TextView` | `android:id` | `@id/shortcut` |
| 30 | `TextView` | `android:duplicateParentState` | `true` |
| 31 | `TextView` | `android:layout_width` | `wrap_content` |
| 32 | `TextView` | `android:layout_height` | `wrap_content` |
| 33 | `TextView` | `android:singleLine` | `true` |
| 34 | `TextView` | `style` | `@style/RtlOverlay.Widget.AppCompat.PopupMenuItem.Shortcut` |
| 35 | `ImageView` | `android:layout_gravity` | `0x00000011` |
| 36 | `ImageView` | `android:id` | `@id/submenuarrow` |
| 37 | `ImageView` | `android:visibility` | `gone` |
| 38 | `ImageView` | `android:layout_width` | `wrap_content` |
| 39 | `ImageView` | `android:layout_height` | `wrap_content` |
| 40 | `ImageView` | `android:scaleType` | `center` |
| 41 | `ImageView` | `style` | `@style/RtlOverlay.Widget.AppCompat.PopupMenuItem.SubmenuArrow` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/RtlOverlay.Widget.AppCompat.PopupMenuItem` | `[{'attr': 'android:paddingEnd', 'attr_id': '0x010103B4', 'value': '16.000000dip', 'value_type': 'dimension'}]` |
| `@style/RtlOverlay.Widget.AppCompat.PopupMenuItem.Shortcut` | `[{'attr': 'android:textAlignment', 'attr_id': '0x010103B1', 'value': '6', 'value_type': 'int_dec'}, {'attr': 'android:layout_marginStart', 'attr_id': '0x010103B5', 'value': '16.000000dip', 'value_type': 'dimension'}]` |
| `@style/RtlOverlay.Widget.AppCompat.PopupMenuItem.SubmenuArrow` | `[{'attr': 'android:layout_marginStart', 'attr_id': '0x010103B5', 'value': '8.000000dip', 'value_type': 'dimension'}]` |
| `@style/RtlOverlay.Widget.AppCompat.PopupMenuItem.Title` | `[{'attr': 'android:textAlignment', 'attr_id': '0x010103B1', 'value': '5', 'value_type': 'int_dec'}, {'attr': 'android:layout_marginStart', 'attr_id': '0x010103B5', 'value': '16.000000dip', 'value_type': 'dimension'}]` |

## ۴. شناسه‌های `@id`

```text
@id/content
@id/group_divider
@id/shortcut
@id/submenuarrow
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
<androidx.appcompat.view.menu.ListMenuItemView xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:layout_width="match_parent" android:layout_height="wrap_content" android:minWidth="196.000000dip">
  <ImageView android:id="@id/group_divider" android:background="@drawable/abc_list_divider_material" android:layout_width="match_parent" android:layout_height="1.000000dip" android:layout_marginTop="4.000000dip" android:layout_marginBottom="4.000000dip"/>
  <LinearLayout android:id="@id/content" android:duplicateParentState="true" android:layout_width="match_parent" android:layout_height="?attr/dropdownListPreferredItemHeight" style="@style/RtlOverlay.Widget.AppCompat.PopupMenuItem">
    <TextView android:textAppearance="?attr/textAppearanceLargePopupMenu" android:layout_gravity="0x00000010" android:id="@id/title" android:duplicateParentState="true" android:layout_width="wrap_content" android:layout_height="wrap_content" android:singleLine="true" style="@style/RtlOverlay.Widget.AppCompat.PopupMenuItem.Title"/>
    <Space android:layout_width="0.000000dip" android:layout_height="1.000000dip" android:layout_weight="1.000000"/>
    <TextView android:textAppearance="?attr/textAppearanceSmallPopupMenu" android:layout_gravity="0x00000010" android:id="@id/shortcut" android:duplicateParentState="true" android:layout_width="wrap_content" android:layout_height="wrap_content" android:singleLine="true" style="@style/RtlOverlay.Widget.AppCompat.PopupMenuItem.Shortcut"/>
    <ImageView android:layout_gravity="0x00000011" android:id="@id/submenuarrow" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:scaleType="center" style="@style/RtlOverlay.Widget.AppCompat.PopupMenuItem.SubmenuArrow"/>
  </LinearLayout>
</androidx.appcompat.view.menu.ListMenuItemView>
```
