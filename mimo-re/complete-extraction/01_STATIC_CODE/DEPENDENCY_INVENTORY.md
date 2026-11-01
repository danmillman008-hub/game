# ۰۱د — فهرست وابستگی‌ها (اندازه‌گیری‌شده با شمارش کلاس)

داده: `DEPENDENCY_INVENTORY.csv` (۱۲,۳۸۷ namespace). جدول زیر بزرگ‌ترین‌ها را نشان می‌دهد.

| Namespace | کلاس | تأمین‌کننده/نقش |
|---|---|---|
| `com.google` | ۵,۷۱۸ | Firebase (Auth/Messaging/RC/IAM/Analytics)، GMS، Play Billing |
| `com.getmimo` | ۳,۱۳۳ | خود برنامه |
| `com.revenuecat` | ۲,۴۳۶ | خرید درون‌برنامه‌ای و entitlement |
| `app.rive` | ۹۸۳ | انیمیشن برداری |
| `androidx.compose` | ۷۸۶ | UI اعلانی (مربی هوشمند، کیبورد کدنویسی) |
| `kotlin.reflect` | ۶۲۴ | بازتاب کاتلین (احتمالاً serialization) |
| `io.customer` | ۳۵۱ | Customer.io (پیام چرخهٔ عمر + Inbox) |
| `com.adjust` | ۳۱۵ | اتریبیوشن نصب |
| `okhttp3.internal` | ۲۹۰ | HTTP |
| `androidx.glance` | ۱۹۶ | ویجت زنجیره |
| `kotlinx.coroutines` | ۱۴۹ | هم‌روندی |
| `androidx.datastore` | ۱۴۸ | ترجیحات/DataStore |
| **`com.segment`** | **۱۳۷** | **Segment — روتر تحلیلی (تازه شناسایی شد)** |
| `com.facebook` | ۱۱۷ | Facebook SDK (Login/Share) |
| `androidx.fragment` | ۹۶ | ناوبری Fragment |
| `io.reactivex` | ۹۶ | RxJava |
| `org.ocpsoft` | ۹۲ | کتابخانهٔ نامشخص (نیازمند بررسی) |
| `androidx.lifecycle` | ۸۷ | چرخهٔ عمر |
| `androidx.room` | ۷۲ | پایگاه دادهٔ محلی |
| `org.joda` | ۷۲ | تاریخ/ساعت |
| `org.chromium` | ۶۷ | WebView سفارشی/بروزرسانی |
| `com.mixpanel` | ۶۲ | تحلیل محصول |

## نکات

1. **Segment** پیش‌تر گزارش نشده بود؛ با توجه به `/v1/events` و Mixpanel، معماری تحلیلی
   احتمالاً «Segment → مقصدها» است (INFERRED).
2. **Retrofit** در بسته با نام اصلی وجود ندارد (`retrofit2` فقط ۴ رشته) چون کل کتابخانه
   مبهم‌سازی شده است؛ annotation‌های `Lie0/*` جای آن را گرفته‌اند. این کشف در
   `10_BACKEND_API/API_CATALOG.md` مستند شده.
3. کتابخانهٔ SQL رمزنگاری‌شده (SQLCipher) مشاهده نشد ⇒ پایگاه دادهٔ محلی رمزنگاری‌نشده.
