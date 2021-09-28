from .. registration import keys as keysdict
from .. registration import classes as classesdict


from bpy.utils import previews
from bpy.utils import register_class, unregister_class

import os
import bpy

"""
工具需要传入布尔属性
然后注册类需在注册表里面(registration)
需要有一个 get_名称 
然后在get_tools()或是get_pie_menus内需要有一个类，在启动时注册此快捷键
"""

def get_path():
    return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def get_addon_name():
    return os.path.basename(get_path())

def get_prefs():
    return bpy.context.preferences.addons[get_addon_name()].preferences

def uprefs():
    return getattr(bpy.context, "user_preferences", None) or \
        getattr(bpy.context, "preferences", None)


def register_icons():
    path = os.path.normpath(os.path.join(get_prefs().path, "assets\icons"))
    icons = previews.new()

    for i in sorted(os.listdir(path)):
        if i.endswith(".png"):
            iconname = i[:-4]
            filepath = os.path.join(path, i)

            icons.load(iconname, filepath, 'IMAGE')

    return icons


def unregister_icons(icons):
    previews.remove(icons)



def register_classes(classlists, debug=False):
    classes = []

    for classlist in classlists:
        for fr, imps in classlist:
            impline = "from ..%s import %s" % (fr, ", ".join([i[0] for i in imps]))
            classline = "classes.extend([%s])" % (", ".join([i[0] for i in imps]))

            exec(impline)
            exec(classline)

    for c in classes:
        if debug:
            print(f"REGISTERING__萌新工具箱__{c}_", )
        try:
            register_class(c)
        except Exception as e:
            print(f'注册错误—类------—{c}—\n———----错误值{e}')
    return classes

def unregister_classes(classes, debug=False):
    for c in classes:
        if debug:
                print(f"UN-REGISTERING__萌新工具箱__{c}_", )
        unregister_class(c)

def get_classes(classlist):
    classes = []

    for fr, imps in classlist:
        if "operators" in fr:
            type = "OT"
        elif "pies" in fr or "menus" in fr:
            type = "MT"

        for imp in imps:
            idname = imp[1]
            rna_name = "EMMMMM_%s_%s" % (type, idname)

            c = getattr(bpy.types, rna_name, False)

            if c:
                classes.append(c)

    return classes

def register_keymaps(keylists):
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    keymaps = []

    if kc:
        for keylist in keylists:
            for item in keylist:
                # print(item, "______keylists")
                keymap = item.get("keymap")
                space_type = item.get("space_type", "EMPTY")

                if keymap:
                    km = kc.keymaps.new(name=keymap, space_type=space_type)

                    if km:
                        idname = item.get("idname")
                        type = item.get("type")
                        value = item.get("value")

                        shift = item.get("shift", False)
                        ctrl = item.get("ctrl", False)
                        alt = item.get("alt", False)
                        oskey = item.get("oskey", False)
                        any = item.get("any", False)
                        key_modifier = item.get("key_modifier", 'NONE')

                        kmi = km.keymap_items.new(
                            idname, type, value, shift=shift, ctrl=ctrl, alt=alt, oskey=oskey, any=any, key_modifier=key_modifier)

                        try:                           
                            properties = item.get("properties")

                            if properties:
                                if get_prefs().debug_keymaps:print(f"注册快捷键 __{idname}__{properties}")

                                for name, value in properties:
                                    setattr(kmi.properties, name, value)  
                            else:
                                if get_prefs().debug_keymaps:print("注册快捷键",idname)
                            keymaps.append((km, kmi))

                        except ValueError as e:
                            print("Value Error found!  ", e.args)
    else:
        print("WARNING: Keyconfig not availabe, skipping 萌新工具箱 keymaps")

    return keymaps

def unregister_keymaps(keymaps):
    for km, kmi in keymaps:
        if get_prefs().debug_keymaps:print("注销快捷键", kmi.idname)
        km.keymap_items.remove(kmi)

def get_keymaps(keylist):
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    keymaps = []

    for item in keylist:
        keymap = item.get("keymap")

        if keymap:
            km = kc.keymaps.get(keymap)

            if km:
                idname = item.get("idname")

                for kmi in km.keymap_items:
                    if kmi.idname == idname:
                        properties = item.get("properties")

                        if properties:
                            if all([getattr(kmi.properties, name, None) == value for name, value in properties]):
                                keymaps.append((km, kmi))

                        else:
                            keymaps.append((km, kmi))

    return keymaps

def activate(self, register, tool):
    debug = True
    debug = get_prefs().debug
    # print(get_prefs().debug, '这是打印的debug')
    # print(get_prefs().debug_keymaps,'这是打印的debug_keymaps')
    # print(get_prefs().debug_class,'这是打印的debug_class')

    name = tool.replace("_", " ").title()


    if register:
        classlist, keylist, _ = eval("get_%s()" % (tool))



        classes = register_classes(classlist, debug=debug)


        from .. import classes as startup_classes

        for c in classes:
            if c not in startup_classes:
                startup_classes.append(c)



        keymaps = register_keymaps(keylist)

        from .. import keymaps as startup_keymaps
        for k in keymaps:
            if k not in startup_keymaps:
                startup_keymaps.append(k)

        # if classes and debug:
        #     print("Registered 萌新工具箱' %s" % (name))
        
        classlist.clear()
        keylist.clear()



    else:

        keylist = keysdict.get(tool.upper())

        if keylist:
            keymaps = get_keymaps(keylist)

            from .. import keymaps as startup_keymaps
            for k in keymaps:
                if k in startup_keymaps:
                    startup_keymaps.remove(k)

            unregister_keymaps(keymaps)



        classlist = classesdict[tool.upper()]


        classes = get_classes(classlist)

        from .. import classes as startup_classes

        for c in classes:
            if c in startup_classes:
                startup_classes.remove(c)


        unregister_classes(classes, debug=debug)

        # if classes and debug:
        #     print("Unregistered 萌新工具箱' %s" % (name))

