# پروندهٔ لایه — `res/layout/codeheader_browser_tabview.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/codeheader_browser_tabview.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/codeheader_browser_tabview.xml`](../../SOURCE/res/layout/codeheader_browser_tabview.xml) |
| SHA-256 دیکد | `ee580069f6060fc8c76937c2d518e6029333daf8a46717ff43f61b2c3c4b94bf` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_codeeditor_tab_title
   └─ com.google.android.material.progressindicator.LinearProgressIndicator  #@id/lpi_browser_loading
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `wrap_content` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `48.000000dip` |
| 3 | `TextView` | `android:textAppearance` | `@style/TextCodeEditorTitleWithBrowserTab` |
| 4 | `TextView` | `android:id` | `@id/tv_codeeditor_tab_title` |
| 5 | `TextView` | `android:layout_width` | `wrap_content` |
| 6 | `TextView` | `android:layout_height` | `wrap_content` |
| 7 | `TextView` | `android:layout_marginHorizontal` | `@dimen/lesson_tableview_cell_padding_start` |
| 8 | `TextView` | `android:layout_marginVertical` | `@dimen/lesson_tablayout_padding_vertical` |
| 9 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 10 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 11 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 12 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 13 | `com.google.android.material.progressindicator.LinearProgressIndicator` | `android:id` | `@id/lpi_browser_loading` |
| 14 | `com.google.android.material.progressindicator.LinearProgressIndicator` | `android:visibility` | `gone` |
| 15 | `com.google.android.material.progressindicator.LinearProgressIndicator` | `android:layout_width` | `0.000000dip` |
| 16 | `com.google.android.material.progressindicator.LinearProgressIndicator` | `android:layout_height` | `2.000000dip` |
| 17 | `com.google.android.material.progressindicator.LinearProgressIndicator` | `android:indeterminate` | `true` |
| 18 | `com.google.android.material.progressindicator.LinearProgressIndicator` | `app:indicatorColor` | `@color/primary_on_reversed` |
| 19 | `com.google.android.material.progressindicator.LinearProgressIndicator` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 20 | `com.google.android.material.progressindicator.LinearProgressIndicator` | `app:layout_constraintEnd_toEndOf` | `0` |
| 21 | `com.google.android.material.progressindicator.LinearProgressIndicator` | `app:layout_constraintStart_toStartOf` | `0` |
| 22 | `com.google.android.material.progressindicator.LinearProgressIndicator` | `app:minHideDelay` | `500` |
| 23 | `com.google.android.material.progressindicator.LinearProgressIndicator` | `app:trackColor` | `@null` |
| 24 | `com.google.android.material.progressindicator.LinearProgressIndicator` | `app:trackCornerRadius` | `100.000000dip` |
| 25 | `com.google.android.material.progressindicator.LinearProgressIndicator` | `app:trackThickness` | `2.000000dip` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/primary_on_reversed` | `#FFB89CED` / `#FF7E4BDE` (night) |
| `@dimen/lesson_tablayout_padding_vertical` | `10.000000dip` / `12.000000dip` (sw600dp) |
| `@dimen/lesson_tableview_cell_padding_start` | `@dimen/spacing_s_expandable` |
| `@style/TextCodeEditorTitleWithBrowserTab` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/codeeditor_browser_tab_color', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/lpi_browser_loading
@id/tv_codeeditor_tab_title
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="wrap_content" android:layout_height="48.000000dip">
  <TextView android:textAppearance="@style/TextCodeEditorTitleWithBrowserTab" android:id="@id/tv_codeeditor_tab_title" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginHorizontal="@dimen/lesson_tableview_cell_padding_start" android:layout_marginVertical="@dimen/lesson_tablayout_padding_vertical" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  <com.google.android.material.progressindicator.LinearProgressIndicator android:id="@id/lpi_browser_loading" android:visibility="gone" android:layout_width="0.000000dip" android:layout_height="2.000000dip" android:indeterminate="true" app:indicatorColor="@color/primary_on_reversed" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:minHideDelay="500" app:trackColor="@null" app:trackCornerRadius="100.000000dip" app:trackThickness="2.000000dip"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
