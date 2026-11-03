// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.streaks.bottomsheet

import com.getmimo.R

// superclass (DEX): Lx7/f0;
// annotations (DEX): 
class c : x7.f0 {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.calendar_month_item   →  SOURCE/res/layout/calendar_month_item.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.calendar_month_item)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.rv_month, R.id.progress_indicator, R.id.tv_error_message

    // Method inventory recovered from DEX (6 methods):
    // DEX: c(I)J
    // DEX: j(Lx7/d1; I)V
    // DEX: k(Landroid/view/ViewGroup; I)Lx7/d1;
    // DEX: t(I)Lkotlin/Pair;
}
