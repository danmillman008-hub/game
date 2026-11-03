// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.authentication

import com.getmimo.R

// superclass (DEX): Lcom/getmimo/ui/authentication/a;
// annotations (DEX): Lkotlin/Metadata;
class b : com.getmimo.ui.authentication.a {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.authentication_login_fragment   →  SOURCE/res/layout/authentication_login_fragment.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.authentication_login_fragment)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.btn_facebook_login, R.id.rive_login, R.id.tv_headline_authentication, R.id.tv_continue_with, R.id.btn_login_with_email, R.id.btn_back, R.id.cv_last_used_auth_method, R.id.tv_delete_account, R.id.layout_terms_conditions, R.id.btn_continue_facebook, R.id.btn_continue_google

    // Method inventory recovered from DEX (5 methods):
    // DEX: G(Landroid/view/LayoutInflater; Landroid/view/ViewGroup; Landroid/os/Bundle;)Landroid/view/View;
    // DEX: H()V
    // DEX: n0(Landroid/view/View;)V
    // DEX: o0(Lg1/j; I)V
}
