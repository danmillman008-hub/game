// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.base

import com.getmimo.R

// superclass (DEX): Laj/s;
// annotations (DEX): Lkotlin/Metadata;
class a : aj.s {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.generic_share_fragment   →  SOURCE/res/layout/generic_share_fragment.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.generic_share_fragment)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.layout_placeholder_original, R.id.layout_share, R.id.layout_share_options, R.id.layout_shareable_image, R.id.placeholder_1, R.id.placeholder_2, R.id.placeholder_3, R.id.placeholder_4, R.id.placeholder_5, R.id.placeholder_6, R.id.placeholder_7, R.id.placeholder_8, R.id.iv_share_facebook, R.id.iv_share_instagram, R.id.iv_share_others, R.id.tv_share_to, R.id.tv_tag

    // Method inventory recovered from DEX (7 methods):
    // DEX: T(Landroid/view/View; Landroid/os/Bundle;)V
    // DEX: l0(Landroid/os/Bundle;)Landroid/app/Dialog;
    // DEX: q0()I
    // DEX: s0()I
    // DEX: u0()Lcom/getmimo/analytics/properties/story/ShareToStoriesSource;
    // DEX: v0(Landroid/widget/FrameLayout;)V
}
