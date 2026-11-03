# پروندهٔ لایه — `res/layout/com_facebook_smart_device_dialog_fragment.xml`

> **کلاس شواهد:** `VERIFIED_STATIC` (دیکد مستقیم AXML باینری APK). هیچ بازسازی یا حدسی در XML زیر وجود ندارد؛ فقط شناسه‌های عددی به نام نمادین حل شده‌اند.

| ویژگی | مقدار |
|---|---|
| مسیر در APK | `res/layout/com_facebook_smart_device_dialog_fragment.xml` |
| فایل دیکدشده | [`SOURCE/res/layout/com_facebook_smart_device_dialog_fragment.xml`](../../SOURCE/res/layout/com_facebook_smart_device_dialog_fragment.xml) |
| SHA-256 دیکد | `40665565672fada7566c1a0928707de2078ae8d3b2aa95134284111dd5b56ee6` |
| ریشه | `androidx.cardview.widget.CardView` |
| تعداد گره | 12 |
| تعداد شناسه | 6 |
| تگ‌های استفاده‌شده | 8 |
| ویوهای سفارشی `com.getmimo` | 0 |
| `ComposeView` | 0 |
| `WebView` | 0 |
| `<include>`/`<ViewStub>` | 0 |
| ارجاع به منابع | 17 |

## ۱. درخت کامل مؤلفه‌ها

```text
└─ androidx.cardview.widget.CardView
   └─ LinearLayout
      ├─ RelativeLayout
      │  ├─ FrameLayout
      │  │  └─ androidx.appcompat.widget.AppCompatImageView
      │  ├─ TextView  #@id/confirmation_code
      │  └─ ProgressBar  #@id/progress_bar
      ├─ TextView  #@id/com_facebook_smart_instructions_0
      ├─ TextView  #@id/com_facebook_smart_instructions_or
      ├─ TextView  #@id/com_facebook_device_auth_instructions
      └─ FrameLayout
         └─ Button  #@id/cancel_button
```

## ۲. جدول کامل ویژگی‌ها (همهٔ گره‌ها)

