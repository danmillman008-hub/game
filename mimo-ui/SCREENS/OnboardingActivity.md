# صفحه — `OnboardingActivity`

> **خاستگاه ثبت:** `PRIOR_WORK_SCREEN_INVENTORY.csv` | **کلاس شواهد:** نام/ساختار `VERIFIED_STATIC`، نگاشت صفحه→لایه `DERIVED` (DEX xref + تطابق نام)، حالت‌ها `PARTIALLY_VERIFIED` (رشتهٔ منبع).

| ویژگی | مقدار |
|---|---|
| کلاس | `com.getmimo.ui.onboarding.OnboardingActivity` |
| نوع | `activity` |
| exported (manifest) | `` |
| launchMode | `` |
| theme | `@style/MaterialDarkModeTheme.NoAnim` |
| orientation | `` |
| targetActivity | `` |
| app-owned | `True` |
| فناوری | `view|compose (unresolved per screen)` |
| تعداد لایه‌های متصل | 11 |
| ComposeView | بله |
| WebView | خیر |

## ۱. لایه‌های XML متصل (فهرست کامل)

- [`res/layout/onboarding_activity.xml`](../SOURCE/res/layout/onboarding_activity.xml) → [dossier](LAYOUTS/layout_onboarding_activity.md)
- [`res/layout/onboarding_intro_slides_page.xml`](../SOURCE/res/layout/onboarding_intro_slides_page.xml) → [dossier](LAYOUTS/layout_onboarding_intro_slides_page.md)
- [`res/layout/onboarding_motive_button.xml`](../SOURCE/res/layout/onboarding_motive_button.xml) → [dossier](LAYOUTS/layout_onboarding_motive_button.md)
- [`res/layout/onboarding_path_completion_estimation_fragment.xml`](../SOURCE/res/layout/onboarding_path_completion_estimation_fragment.xml) → [dossier](LAYOUTS/layout_onboarding_path_completion_estimation_fragment.md)
- [`res/layout/onboarding_pick_a_path.xml`](../SOURCE/res/layout/onboarding_pick_a_path.xml) → [dossier](LAYOUTS/layout_onboarding_pick_a_path.md)
- [`res/layout/onboarding_select_path_fragment.xml`](../SOURCE/res/layout/onboarding_select_path_fragment.xml) → [dossier](LAYOUTS/layout_onboarding_select_path_fragment.md)
- [`res/layout/onboarding_set_daily_goal_fragment.xml`](../SOURCE/res/layout/onboarding_set_daily_goal_fragment.xml) → [dossier](LAYOUTS/layout_onboarding_set_daily_goal_fragment.md)
- [`res/layout/onboarding_step_1_introduction_fragment.xml`](../SOURCE/res/layout/onboarding_step_1_introduction_fragment.xml) → [dossier](LAYOUTS/layout_onboarding_step_1_introduction_fragment.md)
- [`res/layout/onboarding_step_2a_set_occupation_fragment.xml`](../SOURCE/res/layout/onboarding_step_2a_set_occupation_fragment.xml) → [dossier](LAYOUTS/layout_onboarding_step_2a_set_occupation_fragment.md)
- [`res/layout/onboarding_step_2b_set_work_function_fragment.xml`](../SOURCE/res/layout/onboarding_step_2b_set_work_function_fragment.xml) → [dossier](LAYOUTS/layout_onboarding_step_2b_set_work_function_fragment.md)
- [`res/layout/onboarding_step_3_set_experience_fragment.xml`](../SOURCE/res/layout/onboarding_step_3_set_experience_fragment.xml) → [dossier](LAYOUTS/layout_onboarding_step_3_set_experience_fragment.md)

## ۲. درخت مؤلفه‌ها (همهٔ لایه‌های متصل)

### `res/layout/onboarding_activity.xml`

```text
└─ LinearLayout  #@id/onboarding_root
   ├─ androidx.compose.ui.platform.ComposeView  #@id/onboarding_progress_bar
   └─ androidx.fragment.app.FragmentContainerView  #@id/container
```

### `res/layout/onboarding_intro_slides_page.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ app.rive.runtime.kotlin.RiveAnimationView  #@id/iv_rive_animation
   └─ LinearLayout  #@id/layout_slide_text_views
      ├─ TextView  #@id/tv_onboarding_page_title
      └─ TextView  #@id/tv_onboarding_page_description
```

### `res/layout/onboarding_motive_button.xml`

```text
└─ androidx.cardview.widget.CardView
   └─ androidx.constraintlayout.widget.ConstraintLayout  #@id/layout_course_card_root
      ├─ ImageView  #@id/iv_motive_button
      └─ TextView  #@id/tv_motive_button
```

### `res/layout/onboarding_path_completion_estimation_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_set_daily_goal_title
   ├─ app.rive.runtime.kotlin.RiveAnimationView  #@id/rav_path_completion_estimation
   ├─ ProgressBar  #@id/progressbar
   └─ androidx.compose.ui.platform.ComposeView  #@id/compose_content
