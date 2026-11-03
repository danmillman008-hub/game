// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.lesson.interactive.webview

import com.getmimo.R

// superclass (DEX): Ltm/d;
// annotations (DEX): Lkotlin/Metadata;
class b : tm.d {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.lesson_interactive_webview_fragment   →  SOURCE/res/layout/lesson_interactive_webview_fragment.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.lesson_interactive_webview_fragment)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.feedback_container, R.id.database_view, R.id.feedback_sheet, R.id.layout_lesson_content, R.id.layout_lesson_description, R.id.lesson_output_layout, R.id.codebodyview, R.id.codeheaderview, R.id.sv_lesson_noninteractive, R.id.cv_lesson_hard_mode_label, R.id.interaction_keyboard_noninteractive

    // Method inventory recovered from DEX (27 methods):
    // DEX: M0(Lcom/getmimo/ui/lesson/interactive/webview/b;)V
    // DEX: A0(Ljm/p;)V
    // DEX: B0(Ljm/q;)V
    // DEX: D0(Lcom/getmimo/data/content/model/track/LessonContent$Interactive; Lcom/getmimo/ui/lesson/interactive/LessonBundle;)V
    // DEX: E0()V
    // DEX: F0(Z)V
    // DEX: G0()V
    // DEX: H0(Lxm/o;)V
    // DEX: I()V
    // DEX: J0()V
    // DEX: K0()Lcom/getmimo/ui/lesson/interactive/base/c;
    // DEX: N0()V
    // DEX: O0()Ldv/a;
    // DEX: P0()Lcom/getmimo/ui/lesson/interactive/webview/c;
    // DEX: T(Landroid/view/View; Landroid/os/Bundle;)V
    // DEX: l0()V
    // DEX: m0()V
    // DEX: p0()Lcom/getmimo/ui/lesson/view/code/CodeBodyView;
    // DEX: q0()Lcom/getmimo/ui/lesson/view/code/header/CodeHeaderView;
    // DEX: r0()Landroid/view/View;
    // DEX: t0()Lcom/getmimo/ui/lesson/view/database/DatabaseView;
    // DEX: u0()Lcom/getmimo/ui/lesson/view/InteractionKeyboardContainerView;
    // DEX: v0()I
    // DEX: w0()V
    // DEX: y0()V
    // DEX: z0(Ljava/util/List;)V
}
