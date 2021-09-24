# import preferences
import bpy
import inspect
import sys
from bpy.types import Panel, UIList
from bpy.utils import register_class, unregister_class
# from bl_ui.properties_paint_common
from .presets.node_渐变_presets import NODE_PT_ColorRamp_Presets
from .tool.maximize_prefs import 插件面板
from .. utils.registration import get_prefs,get_emm_name
from .. utils.blender_class import TIME_PT_PLAYBACK动画播放
from bl_ui.space_time import TIME_PT_playback as TIME_PT_PLAYBACK
TIME_PT_PLAYBACK__DRAW = TIME_PT_PLAYBACK.draw
from bpy.props import   *
from .. import  bl_info

"""
需注意注册顺序
按EM的顺序来
EM
EMM
EMMM
依次注册
"""

#混合面板
class EM_VIEW3D_PT_N_Panel(Panel):
    bl_idname = "EMMM_VIEW3D_PT_N_Panel"
    bl_label = f"萌新工具箱_{bl_info['version'][0]}.{bl_info['version'][1]}.{bl_info['version'][2]}_{bl_info['version'][3]}"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "EMM"
    bl_options = {'DEFAULT_CLOSED'}


    def draw(self, context):
        pass

class EM_NODE_PT_N_PANEL(Panel):
    bl_idname = "EMM_NODE_PT_N_PANEL_PANEL_PANEL_PANEL_PANEL"
    bl_label = "节点工具"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "EMM"
    bl_options = {'DEFAULT_CLOSED'}


    def draw(self, context):
        pass

class EM_ADDON_PT_N_PANEL(Panel):
    bl_idname = "EMM_ADDON_PT_N_PANEL"
    bl_label = "插件管理"
    bl_space_type = EM_VIEW3D_PT_N_Panel.bl_space_type
    bl_region_type = EM_VIEW3D_PT_N_Panel.bl_region_type
    bl_category = EM_VIEW3D_PT_N_Panel.bl_category
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        pass
        # 插件面板(self, context)

class EM_PT_check_Slow(Panel):
    bl_idname = "EMM_VIEW3D_PT_CHECK_SLOW"
    bl_label = "检查列表"
    bl_space_type = EM_VIEW3D_PT_N_Panel.bl_space_type
    bl_region_type = EM_VIEW3D_PT_N_Panel.bl_region_type
    bl_category = EM_VIEW3D_PT_N_Panel.bl_category
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



##############################      3D视图
##插件

