import bpy
from bpy.types import AddonPreferences as AP
from bpy.types import Operator
from bpy.props import (StringProperty,
                       BoolProperty,
                       FloatProperty,
                       IntProperty,
                       EnumProperty
                       )

from . import list
# from .ui.restore_ui import 开发功能

from .utils.registration import activate, get_addon_name, keymaps, get_path,get_prefs
from .utils.folder_file import BLT全局翻译
from .utils.ui import draw_keymap_items
from .utils.ui import get_icon
from .utils.addon import *

from .ui.tool.maximize_prefs import maximize
from .ui.tool.workspaces_cn import workspaces_cn
from .ui.panel import update_panel_名称

from .ui.presets.object_display_presets import register as object_display_presets
from .ui.presets.eevee_passes_presets import register as eevee_passes_presets
from .ui.presets.cycles_passes_presets import register as cycles_passes_presets

from . import 开发者

臭 =             '''
⬜⬜⬜🏿🏿🏿🏻🏻🏻🏻
⬜⬜🏿🏿🏾🏾🏿🏻🏻🏻
⬜⬜🏿🏼🏽🏽🏼🏻🏻🏻
⬜⬜🏾🏽🏽🏽🏽🏻🏻🏻
⬜⬜🏾🏼🏽🏽🏼🏻🏻🏻
⬜⬜⬜🏾🏼🏼🏼🏻🏻🏻
⬜⬜⬜🏽🏾🏾🏻🏻🏻🏻
⬜⬜⬜🏼🏼🏽🏻🏻🏻🏻
⬜🏿🏿🏿🏿🏼🏿🏿🏻🏻
🏿🏿🏿🏿🏿🏿🏿🏿🏿🏿
嘤～嘿～嘿～啊啊啊啊啊啊啊啊嗯嗯嗯～额啊啊啊啊啊啊啊啊啊～啊啊啊啊啊啊啊    ～啊～啊～啊～啊啊啊～啊～啊～啊～啊啊啊
    '''

preferences_tabs = [
    ("GENERAL", "General", "一些功能开启的地方"),
    ("UI", "Ui", "一些UI启用地方"),
    ("KEYMAPS", "Keymaps", "快捷键设置"),
    ("SCULPT", "Sculpt", "雕刻模式设置"),
    ("ABOUT", "About", "关于此插件信息"),
    ("ADDON", "Addon", "一些插件内容"), ]

def 自定义一些偏好设置_属性():
    A = 偏好设置_属性 = bpy.context.preferences.view
    S = 系统设置_属性 = bpy.context.preferences.system
    I = 视图切换 = bpy.context.preferences.inputs
        
    if 开发者:
        A.ui_scale = 1.5    #界面缩放


    A.language  =  'zh_CN'


    A.show_developer_ui = True      #开发选项
    A.show_tooltips_python = True   #py工具提示
    A.show_statusbar_memory = True  #内存
    A.show_statusbar_stats = True   #场景统计
    A.show_statusbar_version = True #版本
    A.show_statusbar_vram = True    #显存
    A.show_splash = False   #启动画面



    A.use_translate_new_dataname = False    #新建名称
                                                
    S.use_edit_mode_smooth_wire = True      #编辑模式品质
                                                
                                                
    I.use_mouse_depth_navigate = True       #自动深度
    I.use_zoom_to_mouse = True              #缩放至鼠标位置

def 自定义一些快捷键_属性():
    P = bpy.context.window_manager.keyconfigs['Blender'].preferences
    P.use_select_all_toggle = True      #使用全选切换
    P.use_alt_click_leader  = True      #使用ALT点击工具提示
    P.use_pie_click_drag    = True      #拖动显示饼菜单
    P.use_use_v3d_shade_ex_pie  = True  #额外着色饼菜单
    P.use_use_v3d_tab_menu  = True      #饼菜单选项卡

