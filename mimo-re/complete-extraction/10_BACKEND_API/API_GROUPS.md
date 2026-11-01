# ۱۰و — گروه‌بندی کاربردی API و نقش هر گروه

| گروه | تعداد | نقش در محصول | یادداشت |
|---|---|---|---|
| `v1/user` | ۱۹ | اعتبار، کلید، تنظیمات، بازدید، دعوت، علاقه‌مندی، جوایز | پرکاربردترین |
| `v1/tracks` | ۷ | تکمیل مسیر، ETA، آخرین تعامل | وضعیت |
| `v1/code` | ۷ | اجرا، فایل‌های ذخیره‌شده، رمیکس | هستهٔ درس کدی |
| `v1/users` | ۴ | پروفایل عمومی، کد، گزارش | اجتماعی |
| `v1/tutorials` | ۳ | پیشرفت، پیش‌نویس، savefiles | هستهٔ پیشرفت |
| `v1/leaderboards` | ۳ | لیگ/دوستان/رتبه | رقابت |
| `v1/products` | ۲ | محصولات کاربر | فروشگاه |
| `v1/account` | ۲ | حساب و ایمیل | هویت |
| `v1/preview` | ۱ | پیش‌نمایش درس پیش‌نویس | تألیف |
| `v1/practice` | ۱ | آمار تمرین | تحلیل |
| `v1/package` | ۱ | بستهٔ محتوا | توزیع |
| `v1/aiTutor` | ۱ (+۱ literal) | مربی | LLM |
| `v1/invitations` | ۱ | دعوت دوستان | رشد |
| `api/*` | ۷ | `sendCustomerIoData`, push/click (Customer.io) | third-party |
| `v2` | ۱ | `client-config` | پیکربندی |
| third-party | ۶ | Customer.io inbox | جدا |

## نگاشت به معماری پیشنهادی محصول هدف

| گروه Mimo | معادل در کنکور |
|---|---|
| `v1/tutorials` + `v1/tracks` | `/v1/progress` + `/v1/plan` |
| `v1/user` (کلید/اعتبار) | `/v1/entitlements` |
| `v1/code` | `—` (اجرا لازم نیست) |
| `v1/practice` | `/v1/mastery` + `/v1/analytics` |
| `v1/leaderboards` | `/v1/rank` (تراز/رتبه) |
| `v1/tutorials/drafts/...` | `/v1/content/drafts` (پنل تألیف) |
| `v1/aiTutor` | `/v1/assistant` |
| `v2/client-config` | `/v1/config` |