class EMM_WORKSPACE_PT_addons(Panel):
    bl_label = "Filter Add-ons"
    bl_idname = "EMM_VIEW3D_PT_ADDONS"

    bl_space_type = EM_ADDON_PT_N_PANEL.bl_space_type
    bl_region_type = EM_ADDON_PT_N_PANEL.bl_region_type
    bl_category = EM_ADDON_PT_N_PANEL.bl_category
    bl_parent_id = EM_ADDON_PT_N_PANEL.bl_idname
    bl_options = {'DEFAULT_CLOSED'}



    def draw_header_preset(self,context):
        layout = self.layout
        wm = context.window_manager
        prefs = context.preferences
        workspace = context.workspace

        if workspace.use_filter_by_owner:
            layout.row().prop(get_prefs(), "仅过滤用户插件"
                            # ,text = '仅用户插件',
                                                                                # toggle=True
                                                                                )
            layout.row().prop(get_prefs(),'addon_filter',text='')

    def draw_header(self, context):
        workspace = context.workspace
        self.layout.prop(workspace, "use_filter_by_owner", text="")

    def draw(self, context):

        workspace = context.workspace
        prefs = context.preferences
        wm = context.window_manager

        import addon_utils
        addon_map = {mod.__name__: mod for mod in addon_utils.modules()}
        owner_ids = {owner_id.name for owner_id in workspace.owner_ids}
        
        import os
        if bpy.app.version >= (2, 94, 0):
            ## 3.0版本
            addon_user_dirs = tuple(
                p for p in (
                    os.path.join(prefs.filepaths.script_directory, "addons"),
                    bpy.utils.user_resource('SCRIPTS', path="addons"),
                )
                if p
            )
        else:
            ## 2.93版本
            addon_user_dirs = tuple(
                p for p in (
                    os.path.join(prefs.filepaths.script_directory, "addons"),
                    bpy.utils.user_resource('SCRIPTS', "addons"),
                )
                if p
            )

        layout = self.layout        
        col = layout.box().column(align=True)
        row = col.row()
        col.active = workspace.use_filter_by_owner


        if get_prefs().仅过滤用户插件 == False:
            row.prop(wm, "addon_support", expand=True)


        self.filter = filter = get_prefs().addon_filter

        support = wm.addon_support


        跳过插件 = [
            get_emm_name(),
            'BM_WWYL'
        ]

        for addon in prefs.addons:
            module_name = addon.module
            module = addon_map.get(module_name)

            info = addon_utils.module_bl_info(module)

            is_enabled = module_name in owner_ids


            if module_name in 跳过插件:
                if module_name not in owner_ids:
                    bpy.context.workspace.owner_ids.new(module_name)
                continue

            if module is None:
                continue

            if info["support"] not in support and get_prefs().仅过滤用户插件 == False:
                continue
            if get_prefs().仅过滤用户插件:
                if (module.__file__.startswith(addon_user_dirs)) == False:
                    continue

            # check if addon should be visible with current filters
            is_visible = (
                (filter == "All") or
                (filter == info["category"]) or
                (filter == "User" and (module.__file__.startswith(addon_user_dirs)))
            )

            # def 仅用户():
            #     get_prefs().addon_filter = 'User'
            #     # if info["support"] !=
            #     pass

            # if get_prefs().仅过滤用户插件:
            #     仅用户()
                # is_visible = is_visible and is_enabled

            if is_visible:
                row = col.row()
                row.alignment = 'LEFT'
                row.operator(
                    "wm.owner_disable" if is_enabled else "wm.owner_enable",
                    icon='CHECKBOX_HLT' if is_enabled else 'CHECKBOX_DEHLT',
                    text='',
                    emboss=False,
                ).owner_id = module_name
                row.label(text="%s: %s" % (info["category"], info["name"]),)            
                if is_enabled:
                    owner_ids.remove(module_name)

            elif is_visible ==False and get_prefs().仅过滤用户插件:

                if module_name not in owner_ids:
                    # bpy.context.workspace.owner_ids.new(module_name)
                    print(f'add___{module_name}')

        # Detect unused
        # if owner_ids:
        #     layout.label(text="Unknown add-ons", icon='ERROR')
        #     col = layout.box().column(align=True)
        #     for module_name in sorted(owner_ids):
        #         row = col.row()
        #         row.alignment = 'LEFT'
        #         row.operator(
        #             "wm.owner_disable",
        #             icon='CHECKBOX_HLT',
        #             text=module_name,
        #             emboss=False,
        #         ).owner_id = module_name

#曲线
class EMM_PT_曲线(Panel):
    bl_idname = "EMM_VIEW3D_PT_CURVE_TOOL_PANEL"
    bl_label = "曲线拆分"
    bl_space_type = EM_VIEW3D_PT_N_Panel.bl_space_type
    bl_region_type = EM_VIEW3D_PT_N_Panel.bl_region_type
    bl_category = EM_VIEW3D_PT_N_Panel.bl_category
    bl_parent_id = EM_VIEW3D_PT_N_Panel.bl_idname    
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        obj = context.object
        return (obj and obj.type == 'CURVE')

    def draw(self, context):
        layout = self.layout
        C = layout.column(align=True)
        R = C.row()
        # R.operator('emm.separate_splines',text='按松散块').mode = '按松散块'
        # 插件面板(self, context)
#网格

