# import preferences
import bpy
import inspect
import sys
from bpy.types import Panel, UIList
from bpy.utils import register_class, unregister_class
# from bl_ui.properties_paint_common

from .presets.node_渐变_presets import NODE_PT_ColorRamp_Presets
from .tool.maximize_prefs import emm
from .. utils.registration import get_prefs
from .. utils.blender_class import TIME_PT_PLAYBACK动画播放
from bl_ui.space_time import TIME_PT_playback as TIME_PT_PLAYBACK
TIME_PT_PLAYBACK__DRAW = TIME_PT_PLAYBACK.draw


###3D视图
class EMM_VIEW3D_PT_N_Panel(Panel):
    bl_idname = "EMM_VIEW3D_PT_N_PANEL"
    bl_label = "EMM_N_面板"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "EMM"
    # bl_context = "win"
    bl_options = {'DEFAULT_CLOSED'}


    def draw(self, context):
        pass

class EMM_PT_插件属性(Panel):
    bl_idname = "EMM_VIEW3D_PT_SHUXING_PANEL"
    bl_label = "插件属性"
    bl_space_type = EMM_VIEW3D_PT_N_Panel.bl_space_type
    bl_region_type = EMM_VIEW3D_PT_N_Panel.bl_region_type
    bl_category = EMM_VIEW3D_PT_N_Panel.bl_category
    bl_parent_id = EMM_VIEW3D_PT_N_Panel.bl_idname    
    # bl_context = EMM_VIEW3D_PT_N_Panel.bl_context
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        emm(self, context)

class EMM_PT_插件属性1(Panel):
    bl_idname = "EMM_VIEW3D_PT_SHUXING_PANE"
    bl_label = "模板资产"
    bl_space_type = EMM_VIEW3D_PT_N_Panel.bl_space_type
    bl_region_type = EMM_VIEW3D_PT_N_Panel.bl_region_type
    bl_category = EMM_VIEW3D_PT_N_Panel.bl_category
    bl_parent_id = EMM_VIEW3D_PT_N_Panel.bl_idname    
    # bl_context = EMM_VIEW3D_PT_N_Panel.bl_context
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        emm(self, context)

class EMM_PT_插件属性2(Panel):
    bl_idname = "EMM_VIEW3D_PT_SHUXING_PAN"
    bl_label = "模板资产"
    bl_space_type = EMM_VIEW3D_PT_N_Panel.bl_space_type
    bl_region_type = EMM_VIEW3D_PT_N_Panel.bl_region_type
    bl_category = EMM_VIEW3D_PT_N_Panel.bl_category
    bl_parent_id = EMM_VIEW3D_PT_N_Panel.bl_idname    
    # bl_context = EMM_VIEW3D_PT_N_Panel.bl_context
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        emm(self, context)

class EMM_PT_check_Slow(Panel):
    bl_idname = "EMM_VIEW3D_PT_CHECK_SLOW"
    bl_label = "检查列表"
    bl_space_type = EMM_VIEW3D_PT_N_Panel.bl_space_type
    bl_region_type = EMM_VIEW3D_PT_N_Panel.bl_region_type
    bl_category = EMM_VIEW3D_PT_N_Panel.bl_category
    # bl_parent_id = EMM_VIEW3D_PT_N_Panel.bl_idname
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


##节点
class EMM_VIEW3D_NODE_PT_N_PANEL(Panel):
    bl_idname = "EMM_NODE_PT_N_PANEL_PANEL_PANEL_PANEL_PANEL"
    bl_label = "EMM_NODE_面板"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "EMM"
    # bl_context = "win"
    bl_options = {'DEFAULT_CLOSED'}


    def draw(self, context):
        pass

class EMM_NODE_PT_渐变预设(Panel):
    bl_idname = "EMM_NODE_PT_VALTORGB_PANEL"
    bl_label = "渐变预设"
    bl_space_type = EMM_VIEW3D_NODE_PT_N_PANEL.bl_space_type
    bl_region_type = EMM_VIEW3D_NODE_PT_N_PANEL.bl_region_type
    bl_category = EMM_VIEW3D_NODE_PT_N_PANEL.bl_category
    bl_parent_id = EMM_VIEW3D_NODE_PT_N_PANEL.bl_idname
    # bl_context = EMM_NODE_PT_N_Panel.bl_context
    bl_options = {'DEFAULT_CLOSED'}

    # @classmethod
    # def poll(self, context):
            #     AC = bpy.context.active_object.active_material.node_tree.nodes[-1]

    #     return AC.type == 'VALTORGB'


    def draw(self, context):
        layout = self.layout
        AC = bpy.context.active_object.active_material.node_tree.nodes[-1]
        if AC.type == 'VALTORGB':
            AC = AC.color_ramp
            C = layout.column(align=True)
            # R = C.row(align=True)
            C.prop(AC,'interpolation')
            C.prop(AC,'hue_interpolation')
            C.prop(AC,'color_mode')

        # emm(self, context)

    # bpy.context.active_object.active_material.node_tree.nodes
    # bpy.data.materials["Material"].node_tree.nodes["ColorRamp"].color_ramp.interpolation
    # bpy.context.active_object.active_material.node_tree.nodes[-1].color_ramp.elements
    # bpy.data.materials["Material"].node_tree.nodes["ColorRamp"].color_ramp.hue_interpolation
    # bpy.data.materials["Material"].node_tree.nodes["ColorRamp"].color_ramp.color_mode

