// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.profile.view

import com.getmimo.R

// superclass (DEX): Landroid/widget/FrameLayout;
// annotations (DEX): Lkotlin/Metadata;
class SetDailyGoalCard : android.widget.FrameLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.set_daily_goal_card   →  SOURCE/res/layout/set_daily_goal_card.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.set_daily_goal_card)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.daily_goal_level_1, R.id.daily_goal_level_2, R.id.daily_goal_level_3, R.id.line_daily_goal_level_1, R.id.line_daily_goal_level_2

    // Method inventory recovered from DEX (6 methods):
    // DEX: a(I)V
    // DEX: getSelectedGoalIndex()Ljava/lang/Integer;
    // DEX: getSelectedUserGoal()Lcom/getmimo/ui/profile/UserGoal;
    // DEX: setOnClickListener(Loo/e;)V
    // DEX: setSelectedGoalIndex(Ljava/lang/Integer;)V
}
