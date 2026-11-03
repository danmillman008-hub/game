# پروندهٔ لایه — `res/layout/browser_bar.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/browser_bar.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/browser_bar.xml`](../../SOURCE/res/layout/browser_bar.xml) |
| SHA-256 دیکد | `a6053acbd233218201d9091de3c261e81f0eab8740f5792c21430da2edb3991c` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 13 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout  #@id/browser_bar_layout
   ├─ ImageView  #@id/btn_browser_bar_share
   └─ androidx.constraintlayout.widget.ConstraintLayout  #@id/container_browser_bar_url
      ├─ TextView  #@id/tv_browser_bar_url
      └─ ImageView  #@id/btn_browser_bar_refresh
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/browser_bar_layout` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@color/background_secondary` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `48.000000dip` |
| 5 | `ImageView` | `android:id` | `@id/btn_browser_bar_share` |
| 6 | `ImageView` | `android:background` | `?attr/selectableItemBackgroundBorderless` |
| 7 | `ImageView` | `android:layout_width` | `48.000000dip` |
| 8 | `ImageView` | `android:layout_height` | `wrap_content` |
| 9 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 10 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 11 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 12 | `ImageView` | `app:srcCompat` | `@drawable/ic_share` |
| 13 | `ImageView` | `app:tint` | `@color/icon_weak` |
| 14 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:id` | `@id/container_browser_bar_url` |
| 15 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:background` | `@drawable/bg_browser_bar_url` |
| 16 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `0.000000dip` |
| 17 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `0.000000dip` |
| 18 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginTop` | `6.000000dip` |
| 19 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginBottom` | `6.000000dip` |
| 20 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginEnd` | `12.000000dip` |
| 21 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 22 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 23 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintStart_toEndOf` | `@id/btn_browser_bar_share` |
| 24 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 25 | `androidx.constraintlayout.widget.ConstraintLayout` | `app:layout_goneMarginLeft` | `16.000000dip` |
| 26 | `TextView` | `android:textColor` | `@color/text_weak` |
| 27 | `TextView` | `android:ellipsize` | `end` |
| 28 | `TextView` | `android:gravity` | `0x00000010` |
| 29 | `TextView` | `android:id` | `@id/tv_browser_bar_url` |
| 30 | `TextView` | `android:layout_width` | `0.000000dip` |
| 31 | `TextView` | `android:layout_height` | `0.000000dip` |
| 32 | `TextView` | `android:maxLines` | `1` |
| 33 | `TextView` | `android:layout_marginStart` | `12.000000dip` |
| 34 | `TextView` | `android:layout_marginEnd` | `8.000000dip` |
| 35 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 36 | `TextView` | `app:layout_constraintEnd_toStartOf` | `@id/btn_browser_bar_refresh` |
| 37 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 38 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 39 | `TextView` | `style` | `@style/TextP3` |
| 40 | `ImageView` | `android:id` | `@id/btn_browser_bar_refresh` |
| 41 | `ImageView` | `android:background` | `?attr/selectableItemBackgroundBorderless` |
| 42 | `ImageView` | `android:layout_width` | `24.000000dip` |
| 43 | `ImageView` | `android:layout_height` | `0.000000dip` |
| 44 | `ImageView` | `android:layout_marginEnd` | `8.000000dip` |
| 45 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 46 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 47 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 48 | `ImageView` | `app:srcCompat` | `@drawable/ic_refresh_cw` |
| 49 | `ImageView` | `app:tint` | `@color/icon_weak` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/background_secondary` | `#FFFFFFFF` / `#FF333661` (night) |
| `@color/icon_weak` | `#FFA3A5C3` / `#80FFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@style/TextP3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '3.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.199982sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/browser_bar_layout
@id/btn_browser_bar_refresh
@id/btn_browser_bar_share
@id/container_browser_bar_url
@id/tv_browser_bar_url
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:id="@id/browser_bar_layout" android:background="@color/background_secondary" android:layout_width="match_parent" android:layout_height="48.000000dip">
  <ImageView android:id="@id/btn_browser_bar_share" android:background="?attr/selectableItemBackgroundBorderless" android:layout_width="48.000000dip" android:layout_height="wrap_content" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" app:srcCompat="@drawable/ic_share" app:tint="@color/icon_weak"/>
  <androidx.constraintlayout.widget.ConstraintLayout android:id="@id/container_browser_bar_url" android:background="@drawable/bg_browser_bar_url" android:layout_width="0.000000dip" android:layout_height="0.000000dip" android:layout_marginTop="6.000000dip" android:layout_marginBottom="6.000000dip" android:layout_marginEnd="12.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toEndOf="@id/btn_browser_bar_share" app:layout_constraintTop_toTopOf="0" app:layout_goneMarginLeft="16.000000dip">
    <TextView android:textColor="@color/text_weak" android:ellipsize="end" android:gravity="0x00000010" android:id="@id/tv_browser_bar_url" android:layout_width="0.000000dip" android:layout_height="0.000000dip" android:maxLines="1" android:layout_marginStart="12.000000dip" android:layout_marginEnd="8.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toStartOf="@id/btn_browser_bar_refresh" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextP3"/>
    <ImageView android:id="@id/btn_browser_bar_refresh" android:background="?attr/selectableItemBackgroundBorderless" android:layout_width="24.000000dip" android:layout_height="0.000000dip" android:layout_marginEnd="8.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0" app:srcCompat="@drawable/ic_refresh_cw" app:tint="@color/icon_weak"/>
  </androidx.constraintlayout.widget.ConstraintLayout>
</androidx.constraintlayout.widget.ConstraintLayout>
```
