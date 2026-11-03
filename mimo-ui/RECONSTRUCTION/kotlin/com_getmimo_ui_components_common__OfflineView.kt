// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.components.common

import com.getmimo.R

// superclass (DEX): Landroid/widget/FrameLayout;
// annotations (DEX): Lkotlin/Metadata;
class OfflineView : android.widget.FrameLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.offline_view   →  SOURCE/res/layout/offline_view.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.offline_view)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.tv_offline_description, R.id.tv_offline_header, R.id.iv_offline_illustration, R.id.btn_offline_refresh

    // Method inventory recovered from DEX (2 methods):
    // DEX: setRefreshOnClickListener(Lkotlin/jvm/functions/Function0;)V
}
