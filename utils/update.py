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
def 更新三键模拟():
    C = bpy.context  # get 物体上下文
    mode = C.mode  # 物体模式

    if get_prefs().雕刻_自动切换模拟3键鼠标:
        if mode == 'SCULPT':
            C.preferences.inputs.use_mouse_emulate_3_button = True
        else:
            C.preferences.inputs.use_mouse_emulate_3_button = False
    # else:
    #     C.preferences.inputs.use_mouse_emulate_3_button = False


def 单位变更():
    print('单位变更')

def 物体变更():
    print('物体变更')

def 渲染检查():
    print('渲染检查')

def 游标变换():
    print('游标变换')

def 模式切换():
    update_sculpt_switch_rotate_method()        # 更新雕刻旋转方式模块
    更新三键模拟()

    #:添加自动切换，但是不需要了
    # if bpy.context.active_object.mode == 'VERTEX_PAINT':
    #     A = bpy.context.screen.name_full
    #     areas = [area for screen in bpy.context.workspace.screens for area in screen.areas if area.type == "VIEW_3D"]

    #     print(bpy.data.screens[A].shading.color_type)


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

def 透视矩阵():
    print('透视矩阵')

def 窗口矩阵():
    print('窗口矩阵')

def 当前视图矩阵():
    print('当前视图矩阵')

def 视图层():
    print('视图层')

def 切换翻译():
    print('切换翻译')

def 顶点组活动项():
    if get_prefs().顶点组同步 and  bpy.context.object.mode =='EDIT':
        bpy.ops.mesh.select_all(action='DESELECT')
        bpy.ops.object.vertex_group_select()
    print('顶点组活动项')

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
    bpy.msgbus.subscribe_rna(key=(bpy.types.UnitSettings, 'length_unit'),owner=owner,args=(),notify=单位变更,)


    bpy.msgbus.subscribe_rna(key=(bpy.types.View3DCursor, 'location'),owner=owner,args=(),notify=游标变换,)
    bpy.msgbus.subscribe_rna(key=(bpy.types.View3DCursor, 'matrix'),owner=owner,args=(),notify=游标变换,)


    bpy.msgbus.subscribe_rna(key=(bpy.types.RegionView3D, 'perspective_matrix'),owner=owner,args=(),notify=透视矩阵,)
    bpy.msgbus.subscribe_rna(key=(bpy.types.RegionView3D, 'window_matrix'),owner=owner,args=(),notify=窗口矩阵,)
    bpy.msgbus.subscribe_rna(key=(bpy.types.RegionView3D, 'view_matrix'),owner=owner,args=(),notify=当前视图矩阵,)

    bpy.msgbus.subscribe_rna(key=(bpy.types.VertexGroups, 'active_index'),owner=owner,args=(),notify=顶点组活动项,)

    bpy.msgbus.subscribe_rna(key=(bpy.types.ViewLayer, 'objects'),owner=owner,args=(),notify=视图层,)

    bpy.msgbus.subscribe_rna(key=(bpy.types.PreferencesView, 'language'),owner=owner,args=(),notify=切换翻译,)

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