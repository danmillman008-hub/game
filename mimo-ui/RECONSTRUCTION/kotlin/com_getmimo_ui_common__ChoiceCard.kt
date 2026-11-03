// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.common

import com.getmimo.R

// superclass (DEX): Landroid/widget/LinearLayout;
// annotations (DEX): Lkotlin/Metadata;
class ChoiceCard : android.widget.LinearLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.layout_choice_card_separator   →  SOURCE/res/layout/layout_choice_card_separator.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.layout_choice_card_separator)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   (none)

    // Method inventory recovered from DEX (3 methods):
    // DEX: getSelectedItemInfo()Lbk/e;
    // DEX: setChoiceCardData(Ljava/util/List;)V
}
