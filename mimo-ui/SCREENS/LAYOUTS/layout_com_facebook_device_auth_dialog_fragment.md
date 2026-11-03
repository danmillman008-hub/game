# پروندهٔ لایه — `res/layout/com_facebook_device_auth_dialog_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/com_facebook_device_auth_dialog_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/com_facebook_device_auth_dialog_fragment.xml`](../../SOURCE/res/layout/com_facebook_device_auth_dialog_fragment.xml) |
| SHA-256 دیکد | `bfbb86c2eb38dba39104ed7c04acd1b0ad706c4223ebf1431a918d7ca6b83c42` |
| ریشه | `androidx.cardview.widget.CardView` |
| تعداد گره | 11 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 9 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 12 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.cardview.widget.CardView
   └─ LinearLayout
      ├─ RelativeLayout
      │  ├─ FrameLayout
      │  │  └─ androidx.appcompat.widget.AppCompatImageView
      │  ├─ TextView  #@id/confirmation_code
      │  └─ ProgressBar  #@id/progress_bar
      ├─ TextView  #@id/com_facebook_device_auth_instructions
      └─ FrameLayout
         └─ Button  #@id/cancel_button
            └─ requestFocus
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.cardview.widget.CardView` | `android:layout_width` | `wrap_content` |
| 2 | `androidx.cardview.widget.CardView` | `android:layout_height` | `wrap_content` |
| 3 | `androidx.cardview.widget.CardView` | `app:cardBackgroundColor` | `@0x0106000D` |
| 4 | `androidx.cardview.widget.CardView` | `app:cardElevation` | `10.000000dip` |
| 5 | `LinearLayout` | `android:orientation` | `vertical` |
| 6 | `LinearLayout` | `android:background` | `@drawable/com_facebook_auth_dialog_background` |
| 7 | `LinearLayout` | `android:layout_width` | `300.000000dip` |
| 8 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 9 | `RelativeLayout` | `android:orientation` | `horizontal` |
| 10 | `RelativeLayout` | `android:background` | `@drawable/com_facebook_auth_dialog_header_background` |
| 11 | `RelativeLayout` | `android:layout_width` | `match_parent` |
| 12 | `RelativeLayout` | `android:layout_height` | `100.000000dip` |
| 13 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 14 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 15 | `androidx.appcompat.widget.AppCompatImageView` | `android:layout_width` | `18.000000dip` |
| 16 | `androidx.appcompat.widget.AppCompatImageView` | `android:layout_height` | `18.000000dip` |
| 17 | `androidx.appcompat.widget.AppCompatImageView` | `android:layout_marginLeft` | `12.000000dip` |
| 18 | `androidx.appcompat.widget.AppCompatImageView` | `android:layout_marginTop` | `11.000000dip` |
| 19 | `androidx.appcompat.widget.AppCompatImageView` | `android:layout_marginBottom` | `11.000000dip` |
| 20 | `androidx.appcompat.widget.AppCompatImageView` | `android:scaleType` | `fitXY` |
| 21 | `androidx.appcompat.widget.AppCompatImageView` | `android:adjustViewBounds` | `false` |
| 22 | `androidx.appcompat.widget.AppCompatImageView` | `app:srcCompat` | `@drawable/com_facebook_favicon_blue` |
| 23 | `TextView` | `android:textSize` | `30.000000sp` |
| 24 | `TextView` | `android:typeface` | `1` |
| 25 | `TextView` | `android:textColor` | `@color/com_facebook_blue` |
| 26 | `TextView` | `android:gravity` | `0x00000011` |
| 27 | `TextView` | `android:id` | `@id/confirmation_code` |
| 28 | `TextView` | `android:visibility` | `invisible` |
| 29 | `TextView` | `android:layout_width` | `wrap_content` |
| 30 | `TextView` | `android:layout_height` | `wrap_content` |
| 31 | `TextView` | `android:layout_centerInParent` | `true` |
| 32 | `TextView` | `android:fontFamily` | `roboto_condensed` |
| 33 | `ProgressBar` | `android:id` | `@id/progress_bar` |
| 34 | `ProgressBar` | `android:layout_width` | `wrap_content` |
| 35 | `ProgressBar` | `android:layout_height` | `0.000000dip` |
| 36 | `ProgressBar` | `android:layout_alignTop` | `@id/confirmation_code` |
| 37 | `ProgressBar` | `android:layout_alignBottom` | `@id/confirmation_code` |
| 38 | `ProgressBar` | `android:layout_centerInParent` | `true` |
| 39 | `ProgressBar` | `android:layout_centerHorizontal` | `true` |
| 40 | `ProgressBar` | `android:layout_centerVertical` | `true` |
| 41 | `TextView` | `android:textSize` | `12.000000sp` |
| 42 | `TextView` | `android:typeface` | `1` |
| 43 | `TextView` | `android:textColor` | `@color/com_facebook_device_auth_text` |
| 44 | `TextView` | `android:gravity` | `0x00000011` |
| 45 | `TextView` | `android:id` | `@id/com_facebook_device_auth_instructions` |
| 46 | `TextView` | `android:layout_width` | `match_parent` |
| 47 | `TextView` | `android:layout_height` | `wrap_content` |
| 48 | `TextView` | `android:layout_marginTop` | `20.000000dip` |
| 49 | `TextView` | `android:singleLine` | `false` |
| 50 | `TextView` | `android:fontFamily` | `roboto_condensed` |
| 51 | `TextView` | `android:layout_marginStart` | `16.000000dip` |
| 52 | `TextView` | `android:layout_marginEnd` | `16.000000dip` |
| 53 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 54 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 55 | `FrameLayout` | `android:layout_marginTop` | `14.000000dip` |
| 56 | `FrameLayout` | `android:layout_marginBottom` | `17.000000dip` |
| 57 | `Button` | `android:textSize` | `10.000000sp` |
| 58 | `Button` | `android:typeface` | `1` |
| 59 | `Button` | `android:textStyle` | `0x00000001` |
| 60 | `Button` | `android:textColor` | `@color/com_facebook_device_auth_text` |
| 61 | `Button` | `android:layout_gravity` | `0x00000001` |
| 62 | `Button` | `android:id` | `@id/cancel_button` |
| 63 | `Button` | `android:background` | `@drawable/com_facebook_auth_dialog_cancel_background` |
| 64 | `Button` | `android:focusable` | `true` |
| 65 | `Button` | `android:clickable` | `true` |
| 66 | `Button` | `android:layout_width` | `84.000000dip` |
| 67 | `Button` | `android:layout_height` | `27.000000dip` |
| 68 | `Button` | `android:text` | `@0x01040000` |
| 69 | `Button` | `android:textAllCaps` | `true` |
| 70 | `Button` | `android:fontFamily` | `roboto_condensed` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/com_facebook_blue` | `#FF1877F2` |
| `@color/com_facebook_device_auth_text` | `#FF90949C` |

