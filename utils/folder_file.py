import os,bpy

def open_folder(path):
    import platform
    import subprocess

    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        os.system('xdg-open "%s" %s &' % (path, "> /dev/null 2> /dev/null"))  # > sends stdout,  2> sends stderr

def BLT全局翻译():
    path_addons = os.path.normpath(os.path.join((bpy.utils.user_resource('DATAFILES', path="locale\zh_CN\LC_MESSAGES", create=False)),'blender.mo'))
    return os.path.exists(path_addons)
# path_addons = os.path.normpath(os.path.join((bpy.utils.user_resource('CONFIG', path="locale\zh_CN\LC_MESSAGES", create=False)),'blender.mo'))

# path_addons = os.path.normpath(os.path.join((bpy.utils.user_resource('DATAFILES', path="locale\zh_CN\LC_MESSAGES", create=False)),'blender.mo'))
# print(os.path.exists(path_addons))

# import os

# DIRNAME, FILENAME = os.path.split(__file__)
# IDNAME = os.path.splitext(FILENAME)[0]


# print(os.path.split(__file__))
# print(FILENAME)
# print(IDNAME)
