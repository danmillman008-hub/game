# پروندهٔ لایه — `res/layout/flash_bar_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/flash_bar_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/flash_bar_view.xml`](../../SOURCE/res/layout/flash_bar_view.xml) |
| SHA-256 دیکد | `1409dcdb3f947588928cbad860a447a3c7eec0de09a39d1493d5cb32add13bb7` |
| ریشه | `LinearLayout` |
| تعداد گره | 13 |
| تعداد شناسه | 11 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 28 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout  #@id/fbRoot
   └─ LinearLayout  #@id/fbContent
      ├─ LinearLayout
      │  ├─ com.andrognito.flashbar.view.FbProgress  #@id/fbLeftProgress
      │  ├─ ImageView  #@id/fbIcon
      │  ├─ LinearLayout
      │  │  ├─ TextView  #@id/fbTitle
      │  │  └─ TextView  #@id/fbMessage
      │  ├─ com.andrognito.flashbar.view.FbButton  #@id/fbPrimaryAction
      │  └─ com.andrognito.flashbar.view.FbProgress  #@id/fbRightProgress
      └─ LinearLayout  #@id/fbSecondaryActionContainer
         ├─ com.andrognito.flashbar.view.FbButton  #@id/fbPositiveAction
         └─ com.andrognito.flashbar.view.FbButton  #@id/fbNegativeAction
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:id` | `@id/fbRoot` |
| 3 | `LinearLayout` | `android:background` | `@color/warm_grey` |
| 4 | `LinearLayout` | `android:padding` | `@dimen/fb_content_padding_all` |
| 5 | `LinearLayout` | `android:focusable` | `true` |
| 6 | `LinearLayout` | `android:clickable` | `true` |
| 7 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 8 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 9 | `LinearLayout` | `android:foreground` | `?0x0101030E` |
| 10 | `LinearLayout` | `android:orientation` | `vertical` |
| 11 | `LinearLayout` | `android:id` | `@id/fbContent` |
| 12 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 13 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 14 | `LinearLayout` | `android:gravity` | `0x00000010` |
| 15 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 16 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 17 | `com.andrognito.flashbar.view.FbProgress` | `android:layout_gravity` | `0x00000010` |
| 18 | `com.andrognito.flashbar.view.FbProgress` | `android:id` | `@id/fbLeftProgress` |
| 19 | `com.andrognito.flashbar.view.FbProgress` | `android:visibility` | `gone` |
| 20 | `com.andrognito.flashbar.view.FbProgress` | `android:layout_width` | `@dimen/fb_progress_size` |
| 21 | `com.andrognito.flashbar.view.FbProgress` | `android:layout_height` | `@dimen/fb_progress_size` |
| 22 | `com.andrognito.flashbar.view.FbProgress` | `android:layout_marginRight` | `@dimen/fb_margin_progress` |
| 23 | `com.andrognito.flashbar.view.FbProgress` | `android:layout_marginEnd` | `@dimen/fb_margin_progress` |
| 24 | `com.andrognito.flashbar.view.FbProgress` | `style` | `@style/FbCircularIndeterminateProgressStyle` |
| 25 | `ImageView` | `android:layout_gravity` | `0x00000010` |
| 26 | `ImageView` | `android:id` | `@id/fbIcon` |
| 27 | `ImageView` | `android:visibility` | `gone` |
| 28 | `ImageView` | `android:layout_width` | `@dimen/fb_icon_size` |
| 29 | `ImageView` | `android:layout_height` | `@dimen/fb_icon_size` |
| 30 | `ImageView` | `android:layout_marginRight` | `@dimen/fb_margin_right_icon` |
| 31 | `ImageView` | `android:src` | `@drawable/ic_info` |
| 32 | `ImageView` | `android:tint` | `@color/white` |
| 33 | `ImageView` | `android:layout_marginEnd` | `@dimen/fb_margin_right_icon` |
| 34 | `LinearLayout` | `android:orientation` | `vertical` |
| 35 | `LinearLayout` | `android:layout_width` | `0.000000dip` |
| 36 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 37 | `LinearLayout` | `android:layout_weight` | `8.000000` |
| 38 | `TextView` | `android:textAppearance` | `@style/FbTitleTextStyle` |
| 39 | `TextView` | `android:id` | `@id/fbTitle` |
| 40 | `TextView` | `android:visibility` | `gone` |
| 41 | `TextView` | `android:layout_width` | `wrap_content` |
| 42 | `TextView` | `android:layout_height` | `wrap_content` |
| 43 | `TextView` | `android:layout_marginBottom` | `@dimen/fb_title_message_margin` |
| 44 | `TextView` | `android:textAppearance` | `@style/FbMessageStyle` |
| 45 | `TextView` | `android:id` | `@id/fbMessage` |
| 46 | `TextView` | `android:visibility` | `gone` |
| 47 | `TextView` | `android:layout_width` | `wrap_content` |
| 48 | `TextView` | `android:layout_height` | `wrap_content` |
| 49 | `TextView` | `android:layout_marginTop` | `@dimen/fb_title_message_margin` |
| 50 | `TextView` | `android:justificationMode` | `1` |
| 51 | `com.andrognito.flashbar.view.FbButton` | `android:textAppearance` | `@style/FbButtonTextStyle` |
| 52 | `com.andrognito.flashbar.view.FbButton` | `android:id` | `@id/fbPrimaryAction` |
| 53 | `com.andrognito.flashbar.view.FbButton` | `android:visibility` | `gone` |
| 54 | `com.andrognito.flashbar.view.FbButton` | `android:layout_width` | `wrap_content` |
| 55 | `com.andrognito.flashbar.view.FbButton` | `android:layout_height` | `wrap_content` |
| 56 | `com.andrognito.flashbar.view.FbButton` | `style` | `@style/FbButtonStyle` |
| 57 | `com.andrognito.flashbar.view.FbProgress` | `android:layout_gravity` | `0x00000010` |
| 58 | `com.andrognito.flashbar.view.FbProgress` | `android:id` | `@id/fbRightProgress` |
| 59 | `com.andrognito.flashbar.view.FbProgress` | `android:visibility` | `gone` |
| 60 | `com.andrognito.flashbar.view.FbProgress` | `android:layout_width` | `@dimen/fb_progress_size` |
| 61 | `com.andrognito.flashbar.view.FbProgress` | `android:layout_height` | `@dimen/fb_progress_size` |
| 62 | `com.andrognito.flashbar.view.FbProgress` | `android:layout_marginLeft` | `@dimen/fb_margin_progress` |
| 63 | `com.andrognito.flashbar.view.FbProgress` | `android:layout_marginStart` | `@dimen/fb_margin_progress` |
| 64 | `com.andrognito.flashbar.view.FbProgress` | `style` | `@style/FbCircularIndeterminateProgressStyle` |
| 65 | `LinearLayout` | `android:gravity` | `0x00800005` |
| 66 | `LinearLayout` | `android:id` | `@id/fbSecondaryActionContainer` |
| 67 | `LinearLayout` | `android:visibility` | `gone` |
| 68 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 69 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 70 | `LinearLayout` | `android:layout_marginTop` | `@dimen/fb_margin_secondary_action_container` |
| 71 | `com.andrognito.flashbar.view.FbButton` | `android:textAppearance` | `@style/FbButtonTextStyle` |
| 72 | `com.andrognito.flashbar.view.FbButton` | `android:id` | `@id/fbPositiveAction` |
| 73 | `com.andrognito.flashbar.view.FbButton` | `android:visibility` | `gone` |
| 74 | `com.andrognito.flashbar.view.FbButton` | `android:layout_width` | `wrap_content` |
| 75 | `com.andrognito.flashbar.view.FbButton` | `android:layout_height` | `wrap_content` |
| 76 | `com.andrognito.flashbar.view.FbButton` | `style` | `@style/FbButtonStyle` |
| 77 | `com.andrognito.flashbar.view.FbButton` | `android:textAppearance` | `@style/FbButtonTextStyle` |
| 78 | `com.andrognito.flashbar.view.FbButton` | `android:id` | `@id/fbNegativeAction` |
| 79 | `com.andrognito.flashbar.view.FbButton` | `android:visibility` | `gone` |
| 80 | `com.andrognito.flashbar.view.FbButton` | `android:layout_width` | `wrap_content` |
| 81 | `com.andrognito.flashbar.view.FbButton` | `android:layout_height` | `wrap_content` |
| 82 | `com.andrognito.flashbar.view.FbButton` | `android:layout_marginLeft` | `12.000000dip` |
| 83 | `com.andrognito.flashbar.view.FbButton` | `android:layout_marginStart` | `@dimen/fb_margin_secondary_action` |
| 84 | `com.andrognito.flashbar.view.FbButton` | `style` | `@style/FbButtonStyle` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/warm_grey` | `#FF8E8E8E` |
| `@color/white` | `#FFFFFFFF` |
| `@dimen/fb_content_padding_all` | `16.000000dip` |
| `@dimen/fb_icon_size` | `28.000000dip` |
| `@dimen/fb_margin_progress` | `20.000000dip` |
| `@dimen/fb_margin_right_icon` | `16.000000dip` |
| `@dimen/fb_margin_secondary_action` | `12.000000dip` |
| `@dimen/fb_margin_secondary_action_container` | `12.000000dip` |
| `@dimen/fb_progress_size` | `20.000000dip` |
| `@dimen/fb_title_message_margin` | `2.000000dip` |
| `@style/FbButtonStyle` | `[{'attr': 'android:background', 'attr_id': '0x010100D4', 'value': '@drawable/fb_button_background_selector', 'value_type': 'reference'}, {'attr': 'android:paddingLeft', 'attr_id': '0x010100D6', 'value': '8.000000dip', 'value_type': 'dimension'}, {'attr': 'android:paddingTop', 'attr_id': '0x010100D7', 'value': '4.000000dip', 'value_type': 'dimension'}, {'attr': 'android:paddingRight', 'attr_id': '0x010100D8', 'value': '8.000000dip', 'value_type': 'dimension'}, {'attr': 'android:paddingBottom', 'attr_id': '0x010100D9', 'value': '4.000000dip', 'value_type': 'dimension'}, {'attr': 'android:focusable', 'attr_id': '0x010100DA', 'value': 'true', 'value_type': 'int_boolean'}, {'attr': 'android:clickable', 'attr_id': '0x010100E5', 'value': 'true', 'value_type': 'int_boolean'}]` |
| `@style/FbButtonTextStyle` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '@dimen/fb_button_text_size', 'value_type': 'reference'}, {'attr': 'android:textStyle', 'attr_id': '0x01010097', 'value': '0x00000001', 'value_type': 'int_hex'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/white', 'value_type': 'reference'}]` |
| `@style/FbCircularIndeterminateProgressStyle` | `[{'attr': 'attr.fbp_barColor', 'attr_id': '0x7F04027A', 'value': '@color/white', 'value_type': 'reference'}, {'attr': 'attr.fbp_barWidth', 'attr_id': '0x7F04027C', 'value': '2.000000dip', 'value_type': 'dimension'}, {'attr': 'attr.fbp_progressIndeterminate', 'attr_id': '0x7F040280', 'value': 'true', 'value_type': 'int_boolean'}]` |
| `@style/FbMessageStyle` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '@dimen/fb_message_text_size', 'value_type': 'reference'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/white', 'value_type': 'reference'}]` |
| `@style/FbTitleTextStyle` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '@dimen/fb_title_text_size', 'value_type': 'reference'}, {'attr': 'android:textStyle', 'attr_id': '0x01010097', 'value': '0x00000001', 'value_type': 'int_hex'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/white', 'value_type': 'reference'}]` |

## ۴. شناسه‌های `@id`

```text
@id/fbContent
@id/fbIcon
@id/fbLeftProgress
@id/fbMessage
@id/fbNegativeAction
@id/fbPositiveAction
@id/fbPrimaryAction
@id/fbRightProgress
@id/fbRoot
@id/fbSecondaryActionContainer
@id/fbTitle
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:id="@id/fbRoot" android:background="@color/warm_grey" android:padding="@dimen/fb_content_padding_all" android:focusable="true" android:clickable="true" android:layout_width="match_parent" android:layout_height="wrap_content" android:foreground="?0x0101030E">
  <LinearLayout android:orientation="vertical" android:id="@id/fbContent" android:layout_width="match_parent" android:layout_height="wrap_content">
    <LinearLayout android:gravity="0x00000010" android:layout_width="match_parent" android:layout_height="wrap_content">
      <com.andrognito.flashbar.view.FbProgress android:layout_gravity="0x00000010" android:id="@id/fbLeftProgress" android:visibility="gone" android:layout_width="@dimen/fb_progress_size" android:layout_height="@dimen/fb_progress_size" android:layout_marginRight="@dimen/fb_margin_progress" android:layout_marginEnd="@dimen/fb_margin_progress" style="@style/FbCircularIndeterminateProgressStyle"/>
      <ImageView android:layout_gravity="0x00000010" android:id="@id/fbIcon" android:visibility="gone" android:layout_width="@dimen/fb_icon_size" android:layout_height="@dimen/fb_icon_size" android:layout_marginRight="@dimen/fb_margin_right_icon" android:src="@drawable/ic_info" android:tint="@color/white" android:layout_marginEnd="@dimen/fb_margin_right_icon"/>
      <LinearLayout android:orientation="vertical" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:layout_weight="8.000000">
        <TextView android:textAppearance="@style/FbTitleTextStyle" android:id="@id/fbTitle" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginBottom="@dimen/fb_title_message_margin"/>
        <TextView android:textAppearance="@style/FbMessageStyle" android:id="@id/fbMessage" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginTop="@dimen/fb_title_message_margin" android:justificationMode="1"/>
      </LinearLayout>
      <com.andrognito.flashbar.view.FbButton android:textAppearance="@style/FbButtonTextStyle" android:id="@id/fbPrimaryAction" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" style="@style/FbButtonStyle"/>
      <com.andrognito.flashbar.view.FbProgress android:layout_gravity="0x00000010" android:id="@id/fbRightProgress" android:visibility="gone" android:layout_width="@dimen/fb_progress_size" android:layout_height="@dimen/fb_progress_size" android:layout_marginLeft="@dimen/fb_margin_progress" android:layout_marginStart="@dimen/fb_margin_progress" style="@style/FbCircularIndeterminateProgressStyle"/>
    </LinearLayout>
    <LinearLayout android:gravity="0x00800005" android:id="@id/fbSecondaryActionContainer" android:visibility="gone" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/fb_margin_secondary_action_container">
      <com.andrognito.flashbar.view.FbButton android:textAppearance="@style/FbButtonTextStyle" android:id="@id/fbPositiveAction" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" style="@style/FbButtonStyle"/>
      <com.andrognito.flashbar.view.FbButton android:textAppearance="@style/FbButtonTextStyle" android:id="@id/fbNegativeAction" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginLeft="12.000000dip" android:layout_marginStart="@dimen/fb_margin_secondary_action" style="@style/FbButtonStyle"/>
    </LinearLayout>
  </LinearLayout>
</LinearLayout>
```
