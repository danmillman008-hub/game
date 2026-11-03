// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.iap.allplans

import com.getmimo.R

// superclass (DEX): Landroid/widget/LinearLayout;
// annotations (DEX): Lkotlin/Metadata;
class SubscriptionPodiumButton : android.widget.LinearLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.subscription_podium_button   →  SOURCE/res/layout/subscription_podium_button.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.subscription_podium_button)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.view_iap_separator_1, R.id.view_iap_separator_2, R.id.tv_iap_button_podium_big_save_percent, R.id.tv_iap_countdown_promotion_percentage, R.id.tv_iap_countdown_timer, R.id.tv_in_app_button_free_trial, R.id.tv_in_app_button_podium_big_period, R.id.tv_in_app_button_podium_big_price, R.id.tv_in_app_button_podium_big_title, R.id.tv_in_app_button_podium_billing, R.id.cv_in_app_button, R.id.layout_iap_podium_big_countdown

    // Method inventory recovered from DEX (4 methods):
    // DEX: a(Lcom/getmimo/ui/iap/allplans/SubscriptionPodiumButton; Lxg/a;)V
    // DEX: setSavePercentReduction(Ljava/lang/Integer;)V
    // DEX: setDiscountState(Lhl/c;)V
}
