// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.codeeditor.codingkeyboard

import com.getmimo.R

// superclass (DEX): Landroid/widget/FrameLayout;
// annotations (DEX): Lkotlin/Metadata;
class CodingKeyboardView : android.widget.FrameLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.coding_keyboard_layout   →  SOURCE/res/layout/coding_keyboard_layout.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.coding_keyboard_layout)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.group_coding_keyboard_aware, R.id.btn_run_code_coding_keyboard, R.id.background, R.id.btn_ai_tutor, R.id.view_coding_keyboard_gradient, R.id.iv_ai_tutor_pulse, R.id.rv_coding_keyboard

    // Method inventory recovered from DEX (8 methods):
    // DEX: b(Lcom/getmimo/ui/codeeditor/codingkeyboard/CodingKeyboardView; Ljava/util/ArrayList;)V
    // DEX: getCodingKeyboardAdapter()Lsj/a;
    // DEX: a(Lcom/getmimo/data/model/codeeditor/codingkeyboard/CodingKeyboardLayout; Lxn/p;)V
    // DEX: getCodingKeyboardLayout()Lcom/getmimo/data/model/codeeditor/codingkeyboard/CodingKeyboardLayout;
    // DEX: getOnAiTutorClicked()Lkotlin/jvm/functions/Function0;
    // DEX: setOnAiTutorClicked(Lkotlin/jvm/functions/Function0;)V
    // DEX: setRunButtonState(Lcom/getmimo/ui/common/runbutton/RunButton$State;)V
}
