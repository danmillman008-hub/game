// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.onboarding.occupation

import com.getmimo.R

// superclass (DEX): Lln/a;
// annotations (DEX): Lkotlin/Metadata;
class SetOccupationFragment : ln.a {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.onboarding_step_2a_set_occupation_fragment   →  SOURCE/res/layout/onboarding_step_2a_set_occupation_fragment.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.onboarding_step_2a_set_occupation_fragment)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.btn_occupation_self_employed, R.id.layout_motive, R.id.nav_set_occupation, R.id.action_select_path, R.id.tv_set_occupation_title, R.id.nav_set_work_function, R.id.action_set_experience, R.id.action_set_work_function, R.id.btn_occupation_high_school, R.id.btn_occupation_none, R.id.btn_occupation_professional, R.id.btn_occupation_university

    // Method inventory recovered from DEX (5 methods):
    // DEX: G(Landroid/view/LayoutInflater; Landroid/view/ViewGroup; Landroid/os/Bundle;)Landroid/view/View;
    // DEX: I()V
    // DEX: T(Landroid/view/View; Landroid/os/Bundle;)V
    // DEX: m0(Lcom/getmimo/analytics/properties/OnboardingOccupation;)V
}
