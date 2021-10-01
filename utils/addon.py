import addon_utils
import bpy,os
context = bpy.context
prefs = context.preferences

##get所有插件
addons = [
    (mod, addon_utils.module_bl_info(mod))
    for mod in addon_utils.modules(refresh=True)
]
addon_map = {mod.__name__: mod for mod in addon_utils.modules()}


def get_addon_user_dirs():
    if bpy.app.version >= (2, 94, 0):
        ## 3.0版本
        addon_user_dirs = tuple(
            p for p in (
                os.path.join(prefs.filepaths.script_directory, "addons"),
                bpy.utils.user_resource('SCRIPTS', path="addons"),
            )
            if p
        )
    else:
        ## 2.93版本
        addon_user_dirs = tuple(
            p for p in (
                os.path.join(prefs.filepaths.script_directory, "addons"),
                bpy.utils.user_resource('SCRIPTS', "addons"),
            )
            if p
        )
    return addon_user_dirs

def get_all_addon():
    for mod, info in addons:
        module_name = mod.__name__
        return module_name

def get_all_activate_addon():
    used_ext = {ext.module for ext in prefs.addons}
    return list(used_ext)

def get_addon(addon, debug=False):

    for mod in addon_utils.modules():
        name = mod.bl_info["name"]
        version = mod.bl_info.get("version", None)
        foldername = mod.__name__
        path = mod.__file__
        enabled = addon_utils.check(foldername)[1]

        if name == addon:
            if debug:
                print(name)
                print("  enabled:", enabled)
                print("  folder name:", foldername)
                print("  version:", version)
                print("  path:", path)
                print()

            return enabled, foldername, version, path
    return False, None, None, None

def get_addon_prefs(addon):
    _, foldername, _, _ = get_addon(addon)
    return bpy.context.preferences.addons.get(foldername).preferences
