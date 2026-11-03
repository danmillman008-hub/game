// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.leaderboard

import com.getmimo.R

// superclass (DEX): Lwl/b;
// annotations (DEX): Lkotlin/Metadata;
class f : wl.b {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.leaderboard_result_podium_promotion_shareable_image   →  SOURCE/res/layout/leaderboard_result_podium_promotion_shareable_image.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.leaderboard_result_podium_promotion_shareable_image)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.tv_leaderboard_result_header, R.id.tv_leaderboard_result_message, R.id.tv_leaderboard_result_time, R.id.tv_mimo_app_link, R.id.iv_leaderboard_result_illustration_neutral, R.id.iv_leaderboard_result_illustration_podium, R.id.iv_leaderboard_result_illustration_podium_league, R.id.iv_leaderboard_result_illustration_promotion_indicator, R.id.iv_leaderboard_result_illustration_promotion_league, R.id.iv_mimo_logo, R.id.container_leaderboard_result_illustration_podium

    // Method inventory recovered from DEX (4 methods):
    // DEX: r0()Ljava/lang/String;
    // DEX: u0()Lcom/getmimo/analytics/properties/story/ShareToStoriesSource;
    // DEX: v0(Landroid/widget/FrameLayout;)V
}
