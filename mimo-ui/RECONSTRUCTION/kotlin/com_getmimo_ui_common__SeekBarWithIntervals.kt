// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.common

import com.getmimo.R

// superclass (DEX): Landroidx/constraintlayout/widget/ConstraintLayout;
// annotations (DEX): Ldalvik/annotation/Signature;, Lkotlin/Metadata;
class SeekBarWithIntervals : androidx.constraintlayout.widget.ConstraintLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.seekbar_with_intervals   →  SOURCE/res/layout/seekbar_with_intervals.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.seekbar_with_intervals)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.intervals_dots, R.id.intervals_text, R.id.iv_interval_dot, R.id.seekbar, R.id.textViewInterval

    // Method inventory recovered from DEX (8 methods):
    // DEX: k(I)Lbk/s;
    // DEX: l(I)V
    // DEX: m(Lbk/s; I)V
    // DEX: n()V
    // DEX: setIntervals(Ljava/util/List;)V
    // DEX: setOnIntervalChangeListener(Lbk/r;)V
    // DEX: setProgress(I)V
}
