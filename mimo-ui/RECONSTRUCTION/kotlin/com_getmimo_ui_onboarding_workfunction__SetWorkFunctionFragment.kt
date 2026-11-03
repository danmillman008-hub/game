// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.onboarding.workfunction

import com.getmimo.R

// superclass (DEX): Lun/a;
// annotations (DEX): Lkotlin/Metadata;
class SetWorkFunctionFragment : un.a {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.onboarding_step_2b_set_work_function_fragment   →  SOURCE/res/layout/onboarding_step_2b_set_work_function_fragment.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.onboarding_step_2b_set_work_function_fragment)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.action_select_path, R.id.action_set_experience, R.id.tv_set_work_function_title, R.id.btn_work_function_admin_finance, R.id.btn_work_function_customer_support, R.id.btn_work_function_marketing, R.id.btn_work_function_other, R.id.btn_work_function_product_management, R.id.btn_work_function_sales, R.id.btn_work_function_software_it_data, R.id.layout_work_functions

    // Method inventory recovered from DEX (5 methods):
    // DEX: G(Landroid/view/LayoutInflater; Landroid/view/ViewGroup; Landroid/os/Bundle;)Landroid/view/View;
    // DEX: I()V
    // DEX: T(Landroid/view/View; Landroid/os/Bundle;)V
    // DEX: m0(Lcom/getmimo/analytics/properties/OnboardingWorkFunction;)V
}
