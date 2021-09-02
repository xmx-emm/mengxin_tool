#                 ('注册类', [('类名', 'idname 后缀'),('类名','木知')])
#饼菜单按pie结尾  前缀按EMM  饼菜单中缀按_MT_  面板按_MT_ 菜单按_PT_
#wm.call_menu_pie 弹出饼菜单
#所有的面板类先注册
classes = {
    'CORE': [
        ('ui.template_list', [('OBJECT_UL_render_check_slow', '')]),  #
        ('ui.panel', [
            ('EMM_VIEW3D_PT_N_Panel', ''),
            ('EMM_PT_check_slow', ''),
        ]),  #
        ('preferences', [
                                ('EMMUvProperty', ''),
                                ('EMMSculptProperty', ''),
                                ('EMMObjectProperty', ''),
                                ('EMMSceneProperty', ''),
                                ('AddonPreferences', '')]),  # 插件预设面板
        ('utils.modify_keymaps', [('Updaet_Keymaps', '')]),  #
        ('ui.presets.cycles_passes_presets', [('CYCLES_PT_Passes_presets', ''), #cy通道预设类
                                                ('AddPresetCycles_Passes', '')]),
        ('ui.presets.eevee_passes_presets', [('EEVEE_PT_Passes_presets', ''),  # ev通道预设类
                                                ('AddPresetEEVEE_Passes', '')]),
        ('ui.presets.object_display_presets', [('OBJECT_PT_display_presets', ''),  # 物体显示预设类
                                                ('AddPresetObjectDisplay', '')]),
        ('ui.tool.switch_translate', [('switch_translate', '')]),  # 切换翻译     
        ('ui.tool.render_resolution_switch', [('render_resolution_switch', '')]),  # 切换翻译     
        ('development.restart_blender', [('Restart_Blender', '')]),  # 重启Bl                                                
        ('development.scripting_tool', [('scripting_tool', '')]),  # 脚本工具                                                   

        ],

'MODES_PIE': [('ui.pies', [('PieModes_pie', 'modes_pie')])],
'VIEWS_PIE': [('ui.pies', [('PieViewport', 'viewport_pie')])],
'SPACE_PIE': [('ui.pies', [('PieSpace_pie', 'space_pie')])],
'SELECT_PIE': [('ui.pies', [('PieSelect_pie', 'select_pie')])],
'DELETE_PIE': [('ui.pies', [('PieDelete_pie', 'delete_pie')])],
'C_PIE': [('ui.pies', [('Pie_C_pie', 'c_pie')])],
'B_PIE': [('ui.pies', [('Pie_B_pie', 'b_pie')])],
'V_PIE': [('ui.pies', [('Pie_V_pie', 'v_pie')])],
}


"""
'idname': 'wm.call_menu_pie',                   # 所绑定的操作符
'oskey': False,                                 # 组合 win键(win) / command键(mac)
'ctrl': False,                                  # 组合 ctrl
'shift': True,                                  # 组合 shift
'alt': False,                                   # 组合 alt(win) / option(mac)
'key_modifier': 'NONE',         
'any': False,                                   # 任意按键 就是ALT SHIFT CTRL 都可以按
'type': 'A',                                    # 其他按键
'value': 'PRESS',                               # 定义按键状态CLICK_DRAG
DOUBLE_CLICK
CLICK
RELEASE
PRESS
ANY

"properties": {"name": "MY_MT_pietest"}}        # 定义属性 一些操作的模式
"""

