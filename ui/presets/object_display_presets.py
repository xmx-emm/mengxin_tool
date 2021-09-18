# 预设菜单
import bpy
from bpy.types import Operator, Panel, UILayout
from bl_operators.presets import AddPresetBase
from ...utils.registration import get_prefs
from bpy.utils import register_class, unregister_class
from bl_ui.utils import PresetPanel
from bl_ui.properties_object import OBJECT_PT_display


class OBJECT_PT_display_presets(PresetPanel, Panel, UILayout):
    bl_label = "Object Display Presets"
    preset_subdir = "emmmmm/object/display"
    preset_operator = "script.execute_preset"
    preset_add_operator = 'emm.object_display_preset_add'


class AddPresetObjectDisplay(AddPresetBase, Operator):
    bl_idname = "emm.object_display_preset_add"
    bl_label = "Add Object Display Preset"
    preset_menu = "OBJECT_PT_display_presets"

    # 用于存储预设值的变量 <exec>  variable used for all preset values
    preset_defines = ["obj = bpy.context.object"]

    # 存储在预设中的属性列表 <eval> properties to store in the preset
    preset_values = ["obj.display_type",
                     "obj.show_bounds",
                     "obj.display_bounds_type",
                     "obj.show_name",
                     "obj.show_axis",
                     "obj.show_wire",
                     "obj.show_all_edges",
                     "obj.show_texture_space",
                     "obj.display.show_shadows",
                     "obj.show_in_front",
                     "obj.color",
                     ]

    # 存储预设的位置
    # Mac: /用户/用户名/资源库/Application Support/Blender/2.92/scripts/presets/object/display
    # Win: C:/Users/用户名/....../2.92/scripts/presets/object/display
    preset_subdir = "emmmmm/object/display"


def object_display_preset(self, _context):
    OBJECT_PT_display_presets.draw_panel_header(self.layout)


classes = (
    OBJECT_PT_display,
)


def register():
    try:

        print(bpy.types.OBJECT_PT_display.draw_header_preset, '重写面板类')

        if get_prefs().object_display_presets == False:
            for i in classes:
                unregister_class(i)
            del OBJECT_PT_display.draw_header_preset
            for i in classes:
                register_class(i)
    except AttributeError:
        if get_prefs().object_display_presets:
            for i in classes:
                unregister_class(i)
            OBJECT_PT_display.draw_header_preset = object_display_preset
            for i in classes:
                register_class(i)
        else:
            pass

def unregister():
    try:
        print(bpy.types.OBJECT_PT_display.draw_header_preset, '重写面板类')
        for i in classes:
            unregister_class(i)
        del OBJECT_PT_display.draw_header_preset
        for i in classes:
            register_class(i)
    except AttributeError:
        pass