| # | عنصر (tag) | ویژگی | مقدار |
|---:|---|---|---|
| 1 | `androidx.cardview.widget.CardView` | `android:layout_width` | `match_parent` |
| 2 | `androidx.cardview.widget.CardView` | `android:layout_height` | `wrap_content` |
| 3 | `androidx.cardview.widget.CardView` | `app:cardBackgroundColor` | `@0x0106000D` |
| 4 | `androidx.cardview.widget.CardView` | `app:cardElevation` | `10.000000dip` |
| 5 | `androidx.cardview.widget.CardView` | `app:contentPadding` | `16.000000dip` |
| 6 | `LinearLayout` | `android:gravity` | `0x00000001` |
| 7 | `LinearLayout` | `android:orientation` | `vertical` |
| 8 | `LinearLayout` | `android:background` | `@drawable/com_facebook_auth_dialog_background` |
| 9 | `LinearLayout` | `android:layout_width` | `match_parent` |
| 10 | `LinearLayout` | `android:layout_height` | `wrap_content` |
| 11 | `RelativeLayout` | `android:orientation` | `horizontal` |
| 12 | `RelativeLayout` | `android:background` | `@drawable/com_facebook_auth_dialog_header_background` |
| 13 | `RelativeLayout` | `android:layout_width` | `match_parent` |
| 14 | `RelativeLayout` | `android:layout_height` | `110.000000dip` |
| 15 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 16 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 17 | `androidx.appcompat.widget.AppCompatImageView` | `android:layout_width` | `18.000000dip` |
| 18 | `androidx.appcompat.widget.AppCompatImageView` | `android:layout_height` | `18.000000dip` |
| 19 | `androidx.appcompat.widget.AppCompatImageView` | `android:layout_marginLeft` | `12.000000dip` |
| 20 | `androidx.appcompat.widget.AppCompatImageView` | `android:layout_marginTop` | `11.000000dip` |
| 21 | `androidx.appcompat.widget.AppCompatImageView` | `android:layout_marginBottom` | `11.000000dip` |
| 22 | `androidx.appcompat.widget.AppCompatImageView` | `android:scaleType` | `fitXY` |
| 23 | `androidx.appcompat.widget.AppCompatImageView` | `android:adjustViewBounds` | `false` |
| 24 | `androidx.appcompat.widget.AppCompatImageView` | `android:layout_marginStart` | `12.000000dip` |
| 25 | `androidx.appcompat.widget.AppCompatImageView` | `app:srcCompat` | `@drawable/com_facebook_favicon_blue` |
| 26 | `TextView` | `android:textSize` | `52.000000sp` |
| 27 | `TextView` | `android:typeface` | `1` |
| 28 | `TextView` | `android:textColor` | `@color/com_smart_login_code` |
| 29 | `TextView` | `android:gravity` | `0x00000011` |
| 30 | `TextView` | `android:id` | `@id/confirmation_code` |
| 31 | `TextView` | `android:visibility` | `invisible` |
| 32 | `TextView` | `android:layout_width` | `wrap_content` |
| 33 | `TextView` | `android:layout_height` | `wrap_content` |
| 34 | `TextView` | `android:layout_centerInParent` | `true` |
| 35 | `TextView` | `android:fontFamily` | `sans-serif-light` |
| 36 | `ProgressBar` | `android:id` | `@id/progress_bar` |
| 37 | `ProgressBar` | `android:layout_width` | `wrap_content` |
| 38 | `ProgressBar` | `android:layout_height` | `0.000000dip` |
| 39 | `ProgressBar` | `android:layout_alignTop` | `@id/confirmation_code` |
| 40 | `ProgressBar` | `android:layout_alignBottom` | `@id/confirmation_code` |
| 41 | `ProgressBar` | `android:layout_centerInParent` | `true` |
| 42 | `ProgressBar` | `android:layout_centerHorizontal` | `true` |
| 43 | `ProgressBar` | `android:layout_centerVertical` | `true` |
| 44 | `TextView` | `android:id` | `@id/com_facebook_smart_instructions_0` |
| 45 | `TextView` | `android:layout_marginLeft` | `90.000000dip` |
| 46 | `TextView` | `android:layout_marginTop` | `18.000000dip` |
| 47 | `TextView` | `android:layout_marginRight` | `90.000000dip` |
| 48 | `TextView` | `android:text` | `@string/com_facebook_smart_device_instructions` |
| 49 | `TextView` | `android:layout_marginStart` | `90.000000dip` |
| 50 | `TextView` | `android:layout_marginEnd` | `90.000000dip` |
| 51 | `TextView` | `style` | `@style/com_facebook_auth_dialog_instructions_textview` |
| 52 | `TextView` | `android:textStyle` | `0x00000001` |
| 53 | `TextView` | `android:gravity` | `0x00000001` |
| 54 | `TextView` | `android:id` | `@id/com_facebook_smart_instructions_or` |
| 55 | `TextView` | `android:layout_width` | `match_parent` |
| 56 | `TextView` | `android:layout_marginTop` | `12.000000dip` |
| 57 | `TextView` | `android:text` | `@string/com_facebook_smart_device_instructions_or` |
| 58 | `TextView` | `android:layout_marginStart` | `0.000000dip` |
| 59 | `TextView` | `android:layout_marginEnd` | `0.000000dip` |
| 60 | `TextView` | `style` | `@style/com_facebook_auth_dialog_instructions_textview` |
| 61 | `TextView` | `android:id` | `@id/com_facebook_device_auth_instructions` |
| 62 | `TextView` | `android:layout_marginTop` | `12.000000dip` |
| 63 | `TextView` | `style` | `@style/com_facebook_auth_dialog_instructions_textview` |
| 64 | `FrameLayout` | `android:layout_width` | `match_parent` |
| 65 | `FrameLayout` | `android:layout_height` | `wrap_content` |
| 66 | `FrameLayout` | `android:layout_marginTop` | `17.000000dip` |
| 67 | `FrameLayout` | `android:layout_marginBottom` | `17.000000dip` |
| 68 | `Button` | `android:textSize` | `18.000000sp` |
| 69 | `Button` | `android:typeface` | `1` |
| 70 | `Button` | `android:textStyle` | `0x00000001` |
| 71 | `Button` | `android:textColor` | `@color/com_facebook_device_auth_text` |
| 72 | `Button` | `android:layout_gravity` | `0x00000001` |
| 73 | `Button` | `android:id` | `@id/cancel_button` |
| 74 | `Button` | `android:background` | `@drawable/com_facebook_auth_dialog_cancel_background` |
| 75 | `Button` | `android:focusable` | `true` |
| 76 | `Button` | `android:clickable` | `true` |
| 77 | `Button` | `android:layout_width` | `wrap_content` |
| 78 | `Button` | `android:layout_height` | `wrap_content` |
| 79 | `Button` | `android:minWidth` | `200.000000dip` |
| 80 | `Button` | `android:text` | `@0x01040000` |
| 81 | `Button` | `android:textAllCaps` | `true` |
| 82 | `Button` | `android:fontFamily` | `sans-serif-medium` |

