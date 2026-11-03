# پروندهٔ لایه — `res/layout/profile_certificates_max_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/profile_certificates_max_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/profile_certificates_max_item.xml`](../../SOURCE/res/layout/profile_certificates_max_item.xml) |
| SHA-256 دیکد | `b470c42c117200ddc0b15f66287c56a31df43683bbddde49ae3404537dc8f12b` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 4 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 10 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_certificate_title
   ├─ ImageView  #@id/iv_certificate_info_icon
   └─ com.getmimo.ui.profile.view.ProfileCertificatesView  #@id/profile_paths_progress_view
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginTop` | `@dimen/spacing_l_expandable` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginBottom` | `@dimen/spacing_m_expandable` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_m_expandable` |
| 6 | `TextView` | `android:textColor` | `@color/text_primary` |
| 7 | `TextView` | `android:id` | `@id/tv_certificate_title` |
| 8 | `TextView` | `android:layout_width` | `wrap_content` |
| 9 | `TextView` | `android:layout_height` | `wrap_content` |
| 10 | `TextView` | `android:text` | `@string/profile_certificates` |
| 11 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 12 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 13 | `TextView` | `style` | `@style/TextH3` |
| 14 | `ImageView` | `android:gravity` | `0x00800005` |
| 15 | `ImageView` | `android:id` | `@id/iv_certificate_info_icon` |
| 16 | `ImageView` | `android:layout_width` | `wrap_content` |
| 17 | `ImageView` | `android:layout_height` | `wrap_content` |
| 18 | `ImageView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 19 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 20 | `ImageView` | `app:srcCompat` | `@drawable/ic_info_circle` |
| 21 | `ImageView` | `app:tint` | `@color/icon_primary` |
| 22 | `com.getmimo.ui.profile.view.ProfileCertificatesView` | `android:id` | `@id/profile_paths_progress_view` |
| 23 | `com.getmimo.ui.profile.view.ProfileCertificatesView` | `android:layout_width` | `0.000000dip` |
| 24 | `com.getmimo.ui.profile.view.ProfileCertificatesView` | `android:layout_height` | `wrap_content` |
| 25 | `com.getmimo.ui.profile.view.ProfileCertificatesView` | `android:layout_marginTop` | `@dimen/spacing_m_expandable` |
| 26 | `com.getmimo.ui.profile.view.ProfileCertificatesView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 27 | `com.getmimo.ui.profile.view.ProfileCertificatesView` | `app:layout_constraintStart_toStartOf` | `0` |
| 28 | `com.getmimo.ui.profile.view.ProfileCertificatesView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_certificate_title` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/icon_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/spacing_l_expandable` | `24.000000dip` / `36.000000dip` (sw600dp) |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@string/profile_certificates` | `Certificates` / `Zertifikate` (de) / `Certificados` (es) / `Certificats` (fr) / `Sertifikat` (in) / `Certificati` (it) / `Certyfikaty` (pl) / `Certificados` (pt-rBR) / `Сертификаты` (ru) / `Sertifikalar` (tr) |
| `@style/TextH3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/iv_certificate_info_icon
@id/profile_paths_progress_view
@id/tv_certificate_title
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l_expandable" android:layout_marginBottom="@dimen/spacing_m_expandable" android:layout_marginHorizontal="@dimen/spacing_m_expandable">
  <TextView android:textColor="@color/text_primary" android:id="@id/tv_certificate_title" android:layout_width="wrap_content" android:layout_height="wrap_content" android:text="@string/profile_certificates" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0" style="@style/TextH3"/>
  <ImageView android:gravity="0x00800005" android:id="@id/iv_certificate_info_icon" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintTop_toTopOf="0" app:srcCompat="@drawable/ic_info_circle" app:tint="@color/icon_primary"/>
  <com.getmimo.ui.profile.view.ProfileCertificatesView android:id="@id/profile_paths_progress_view" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m_expandable" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_certificate_title"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
