// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.lesson.report

import com.getmimo.R

// superclass (DEX): Lvm/a;
// annotations (DEX): Lkotlin/Metadata;
class b : vm.a {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.report_lesson_fragment   →  SOURCE/res/layout/report_lesson_fragment.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.report_lesson_fragment)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.btn_report_lesson_close, R.id.btn_report_lesson_report, R.id.nsv_report_content, R.id.et_report_lesson_feedback, R.id.layout_report_lesson_choice_card, R.id.report_lesson_header, R.id.vf_report_lesson_view_flipper, R.id.tv_report_lesson_header, R.id.tv_report_lesson_title

    // Method inventory recovered from DEX (11 methods):
    // DEX: E(Landroid/os/Bundle;)V
    // DEX: G(Landroid/view/LayoutInflater; Landroid/view/ViewGroup; Landroid/os/Bundle;)Landroid/view/View;
    // DEX: I()V
    // DEX: O()V
    // DEX: T(Landroid/view/View; Landroid/os/Bundle;)V
    // DEX: k0()I
    // DEX: l0(Landroid/os/Bundle;)Landroid/app/Dialog;
    // DEX: q0()V
    // DEX: s0()V
    // DEX: t0()Lcom/getmimo/ui/lesson/report/ReportLessonViewModel;
}
