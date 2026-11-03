// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.leaderboard

import com.getmimo.R

// superclass (DEX): Landroid/widget/FrameLayout;
// annotations (DEX): Lkotlin/Metadata;
class LeaderboardLeagueHeaderView : android.widget.FrameLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.leaderboard_league_header_view   →  SOURCE/res/layout/leaderboard_league_header_view.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.leaderboard_league_header_view)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.frameLayout, R.id.tv_leaderboard_header_results_available_timer, R.id.tv_leaderboard_results_league_label, R.id.rv_leaderboard_result_leagues

    // Method inventory recovered from DEX (3 methods):
    // DEX: setLeagueInfo(Lwl/i0;)V
    // DEX: setLeagueInfoForIndex(I)V
}
