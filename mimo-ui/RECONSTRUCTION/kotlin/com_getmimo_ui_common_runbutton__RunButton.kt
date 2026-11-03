// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.common.runbutton

import com.getmimo.R

// superclass (DEX): Landroid/widget/FrameLayout;
// annotations (DEX): Ldalvik/annotation/MemberClasses;, Lkotlin/Metadata;
class RunButton : android.widget.FrameLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.run_button_view   →  SOURCE/res/layout/run_button_view.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.run_button_view)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.btn_submit, R.id.btn_continue_big, R.id.btn_play

    // Method inventory recovered from DEX (4 methods):
    // DEX: getOnContinueButtonClick()Lua0/s;
    // DEX: getOnRunButtonClick()Lua0/s;
    // DEX: setRunButtonState(Lcom/getmimo/ui/common/runbutton/RunButton$State;)V
}
