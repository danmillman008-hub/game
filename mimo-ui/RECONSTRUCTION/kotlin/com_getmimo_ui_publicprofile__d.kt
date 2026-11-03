// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.publicprofile

import com.getmimo.R

// superclass (DEX): Lij/g;
// annotations (DEX): Lkotlin/Metadata;
class d : ij.g {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.public_profile_code_header_view   →  SOURCE/res/layout/public_profile_code_header_view.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.public_profile_code_header_view)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.appbar_profile, R.id.profile_offline_view, R.id.rv_profile, R.id.layout_toolbar

    // Method inventory recovered from DEX (5 methods):
    // DEX: E(Landroid/os/Bundle;)V
    // DEX: G(Landroid/view/LayoutInflater; Landroid/view/ViewGroup; Landroid/os/Bundle;)Landroid/view/View;
    // DEX: T(Landroid/view/View; Landroid/os/Bundle;)V
    // DEX: p0()Lcom/getmimo/ui/publicprofile/PublicProfileViewModel;
}
