import os,sys
import os as _os
import bpy
import addon_utils as _addon_utils
from ..utils.blender_class import PRESET_PATHS

B = bpy.utils
pr = False #print_re_info True or False
reg = (
    # icon,
    # addonTemplates,
)
def 路径():
    return os.path.dirname(os.path.realpath(__file__))
path_ = os.path.dirname(os.path.realpath(__file__))

def preset_paths(subdir):
    """
    Returns a list of paths for a specific preset.

    :arg subdir: preset subdirectory (must not be an absolute path).
    :type subdir: string
    :return: script paths.
    :rtype: list
    """
    dirs = []
    for path in bpy.utils.script_paths(subdir="presets", check_all=True):
        directory = _os.path.join(path, subdir)
        # print(f'EMM{directory}____')
        if not directory.startswith(path):
            raise Exception("invalid subdir given %r" % subdir)
        elif _os.path.isdir(directory):
            dirs.append(directory)

    directory = _os.path.join(路径(), subdir)
    # print(f'EMM{directory}____')
    if not directory.startswith(路径()):
        raise Exception("invalid subdir given %r" % subdir)
    elif _os.path.isdir(directory):
        dirs.append(directory)


    # Find addons preset paths
    for path in _addon_utils.paths():
        # print(f'{directory}____')
        directory = _os.path.join(path, "presets", subdir)
        if _os.path.isdir(directory):
            dirs.append(directory)

    return dirs

# def 

def 资产_register():

    B.preset_paths = preset_paths
    # for i in reg:
    #     i.register()
    if pr:
        print('re_assets')

    # if path not in sys.path:
    #     sys.path.append(path)


def 资产_unregister():

    # if path  in sys.path:
    #     sys.path.remove(path)
    B.preset_paths = PRESET_PATHS

    # for i in reg:
    #     i.unregister()

    if pr:
        print('un_re_assets')

# if __name__ == "__main__":
#     register()