keys = {
    'MODES_PIE':   [{'keymap': '3D View', 'space_type': 'VIEW_3D', 'idname': 'wm.call_menu_pie',    'type': 'TAB', 'ctrl':True,    'value': 'CLICK_DRAG', 'properties': [('name', 'EMMMMM_MT_modes_pie')]}],
    'VIEWS_PIE':   [{'keymap': '3D View', 'space_type': 'VIEW_3D', 'idname': 'wm.call_menu_pie',    'type': 'Z',       'value': 'CLICK_DRAG', 'properties': [('name', 'EMMMMM_MT_viewport_pie')]}],
    'SPACE_PIE':   [{'keymap': '3D View', 'space_type': 'VIEW_3D', 'idname': 'wm.call_menu_pie',    'type': 'SPACE',   'value': 'CLICK_DRAG', 'properties': [('name', 'EMMMMM_MT_space_pie')]}],
    'SELECT_PIE':  [{'keymap': '3D View', 'space_type': 'VIEW_3D', 'idname': 'wm.call_menu_pie',    'type': 'A',       'value': 'CLICK_DRAG', 'properties': [('name', 'EMMMMM_MT_select_pie')]}],
    'DELETE_PIE':  [{'keymap': '3D View', 'space_type': 'VIEW_3D', 'idname': 'wm.call_menu_pie',    'type': 'X',       'value': 'CLICK_DRAG', 'properties': [('name', 'EMMMMM_MT_delete_pie')]},
                    # {'keymap': 'Object Mode', 'space_type': 'VIEW_3D', 'idname': 'object.delete',    'type': 'X',       'value': 'RELEASE', 'properties': [('confirm', True)]}
                    ],
    'C_PIE':       [{'keymap': '3D View', 'space_type': 'VIEW_3D', 'idname': 'wm.call_menu_pie',    'type': 'C',       'value': 'CLICK_DRAG', 'properties': [('name', 'EMMMMM_MT_c_pie')]}],
    'B_PIE':       [{'keymap': '3D View', 'space_type': 'VIEW_3D', 'idname': 'wm.call_menu_pie',    'type': 'B',       'value': 'CLICK_DRAG', 'properties': [('name', 'EMMMMM_MT_b_pie')]}],
    'V_PIE':       [{'keymap': '3D View', 'space_type': 'VIEW_3D', 'idname': 'wm.call_menu_pie',    'type': 'V',       'value': 'CLICK_DRAG', 'properties': [('name', 'EMMMMM_MT_v_pie')]}],


    'SWITCH_TRANSLATE':     [{'keymap': 'Window',  'space_type': 'EMPTY',   'idname': 'emm.switch_translate',   'type': 'MIDDLEMOUSE',  'value': 'PRESS',  'ctrl':True,    'shift': True, 'properties': [('mode', 'interface')]}],
    'CONSOLE_TOGGLE':       [{'keymap': 'Window',  'space_type': 'EMPTY',   'idname': 'wm.console_toggle',      'type': 'MIDDLEMOUSE',  'value': 'PRESS',  'ctrl':True,    'alt':True}],
    'CUSTOM_KEYMAP':        [{'keymap': 'Screen',      'idname': 'screen.userpref_show',         'type': 'U',            'value': 'PRESS',   'ctrl':True,'alt':True  },
                            {'keymap': 'Window',      'idname': 'wm.save_homefile',             'type': 'ACCENT_GRAVE', 'value': 'PRESS',   'ctrl':True,'alt':True  },
                            {'keymap': 'Screen',      'idname': 'screen.region_flip',           'type': 'RIGHTMOUSE',    'value': 'PRESS',   'shift':True            },
                            {'keymap': 'Window',      'idname': 'wm.window_fullscreen_toggle',  'type': 'SPACE',        'value': 'PRESS',   'alt':True              },
                            {'keymap': 'Text',        'idname': 'text.run_script',              'type': 'B',    'ctrl':True,        'value': 'PRESS',   'alt':True              },
                            # {'keymap': '3D View',     'idname': 'object.select_grouped',               'type': 'RIGHTMOUSE',    'value': 'DOUBLE_CLICK',   'shift':True ,'properties': [('type', 'COLLECTION'),('extend',True)]},
                            ]
    }



