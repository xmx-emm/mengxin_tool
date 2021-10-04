from ..utils.registration import get_prefs
import bpy
from bpy.props import EnumProperty, BoolProperty, StringProperty
from .menu import *



#顶部标题栏
def append_TOPBAR_MT_editor_menus(self, context):
    layout = self.layout
    row = layout.row(align=True)
    if get_prefs().restart_blender:
        a = row.row()
        a.alert = True
        a.operator(operator="emm.restart_blender",
                     text="", emboss=False, icon='QUIT')

    if get_prefs().console_toggle:
        row.operator(operator="wm.console_toggle",
                     text="", emboss=False, icon='CONSOLE')

    if get_prefs().switch_translate:
        row.operator(operator="emm.switch_translate", text="",
                     emboss=False, icon='OUTLINER_DATA_FONT')

#文本编辑器底栏
def append_TEXT_HT_header(self, context):
    if get_prefs().scripting_tool:
        preference = get_prefs()
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
        if get_prefs().auto_reload_script:
            if text and text.is_modified:
                get_prefs().reload_script = get_prefs().reload_script ^ True
                # Text = False

        #     else:
        #         pass
        #         # print('没有改')
        # else:
        #     # print('不重载')
        #     pass
    # bpy.types.USERPREF_PT_addons.draw

def 右键上下文菜单(self,context):
    layout = self.layout

    property_pointer = getattr(context, "button_pointer", None)
    property_value = getattr(context, "button_prop", None)
    button_value = getattr(context, "button_operator", None) 
    layout.operator(
        右键上下文菜单_cl.bl_idname, text="复制属性",
        icon='RNA')