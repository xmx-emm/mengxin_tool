import bpy
from .registration import get_prefs

from bpy.app.handlers import persistent

def EMM_object_index():
    for i, j in enumerate(bpy.data.objects):
        j.EMM.object_index = i
        print(i, j.EMM.object_index)

# def EMM_active_object_index():
#     for i, j in enumerate(bpy.data.objects):
#         j.EMM.object_index = i
#         print(i, j.EMM.object_index)


# 自动更新雕刻旋转方式模块
# @persistent

def update_sculpt_switch_rotate_method():
    C = bpy.context  # get 物体上下文
    mode = C.mode  # 物体模式

    if get_prefs().sculpt_switch_rotate_method:
        if mode == 'SCULPT':
            C.preferences.inputs.view_rotate_method = 'TRACKBALL'
        else:
            C.preferences.inputs.view_rotate_method = 'TURNTABLE'
    else:
        C.preferences.inputs.view_rotate_method = 'TURNTABLE'




def 物体变更():
    print('物体变更')

def 渲染检查():
    print('渲染检查')


def 模式切换():
    update_sculpt_switch_rotate_method()        # 更新雕刻旋转方式模块


def 到结束帧后暂停():
    try:    ##渲染时新建的窗口没有emm属性
        screen = bpy.context.screen.EMM

        CC = bpy.context.scene.frame_end
        scene = bpy.context.scene
        if scene.frame_current == CC and bpy.context.screen.is_animation_playing and screen.循环播放 == False:
            bpy.ops.screen.animation_cancel(restore_frame=False)
            if screen.回到起始帧:bpy.ops.screen.frame_jump(end=False)
    except Exception as e:
        # print(e.args)
        pass

# 渲染前
@persistent
def render_pre(self,context):
    print('render_pre')
    # O = bpy.data.objects["Suzanne"].location[2]
    # bpy.data.textures['Texture'].noise_scale = O


@persistent
def 帧更改前frame_change_pre(self,context):
    到结束帧后暂停()
    pass

@persistent
def 帧更改后_frame_change_post(self,context):
    pass


        




#### msgbus
owner = object()
def register_msgbus():
    bpy.msgbus.subscribe_rna(key=(bpy.types.Object, 'mode'),owner=owner,args=(),notify=模式切换,)

    bpy.msgbus.subscribe_rna(key=(bpy.types.Object, 'hide_render'),owner=owner,args=(),notify=渲染检查,)
    bpy.msgbus.subscribe_rna(key=(bpy.types.Object, 'hide_viewport'),owner=owner,args=(),notify=渲染检查,)
    bpy.msgbus.subscribe_rna(key=(bpy.types.ObjectBase, 'hide_viewport'),owner=owner,args=(),notify=渲染检查,)

    bpy.msgbus.subscribe_rna(key=(bpy.types.Collection, 'hide_render'),owner=owner,args=(),notify=渲染检查,)
    bpy.msgbus.subscribe_rna(key=(bpy.types.Collection, 'hide_viewport'),owner=owner,args=(),notify=渲染检查,)
    bpy.msgbus.subscribe_rna(key=(bpy.types.LayerCollection, 'hide_viewport'),owner=owner,args=(),notify=渲染检查,)

    bpy.msgbus.subscribe_rna(key=(bpy.types.ObjectBase, 'object'),owner=owner,args=(),notify=物体变更,)


def unregister_msgbus():
    bpy.msgbus.clear_by_owner(owner)


def reload_msgbus():    #重置
    unregister_msgbus(owner)
    register_msgbus(owner)
#### msgbus______________





from bpy.app.handlers import render_pre as RENDER_PRE
from bpy.app.handlers import frame_change_post
from bpy.app.handlers import frame_change_pre

def register_注册更新数据模块():
    register_msgbus()
    # print('re update')
    # bpy.types.VIEW3D_HT_header.prepend(mode)
    RENDER_PRE.append(render_pre)
    frame_change_pre.append(帧更改后_frame_change_post)
    frame_change_post.append(帧更改前frame_change_pre)


def unregister_注销更新数据模块():
    unregister_msgbus()
    # bpy.types.VIEW3D_HT_header.remove(mode)
    RENDER_PRE.remove(render_pre)
    frame_change_pre.remove(帧更改后_frame_change_post)
    frame_change_post.remove(帧更改前frame_change_pre)

    # print('un update')