modify_keymapss = {
    # 'M3_MODES_PIE':    [
    #     {'keymap': 'Object Non-modal', 'idname': 'wm.call_menu_pie',  'value':'CLICK', 'properties': [('name', 'MACHIN3_MT_modes_pie')]},
    #     {'keymap': 'Object Non-modal', 'idname': 'wm.call_menu_pie',  'value':'CLICK', 'properties': [('name', 'VIEW3D_MT_object_mode_pie')]}
    #     ],
    # 'MODES_PIE':    [{'keymap': 'Object Non-modal', 'idname': 'view3d.object_mode_pie_or_toggle', 'value': 'CLICK'}],
    # 'VIEWS_PIE':    [{'keymap': '3D View', 'idname': 'wm.call_menu_pie',    'active': False, 'properties': [('name', 'VIEW3D_MT_shading_ex_pie')]}],
    #空格键的修改，因为有仨个，所有需要多个选项
    'SEARCH_SPACE_PIE': [{'keymap': 'Window', 'idname': 'wm.search_menu',     'active': False,       'value': 'CLICK'}],
    'PLAY_SPACE_PIE':   [{'keymap': 'Frames', 'idname': 'screen.animation_play',  'active': False,   'value': 'CLICK'}],
    'TOOLS_SPACE_PIE':  [{'keymap': 'Window', 'idname': 'wm.toolbar',           'active': False,     'value': 'CLICK'}],
    ##---
    # 'SELECT_PIE':    [  {'keymap': 'Object Mode', 'idname': 'object.select_all', 'value': 'CLICK'},
    #                     {'keymap': 'Mesh', 'idname': 'mesh.select_all', 'value': 'CLICK'},      ],
    # 'DELETE_PIE':    [
    #                 {'keymap': 'Object Mode', 'idname': 'object.delete', 'value': 'CLICK'},
    #                 {'keymap': 'Mesh', 'idname': 'wm.call_menu', 'value': 'CLICK', 'properties': [('name', 'VIEW3D_MT_edit_mesh_delete')]},
    #                 # {'keymap': 'Mesh', 'idname': 'mesh.dissolve_mode', 'value': 'CLICK'}     CTRL X删除内容，先不改吧
    #                 ],
    # 'C_PIE':    [{'keymap': '3D View', 'idname': 'view3d.select_circle',  'value': 'CLICK'}     ],
    # 'CTRL_C_PIE':    [{'keymap': '3D View', 'idname': 'view3d.copybuffer',  'value': 'CLICK'}     ],
    # 'B_PIE':    [{'keymap': '3D View', 'idname': 'view3d.select_box', 'value': 'CLICK'}],
    # 'V_PIE':    [{'keymap': 'Mesh', 'idname': 'mesh.rip_move',  'value': 'CLICK'}],

    'TEST':    [{'keymap': '3D View', 'idname': 'view3d.cursor3d',     'active': False, 'alt': True, 'shift': True, 'ctrl': True, 'oskey': True, 'properties': [('name', 'VIEW3D_MT_orientations_pie'), ('', '')]},
                {'keymap': '3D View', 'idname': 'view3d.localview',     'active': False, 'alt':True,'shift':True,'ctrl':True,'oskey':True,   'value': 'PRESS', 'properties': [('name', 'VIEW3D_MT_view_pie')]},
                {'keymap': '3D View', 'idname': 'view3d.localview_remove_from',     'active': False, 'alt':True,'shift':True,'ctrl':True,'oskey':True,   'value': 'PRESS','properties': [('name', 'VIEW3D_MT_snap_pie')]},
                    ],
    }


"""
# Ctrl alt u      bpy.ops.screen.userpref_show()          偏好设置
# Ctrl shift `    bpy.ops.wm.save_homefile()              保存启动文件
# shift 左键         bpy.ops.screen.region_flip()            切换左右区域
# alt 空格   bpy.ops.wm.window_fullscreen_toggle()   窗口全屏
# ctrl 右键 view3d.view_roll        这个先不加
# alt A           text.run_script     运行脚本


# V
# A   mesh.select_all
# C
# Z
# X object.delete
# B   
# TAB 材质模式
# 空格


万物有灵的
ALT 空格 l_light.bool_rchg
e   L_LIGHT_MT_pie

Window
Screen
3D View Generic
View2D
Info
Object Non-modal
3D View

Screen Editing
User Interface
Region Context Menu
View2D Buttons List
Text Generic
Text
Frames
Property Editor
Grease Pencil
Paint Curve
Weight Paint
Vertex Paint
Pose
Object Mode
Curve
Image Paint
Sculpt
Mesh
Armature
Metaball
Lattice
Particle
Font
Console
View3D Gesture Circle
Gesture Box
Gesture Zoom Border
Gesture Straight Line
Gesture Lasso
Standard Modal Map
Animation
Animation Channels
Knife Tool Modal Map
Custom Normals Modal Map
Bevel Modal Map
UV Editor
Paint Stroke Modal
Sculpt Expand Modal
Mask Editing
Markers
Eyedropper Modal Map
Transform Modal Map
Outliner
View3D Fly Modal
View3D Walk Modal
View3D Rotate Modal
View3D Move Modal
View3D Zoom Modal
View3D Dolly Modal
View3D Placement Modal
Graph Editor Generic
Graph Editor
Image Generic
Image
Node Generic
Node Editor
File Browser
File Browser Main
File Browser Buttons
Dopesheet Generic
Dopesheet
NLA Generic
NLA Channels
NLA Editor
SequencerCommon
Sequencer
SequencerPreview
Clip
Clip Editor
Clip Graph Editor
Clip Dopesheet Editor
Time Scrub
Clip Time Scrub
Toolbar Popup


"""
