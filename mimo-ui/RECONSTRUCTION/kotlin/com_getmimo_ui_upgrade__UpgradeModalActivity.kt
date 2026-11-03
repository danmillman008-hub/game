// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.upgrade

import com.getmimo.R

// superclass (DEX): Lbl/b;
// annotations (DEX): Lkotlin/Metadata;
class UpgradeModalActivity : bl.b {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.upgrade_modal_activity   →  SOURCE/res/layout/upgrade_modal_activity.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.upgrade_modal_activity)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.upgrade_modal_bottom_view, R.id.iv_upgrade_modal_close, R.id.vp_in_app, R.id.vpi_in_app

    // Method inventory recovered from DEX (7 methods):
    // DEX: finish()V
    // DEX: onCreate(Landroid/os/Bundle;)V
    // DEX: t()V
    // DEX: u()Z
    // DEX: y()V
    // DEX: z()Lcom/getmimo/ui/iap/a;
}
