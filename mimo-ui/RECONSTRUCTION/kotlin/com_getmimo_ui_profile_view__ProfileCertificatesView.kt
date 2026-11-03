// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.profile.view

import com.getmimo.R

// superclass (DEX): Landroidx/cardview/widget/CardView;
// annotations (DEX): Lkotlin/Metadata;
class ProfileCertificatesView : androidx.cardview.widget.CardView {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.profile_certificate_view   →  SOURCE/res/layout/profile_certificate_view.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.profile_certificate_view)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.v_separator, R.id.tv_certificate_progress_text, R.id.certificate_progress, R.id.profile_paths_container, R.id.iv_certificate_download, R.id.iv_certificate_icon, R.id.tv_certificate_title

    // Method inventory recovered from DEX (4 methods):
    // DEX: b(Ljava/util/List; Z)V
    // DEX: getOnCertificateClickListener()Lo70/j;
    // DEX: setOnCertificateClickListener(Lo70/j;)V
}