class AddonPreferences(AP):
    path = get_path()
    bl_idname = get_addon_name()


    #杂项属性
    仅过滤用户插件: BoolProperty(name='仅过滤用户插件',description='只过滤用户的插件，其它自带的插件全部启用',default = False)

    prefs = bpy.context.preferences

    addon_map = addon_map
    def addon_filter_items(self, _context):
        import addon_utils
        addon_user_dirs = get_addon_user_dirs()

        items = [
            ('All', "All", "All Add-ons"),
            ('User', "User", "All Add-ons Installed by User"),
        ]

        items_unique = set()

        for addon in bpy.context.preferences.addons:
            module = self.addon_map.get(addon.module)
            info = addon_utils.module_bl_info(module)
            if get_prefs().仅过滤用户插件:
                if (module.__file__.startswith(addon_user_dirs)):
                    items_unique.add(info["category"])
            else:
                items_unique.add(info["category"])

        items.extend([(cat, cat, "") for cat in sorted(items_unique)])        
        return items

    addon_filter: EnumProperty(
        items=addon_filter_items,
        name="Category",
        description="Filter add-ons by category",
    )




    #网格工具
    顶点组同步:BoolProperty(name='顶点组同步',default=False)

    #雕刻
    sculpt_switch_rotate_method: BoolProperty(name="自动切换视图旋转方法", default=True,
                                description='''
        当在雕刻模式时,将会自动切换视图旋转方法为 轨迹球
        在其它模式自动切换为  转盘''')
    
    雕刻_自动切换模拟3键鼠标: BoolProperty(name="自动切换模拟3键鼠标", default=False,
                                description='''
        当在雕刻模式时,将会自动切换模拟3键鼠标为 打开
        在其它模式自动切换为  关闭''')


    n_panel_name: StringProperty(name='插件N面板名称', description='在N面板中的名字啊',
                                 default='EMM', 
                                 update=update_panel_名称
                                 )


    remove_doubles_threshold: FloatProperty(name='按间距合并距离',max=114514,min=0.00000001,default=0.00001)
    ##饼菜单
    def update_activate_modes_pie(self,context):
        activate(self,register=self.activate_modes_pie,tool='modes_pie')
    def update_activate_views_pie(self, context):
        activate(self, register=self.activate_views_pie, tool='views_pie')
    def update_activate_space_pie(self,context):
        
        activate(self,register=self.activate_space_pie,tool='space_pie')
    def update_activate_select_pie(self,context):
        
        activate(self,register=self.activate_select_pie,tool='select_pie')
    def update_activate_delete_pie(self,context):
        
        activate(self,register=self.activate_delete_pie,tool='delete_pie')
    def update_activate_C_pie(self,context):
        
        activate(self,register=self.activate_C_pie,tool='C_pie')
    def update_activate_B_pie(self,context):
        
        activate(self,register=self.activate_B_pie,tool='B_pie')
    def update_activate_V_pie(self,context):
        
        activate(self,register=self.activate_V_pie,tool='V_pie')    
    activate_modes_pie: BoolProperty(name="物体切换", default=False, update=update_activate_modes_pie)
    activate_views_pie: BoolProperty(name="视图切换", default=False, update=update_activate_views_pie)
    activate_space_pie: BoolProperty(name="空格菜单", default=False, update=update_activate_space_pie)
    activate_select_pie: BoolProperty(name="选择菜单", default=False, update=update_activate_select_pie)
    activate_delete_pie: BoolProperty(name="删除菜单", default=False, update=update_activate_delete_pie)
    activate_C_pie: BoolProperty(name="C键", default=False, update=update_activate_C_pie)
    activate_B_pie: BoolProperty(name="B键", default=False, update=update_activate_B_pie)
    activate_V_pie: BoolProperty(name="V键", default=False, update=update_activate_V_pie)


    ##预设
    def update_object_display_presets(self,context):
        object_display_presets()
    def update_render_passes_presets(self,context):
        cycles_passes_presets()
        eevee_passes_presets()
    object_display_presets: BoolProperty(name="物体显示预设", default=True,update=update_object_display_presets)
    render_passes_presets: BoolProperty(name="通道预设", default=True, update=update_render_passes_presets)
    # overlay_shows_presets: BoolProperty(name="叠加层显示预设", default=True)      ##因为叠加层里面的内容太多了，暂时不弄

    ##界面
    def update_activate_switch_translate(self, context):        keymaps(self, register=self.activate_switch_translate, tool="switch_translate")
    def update_activate_console_toggle(self, context):          keymaps(self, register=self.activate_console_toggle, tool="console_toggle")
    activate_switch_translate: BoolProperty(name="翻译快捷键",         default=True,        update=update_activate_switch_translate)
    activate_console_toggle: BoolProperty(name="控制台切换快捷键",     default=True,        update=update_activate_console_toggle)

    #开发工具
    switch_translate: BoolProperty(name="切换翻译", default=False if 开发者 else True)
    console_toggle: BoolProperty(name="控制台切换", default=False)
    restart_blender: BoolProperty(name="重启Bl", default=True if 开发者 else False)
    development_options: BoolProperty(name="开发选项", default=True)
    
    开发模式: BoolProperty(name="开发模式", default=True if 开发者 else False,
        # update=开发功能,
        description='''
        右键添加菜单功能
        '''
        )

    debug_keymaps: BoolProperty(name="快捷键", default=False)
    debug_modify_keymaps: BoolProperty(name="修改键", default=False)
    debug_class: BoolProperty(name="类", default=False)
    debug: BoolProperty(name="DEBUG", default=False)
    
    def update_maximize_prefs(self, context):maximize()        # print('maximize_prefs')
    maximize_prefs: BoolProperty(name="最大化插件选项", default=False,options={'SKIP_SAVE'}, update=update_maximize_prefs    )
    prefs_draw_emm: BoolProperty(name="绘制开发插件面板", default=True if 开发者 else False,update=update_maximize_prefs)

    #自定义内容
    def update_activate_custom_keymap(self,context):            
        keymaps(self, register=self.activate_custom_keymap, tool="custom_keymap")
        自定义一些快捷键_属性()

        # kc = context.window_manager.keyconfigs.user.keymaps
        # km = kc.get('Text')  # get 属性keymap快捷键
        # for kmi in km.keymap_items:
        #     if kmi.idname == 'text.run_script':
        #         if self.activate_custom_keymap:
        #             kmi.type = 'A'
        #         else:
        #             kmi.type = 'P'
                # print(kmi)

    activate_custom_keymap: BoolProperty(name="萌新爱用的快捷键", default=True,update=update_activate_custom_keymap,
        description="""        注册以下快捷键:
        Ctrl Alt U        偏好设置
        Ctrl Shift ~    保存启动文件
        Shift 右键       切换左右区域
        Alt 空格          切换窗口全屏
        Alt A               运行脚本

        使用全选切换    True
        使用ALT点击工具提示     True
        拖动显示饼菜单  True
        额外着色饼菜单  True
        饼菜单选项卡    True
        """
        # Shift 左键双击       选择物体集合
        )

    def update_activate_workspaces_cn(self,context):
        workspaces_cn()
    # activate_customize: BoolProperty(name="Customize", default=True)
    activate_workspaces_cn:BoolProperty(name="翻译工作区名称", default=False,update=update_activate_workspaces_cn,
        description="""注册以下快捷键:
        Ctrl Alt U        偏好设置
        Ctrl Shift ~    保存启动文件
        Shift 左键       切换左右区域
        Alt 空格          切换窗口全屏
        Alt A               运行脚本"""
        )

    def update_偏好设置_属性自定义(self,context):            
        自定义一些偏好设置_属性()
    偏好设置_属性自定义: BoolProperty(name="萌新爱用的偏好设置_属性", default=True,update=update_偏好设置_属性自定义,
        description="""
        无法撤销！！！！！！！！

        开发选项 True
        PY工具提示 True
        内存 True
        场景统计 True
        版本 True
        显存 True
        新建名称 False
        编辑模式品质 True
        自动深度 True
        缩放至鼠标位置 True
        """
        # Shift 左键双击       选择物体集合
        )


    #自动重载脚本
    def update_reload_script(self,context):
        try:
            bpy.ops.text.reload()
            if self.auto_run_script:
                try:
                    bpy.ops.text.run_script()
                    print(f'重载脚本{context.space_data.text.name},并运行此脚本！！！')
                except:
                    print('运行错误！！')
        except:
            print(f'重载脚本{context.space_data.text.name}错误,可能此脚本不存在')
            self.auto_reload_script = False
    reload_script: BoolProperty(name="自动重载", default=True,update=update_reload_script) ##重载脚本,作为触发,没在界面上
    auto_run_script: BoolProperty(name="自动运行脚本开关,只有自动重载脚本打开才能运行",options={'SKIP_SAVE'}, default=False)  ##自动运行用,没在界面上
    auto_reload_script: BoolProperty(name="自动重载脚本开关", default=True)
    scripting_tool: BoolProperty(name="脚本工具箱", default=True)  #界面开关

    ##选项栏
    tabs: EnumProperty(name="Tabs", items=preferences_tabs, default="GENERAL")


    #主绘制 ----------------------
    def draw(self, context):
        layout = self.layout
        column = layout.column(align=True)
        row = column.row(align=False)

        row.prop(self, "tabs", expand=True)
        
        if self.tabs == "UI":row.prop(self, "development_options", expand=True,text="", icon="FILE_SCRIPT")
        
        maximize_prefs_icon = 'FULLSCREEN_EXIT' if self.maximize_prefs else 'FULLSCREEN_ENTER'
        
        row.prop(self, "maximize_prefs", 
        expand=False, 
        emboss=True,
        text=""
        , icon=maximize_prefs_icon)



        box = column.box()
        if self.tabs == "GENERAL":
            self.draw_general(box)

        elif self.tabs == "UI":

            self.draw_ui(box)

        elif self.tabs == "KEYMAPS":
            self.draw_keymaps(box)

        elif self.tabs == "SCULPT":
            self.draw_sculpt(box)

        elif self.tabs == "ABOUT":
            self.draw_about(box)

        elif self.tabs == "ADDON":
            self.draw_addon(box,context)

    使用M3模式切换饼菜单: BoolProperty(name="使用M3模式切换饼菜单", default=True)  #界面开关
    def draw_general(self, box):
        split = box.split(factor=0.5)
        column = split.column()
        gt = 0.25   #拆分系数



        # 第一列----------------
        b = column.box()
        b.label(text="Tools")


        dgicon = 'FILE_BLEND'
        b = b.box()
        c = b.column()  # 将列之间的间距弄小
        c.label(text="饼菜单工具     调整功能后需点击更新快捷键按钮，避免键位冲突")

        gtt = 0.75

        # if self.activate_modes_pie:            
        #     d = c.split(factor=gt)
        #     e = d.split(factor=gtt, align=True)
        #     e.prop(self, 'activate_modes_pie', toggle=True)
        # else:

        d = c.split(factor=gt)
        d.scale_y = 1.2
        d.operator('emm.updaet_keymaps').Updaet_ = 'updaet_keymaps'
        d.alert = True
        d.label(text="更改了饼菜单工具后需点击此按钮进行更新")

        c.separator()
        # c.separator()

        d = c.split(factor=gt)
        d.prop(self, 'activate_modes_pie', toggle=True)
        d.label(text="物体切换 TAB")

        d = c.split(factor=gt)
        d.prop(self, 'activate_views_pie', toggle=True)
        d.label(text="3D视图中的Z键 可快速切换着色,在其它模式也有内容哦")


        d = c.split(factor=gt)
        d.prop(self, 'activate_space_pie', toggle=True)
        if self.activate_space_pie:
            d.alert = True
            d.label(text="启用此功能后请不要经常更换空格建操作方式，避免快捷键错乱!!!")
        else:
            d.label(text="空格饼菜单")

        d = c.split(factor=gt)
        d.prop(self, 'activate_select_pie', toggle=True)
        d.label(text="选择饼菜单 A")
            
        d = c.split(factor=gt)
        d.prop(self, 'activate_delete_pie', toggle=True)
        d.label(text="删除饼菜单 X")

        d = c.split(factor=gt)
        d.prop(self, 'activate_C_pie', toggle=True)
        d.label(text="合并饼菜单 C 键")
            
        d = c.split(factor=gt)
        d.prop(self, 'activate_B_pie', toggle=True)
        d.label(text="属性饼菜单 B 键")
          
        d = c.split(factor=gt)
        d.prop(self, 'activate_V_pie', toggle=True)
        d.label(text="视图饼菜单 V 键")


        # 第二列----------------
        gt = 0.3  # 拆分系数
        b = split.box()
        b.label(text="设置")




        # d = b.split(factor=gt)
        # d.prop(self, 'activate_customize', toggle=True,icon = "TRIA_DOWN" \
        #     if self.activate_customize else "TRIA_RIGHT", 
        #      icon_only = False, emboss = False
        #      )
        #         
        # if self.activate_customize:

        bs = b.box().column()
        
        bs.label(text="自定义一些内容")
        # bs.label(text="自定义内容")
        row = bs.row()
        row.scale_y = 1.3
        # row.scale_x = 1
        row.prop(self, "activate_custom_keymap",icon_value=get_icon('头'))
        row.prop(self, "activate_workspaces_cn",icon_value=get_icon('翻译'))

        row = bs.row()
        row.prop(self, "偏好设置_属性自定义",icon='ALIGN_LEFT')
        if BLT全局翻译() == False:
            row.operator(
                        "wm.url_open", text="使用BLT完善翻译", icon_value=get_icon('BLT'),
                    ).url = list.url.get('BLT')

        if getattr(bpy.types, "EMMMMM_MT_modes_pie", False):
            d = b.box()
            d = d.split(factor=gt)
            d.label(text="物体切换饼菜单")

            d.prop(self, '使用M3模式切换饼菜单', toggle=True)

        if getattr(bpy.types, "EMMMMM_MT_space_pie", False):
            context = bpy.context
            # d = b.box().column(align=True)
            # d.label(text="空格键饼菜单")
            # d.row().prop(self, 'spacebar_action',expand=True)

            # d.operator('emm.updaet_keymaps').Updaet_ = 'updaet_spacebar'
            # d.alert = True
            # d.label(text="更改了空格操作后需点击此按钮进行更新")

        if getattr(bpy.types, "EMMMMM_MT_c_pie", False):
            d = b.box()
            d = d.split(factor=gt)
            d.label(text="C键饼菜单")
            d.prop(self, 'remove_doubles_threshold', toggle=True)

    def draw_ui(self, box):
        split = box.split(factor=0.51, align=False)

        #第一列
        b = split.box()
        uit = 0.3   #拆分系数
        b.label(text="Tools")

        d = b.split(factor=uit)
        f = d.split(factor=0.8, align=True)
        f.prop(self, 'switch_translate', toggle=True)
        f.prop(self, 'activate_switch_translate', toggle=True, icon='EVENT_K',text='')
        d.label(text="在顶栏显示切换翻译按钮;注册CTRL SHIFT 中键的快捷键")

        d = b.box()
        c = d.column()  # 将列之间的间距弄小
        c.label(text='N面板')
        c.prop(self, 'n_panel_name', toggle=True)
        

        if self.development_options:  # 功能开关
            d = b.box()
            c = d.column()  # 将列之间的间距弄小
            c.label(text='开发功能')

            d = c.split(factor=uit)
            d.prop(self, 'restart_blender', toggle=True)
            e = d
            e.alert = True
            e.label(text="在顶栏显示重启BL按钮,开发功能,慎用！！！")
            d = c.split(factor=uit)
            
            f = d.split(factor=0.8, align=True)
            f.prop(self, 'console_toggle', toggle=True)
            f.prop(self, 'activate_console_toggle', toggle=True, icon='EVENT_K',text='')
            d.label(text="在顶栏显示系统控制台切换按钮;注册CTRL ALT 中键的快捷键")

            d = c.split(factor=uit)
            d.prop(self, 'scripting_tool', toggle=True)
            d.label(text="在文本编辑器左下角显示辅助工具")

            d.separator()

            d = c.split(factor=uit)
            d.prop(self, 'prefs_draw_emm', toggle=True)
            d.label(text="绘制插件界面打开文件功能")

            d = c.split(factor=uit)
            d.prop(self, '开发模式', toggle=True)
            d.label(text="开发模式_会加一些开发功能")

            if self.debug:
                b = c.box()
                d = b.row()

                c = d.row()
                c.alert = True
                c.prop(self, 'debug', toggle=True)

                d.prop(self, 'debug_class', toggle=True)
                d.prop(self, 'debug_keymaps', toggle=True)
                d.prop(self, 'debug_modify_keymaps', toggle=True)

            else:
                d = c.split(factor=uit)
                d.prop(self, 'debug', toggle=True)
                d.label(text="启用调试功能,如果开启则会在控制台打印调试信息")

        #第二列
        b = split.box()
        uit = 0.3  # 拆分系数
        d = b.box()
        c = d.column()  # 将列之间的间距弄小
        c.label(text='预设栏')
        d = c.split(factor=uit)
        d.prop(self, 'render_passes_presets', toggle=True)
        d.label(text="在输出通道属性里面显示预设栏(目前仅支持Cy和ev)")
        d = c.split(factor=uit)
        d.prop(self, 'object_display_presets', toggle=True)
        d.label(text="在物体显示属性里面显示预设栏")
        # d = c.split(factor=uit)
        # d.prop(self, 'overlay_shows_presets', toggle=True)
        # d.label(text="在叠加层属性里面显示预设栏")                 ##因为叠加层里面的内容太多了，暂时不弄


    def draw_keymaps(self, box):
        wm = bpy.context.window_manager
        kc = wm.keyconfigs.user

        from . registration import keys

        split = box.split()

        b = split.box()
        b.label(text="Tools")

        if not self.draw_tool_keymaps(kc, keys, b):
            b.label(
                text="No keymappings available, because none of the tools have been activated.")

        b = split.box()
        b.label(text="Pie Menus")

        if not self.draw_pie_keymaps(kc, keys, b):
            b.label(
                text="No keymappings created, because none of the pies have been activated.")

    def draw_sculpt(self, box):
        scf = 0.5
        split = box.split(factor=scf, align=True)

        b = split.box()

        b.label(text="Tools")
        bb = b.box()
        bb.label(text="Tools")

        b = split.box()
        b.label(text="属性")
        b = b.box()
        bb = b.row()
        bb.label(text="视图")
        bb.prop(self, 'sculpt_switch_rotate_method', icon_value=get_icon('p1'))
        bb.prop(self, '雕刻_自动切换模拟3键鼠标', 
        # icon_value=get_icon('p1')
        )

    def draw_about(self, box):
        abf = 0.5
        b = box.column()
        # b.
        layout = box.column()
        label_multiline(layout,text=关于文字)
    def draw_addon(self, box, context):
        adf = 0.5
        split = box.split(factor=0.5, align=False)
        b = split.box()

        bb = b.box()
        bb.label(text="Tools")

        b = split.box()
        b.label(text="Activate")

    def draw_tool_keymaps(self, kc, keysdict, layout):
        drawn = False

        for name in keysdict:
            if "PIE" not in name:
                keylist = keysdict.get(name)

                if draw_keymap_items(kc, name, keylist, layout):
                    drawn = True

        return drawn

    def draw_pie_keymaps(self, kc, keysdict, layout):
        drawn = False

        for name in keysdict:
            if "PIE" in name:
                keylist = keysdict.get(name)

                if draw_keymap_items(kc, name, keylist, layout):
                    drawn = True

        return drawn

