import bpy
from .registration import get_emm_prefs


# 自动更新雕刻旋转方式模块
def update_sculpt_switch_rotate_method(self, context):
    C = context     #get 物体上下文
    mode = C.mode   #物体模式

    if get_emm_prefs().sculpt_switch_rotate_method:
        if mode == 'SCULPT':
            C.preferences.inputs.view_rotate_method = 'TRACKBALL'
        else:
            C.preferences.inputs.view_rotate_method = 'TURNTABLE'
    else:
        C.preferences.inputs.view_rotate_method = 'TURNTABLE'

# bpy.types.VIEW3D_HT_header.prepend(update_sculpt_switch_rotate_method)      # 更新雕刻旋转方式模块


# bpy.types.VIEW3D_HT_header.pop(update_sculpt_switch_rotate_method)