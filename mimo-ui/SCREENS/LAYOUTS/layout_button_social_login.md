# پروندهٔ لایه — `res/layout/button_social_login.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/button_social_login.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/button_social_login.xml`](../../SOURCE/res/layout/button_social_login.xml) |
| SHA-256 دیکد | `9702c0adcea6384fce15f59808e314c20e91b87a1c2a4a6c07b37e6b0150b129` |
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
   ├─ ImageView  #@id/iv_social_signin
   └─ TextView  #@id/tv_social_signin
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_gravity` | `0x00000011` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:orientation` | `horizontal` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `48.000000dip` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingHorizontal` | `@dimen/spacing_xxs` |
| 6 | `ImageView` | `android:id` | `@id/iv_social_signin` |
| 7 | `ImageView` | `android:background` | `@drawable/button_social_login_logo_round_background` |
| 8 | `ImageView` | `android:padding` | `10.000000dip` |
| 9 | `ImageView` | `android:layout_width` | `@dimen/sociallogin_imageview_size` |
| 10 | `ImageView` | `android:layout_height` | `@dimen/sociallogin_imageview_size` |
| 11 | `ImageView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 12 | `ImageView` | `app:layout_constraintEnd_toStartOf` | `@id/tv_social_signin` |
| 13 | `ImageView` | `app:layout_constraintHorizontal_bias` | `0.000000` |
| 14 | `ImageView` | `app:layout_constraintHorizontal_chainStyle` | `2` |
| 15 | `ImageView` | `app:layout_constraintStart_toStartOf` | `0` |
| 16 | `ImageView` | `app:layout_constraintTop_toTopOf` | `0` |
| 17 | `TextView` | `android:gravity` | `0x00000011` |
| 18 | `TextView` | `android:id` | `@id/tv_social_signin` |
| 19 | `TextView` | `android:layout_width` | `0.000000dip` |
| 20 | `TextView` | `android:layout_height` | `wrap_content` |
| 21 | `TextView` | `android:layout_marginStart` | `@dimen/spacing_xxs` |
| 22 | `TextView` | `android:layout_marginEnd` | `@dimen/spacing_xl` |
| 23 | `TextView` | `app:layout_constraintBottom_toBottomOf` | `0` |
| 24 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 25 | `TextView` | `app:layout_constraintStart_toEndOf` | `@id/iv_social_signin` |
| 26 | `TextView` | `app:layout_constraintTop_toTopOf` | `0` |
| 27 | `TextView` | `style` | `@style/TextViewSocialLogin` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/sociallogin_imageview_size` | `40.000000dip` |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@dimen/spacing_xxs` | `4.000000dip` |
| `@style/TextViewSocialLogin` | `[{'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/support_white', 'value_type': 'reference'}, {'attr': 'android:textAllCaps', 'attr_id': '0x0101038C', 'value': 'true', 'value_type': 'int_boolean'}]` |

## ۴. شناسه‌های `@id`

```text
@id/iv_social_signin
@id/tv_social_signin
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
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:layout_gravity="0x00000011" android:orientation="horizontal" android:layout_width="match_parent" android:layout_height="48.000000dip" android:paddingHorizontal="@dimen/spacing_xxs">
  <ImageView android:id="@id/iv_social_signin" android:background="@drawable/button_social_login_logo_round_background" android:padding="10.000000dip" android:layout_width="@dimen/sociallogin_imageview_size" android:layout_height="@dimen/sociallogin_imageview_size" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toStartOf="@id/tv_social_signin" app:layout_constraintHorizontal_bias="0.000000" app:layout_constraintHorizontal_chainStyle="2" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0"/>
  <TextView android:gravity="0x00000011" android:id="@id/tv_social_signin" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginStart="@dimen/spacing_xxs" android:layout_marginEnd="@dimen/spacing_xl" app:layout_constraintBottom_toBottomOf="0" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toEndOf="@id/iv_social_signin" app:layout_constraintTop_toTopOf="0" style="@style/TextViewSocialLogin"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
