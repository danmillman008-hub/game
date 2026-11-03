// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.profile.view

import com.getmimo.R

// superclass (DEX): Landroidx/constraintlayout/widget/ConstraintLayout;
// annotations (DEX): Ldalvik/annotation/MemberClasses;, Lkotlin/Metadata;
class ProfileHeaderView : androidx.constraintlayout.widget.ConstraintLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.profile_header_view   →  SOURCE/res/layout/profile_header_view.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.profile_header_view)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.btn_unfollow, R.id.barrier_bio_bottom, R.id.tv_profile_header_bio, R.id.profile_header_unlocked, R.id.profile_info_card_league, R.id.profile_info_card_longest_streak, R.id.profile_info_card_streak, R.id.profile_info_card_xp, R.id.iv_settings_user_picture, R.id.tv_settings_max_badge, R.id.tv_settings_premium_badge, R.id.tv_settings_user_name, R.id.btn_follow, R.id.btn_profile_header_add_bio, R.id.btn_profile_header_upgrade, R.id.cw_share_my_progress

    // Method inventory recovered from DEX (18 methods):
    // DEX: setBadge(Lcom/getmimo/data/source/remote/iap/model/SubscriptionTier;)V
    // DEX: setBioState(Lcom/getmimo/data/model/profile/BiographyState;)V
    // DEX: setProfileHeaderState(Lgo/b;)V
    // DEX: setProfilePictureWithUrl(Ljava/lang/String;)V
    // DEX: setUserLeagueInformation(I)V
    // DEX: setUserLevelInformation(Lii/a;)V
    // DEX: setUserStreak(I)V
    // DEX: getFollowAction()Lcom/getmimo/ui/profile/view/ProfileHeaderView$FollowAction;
    // DEX: getOnAddBioClickListener()Lkotlin/jvm/functions/Function0;
    // DEX: getOnFollowButtonClickListener()Lo70/j;
    // DEX: k(Lko/b; Lko/d;)V
    // DEX: l(Z)V
    // DEX: m(Lgo/a;)V
    // DEX: setFollowAction(Lcom/getmimo/ui/profile/view/ProfileHeaderView$FollowAction;)V
    // DEX: setOnAddBioClickListener(Lkotlin/jvm/functions/Function0;)V
    // DEX: setOnFollowButtonClickListener(Lo70/j;)V
    // DEX: setShareMyProgressBtn(Lkotlin/jvm/functions/Function0;)V
}
