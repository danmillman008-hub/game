// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.common

import com.getmimo.R

// superclass (DEX): Landroidx/constraintlayout/widget/ConstraintLayout;
// annotations (DEX): Ldalvik/annotation/MemberClasses;, Lkotlin/Metadata;
class CodeViewActionButton : androidx.constraintlayout.widget.ConstraintLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.code_view_action_button   →  SOURCE/res/layout/code_view_action_button.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.code_view_action_button)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.iv_code_view_action_button, R.id.tv_code_view_action_button

    // Method inventory recovered from DEX (2 methods):
    // DEX: setButtonState(Lcom/getmimo/ui/common/CodeViewActionButton$ButtonState;)V
}
