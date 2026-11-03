# پروندهٔ لایه — `res/layout/profile_friends_offline.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/profile_friends_offline.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/profile_friends_offline.xml`](../../SOURCE/res/layout/profile_friends_offline.xml) |
| SHA-256 دیکد | `4dc7ced8a3d93715adb47bfc83cd2e8b598f11e7268738cef8e89c74f34b8a15` |
| ریشه | `LinearLayout` |
| تعداد گره | 3 |
| تعداد شناسه | 1 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 11 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ ImageView
   └─ TextView  #@id/layout_saved_code_empty_view_description
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:background` | `@drawable/rounded_background` |
| 3 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 4 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 5 | `LinearLayout` | `android:foreground` | `?attr/selectableItemBackground` |
| 6 | `LinearLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_s` |
| 7 | `ImageView` | `android:layout_gravity` | `0x00000001` |
| 8 | `ImageView` | `android:layout_width` | `20.000000dip` |
| 9 | `ImageView` | `android:layout_height` | `20.000000dip` |
| 10 | `ImageView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 11 | `ImageView` | `android:src` | `@drawable/ic_alert_circle_filled` |
| 12 | `ImageView` | `app:tint` | `@color/icon_weak` |
| 13 | `TextView` | `android:textColor` | `@color/text_weak` |
| 14 | `TextView` | `android:gravity` | `0x00000001` |
| 15 | `TextView` | `android:layout_gravity` | `0x00000001` |
| 16 | `TextView` | `android:id` | `@id/layout_saved_code_empty_view_description` |
| 17 | `TextView` | `android:layout_width` | `wrap_content` |
| 18 | `TextView` | `android:layout_height` | `wrap_content` |
| 19 | `TextView` | `android:layout_marginLeft` | `@dimen/spacing_xl` |
| 20 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_s` |
| 21 | `TextView` | `android:layout_marginRight` | `@dimen/spacing_xl` |
| 22 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_l` |
| 23 | `TextView` | `android:text` | `@string/profile_friends_offline` |
| 24 | `TextView` | `style` | `@style/TextP2` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/icon_weak` | `#FFA3A5C3` / `#80FFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@string/profile_friends_offline` | `Looks like you’re offline. Connect to the internet to see your friends.` / `Scheinbar bist du offline. Verbinde dich mit dem Internet, um deine Freunde zu sehen.` (de) / `Parece que estás offline. Conéctate a internet para ver tu círculo de amistades.` (es) / `Il semble que tu sois hors ligne. Connecte-toi à l'internet pour voir tes amis.` (fr) / `Sepertinya kamu sedang offline. Hubungkan ke internet untuk melihat temanmu.` (in) / `Sembra che tu sia offline. Connettiti a internet per vedere i tuoi amici.` (it) / `Wygląda na to, że jesteś offline. Połącz się z internetem, aby zobaczyć znajomych.` (pl) / `Parece que você está off-line. Conecte-se à internet para ver seus amigos.` (pt-rBR) / `Кажется, ты оффлайн. Подключись к интернету, чтобы просмотреть друзей.` (ru) / `Görünüşe göre çevrimdışısın. Arkadaşlarını görmek için internete bağlan.` (tr) |
| `@style/TextP2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
@id/layout_saved_code_empty_view_description
```

## ۵. ارجاع به لایه‌های دیگر

```text
(none)
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

```text
com.getmimo.ui.profile.main.ProfileFragment
```

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:orientation="vertical" android:background="@drawable/rounded_background" android:layout_width="match_parent" android:layout_height="wrap_content" android:foreground="?attr/selectableItemBackground" android:layout_marginHorizontal="@dimen/spacing_s">
  <ImageView android:layout_gravity="0x00000001" android:layout_width="20.000000dip" android:layout_height="20.000000dip" android:layout_marginTop="@dimen/spacing_l" android:src="@drawable/ic_alert_circle_filled" app:tint="@color/icon_weak"/>
  <TextView android:textColor="@color/text_weak" android:gravity="0x00000001" android:layout_gravity="0x00000001" android:id="@id/layout_saved_code_empty_view_description" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginLeft="@dimen/spacing_xl" android:layout_marginTop="@dimen/spacing_s" android:layout_marginRight="@dimen/spacing_xl" android:layout_marginBottom="@dimen/spacing_l" android:text="@string/profile_friends_offline" style="@style/TextP2"/>
</LinearLayout>
```
