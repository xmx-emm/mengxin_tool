import bpy
from .registration import get_prefs
from bpy.app.handlers import render_pre as RENDER_PRE

from bpy.app.handlers import persistent


#  模式切换
def mode():
    update_sculpt_switch_rotate_method()        # 更新雕刻旋转方式模块

# 自动更新雕刻旋转方式模块
# @persistent
def update_sculpt_switch_rotate_method():
    C = bpy.context  # get 物体上下文
    mode = C.mode   #物体模式

    if get_prefs().sculpt_switch_rotate_method:
        if mode == 'SCULPT':
            C.preferences.inputs.view_rotate_method = 'TRACKBALL'
        else:
            C.preferences.inputs.view_rotate_method = 'TURNTABLE'
    else:
        C.preferences.inputs.view_rotate_method = 'TURNTABLE'


# 渲染前
@persistent
def render_pre(self,context):
    print('render_pre')


#### msgbus
owner = object()


def register_msgbus():
    bpy.msgbus.subscribe_rna(key=(bpy.types.Object, 'mode'),owner=owner,args=(),notify=mode,)


def unregister_msgbus():
    bpy.msgbus.clear_by_owner(owner)


def reload_msgbus():    #重置
    unregister_msgbus(owner)
    register_msgbus(owner)
#### msgbus______________





def register():
    register_msgbus()
    # print('re update')
    # bpy.types.VIEW3D_HT_header.prepend(mode)
    RENDER_PRE.append(render_pre)


def unregister():
    unregister_msgbus()
    # bpy.types.VIEW3D_HT_header.remove(mode)
    RENDER_PRE.remove(render_pre)

    # print('un update')
