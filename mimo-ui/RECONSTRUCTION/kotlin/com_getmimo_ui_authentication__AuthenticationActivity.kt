// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.authentication

import com.getmimo.R

// superclass (DEX): Lbl/b;
// annotations (DEX): Lkotlin/Metadata;
class AuthenticationActivity : bl.b {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.authentication_activity   →  SOURCE/res/layout/authentication_activity.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.authentication_activity)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.authentication_progress, R.id.container

    // Method inventory recovered from DEX (7 methods):
    // DEX: A(Laj/n;)V
    // DEX: onBackPressed()V
    // DEX: onCreate(Landroid/os/Bundle;)V
    // DEX: t()V
    // DEX: y()V
    // DEX: z()Lcom/getmimo/ui/authentication/t;
}
