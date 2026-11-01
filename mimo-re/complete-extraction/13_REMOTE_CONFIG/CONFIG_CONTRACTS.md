# ۱۳ج — قرارداد پیکربندی برای محصول هدف

```jsonc
// GET /v1/config  → 200
{
  "configVersion": 42,
  "minClientVersion": "1.4.0",
  "flags": {
    "ai_assistant":       { "enabled": true, "rollout": 100 },
    "exam_simulation":    { "enabled": true, "rollout": 100 },
    "diagnostic_report":  { "enabled": false, "rollout": 30 }
  },
  "limits": {
    "assistantMessagesPerDay": 5,
    "freeMockExams": 1,
    "offlinePackMaxBytes": 52428800
  },
  "experiments": [
    { "id": "lesson_length", "variants": ["short","long"], "bucket": 1 }
  ],
  "content": { "manifestUrl": "/v1/content/manifest", "publishSetVersion": 12 }
}
```
## قواعد الزامی

| قاعده | دلیل |
|---|---|
| `configVersion` و کش TTL (۵ دقیقه) | جلوگیری از درخواست تکراری |
| `minClientVersion` | اجبار به‌روزرسانی امن |
| سقف‌ها در سرور اعمال شوند | کلاینت فقط نمایش می‌دهد |
| flags با `rollout` درصدی | تدریجی و برگشت‌پذیر |
| پیکربندی هرگز کد اجرایی نداشته باشد | امنیت |
| مشاهدات: هر بار تغییر flag ⇒ رویداد `config_flag_changed` | ردیابی |

**تفاوت با Mimo:** Mimo فقط ۲ پرچم نام‌دار + یک endpoint دارد؛ این قرارداد کامل‌تر و
قابل ساخت است، ولی آنچه از Mimo آمده صرفاً «وجود مکانیزم» است، نه این ساختار.
