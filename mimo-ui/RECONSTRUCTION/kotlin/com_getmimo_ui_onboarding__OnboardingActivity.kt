// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.onboarding

import com.getmimo.R

// superclass (DEX): Lbl/b;
// annotations (DEX): Ldalvik/annotation/MemberClasses;, Lkotlin/Metadata;
class OnboardingActivity : bl.b {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.onboarding_activity   →  SOURCE/res/layout/onboarding_activity.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.onboarding_activity)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.onboarding_progress_bar, R.id.onboarding_root, R.id.nav_path_completion_estimation

    // Method inventory recovered from DEX (4 methods):
    // DEX: onCreate(Landroid/os/Bundle;)V
    // DEX: onSaveInstanceState(Landroid/os/Bundle;)V
    // DEX: z(Li7/y;)V
}