## ۳. مقادیر حل‌شدهٔ ارجاعات

| ارجاع | مقدار حل‌شده |
|---|---|
| `@color/com_facebook_device_auth_text` | `#FF90949C` |
| `@color/com_smart_login_code` | `#FF3C6499` |
| `@string/com_facebook_smart_device_instructions` | `To connect your account, open the Facebook app on your mobile device and check for notifications.` / `Maak die Facebook-toepassing op jou mobiele toestel oop en soek kennisgewings om jou rekening te koppel.` (af) / `لربط حسابك، افتح تطبيق فيسبوك على جهازك المحمول وراجع الإشعارات.` (ar) / `আপনার অ্যাকাউন্ট সংযুক্ত করতে, আপনার মোবাইল ডিভাইসে Facebook অ্যাপ খুলুন এবং বিজ্ঞপ্তিগুলির জন্য পরীক্ষা করুন।` (bn) / `Pokud chcete připojit svůj účet, spusťte aplikaci Facebook ve svém mobilním zařízení a zkontrolujte upozornění.` (cs) / `For at tilslutte din konto skal du åbne Facebook-appen på din mobilenhed og se efter, om der er notifikationer.` (da) / `Öffne die Facebook-App auf deinem Mobilgerät, um dich mit deinem Konto zu verbinden und nach Benachrichtigungen zu suchen.` (de) / `Για να συνδέσετε το λογαριασμό σας, ανοίξτε την εφαρμογή Facebook στη φορητή συσκευή σας και ελέγξτε για ειδοποιήσεις.` (el) / `Para conectar tu cuenta, abre la app de Facebook en tu dispositivo móvil y comprueba las notificaciones.` (es) / `Para conectar tu cuenta, abre la aplicación de Facebook en tu dispositivo móvil y comprueba las notificaciones.` (es-rES) / `Liitä tilisi avaamalla Facebook-sovellus matkapuhelimellasi ja tarkistamalla ilmoitukset.` (fi) / `Pour associer votre compte, ouvrez l’app Facebook sur votre appareil mobile et vérifiez les notifications.` (fr) / `Pour associer votre compte, ouvrez l’application Facebook sur votre appareil mobile et consultez les notifications.` (fr-rCA) / `તમારા એકાઉન્ટને કનેક્ટ કરવા માટે, તમારા મોબાઇલ ડિવાઇસ પર Facebook ઍપ ખોલો અને નોટિફિકેશન જુઓ.` (gu) / `अपने खाते से कनेक्ट करने के लिए, अपने मोबाइल डिवाइस पर Facebook एप्लिकेशन खोलें और सूचनाएँ जाँचें.` (hi) / `Za povezivanje svog računa otvorite aplikaciju Facebook na mobilnom uređaju i pročitajte obavijesti.` (hr) / `A fiók hozzákapcsolásához nyisd meg a mobilkészülékeden a Facebook alkalmazást, és nézd meg az értesítéseket.` (hu) / `Untuk menghubungkan akun Anda, buka aplikasi Facebook di perangkat seluler Anda dan periksa pemberitahuan.` (id) / `Untuk menghubungkan akun Anda, buka aplikasi Facebook di perangkat seluler Anda dan lihat pemberitahuan.` (in) / `Per connettere il tuo account, apri l'app Facebook dal tuo dispositivo mobile e controlla le notifiche.` (it) / `כדי לחבר את חשבונך, יש לפתוח את אפליקציית פייסבוק במכשיר הנייד ולבדוק אם יש התראות.` (iw) / `アカウントをリンクするには、モバイル機器でFacebookアプリを開いて、お知らせをご確認ください。` (ja) / `ನಿಮ್ಮ ಖಾತೆಯನ್ನು ಸಂಪರ್ಕಿಸಲು, ನಿಮ್ಮ ಮೊಬೈಲ್ ಸಾಧನದಲ್ಲಿ Facebook ಅಪ್ಲಿಕೇಶನ್ ತೆರೆಯಿರಿ ಮತ್ತು ಅಧಿಸೂಚನೆಗಳಿಗಾಗಿ ಪರಿಶೀಲಿಸಿ.` (kn) / `계정에 연결하려면 모바일 기기에서 Facebook 앱을 열고 알림을 확인하세요.` (ko) / `നിങ്ങളുടെ അക്കൗണ്ട് കണക്‌റ്റ്ചെയ്യാൻ, നിങ്ങളുടെ മൊബൈൽ ഉപകരണത്തിലെ Facebook ആപ്പ് തുറന്ന് അറിയിപ്പുകൾ പരിശോധിക്കുക.` (ml) / `तुमचे खाते कनेक्ट करण्यासाठी, तुमच्या मोबाईल डिव्हाइसवर Facebook अ‍ॅप उघडा आणि सूचना तपासा.` (mr) / `Untuk menyambungkan akaun anda, buka aplikasi Facebook pada peranti mudah alih anda, dan semak untuk pemberitahuan.` (ms) / `Koble til kontoen din ved å åpne Facebook-appen på mobilenheten din og se etter varsler.` (nb) / `Als je je account wilt koppelen, open je de Facebook-app op je mobiele apparaat en controleer je je meldingen.` (nl) / `ਆਪਣੇ ਖਾਤੇ ਨੂੰ ਕਨੈਕਟ ਕਰਨ ਲਈ, ਮੋਬਾਈਲ ਡਿਵਾਈਸ 'ਤੇ Facebook ਐਪ ਖੋਲ੍ਹੋ ਅਤੇ ਸੂਚਨਾਵਾਂ ਦੀ ਜਾਂਚ ਕਰੋ।` (pa) / `Aby połączyć konto, otwórz aplikację Facebook na urządzeniu mobilnym i sprawdź powiadomienia.` (pl) / `Para conectar sua conta, abra o aplicativo do Facebook no seu dispositivo móvel e verifique se há notificações.` (pt) / `Para associares a tua conta, abre a app Facebook no teu dispositivo móvel e consulta as notificações.` (pt-rPT) / `Pentru a te conecta la contul tău, deschide aplicaţia Facebook de pe dispozitivul mobil şi verifică notificările.` (ro) / `Чтобы привязать ваш аккаунт, откройте приложение Facebook на своем мобильном устройстве и проверьте уведомления.` (ru) / `Ak si chcete pripojiť účet, vo svojom mobilnom zariadení otvorte aplikáciu Facebook a pozrite si upozornenia.` (sk) / `Anslut ditt konto genom att öppna Facebook-appen på din mobila enhet och leta efter aviseringar.` (sv) / `உங்கள் கணக்கை இணைக்க, உங்கள் மொபைல் சாதனத்தில் Facebook பயன்பாட்டைத் திறந்து, அறிவிப்புகளைப் பார்க்கவும்.` (ta) / `మీ ఖాతాను కనెక్ట్ చేసేందుకు, మీ మొబైల్ పరికరంలో Facebook యాప్‌ని తెరిచి, నోటిఫికేషన్‌లను తనిఖీ చేయండి.` (te) / `หากต้องการเชื่อมต่อกับบัญชีผู้ใช้ของคุณ ให้เปิดแอพ Facebook บนอุปกรณ์มือถือของคุณแล้วตรวจสอบการแจ้งเตือน` (th) / `Para ikonekta ang iyong account, buksan ang Facebook app sa iyong cellphone at tumingin ng mga notification.` (tl) / `Hesabını bağlamak için, mobil cihazında Facebook uygulamasını aç ve bildirimleri kontrol et.` (tr) / `Để kết nối tài khoản của bạn, hãy mở ứng dụng Facebook trên thiết bị di động và kiểm tra thông báo.` (vi) / `要关联帐户，请在移动设备上打开 Facebook 应用并查看通知。` (zh-rCN) / `若要連結帳戶，請在流動裝置上開啟 Facebook 應用程式，然後查看通知。` (zh-rHK) / `若要連結帳號，請在行動裝置上開啟 Facebook 應用程式，然後查看通知。` (zh-rTW) |
| `@string/com_facebook_smart_device_instructions_or` | `- OR -` / `- OF -` (af) / `- أو -` (ar) / `- বা -` (bn) / `- NEBO -` (cs) / `- ELLER -` (da) / `- ODER -` (de) / `- Ή -` (el) / `o` (es) / `- O -` (es-rES) / `- TAI -` (fi) / `- OU -` (fr) / `– OU –` (fr-rCA) / `- અથવા -` (gu) / `- या -` (hi) / `- ILI -` (hr) / `- VAGY -` (hu) / `- ATAU -` (id) / `- ATAU -` (in) / `- oppure -` (it) / `- או -` (iw) / `- または -` (ja) / `- ಅಥವಾ -` (kn) / `- 또는 -` (ko) / `- അല്ലെങ്കിൽ -` (ml) / `- किंवा -` (mr) / `- ATAU -` (ms) / `– ELLER –` (nb) / `- OF -` (nl) / `- ਜਾਂ -` (pa) / `- LUB -` (pl) / `- OU -` (pt) / `- OU -` (pt-rPT) / `- SAU -` (ro) / `- ИЛИ -` (ru) / `– ALEBO –` (sk) / `- ELLER -` (sv) / `- அல்லது -` (ta) / `- లేదా -` (te) / `- หรือ -` (th) / `- O -` (tl) / `- VEYA -` (tr) / `- HOẶC -` (vi) / `- 或 -` (zh-rCN) / `- 或 -` (zh-rHK) / `- 或 -` (zh-rTW) |
| `@style/com_facebook_auth_dialog_instructions_textview` | `[{'attr': 'android:textSize', 'attr_id': '0x01010095', 'value': '16.000000sp', 'value_type': 'dimension'}, {'attr': 'android:typeface', 'attr_id': '0x01010096', 'value': '1', 'value_type': 'int_dec'}, {'attr': 'android:textColor', 'attr_id': '0x01010098', 'value': '@color/com_facebook_device_auth_text', 'value_type': 'reference'}, {'attr': 'android:gravity', 'attr_id': '0x010100AF', 'value': '0x00000011', 'value_type': 'int_hex'}, {'attr': 'android:layout_width', 'attr_id': '0x010100F4', 'value': '-2', 'value_type': 'int_dec'}, {'attr': 'android:layout_height', 'attr_id': '0x010100F5', 'value': '-2', 'value_type': 'int_dec'}, {'attr': 'android:singleLine', 'attr_id': '0x0101015D', 'value': 'false', 'value_type': 'int_boolean'}, {'attr': 'android:drawablePadding', 'attr_id': '0x01010171', 'value': '12.000000dip', 'value_type': 'dimension'}, {'attr': 'android:fontFamily', 'attr_id': '0x010103AC', 'value': 'roboto', 'value_type': 'string'}]` |