```

### `res/layout/onboarding_pick_a_path.xml`

```text
└─ androidx.compose.ui.platform.ComposeView  #@id/cv_content
```

### `res/layout/onboarding_select_path_fragment.xml`

```text
└─ FrameLayout  #@id/onboarding_select_path_container
```

### `res/layout/onboarding_set_daily_goal_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_set_daily_goal_title
   ├─ TextView  #@id/tv_goal_subtitle
   ├─ com.getmimo.ui.profile.view.SetDailyGoalCard  #@id/layout_daily_goal_card
   └─ androidx.compose.ui.platform.ComposeView  #@id/compose_content
```

### `res/layout/onboarding_step_1_introduction_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_set_experience_introduction_title
   ├─ TextView  #@id/tv_set_experience_introduction_description
   ├─ app.rive.runtime.kotlin.RiveAnimationView  #@id/lv_set_experience_introduction
   └─ androidx.compose.ui.platform.ComposeView  #@id/compose_content
```

### `res/layout/onboarding_step_2a_set_occupation_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   └─ ScrollView
      └─ androidx.constraintlayout.widget.ConstraintLayout
         ├─ TextView  #@id/tv_set_occupation_title
         └─ LinearLayout  #@id/layout_motive
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_occupation_high_school
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_occupation_university
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_occupation_professional
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_occupation_self_employed
            └─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_occupation_none
```

### `res/layout/onboarding_step_2b_set_work_function_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   └─ ScrollView
      └─ androidx.constraintlayout.widget.ConstraintLayout
         ├─ TextView  #@id/tv_set_work_function_title
         └─ LinearLayout  #@id/layout_work_functions
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_work_function_marketing
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_work_function_sales
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_work_function_customer_support
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_work_function_software_it_data
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_work_function_product_management
            ├─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_work_function_admin_finance
            └─ com.getmimo.ui.onboarding.motive.OnboardingMotiveButton  #@id/btn_work_function_other
```

### `res/layout/onboarding_step_3_set_experience_fragment.xml`

```text
└─ androidx.constraintlayout.widget.ConstraintLayout
   ├─ TextView  #@id/tv_set_experience_slider_title
   ├─ app.rive.runtime.kotlin.RiveAnimationView  #@id/iv_set_experience_animation
   ├─ LinearLayout  #@id/layout_set_experience_slider_and_text
   │  ├─ com.getmimo.ui.common.SeekBarWithIntervals  #@id/seekbar_set_experience
   │  └─ TextView  #@id/tv_set_experience_slider_description
   └─ androidx.compose.ui.platform.ComposeView  #@id/compose_content
