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


        # 'MODES_PIE': [{'label': '3D View', 'keymap': 'Object Non-modal', 'idname': 'wm.call_menu_pie', 'type': 'TAB', 'value': 'PRESS', 'properties': [('name', 'MACHIN3_MT_modes_pie')]},
        #               {'label': 'Image Editor', 'keymap': 'Image', 'space_type': 'IMAGE_EDITOR', 'idname': 'wm.call_menu_pie', 'type': 'TAB', 'value': 'PRESS', 'properties': [('name', 'MACHIN3_MT_modes_pie')]}],

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


        # 'MODES_PIE': [{'label': '3D View', 'keymap': 'Object Non-modal', 'idname': 'wm.call_menu_pie', 'type': 'TAB', 'value': 'PRESS', 'properties': [('name', 'MACHIN3_MT_modes_pie')]},
        #               {'label': 'Image Editor', 'keymap': 'Image', 'space_type': 'IMAGE_EDITOR', 'idname': 'wm.call_menu_pie', 'type': 'TAB', 'value': 'PRESS', 'properties': [('name', 'MACHIN3_MT_modes_pie')]}],



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

                # if kmi.idname == 'object.delete':
                #     if get_prefs().activate_select_pie:
                #         kmi.value = 'CLICK'
                #     else:
                #         kmi.value = 'PRESS'
            
            # km = kc.get('Text')  # get 属性keymap快捷键
            # for kmi in km.keymap_items:
            #     if kmi.idname == 'text.run_script':
            #         if get_prefs().activate_space_pie and preferences.spacebar_action == 'PLAY':
            #             kmi.value = 'CLICK'
            #         else:
            #             kmi.value = 'PRESS'

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