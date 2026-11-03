# پروندهٔ لایه — `res/layout/profile_certificate_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/profile_certificate_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/profile_certificate_view.xml`](../../SOURCE/res/layout/profile_certificate_view.xml) |
| SHA-256 دیکد | `9048ffdc1f0c5a4f36b7fb44015fe9b813837fcf21252128c7b3705061d2c008` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 7 |
| تعداد شناسه | 6 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 18 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ ImageView  #@id/iv_certificate_icon
   ├─ TextView  #@id/tv_certificate_title
   ├─ com.google.android.material.progressindicator.CircularProgressIndicator  #@id/certificate_progress
   ├─ TextView  #@id/tv_certificate_progress_text
   ├─ ImageView  #@id/iv_certificate_download
   └─ View  #@id/v_separator
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:clickable` | `true` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `80.000000dip` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:foreground` | `?attr/selectableItemBackground` |
| 5 | `ImageView` | `android:id` | `@id/iv_certificate_icon` |
| 6 | `ImageView` | `android:layout_width` | `42.000000dip` |
| 7 | `ImageView` | `android:layout_height` | `56.000000dip` |
| 8 | `ImageView` | `android:scaleType` | `centerInside` |
| 9 | `ImageView` | `android:layout_marginStart` | `@dimen/spacing_m` |
| 10 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 11 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 12 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 13 | `TextView` | `android:textColor` | `@color/text_primary` |
| 14 | `TextView` | `android:id` | `@id/tv_certificate_title` |
| 15 | `TextView` | `android:layout_width` | `0.000000dip` |
| 16 | `TextView` | `android:layout_height` | `wrap_content` |
| 17 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_m` |
| 18 | `TextView` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 19 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 20 | `TextView` | `app:layout_constraintEnd_toStartOf` | `@id/certificate_progress` |
| 21 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_certificate_icon` |
| 22 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 23 | `TextView` | `style` | `@style/TextH4` |
| 24 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `android:id` | `@id/certificate_progress` |
| 25 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `android:layout_width` | `wrap_content` |
| 26 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `android:layout_height` | `wrap_content` |
| 27 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `android:layout_marginEnd` | `@dimen/spacing_m` |
| 28 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:indicatorColor` | `@color/progress_primary` |
| 29 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:indicatorInset` | `0.000000dip` |
| 30 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:indicatorSize` | `56.000000dip` |
| 31 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 32 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:layout_constraintEnd_toEndOf` | `0` |
| 33 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:layout_constraintTop_toTopOf` | `0` |
| 34 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:trackColor` | `@color/progress_empty` |
| 35 | `com.google.android.material.progressindicator.CircularProgressIndicator` | `app:trackCornerRadius` | `3.000000dip` |
| 36 | `TextView` | `android:textColor` | `@color/text_primary` |
| 37 | `TextView` | `android:id` | `@id/tv_certificate_progress_text` |
| 38 | `TextView` | `android:layout_width` | `wrap_content` |
| 39 | `TextView` | `android:layout_height` | `wrap_content` |
| 40 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `@id/certificate_progress` |
| 41 | `TextView` | `app:layout_constraintEnd_toEndOf` | `@id/certificate_progress` |
| 42 | `TextView` | `app:layout_constraintStart_toStartOf` | `@id/certificate_progress` |
| 43 | `TextView` | `app:layout_constraintTop_toTopOf` | `@id/certificate_progress` |
| 44 | `TextView` | `style` | `@style/TextTitle2` |
| 45 | `ImageView` | `android:id` | `@id/iv_certificate_download` |
| 46 | `ImageView` | `android:visibility` | `invisible` |
| 47 | `ImageView` | `android:layout_width` | `@dimen/icon_size_large_expandable` |
| 48 | `ImageView` | `android:layout_height` | `@dimen/icon_size_large_expandable` |
| 49 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `@id/certificate_progress` |
| 50 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `@id/certificate_progress` |
| 51 | `ImageView` | `app:layout_constraintStart_toStartOf` | `@id/certificate_progress` |
| 52 | `ImageView` | `app:layout_constraintTop_toTopOf` | `@id/certificate_progress` |
| 53 | `ImageView` | `app:srcCompat` | `@drawable/ic_download` |
| 54 | `ImageView` | `app:tint` | `@color/icon_primary` |
| 55 | `View` | `android:id` | `@id/v_separator` |
| 56 | `View` | `android:background` | `@color/line_primary` |
| 57 | `View` | `android:layout_width` | `0.000000dip` |
| 58 | `View` | `android:layout_height` | `1.000000dip` |
| 59 | `View` | `android:layout_marginHorizontal` | `@dimen/spacing_m_expandable` |
| 60 | `View` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 61 | `View` | `app:layout_constraintEnd_toEndOf` | `0` |
| 62 | `View` | `app:layout_constraintStart_toStartOf` | `0` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/icon_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/line_primary` | `#FFEDEEF6` / `#FF3F4273` (night) |
| `@color/progress_empty` | `#FFE4E6F1` / `#FF4A4D85` (night) |
| `@color/progress_primary` | `#FF7E4BDE` / `#FFA175EA` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/icon_size_large_expandable` | `24.000000dip` / `32.000000dip` (sw600dp) |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@style/TextH4` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '11.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextTitle2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/certificate_progress
@id/iv_certificate_download
@id/iv_certificate_icon
@id/tv_certificate_progress_text
@id/tv_certificate_title
@id/v_separator
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.certificates.CertificateActivity
com.getmimo.ui.profile.main.ProfileFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:clickable="true" android:layout_width="match_parent" android:layout_height="80.000000dip" android:foreground="?attr/selectableItemBackground">
  <ImageView android:id="@id/iv_certificate_icon" android:layout_width="42.000000dip" android:layout_height="56.000000dip" android:scaleType="centerInside" android:layout_marginStart="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  <TextView android:textColor="@color/text_primary" android:id="@id/tv_certificate_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginEnd="@dimen/spacing_m" android:layout_marginHorizontal="@dimen/spacing_m" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toStartOf="@id/certificate_progress" app:layout_constraintStart_toEndOf="@id/iv_certificate_icon" app:layout_constraintTop_toTopOf="0" style="@style/TextH4"/>
  <com.google.android.material.progressindicator.CircularProgressIndicator android:id="@id/certificate_progress" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginEnd="@dimen/spacing_m" app:indicatorColor="@color/progress_primary" app:indicatorInset="0.000000dip" app:indicatorSize="56.000000dip" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0" app:trackColor="@color/progress_empty" app:trackCornerRadius="3.000000dip"/>
  <TextView android:textColor="@color/text_primary" android:id="@id/tv_certificate_progress_text" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintBottom_toBottomOf="@id/certificate_progress" app:layout_constraintEnd_toEndOf="@id/certificate_progress" app:layout_constraintStart_toStartOf="@id/certificate_progress" app:layout_constraintTop_toTopOf="@id/certificate_progress" style="@style/TextTitle2"/>
  <ImageView android:id="@id/iv_certificate_download" android:visibility="invisible" android:layout_width="@dimen/icon_size_large_expandable" android:layout_height="@dimen/icon_size_large_expandable" app:layout_constraintBottom_toBottomOf="@id/certificate_progress" app:layout_constraintEnd_toEndOf="@id/certificate_progress" app:layout_constraintStart_toStartOf="@id/certificate_progress" app:layout_constraintTop_toTopOf="@id/certificate_progress" app:srcCompat="@drawable/ic_download" app:tint="@color/icon_primary"/>
  <View android:id="@id/v_separator" android:background="@color/line_primary" android:layout_width="0.000000dip" android:layout_height="1.000000dip" android:layout_marginHorizontal="@dimen/spacing_m_expandable" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