## ۴. شناسه‌های `@id`

```text
@id/cancel_button
@id/com_facebook_device_auth_instructions
@id/com_facebook_smart_instructions_0
@id/com_facebook_smart_instructions_or
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
<androidx.cardview.widget.CardView xmlns:android="http://schemas.android.com/apk/res/android" xmlns:app="http://schemas.android.com/apk/res-auto" android:layout_width="match_parent" android:layout_height="wrap_content" app:cardBackgroundColor="@0x0106000D" app:cardElevation="10.000000dip" app:contentPadding="16.000000dip">
  <LinearLayout android:gravity="0x00000001" android:orientation="vertical" android:background="@drawable/com_facebook_auth_dialog_background" android:layout_width="match_parent" android:layout_height="wrap_content">
    <RelativeLayout android:orientation="horizontal" android:background="@drawable/com_facebook_auth_dialog_header_background" android:layout_width="match_parent" android:layout_height="110.000000dip">
      <FrameLayout android:layout_width="match_parent" android:layout_height="wrap_content">
        <androidx.appcompat.widget.AppCompatImageView android:layout_width="18.000000dip" android:layout_height="18.000000dip" android:layout_marginLeft="12.000000dip" android:layout_marginTop="11.000000dip" android:layout_marginBottom="11.000000dip" android:scaleType="fitXY" android:adjustViewBounds="false" android:layout_marginStart="12.000000dip" app:srcCompat="@drawable/com_facebook_favicon_blue"/>
      </FrameLayout>
      <TextView android:textSize="52.000000sp" android:typeface="1" android:textColor="@color/com_smart_login_code" android:gravity="0x00000011" android:id="@id/confirmation_code" android:visibility="invisible" android:layout_width="wrap_content" android:layout_height="wrap_content" android:layout_centerInParent="true" android:fontFamily="sans-serif-light"/>
      <ProgressBar android:id="@id/progress_bar" android:layout_width="wrap_content" android:layout_height="0.000000dip" android:layout_alignTop="@id/confirmation_code" android:layout_alignBottom="@id/confirmation_code" android:layout_centerInParent="true" android:layout_centerHorizontal="true" android:layout_centerVertical="true"/>
    </RelativeLayout>
    <TextView android:id="@id/com_facebook_smart_instructions_0" android:layout_marginLeft="90.000000dip" android:layout_marginTop="18.000000dip" android:layout_marginRight="90.000000dip" android:text="@string/com_facebook_smart_device_instructions" android:layout_marginStart="90.000000dip" android:layout_marginEnd="90.000000dip" style="@style/com_facebook_auth_dialog_instructions_textview"/>
    <TextView android:textStyle="0x00000001" android:gravity="0x00000001" android:id="@id/com_facebook_smart_instructions_or" android:layout_width="match_parent" android:layout_marginTop="12.000000dip" android:text="@string/com_facebook_smart_device_instructions_or" android:layout_marginStart="0.000000dip" android:layout_marginEnd="0.000000dip" style="@style/com_facebook_auth_dialog_instructions_textview"/>
    <TextView android:id="@id/com_facebook_device_auth_instructions" android:layout_marginTop="12.000000dip" style="@style/com_facebook_auth_dialog_instructions_textview"/>
    <FrameLayout android:layout_width="match_parent" android:layout_height="wrap_content" android:layout_marginTop="17.000000dip" android:layout_marginBottom="17.000000dip">
      <Button android:textSize="18.000000sp" android:typeface="1" android:textStyle="0x00000001" android:textColor="@color/com_facebook_device_auth_text" android:layout_gravity="0x00000001" android:id="@id/cancel_button" android:background="@drawable/com_facebook_auth_dialog_cancel_background" android:focusable="true" android:clickable="true" android:layout_width="wrap_content" android:layout_height="wrap_content" android:minWidth="200.000000dip" android:text="@0x01040000" android:textAllCaps="true" android:fontFamily="sans-serif-medium"/>
    </FrameLayout>
  </LinearLayout>
</androidx.cardview.widget.CardView>
```
