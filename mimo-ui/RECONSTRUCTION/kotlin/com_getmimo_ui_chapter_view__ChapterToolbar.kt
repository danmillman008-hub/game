// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.chapter.view

import com.getmimo.R

// superclass (DEX): Landroidx/constraintlayout/widget/ConstraintLayout;
// annotations (DEX): Lkotlin/Metadata;
class ChapterToolbar : androidx.constraintlayout.widget.ConstraintLayout {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.chapter_toolbar   →  SOURCE/res/layout/chapter_toolbar.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.chapter_toolbar)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.tv_chapter_toolbar_label, R.id.btn_lesson_close, R.id.btn_lesson_report, R.id.v_line, R.id.tv_lesson_streak_chapter_toolbar, R.id.pb_chapter

    // Method inventory recovered from DEX (8 methods):
    // DEX: getProgressBar()Lcom/getmimo/ui/common/SpringAnimatingProgressBar;
    // DEX: getCloseButton()Landroid/widget/ImageView;
    // DEX: getReportButton()Landroid/widget/ImageView;
    // DEX: k(Z)V
    // DEX: l(I I Ljava/lang/String;)V
    // DEX: m(Ldj/n;)V
    // DEX: n(I I)V
}
