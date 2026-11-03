// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.profile.view

import com.getmimo.R

// superclass (DEX): Landroidx/cardview/widget/CardView;
// annotations (DEX): Lkotlin/Metadata;
class ProfileInfoCard : androidx.cardview.widget.CardView {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.profile_info_card_view   →  SOURCE/res/layout/profile_info_card_view.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.profile_info_card_view)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.iv_profile_card_icon, R.id.tv_profile_card_label, R.id.tv_profile_card_value, R.id.profile_card_placeholder

    // Method inventory recovered from DEX (2 methods):
    // DEX: b(I Ljava/lang/String; Ljava/lang/String;)V
}
