from ..utils.registration import get_emm_prefs
import bpy
from bpy.props import EnumProperty, BoolProperty, StringProperty




#顶部标题栏
def append_TOPBAR_MT_editor_menus(self, context):
    layout = self.layout
    row = layout.row(align=True)
    if get_emm_prefs().restart_blender:
        a = row.row()
        a.alert = True
        a.operator(operator="emm.restart_blender",
                     text="", emboss=False, icon='QUIT')

    if get_emm_prefs().console_toggle:
        row.operator(operator="wm.console_toggle",
                     text="", emboss=False, icon='CONSOLE')

    if get_emm_prefs().switch_translate:
        row.operator(operator="emm.switch_translate", text="",
                     emboss=False, icon='OUTLINER_DATA_FONT')

#文本编辑器底栏

def append_TEXT_HT_header(self, context):
    if get_emm_prefs().scripting_tool:
        preference = get_emm_prefs()
        layout = self.layout
        row = layout.row(align=True)
        row.prop(preference, 'auto_reload_script', text="",
                 toggle=True, icon="FILE_REFRESH")
        if preference.auto_reload_script:
            row.prop(preference, 'auto_run_script', text="",
                        toggle=True, icon="PLAY")

        row.operator(operator="emm.scripting_tool",
                     text="", emboss=False, icon='COPYDOWN')


        context = bpy.context
        st = context.space_data
        text = st.text

        
        # t = bpy.context.space_data.text.filepath
        if get_emm_prefs().auto_reload_script:
            if text and text.is_modified:
                get_emm_prefs().reload_script = get_emm_prefs().reload_script ^ True
                # Text = False

        #     else:
        #         pass
        #         # print('没有改')
        # else:
        #     # print('不重载')
        #     pass
# bpy.types.USERPREF_PT_addons.draw
