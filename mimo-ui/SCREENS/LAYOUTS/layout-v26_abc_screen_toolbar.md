# پروندهٔ لایه — `res/layout-v26/abc_screen_toolbar.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-v26/abc_screen_toolbar.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-v26/abc_screen_toolbar.xml`](../../SOURCE/res/layout-v26/abc_screen_toolbar.xml) |
| SHA-256 دیکد | `91b79d225f1c12ab0737c3ccd9f0c6c790ad2ce7f6f898eee8aadeea37dcb36d` |
| ریشه | `androidx.appcompat.widget.ActionBarOverlayLayout` |
| تعداد گره | 5 |
| تعداد شناسه | 4 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 1 |
| ارجاع به منابع | 10 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.appcompat.widget.ActionBarOverlayLayout  #@id/decor_content_parent
   ├─ include
   └─ androidx.appcompat.widget.ActionBarContainer  #@id/action_bar_container
      ├─ androidx.appcompat.widget.Toolbar  #@id/action_bar
      └─ androidx.appcompat.widget.ActionBarContextView  #@id/action_context_bar
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.appcompat.widget.ActionBarOverlayLayout` | `android:id` | `@id/decor_content_parent` |
| 2 | `androidx.appcompat.widget.ActionBarOverlayLayout` | `android:fitsSystemWindows` | `true` |
| 3 | `androidx.appcompat.widget.ActionBarOverlayLayout` | `android:layout_width` | `match_parent` |
| 4 | `androidx.appcompat.widget.ActionBarOverlayLayout` | `android:layout_height` | `match_parent` |
| 5 | `include` | `layout` | `@layout/abc_screen_content_include` |
| 6 | `androidx.appcompat.widget.ActionBarContainer` | `android:gravity` | `0x00000030` |
| 7 | `androidx.appcompat.widget.ActionBarContainer` | `android:id` | `@id/action_bar_container` |
| 8 | `androidx.appcompat.widget.ActionBarContainer` | `android:layout_width` | `match_parent` |
| 9 | `androidx.appcompat.widget.ActionBarContainer` | `android:layout_height` | `wrap_content` |
| 10 | `androidx.appcompat.widget.ActionBarContainer` | `android:layout_alignParentTop` | `true` |
| 11 | `androidx.appcompat.widget.ActionBarContainer` | `android:touchscreenBlocksFocus` | `true` |
| 12 | `androidx.appcompat.widget.ActionBarContainer` | `android:keyboardNavigationCluster` | `true` |
| 13 | `androidx.appcompat.widget.ActionBarContainer` | `style` | `?attr/actionBarStyle` |
| 14 | `androidx.appcompat.widget.Toolbar` | `android:id` | `@id/action_bar` |
| 15 | `androidx.appcompat.widget.Toolbar` | `android:layout_width` | `match_parent` |
| 16 | `androidx.appcompat.widget.Toolbar` | `android:layout_height` | `wrap_content` |
| 17 | `androidx.appcompat.widget.Toolbar` | `app:navigationContentDescription` | `@string/abc_action_bar_up_description` |
| 18 | `androidx.appcompat.widget.Toolbar` | `style` | `?attr/toolbarStyle` |
| 19 | `androidx.appcompat.widget.ActionBarContextView` | `android:theme` | `?attr/actionModeTheme` |
| 20 | `androidx.appcompat.widget.ActionBarContextView` | `android:id` | `@id/action_context_bar` |
| 21 | `androidx.appcompat.widget.ActionBarContextView` | `android:visibility` | `gone` |
| 22 | `androidx.appcompat.widget.ActionBarContextView` | `android:layout_width` | `match_parent` |
| 23 | `androidx.appcompat.widget.ActionBarContextView` | `android:layout_height` | `wrap_content` |
| 24 | `androidx.appcompat.widget.ActionBarContextView` | `style` | `?attr/actionModeStyle` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@string/abc_action_bar_up_description` | `Navigate up` / `Gaan op` (af) / `ወደ ላይ ያስሱ` (am) / `التنقل إلى أعلى` (ar) / `ওপৰলৈ যাওক` (as) / `Yuxarı keçin` (az) / `Перайсці ўверх` (be) / `Навигиране нагоре` (bg) / `উপরে নেভিগেট করুন` (bn) / `Idi gore` (bs) / `Navega cap amunt` (ca) / `Přejít nahoru` (cs) / `Gå op` (da) / `Nach oben` (de) / `Πλοήγηση προς τα επάνω` (el) / `Navigate up` (en-rAU) / `Navigate up` (en-rCA) / `Navigate up` (en-rGB) / `Navigate up` (en-rIN) / `‎‏‎‎‎‎‎‏‎‏‏‏‎‎‎‎‎‎‏‎‎‏‎‎‎‎‏‏‏‏‏‏‏‏‏‏‎‏‎‎‎‏‏‎‏‎‎‎‏‏‎‎‎‏‏‏‏‎‏‎‎‎‎‏‏‎‏‏‎‏‎‎‏‎‎‏‎‎‎‎‎‎‏‎‏‎‎‎‎‏‏‏‎‎‎‎‎Navigate up‎‏‎‎‏‎` (en-rXC) / `Desplazarse hacia arriba` (es) / `Navegar hacia arriba` (es-rUS) / `Liigu üles` (et) / `Joan gora` (eu) / `رفتن به بالا` (fa) / `Siirry ylös` (fi) / `Revenir en haut de la page` (fr) / `Revenir en arrière` (fr-rCA) / `Vai cara arriba` (gl) / `ઉપર નૅવિગેટ કરો` (gu) / `वापस जाएं` (hi) / `Natrag` (hr) / `Fel` (hu) / `Անցնել վերև` (hy) / `Kembali ke atas` (in) / `Fara upp` (is) / `Torna indietro` (it) / `ניווט למעלה` (iw) / `前に戻る` (ja) / `ზემოთ გადასვლა` (ka) / `Жоғары қарай өту` (kk) / `រំកិលឡើងលើ` (km) / `ಮೇಲಕ್ಕೆ ನ್ಯಾವಿಗೇಟ್ ಮಾಡಿ` (kn) / `위로 이동` (ko) / `Мурунку экранга өтүү` (ky) / `ເລື່ອນຂຶ້ນເທິງ` (lo) / `Naršyti aukštyn` (lt) / `Pārvietoties uz augšu` (lv) / `Движи се нагоре` (mk) / `മുകളിലേക്ക് പോവുക` (ml) / `Дээш шилжих` (mn) / `वर नेव्‍हिगेट करा` (mr) / `Navigasi ke atas` (ms) / `အပေါ်သို့ ရွှေ့ရန်` (my) / `Gå opp` (nb) / `माथि नेभिगेट गर्नुहोस्` (ne) / `Omhoog navigeren` (nl) / `ଉପରକୁ ନେଭିଗେଟ୍ କରନ୍ତୁ` (or) / `ਉੱਪਰ ਜਾਓ` (pa) / `Przejdź wyżej` (pl) / `Navegar para cima` (pt) / `Navegar para cima` (pt-rBR) / `Navegar para cima` (pt-rPT) / `Navighează în sus` (ro) / `Перейти вверх` (ru) / `ඉහළට සංචාලනය කරන්න` (si) / `Prejsť nahor` (sk) / `Pomik navzgor` (sl) / `Ngjitu lart` (sq) / `Идите нагоре` (sr) / `Navigera uppåt` (sv) / `Sogeza juu` (sw) / `மேலே செல்லும்` (ta) / `పైకి నావిగేట్ చేస్తుంది` (te) / `กลับ` (th) / `Mag-navigate pataas` (tl) / `Yukarı git` (tr) / `Перейти вгору` (uk) / `اوپر نیویگیٹ کریں` (ur) / `Yopish` (uz) / `Di chuyển lên` (vi) / `转到上一层级` (zh-rCN) / `向上瀏覽` (zh-rHK) / `向上瀏覽` (zh-rTW) / `Zulazulela phezulu` (zu) |

