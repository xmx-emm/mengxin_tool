

bl_info = {
    "name": "1a_乱七八糟的插件",
    "author": "小萌新",
    "description": "EMM,新出的插件",
    "blender": (2, 93, 0),  # 插件所支持的blender版本
    "location": "",  # 插件显示的位置
    "warning": "",         # 警告信息
    "category": "3D View",  # 归类信息 搜索插件的时候显示的分类
    "version": (1, 0, 0, "测试版")
}

from . import ui,ops

reg = (ui, ops)

def register():
    for cls in reg:
        cls.register()
    print('register EMM addon')
    print("registered %s %s." % (bl_info["name"], ".".join([str(i) for i in bl_info['version']])))

def unregister():
    for cls in reg:
        cls.unregister()
    print('unregister EMM addon')
    print("Unregistered %s %s." % (bl_info["name"], ".".join([str(i) for i in bl_info['version']])))


if __name__ == "__main__":
    print('插件正在启用')
    register()