// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.leaderboard

import com.getmimo.R

// superclass (DEX): Lwl/a;
// annotations (DEX): Lkotlin/Metadata;
class c : wl.a {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.leaderboard_fragment   →  SOURCE/res/layout/leaderboard_fragment.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.leaderboard_fragment)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.layout_leaderboard_active, R.id.layout_leaderboard_locked, R.id.layout_leaderboard_offline, R.id.tv_leaderboard_fragment_locked_header, R.id.tv_leaderboard_fragment_locked_message, R.id.anonymous_user_lock_view, R.id.appbar_leaderboard, R.id.pb_leaderboard_loading_progress, R.id.layout_toolbar, R.id.leaderboard_league_header_view, R.id.leaderboard_league_header_view_locked, R.id.iv_leaderboard_fragment_locked_illustration, R.id.srl_leaderboard_refresh_layout, R.id.btn_leaderboard_fragment_locked_jump_into_lesson, R.id.rv_leaderboard

    // Method inventory recovered from DEX (10 methods):
    // DEX: E(Landroid/os/Bundle;)V
    // DEX: G(Landroid/view/LayoutInflater; Landroid/view/ViewGroup; Landroid/os/Bundle;)Landroid/view/View;
    // DEX: I()V
    // DEX: R()V
    // DEX: T(Landroid/view/View; Landroid/os/Bundle;)V
    // DEX: i0()V
    // DEX: k0()V
    // DEX: l0()V
    // DEX: o0()Lcom/getmimo/ui/leaderboard/LeaderboardViewModel;
}
