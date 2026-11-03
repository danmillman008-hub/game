// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.lesson.view

import com.getmimo.R

// superclass (DEX): Landroid/widget/LinearLayout;
// annotations (DEX): Lkotlin/Metadata;
class InteractionKeyboardContainerView : android.widget.LinearLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.interaction_keyboard_with_lesson_feedback   →  SOURCE/res/layout/interaction_keyboard_with_lesson_feedback.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.interaction_keyboard_with_lesson_feedback)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.fillthegap_view, R.id.interaction_keyboard

    // Method inventory recovered from DEX (9 methods):
    // DEX: getFillTheGapView()Lcom/getmimo/ui/lesson/view/tags/TagSelectionView;
    // DEX: getOnContinueButtonClick()Lua0/s;
    // DEX: getOnResetButtonClick()Lua0/s;
    // DEX: getOnRunButtonClick()Lua0/s;
    // DEX: getOnUndoButtonClick()Lua0/s;
    // DEX: setResetButtonState(Lcom/getmimo/ui/lesson/view/InteractionKeyboardButtonState;)V
    // DEX: setRunButtonState(Lcom/getmimo/ui/common/runbutton/RunButton$State;)V
    // DEX: setUndoButtonState(Lcom/getmimo/ui/lesson/view/InteractionKeyboardButtonState;)V
}