## ۴. شناسه‌های `@id`

```text
@id/action_bar
@id/action_bar_container
@id/action_context_bar
@id/decor_content_parent
```

## ۵. ارجاع به لایه‌های دیگر

```text
@layout/abc_screen_content_include
```

## ۶. صفحاتی که از این لایه استفاده می‌کنند

(هیچ صفحهٔ نام‌برداری به این لایه متصل نشد؛ ممکن است لایهٔ کتابخانه/`<include>` باشد)

## ۷. لایه‌هایی که این لایه را include می‌کنند

(none)

## ۸. کد XML کامل (همانطور که در APK نوشته شده)

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.appcompat.widget.ActionBarOverlayLayout xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:id="@id/decor_content_parent" android:fitsSystemWindows="true" android:layout_width="match_parent" android:layout_height="match_parent">
  <include layout="@layout/abc_screen_content_include"/>
  <androidx.appcompat.widget.ActionBarContainer android:gravity="0x00000030" android:id="@id/action_bar_container" android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_alignParentTop="true" android:touchscreenBlocksFocus="true" android:keyboardNavigationCluster="true" style="?attr/actionBarStyle">
    <androidx.appcompat.widget.Toolbar android:id="@id/action_bar" android:layout_width="match_parent" android:layout_height="wrap_content" app:navigationContentDescription="@string/abc_action_bar_up_description" style="?attr/toolbarStyle"/>
    <androidx.appcompat.widget.ActionBarContextView android:theme="?attr/actionModeTheme" android:id="@id/action_context_bar" android:visibility="gone" android:layout_width="match_parent" android:layout_height="wrap_content" style="?attr/actionModeStyle"/>
  </androidx.appcompat.widget.ActionBarContainer>
</androidx.appcompat.widget.ActionBarOverlayLayout>
```
