# def BLT全局翻译():
import os,bpy
path_addons = os.path.normpath(os.path.join((bpy.utils.user_resource('DATAFILES', path="locale\zh_CN\LC_MESSAGES", create=False)),'blender.mo'))
print(os.path.exists(path_addons))
# C:\Users\32099\AppData\Roaming\Blender Foundation\Blender\3.0\config\locale\zh_CN\LC_MESSAGES
# C:\Users\32099\AppData\Roaming\Blender Foundation\Blender\3.0\datafiles\locale\zh_CN\LC_MESSAGES