## ۴. شناسه‌های `@id`

```text
@id/cancel_button
@id/com_facebook_device_auth_instructions
@id/confirmation_code
@id/progress_bar
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.facebook.FacebookActivity
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.cardview.widget.CardView xmlns:app="http://schemas.android.com/apk/res-auto" xmlns:android="http://schemas.android.com/apk/res/android" android:layout_width="wrap_content" android:layout_height="wrap_content" app:cardBackgroundColor="@0x0106000D" app:cardElevation="10.000000dip">
  <LinearLayout android:orientation="vertical" android:background="@drawable/com_facebook_auth_dialog_background" android:layout_width="300.000000dip" android:layout_height="wrap_content">
    <RelativeLayout android:orientation="horizontal" android:background="@drawable/com_facebook_auth_dialog_header_background" android:layout_width="match_parent" android:layout_height="100.000000dip">
      <FrameLayout android:layout_width="match_parent" android:layout_height="wrap_content">
        <androidx.appcompat.widget.AppCompatImageView android:layout_width="18.000000dip" android:layout_height="18.000000dip" android:layout_marginLeft="12.000000dip" android:layout_marginTop="11.000000dip" android:layout_marginBottom="11.000000dip" android:scaleType="fitXY" android:adjustViewBounds="false" app:srcCompat="@drawable/com_facebook_favicon_blue"/>
      </FrameLayout>
      <TextView android:textSize="30.000000sp" android:typeface="1" android:textColor="@color/com_facebook_blue" android:gravity="0x00000011" android:id="@id/confirmation_code" android:visibility="invisible" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_centerInParent="true" android:fontFamily="roboto_condensed"/>
      <ProgressBar android:id="@id/progress_bar" android:layout_width="wrap_content" android:layout_height="0.000000dip" android:layout_alignTop="@id/confirmation_code" android:layout_alignBottom="@id/confirmation_code" android:layout_centerInParent="true" android:layout_centerHorizontal="true" android:layout_centerVertical="true"/>
    </RelativeLayout>
    <TextView android:textSize="12.000000sp" android:typeface="1" android:textColor="@color/com_facebook_device_auth_text" android:gravity="0x00000011" android:id="@id/com_facebook_device_auth_instructions" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="20.000000dip" android:singleLine="false" android:fontFamily="roboto_condensed" android:layout_marginStart="16.000000dip" android:layout_marginEnd="16.000000dip"/>
    <FrameLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="14.000000dip" android:layout_marginBottom="17.000000dip">
      <Button android:textSize="10.000000sp" android:typeface="1" android:textStyle="0x00000001" android:textColor="@color/com_facebook_device_auth_text" android:layout_gravity="0x00000001" android:id="@id/cancel_button" android:background="@drawable/com_facebook_auth_dialog_cancel_background" android:focusable="true" android:clickable="true" android:layout_width="84.000000dip" android:layout_height="27.000000dip" android:text="@0x01040000" android:textAllCaps="true" android:fontFamily="roboto_condensed">
        <requestFocus/>
      </Button>
    </FrameLayout>
  </LinearLayout>
</androidx.cardview.widget.CardView>
```
