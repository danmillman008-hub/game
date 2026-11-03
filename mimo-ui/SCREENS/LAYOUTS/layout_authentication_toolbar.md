# پروندهٔ لایه — `res/layout/authentication_toolbar.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/authentication_toolbar.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/authentication_toolbar.xml`](../../SOURCE/res/layout/authentication_toolbar.xml) |
| SHA-256 دیکد | `34ee0e54c6948e7248ab4eb1f224b753ffba23dca7486abea3eb398937abac3f` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 2 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 6 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ ImageView  #@id/btn_back
   └─ TextView  #@id/tv_authentication_step
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `wrap_content` |
| 3 | `ImageView` | `android:id` | `@id/btn_back` |
| 4 | `ImageView` | `android:padding` | `@dimen/spacing_s` |
| 5 | `ImageView` | `android:layout_width` | `wrap_content` |
| 6 | `ImageView` | `android:layout_height` | `wrap_content` |
| 7 | `ImageView` | `app:layout_constraintLeft_toLeftOf` | `0` |
| 8 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 9 | `ImageView` | `app:srcCompat` | `@drawable/ic_arrow_left` |
| 10 | `ImageView` | `app:tint` | `@color/icon_weak` |
| 11 | `TextView` | `android:gravity` | `0x00000011` |
| 12 | `TextView` | `android:id` | `@id/tv_authentication_step` |
| 13 | `TextView` | `android:layout_width` | `wrap_content` |
| 14 | `TextView` | `android:layout_height` | `wrap_content` |
| 15 | `TextView` | `android:layout_marginRight` | `16.000000dip` |
| 16 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `@id/btn_back` |
| 17 | `TextView` | `app:layout_constraintRight_toRightOf` | `0` |
| 18 | `TextView` | `app:layout_constraintTop_toTopOf` | `@id/btn_back` |
| 19 | `TextView` | `style` | `@style/TextViewSignUpStep` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/icon_weak` | `#FFA3A5C3` / `#80FFFFFF` (night) |
| `@dimen/spacing_s` | `12.000000dip` |
| `@style/TextViewSignUpStep` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/text_weak', 'value_type': 'reference'}, {'attr': 'android:textAllCaps', 'attr_id': '0x0101038C', 'value': 'true', 'value_type': 'int_boolean'}]` |

## ۴. شناسه‌های `@id`

```text
@id/btn_back
@id/tv_authentication_step
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.authentication.AuthenticationActivity
com.getmimo.ui.authentication.AuthenticationFragment$configureButtons$2
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/login_set_email_fragment.xml
res/layout/login_set_password_fragment.xml
res/layout/sign_up_set_email_fragment.xml
res/layout/sign_up_set_password_fragment.xml
res/layout/sign_up_set_username_fragment.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:layout_width="match_parent" android:layout_height="wrap_content">
  <ImageView android:id="@id/btn_back" android:padding="@dimen/spacing_s" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintLeft_toLeftOf="0" app:layout_constraintTop_toTopOf="0" app:srcCompat="@drawable/ic_arrow_left" app:tint="@color/icon_weak"/>
  <TextView android:gravity="0x00000011" android:id="@id/tv_authentication_step" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginRight="16.000000dip" app:layout_constraintBottom_toBottomOf="@id/btn_back" app:layout_constraintRight_toRightOf="0" app:layout_constraintTop_toTopOf="@id/btn_back" style="@style/TextViewSignUpStep"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