关于文字 ='''

emmmmmmmmmmmmmmoeIAWEFAWEFAWUEGHIUAWEHRIGHAWKEJHRGKLJQEARIOUGLKJAWEDRHGJBAKEWGHKAEJHRKGUHALWKEGHKAWHEGIOUHFHOWIEFHO

'''

#多行，直接COPY的KIT的
def label_multiline(layout, text='', icon='NONE', width=-1, max_lines = 10):
    '''
    draw a ui label, but try to split it in multiple lines.

    Parameters
    ----------
    layout
    text
    icon
    width width to split by in character count
    max_lines maximum lines to draw

    Returns
    -------
    True if max_lines was overstepped
    '''
    if text.strip() == '':
        return
    text = text.replace('\r\n','\n')
    lines = text.split('\n')
    if width > 0:
        threshold = int(width / 5.5)
    else:
        threshold = 35
    li = 0
    for l in lines:
        # if is_url(l):
        li+=1
        while len(l) > threshold:
            i = l.rfind(' ', 0, threshold)
            if i < 1:
                i = threshold
            l1 = l[:i]
            layout.label(text=l1, icon=icon)
            icon = 'NONE'
            l = l[i:].lstrip()
            li += 1
            if li > max_lines:
                break;
        if li > max_lines:
            break;
        layout.label(text=l, icon=icon)
        icon = 'NONE'
    if li>max_lines:
        return True
