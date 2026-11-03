// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.leaderboard

import com.getmimo.R

// superclass (DEX): Laj/n;
// annotations (DEX): Lkotlin/Metadata;
class e : aj.n {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.leaderboard_result_fragment   →  SOURCE/res/layout/leaderboard_result_fragment.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.leaderboard_result_fragment)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.btn_leaderboard_result_continue, R.id.tv_leaderboard_result_header, R.id.tv_leaderboard_result_message, R.id.tv_leaderboard_result_time, R.id.container_leaderboard_result_illustration_demotion, R.id.iv_leaderboard_result_illustration_demotion_indicator, R.id.iv_leaderboard_result_illustration_demotion_league, R.id.iv_leaderboard_result_illustration_header, R.id.iv_leaderboard_result_illustration_neutral

    // Method inventory recovered from DEX (5 methods):
    // DEX: G(Landroid/view/LayoutInflater; Landroid/view/ViewGroup; Landroid/os/Bundle;)Landroid/view/View;
    // DEX: I()V
    // DEX: T(Landroid/view/View; Landroid/os/Bundle;)V
    // DEX: l0(I)V
}
