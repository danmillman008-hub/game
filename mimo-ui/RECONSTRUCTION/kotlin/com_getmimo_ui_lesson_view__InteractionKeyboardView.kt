// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.lesson.view

import com.getmimo.R

// superclass (DEX): Landroidx/constraintlayout/widget/ConstraintLayout;
// annotations (DEX): Lkotlin/Metadata;
class InteractionKeyboardView : androidx.constraintlayout.widget.ConstraintLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.interaction_keyboard_view   →  SOURCE/res/layout/interaction_keyboard_view.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.interaction_keyboard_view)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.btn_reset, R.id.btn_run, R.id.btn_undo, R.id.border_top, R.id.fab_code_playground

    // Method inventory recovered from DEX (11 methods):
    // DEX: setResetBtnEnabled(Z)V
    // DEX: setUndoBtnEnabled(Z)V
    // DEX: getOnContinueButtonClick()Lua0/s;
    // DEX: getOnResetButtonClick()Lua0/s;
    // DEX: getOnRunButtonClick()Lua0/s;
    // DEX: getOnUndoButtonClick()Lua0/s;
    // DEX: setOnCodePlaygroundClickListener(Lkotlin/jvm/functions/Function0;)V
    // DEX: setResetButtonState(Lcom/getmimo/ui/lesson/view/InteractionKeyboardButtonState;)V
    // DEX: setRunButtonState(Lcom/getmimo/ui/common/runbutton/RunButton$State;)V
    // DEX: setUndoButtonState(Lcom/getmimo/ui/lesson/view/InteractionKeyboardButtonState;)V
}
