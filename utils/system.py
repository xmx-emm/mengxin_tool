import os
import sys
import bpy

def open_folder(path):
    import platform
    import subprocess

    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        os.system('xdg-open "%s" %s &' % (path, "> /dev/null 2> /dev/null"))  # > sends stdout,  2> sends stderr


def abspath(path):
    return os.path.abspath(bpy.path.abspath(path))

def Exit():
    print("程序退出测试")
    sys.exit()