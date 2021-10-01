from .registration import get_prefs
from bpy.types import Operator as OPS
from bpy.props import EnumProperty
import bpy

context = bpy.context
kc = context.window_manager.keyconfigs.user.keymaps
class Updaet_Keymaps(OPS):
    bl_idname = 'emm.updaet_keymaps'
    bl_label = '更新快捷键'
    bl_description = """更新快捷键 呀"""
    bl_options = {'REGISTER', 'UNDO'}

    Updaet_: EnumProperty(
        name="操作项",
        default='updaet_keymaps',
        items=(
            ('updaet_keymaps', "更新快捷键", ""),
            ('updaet_spacebar', "重置空格建", ""),
        ),
    )

    def execute(self, context):
        preferences = bpy.context.window_manager.keyconfigs['Blender'].preferences


        if self.Updaet_ == 'updaet_keymaps':
            km = kc.get('Object Non-modal')  # get 属性keymap快捷键
            for kmi in km.keymap_items:
                ## 饼菜单
                if kmi.idname == 'wm.call_menu_pie':
                    for item in kmi.properties.items():     # 循环 properties的name项
                        name = item[1]                      # 切片出来 快捷键 properties的name项.name

                        if name == 'MACHIN3_MT_modes_pie':                          
                            
                            # kmi.active = kmi.active ^ True
                            # kmi.value = 'CLICK_DRAG'
                            if getattr(bpy.types, "MACHIN3_MT_modes_pie", False) and get_prefs().activate_modes_pie:
                                kmi.active = False
                            else:
                                kmi.active = True
                        # if name == 'VIEW3D_MT_object_mode_pie':
                        #     pass
                            # kmi.active = kmi.active ^ True
                            # kmi.value = 'CLICK_DRAG'
                        
                        # print(name)
                        # if name == 'MACHIN3_MT_modes_pie':
 

                        # if name == 'MACHIN3_MT_modes_pie':
                        #     if getattr(bpy.types, "MACHIN3_MT_modes_pie", False) and get_prefs().activate_modes_pie:
                        #         kmi.active = False
                        #     else:
                        #         kmi.active = True

            km = kc.get('Window')  # get 属性keymap快捷键
            for kmi in km.keymap_items:
                if kmi.idname == 'wm.call_menu_pie':
                    for item in kmi.properties.items():     # 循环 properties的name项
                        name = item[1]                      # 切片出来 快捷键 properties的name项.name

                        if name == 'VIEW3D_MT_shading_pie':
                            if get_prefs().activate_views_pie:
                                kmi.active = False
                            else:
                                kmi.active = True

                if kmi.idname == 'wm.search_menu':
                    if get_prefs().activate_space_pie and preferences.spacebar_action == 'SEARCH':
                        kmi.value = 'CLICK'
                    else:
                        kmi.value = 'PRESS'
                if kmi.idname == 'wm.toolbar':
                    if get_prefs().activate_space_pie and preferences.spacebar_action == 'TOOL':
                        kmi.value = 'CLICK'
                    else:
                        kmi.value = 'PRESS'

            km = kc.get('Image')  # get 属性keymap快捷键
            for kmi in km.keymap_items:
                if kmi.idname == 'wm.call_menu_pie':
                    for item in kmi.properties.items():     # 循环 properties的name项
                        # 切片出来 快捷键 properties的name项.name
                        name = item[1]              
                        if name == 'MACHIN3_MT_modes_pie':

                            if getattr(bpy.types, "MACHIN3_MT_modes_pie", False) and get_prefs().activate_modes_pie:
                                kmi.active = False
                            else:
                                kmi.active = True
                                
                        # if name == 'VIEW3D_MT_object_mode_pie':
                        #     pass
                            # kmi.active = kmi.active ^ True
                            # kmi.value = 'CLICK_DRAG'
                        
                        # print(name)
                        # if name == 'MACHIN3_MT_modes_pie':
 

                        #     if getattr(bpy.types, "MACHIN3_MT_modes_pie", False) and get_prefs().activate_modes_pie:
                        #         kmi.active = False
                        #     else:
                        #         kmi.active = True

                if kmi.idname == 'object.mode_set':
                        if get_prefs().activate_modes_pie and get_prefs().使用M3模式切换饼菜单:
                            kmi.value = 'CLICK'
                        else:
                            kmi.value = 'PRESS'


            km = kc.get('3D View')  # get 属性keymap快捷键
            for kmi in km.keymap_items:
                if kmi.idname == 'wm.call_menu_pie':
                    for item in kmi.properties.items():     # 循环 properties的name项
                        # 切片出来 快捷键 properties的name项.name
                        name = item[1]
                        if name == 'VIEW3D_MT_shading_ex_pie':
                            if get_prefs().activate_views_pie:                        
                                kmi.active = False
                            else:
                                kmi.active = True

                            # kmi.value = 'CLICK_DRAG'                        

                if kmi.idname == 'view3d.select_circle':
                    if get_prefs().activate_C_pie:
                        kmi.value = 'CLICK'
                    else:
                        kmi.value = 'PRESS'

                if kmi.idname == 'view3d.select_box':
                    if get_prefs().activate_B_pie:
                        kmi.value = 'CLICK'
                    else:
                        kmi.value = 'PRESS'

            km = kc.get('Mesh')  # get 属性keymap快捷键
            for kmi in km.keymap_items:
                if kmi.idname == 'wm.call_menu':
                    for item in kmi.properties.items():     # 循环 properties的name项
                        # 切片出来 快捷键 properties的name项.name
                        name = item[1]

                        if name == 'VIEW3D_MT_edit_mesh_delete':

                            if get_prefs().activate_delete_pie:
                                kmi.value = 'CLICK'
                            else:
                                kmi.value = 'PRESS'

                if kmi.idname == 'mesh.select_all':
                    if get_prefs().activate_select_pie:
                        kmi.value = 'CLICK'
                    else:
                        kmi.value = 'PRESS'

                if kmi.idname == 'mesh.rip_move':
                    if get_prefs().activate_select_pie:
                        kmi.value = 'CLICK'
                    else:
                        kmi.value = 'PRESS'

            km = kc.get('Object Mode')  # get 属性keymap快捷键
            for kmi in km.keymap_items:
                if kmi.idname == 'object.select_all':
                    if get_prefs().activate_select_pie:
                        kmi.value = 'CLICK'
                    else:
                        kmi.value = 'PRESS'
                if kmi.idname == 'object.delete':
                    if get_prefs().activate_select_pie:
                        kmi.value = 'CLICK'
                    else:
                        kmi.value = 'PRESS'

            km = kc.get('Frames')  # get 属性keymap快捷键
            for kmi in km.keymap_items:
                if kmi.idname == 'screen.animation_play':
                    if get_prefs().activate_space_pie and preferences.spacebar_action == 'PLAY':
                        kmi.value = 'CLICK'
                    else:
                        kmi.value = 'PRESS'

            km = kc.get('Text')  # get 属性keymap快捷键
            for kmi in km.keymap_items:
                if kmi.idname == 'text.run_script':
                    if get_prefs().activate_custom_keymap:
                        kmi.type = 'A'
                    else:
                        kmi.type = 'P'

                # if kmi.idname == 'object.delete':
                #     if get_prefs().activate_select_pie:
                #         kmi.value = 'CLICK'
                #     else:
                #         kmi.value = 'PRESS'
            
            km = kc.get('Node Editor')  # get 属性keymap快捷键
            for kmi in km.keymap_items:
                if kmi.idname == 'node.group_edit':
                    if get_prefs().activate_modes_pie:
                        kmi.value = 'CLICK'
                    else:
                        kmi.value = 'PRESS'

                # if kmi.idname == 'object.delete':
                #     if get_prefs().activate_select_pie:
                #         kmi.value = 'CLICK'
                #     else:
                #         kmi.value = 'PRESS'
            
            
            return {'FINISHED'}

        if self.Updaet_ == 'updaet_spacebar':
            km = kc.get('Window')  # get 属性keymap快捷键
            for kmi in km.keymap_items:
                if kmi.idname == 'wm.search_menu':
                    kmi.value = 'PRESS'
                if kmi.idname == 'wm.toolbar':
                    kmi.value = 'PRESS'

            km = kc.get('Frames')  # get 属性keymap快捷键
            for kmi in km.keymap_items:
                if kmi.idname == 'screen.animation_play':
                    kmi.value = 'PRESS'

            return {'FINISHED'}

