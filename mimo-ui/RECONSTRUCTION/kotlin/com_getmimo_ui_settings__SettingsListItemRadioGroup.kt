// RECONSTRUCTED SKELETON — not decompiled source.
// Evidence: DEX class/method table + const resource-id operands (SOURCE/dex/UI_CLASSES.json).
// APK SHA-256: 48ce1740aa4b1f892a267ae54199d514d929b97e947b612f4e53c3571e0f7c7a
package com.getmimo.ui.settings

import com.getmimo.R

// superclass (DEX): Lcom/getmimo/ui/settings/SettingsListItem;
// annotations (DEX): Lkotlin/Metadata;
class SettingsListItemRadioGroup : com.getmimo.ui.settings.SettingsListItem {

    // Layout inflated by this class (DEX const operand → R.layout):
    //   R.layout.settings_list_item_radio_group   →  SOURCE/res/layout/settings_list_item_radio_group.xml
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.settings_list_item_radio_group)  // recovered from LayoutInflater.inflate(I)
    }

    // IDs referenced by this class' bytecode:
    //   R.id.tv_settings_item_radio_group_group, R.id.iv_settings_item_radio_group_group_icon, R.id.tv_settings_item_radio_group_group_title

    // Method inventory recovered from DEX (8 methods):
    // DEX: a()V
    // DEX: b(Ljava/util/List; Ljava/lang/Integer;)V
    // DEX: getIcon()Landroid/widget/ImageView;
    // DEX: getListener()Lzo/n;
    // DEX: getTextView()Landroid/widget/TextView;
    // DEX: setListener(Lzo/n;)V
    // DEX: setTitle(Ljava/lang/CharSequence;)V
}