def keymaps(self, register, tool):
    # debug = False
    # debug = False

    # name = tool.replace("_", " ").title()

    if register:
        keylist, _ = eval("get_%s()" % (tool))
        keymaps = register_keymaps(keylist)

        from .. import keymaps as startup_keymaps
        for k in keymaps:
            if k not in startup_keymaps:
                startup_keymaps.append(k)
        keylist.clear()

    if register == False:
        
        keylist = keysdict.get(tool.upper())
        if keylist:
            keymaps = get_keymaps(keylist)
            
            from .. import keymaps as startup_keymaps
            for k in keymaps:
                if k in startup_keymaps:
                    startup_keymaps.remove(k)

            unregister_keymaps(keymaps)
    
def get_core():
    return [classesdict["CORE"]]


def get_tools():
    classlists = []
    keylists = []
    count = 0

    keylists, count = get_switch_translate(keylists, count)
    keylists, count = get_console_toggle(keylists, count)
    keylists, count = get_custom_keymap(keylists, count)


    return classlists, keylists, count

def get_pie_menus():
    classlists = []
    keylists = []
    count = 0
    
    classlists, keylists, count = get_modes_pie     (classlists, keylists, count)
    classlists, keylists, count = get_views_pie     (classlists, keylists, count)
    classlists, keylists, count = get_space_pie     (classlists, keylists, count)
    classlists, keylists, count = get_select_pie    (classlists, keylists, count)
    classlists, keylists, count = get_delete_pie    (classlists, keylists, count)
    classlists, keylists, count = get_C_pie         (classlists, keylists, count)
    classlists, keylists, count = get_B_pie         (classlists, keylists, count)
    classlists, keylists, count = get_V_pie         (classlists, keylists, count)
    return classlists, keylists, count



#仅快捷键
def get_switch_translate(keylists=[], count=0):
    if get_prefs().activate_switch_translate:
        keylists.append(keysdict["SWITCH_TRANSLATE"])
        count += 1

    return keylists, count
def get_console_toggle(keylists=[], count=0):
    if get_prefs().activate_console_toggle:
        keylists.append(keysdict["CONSOLE_TOGGLE"])
        count += 1

    return  keylists, count
def get_custom_keymap(keylists=[], count=0):
    if get_prefs().activate_custom_keymap:
        keylists.append(keysdict["CUSTOM_KEYMAP"])
        count += 1



    return keylists, count

#饼菜单
def get_modes_pie(classlists=[],keylists=[],count=0):
    if get_prefs().activate_modes_pie:
        classlists.append(classesdict["MODES_PIE"])
        keylists.append(keysdict["MODES_PIE"])
        count += 1
    return classlists, keylists ,count

def get_views_pie(classlists=[],keylists=[],count=0):
    if get_prefs().activate_views_pie:
        classlists.append(classesdict["VIEWS_PIE"])
        keylists.append(keysdict["VIEWS_PIE"])
        count += 1
    return classlists, keylists ,count

def get_space_pie(classlists=[],keylists=[],count=0):
    if get_prefs().activate_space_pie:
        classlists.append(classesdict["SPACE_PIE"])
        keylists.append(keysdict["SPACE_PIE"])
        count += 1
    return classlists, keylists ,count

def get_select_pie(classlists=[],keylists=[],count=0):
    if get_prefs().activate_select_pie:
        classlists.append(classesdict["SELECT_PIE"])
        keylists.append(keysdict["SELECT_PIE"])
        count += 1
    return classlists, keylists ,count

def get_delete_pie(classlists=[],keylists=[],count=0):
    if get_prefs().activate_delete_pie:
        classlists.append(classesdict["DELETE_PIE"])
        keylists.append(keysdict["DELETE_PIE"])
        count += 1
    return classlists, keylists ,count

def get_C_pie(classlists=[],keylists=[],count=0):
    if get_prefs().activate_C_pie:
        classlists.append(classesdict["C_PIE"])
        keylists.append(keysdict["C_PIE"])
        count += 1
    return classlists, keylists ,count

def get_B_pie(classlists=[],keylists=[],count=0):
    if get_prefs().activate_B_pie:
        classlists.append(classesdict["B_PIE"])
        keylists.append(keysdict["B_PIE"])
        count += 1
    return classlists, keylists ,count

def get_V_pie(classlists=[],keylists=[],count=0):
    if get_prefs().activate_V_pie:
        classlists.append(classesdict["V_PIE"])
        keylists.append(keysdict["V_PIE"])
        count += 1
    return classlists, keylists ,count
