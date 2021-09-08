
import bpy
from bpy.utils import register_class , unregister_class


from bpy.types import Operator as OPS
from ...utils.blender_class import 渲染预设_PRESETS
from bpy.types import Menu, Panel, UIList

if  "RENDER_PT_format_presets" in dir(bpy.types):
    from bl_ui.properties_output import RENDER_PT_format_presets as 渲染预设_PRESETS_界面
elif  "RENDER_PT_presets" in dir(bpy.types):
    from bl_ui.properties_output import RENDER_PT_presets as 渲染预设_PRESETS_界面


if  "RENDER_PT_dimensions" in dir(bpy.types):
    from bl_ui.properties_output import RENDER_PT_dimensions as 渲染预设_PRESETS_题头
elif  "RENDER_PT_format" in dir(bpy.types):
    from bl_ui.properties_output import RENDER_PT_format as 渲染预设_PRESETS_题头


class render_resolution_switch(OPS, UIList):
    """切换分辨率"""
    bl_idname = 'emm.render_resolution_switch'
    bl_label = '切换翻译'
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = """点一下就可以切换XY的分辨率"""

    def execute(self, context):
        render = bpy.context.scene.render
        x = render.resolution_x
        y = render.resolution_y
        e = x

        render.resolution_x = y
        render.resolution_y = e

        return {'FINISHED'}
    
    # def __init__(self):
    def DRAW_HEADER_PRESET(self, _context):
        self.layout.operator(operator="emm.render_resolution_switch", emboss=False,text='',icon='UV_SYNC_SELECT')

        渲染预设_PRESETS_界面.draw_panel_header(self.layout)


    RENDER_PT_DIMENSIONS = 渲染预设_PRESETS_题头
    RENDER_PT_DIMENSIONS.draw_header_preset = DRAW_HEADER_PRESET
    
    def __del__(self):
        def DRAW_HEADE(self, _context):
            # self.layout.operator(operator="emm.render_resolution_switch", emboss=False,text='',icon='UV_SYNC_SELECT')
            渲染预设_PRESETS_界面.draw_panel_header(self.layout)
        RENDER_PT_DIMENSIONS = 渲染预设_PRESETS_题头
        RENDER_PT_DIMENSIONS.draw_header_preset = DRAW_HEADE
