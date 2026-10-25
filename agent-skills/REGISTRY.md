# منابع نصب‌شده

> منبع حقیقت ماشین‌خوان: `registry.json` (همین اطلاعات + دلیل انتخاب).
> به‌روزرسانی: `bash agent-skills/tools/sync-skills.sh` — نسخه‌ها **پین‌شده** هستند تا
> رفتار ایجنت بین اجراها تغییر نکند.

| پوشه | ریپو | نقش | لایسنس | commit پین‌شده | مهارت | فاز |
|---|---|---|---|---|---|---|
| `android-official-skills` | `android/skills` | core | Apache-2.0 | `4ebabf2b0fd6` | 33 | همه فازها |
| `chrisbanes-skills` | `chrisbanes/skills` | core | Apache-2.0 | `6c30c500c36a` | 19 | هر فاز UI/داده، بازبینی |
| `compose-kotlin-agent-skills` | `haidrrrry/compose-kotlin-agent-skills` | core | MIT | `3851303e2788` | 4 | C اتصال UI به دامنه، E اسکن، H UX |
| `android-review` | `liuyi0808/android-review` | core | MIT | `26fbdc85360e` | 7 | پایان هر milestone، قبل از انتشار |
| `android-agent-skills` | `krutikJain/android-agent-skills` | phase | MIT | `c5bf6731b844` | 68 | E اسکن، F موجودی، H اعلان‌ها |
| `android-testing-skills` | `skydoves/android-testing-skills` | phase | Apache-2.0 | `8665ed59643c` | 54 | G تست، H instrumentation |
| `mobile-app-ux-auditor-skill` | `AjnasNB/mobile-app-ux-auditor-skill` | phase | MIT | `514c75823a46` | 2 | H بازبینی UX |
| `android-ai-skills` | `RanaNadeemAslam/android-ai-skills` | rules | MIT | `3d9174c18d52` | 0 | مرجع |

## نقش‌ها

- **core** — همیشه در دسترس؛ برای کارهای روزمرهٔ UI/داده به آن رجوع می‌شود.
- **phase** — فقط در فاز مربوطه باز می‌شود (تست، UX، اعلان‌ها).
- **rules** — فقط مرجع مقایسه‌ای؛ کپی نمی‌شود و بر `PROJECT-RULES.md` مقدم نیست.

## چه چیزی از مخازن حذف شد (و چرا)

| مخزن | حذف‌شده | دلیل |
|---|---|---|
| `chrisbanes/skills` | `evals/` (۵ مگابایت) | fixture ارزیابی خودشان؛ برای ما کاربردی ندارد |
| `haidrrrry/compose-kotlin-agent-skills` | `assets/logo.png` (۱٫۲ مگابایت)، `marketing/` | تصویر و متن تبلیغاتی |
| بقیه | — | کامل و دست‌نخورده |

حذف‌ها فقط فایل‌های غیرآموزشی/حجیم را می‌گیرند؛ هیچ `SKILL.md` یا `references/` حذف نشده است.

## لایسنس

همهٔ مخازن MIT یا Apache-2.0 هستند و فایل لایسنس هر کدام در همان پوشه باقی مانده است.
متون مهارت‌ها دست‌نخورده کپی شده‌اند (فقط حذف فایل، بدون ویرایش محتوا). اگر روزی از
این متون در مستندات عمومی محصول استفاده شد، نام نویسندهٔ اصلی ذکر شود.
