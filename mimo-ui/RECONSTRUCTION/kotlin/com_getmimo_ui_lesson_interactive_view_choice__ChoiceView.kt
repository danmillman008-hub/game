// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.lesson.interactive.view.choice

import com.getmimo.R

// superclass (DEX): Landroid/widget/LinearLayout;
// annotations (DEX): Lkotlin/Metadata;
class ChoiceView : android.widget.LinearLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.choice_view   →  SOURCE/res/layout/choice_view.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.choice_view)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.rv_multiplechoice_options, R.id.tv_multiplechoice_hint

    // Method inventory recovered from DEX (3 methods):
    // DEX: getOnItemClick()Lo70/j;
    // DEX: setOnItemClick(Lo70/j;)V
}
