import addon_utils
import bpy
context = bpy.context
prefs = context.preferences

##get所有插件
addons = [
    (mod, addon_utils.module_bl_info(mod))
    for mod in addon_utils.modules(refresh=True)
]

def get_all_addon():
    for mod, info in addons:
        module_name = mod.__name__
        return module_name

def get_all_activate_addon():
    used_ext = {ext.module for ext in prefs.addons}
    return list(used_ext)


# bcprefs = get_addon_prefs('BoxCutter')

# bcprefs.behavior.orient_method = 'LOCAL'

# a = get_addon('3D Navigation')
# print(a[3])

def get_addon(addon, debug=False):
    import addon_utils

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

