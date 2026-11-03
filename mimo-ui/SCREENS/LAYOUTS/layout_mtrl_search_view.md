# پروندهٔ لایه — `res/layout/mtrl_search_view.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/mtrl_search_view.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/mtrl_search_view.xml`](../../SOURCE/res/layout/mtrl_search_view.xml) |
| SHA-256 دیکد | `cad10dc4671eb52d8642a7a9c1b31dd58164026dfbfe7bb7b322cf356c2c0c55` |
| ریشه | `merge` |
| تعداد گره | 16 |
| تعداد شناسه | 15 |
| تگ‌های استفاده‌شده | 10 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 26 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ merge
   ├─ View  #@id/open_search_view_scrim
   └─ com.google.android.material.internal.ClippableRoundedCornerLayout  #@id/open_search_view_root
      └─ LinearLayout  #@id/open_search_view_background
         ├─ View  #@id/open_search_view_status_bar_spacer
         ├─ FrameLayout  #@id/open_search_view_header_container
         ├─ FrameLayout  #@id/open_search_view_toolbar_container
         │  ├─ com.google.android.material.appbar.MaterialToolbar  #@id/open_search_view_dummy_toolbar
         │  │  └─ TextView  #@id/open_search_view_dummy_text_view
         │  └─ com.google.android.material.appbar.MaterialToolbar  #@id/open_search_view_toolbar
         │     └─ LinearLayout  #@id/open_search_view_text_container
         │        ├─ TextView  #@id/open_search_view_search_prefix
         │        ├─ EditText  #@id/open_search_view_edit_text
         │        └─ ImageButton  #@id/open_search_view_clear_button
         ├─ View  #@id/open_search_view_divider
         └─ com.google.android.material.internal.TouchObserverFrameLayout  #@id/open_search_view_content_container
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `View` | `android:id` | `@id/open_search_view_scrim` |
| 2 | `View` | `android:background` | `?attr/scrimBackground` |
| 3 | `View` | `android:layout_width` | `match_parent` |
| 4 | `View` | `android:layout_height` | `match_parent` |
| 5 | `View` | `android:alpha` | `0.000000` |
| 6 | `com.google.android.material.internal.ClippableRoundedCornerLayout` | `android:id` | `@id/open_search_view_root` |
| 7 | `com.google.android.material.internal.ClippableRoundedCornerLayout` | `android:visibility` | `gone` |
| 8 | `com.google.android.material.internal.ClippableRoundedCornerLayout` | `android:layout_width` | `match_parent` |
| 9 | `com.google.android.material.internal.ClippableRoundedCornerLayout` | `android:layout_height` | `match_parent` |
| 10 | `com.google.android.material.internal.ClippableRoundedCornerLayout` | `android:touchscreenBlocksFocus` | `true` |
| 11 | `com.google.android.material.internal.ClippableRoundedCornerLayout` | `android:keyboardNavigationCluster` | `true` |
| 12 | `LinearLayout` | `android:orientation` | `vertical` |
| 13 | `LinearLayout` | `android:id` | `@id/open_search_view_background` |
| 14 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 15 | `LinearLayout` | `android:layout_height` | `match_parent` |
| 16 | `View` | `android:id` | `@id/open_search_view_status_bar_spacer` |
| 17 | `View` | `android:visibility` | `gone` |
| 18 | `View` | `android:layout_width` | `match_parent` |
| 19 | `View` | `android:layout_height` | `wrap_content` |
| 20 | `FrameLayout` | `android:id` | `@id/open_search_view_header_container` |
| 21 | `FrameLayout` | `android:visibility` | `gone` |
| 22 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 23 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 24 | `FrameLayout` | `android:id` | `@id/open_search_view_toolbar_container` |
| 25 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 26 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 27 | `com.google.android.material.appbar.MaterialToolbar` | `android:layout_gravity` | `0x00800005` |
| 28 | `com.google.android.material.appbar.MaterialToolbar` | `android:id` | `@id/open_search_view_dummy_toolbar` |
| 29 | `com.google.android.material.appbar.MaterialToolbar` | `android:visibility` | `gone` |
| 30 | `com.google.android.material.appbar.MaterialToolbar` | `android:layout_width` | `wrap_content` |
| 31 | `com.google.android.material.appbar.MaterialToolbar` | `android:layout_height` | `wrap_content` |
| 32 | `com.google.android.material.appbar.MaterialToolbar` | `app:navigationIcon` | `@null` |
| 33 | `com.google.android.material.appbar.MaterialToolbar` | `style` | `?attr/materialSearchViewToolbarStyle` |
| 34 | `TextView` | `android:ellipsize` | `end` |
| 35 | `TextView` | `android:id` | `@id/open_search_view_dummy_text_view` |
| 36 | `TextView` | `android:visibility` | `gone` |
| 37 | `TextView` | `android:layout_width` | `wrap_content` |
| 38 | `TextView` | `android:layout_height` | `wrap_content` |
| 39 | `TextView` | `android:maxLines` | `1` |
| 40 | `TextView` | `android:importantForAccessibility` | `no` |
| 41 | `com.google.android.material.appbar.MaterialToolbar` | `android:id` | `@id/open_search_view_toolbar` |
| 42 | `com.google.android.material.appbar.MaterialToolbar` | `android:clipChildren` | `false` |
| 43 | `com.google.android.material.appbar.MaterialToolbar` | `android:layout_width` | `match_parent` |
| 44 | `com.google.android.material.appbar.MaterialToolbar` | `android:layout_height` | `wrap_content` |
| 45 | `com.google.android.material.appbar.MaterialToolbar` | `app:navigationContentDescription` | `@string/searchview_navigation_content_description` |
| 46 | `com.google.android.material.appbar.MaterialToolbar` | `style` | `?attr/materialSearchViewToolbarStyle` |
| 47 | `LinearLayout` | `android:gravity` | `0x00000010` |
| 48 | `LinearLayout` | `android:orientation` | `horizontal` |
| 49 | `LinearLayout` | `android:id` | `@id/open_search_view_text_container` |
| 50 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 51 | `LinearLayout` | `android:layout_height` | `?attr/materialSearchViewToolbarHeight` |
| 52 | `TextView` | `android:id` | `@id/open_search_view_search_prefix` |
| 53 | `TextView` | `android:visibility` | `gone` |
| 54 | `TextView` | `android:layout_width` | `wrap_content` |
| 55 | `TextView` | `android:layout_height` | `wrap_content` |
| 56 | `TextView` | `style` | `?attr/materialSearchViewPrefixStyle` |
| 57 | `EditText` | `android:id` | `@id/open_search_view_edit_text` |
| 58 | `EditText` | `android:background` | `@null` |
| 59 | `EditText` | `android:layout_width` | `0.000000dip` |
| 60 | `EditText` | `android:layout_height` | `match_parent` |
| 61 | `EditText` | `android:layout_weight` | `1.000000` |
| 62 | `EditText` | `android:inputType` | `0x00080001` |
| 63 | `EditText` | `android:imeOptions` | `0x10000003` |
| 64 | `EditText` | `android:textDirection` | `firstStrong` |
| 65 | `EditText` | `android:importantForAutofill` | `0x00000002` |
| 66 | `ImageButton` | `android:id` | `@id/open_search_view_clear_button` |
| 67 | `ImageButton` | `android:background` | `?attr/actionBarItemBackground` |
| 68 | `ImageButton` | `android:padding` | `16.000000dip` |
| 69 | `ImageButton` | `android:visibility` | `gone` |
| 70 | `ImageButton` | `android:layout_width` | `wrap_content` |
| 71 | `ImageButton` | `android:layout_height` | `wrap_content` |
| 72 | `ImageButton` | `android:contentDescription` | `@string/searchview_clear_text_content_description` |
| 73 | `ImageButton` | `app:srcCompat` | `@drawable/ic_clear_black_24` |
| 74 | `View` | `android:id` | `@id/open_search_view_divider` |
| 75 | `View` | `android:background` | `?attr/colorOutline` |
| 76 | `View` | `android:layout_width` | `match_parent` |
| 77 | `View` | `android:layout_height` | `@dimen/m3_searchview_divider_size` |
| 78 | `com.google.android.material.internal.TouchObserverFrameLayout` | `android:id` | `@id/open_search_view_content_container` |
| 79 | `com.google.android.material.internal.TouchObserverFrameLayout` | `android:layout_width` | `match_parent` |
| 80 | `com.google.android.material.internal.TouchObserverFrameLayout` | `android:layout_height` | `match_parent` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@dimen/m3_searchview_divider_size` | `1.000000dip` |
| `@string/searchview_clear_text_content_description` | `Clear text` / `Vee teks uit` (af) / `ጽሁፍን አጽዳ` (am) / `محو النص` (ar) / `Clear text` (as) / `Mətni təmizləyin` (az) / `Ачысціць тэкст` (be) / `Изчистване на текста` (bg) / `টেক্সট মুছুন` (bn) / `Brisanje teksta` (bs) / `Esborra el text` (ca) / `Vymazat text` (cs) / `Ryd tekst` (da) / `Text löschen` (de) / `Διαγραφή κειμένου` (el) / `Clear text` (en-rGB) / `Borrar texto` (es) / `Borrar texto` (es-r419) / `Borrar texto` (es-rUS) / `Teksti kustutamine` (et) / `Garbitu testua` (eu) / `پاک کردن نوشتار` (fa) / `Tyhjennä teksti` (fi) / `Effacer le texte` (fr) / `Effacez le texte` (fr-rCA) / `Borrar texto` (gl) / `ટેક્સ્ટ સાફ કરો` (gu) / `टेक्स्ट मिटाएं` (hi) / `Ukloni tekst` (hr) / `Szöveg törlése` (hu) / `Ջնջել տեքստը` (hy) / `Hapus teks` (in) / `Hreinsa texta` (is) / `Cancella testo` (it) / `מחיקת הטקסט` (iw) / `テキストを消去` (ja) / `ტექსტის გასუფთავება` (ka) / `Мәтінді өшіру` (kk) / `សម្អាតអក្សរ` (km) / `ಪಠ್ಯವನ್ನು ತೆರವುಗೊಳಿಸಿ` (kn) / `텍스트 삭제` (ko) / `Текстти тазалоо` (ky) / `ລຶບລ້າງຂໍ້ຄວາມ` (lo) / `Išvalyti tekstą` (lt) / `Notīrīt tekstu` (lv) / `Бришење на текстот` (mk) / `ടെക്‌സ്‌റ്റ് മായ്‌ക്കുക` (ml) / `Текстийг арилгах` (mn) / `मजकूर साफ करा` (mr) / `Kosongkan teks` (ms) / `စာသား ဖယ်ရှားရန်` (my) / `Fjern teksten` (nb) / `टेक्स्ट हटाउनुहोस्` (ne) / `Tekst wissen` (nl) / `Clear text` (or) / `ਲਿਖਤ ਕਲੀਅਰ ਕਰੋ` (pa) / `Wyczyść tekst` (pl) / `Limpar texto` (pt-rBR) / `Limpar texto` (pt-rPT) / `Ștergeți textul` (ro) / `Очистить текстовое поле` (ru) / `පෙළ හිස් කරන්න` (si) / `Vymazať text` (sk) / `Počisti besedilo` (sl) / `Pastro tekstin` (sq) / `Обриши текст` (sr) / `Rensa text` (sv) / `Futa maandishi` (sw) / `வார்த்தைகளை அழிக்கும்` (ta) / `టెక్స్ట్‌ను క్లియర్ చేయండి` (te) / `ล้างข้อความ` (th) / `I-clear ang text` (tl) / `Metni temizle` (tr) / `Видалити текст` (uk) / `ٹیکسٹ صاف کریں` (ur) / `Matnni tozalash` (uz) / `Xoá văn bản` (vi) / `清除文字` (zh-rCN) / `清除文字` (zh-rHK) / `清除文字` (zh-rTW) / `Sula umbhalo` (zu) |
| `@string/searchview_navigation_content_description` | `Back` / `Terug` (af) / `ተመለስ` (am) / `رجوع` (ar) / `Back` (as) / `Geri` (az) / `Назад` (be) / `Назад` (bg) / `ফিরে যান` (bn) / `Nazad` (bs) / `Enrere` (ca) / `Zpět` (cs) / `Tilbage` (da) / `Zurück` (de) / `Πίσω` (el) / `Back` (en-rGB) / `Atrás` (es) / `Atrás` (es-r419) / `Atrás` (es-rUS) / `Tagasi` (et) / `Atzera` (eu) / `برگشتن` (fa) / `Takaisin` (fi) / `Retour` (fr) / `Retour` (fr-rCA) / `Anterior` (gl) / `પાછળ` (gu) / `वापस जाएं` (hi) / `Natrag` (hr) / `Vissza` (hu) / `Հետ` (hy) / `Kembali` (in) / `Til baka` (is) / `Indietro` (it) / `חזרה` (iw) / `戻る` (ja) / `უკან` (ka) / `Артқа` (kk) / `ថយក្រោយ` (km) / `ಹಿಂದಕ್ಕೆ` (kn) / `뒤로` (ko) / `Артка` (ky) / `ກັບຄືນ` (lo) / `Atgal` (lt) / `Atpakaļ` (lv) / `Враќање назад` (mk) / `മടങ്ങുക` (ml) / `Буцах` (mn) / `मागे जा` (mr) / `Kembali` (ms) / `နောက်သို့` (my) / `Tilbake` (nb) / `पछाडि` (ne) / `Terug` (nl) / `Back` (or) / `ਪਿੱਛੇ` (pa) / `Wstecz` (pl) / `Voltar` (pt-rBR) / `Anterior` (pt-rPT) / `Înapoi` (ro) / `Назад` (ru) / `ආපසු` (si) / `Späť` (sk) / `Nazaj` (sl) / `Pas` (sq) / `Назад` (sr) / `Tillbaka` (sv) / `Rudi nyuma` (sw) / `பின்செல்லும்` (ta) / `వెనుకకు` (te) / `กลับ` (th) / `Bumalik` (tl) / `Geri` (tr) / `Назад` (uk) / `واپس جائیں` (ur) / `Orqaga` (uz) / `Quay lại` (vi) / `返回` (zh-rCN) / `返回` (zh-rHK) / `返回` (zh-rTW) / `Emuva` (zu) |

## ۴. شناسه‌های `@id`

```text
@id/open_search_view_background
@id/open_search_view_clear_button
@id/open_search_view_content_container
@id/open_search_view_divider
@id/open_search_view_dummy_text_view
@id/open_search_view_dummy_toolbar
@id/open_search_view_edit_text
@id/open_search_view_header_container
@id/open_search_view_root
@id/open_search_view_scrim
@id/open_search_view_search_prefix
@id/open_search_view_status_bar_spacer
@id/open_search_view_text_container
@id/open_search_view_toolbar
@id/open_search_view_toolbar_container
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
<merge xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto">
  <View android:id="@id/open_search_view_scrim" android:background="?attr/scrimBackground" android:layout_width="match_parent" android:layout_height="match_parent" android:alpha="0.000000"/>
  <com.google.android.material.internal.ClippableRoundedCornerLayout android:id="@id/open_search_view_root" android:visibility="gone" android:layout_width="match_parent" android:layout_height="match_parent" android:touchscreenBlocksFocus="true" android:keyboardNavigationCluster="true">
    <LinearLayout android:orientation="vertical" android:id="@id/open_search_view_background" android:layout_width="match_parent" android:layout_height="match_parent">
      <View android:id="@id/open_search_view_status_bar_spacer" android:visibility="gone" android:layout_width="match_parent" android:layout_height="wrap_content"/>
      <FrameLayout android:id="@id/open_search_view_header_container" android:visibility="gone" android:layout_width="match_parent" android:layout_height="wrap_content"/>
      <FrameLayout android:id="@id/open_search_view_toolbar_container" android:layout_width="match_parent" android:layout_height="wrap_content">
        <com.google.android.material.appbar.MaterialToolbar android:layout_gravity="0x00800005" android:id="@id/open_search_view_dummy_toolbar" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" app:navigationIcon="@null" style="?attr/materialSearchViewToolbarStyle">
          <TextView android:ellipsize="end" android:id="@id/open_search_view_dummy_text_view" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:maxLines="1" android:importantForAccessibility="no"/>
        </com.google.android.material.appbar.MaterialToolbar>
        <com.google.android.material.appbar.MaterialToolbar android:id="@id/open_search_view_toolbar" android:clipChildren="false" android:layout_width="match_parent" android:layout_height="wrap_content" app:navigationContentDescription="@string/searchview_navigation_content_description" style="?attr/materialSearchViewToolbarStyle">
          <LinearLayout android:gravity="0x00000010" android:orientation="horizontal" android:id="@id/open_search_view_text_container" android:layout_width="match_parent" android:layout_height="?attr/materialSearchViewToolbarHeight">
            <TextView android:id="@id/open_search_view_search_prefix" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" style="?attr/materialSearchViewPrefixStyle"/>
            <EditText android:id="@id/open_search_view_edit_text" android:background="@null" android:layout_width="0.000000dip" android:layout_height="match_parent" android:layout_weight="1.000000" android:inputType="0x00080001" android:imeOptions="0x10000003" android:textDirection="firstStrong" android:importantForAutofill="0x00000002"/>
            <ImageButton android:id="@id/open_search_view_clear_button" android:background="?attr/actionBarItemBackground" android:padding="16.000000dip" android:visibility="gone" android:layout_width="wrap_content" android:layout_height="wrap_content" android:contentDescription="@string/searchview_clear_text_content_description" app:srcCompat="@drawable/ic_clear_black_24"/>
          </LinearLayout>
        </com.google.android.material.appbar.MaterialToolbar>
      </FrameLayout>
      <View android:id="@id/open_search_view_divider" android:background="?attr/colorOutline" android:layout_width="match_parent" android:layout_height="@dimen/m3_searchview_divider_size"/>
      <com.google.android.material.internal.TouchObserverFrameLayout android:id="@id/open_search_view_content_container" android:layout_width="match_parent" android:layout_height="match_parent"/>
    </LinearLayout>
  </com.google.android.material.internal.ClippableRoundedCornerLayout>
</merge>
```