class EMM_PT_网格工具(Panel):
    bl_idname = "EMM_VIEW3D_PT_MESH_TOOL_PANE"
    bl_label = "网格工具"
    bl_space_type = EM_VIEW3D_PT_N_Panel.bl_space_type
    bl_region_type = EM_VIEW3D_PT_N_Panel.bl_region_type
    bl_category = EM_VIEW3D_PT_N_Panel.bl_category
    bl_parent_id = EM_VIEW3D_PT_N_Panel.bl_idname    
    # bl_context = EMMM_VIEW3D_PT_N_Panel.bl_context
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        obj = context.object
        return (obj and obj.type == 'MESH')

    def draw(self, context):
        act = context.active_object
        layout = self.layout
        C = layout.column(align=True)
        R = C.row()

        G = R.operator('emm.join_mesh')
        if act.EMM.is_join_obj:G.mode = '拆分'
        else:G.mode ='合并'

class EMM_PT_网格_面映射(Panel):
    bl_idname = "EMM_VIEW3D_PT_MESH_FACE_MAP_PANEL"
    bl_label = "面映射"
    bl_space_type = EM_VIEW3D_PT_N_Panel.bl_space_type
    bl_region_type = EM_VIEW3D_PT_N_Panel.bl_region_type
    bl_category = EM_VIEW3D_PT_N_Panel.bl_category
    bl_parent_id = EM_VIEW3D_PT_N_Panel.bl_idname    
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        obj = context.object
        return (obj and obj.type == 'MESH')

    def draw(self, context):

        layout = self.layout

        ob = context.object
        facemap = ob.face_maps.active

        rows = 2
        if facemap:
            rows = 4

        row = layout.row()
        row.template_list("MESH_UL_fmaps", "", ob, "face_maps", ob.face_maps, "active_index", rows=rows)

        col = row.column(align=True)
        col.operator("object.face_map_add", icon='ADD', text="")
        col.operator("object.face_map_remove", icon='REMOVE', text="")

        col.separator()

        col.menu("EMM_MESH_MT_FACE_MAP", icon='DOWNARROW_HLT', text="")

        if facemap:
            col.separator()
            col.operator("object.face_map_move", icon='TRIA_UP', text="").direction = 'UP'
            col.operator("object.face_map_move", icon='TRIA_DOWN', text="").direction = 'DOWN'

        if ob.face_maps and (ob.mode == 'EDIT' and ob.type == 'MESH'):
            row = layout.row()

            sub = row.row(align=True)
            sub.operator("object.face_map_assign", text="Assign")
            sub.operator("object.face_map_remove_from", text="Remove")

            sub = row.row(align=True)
            sub.operator("object.face_map_select", text="Select")
            sub.operator("object.face_map_deselect", text="Deselect")

class EMM_PT_网格_顶点组(Panel):
    bl_idname = "EMM_VIEW3D_PT_MESH_VERTEX_GROUPS_PANEL"
    bl_label = "顶点组"
    bl_space_type = EM_VIEW3D_PT_N_Panel.bl_space_type
    bl_region_type = EM_VIEW3D_PT_N_Panel.bl_region_type
    bl_category = EM_VIEW3D_PT_N_Panel.bl_category
    bl_parent_id = EM_VIEW3D_PT_N_Panel.bl_idname    
    bl_options = {'DEFAULT_CLOSED'}
    
    @classmethod
    def poll(cls, context):
        # engine = context.engine
        obj = context.object
        return (obj and obj.type in {'MESH', 'LATTICE'} 
        # and (engine in cls.COMPAT_ENGINES)
        )
    def draw_header_preset(self, _context):
        layout = self.layout

        layout.prop(get_prefs(),'顶点组同步',icon='UV_SYNC_SELECT',icon_only=True)

    def draw(self, context):
        layout = self.layout

        ob = context.object
        group = ob.vertex_groups.active

        rows = 3
        if group:
            rows = 5

        row = layout.row()
        row.template_list("MESH_UL_vgroups", "", ob, "vertex_groups", ob.vertex_groups, "active_index", rows=rows)

        col = row.column(align=True)

        col.operator("object.vertex_group_add", icon='ADD', text="")
        props = col.operator("object.vertex_group_remove", icon='REMOVE', text="")
        props.all_unlocked = props.all = False

        col.separator()

        col.menu("MESH_MT_vertex_group_context_menu", icon='DOWNARROW_HLT', text="")

        if group:
            col.separator()
            col.operator("object.vertex_group_move", icon='TRIA_UP', text="").direction = 'UP'
            col.operator("object.vertex_group_move", icon='TRIA_DOWN', text="").direction = 'DOWN'

        if (
                ob.vertex_groups and
                (ob.mode == 'EDIT' or
                 (ob.mode == 'WEIGHT_PAINT' and ob.type == 'MESH' and ob.data.use_paint_mask_vertex))
        ):
            row = layout.row()

            sub = row.row(align=True)
            sub.operator("object.vertex_group_assign", text="Assign")
            sub.operator("object.vertex_group_remove_from", text="Remove")

            sub = row.row(align=True)
            sub.operator("object.vertex_group_select", text="Select")
            sub.operator("object.vertex_group_deselect", text="Deselect")

            layout.prop(context.tool_settings, "vertex_group_weight", text="Weight")


