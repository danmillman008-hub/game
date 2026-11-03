// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.profile.view

import com.getmimo.R

// superclass (DEX): Landroid/widget/FrameLayout;
// annotations (DEX): Lkotlin/Metadata;
class SetDailyGoalCardItem : android.widget.FrameLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.set_daily_goal_card_item   →  SOURCE/res/layout/set_daily_goal_card_item.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.set_daily_goal_card_item)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.radio_daily_goal_level, R.id.tv_daily_goal_level_name, R.id.tv_daily_goal_level

    // Method inventory recovered from DEX (4 methods):
    // DEX: getUserGoal()Lcom/getmimo/ui/profile/UserGoal;
    // DEX: setChecked(Z)V
    // DEX: setUserGoal(Lcom/getmimo/ui/profile/UserGoal;)V
}
