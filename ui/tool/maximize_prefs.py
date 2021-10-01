import bpy
import os
import addon_utils
from bl_ui.space_userpref import USERPREF_PT_addons
from ...utils.blender_class import  USERPREF
from ...utils.registration import get_prefs, get_addon_name
from ...utils.addon import get_addon_user_dirs
# from ...utils.folder_file import open_folder
from bpy.props import BoolProperty

a = False
# module_name = 'mengxin_tool'        ###最大化插件名称
module_name = get_addon_name()

addons = [
    (mod, addon_utils.module_bl_info(mod))
    for mod in addon_utils.modules(refresh=False)
]


#   最大化显示插件的模块
def 插件面板(self, context):

    prefs = context.preferences

    # for mod, info in addons:
    # module_name = mod.__name__
    layout = self.layout
    col = layout.column()
    col_box = col.column()
    addon_preferences = prefs.addons[module_name].preferences
    # if addon_preferences is not None:
    draw = getattr(addon_preferences, "draw", None)
    if draw is not None:
        addon_preferences_class = type(addon_preferences)
        box_prefs = col_box.box()
        addon_preferences_class.layout = box_prefs
        try:
            draw(context)

            box_prefs.label(text=f"萌新工具箱  {module_name}")
        except:
            import traceback
            traceback.print_exc()
            box_prefs.label(
                text="Error (see console)", icon='ERROR')
        del addon_preferences_class.layout

#bl插件显示模块，无法导入，只能直接copy过来了，后面如果改了的话可能会有问题，指官方更改
def draw_emm(self, context):
    layout = self.layout

    wm = context.window_manager
    prefs = context.preferences
    used_ext = {ext.module for ext in prefs.addons}

    addon_user_dirs = get_addon_user_dirs()
    # Development option for 2.8x, don't show users bundled addons
    # unless they have been updated for 2.8x.
    # Developers can turn them on with '--debug'
    show_official_27x_addons = bpy.app.debug

    # collect the categories that can be filtered on
    addons = [
        (mod, addon_utils.module_bl_info(mod))
        for mod in addon_utils.modules(refresh=False)
    ]

    split = layout.split(factor=0.6)

    row = split.row()
    row.prop(wm, "addon_support", expand=True)

    row = split.row(align=True)
    row.operator("preferences.addon_install",
                    icon='IMPORT', text="Install...")
    row.operator("preferences.addon_refresh",
                    icon='FILE_REFRESH', text="Refresh")

    row = layout.row()
    row.prop(prefs.view, "show_addons_enabled_only")
    row.prop(wm, "addon_filter", text="")
    row.prop(wm, "addon_search", text="", icon='VIEWZOOM')

    col = layout.column()

    # set in addon_utils.modules_refresh()
    if addon_utils.error_duplicates:
        box = col.box()
        row = box.row()
        row.label(text="Multiple add-ons with the same name found!")
        row.label(icon='ERROR')
        box.label(text="Delete one of each pair to resolve:")
        for (addon_name, addon_file, addon_path) in addon_utils.error_duplicates:
            box.separator()
            sub_col = box.column(align=True)
            sub_col.label(text=addon_name + ":")
            sub_col.label(text="    " + addon_file)
            sub_col.label(text="    " + addon_path)

    if addon_utils.error_encoding:
        self.draw_error(
            col,
            "One or more addons do not have UTF-8 encoding\n"
            "(see console for details)",
        )

    show_enabled_only = prefs.view.show_addons_enabled_only
    filter = wm.addon_filter
    search = wm.addon_search.lower()
    support = wm.addon_support

    # initialized on demand
    user_addon_paths = []

    for mod, info in addons:
        module_name = mod.__name__

        is_enabled = module_name in used_ext

        if info["support"] not in support:
            continue

        # check if addon should be visible with current filters
        is_visible = (
            (filter == "All") or
            (filter == info["category"]) or
            (filter == "User" and (mod.__file__.startswith(addon_user_dirs)))
        )
        if show_enabled_only:
            is_visible = is_visible and is_enabled

        if is_visible:
            if search and not (
                    (search in info["name"].lower()) or
                    (info["author"] and (search in info["author"].lower())) or
                    ((filter == "All") and (
                        search in info["category"].lower()))
            ):
                continue

            # Skip 2.7x add-ons included with Blender, unless in debug mode.
            is_addon_27x = info.get("blender", (0,)) < (2, 80)
            if (
                    is_addon_27x and
                    (not show_official_27x_addons) and
                    (not mod.__file__.startswith(addon_user_dirs))
            ):
                continue

            # Addon UI Code
            col_box = col.column()
            box = col_box.box()
            colsub = box.column()
            row = colsub.row(align=True)

            row.operator(
                "preferences.addon_expand",
                icon='DISCLOSURE_TRI_DOWN' if info["show_expanded"] else 'DISCLOSURE_TRI_RIGHT',
                emboss=False,
            ).module = module_name

            row.operator(
                "preferences.addon_disable" if is_enabled else "preferences.addon_enable",
                icon='CHECKBOX_HLT' if is_enabled else 'CHECKBOX_DEHLT', text="",
                emboss=False,
            ).module = module_name

            sub = row.row()
            sub.active = is_enabled
            sub.label(text="%s: %s" % (info["category"], info["name"]))

            # use disabled state for old add-ons, chances are they are broken.
            if is_addon_27x:
                sub.label(text="Upgrade to 2.8x required")
                sub.label(icon='ERROR')
            # Remove code above after 2.8x migration is complete.
            elif info["warning"]:
                sub.label(icon='ERROR')

            # icon showing support level.
            sub.label(icon=self._support_icon_mapping.get(
                info["support"], 'QUESTION'))

            # Expanded UI (only if additional info is available)
            if info["show_expanded"]:
                if info["description"]:
                    split = colsub.row().split(factor=0.15)
                    split.label(text="Description:")
                    split.label(text=info["description"])
                if info["location"]:
                    split = colsub.row().split(factor=0.15)
                    split.label(text="Location:")
                    split.label(text=info["location"])
                if mod:
                    split = colsub.row().split(factor=0.15)
                    split.label(text="File:")
                    split.label(text=mod.__file__, translate=False)
                if info["author"]:
                    split = colsub.row().split(factor=0.15)
                    split.label(text="Author:")
                    split.label(text=info["author"], translate=False)
                if info["version"]:
                    split = colsub.row().split(factor=0.15)
                    split.label(text="Version:")
                    split.label(text=".".join(str(x)
                                for x in info["version"]), translate=False)
                if info["warning"]:
                    split = colsub.row().split(factor=0.15)
                    split.label(text="Warning:")
                    split.label(text="  " + info["warning"], icon='ERROR')

                user_addon = USERPREF_PT_addons.is_user_addon(
                    mod, user_addon_paths)
                tot_row = bool(info["doc_url"]) + bool(user_addon)

                if tot_row:
                    split = colsub.row().split(factor=0.15)
                    split.label(text="Internet:")
                    sub = split.row()
                    if info["doc_url"]:
                        sub.operator(
                            "wm.url_open", text="Documentation", icon='HELP',
                        ).url = info["doc_url"]
                    # Only add "Report a Bug" button if tracker_url is set
                    # or the add-on is bundled (use official tracker then).
                    if info.get("tracker_url"):
                        sub.operator(
                            "wm.url_open", text="Report a Bug", icon='URL',
                        ).url = info["tracker_url"]
                    elif not user_addon:
                        addon_info = (
                            "Name: %s %s\n"
                            "Author: %s\n"
                        ) % (info["name"], str(info["version"]), info["author"])
                        props = sub.operator(
                            "wm.url_open_preset", text="Report a Bug", icon='URL',
                        )
                        props.type = 'BUG_ADDON'
                        props.id = addon_info

