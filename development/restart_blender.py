import sys
import os
import bpy
from bpy.types import Operator as OPS
from bpy.utils import register_class, unregister_class
from bpy.props import EnumProperty, IntProperty
import platform  # 导入作为系统判断


class Restart_Blender(OPS):
    """重启bl(mode = '操作执行方式'  forNum = '打开blender次数')
    mode = 'restart' 正常重启Blender
    mode = 'Double_open' 双开Blender
    mode = 'Three_open' 三开Blender
    mode = 'no_exit_cmd' 不退出cmd重启Bl    ##emm,然而看起来好像两个是差不多的
    mode = 'for_bl'        一直循环打开bl，爆炸专用,但是只能保留一次的cmd,emm
    """
    bl_idname = 'emm.restart_blender'
    bl_label = '重启Blender'
    bl_description = """左键                - 正常重启Blender
ctrl+左键        - 双开Blender
shift+左键      - 三开Blender
alt+左键         - 不退出cmd重启Bl(但是只能保留一次的cmd)

ctrl+alt+shift+左键 循环打开bl，爆炸专用"""
    bl_options = {'REGISTER', 'UNDO'}

    blpath = ()  # bl路径
    mode: EnumProperty(
        name="操作的模式",
        default='no',
        items=(
            ('restart', "重启Blender", ""),
            ('Double_open', "双开Blender", ""),
            ('Three_open', "三开Blender", ""),
            ('no_exit_cmd', "不退出cmd重启Bl", ""),
            ('for_bl', "一直循环打开bl，爆炸专用", ""),
            ('no', "no", "no"),

            )
        )
    forNum: IntProperty(name="打开bl数量", default=20,
                        max=114514, min=3, subtype="FACTOR")

    def __init__(self):
        pass

    # @classmethod
    # def poll(cls, context):
    #     return (
    #         context.space_data.type == 'VIEW_3D'
    #         or context.active_object is not None
    #         or context.active_object.mode == 'OBJECT')

    # got blender.exe path
    # C:\Program Files (x86)\Steam\steamapps\common\Blender\blender.exe

    def getpath(self):
        # dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))
        self.blpath = blpath = os.path.realpath(sys.argv[0])
        # C:\Program Files (x86)\Steam\steamapps\common\Blender
        s = str(blpath[:-12])
        self.with_restart = (f'''
        @chcp 65001
        @title 重启bl
        :forblop
        tasklist|find /i "Blender.exe" && taskkill /f /im "Blender.exe" || goto opbl
        
        :opbl
        ::cd /d {s}
        blender.exe
        exit''')

        self.with_no_exit_cmd = (f'''
        @chcp 65001
        @title 重启bl但保持cmd
        :forblop
        tasklist|find /i "Blender.exe" && Blender.exe || goto opbl
        
        :opbl
        ::cd /d {s}
        blender.exe
        ''')

        # b=(f'@chcp 65001 ^@title 双开bl 可同时开启两个blender.exe  !! 保持当前blender.exe运行，并打开一个新的bl ^cd /d {s}^blender.exe ^exit')
        # c=(f'@chcp 65001\n@title 仨开bl 可同时开启仨个blender.exe  !! 保持当前blender.exe运行，并打开两个新的bl\n\n:forblop\ntasklist|find /i "Blender.exe" && goto opbl || goto opbl\n\n:opbl\ncd /d {s}\nblender.exe\nblender.exe\nexit')
        # d=(f'@chcp 65001\n@title 重启bl 仅支持开启一个blender.exe  !! 不然会一直循环下去，直到没有blender.exe才会停止，并打开bl\n\n:forblop\n\ntasklist|find /i "Blender.exe" && taskkill /f /im "Blender.exe || goto opbl\n\n:opbl\ncd /d {s}\nblender.exe')
        # choice /t 5 /d y /n >nul 时停
        # print(blpath)

    def invoke(self, context, event):
        if not event.alt and not event.shift and not event.ctrl and not event.oskey:
            self.restart()
            if pr:
                print('左键')
            return {'FINISHED'}
        if event.ctrl and not event.alt and not event.shift and not event.oskey:
            self.Double_open()
            if pr:
                print('ctrl+左键')
            return {'FINISHED'}
        if event.shift and not event.alt and not event.ctrl and not event.oskey:
            self.Three_open()
            if pr:
                print('shift+左键')
            return {'FINISHED'}
        if event.alt and not event.shift and not event.ctrl and not event.oskey:
            self.no_exit_cmd()
            if pr:
                print('alt+左键')
            return {'FINISHED'}
        if event.alt and event.shift and event.ctrl and not event.oskey:
            self.for_bl()
            if pr:
                print('ctrl+alt+shift+左键')
            return {'FINISHED'}

        elif event.oskey and not event.alt and not event.shift and not event.ctrl:
            if pr:
                print('os+左键')
            # self.forNum = 10
            self.for_bl()
            return {'FINISHED'}
        else:
            self.report({"INFO"}, self.bl_description)
            return {'FINISHED'}

    def restart(self):
        self.getpath()
        a = self.with_restart
        os.system('@ if not exist "C:/tmp" md "C:/tmp"')
        with open("C:/tmp\Restart_Blender.cmd", "w") as f:
            f.write(str(a))
        # print('restart_blender')
        # print('exitBledner________')

        os.system('C:/tmp\Restart_Blender.cmd')
        bpy.ops.wm.quit_blender
        return {"FINISHED"}

    def Double_open(self):
        os.system('start blender.exe')
        return {"FINISHED"}

    def Three_open(self):
        os.system('start blender.exe')
        os.system('start blender.exe')
        return {"FINISHED"}

    def no_exit_cmd(self):
        self.getpath()
        a = self.with_no_exit_cmd
        os.system('@ if not exist "C:/tmp" md "C:/tmp"')
        with open("C:/tmp\Restart_Blender.cmd", "w") as f:
            f.write(str(a))
        os.system('start /tmp\Restart_Blender.cmd')
        os.system('taskkill /f /im "Blender.exe"')
        os.system('start blender.exe')
        return {"FINISHED"}

    def for_bl(self):
        fn = self.forNum
        print('开始作死模式----------------------------')
        for i in range(fn):
            print(f"循环打开第 {i} 个Blender")
            os.system('start blender.exe')
        return {"FINISHED"}

    def execute(self, context):
        mo = self.mode
        if(platform.system() == 'Windows'):
            print('Windows系统')
            if mo == 'restart':
                self.restart()
            if mo == 'Double_open':
                self.Double_open()
            if mo == 'Three_open':
                self.Three_open()
            if mo == 'no_exit_cmd':
                self.no_exit_cmd()
            if mo == 'for_bl':
                self.for_bl()
            else:
                self.report({"INFO"}, self.bl_description)
                return {'FINISHED'}

        elif(platform.system() == 'Linux'):
            print('此功能暂不支持Linux系统')
        else:
            print('此功能暂不支持此系统')

        return {'FINISHED'}


pr = True  # print_re_info True or False
reg = (
    # Restart_Blender,
)


def register():

    for i in reg:
        register_class(i)
        if pr:print('re_restart_blender')


def unregister():

    for i in reg:
        unregister_class(i)

    if pr:print('un_re_restart_blender')


if __name__ == "__main__":
    register()
