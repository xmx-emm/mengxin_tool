from . utils.registration import register_classes, unregister_classes, register_keymaps, unregister_keymaps, register_icons, unregister_icons
from . utils.registration import get_prefs
from . utils.registration import get_core, get_tools, get_pie_menus
from . ui.restore_ui import rewrite_ui_更改UI,restore_ui_恢复UI
from . ui.panel import register_注册面板,register_注销面板
from . utils.update import register_注册更新数据模块,unregister_注销更新数据模块
from . property import 注册属性_Property,注销属性_Property
from . assets import 资产_register,资产_unregister
from . ui.presets import 注册预设,注销预设
import bpy
import sys
import os

"""

每次更新需检查 
ui\panel.py 动画添加项
ui\tool\maximize_prefs.py   def emm(self, context):
替换自带的面板，避免功能缺失

"""
bl_info = {
    "name": "萌新工具箱",
    "author": "小萌新",
    "version": (0, 0, 1,5, '萌新工具箱__2021-9-5'),
    "blender": (2, 83, 0),
    "location": "到处都是",
    "description": "这是一个萌新工具箱",
    "warning": "",
    "doc_url": "https://space.bilibili.com/231639322",
    # "tracker_url": "https://github.com/1234EMMM/mengxin_tool",
    "wiki_url": "https://space.bilibili.com/231639322",
    # "category": "3D View"
    }


# if 'bpy' in locals():
#     print("这是一个测试")


def register():
    if sys.platform == 'win32':os.system('@chcp 65001')
    print(f"{bl_info['name']}  启动！！！")

    资产_register()
    注册属性_Property()
    register_注册面板()## 需要先注册面板，不然在插件属性里面更新面板的名称会找不到 Panel_Class 这个列表而报错


    global classes, keymaps, modify_key, icons  ##注册激活功能类和快捷键图标啥的
    core_classes = register_classes(get_core())

    tool_classlists, tool_keylists, tool_count = get_tools()
    pie_classlists, pie_keylists, pie_count = get_pie_menus()
    # # modify_keylists,  modify_count = get_modify_keymaps()

    classes = register_classes(tool_classlists + pie_classlists) + core_classes
    keymaps = register_keymaps(tool_keylists + pie_keylists)
    # # modify_key = modify_keymaps(modify_keylists)

    icons = register_icons()

    注册预设()  #先注册预设再更改UI,不然改UI没有预设按钮给加上去    这里只管注册，添加到界面让下一个更改UI来做


    rewrite_ui_更改UI()
    register_注册更新数据模块()


    get_prefs().maximize_prefs = False  # 在注册类后设置这个最大化偏好设置
    get_prefs().auto_run_script = False  # 自动重载脚本控制，启动插件默认关闭

    print(f"自动注册完成  Registered {bl_info['name']} {'.'.join([str(i) for i in bl_info['version']])} with {tool_count} {'tool' if tool_count == 1 else 'tools'}, {pie_count} pie {'menu' if pie_count == 1 else 'menus'}")


def unregister():
    unregister_注销更新数据模块()
    register_注销面板()    
    restore_ui_恢复UI()
    注销预设()

    global classes, keymaps, modify_key , icons
    unregister_keymaps(keymaps)
    unregister_classes(classes)
    注销属性_Property()
    
    资产_unregister()

    unregister_icons(icons)
    print(f"注销完成  Unregistered {bl_info['name']} {'.'.join([str(i) for i in bl_info['version']])}.")
    print('-----------------------------------------------------------')
