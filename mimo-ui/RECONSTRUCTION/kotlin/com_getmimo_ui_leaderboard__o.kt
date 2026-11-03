// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.leaderboard

import com.getmimo.R

// superclass (DEX): Lwl/d;
// annotations (DEX): Lkotlin/Metadata;
class o : wl.d {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.leaderboard_result_standard_promotion_fragment   →  SOURCE/res/layout/leaderboard_result_standard_promotion_fragment.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.leaderboard_result_standard_promotion_fragment)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.iv_leaderboard_result_illustration_promotion_league, R.id.btn_share, R.id.btn_leaderboard_result_continue, R.id.tv_leaderboard_result_header, R.id.constraintLayout, R.id.tv_leaderboard_result_message, R.id.tv_leaderboard_result_time, R.id.iv_leaderboard_result_illustration_promotion_indicator

    // Method inventory recovered from DEX (4 methods):
    // DEX: G(Landroid/view/LayoutInflater; Landroid/view/ViewGroup; Landroid/os/Bundle;)Landroid/view/View;
    // DEX: I()V
    // DEX: T(Landroid/view/View; Landroid/os/Bundle;)V
}
