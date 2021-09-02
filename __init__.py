from . utils.registration import register_classes, unregister_classes, register_keymaps, unregister_keymaps
from . utils.registration import get_emm_prefs
from . utils.registration import get_core, get_tools, get_pie_menus
from . ui.restore_ui import restore_ui, rewrite_ui  # 重置UI，将一些添加在UI里面的内容删掉
from . ui.panel import EMM_VIEW3D_PT_N_Panel
from . preferences import EMMSculptProperty, EMMObjectProperty, EMMSceneProperty, EMMUvProperty


import bpy
import sys
import os
from bpy.props import PointerProperty
from bpy.utils import register_class, unregister_class

bl_info = {
    "name": "萌新工具箱",
    "author": "小萌新",
    "version": (0, 0, 1, '萌新工具箱','__','2021-8-31'),
    "blender": (2, 83, 0),
    "location": "",
    "description": "这是一个萌新工具箱",
    "warning": "",
    "doc_url": "https://space.bilibili.com/231639322",
    # "category": "3D View"
    }


# if 'bpy' in locals():
#     print("这是一个测试")


def register():
    if sys.platform == 'win32':os.system('@chcp 65001')
    print(f"{bl_info['name']}  启动！！！")

    global classes, keymaps, modify_key
    core_classes = register_classes(get_core())

    bpy.types.Scene.EMM = PointerProperty(type=EMMSceneProperty)
    bpy.types.Object.EMM = PointerProperty(type=EMMObjectProperty)
    bpy.types.Scene.EMM_UV = PointerProperty(type=EMMUvProperty)
    bpy.types.Scene.EMM_Sculpt = PointerProperty(type=EMMSculptProperty)
    # bpy.types.Uv = 


    tool_classlists, tool_keylists, tool_count = get_tools()
    pie_classlists, pie_keylists, pie_count = get_pie_menus()
    # modify_keylists,  modify_count = get_modify_keymaps()

    classes = register_classes(tool_classlists + pie_classlists) + core_classes
    keymaps = register_keymaps(tool_keylists + pie_keylists)
    # modify_key = modify_keymaps(modify_keylists)


    ##IF面板是不是一样的，如果不是一样的就改

    if getattr(bpy.types, "EMM_VIEW3D_PT_N_Panel", False):
        if hasattr(EMM_VIEW3D_PT_N_Panel, 'bl_category') and EMM_VIEW3D_PT_N_Panel.bl_category and EMM_VIEW3D_PT_N_Panel.bl_category != 'Tool':
            unregister_class(EMM_VIEW3D_PT_N_Panel)
            EMM_VIEW3D_PT_N_Panel.bl_category = get_emm_prefs().n_panel_name
            register_class(EMM_VIEW3D_PT_N_Panel)

    rewrite_ui()    #最后更改面板
    from . utils.update import register as update
    update()

    get_emm_prefs().maximize_prefs = False  # 在注册类后设置这个最大化偏好设置
    get_emm_prefs().auto_run_script = False  # 自动重载脚本控制，启动插件默认关闭

    print(f"自动注册完成  Registered {bl_info['name']} {'.'.join([str(i) for i in bl_info['version']])} with {tool_count} {'tool' if tool_count == 1 else 'tools'}, {pie_count} pie {'menu' if pie_count == 1 else 'menus'}")
def unregister():
    from . utils.update import unregister as update
    update()

    restore_ui()    #先重置那些预设面板

    global classes, keymaps, modify_key
    unregister_keymaps(keymaps)
    unregister_classes(classes)

    del bpy.types.Scene.EMM
    del bpy.types.Object.EMM
    del bpy.types.Scene.EMM_UV
    del bpy.types.Scene.EMM_Sculpt

    print(f"注销完成  Unregistered {bl_info['name']} {'.'.join([str(i) for i in bl_info['version']])}.")
    print('-----------------------------------------------------------')
