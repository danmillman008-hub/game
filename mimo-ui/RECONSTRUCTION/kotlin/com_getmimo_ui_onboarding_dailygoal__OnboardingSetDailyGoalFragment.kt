// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.onboarding.dailygoal

import com.getmimo.R

// superclass (DEX): Landroidx/fragment/app/e0;
// annotations (DEX): Lkotlin/Metadata;
class OnboardingSetDailyGoalFragment : androidx.fragment.app.e0 {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.onboarding_set_daily_goal_fragment   →  SOURCE/res/layout/onboarding_set_daily_goal_fragment.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.onboarding_set_daily_goal_fragment)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.compose_content, R.id.tv_set_daily_goal_title, R.id.tv_goal_subtitle, R.id.layout_daily_goal_card

    // Method inventory recovered from DEX (10 methods):
    // DEX: C(Landroid/app/Activity;)V
    // DEX: D(Landroid/content/Context;)V
    // DEX: K(Landroid/os/Bundle;)Landroid/view/LayoutInflater;
    // DEX: T(Landroid/view/View; Landroid/os/Bundle;)V
    // DEX: b()Ljava/lang/Object;
    // DEX: getDefaultViewModelProviderFactory()Landroidx/lifecycle/i1;
    // DEX: i0()Lcom/getmimo/ui/onboarding/dailygoal/OnboardingSetDailyGoalViewModel;
    // DEX: j0()V
    // DEX: m()Landroid/content/Context;
}
