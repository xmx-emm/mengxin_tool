from bpy.types import Operator as OPS
from bpy.props import EnumProperty
import bpy

class switch_translate(OPS):
    """切换翻译"""
    bl_idname = 'emm.switch_translate'
    bl_label = '切换翻译'
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = """
    左键                - 切换界面翻译
    ctrl+左键        - 切换工具提示
    shift+左键      - 切换工具提示和界面    """
    # alt+左键         - 切换新建

    # ctrl+alt+shift+左键 切换所有

    mode: EnumProperty(
        name="操作的模式",
        default='interface',
        items=(
            ('interface', "界面", ""),
            ('tooltips', "工具提示", ""),
            ('interface_tooltips', "工具提示和界面都有", ""),
            ('all_', "切换所有", ""),
            ('new', "新建名称", ""),
        ),
    )

    # def __init__(self):
    # bpy.context.preferences.view.use_translate_interface
    # bpy.context.preferences.view.use_translate_new_dataname
    # bpy.context.preferences.view.use_translate_tooltips
    # pv = bpy.context.preferences.view
    # it = pv.use_translate_interface
    # nt = pv.use_translate_new_dataname
    # tt = pv.use_translate_tooltips

    def invoke(self, context, event):
        if not event.alt and not event.shift and not event.ctrl and not event.oskey:
            self.interface()
            if pr:
                print('左键')
            return {'FINISHED'}
        if event.ctrl and not event.alt and not event.shift and not event.oskey:
            self.tooltips()
            if pr:
                print('ctrl+左键')
            return {'FINISHED'}
        if event.shift and not event.alt and not event.ctrl and not event.oskey:
            self.interface_tooltips()
            if pr:
                print('shift+左键')
            return {'FINISHED'}
        if event.alt and not event.shift and not event.ctrl and not event.oskey:
            self.new()
            if pr:
                print('alt+左键')
            return {'FINISHED'}
        if event.alt and event.shift and event.ctrl and not event.oskey:
            self.all_()
            if pr:
                print('ctrl+alt+shift+左键')
            return {'FINISHED'}
        else:
        #     self.report({"INFO"}, self.bl_description)
            return self.execute(context)

    def interface(self):
        i = bpy.context.preferences.view
        i.use_translate_interface = i.use_translate_interface ^ True
        return {'FINISHED'}

    def tooltips(self):
        i = bpy.context.preferences.view
        i.use_translate_tooltips = i.use_translate_tooltips ^ True
        return {'FINISHED'}

    def interface_tooltips(self):
        i = bpy.context.preferences.view
        i.use_translate_interface = i.use_translate_interface ^ True
        i.use_translate_tooltips = i.use_translate_tooltips ^ True
        return {'FINISHED'}

    def all_(self):
        i = bpy.context.preferences.view
        i.use_translate_interface = i.use_translate_interface ^ True
        i.use_translate_tooltips = i.use_translate_tooltips ^ True
        i.use_translate_new_dataname = i.use_translate_new_dataname ^ True
        return {"FINISHED"}

    def new(self):
        i = bpy.context.preferences.view
        i.use_translate_new_dataname = i.use_translate_new_dataname ^ True
        return {"FINISHED"}

    def execute(self, context):
        mo = self.mode
        if mo == 'interface':
            self.interface()
        if mo == 'tooltips':
            self.tooltips()
        if mo == 'interface_tooltips':
            self.interface_tooltips()
        if mo == 'all_':
            self.all_()
        if mo == 'new':
            self.new()
        # else:
            # self.report({"INFO"}, self.bl_description)

        return {'FINISHED'}

pr = True  # print_re_info True or False
