# مهارت‌های ایجنت — «انبار دارو»

این پوشه **کتابخانهٔ راهنمای ایجنت** است، نه بخشی از محصول:

- هیچ فایلی از اینجا در APK نیست و هیچ وابستگی Gradle اضافه نمی‌کند.
- در `android/` هیچ ارجاعی به این پوشه وجود ندارد (workflow `skills-check` تضمین می‌کند).
- محتوای آن نسخهٔ پین‌شدهٔ مخازن عمومی با لایسنس MIT/Apache-2.0 است (فایل `LICENSE` هر
  مخزن دست‌نخورده کنارش مانده).

```
agent-skills/
├── README.md          ← همین فایل: چطور استفاده کنیم
├── PROJECT-RULES.md   ← قوانین ما؛ بر همهٔ مهارت‌ها مقدم است  ⚠️ اول این
├── INDEX.md           ← فهرست خودکار ۱۸۷ مهارت با توضیح یک‌خطی و مسیر
├── REGISTRY.md        ← جدول منابع: ریپو، commit، لایسنس، نقش، چه‌چیزی حذف شد
├── registry.json      ← همان اطلاعات به شکل ماشین‌خوان (منبع حقیقت)
├── NOT-INSTALLED.md   ← چه چیزهایی را عمداً نصب نکردیم و چرا
├── vendor/            ← نسخهٔ پین‌شدهٔ ۸ مخزن (بدون .git)
└── tools/
    ├── sync-skills.sh ← بازنصب/به‌روزرسانی (پین‌شده یا --latest)
    ├── build_index.py ← ساخت INDEX.md
    └── check.py       ← اعتبارسنجی (همین در CI اجرا می‌شود)
```

## چطور استفاده می‌شود (برای ایجنت)

1. **اول** `PROJECT-RULES.md` را بخوان. اگر مهارتی خلاف آن گفت، قوانین پروژه برنده است.
2. برای کار جاری **فقط** مهارت مرتبط را باز کن (جدول پایین). کل ۱۸۷ مهارت را نخوان؛
   context را شلوغ و دستورها را متناقض می‌کند.
3. پیشنهادهای بازبینی را با شدت گزارش کن: **Critical / High / Medium / Low**.

| کار جاری | منبع اول |
|---|---|
| build، AGP 9، R8، اندازهٔ APK، edge-to-edge | `vendor/android-official-skills/build-system/`, `performance/r8-analyzer`, `system/edge-to-edge` |
| ViewModel، UiState، Flow، side-effect، concurrency | `vendor/chrisbanes-skills/skills/compose-state-and-effects`, `kotlin-concurrency-and-flow` |
| نوشتن/اصلاح صفحهٔ Compose | `vendor/compose-kotlin-agent-skills/SKILL.md` + `references/02-compose-ui.md` + `references/00-banned-antipatterns.md` |
| Room، DAO، migration، transaction | `vendor/android-agent-skills/skills/android-room-database` |
| اسکنر CameraX + ML Kit | `vendor/android-official-skills/camera/camerax` + `vendor/compose-kotlin-agent-skills/references/12-camera-mlkit.md` |
| اعلان محلی + WorkManager (فاز H) | `vendor/android-agent-skills/skills/android-workmanager-notifications` + `android-permissions-activity-results` |
| دسترس‌پذیری و Material 3 | `vendor/android-agent-skills/skills/android-compose-accessibility`, `android-material3-design-system` |
| تست UI، instrumentation، ADB | `vendor/android-testing-skills/compose`, `.../adb`, `.../instrumentation` |
| بازبینی معماری با شدت‌بندی | `vendor/android-review/skills/` (۷ حوزه) |
| بازبینی UX و جریان کاربر | `vendor/mobile-app-ux-auditor-skill/skills/mobile-app-ux-auditor` |

### نقشهٔ فازها

| فاز | از کدام منابع استفاده شود |
|---|---|
| F — موجودی، بچ، آستانه‌ها (جاری) | android-official (Room/Compose) + android-agent-skills (room, state-effects) + chrisbanes (concurrency) |
| H — تنظیمات آستانه، اعلان محلی، UX | + workmanager-notifications + ux-auditor + accessibility |
| بازبینی پایان هر milestone | android-review (هر ۷ حوزه) |
| قبل از انتشار | android-review کامل + `references/13-release-checklist.md` + `play-store` |

## نصب روی ابزارهای دیگر (اختیاری)

اگر خواستید همین مهارت‌ها را به Cursor / Claude Code بدهید، به‌جای clone مجدد از همین
نسخهٔ پین‌شده استفاده کنید:

```bash
# Cursor — در ریشهٔ ریپو
ln -s ../../agent-skills/vendor/compose-kotlin-agent-skills .cursor/skills/compose-kotlin-agent-skills
# Claude Code
ln -s "$PWD/agent-skills/vendor/compose-kotlin-agent-skills" ~/.claude/skills/compose-kotlin-agent-skills
```

`AGENTS.md` در ریشهٔ ریپو خوکار توسط Cursor/Copilot/Codex/Claude خوانده می‌شود و به همین
پوشه و قوانین اشاره می‌کند.

## به‌روزرسانی

```bash
bash agent-skills/tools/sync-skills.sh            # دقیقاً همان commit های ثبت‌شده
bash agent-skills/tools/sync-skills.sh --latest   # HEAD روزِ upstream (بعدش بازبینی لازم است)
python3 agent-skills/tools/check.py               # اعتبارسنجی
```

بعد از هر به‌روزرسانی، `registry.json` و `REGISTRY.md` را به‌روز کنید و
`python3 agent-skills/tools/build_index.py` را اجرا کنید.

## چه چیزی اینجا **نیست**

مخازن سنگین یا KMP-محور (مثل `michaelbel/cuckcoder`، `ronjunevaldoz/kmp-agent-skills`)
عمداً نصب نشده‌اند. دلیلش در `NOT-INSTALLED.md` است.
