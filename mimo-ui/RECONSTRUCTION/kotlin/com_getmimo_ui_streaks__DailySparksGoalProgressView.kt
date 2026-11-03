// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.streaks

import com.getmimo.R

// superclass (DEX): Landroid/widget/FrameLayout;
// annotations (DEX): Ldalvik/annotation/MemberClasses;, Lkotlin/Metadata;
class DailySparksGoalProgressView : android.widget.FrameLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.daily_sparks_goal_progress_view   →  SOURCE/res/layout/daily_sparks_goal_progress_view.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.daily_sparks_goal_progress_view)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.pb_daily_goal_progress_view, R.id.iv_daily_goal_progress_view_streak, R.id.tv_daily_goal_progress_view_current_sparks, R.id.tv_daily_goal_progress_view_daily_sparks, R.id.tv_daily_goal_progress_view_today

    // Method inventory recovered from DEX (7 methods):
    // DEX: setProgress(I)V
    // DEX: setProgressAnimated(I)V
    // DEX: setProgressColor(I)V
    // DEX: setTextStyle(Lcom/getmimo/ui/streaks/DailySparksGoalProgressView$TextStyle;)V
    // DEX: setTodayColor(I)V
    // DEX: setSparkProgress(Lgp/a;)V
}
