# پروندهٔ لایه — `res/layout/profile_certificates_item.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/profile_certificates_item.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/profile_certificates_item.xml`](../../SOURCE/res/layout/profile_certificates_item.xml) |
| SHA-256 دیکد | `f86984cc6ca88e766592c99a0bd143c4b3d2dec7c0cf1ab4947bb0eb58813bcc` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 1 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ TextView
   └─ com.getmimo.ui.profile.view.ProfileCertificatesView  #@id/profile_paths_progress_view
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 3 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 4 | `LinearLayout` | `android:layout_marginTop` | `@dimen/spacing_l_expandable` |
| 5 | `LinearLayout` | `android:layout_marginBottom` | `@dimen/spacing_m_expandable` |
| 6 | `LinearLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_m_expandable` |
| 7 | `TextView` | `android:textColor` | `@color/text_primary` |
| 8 | `TextView` | `android:layout_width` | `wrap_content` |
| 9 | `TextView` | `android:layout_height` | `wrap_content` |
| 10 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_m_expandable` |
| 11 | `TextView` | `android:text` | `@string/profile_certificates` |
| 12 | `TextView` | `style` | `@style/TextH3` |
| 13 | `com.getmimo.ui.profile.view.ProfileCertificatesView` | `android:id` | `@id/profile_paths_progress_view` |
| 14 | `com.getmimo.ui.profile.view.ProfileCertificatesView` | `android:layout_width` | `match_parent` |
| 15 | `com.getmimo.ui.profile.view.ProfileCertificatesView` | `android:layout_height` | `wrap_content` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@dimen/spacing_l_expandable` | `24.000000dip` / `36.000000dip` (sw600dp) |
| `@dimen/spacing_m_expandable` | `16.000000dip` / `24.000000dip` (sw600dp) |
| `@string/profile_certificates` | `Certificates` / `Zertifikate` (de) / `Certificados` (es) / `Certificats` (fr) / `Sertifikat` (in) / `Certificati` (it) / `Certyfikaty` (pl) / `Certificados` (pt-rBR) / `Сертификаты` (ru) / `Sertifikalar` (tr) |
| `@style/TextH3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/profile_paths_progress_view
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_l_expandable" android:layout_marginBottom="@dimen/spacing_m_expandable" android:layout_marginHorizontal="@dimen/spacing_m_expandable">
  <TextView android:textColor="@color/text_primary" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/spacing_m_expandable" android:text="@string/profile_certificates" style="@style/TextH3"/>
  <com.getmimo.ui.profile.view.ProfileCertificatesView android:id="@id/profile_paths_progress_view" android:layout_width="match_parent" android:layout_height="wrap_content"/>
</LinearLayout>
```
