# پروندهٔ لایه — `res/layout/abc_popup_menu_item_layout.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/abc_popup_menu_item_layout.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/abc_popup_menu_item_layout.xml`](../../SOURCE/res/layout/abc_popup_menu_item_layout.xml) |
| SHA-256 دیکد | `62f60ebfb816e79bf4e60329476135025e1a07a5f401d2a6f25c7b841549f5df` |
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
      ├─ RelativeLayout
      │  ├─ TextView  #@id/title
      │  └─ TextView  #@id/shortcut
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
| 16 | `RelativeLayout` | `android:layout_gravity` | `0x00000010` |
| 17 | `RelativeLayout` | `android:duplicateParentState` | `true` |
| 18 | `RelativeLayout` | `android:layout_width` | `0.000000dip` |
| 19 | `RelativeLayout` | `android:layout_height` | `wrap_content` |
| 20 | `RelativeLayout` | `android:layout_weight` | `1.000000` |
| 21 | `RelativeLayout` | `style` | `@style/RtlOverlay.Widget.AppCompat.PopupMenuItem.InternalGroup` |
| 22 | `TextView` | `android:textAppearance` | `?attr/textAppearanceLargePopupMenu` |
| 23 | `TextView` | `android:ellipsize` | `marquee` |
| 24 | `TextView` | `android:id` | `@id/title` |
| 25 | `TextView` | `android:fadingEdge` | `0x00001000` |
| 26 | `TextView` | `android:duplicateParentState` | `true` |
| 27 | `TextView` | `android:layout_width` | `match_parent` |
| 28 | `TextView` | `android:layout_height` | `wrap_content` |
| 29 | `TextView` | `android:singleLine` | `true` |
| 30 | `TextView` | `android:layout_alignParentTop` | `true` |
| 31 | `TextView` | `style` | `@style/RtlOverlay.Widget.AppCompat.PopupMenuItem.Text` |
| 32 | `TextView` | `android:textAppearance` | `?attr/textAppearanceSmallPopupMenu` |
| 33 | `TextView` | `android:id` | `@id/shortcut` |
| 34 | `TextView` | `android:duplicateParentState` | `true` |
| 35 | `TextView` | `android:layout_width` | `wrap_content` |
| 36 | `TextView` | `android:layout_height` | `wrap_content` |
| 37 | `TextView` | `android:singleLine` | `true` |
| 38 | `TextView` | `android:layout_below` | `@id/title` |
| 39 | `TextView` | `style` | `@style/RtlOverlay.Widget.AppCompat.PopupMenuItem.Text` |
| 40 | `ImageView` | `android:layout_gravity` | `0x00000011` |
| 41 | `ImageView` | `android:id` | `@id/submenuarrow` |
| 42 | `ImageView` | `android:visibility` | `gone` |
| 43 | `ImageView` | `android:layout_width` | `wrap_content` |
| 44 | `ImageView` | `android:layout_height` | `wrap_content` |
| 45 | `ImageView` | `android:scaleType` | `center` |
| 46 | `ImageView` | `style` | `@style/RtlOverlay.Widget.AppCompat.PopupMenuItem.SubmenuArrow` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@style/RtlOverlay.Widget.AppCompat.PopupMenuItem` | `[{'attr': 'android:paddingEnd', 'attr_id': '0x010103B4', 'value': '16.000000dip', 'value_type': 'dimension'}]` |
| `@style/RtlOverlay.Widget.AppCompat.PopupMenuItem.InternalGroup` | `[{'attr': 'android:layout_marginStart', 'attr_id': '0x010103B5', 'value': '16.000000dip', 'value_type': 'dimension'}]` |
| `@style/RtlOverlay.Widget.AppCompat.PopupMenuItem.SubmenuArrow` | `[{'attr': 'android:layout_marginStart', 'attr_id': '0x010103B5', 'value': '8.000000dip', 'value_type': 'dimension'}]` |
| `@style/RtlOverlay.Widget.AppCompat.PopupMenuItem.Text` | `[{'attr': 'android:textAlignment', 'attr_id': '0x010103B1', 'value': '5', 'value_type': 'int_dec'}, {'attr': 'android:layout_alignParentStart', 'attr_id': '0x010103BB', 'value': 'true', 'value_type': 'int_boolean'}]` |

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
    <RelativeLayout android:layout_gravity="0x00000010" android:duplicateParentState="true" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_weight="1.000000" style="@style/RtlOverlay.Widget.AppCompat.PopupMenuItem.InternalGroup">
      <TextView android:textAppearance="?attr/textAppearanceLargePopupMenu" android:ellipsize="marquee" android:id="@id/title" android:fadingEdge="0x00001000" android:duplicateParentState="true" android:layout_width="match_parent" android:layout_height="wrap_content" android:singleLine="true" android:layout_alignParentTop="true" style="@style/RtlOverlay.Widget.AppCompat.PopupMenuItem.Text"/>
      <TextView android:textAppearance="?attr/textAppearanceSmallPopupMenu" android:id="@id/shortcut" android:duplicateParentState="true" android:layout_width="wrap_content" android:layout_height="wrap_content" android:singleLine="true" android:layout_below="@id/title" style="@style/RtlOverlay.Widget.AppCompat.PopupMenuItem.Text"/>
    </RelativeLayout>
    <ImageView android:layout_gravity="0x00000011" android:id="@id/submenuarrow" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:scaleType="center" style="@style/RtlOverlay.Widget.AppCompat.PopupMenuItem.SubmenuArrow"/>
  </LinearLayout>
</androidx.appcompat.view.menu.ListMenuItemView>
```