class EMM_NODE_PT_渐变(Panel):
    bl_idname = "EMM_NODE_PT_VALTORGB_EMM"
    bl_label = "渐变信息"
    bl_space_type = EMM_NODE_PT_渐变预设.bl_space_type
    bl_region_type = EMM_NODE_PT_渐变预设.bl_region_type
    bl_category = EMM_NODE_PT_渐变预设.bl_category
    bl_parent_id = EMM_NODE_PT_渐变预设.bl_idname
    # bl_context = EMM_NODE_PT_N_Panel.bl_context
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(self, context):
        AC = bpy.context.active_object.active_material.node_tree.nodes[-1]

        return AC.type == 'VALTORGB'
    
    # TODO 渐变预设
    # def draw_header_preset(self, _context):
    #     NODE_PT_ColorRamp_Presets.draw_panel_header(self.layout)

    def draw(self, context):
        layout = self.layout
        AC = bpy.context.active_object.active_material.node_tree.nodes[-1]
        if AC.type == 'VALTORGB':
            AC = AC.color_ramp
            for i in AC.elements:
                C = layout.column(align=True)
                C = C.row()
                C.prop(i,'color',text='')
                C.prop(i,'alpha')
                C.prop(i,'position')



## TODO 绘制调色盘
# settings = self.paint_settings(context)

# layout.template_ID(settings, "palette", new="palette.new")
# if settings.palette:
#     layout.template_palette(settings, "palette", color=True)

# @classmethod
def 动画添加项(self,context):    
    layout = self.layout
    layout.use_property_split = True
    layout.use_property_decorate = False

    screen = context.screen
    scene = context.scene
    EMM = screen.EMM

    layout.prop(scene, "sync_mode", text="Sync")
    col = layout.column(heading="Audio")
    col.prop(scene, "use_audio_scrub", text="Scrubbing")
    col.prop(scene, "use_audio", text="Mute")

    col = layout.column(heading="Playback")
    col.prop(scene, "lock_frame_selection_to_range", text="Limit to Frame Range")
    col.prop(screen, "use_follow", text="Follow Current Frame")

    col.separator(factor=0.5)
    col.prop(EMM, "循环播放")
    col.prop(EMM, "回到起始帧")

    col = layout.column(heading="Play In")
    col.prop(screen, "use_play_top_left_3d_editor", text="Active Editor")
    col.prop(screen, "use_play_3d_editors", text="3D Viewport")
    col.prop(screen, "use_play_animation_editors", text="Animation Editors")
    col.prop(screen, "use_play_image_editors", text="Image Editor")
    col.prop(screen, "use_play_properties_editors", text="Properties Editor")
    col.prop(screen, "use_play_clip_editors", text="Movie Clip Editor")
    col.prop(screen, "use_play_node_editors", text="Node Editors")
    col.prop(screen, "use_play_sequence_editors", text="Video Sequencer")

    col = layout.column(heading="Show")
    col.prop(scene, "show_subframe", text="Subframes")

    layout.separator()

    row = layout.row(align=True)
    row.operator("anim.start_frame_set")
    row.operator("anim.end_frame_set")


排除类列表 = (
    TIME_PT_PLAYBACK,
    Panel,
    UIList,
    NODE_PT_ColorRamp_Presets,
)



def register_注册面板():
    
    ###这个方法需要注意名称的长度，注册的顺序是按名称的长度来的，子面板要后注册
    for name, class_ in reversed(inspect.getmembers(sys.modules[__name__], inspect.isclass)):
        if class_ not in 排除类列表:
            try:
                register_class(class_)
                # print(class_)
            except Exception as e:
                print(e.args)


    unregister_class(TIME_PT_PLAYBACK)
    TIME_PT_PLAYBACK.draw = 动画添加项
    register_class(TIME_PT_PLAYBACK)


def register_注销面板():    
    for name, class_ in reversed(inspect.getmembers(sys.modules[__name__], inspect.isclass)):
        if class_ not in 排除类列表:
            
            try:
                unregister_class(class_)
                # print(class_)
            except Exception as e:
                print(e.args)

            # unregister_class(class_)
    
    unregister_class(TIME_PT_PLAYBACK)
    TIME_PT_PLAYBACK.draw = TIME_PT_PLAYBACK动画播放
    register_class(TIME_PT_PLAYBACK)


Panel_Class= reversed(inspect.getmembers(sys.modules[__name__], inspect.isclass))
# (
#     EMM_VIEW3D_PT_N_Panel,
#     EMM_PT_插件属性,
#     EMM_PT_插件属性1,
#     EMM_PT_插件属性2,
#     EMM_PT_check_Slow,
# )


## N面板工具箱
def update_panel_名称(self,context):
    # print('update_panel_名称')
    for name, panel in reversed(inspect.getmembers(sys.modules[__name__], inspect.isclass)):
            if panel not in 排除类列表:
                # print(panel,'__dict__')
                if "bl_rna" in panel.__dict__:
                    bpy.utils.unregister_class(panel)
    for name, panel in reversed(inspect.getmembers(sys.modules[__name__], inspect.isclass)):
            if panel not in 排除类列表:
                panel.bl_category = get_prefs().n_panel_name
                bpy.utils.register_class(panel)