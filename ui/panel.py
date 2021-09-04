import bpy
from .tool.maximize_prefs import emm
from bpy.types import Panel, UIList
from bpy.utils import register_class, unregister_class

class EMM_VIEW3D_PT_N_Panel(Panel):
    bl_idname = "EMM_VIEW3D_PT_N_PANEL"
    bl_label = "插件预设"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "EMM"
    # bl_context = "win"
    bl_options = {'DEFAULT_CLOSED'}


    def draw(self, context):
        emm(self, context)


class EMM_PT_check_slow(Panel):
    bl_idname = "EMM_VIEW3D_PT_CHECK_SLOW"
    bl_label = "检查列表"
    bl_space_type = EMM_VIEW3D_PT_N_Panel.bl_space_type
    bl_region_type = EMM_VIEW3D_PT_N_Panel.bl_region_type
    bl_category = EMM_VIEW3D_PT_N_Panel.bl_category
    # bl_context = EMM_VIEW3D_PT_N_Panel.bl_context
    bl_options = {'DEFAULT_CLOSED'}

    

    def draw(self, context):
        layout = self.layout

        # sn = bpy.context.scene.name
        # obj = bpy.data.scenes[sn].objects

        # acto = bpy.context.active_object
        C = context
        S =C.scene
        # layout.template_list(
        #     "OBJECT_UL_render_check_slow",      #list type_name
        #     "",                  #list_id
        #     S,  # dataptr 获取集合属性的数据  
        #     'objects',  # propname数据中集合属性的标识符 string
        #     S.objects,  # active_dataptr 活动项数据中整数属性的标识符，活动项的索引AnyType
        #     str(C.active_object.name)         # string active_propname            
        # )
        # layout.template_list("OBJECT_UL_render_check_slow",     "",     obj,    "vertex_groups",    obj.vertex_groups,  "active_index")
        # layout.template_list("OBJECT_UL_render_check_slow", "compact", obj,    "material_slots",   obj,                "active_material_index", type='COMPACT')


# bpy.data.objects["Cube"].active_material_index