####添加打开文件夹按钮
                if user_addon:
                    sub.operator(
                        "preferences.addon_remove", text="Remove", icon='CANCEL',
                    ).module = mod.__name__
                sub.alert = True
                sub.operator('wm.path_open',text = '打开脚本').filepath = mod.__file__
                DIRNAME, FILENAME = os.path.split(mod.__file__)

                # IDNAME = os.path.splitext(FILENAME)[0]
                # sub.label(text=DIRNAME)
                sub.operator('wm.path_open',icon = 'FILEBROWSER',text='').filepath = DIRNAME

                # Show addon user preferences
                if is_enabled:
                    addon_preferences = prefs.addons[module_name].preferences
                    if addon_preferences is not None:
                        draw = getattr(addon_preferences, "draw", None)
                        if draw is not None:
                            addon_preferences_class = type(
                                addon_preferences)
                            box_prefs = col_box.box()
                            box_prefs.label(text="Preferences:")
                            addon_preferences_class.layout = box_prefs
                            try:
                                draw(context)
                            except:
                                import traceback
                                traceback.print_exc()
                                box_prefs.label(
                                    text="Error (see console)", icon='ERROR')
                            del addon_preferences_class.layout

    # Append missing scripts
    # First collect scripts that are used but have no script file.
    module_names = {mod.__name__ for mod, info in addons}
    missing_modules = {ext for ext in used_ext if ext not in module_names}

    if missing_modules and filter in {"All", "Enabled"}:
        col.column().separator()
        col.column().label(text="Missing script files")

        module_names = {mod.__name__ for mod, info in addons}
        for module_name in sorted(missing_modules):
            is_enabled = module_name in used_ext
            # Addon UI Code
            box = col.column().box()
            colsub = box.column()
            row = colsub.row(align=True)

            row.label(text="", icon='ERROR')

            if is_enabled:
                row.operator(
                    "preferences.addon_disable", icon='CHECKBOX_HLT', text="", emboss=False,
                ).module = module_name

            row.label(text=module_name, translate=False)

def maximize():

    if get_prefs().maximize_prefs:
        # print(f'开启插件{module_name}最大化显示')

        # print('mengxin_tool')
        bpy.types.USERPREF_PT_addons.draw = 插件面板
        # print(f'当前的  {bpy.types.USERPREF_PT_addons.draw}')
        # print(f'用于重写的 {emm}')

    else:
        # print(f'关闭插件{module_name}最大化显示')
        # print(US.draw)
        if get_prefs().prefs_draw_emm:
            try:
                bpy.types.USERPREF_PT_addons.draw = draw_emm
            except Exception as e:
                print(e.args)
                bpy.types.USERPREF_PT_addons.draw = USERPREF
        else:
            bpy.types.USERPREF_PT_addons.draw = USERPREF

        # print(f'当前的  {bpy.types.USERPREF_PT_addons.draw}')
        # print(f'用于重写的 {USERPREF}')