#骨骼
class EMM_PT_骨骼_面映射(Panel):
    bl_idname = "EMM_VIEW3D_PT_BONE_FACE_MAP_PANEL"
    bl_label = "面映射"
    bl_space_type = EM_VIEW3D_PT_N_Panel.bl_space_type
    bl_region_type = EM_VIEW3D_PT_N_Panel.bl_region_type
    bl_category = EM_VIEW3D_PT_N_Panel.bl_category
    bl_parent_id = EM_VIEW3D_PT_N_Panel.bl_idname    
    bl_options = {'DEFAULT_CLOSED'}

    @classmethod
    def poll(cls, context):
        obj = context.object
        return (obj and obj.type == 'ARMATURE' 
        # and obj.mode == 'POSE'
        )

    def draw(self, context):

        layout = self.layout

        ob = context.object
        facemap = ob.face_maps.active

        rows = 2
        if facemap:
            rows = 4

        row = layout.row()
        row.template_list("MESH_UL_fmaps", "", ob, "face_maps", ob.face_maps, "active_index", rows=rows)

        col = row.column(align=True)
        col.operator("object.face_map_add", icon='ADD', text="")
        col.operator("object.face_map_remove", icon='REMOVE', text="")

        col.separator()

        col.menu("EMM_MESH_MT_FACE_MAP", icon='DOWNARROW_HLT', text="")

        if facemap:
            col.separator()
            col.operator("object.face_map_move", icon='TRIA_UP', text="").direction = 'UP'
            col.operator("object.face_map_move", icon='TRIA_DOWN', text="").direction = 'DOWN'

        if ob.face_maps and (ob.mode == 'EDIT' and ob.type == 'MESH'):
            row = layout.row()

            sub = row.row(align=True)
            sub.operator("object.face_map_assign", text="Assign")
            sub.operator("object.face_map_remove_from", text="Remove")

            sub = row.row(align=True)
            sub.operator("object.face_map_select", text="Select")
            sub.operator("object.face_map_deselect", text="Deselect")



class EMM_PT_模板资产(Panel):
    bl_idname = "EMM_VIEW3D_PT_SHUXING_PAN"
    bl_label = "模板资产"
    bl_space_type = EM_VIEW3D_PT_N_Panel.bl_space_type
    bl_region_type = EM_VIEW3D_PT_N_Panel.bl_region_type
    bl_category = EM_VIEW3D_PT_N_Panel.bl_category
    bl_parent_id = EM_PT_check_Slow.bl_idname    
    bl_options = {'DEFAULT_CLOSED'}

    def draw(self, context):
        插件面板(self, context)


##节点
class EMM_NODE_PT_渐变预设(Panel):
    bl_idname = "EMM_NODE_PT_VALTORGB_PANEL"
    bl_label = "渐变预设"
    bl_space_type = EM_NODE_PT_N_PANEL.bl_space_type
    bl_region_type = EM_NODE_PT_N_PANEL.bl_region_type
    bl_category = EM_NODE_PT_N_PANEL.bl_category
    bl_parent_id = EM_NODE_PT_N_PANEL.bl_idname
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
#     EMMM_VIEW3D_PT_N_Panel,
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