# پروندهٔ لایه — `res/layout/profile_friends_empty.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/profile_friends_empty.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/profile_friends_empty.xml`](../../SOURCE/res/layout/profile_friends_empty.xml) |
| SHA-256 دیکد | `78092d6c60ceef1cfc70a757242a961619d287709b18a649ae1e45b76e28a918` |
| ریشه | `LinearLayout` |
| تعداد گره | 4 |
| تعداد شناسه | 0 |
| تگ‌های استفاده‌شده | 3 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 15 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ ImageView
   ├─ TextView
   └─ TextView
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:background` | `@drawable/dotted_border_background` |
| 3 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 4 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 5 | `LinearLayout` | `android:layout_marginTop` | `@dimen/spacing_xxs` |
| 6 | `LinearLayout` | `android:layout_marginBottom` | `@dimen/spacing_s` |
| 7 | `LinearLayout` | `android:foreground` | `?attr/selectableItemBackgroundBorderless` |
| 8 | `LinearLayout` | `android:layout_marginHorizontal` | `@dimen/spacing_m` |
| 9 | `ImageView` | `android:layout_gravity` | `0x00000001` |
| 10 | `ImageView` | `android:layout_width` | `wrap_content` |
| 11 | `ImageView` | `android:layout_height` | `72.000000dip` |
| 12 | `ImageView` | `android:layout_marginTop` | `@dimen/spacing_l` |
| 13 | `ImageView` | `android:src` | `@drawable/ic_invite_friends_accepted_pro` |
| 14 | `TextView` | `android:textColor` | `@color/text_primary` |
| 15 | `TextView` | `android:gravity` | `0x00000001` |
| 16 | `TextView` | `android:layout_width` | `match_parent` |
| 17 | `TextView` | `android:layout_height` | `wrap_content` |
| 18 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_m` |
| 19 | `TextView` | `android:text` | `@string/friends_title_empty_header` |
| 20 | `TextView` | `style` | `@style/TextH3` |
| 21 | `TextView` | `android:textColor` | `@color/text_weak` |
| 22 | `TextView` | `android:gravity` | `0x00000001` |
| 23 | `TextView` | `android:layout_gravity` | `0x00000001` |
| 24 | `TextView` | `android:layout_width` | `wrap_content` |
| 25 | `TextView` | `android:layout_height` | `wrap_content` |
| 26 | `TextView` | `android:layout_marginLeft` | `@dimen/spacing_xl` |
| 27 | `TextView` | `android:layout_marginTop` | `@dimen/spacing_xs` |
| 28 | `TextView` | `android:layout_marginRight` | `@dimen/spacing_xl` |
| 29 | `TextView` | `android:layout_marginBottom` | `@dimen/spacing_m` |
| 30 | `TextView` | `android:text` | `@string/friends_profile_empty` |
| 31 | `TextView` | `style` | `@style/TextP2` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/text_primary` | `#FF252746` / `#FFFFFFFF` (night) |
| `@color/text_weak` | `#FF4A4D85` / `#CCFFFFFF` (night) |
| `@dimen/spacing_l` | `24.000000dip` |
| `@dimen/spacing_m` | `16.000000dip` |
| `@dimen/spacing_s` | `12.000000dip` |
| `@dimen/spacing_xl` | `32.000000dip` |
| `@dimen/spacing_xs` | `8.000000dip` |
| `@dimen/spacing_xxs` | `4.000000dip` |
| `@string/friends_profile_empty` | `Learning is even more fun if you do it together with your friends` / `Lernen macht gemeinsam mit deinen Freunden noch mehr Spaß` (de) / `Aprender es más divertido si lo haces con tu círculo de amistades` (es) / `L'apprentissage est encore plus amusant si tu le fais avec tes amis` (fr) / `Belajar makin seru kalau kamu lakukan bareng teman-temanmu` (in) / `Imparare è ancora più divertente insieme agli amici` (it) / `Nauka jest jeszcze przyjemniejsza razem ze znajomymi` (pl) / `Aprender é ainda mais divertido se você fizer isso junto com seus amigos` (pt-rBR) / `Учиться еще веселее, если ты делаешь это вместе с друзьями` (ru) / `Arkadaşlarınla birlikte öğrenmek çok daha eğlenceli` (tr) |
| `@string/friends_title_empty_header` | `No friends yet` / `Noch keine Freunde` (de) / `Aún sin amigos/as` (es) / `Pas encore d'amis` (fr) / `Belum ada teman` (in) / `Ancora nessun amico` (it) / `Brak znajomych` (pl) / `Nenhum amigo ainda` (pt-rBR) / `Пока нет друзей в Mimo` (ru) / `Henüz arkadaş yok` (tr) |
| `@style/TextH3` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '18.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '5.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '23.399996sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '13.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_fono_medium', 'value_type': 'reference'}]` (sw600dp) |
| `@style/TextP2` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '4.000000sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` / `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '20.799990sp', 'value_type': 'dimension'}, {'attr': 'android:lineSpacingExtra', 'attr_id': '0x01010217', 'value': '7.799988sp', 'value_type': 'dimension'}, {'attr': 'attr.fontFamily', 'attr_id': '0x7F0402B7', 'value': '@font/aeonik_pro_regular', 'value_type': 'reference'}]` (sw600dp) |

## ۴. شناسه‌های `@id`

```text
(none)
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:background="@drawable/dotted_border_background" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_xxs" android:layout_marginBottom="@dimen/spacing_s" android:foreground="?attr/selectableItemBackgroundBorderless" android:layout_marginHorizontal="@dimen/spacing_m">
  <ImageView android:layout_gravity="0x00000001" android:layout_width="wrap_content" android:layout_height="72.000000dip" android:layout_marginTop="@dimen/spacing_l" android:src="@drawable/ic_invite_friends_accepted_pro"/>
  <TextView android:textColor="@color/text_primary" android:gravity="0x00000001" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="@dimen/spacing_m" android:text="@string/friends_title_empty_header" style="@style/TextH3"/>
  <TextView android:textColor="@color/text_weak" android:gravity="0x00000001" android:layout_gravity="0x00000001" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_marginLeft="@dimen/spacing_xl" android:layout_marginTop="@dimen/spacing_xs" android:layout_marginRight="@dimen/spacing_xl" android:layout_marginBottom="@dimen/spacing_m" android:text="@string/friends_profile_empty" style="@style/TextP2"/>
</LinearLayout>
```
