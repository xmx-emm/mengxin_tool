
import os
import bpy
from bpy.utils.toolsystem import ToolDef
from bl_ui.space_toolsystem_toolbar import VIEW3D_PT_tools_active as view3d_tools
from bl_ui.space_toolsystem_toolbar import IMAGE_PT_tools_active as image_tools
###### register 传入同目录的restore_ui里面，再由__init__.py调用


def bc_():
    wm = bpy.context.window_manager

    if hasattr(wm, 'bc'):
        return bpy.context.preferences.addons[wm.bc.addon].preferences

    return False


def getToolList(spaceType, contextMode):
    from bl_ui.space_toolsystem_common import ToolSelectPanelHelper
    cls = ToolSelectPanelHelper._tool_class_from_space_type(spaceType)
    return cls._tools[contextMode]


def icons(toolbar):
    return os.path.join(os.path.dirname(__file__), '..', 'assets\icons', toolbar)


@ToolDef.from_fn
def EMM_UV_ObjectEditMode():
    return dict(
        idname="emm.uv_edit.edit_mode",
        label="UV工具",
        description="在编辑模式下的UV工具箱",
        icon=icons('UvEdit'),
        widget=None,
        # keymap = "3D视图工具: 编辑模式下的UV工具箱"
        # ~ draw_settings = drawSettingsFT,
    )


@ToolDef.from_fn
def EMM_UV_Edit_UVmode():
    return dict(
        idname="emm.uv_edit.uv_mode",
        label="UV工具",
        description="在2DUV模式下的UV工具箱",
        icon=icons('UvEdit'),
        widget=None,
        # keymap="2DUV工具: 编辑模式下的UV工具箱"
        # ~ draw_settings = drawSettingsFT,
    )


@ToolDef.from_fn
def EMM_Sculpt():
    return dict(
        idname="emm.sculpt.sculpt_mode",
        label="雕刻工具",
        description="在雕刻模式下的工具",
        icon=icons('Sculpt'),
        widget=None,
        # keymap = "3D视图工具: 雕刻模式下的工具箱"
        # ~ draw_settings = drawSettingsFT,
    )


@ToolDef.from_fn
def EMM_Object_ObjMode():
    return dict(
        idname="emm.Object_mode",
        label="工具",
        description="工具",
        icon=icons('Object_Mode_Tool'),
        widget=None,
        # keymap="3D视图工具: 雕刻模式下的工具箱"
        # ~ draw_settings = drawSettingsFT,
    )


@ToolDef.from_fn
def EMM_Object_EditMode():
    return dict(
        idname="emm.Edit_mode",
        label="工具",
        description="工具",
        icon=icons('Object_Edit_Tool'),
        widget=None,
        # keymap="3D视图工具: 雕刻模式下的工具箱"
        # ~ draw_settings = drawSettingsFT,
    )

# EDIT_MESH = view3d_tools._tools['EDIT_MESH']
# SCULPT = view3d_tools._tools['SCULPT']
# PARTICLE = view3d_tools._tools['PARTICLE']
# EDIT_TEXT = view3d_tools._tools['EDIT_TEXT']
# EDIT_CURVE = view3d_tools._tools['EDIT_CURVE']
# OBJECT = view3d_tools._tools['OBJECT']

# UV = image_tools._tools['UV']



lists = {
    'UV': [('EMM_UV_Edit_UVmode'), ],

    'EDIT_MESH': [('EMM_UV_ObjectEditMode'), ('EMM_Object_EditMode')],
    'OBJECT': [('EMM_Object_ObjMode'), ],
    'SCULPT': [('EMM_Sculpt')],
}


## VIEW_3D PROPERTIES IMAGE_EDITOR VIEW NODE_EDITOR SEQUENCE_EDITOR

debug = False

EDIT_MESH = getToolList('VIEW_3D', 'OBJECT')
def register():

    ###bc
    bc = None
    if not bc_():
        EDIT_MESH.append(None)
    else:
        bc = EDIT_MESH.pop()
    ###bc

    for lis in lists:
        li = lists.get(lis)
        eli=[]
        try:

            if lis in ['EDIT_MESH', 'OBJECT', 'SCULPT']:
                for l in li:
                    eli.append(eval(l))
                tools = getToolList('VIEW_3D', lis)
                tools += eli
                if debug:print(lis, '_ADD__', li)
                del tools, eli

            elif lis == 'UV':
                for l in li:
                    eli.append(eval(l))
                tools = getToolList('IMAGE_EDITOR', lis)
                tools += eli
                if debug:print(lis, '_ADD__', li)
                del tools, eli
            else:
                print(lis,' 未定义')
                pass

            
        except Exception as e:
            print('T工具栏添加++ 注册错误!!!  ', lis, '___', '\n', e.args)


    ###bc
    if bc_():
        EDIT_MESH.append(bc)
    ###bc

def unregister():
    debug = True
    for lis in lists:
        li = lists.get(lis)
        try:
            if lis in ['EDIT_MESH', 'OBJECT', 'SCULPT']:

                for l in li:
                    tools = getToolList('VIEW_3D', lis)                    
                    if debug:print(lis, '_DEL__', li)
                    tools.remove(eval(l))
                    clear_trailing_separators(tools)
                del tools
                
                # for i in li:
                #     tools = getToolList('VIEW_3D', lis)
                #     index = tools.index(eval(i)) - 1  # None
                #     tools.pop(index)
                #     tools.remove(eval(i))
                #     if debug:print(lis, '_DEL__', i)
                # del tools

            # elif lis == 'UV':
            #     for l in li:               
            #         if debug:print(lis, '_DEL__', li)
            #         tools = getToolList('IMAGE_EDITOR', lis)
            #         index = tools.index(eval(l))
            #         tools.remove(eval(l))
            #         tools.pop(index)
            #         del tools
            else:
                print(lis,' 未定义')
                pass
        except Exception as e:
            print('T工具栏删除-- 注销错误!!!  ', lis, '_DEL__', e)


def clear_trailing_separators(tools):
    if not tools[-1]:
        tools.pop()
        clear_trailing_separators(tools)
