'''
每次更新需检查 
ui\panel.py 动画添加项
ui\tool\maximize_prefs.py   def emm(self, context):
替换自带的面板，避免功能缺失
'''


bl_info = {
    "name": "萌新工具箱",
    "author": "小萌新",
    "version": (0, 1, 0, '2021-9-20'),
    "blender": (2, 83, 0),
    "location": "到处都是",
    "description": "这是一个萌新工具箱",
    "warning": "",
    "doc_url": "https://space.bilibili.com/231639322",
    "tracker_url": "https://github.com/1234EMMM/mengxin_tool",
    "wiki_url": "https://space.bilibili.com/231639322",
    # "category": "3D View"
    }


from . utils.registration import register_classes, unregister_classes, register_keymaps, unregister_keymaps, register_icons, unregister_icons
from . utils.registration import get_prefs
from . utils.registration import get_core, get_tools, get_pie_menus

from . ui.restore_ui import rewrite_ui_更改UI,restore_ui_恢复UI
from . ui import 注册UI,注销UI

from . ops import 注册OPS,注销OPS

from . utils.update import register_注册更新数据模块,unregister_注销更新数据模块
from . property import 注册属性_Property,注销属性_Property
from . assets import 资产_register,资产_unregister

import bpy
import sys
import os
import getpass



# if 'bpy' in locals():
#     print("这是一个测试")


开发者 = True   if getpass.getuser() in ('32099','') else    False  # 如果是萌新的电脑，那么一些属性就会不一样

def register():
    if sys.platform == 'win32':os.system('@chcp 65001')
    print(f"{bl_info['name']}  启动！！！")

    注册UI()
    注册OPS()
    资产_register()
    注册属性_Property()

    global classes, keymaps, modify_key, icons  ##注册激活功能类和快捷键图标啥的
    core_classes = register_classes(get_core())

    tool_classlists, tool_keylists, tool_count = get_tools()
    pie_classlists, pie_keylists, pie_count = get_pie_menus()
    # # modify_keylists,  modify_count = get_modify_keymaps()

    classes = register_classes(tool_classlists + pie_classlists) + core_classes
    keymaps = register_keymaps(tool_keylists + pie_keylists)
    # # modify_key = modify_keymaps(modify_keylists)

    icons = register_icons()

    rewrite_ui_更改UI()
    register_注册更新数据模块()


    get_prefs().maximize_prefs = False  # 在注册类后设置这个最大化偏好设置
    if 开发者 == False:get_prefs().auto_run_script = False  # 自动重载脚本控制，启动插件默认关闭

    print(f"自动注册完成  Registered {bl_info['name']} {'.'.join([str(i) for i in bl_info['version']])} with {tool_count} {'tool' if tool_count == 1 else 'tools'}, {pie_count} pie {'menu' if pie_count == 1 else 'menus'}")


def unregister():
    unregister_注销更新数据模块()
    restore_ui_恢复UI()
    注销OPS()
    注销UI()
    
    global classes, keymaps, modify_key , icons
    unregister_keymaps(keymaps)
    unregister_classes(classes)
    注销属性_Property()
    
    资产_unregister()

    unregister_icons(icons)
    print(f"注销完成  Unregistered {bl_info['name']} {'.'.join([str(i) for i in bl_info['version']])}.")
    print('-----------------------------------------------------------')
