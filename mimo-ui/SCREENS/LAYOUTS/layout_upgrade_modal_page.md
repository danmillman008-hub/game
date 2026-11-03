# پروندهٔ لایه — `res/layout/upgrade_modal_page.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/upgrade_modal_page.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/upgrade_modal_page.xml`](../../SOURCE/res/layout/upgrade_modal_page.xml) |
| SHA-256 دیکد | `beb353adcc3b049f7b71b9e94644a413d3143065594d0527b3ec35c87fc90949` |
| ریشه | `androidx.constraintlayout.widget.ConstraintLayout` |
| تعداد گره | 6 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 13 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ FrameLayout  #@id/image_container_upgrade_modal
   │  ├─ ImageView  #@id/iv_upgrade_modal
   │  └─ app.rive.runtime.kotlin.RiveAnimationView  #@id/rive_upgrade_modal_animation
   ├─ TextView  #@id/tv_upgrade_modal_title
   └─ TextView  #@id/tv_upgrade_modal_description
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:gravity` | `0x00000011` |
| 2 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_gravity` | `0x00000011` |
| 3 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_width` | `match_parent` |
| 4 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:layout_height` | `match_parent` |
| 5 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingStart` | `@dimen/modal_default_padding_horizontal` |
| 6 | `androidx.constraintlayout.widget.ConstraintLayout` | `android:paddingEnd` | `@dimen/modal_default_padding_horizontal` |
| 7 | `FrameLayout` | `android:id` | `@id/image_container_upgrade_modal` |
| 8 | `FrameLayout` | `android:layout_width` | `wrap_content` |
| 9 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 10 | `FrameLayout` | `app:layout_constraintEnd_toEndOf` | `0` |
| 11 | `FrameLayout` | `app:layout_constraintStart_toStartOf` | `0` |
| 12 | `FrameLayout` | `app:layout_constraintTop_toTopOf` | `0` |
| 13 | `ImageView` | `android:id` | `@id/iv_upgrade_modal` |
| 14 | `ImageView` | `android:layout_width` | `wrap_content` |
| 15 | `ImageView` | `android:layout_height` | `120.000000dip` |
| 16 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_gravity` | `0x00000001` |
| 17 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:id` | `@id/rive_upgrade_modal_animation` |
| 18 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_width` | `wrap_content` |
| 19 | `app.rive.runtime.kotlin.RiveAnimationView` | `android:layout_height` | `120.000000dip` |
| 20 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveFit` | `4` |
| 21 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveLoop` | `1` |
| 22 | `app.rive.runtime.kotlin.RiveAnimationView` | `app:riveStateMachine` | `default` |
| 23 | `TextView` | `android:textColor` | `@color/text_primary` |
| 24 | `TextView` | `android:gravity` | `0x00000011` |
| 25 | `TextView` | `android:id` | `@id/tv_upgrade_modal_title` |
| 26 | `TextView` | `android:layout_width` | `0.000000dip` |
| 27 | `TextView` | `android:layout_height` | `wrap_content` |
| 28 | `TextView` | `android:layout_marginTop` | `@dimen/modal_default_image_margin_bottom` |
| 29 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 30 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 31 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/image_container_upgrade_modal` |
| 32 | `TextView` | `style` | `@style/TextH2` |
| 33 | `TextView` | `android:textColor` | `@color/text_weak` |
| 34 | `TextView` | `android:gravity` | `0x00000031` |
| 35 | `TextView` | `android:id` | `@id/tv_upgrade_modal_description` |
| 36 | `TextView` | `android:layout_width` | `0.000000dip` |
| 37 | `TextView` | `android:layout_height` | `wrap_content` |
| 38 | `TextView` | `android:layout_marginTop` | `@dimen/modal_default_title_margin_bottom` |
| 39 | `TextView` | `android:layout_marginBottom` | `@dimen/modal_default_description_margin_bottom` |
| 40 | `TextView` | `app:layout_constraintEnd_toEndOf` | `0` |
| 41 | `TextView` | `app:layout_constraintStart_toStartOf` | `0` |
| 42 | `TextView` | `app:layout_constraintTop_toBottomOf` | `@id/tv_upgrade_modal_title` |
| 43 | `TextView` | `style` | `@style/TextP2` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/modal_default_description_margin_bottom` | `24.000000dip` |
| `@dimen/modal_default_image_margin_bottom` | `16.000000dip` / `20.000000dip` (sw600dp) |
| `@dimen/modal_default_padding_horizontal` | `24.000000dip` |
| `@dimen/modal_default_title_margin_bottom` | `8.000000dip` / `12.000000dip` (sw600dp) |
| `@style/TextH2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '26.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/image_container_upgrade_modal
@id/iv_upgrade_modal
@id/rive_upgrade_modal_animation
@id/tv_upgrade_modal_description
@id/tv_upgrade_modal_title
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.upgrade.UpgradeModalActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:gravity="0x00000011" android:layout_gravity="0x00000011" android:layout_width="match_parent" android:layout_height="match_parent" android:paddingStart="@dimen/modal_default_padding_horizontal" android:paddingEnd="@dimen/modal_default_padding_horizontal">
  <FrameLayout android:id="@id/image_container_upgrade_modal" android:layout_width="wrap_content" android:layout_height="wrap_content" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toTopOf="0">
    <ImageView android:id="@id/iv_upgrade_modal" android:layout_width="wrap_content" android:layout_height="120.000000dip"/>
    <app.rive.runtime.kotlin.RiveAnimationView android:layout_gravity="0x00000001" android:id="@id/rive_upgrade_modal_animation" android:layout_width="wrap_content" android:layout_height="120.000000dip" app:riveFit="4" app:riveLoop="1" app:riveStateMachine="default"/>
  </FrameLayout>
  <TextView android:textColor="@color/text_primary" android:gravity="0x00000011" android:id="@id/tv_upgrade_modal_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/modal_default_image_margin_bottom" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/image_container_upgrade_modal" style="@style/TextH2"/>
  <TextView android:textColor="@color/text_weak" android:gravity="0x00000031" android:id="@id/tv_upgrade_modal_description" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_marginTop="@dimen/modal_default_title_margin_bottom" android:layout_marginBottom="@dimen/modal_default_description_margin_bottom" app:layout_constraintEnd_toEndOf="0" app:layout_constraintStart_toStartOf="0" app:layout_constraintTop_toBottomOf="@id/tv_upgrade_modal_title" style="@style/TextP2"/>
</androidx.constraintlayout.widget.ConstraintLayout>
```
