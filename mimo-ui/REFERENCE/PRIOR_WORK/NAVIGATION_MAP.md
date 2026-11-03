# ۰۳ج — نقشهٔ ناوبری

```mermaid
graph TD
  S[SplashActivity / alias SplashActivity_default] -->|no session| A[AuthenticationActivity]
  S -->|session, onboarding incomplete| O[OnboardingActivity<br/>nav_onboarding_graph.xml]
  S -->|session + onboarding| M[MainActivity]
  O -->|12 steps| M
  M --> T1[Tab: learning]
  M --> T2[Tab: practice]
  M --> T3[Tab: profile]
  T1 --> C[ChapterActivity]
  C --> L1[Interactive player]
  C --> L2[Executable player]
  C --> CE[Chapter end modal chain]
  CE --> SP[Smart practice]
  M --> ST[Paywall / AllPlans / Store]
  M --> PF[ProfileFragment] --> PP[PublicProfileActivity]
  PF --> CERT[CertificateActivity / ProfessionalCertificateActivity]
  L1 --> AI[AI Tutor bottom sheet]
  L2 --> AI
  L2 --> PG[CodePlaygroundActivity]
  M -.hidden.-> DM[DeveloperMenu]
```

## قواعد ناوبری (شاهد)

| قاعده | شاهد | اطمینان |
|---|---|---|
| تنها یک گراف ناوبری اعلانی وجود دارد (آنبوردینگ) | `nav_onboarding_graph.xml` | HIGH |
| بقیهٔ ناوبری imperative است (Intent/Fragment) | ۶۱ activity، فقط ۱ graph | HIGH |
| تب‌ها می‌توانند پنهان/نمایش/بج شوند | `NavigationBar$listenToTabVisibilityChanges` | HIGH |
| انتخاب تب پس از kill شدن فرایند حفظ می‌شود | `NavigationBar$NavigationBarSavedState` | MEDIUM |
| لینک `/learn/.*` هر مسیری را می‌پذیرد | manifest pathPattern | HIGH |
| پایان فصل یک زنجیرهٔ modal است، نه صفحه | `ModalData$*` + `reward_drag_to_dismiss` | MEDIUM |

## آنچه نیاز به اجرا دارد (NOT_TESTED)

* رفتار Back در میانهٔ زنجیرهٔ مودال.
* بازگشت از deep link به درس نیمه‌تمام (بازسازی context از Room).
* ترتیب واقعی تب‌ها و برچسب‌ها.
