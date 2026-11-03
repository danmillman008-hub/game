// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.upgrade

import com.getmimo.R

// superclass (DEX): Landroidx/constraintlayout/widget/ConstraintLayout;
// annotations (DEX): Lkotlin/Metadata;
class UpgradeModalBottomView : androidx.constraintlayout.widget.ConstraintLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.upgrade_modal_bottom_view   →  SOURCE/res/layout/upgrade_modal_bottom_view.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.upgrade_modal_bottom_view)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.tv_countdown_timer, R.id.btn_upgrade_modal_other_plans, R.id.btn_upgrade_modal_upgrade, R.id.view_bottom_part, R.id.tv_yearly_price

    // Method inventory recovered from DEX (11 methods):
    // DEX: getUpgradeBtnText()Ljava/lang/String;
    // DEX: k(Lcom/getmimo/ui/upgrade/UpgradeModalBottomView; Lg1/j; I)V
    // DEX: setUpgradeBtnEnabled(Z)V
    // DEX: setUpgradeBtnText(Ljava/lang/String;)V
    // DEX: getOnOtherPlanClick()Lkotlin/jvm/functions/Function0;
    // DEX: getOnUpgradeClick()Lkotlin/jvm/functions/Function0;
    // DEX: setDiscountState(Lhl/c;)V
    // DEX: setOnOtherPlanClick(Lkotlin/jvm/functions/Function0;)V
    // DEX: setOnUpgradeClick(Lkotlin/jvm/functions/Function0;)V
    // DEX: setViewState(Lhl/f;)V
}
