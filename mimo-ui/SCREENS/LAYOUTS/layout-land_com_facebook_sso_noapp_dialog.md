# پروندهٔ لایه — `res/layout-land/com_facebook_sso_noapp_dialog.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout-land/com_facebook_sso_noapp_dialog.xml` |
| فایل دیکدشده | [`SOURCE/res/layout-land/com_facebook_sso_noapp_dialog.xml`](../../SOURCE/res/layout-land/com_facebook_sso_noapp_dialog.xml) |
| SHA-256 دیکد | `d82dbb2b65bc847c40a077021181616f854246f7cb3d888b83147d69f1f32bb3` |
| ریشه | `LinearLayout` |
| تعداد گره | 9 |
| تعداد شناسه | 5 |
| تگ‌های استفاده‌شده | 5 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 19 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ LinearLayout
   ├─ LinearLayout
   │  ├─ ImageView
   │  ├─ TextView  #@id/com_facebook_sso_noapp_title
   │  └─ ImageButton  #@id/com_facebook_sso_noapp_close
   ├─ TextView  #@id/com_facebook_sso_noapp_body
   └─ LinearLayout
      ├─ Button  #@id/com_facebook_sso_noapp_not_now
      └─ Button  #@id/com_facebook_sso_noapp_continue
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `LinearLayout` | `android:orientation` | `vertical` |
| 2 | `LinearLayout` | `android:background` | `@drawable/com_facebook_sso_noapp_background` |
| 3 | `LinearLayout` | `android:paddingBottom` | `24.000000dip` |
| 4 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 5 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 6 | `LinearLayout` | `android:paddingStart` | `24.000000dip` |
| 7 | `LinearLayout` | `android:paddingEnd` | `24.000000dip` |
| 8 | `LinearLayout` | `android:gravity` | `0x00000010` |
| 9 | `LinearLayout` | `android:orientation` | `horizontal` |
| 10 | `LinearLayout` | `android:paddingTop` | `16.000000dip` |
| 11 | `LinearLayout` | `android:paddingBottom` | `12.000000dip` |
| 12 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 13 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 14 | `ImageView` | `android:layout_width` | `24.000000dip` |
| 15 | `ImageView` | `android:layout_height` | `24.000000dip` |
| 16 | `ImageView` | `android:src` | `@drawable/com_facebook_sso_logo` |
| 17 | `ImageView` | `android:contentDescription` | `@string/com_facebook_loginview_log_in_button_long` |
| 18 | `TextView` | `android:textSize` | `17.000000sp` |
| 19 | `TextView` | `android:textColor` | `#FF0A1317` |
| 20 | `TextView` | `android:id` | `@id/com_facebook_sso_noapp_title` |
| 21 | `TextView` | `android:layout_width` | `0.000000dip` |
| 22 | `TextView` | `android:layout_height` | `wrap_content` |
| 23 | `TextView` | `android:text` | `@string/com_facebook_sso_noapp_title` |
| 24 | `TextView` | `android:layout_weight` | `1.000000` |
| 25 | `TextView` | `android:fontFamily` | `@font/optimistic_vf` |
| 26 | `TextView` | `android:layout_marginStart` | `8.000000dip` |
| 27 | `TextView` | `android:textFontWeight` | `600` |
| 28 | `ImageButton` | `android:id` | `@id/com_facebook_sso_noapp_close` |
| 29 | `ImageButton` | `android:background` | `?0x0101045C` |
| 30 | `ImageButton` | `android:padding` | `4.000000dip` |
| 31 | `ImageButton` | `android:layout_width` | `40.000000dip` |
| 32 | `ImageButton` | `android:layout_height` | `40.000000dip` |
| 33 | `ImageButton` | `android:src` | `@drawable/com_facebook_sso_close` |
| 34 | `ImageButton` | `android:scaleType` | `centerInside` |
| 35 | `ImageButton` | `android:contentDescription` | `@string/com_facebook_loginview_cancel_action` |
| 36 | `ImageButton` | `android:layout_marginStart` | `8.000000dip` |
| 37 | `TextView` | `android:textSize` | `15.000000sp` |
| 38 | `TextView` | `android:textColor` | `#FF0A1317` |
| 39 | `TextView` | `android:id` | `@id/com_facebook_sso_noapp_body` |
| 40 | `TextView` | `android:paddingBottom` | `20.000000dip` |
| 41 | `TextView` | `android:layout_width` | `match_parent` |
| 42 | `TextView` | `android:layout_height` | `wrap_content` |
| 43 | `TextView` | `android:text` | `@string/com_facebook_sso_noapp_body` |
| 44 | `TextView` | `android:fontFamily` | `@font/optimistic_vf` |
| 45 | `LinearLayout` | `android:orientation` | `horizontal` |
| 46 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 47 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 48 | `Button` | `android:textSize` | `15.000000sp` |
| 49 | `Button` | `android:textColor` | `#FF0A1317` |
| 50 | `Button` | `android:gravity` | `0x00000011` |
| 51 | `Button` | `android:id` | `@id/com_facebook_sso_noapp_not_now` |
| 52 | `Button` | `android:background` | `@drawable/com_facebook_sso_noapp_not_now_button_bg` |
| 53 | `Button` | `android:layout_width` | `0.000000dip` |
| 54 | `Button` | `android:layout_height` | `40.000000dip` |
| 55 | `Button` | `android:text` | `@string/com_facebook_sso_noapp_not_now` |
| 56 | `Button` | `android:layout_weight` | `1.000000` |
| 57 | `Button` | `android:textAllCaps` | `false` |
| 58 | `Button` | `android:fontFamily` | `@font/optimistic_vf` |
| 59 | `Button` | `android:layout_marginEnd` | `8.000000dip` |
| 60 | `Button` | `android:textSize` | `15.000000sp` |
| 61 | `Button` | `android:textColor` | `#FFF1F4F7` |
| 62 | `Button` | `android:gravity` | `0x00000011` |
| 63 | `Button` | `android:id` | `@id/com_facebook_sso_noapp_continue` |
| 64 | `Button` | `android:background` | `@drawable/com_facebook_sso_noapp_continue_button_bg` |
| 65 | `Button` | `android:layout_width` | `0.000000dip` |
| 66 | `Button` | `android:layout_height` | `40.000000dip` |
| 67 | `Button` | `android:text` | `@string/com_facebook_loginview_log_in_button_continue` |
| 68 | `Button` | `android:layout_weight` | `2.000000` |
| 69 | `Button` | `android:textAllCaps` | `false` |
| 70 | `Button` | `android:fontFamily` | `@font/optimistic_vf` |
| 71 | `Button` | `android:layout_marginStart` | `8.000000dip` |
| 72 | `Button` | `android:stateListAnimator` | `@null` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@string/com_facebook_loginview_cancel_action` | `Cancel` / `Kanselleer` (af) / `إلغاء` (ar) / `বাতিল করুন` (bn) / `Zrušit` (cs) / `Annuller` (da) / `Abbrechen` (de) / `Ακύρωση` (el) / `Cancelar` (es) / `Cancelar` (es-rES) / `Peruuta` (fi) / `Annuler` (fr) / `Annuler` (fr-rCA) / `રદ કરો` (gu) / `कैंसल करें` (hi) / `Odustani` (hr) / `Mégsem` (hu) / `Batal` (id) / `Batal` (in) / `Annulla` (it) / `ביטול` (iw) / `キャンセル` (ja) / `ರದ್ದುಮಾಡಿ` (kn) / `취소` (ko) / `റദ്ദാക്കുക` (ml) / `रद्द करा` (mr) / `Batal` (ms) / `Avbryt` (nb) / `Annuleren` (nl) / `ਰੱਦ ਕਰੋ` (pa) / `Anuluj` (pl) / `Cancelar` (pt) / `Cancelar` (pt-rPT) / `Anulează` (ro) / `Отмена` (ru) / `Zrušiť` (sk) / `Avbryt` (sv) / `ரத்துசெய்க` (ta) / `రద్దు చేయి` (te) / `ยกเลิก` (th) / `I-cancel` (tl) / `İptal` (tr) / `Скасувати` (uk) / `Hủy` (vi) / `取消` (zh-rCN) / `取消` (zh-rHK) / `取消` (zh-rTW) |
| `@string/com_facebook_loginview_log_in_button_continue` | `Continue with Facebook` / `Gaan voort met Facebook` (af) / `متابعة بحساب فيسبوك` (ar) / `Facebook এর সাথে চালিয়ে যান` (bn) / `Pokračovat přes Facebook` (cs) / `Fortsæt med Facebook` (da) / `Weiter mit Facebook` (de) / `Συνέχεια με το Facebook` (el) / `Continuar con Facebook` (es) / `Continuar con Facebook` (es-rES) / `Jatka Facebook-tunnuksilla` (fi) / `Continuer avec Facebook` (fr) / `Continuer avec Facebook` (fr-rCA) / `Facebook સાથે ચાલુ રાખો` (gu) / `Facebook के साथ जारी रखें` (hi) / `Nastavak uz Facebook` (hr) / `Folytatás a Facebookkal` (hu) / `Lanjutkan dengan Facebook` (id) / `Lanjutkan dengan Facebook` (in) / `Continua con Facebook` (it) / `המשך/המשיכי עם פייסבוק` (iw) / `Facebookでログイン` (ja) / `Facebook ನೊಂದಿಗೆ ಮುಂದುವರಿಸಿ` (kn) / `Facebook으로 계속하기` (ko) / `Facebook ഉപയോഗിച്ച് തുടരുക` (ml) / `Facebook सह चालू ठेवा` (mr) / `Teruskan dengan Facebook` (ms) / `Fortsett med Facebook` (nb) / `Doorgaan met Facebook` (nl) / `Facebook ਨਾਲ ਜਾਰੀ ਰੱਖੋ` (pa) / `Kontynuuj za pośrednictwem Facebooka` (pl) / `Continuar com o Facebook` (pt) / `Continuar com o Facebook` (pt-rPT) / `Continuă cu Facebook` (ro) / `Продолжить с Facebook` (ru) / `Pokračovať s Facebookom` (sk) / `Fortsätt med Facebook` (sv) / `Facebook மூலம் தொடரவும்` (ta) / `Facebookతో కొనసాగించండి` (te) / `ดำเนินการต่อด้วย Facebook` (th) / `Magpatuloy gamit ang Facebook` (tl) / `Facebook ile Devam Et` (tr) / `Продовжити у Facebook` (uk) / `Tiếp tục với Facebook` (vi) / `使用 Facebook 登录` (zh-rCN) / `繼續使用 Facebook 帳戶` (zh-rHK) / `以 Facebook 帳號繼續` (zh-rTW) |
| `@string/com_facebook_loginview_log_in_button_long` | `Log in with Facebook` / `Meld aan met Facebook` (af) / `تسجيل الدخول بحساب فيسبوك` (ar) / `Facebook দিয়ে লগইন করুন` (bn) / `Přihlásit se přes Facebook` (cs) / `Log på med Facebook` (da) / `Mit Facebook anmelden` (de) / `Συνδεθείτε μέσω Facebook` (el) / `Log In With Facebook` (en-rGB) / `Iniciar sesión con Facebook` (es) / `Inicia sesión con Facebook` (es-rES) / `Kirjaudu Facebook-tunnuksilla` (fi) / `Se connecter avec Facebook` (fr) / `Se connecter avec Facebook` (fr-rCA) / `Facebook વડે લોગ ઇન કરો` (gu) / `Facebook से लॉग इन करें` (hi) / `Prijavi se putem Facebooka` (hr) / `Bejelentkezés Facebookkal` (hu) / `Masuk menggunakan Facebook` (id) / `Masuk dengan Facebook` (in) / `Accedi con Facebook` (it) / `התחברות באמצעות פייסבוק` (iw) / `Facebookでログイン` (ja) / `Facebook ನೊಂದಿಗೆ ಲಾಗ್ ಇನ್ ಮಾಡಿ` (kn) / `Facebook으로 로그인` (ko) / `Facebook ഉപയോഗിച്ച് ലോഗിൻ ചെയ്യുക` (ml) / `Facebook सह लॉग इन करा` (mr) / `Log masuk dengan Facebook` (ms) / `Logg inn med Facebook` (nb) / `Aanmelden met Facebook` (nl) / `Facebook ਦੇ ਨਾਲ ਲੌਗ ਇਨ ਕਰੋ` (pa) / `Zaloguj się przez Facebooka` (pl) / `Entrar com o Facebook` (pt) / `Iniciar sessão com o Facebook` (pt-rPT) / `Conectare cu Facebook` (ro) / `Вход через Facebook` (ru) / `Prihlásiť sa cez Facebook` (sk) / `Logga in med Facebook` (sv) / `Facebook மூலம் உள்நுழையவும்` (ta) / `Facebookతో లాగిన్ చేయండి` (te) / `เข้าสู่ระบบด้วย Facebook` (th) / `Mag-log in sa Facebook` (tl) / `Facebook ile Giriş Yap` (tr) / `Увійдіть використовуючи Facebook` (uk) / `Đăng nhập bằng Facebook` (vi) / `使用 Facebook 登录` (zh-rCN) / `使用 Facebook 登入` (zh-rHK) / `使用 Facebook 帳號登入` (zh-rTW) |
| `@string/com_facebook_sso_noapp_body` | `Create your account in seconds with Facebook.` |
| `@string/com_facebook_sso_noapp_not_now` | `Not now` / `Teď ne` (cs) / `Ikke nu` (da) / `Jetzt nicht` (de) / `Όχι τώρα` (el) / `Not now` (en-rGB) / `Ahora no` (es) / `Ahora no` (es-rES) / `Ei nyt` (fi) / `Plus tard` (fr) / `Non ora` (it) / `後で` (ja) / `나중에 하기` (ko) / `Ikke nå` (nb) / `Niet nu` (nl) / `Nie teraz` (pl) / `Agora não` (pt) / `Agora não` (pt-rPT) / `Nu acum` (ro) / `Не сейчас` (ru) / `Inte nu` (sv) / `ไม่ใช่ตอนนี้` (th) / `Şimdi değil` (tr) / `以后再说` (zh-rCN) / `稍後再說` (zh-rHK) / `稍後再說` (zh-rTW) |
| `@string/com_facebook_sso_noapp_title` | `Sign up faster with Facebook` |

## ۴. شناسه‌های `@id`

```text
@id/com_facebook_sso_noapp_body
@id/com_facebook_sso_noapp_close
@id/com_facebook_sso_noapp_continue
@id/com_facebook_sso_noapp_not_now
@id/com_facebook_sso_noapp_title
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
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android" android:orientation="vertical" android:background="@drawable/com_facebook_sso_noapp_background" android:paddingBottom="24.000000dip" android:layout_width="match_parent" android:layout_height="wrap_content" android:paddingStart="24.000000dip" android:paddingEnd="24.000000dip">
  <LinearLayout android:gravity="0x00000010" android:orientation="horizontal" android:paddingTop="16.000000dip" android:paddingBottom="12.000000dip" android:layout_width="match_parent" android:layout_height="wrap_content">
    <ImageView android:layout_width="24.000000dip" android:layout_height="24.000000dip" android:src="@drawable/com_facebook_sso_logo" android:contentDescription="@string/com_facebook_loginview_log_in_button_long"/>
    <TextView android:textSize="17.000000sp" android:textColor="#FF0A1317" android:id="@id/com_facebook_sso_noapp_title" android:layout_width="0.000000dip" android:layout_height="wrap_content" android:text="@string/com_facebook_sso_noapp_title" android:layout_weight="1.000000" android:fontFamily="@font/optimistic_vf" android:layout_marginStart="8.000000dip" android:textFontWeight="600"/>
    <ImageButton android:id="@id/com_facebook_sso_noapp_close" android:background="?0x0101045C" android:padding="4.000000dip" android:layout_width="40.000000dip" android:layout_height="40.000000dip" android:src="@drawable/com_facebook_sso_close" android:scaleType="centerInside" android:contentDescription="@string/com_facebook_loginview_cancel_action" android:layout_marginStart="8.000000dip"/>
  </LinearLayout>
  <TextView android:textSize="15.000000sp" android:textColor="#FF0A1317" android:id="@id/com_facebook_sso_noapp_body" android:paddingBottom="20.000000dip" android:layout_width="match_parent" android:layout_height="wrap_content" android:text="@string/com_facebook_sso_noapp_body" android:fontFamily="@font/optimistic_vf"/>
  <LinearLayout android:orientation="horizontal" android:layout_width="match_parent" android:layout_height="wrap_content">
    <Button android:textSize="15.000000sp" android:textColor="#FF0A1317" android:gravity="0x00000011" android:id="@id/com_facebook_sso_noapp_not_now" android:background="@drawable/com_facebook_sso_noapp_not_now_button_bg" android:layout_width="0.000000dip" android:layout_height="40.000000dip" android:text="@string/com_facebook_sso_noapp_not_now" android:layout_weight="1.000000" android:textAllCaps="false" android:fontFamily="@font/optimistic_vf" android:layout_marginEnd="8.000000dip"/>
    <Button android:textSize="15.000000sp" android:textColor="#FFF1F4F7" android:gravity="0x00000011" android:id="@id/com_facebook_sso_noapp_continue" android:background="@drawable/com_facebook_sso_noapp_continue_button_bg" android:layout_width="0.000000dip" android:layout_height="40.000000dip" android:text="@string/com_facebook_loginview_log_in_button_continue" android:layout_weight="2.000000" android:textAllCaps="false" android:fontFamily="@font/optimistic_vf" android:layout_marginStart="8.000000dip" android:stateListAnimator="@null"/>
  </LinearLayout>
</LinearLayout>
```
