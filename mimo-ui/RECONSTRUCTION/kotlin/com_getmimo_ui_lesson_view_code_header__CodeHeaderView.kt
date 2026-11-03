// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.lesson.view.code.header

import com.getmimo.R

// superclass (DEX): Landroidx/constraintlayout/widget/ConstraintLayout;
// annotations (DEX): Lkotlin/Metadata;
class CodeHeaderView : androidx.constraintlayout.widget.ConstraintLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.code_header_view   →  SOURCE/res/layout/code_header_view.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.code_header_view)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.tab_start_margin, R.id.barrier_end_of_header, R.id.btn_action_add, R.id.code_header_run_button, R.id.btn_action, R.id.code_header_separator, R.id.code_header_tablayout, R.id.view_coding_keyboard_gradient_end, R.id.view_coding_keyboard_gradient_start

    // Method inventory recovered from DEX (5 methods):
    // DEX: getActionButton()Lcom/getmimo/ui/common/CodeViewActionButton;
    // DEX: getTabLayout()Lcom/google/android/material/tabs/TabLayout;
    // DEX: setActionButtonClickListener(Landroid/view/View$OnClickListener;)V
    // DEX: setActionButtonState(Lcom/getmimo/ui/common/CodeViewActionButton$ButtonState;)V
}
