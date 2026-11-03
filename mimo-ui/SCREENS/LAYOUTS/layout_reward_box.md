# پروندهٔ لایه — `res/layout/reward_box.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/reward_box.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/reward_box.xml`](../../SOURCE/res/layout/reward_box.xml) |
| SHA-256 دیکد | `266ca848f8046e9826b3e71aaa70925668bcb689265f30b1ac1f0906e9ab2809` |
| ریشه | `FrameLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 10 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout
   ├─ com.airbnb.lottie.LottieAnimationView  #@id/lottie_reward_box
   ├─ TextView  #@id/tv_reward_box_label_main
   └─ TextView  #@id/tv_reward_box_label_light
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:layout_width` | `wrap_content` |
| 2 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 3 | `com.airbnb.lottie.LottieAnimationView` | `android:layout_gravity` | `0x00000050` |
| 4 | `com.airbnb.lottie.LottieAnimationView` | `android:id` | `@id/lottie_reward_box` |
| 5 | `com.airbnb.lottie.LottieAnimationView` | `android:layout_width` | `wrap_content` |
| 6 | `com.airbnb.lottie.LottieAnimationView` | `android:layout_height` | `wrap_content` |
| 7 | `com.airbnb.lottie.LottieAnimationView` | `android:adjustViewBounds` | `true` |
| 8 | `com.airbnb.lottie.LottieAnimationView` | `android:maxWidth` | `116.000000dip` |
| 9 | `com.airbnb.lottie.LottieAnimationView` | `android:maxHeight` | `120.000000dip` |
| 10 | `com.airbnb.lottie.LottieAnimationView` | `app:lottie_rawRes` | `@raw/onboarding_curriculum` |
| 11 | `TextView` | `android:textColor` | `@color/text_reversed` |
| 12 | `TextView` | `android:gravity` | `0x00000011` |
| 13 | `TextView` | `android:layout_gravity` | `0x00000051` |
| 14 | `TextView` | `android:id` | `@id/tv_reward_box_label_main` |
| 15 | `TextView` | `android:background` | `@drawable/bg_reward_label` |
| 16 | `TextView` | `android:layout_width` | `wrap_content` |
| 17 | `TextView` | `android:layout_height` | `30.000000dip` |
| 18 | `TextView` | `android:scaleX` | `0.000000` |
| 19 | `TextView` | `android:scaleY` | `0.000000` |
| 20 | `TextView` | `android:paddingStart` | `10.000000dip` |
| 21 | `TextView` | `android:paddingEnd` | `10.000000dip` |
| 22 | `TextView` | `style` | `@style/TextH4` |
| 23 | `TextView` | `android:textColor` | `@color/text_disabled` |
| 24 | `TextView` | `android:gravity` | `0x00000011` |
| 25 | `TextView` | `android:layout_gravity` | `0x00000051` |
| 26 | `TextView` | `android:id` | `@id/tv_reward_box_label_light` |
| 27 | `TextView` | `android:background` | `@drawable/bg_reward_label_missed` |
| 28 | `TextView` | `android:layout_width` | `wrap_content` |
| 29 | `TextView` | `android:layout_height` | `30.000000dip` |
| 30 | `TextView` | `android:scaleX` | `0.000000` |
| 31 | `TextView` | `android:scaleY` | `0.000000` |
| 32 | `TextView` | `android:paddingStart` | `10.000000dip` |
| 33 | `TextView` | `android:paddingEnd` | `10.000000dip` |
| 34 | `TextView` | `style` | `@style/TextTitle2` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_disabled` | `#40252746` / `#4DFFFFFF` (night) |
| `@color/text_reversed` | `#FFFFFFFF` / `#FF252746` (night) |
| `@style/TextH4` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '11.399995sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextTitle2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '14.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.199983sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '10.399995sp', 'value_type': 'dimension'}, {'attr': 'android:letterSpacing', 'attr_id': '0x010104B6', 'value': '0.000000', 'value_type': 'float'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_medium', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/lottie_reward_box
@id/tv_reward_box_label_light
@id/tv_reward_box_label_main
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.reward.RewardFragment$loadUserName$1
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="wrap_content" android:layout_height="wrap_content">
  <com.airbnb.lottie.LottieAnimationView android:layout_gravity="0x00000050" android:id="@id/lottie_reward_box" android:layout_width="wrap_content" android:layout_height="wrap_content" android:adjustViewBounds="true" android:maxWidth="116.000000dip" android:maxHeight="120.000000dip" app:lottie_rawRes="@raw/onboarding_curriculum"/>
  <TextView android:textColor="@color/text_reversed" android:gravity="0x00000011" android:layout_gravity="0x00000051" android:id="@id/tv_reward_box_label_main" android:background="@drawable/bg_reward_label" android:layout_width="wrap_content" android:layout_height="30.000000dip" android:scaleX="0.000000" android:scaleY="0.000000" android:paddingStart="10.000000dip" android:paddingEnd="10.000000dip" style="@style/TextH4"/>
  <TextView android:textColor="@color/text_disabled" android:gravity="0x00000011" android:layout_gravity="0x00000051" android:id="@id/tv_reward_box_label_light" android:background="@drawable/bg_reward_label_missed" android:layout_width="wrap_content" android:layout_height="30.000000dip" android:scaleX="0.000000" android:scaleY="0.000000" android:paddingStart="10.000000dip" android:paddingEnd="10.000000dip" style="@style/TextTitle2"/>
</FrameLayout>
```