def modify_keymaps(name):


    pass

"""
TypeError: KeyMaps.new(): error with keyword argument "space_type" -  enum "PROPERTY_EDITOR"
 not found in ('EMPTY', 
 'VIEW_3D', 
 'IMAGE_EDITOR', 
 'NODE_EDITOR', 
 'SEQUENCE_EDITOR', 
 'CLIP_EDITOR', 
 'DOPESHEET_EDITOR', 
 'GRAPH_EDITOR',
  'NLA_EDITOR', 
  'TEXT_EDITOR', 
  'CONSOLE', 
  'INFO', 
  'TOPBAR', 
  'STATUSBAR', 
  'OUTLINER', 
  'PROPERTIES', 
  'FILE_BROWSER', 
  'SPREADSHEET', 
  'PREFERENCES')
"""
""""
Window
Screen
3D View Generic
View2D
Info
Object Non-modal
3D View

Screen Editing
User Interface
Region Context Menu
View2D Buttons List
Text Generic
Text
Frames
Property Editor
Grease Pencil
Paint Curve
Weight Paint
Vertex Paint
Pose
Object Mode
Curve
Image Paint
Sculpt
Mesh
Armature
Metaball
Lattice
Particle
Font
Console
View3D Gesture Circle
Gesture Box
Gesture Zoom Border
Gesture Straight Line
Gesture Lasso
Standard Modal Map
Animation
Animation Channels
Knife Tool Modal Map
Custom Normals Modal Map
Bevel Modal Map
UV Editor
Paint Stroke Modal
Sculpt Expand Modal
Mask Editing
Markers
Eyedropper Modal Map
Transform Modal Map
Outliner
View3D Fly Modal
View3D Walk Modal
View3D Rotate Modal
View3D Move Modal
View3D Zoom Modal
View3D Dolly Modal
View3D Placement Modal
Graph Editor Generic
Graph Editor
Image Generic
Image
Node Generic
Node Editor
File Browser
File Browser Main
File Browser Buttons
Dopesheet Generic
Dopesheet
NLA Generic
NLA Channels
NLA Editor
SequencerCommon
Sequencer
SequencerPreview
Clip
Clip Editor
Clip Graph Editor
Clip Dopesheet Editor
Time Scrub
Clip Time Scrub
Toolbar Popup


"""
