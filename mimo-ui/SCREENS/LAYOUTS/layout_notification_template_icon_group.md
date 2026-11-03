# پروندهٔ لایه — `res/layout/notification_template_icon_group.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/notification_template_icon_group.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/notification_template_icon_group.xml`](../../SOURCE/res/layout/notification_template_icon_group.xml) |
| SHA-256 دیکد | `63d6de5fef10150b62a1348de9cc8db34b079322c9d2fc2355eaae0fe3e33e01` |
| ریشه | `FrameLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 3 |
| تگ‌های استفاده‌شده | 2 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 7 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ FrameLayout  #@id/icon_group
   ├─ ImageView  #@id/icon
   └─ ImageView  #@id/right_icon
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `FrameLayout` | `android:id` | `@id/icon_group` |
| 2 | `FrameLayout` | `android:layout_width` | `@dimen/notification_large_icon_width` |
| 3 | `FrameLayout` | `android:layout_height` | `@dimen/notification_large_icon_height` |
| 4 | `ImageView` | `android:id` | `@id/icon` |
| 5 | `ImageView` | `android:layout_width` | `match_parent` |
| 6 | `ImageView` | `android:layout_height` | `match_parent` |
| 7 | `ImageView` | `android:layout_marginTop` | `@dimen/notification_big_circle_margin` |
| 8 | `ImageView` | `android:layout_marginBottom` | `@dimen/notification_big_circle_margin` |
| 9 | `ImageView` | `android:scaleType` | `centerInside` |
| 10 | `ImageView` | `android:layout_marginStart` | `@dimen/notification_big_circle_margin` |
| 11 | `ImageView` | `android:layout_marginEnd` | `@dimen/notification_big_circle_margin` |
| 12 | `ImageView` | `android:layout_gravity` | `0x00800055` |
| 13 | `ImageView` | `android:id` | `@id/right_icon` |
| 14 | `ImageView` | `android:visibility` | `gone` |
| 15 | `ImageView` | `android:layout_width` | `@dimen/notification_right_icon_size` |
| 16 | `ImageView` | `android:layout_height` | `@dimen/notification_right_icon_size` |
| 17 | `ImageView` | `android:layout_marginBottom` | `8.000000dip` |
| 18 | `ImageView` | `android:scaleType` | `centerInside` |
| 19 | `ImageView` | `android:layout_marginEnd` | `8.000000dip` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/notification_big_circle_margin` | `12.000000dip` |
| `@dimen/notification_large_icon_height` | `64.000000dip` |
| `@dimen/notification_large_icon_width` | `64.000000dip` |
| `@dimen/notification_right_icon_size` | `16.000000dip` |

## ۴. شناسه‌های `@id`

```text
@id/icon
@id/icon_group
@id/right_icon
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

```text
res/layout/notification_template_big_media.xml
res/layout/notification_template_big_media_custom.xml
res/layout/notification_template_custom_big.xml
res/layout/notification_template_media.xml
res/layout/notification_template_media_custom.xml
```

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android" android:id="@id/icon_group" android:layout_width="@dimen/notification_large_icon_width" android:layout_height="@dimen/notification_large_icon_height">
  <ImageView android:id="@id/icon" android:layout_width="match_parent" android:layout_height="match_parent" android:layout_marginTop="@dimen/notification_big_circle_margin" android:layout_marginBottom="@dimen/notification_big_circle_margin" android:scaleType="centerInside" android:layout_marginStart="@dimen/notification_big_circle_margin" android:layout_marginEnd="@dimen/notification_big_circle_margin"/>
  <ImageView android:layout_gravity="0x00800055" android:id="@id/right_icon" android:visibility="gone" android:layout_width="@dimen/notification_right_icon_size" android:layout_height="@dimen/notification_right_icon_size" android:layout_marginBottom="8.000000dip" android:scaleType="centerInside" android:layout_marginEnd="8.000000dip"/>
</FrameLayout>
```
