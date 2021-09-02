import bpy
from .registration import get_prefs
from bpy.app.handlers import render_pre as RENDER_PRE

from bpy.app.handlers import persistent


# 自动更新雕刻旋转方式模块
# @persistent
def update_sculpt_switch_rotate_method(self, context):
    C = context  # get 物体上下文
    mode = C.mode   #物体模式

    if get_prefs().sculpt_switch_rotate_method:
        if mode == 'SCULPT':
            C.preferences.inputs.view_rotate_method = 'TRACKBALL'
        else:
            C.preferences.inputs.view_rotate_method = 'TURNTABLE'
    else:
        C.preferences.inputs.view_rotate_method = 'TURNTABLE'

#  模式切换
def mode(self,context):
    update_sculpt_switch_rotate_method(self, context)        # 更新雕刻旋转方式模块


# 渲染前
@persistent
def render_pre(self, context):
    print('render_pre')



def register():
    # print('re update')
    bpy.types.VIEW3D_HT_header.prepend(mode)
    RENDER_PRE.append(render_pre)


def unregister():
    bpy.types.VIEW3D_HT_header.remove(mode)
    RENDER_PRE.remove(render_pre)

    # print('un update')
