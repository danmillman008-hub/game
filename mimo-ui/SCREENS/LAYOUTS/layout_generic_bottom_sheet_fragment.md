# پروندهٔ لایه — `res/layout/generic_bottom_sheet_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/generic_bottom_sheet_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/generic_bottom_sheet_fragment.xml`](../../SOURCE/res/layout/generic_bottom_sheet_fragment.xml) |
| SHA-256 دیکد | `8545b0674008cb956dd709512a8255dbae718d5e999751b4cfa6a81fdd9bdd43` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 2 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 1 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 4 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/bottom_sheet_content_root
   └─ androidx.compose.ui.platform.ComposeView  #@id/cv_bottom_sheet_header
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_gravity` | `0x00000001` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/bottom_sheet_content_root` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@drawable/drawer_bottom_sheet_background` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 6 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:maxWidth` | `@dimen/bottom_sheet_content_max_width` |
| 7 | `androidx.compose.ui.platform.ComposeView` | `android:id` | `@id/cv_bottom_sheet_header` |
| 8 | `androidx.compose.ui.platform.ComposeView` | `android:layout_width` | `0.000000dip` |
| 9 | `androidx.compose.ui.platform.ComposeView` | `android:layout_height` | `wrap_content` |
| 10 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 11 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintStart_toStartOf` | `0` |
| 12 | `androidx.compose.ui.platform.ComposeView` | `app:layout_constraintTop_toTopOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/bottom_sheet_content_max_width` | `496.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/bottom_sheet_content_root
@id/cv_bottom_sheet_header
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_gravity="0x00000001" android:id="@id/bottom_sheet_content_root" android:background="@drawable/drawer_bottom_sheet_background" android:layout_width="match_parent" android:layout_height="match_parent" android:maxWidth="@dimen/bottom_sheet_content_max_width">
  <androidx.compose.ui.platform.ComposeView android:id="@id/cv_bottom_sheet_header" android:layout_width="0.000000dip" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
