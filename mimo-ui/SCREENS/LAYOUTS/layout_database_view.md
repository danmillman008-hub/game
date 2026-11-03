# پروندهٔ لایه — `res/layout/database_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/database_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/database_view.xml`](../../SOURCE/res/layout/database_view.xml) |
| SHA-256 دیکد | `571a4cea94599159a03308350b349601437fa251eaf7eb2254c6ad2ae16ad951` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 2 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ com.google.android.material.tabs.TabLayout  #@id/tl_database_header
   ├─ View  #@id/code_header_separator
   └─ com.getmimo.ui.common.viewpager2.NestedScrollableHost
      └─ com.getmimo.ui.common.viewpager2.TwoWayNestedScrollView  #@id/nsv_table_content
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 3 | `com.google.android.material.tabs.TabLayout` | `android:gravity` | `0x00800013` |
| 4 | `com.google.android.material.tabs.TabLayout` | `android:id` | `@id/tl_database_header` |
| 5 | `com.google.android.material.tabs.TabLayout` | `android:background` | `@color/background_secondary` |
| 6 | `com.google.android.material.tabs.TabLayout` | `android:paddingTop` | `0.000000dip` |
| 7 | `com.google.android.material.tabs.TabLayout` | `android:paddingBottom` | `0.000000dip` |
| 8 | `com.google.android.material.tabs.TabLayout` | `android:focusable` | `true` |
| 9 | `com.google.android.material.tabs.TabLayout` | `android:focusableInTouchMode` | `true` |
| 10 | `com.google.android.material.tabs.TabLayout` | `android:layout_width` | `0.000000dip` |
| 11 | `com.google.android.material.tabs.TabLayout` | `android:layout_height` | `48.000000dip` |
| 12 | `com.google.android.material.tabs.TabLayout` | `android:paddingStart` | `@dimen/spacing_s` |
| 13 | `com.google.android.material.tabs.TabLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 14 | `com.google.android.material.tabs.TabLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 15 | `com.google.android.material.tabs.TabLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 16 | `com.google.android.material.tabs.TabLayout` | `style` | `@style/CodeEditorTabLayout` |
| 17 | `View` | `android:id` | `@id/code_header_separator` |
| 18 | `View` | `android:background` | `@color/line_primary` |
| 19 | `View` | `android:layout_width` | `match_parent` |
| 20 | `View` | `android:layout_height` | `1.000000dip` |
| 21 | `View` | `app:layout_constraintBottom_toBottomOf` | `@id/tl_database_header` |
| 22 | `com.getmimo.ui.common.viewpager2.NestedScrollableHost` | `android:layout_width` | `0.000000dip` |
| 23 | `com.getmimo.ui.common.viewpager2.NestedScrollableHost` | `android:layout_height` | `wrap_content` |
| 24 | `com.getmimo.ui.common.viewpager2.NestedScrollableHost` | `app:layout_constraintEnd_toEndOf` | `0` |
| 25 | `com.getmimo.ui.common.viewpager2.NestedScrollableHost` | `app:layout_constraintStart_toStartOf` | `0` |
| 26 | `com.getmimo.ui.common.viewpager2.NestedScrollableHost` | `app:layout_constraintTop_toBottomOf` | `@id/tl_database_header` |
| 27 | `com.getmimo.ui.common.viewpager2.TwoWayNestedScrollView` | `android:scrollbarStyle` | `0x00000000` |
| 28 | `com.getmimo.ui.common.viewpager2.TwoWayNestedScrollView` | `android:id` | `@id/nsv_table_content` |
| 29 | `com.getmimo.ui.common.viewpager2.TwoWayNestedScrollView` | `android:scrollbars` | `0x00000300` |
| 30 | `com.getmimo.ui.common.viewpager2.TwoWayNestedScrollView` | `android:layout_width` | `match_parent` |
| 31 | `com.getmimo.ui.common.viewpager2.TwoWayNestedScrollView` | `android:layout_height` | `match_parent` |
| 32 | `com.getmimo.ui.common.viewpager2.TwoWayNestedScrollView` | `android:scrollbarFadeDuration` | `200` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |
| `@color/line_primary` | `#FFEDEEF6` / `#FF3F4273` (night) |
| `@dimen/spacing_s` | `12.000000dip` |
| `@style/CodeEditorTabLayout` | `[{'attr': 'attr.tabBackground', 'attr_id': '0x7F04059F', 'value': '@color/transparent', 'value_type': 'reference'}, {'attr': 'attr.tabGravity', 'attr_id': '0x7F0405A1', 'value': '0', 'value_type': 'int_dec'}, {'attr': 'attr.tabIndicator', 'attr_id': '0x7F0405A4', 'value': '@drawable/tab_indicator', 'value_type': 'reference'}, {'attr': 'attr.tabIndicatorHeight', 'attr_id': '0x7F0405AA', 'value': '2.000000dip', 'value_type': 'dimension'}, {'attr': 'attr.tabMinWidth', 'attr_id': '0x7F0405AD', 'value': '0.000000dip', 'value_type': 'dimension'}, {'attr': 'attr.tabMode', 'attr_id': '0x7F0405AE', 'value': '0', 'value_type': 'int_dec'}, {'attr': 'attr.tabPadding', 'attr_id': '0x7F0405AF', 'value': '0.000000dip', 'value_type': 'dimension'}, {'attr': 'attr.tabSelectedTextColor', 'attr_id': '0x7F0405B7', 'value': '@color/text_primary', 'value_type': 'reference'}, {'attr': 'attr.tabTextAppearance', 'attr_id': '0x7F0405B9', 'value': '@style/TextCodeEditorTitleWithMultipleTabs', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/code_header_separator
@id/nsv_table_content
@id/tl_database_header
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="match_parent" android:layout_height="match_parent">
  <com.google.android.material.tabs.TabLayout android:gravity="0x00800013" android:id="@id/tl_database_header" android:background="@color/background_secondary" android:paddingTop="0.000000dip" android:paddingBottom="0.000000dip" android:focusable="true" android:focusableInTouchMode="true" android:layout_width="0.000000dip" android:layout_height="48.000000dip" android:paddingStart="@dimen/spacing_s" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/CodeEditorTabLayout"/>
  <View android:id="@id/code_header_separator" android:background="@color/line_primary" android:layout_width="match_parent" android:layout_height="1.000000dip" app:layout_constraintBottom_toBottomOf="@id/tl_database_header"/>
  <com.getmimo.ui.common.viewpager2.NestedScrollableHost android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tl_database_header">
    <com.getmimo.ui.common.viewpager2.TwoWayNestedScrollView android:scrollbarStyle="0x00000000" android:id="@id/nsv_table_content" android:scrollbars="0x00000300" android:layout_width="match_parent" android:layout_height="match_parent" android:scrollbarFadeDuration="200"/>
  </com.getmimo.ui.common.viewpager2.NestedScrollableHost>
</androidx.constraintlayout.widget.ConstraintLayout>
```
