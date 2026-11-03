// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.navigation

import com.getmimo.R

// superclass (DEX): Landroid/widget/FrameLayout;
// annotations (DEX): Ldalvik/annotation/MemberClasses;, Lkotlin/Metadata;
class NavigationBar : android.widget.FrameLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.bottom_navigation_view   →  SOURCE/res/layout/bottom_navigation_view.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.bottom_navigation_view)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.bottom_navigation_item_leaderboard, R.id.bottom_navigation_item_practice, R.id.bottom_navigation_item_profile, R.id.bottom_navigation_item_track

    // Method inventory recovered from DEX (10 methods):
    // DEX: a(Lcom/getmimo/ui/navigation/NavigationBar; Len/k;)V
    // DEX: setActive(Len/k;)V
    // DEX: b(I Z)V
    // DEX: onAttachedToWindow()V
    // DEX: onDetachedFromWindow()V
    // DEX: onMeasure(I I)V
    // DEX: onRestoreInstanceState(Landroid/os/Parcelable;)V
    // DEX: onSaveInstanceState()Landroid/os/Parcelable;
}