```

## ۳. رشته‌های مرتبط (فهرست کامل)

```text
onboarding_adapted_all_courses_title
onboarding_adapted_curriculum_ready
onboarding_adapted_daily_goal_title
onboarding_adapted_device_preference_both
onboarding_adapted_device_preference_desktop
onboarding_adapted_device_preference_phone
onboarding_adapted_device_preference_title
onboarding_adapted_device_reassurance_description
onboarding_adapted_device_reassurance_title
onboarding_adapted_experience_advanced
onboarding_adapted_experience_beginner
onboarding_adapted_experience_intermediate
onboarding_adapted_experience_title
onboarding_adapted_explore_courses_anytime
onboarding_adapted_goal_ai_agents
onboarding_adapted_goal_analyzing_data
onboarding_adapted_goal_apps_or_games
onboarding_adapted_goal_automated_workflows
onboarding_adapted_goal_automating_repetitive_tasks
onboarding_adapted_goal_build_title
onboarding_adapted_goal_building_learning_habit
onboarding_adapted_goal_career_advancement
onboarding_adapted_goal_career_change
onboarding_adapted_goal_career_exploration
onboarding_adapted_goal_career_title
onboarding_adapted_goal_checking_code
onboarding_adapted_goal_dashboards_or_reports
onboarding_adapted_goal_easier_title
onboarding_adapted_goal_finding_new_hobby
onboarding_adapted_goal_fun_title
onboarding_adapted_goal_keeping_mind_sharp
onboarding_adapted_goal_keeping_skills_relevant
onboarding_adapted_goal_understanding_technical_topics
onboarding_adapted_goal_using_screen_time_better
onboarding_adapted_goal_websites_or_landing_pages
onboarding_adapted_motive_career
onboarding_adapted_motive_easier
onboarding_adapted_motive_fun
onboarding_adapted_motive_reassurance_build
onboarding_adapted_motive_reassurance_career
onboarding_adapted_motive_reassurance_easier
onboarding_adapted_motive_reassurance_fun
onboarding_adapted_motive_reassurance_title
onboarding_adapted_motive_title
onboarding_adapted_not_sure_yet
onboarding_adapted_path_reassurance_description
onboarding_adapted_path_reassurance_title
onboarding_adapted_privacy_policy
onboarding_adapted_recommendation_title
onboarding_adapted_reminder_title
onboarding_adapted_see_all_courses
onboarding_adapted_see_personalized_curriculum
onboarding_adapted_something_else
onboarding_adapted_terms
onboarding_adapted_terms_and_privacy
onboarding_continue
onboarding_curriculum_loading
onboarding_curriculum_see_personalized_plan
onboarding_device_preference_both
onboarding_device_preference_desktop
onboarding_device_preference_phone
onboarding_device_preference_title
onboarding_device_reassurance_both_description
onboarding_device_reassurance_both_title
onboarding_device_reassurance_desktop_description
onboarding_device_reassurance_desktop_title
onboarding_device_reassurance_phone_description
onboarding_device_reassurance_phone_title
onboarding_get_started
onboarding_idea_booking_system_title
onboarding_intro_slides_already_have_an_account
onboarding_motive_reassurance_build
onboarding_motive_reassurance_career
onboarding_motive_reassurance_other_fun
onboarding_motive_reassurance_title
onboarding_motive_reassurance_work_or_school
onboarding_page_1_description
onboarding_page_1_title
onboarding_page_2_description
onboarding_page_2_title
onboarding_page_3_description
onboarding_page_3_title
onboarding_page_5_description
onboarding_page_5_title
onboarding_path_completion_estimation_title
onboarding_path_reassurance_description
onboarding_path_reassurance_description_ai
onboarding_path_reassurance_title_ai
onboarding_path_reassurance_title_other
onboarding_path_reassurance_title_python
onboarding_path_reassurance_title_web_development
onboarding_path_technologies
onboarding_path_type_career_path
onboarding_path_type_career_paths
onboarding_pick_a_path_all_options_title
onboarding_pick_a_path_choice_see_all_options
onboarding_pick_a_path_early_access
onboarding_pick_a_path_interests_ai
onboarding_pick_a_path_interests_automation
onboarding_pick_a_path_interests_data_science
onboarding_pick_a_path_interests_games
onboarding_pick_a_path_interests_not_sure
onboarding_pick_a_path_interests_title
onboarding_pick_a_path_interests_webapps
onboarding_pick_a_path_preference_appearance
onboarding_pick_a_path_preference_both
onboarding_pick_a_path_preference_logic
onboarding_pick_a_path_preference_title
onboarding_pick_a_path_recommendation_subtitle
onboarding_pick_a_path_recommendation_title
onboarding_pick_a_path_recommended
onboarding_set_daily_goal_title
onboarding_set_experience_little_description
onboarding_set_experience_little_title
onboarding_set_experience_lot_description
onboarding_set_experience_lot_title
onboarding_set_experience_none_description
onboarding_set_experience_none_title
onboarding_set_experience_title
onboarding_set_goal_better_screen_time
onboarding_set_goal_build_habit
onboarding_set_goal_build_myself
onboarding_set_goal_build_skills
onboarding_set_goal_build_something
onboarding_set_goal_enjoy_coding
onboarding_set_goal_find_opportunities
onboarding_set_goal_get_a_job
onboarding_set_goal_quick_result
onboarding_set_goal_sharp_mind
onboarding_set_goal_title
onboarding_set_goal_try_coding
onboarding_set_goal_understand_tech
onboarding_set_motive_build
onboarding_set_motive_fun_and_learn
onboarding_set_motive_improve
onboarding_set_motive_none
onboarding_set_motive_switch_career
onboarding_set_motive_title
onboarding_set_occupation_high_school_student
onboarding_set_occupation_none
onboarding_set_occupation_professional
onboarding_set_occupation_self_employed
onboarding_set_occupation_title
onboarding_set_occupation_university_student
onboarding_set_work_function_admin_finance
onboarding_set_work_function_customer_support
onboarding_set_work_function_marketing
onboarding_set_work_function_other
onboarding_set_work_function_product_management
onboarding_set_work_function_sales
onboarding_set_work_function_software_it_data
onboarding_set_work_function_title
onboarding_skill_preference_ai
onboarding_skill_preference_coding
onboarding_skill_preference_data
onboarding_skill_preference_subtitle
onboarding_skill_preference_title
sign_up_headline_onboarding
```

## ۴. رنگ‌های مرتبط (فهرست کامل)

(none)

## ۵. دایمنشن‌های مرتبط (فهرست کامل)

```text
onboarding_container_intro_slides_dots_margin_vertical
onboarding_container_margin_bottom
onboarding_container_slider_description_margin_bottom
onboarding_indicator_margin
onboarding_set_goal_item_height
onboarding_set_goal_margin_horizontal
```

## ۶. استایل‌های مرتبط (فهرست کامل)

(none)

## ۷. شواهد حالت‌ها (رشته‌های منبع)

```text
onboarding_curriculum_loading
```

## ۸. ناوبری / deep link

(هیچ intent-filter/data برای این سطح اعلان نشده)
