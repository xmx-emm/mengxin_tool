import bpy
import os
from bpy.types import Operator as OPS
# from ..utils.registration import get_prefs
from bpy.utils import register_class, unregister_class
from ..utils.folder_file import open_folder as of
pr = False  # print_re_info True or False

class scripting_tool(OPS):
    bl_idname = 'emm.scripting_tool'
    bl_label = '脚本工具'
    bl_options = {'REGISTER', 'UNDO'}
    bl_description = """
    左键                - 使用系统默认文本工具打开文件
    ctrl+左键        - 打开此文本所在的文件夹
    shift+左键      - 从Blender中移除所有脚本或文本"""

    def __init__(self):
        context = bpy.context
        text = context.space_data.text
        self.path = text.filepath  # 文本路径
        dirty = text.is_dirty  # 上次保存后文本被修改过
        library = text.library  # 是否是库文件
        name = text.name  # txt文件名称
        _del = "\\"+name  # 删除文件名称
        self.folder = self.path.replace(_del, '')  # 文件夹

    def invoke(self, context, event):
        if not event.alt and not event.shift and not event.ctrl and not event.oskey:
            self.open_file()
            if pr:
                print('左键')
            return {'FINISHED'}
        if event.ctrl and not event.alt and not event.shift and not event.oskey:
            self.open_folder()
            if pr:
                print('ctrl+左键')
            return {'FINISHED'}
        if event.shift and not event.alt and not event.ctrl and not event.oskey:
            for text in bpy.data.texts:
                print(text.name)
                bpy.ops.text.unlink()
            if pr:
                print('shift+左键')
            return {'FINISHED'}
    #     if event.alt and not event.shift and not event.ctrl and not event.oskey:
    #         self.new()
    #         if pr:
    #             print('alt+左键')
    #         return {'FINISHED'}
    #     if event.alt and event.shift and event.ctrl and not event.oskey:
    #         self.all_()
    #         if pr:
    #             print('ctrl+alt+shift+左键')
    #         return {'FINISHED'}
        else:
            self.report({"INFO"}, self.bl_description)
            return {'FINISHED'}

    def open_file(self):
        of(self.path)

    def open_folder(self):
        of(self.folder)

    def execute(self,context):

        return self.invoke


def register():
    register_class(scripting_tool)


def unregister():
    unregister_class(scripting_tool)


if __name__ == "__main__":
    register()
