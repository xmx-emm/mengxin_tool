# from ..registration import modify_keymapss as keysdict
# import bpy
# from .registration import get_prefs

# def get_play_space_pie(keylists=[],count=0):
#     keylists.append(keysdict["PLAY_SPACE_PIE"])
#     return keylists,count
# def get_tools_space_pie(keylists=[],count=0):
#     keylists.append(keysdict["TOOLS_SPACE_PIE"])
#     return keylists,count
# def get_search_space_pie(keylists=[],count=0):
#     keylists.append(keysdict["SEARCH_SPACE_PIE"])
#     return keylists,count



# def activate_modify_keymaps(register,items):
#     DEBUG = get_prefs().debug_modify_keymaps

#     # items 是传入的要修改快捷键的 键 ，会自动大写，所以不用
#     keylist = keysdict[items.upper()]
#     if keylist:
            
#         context = bpy.context
#         kc = context.window_manager.keyconfigs.user.keymaps
#         call_list = ("wm.call_menu_pie", "wm.call_menu", "wm.call_panel")
#         for i in keylist:
#             keymap =       i.get("keymap")

#             idname =       i.get("idname")
#             properties =   i.get("properties")

#             type =         i.get("type")
#             value =        i.get("value")
#             shift =        i.get("shift")
#             ctrl =         i.get("ctrl")
#             alt =          i.get("alt")
#             oskey =        i.get("oskey")
#             any =          i.get("any")

#             active =       i.get("active")
#             map_type =     i.get("map_type")
#             repeat =       i.get("repeat")

#             ##get 字典pr属性
#             if properties != None:
#                 a = properties[0]
#                 properties_name = a[1]
#             km = kc.get(keymap)  # get 属性keymap快捷键
#             for kmi in km.keymap_items:

#                 def modify():
#                     # if type           != None: kmi.type               =   type
#                     if value          != None: kmi.value              =   value
#                     if shift          != None: kmi.shift              =   shift
#                     if ctrl           != None: kmi.ctrl               =   ctrl
#                     if alt            != None: kmi.alt                =   alt
#                     if oskey          != None: kmi.oskey              =   oskey
#                     if any            != None: kmi.any                =   any
#                     if active         != None: kmi.active             =   active
#                     # if map_type       != None: kmi.map_type           =   map_type
#                     # if repeat         != None: kmi.repeat             =   repeat

#                 def restore():
#                     if (not kmi.is_user_defined) and kmi.is_user_modified:
#                         km.restore_item_to_default(kmi)     ###重置快捷键项 我的天，弄了好久 重置快捷键的选项，激活还没弄
#                         if active         != None: kmi.active          =   True
#                         print(f'重置被修改快捷键 __{kmi.idname}__')

#                 if kmi.idname == idname:
#                     if kmi.idname in call_list and kmi.idname == idname:
#                         for item in kmi.properties.items():     # 循环 properties的name项
#                             name = item[1]                      # 切片出来 快捷键 properties的name项.name
#                             if name == properties_name:         # 快捷键是调用菜单
#                                 if register:
#                                     # modify()
#                                     kmi.active = False                                    
#                                     print(f'修改调用快捷键 {keymap} {kmi.idname}__{name}')
#                                 else:
#                                     # restore()
#                                     # kmi.active = True
#                                     print(f'还原调用快捷键 {keymap} {kmi.idname}__{name}')

#                     else:
#                         if register:
#                             # modify()
#                             kmi.active = False
#                             print(f'修改快捷键 {keymap} {kmi.idname}')
#                         else:
#                             # restore()
#                             # kmi.active = True
#                             print(f'还原快捷键 {keymap} {kmi.idname}')

# #                     #     else:
                            
# #                     #         if type           != None: kmi.type               =   type
# #                     #         if value          != None: kmi.value              =   value
# #                     #         if shift          != None: kmi.shift              =   shift
# #                     #         if ctrl           != None: kmi.ctrl               =   ctrl
# #                     #         if alt            != None: kmi.alt                =   alt
# #                     #         if oskey          != None: kmi.oskey              =   oskey
# #                     #         if any            != None: kmi.any                =   any
# #                     #         if active         != None: kmi.active             =   active
# #                     #         if map_type       != None: kmi.map_type           =   map_type
# #                     #         if repeat         != None: kmi.repeat             =   repeat
# #                     #         print(f'修改快捷键 __{kmi.idname}__')


#     #         # for k in keymaps:
#     #         #     if k not in startup_keymaps:
#     #         #         startup_keymaps.append(k)

#     #         keylist.clear()
#     #     else:
#     #         print('未获取到快捷键表，已跳过')
#     # else:
#     #     context = bpy.context
#     #     kc = context.window_manager.keyconfigs.user.keymaps
#     #     call_list = ("wm.call_menu_pie", "wm.call_menu", "wm.call_panel")
#     #     print('restore_keymaps')
#     #     # for keylist in keylists:
#     #     #     for i in keylist:
#     #     #         keymap =        i.get("keymap")
#     #     #         idname =        i.get("idname")
#     #     #         properties =    i.get("properties")

#     #     #         active =        i.get("active")

#     #     #         if properties != None:
#     #     #             a = properties[0]  # get 字典pr属性
#     #     #             properties_name = a[1]

#     #     #         km = kc.get(keymap)  # get 属性keymap快捷键
#     #     #         for kmi in km.keymap_items:
#     #     #             if kmi.idname == idname:
#     #     #                 if kmi.properties:
#     #     #                     for item in kmi.properties.items():
#     #     #                         name = item[1]
#     #     #                 if kmi.idname in call_list:
#     #     #                     if name == properties_name:         # 快捷键是调用菜单

#     #     #                         pass
#     #     #         if (not kmi.is_user_defined) and kmi.is_user_modified:
#     #     #             km.restore_item_to_default(kmi)     ###重置快捷键项 我的天，弄了好久 重置快捷键的选项，激活还没弄
#     #     #             if active         != None: kmi.active             =   True
#     #     #             print(f'重置被修改调用快捷键 {kmi.idname}__{name}')

#     #     # else:
#     #     #     if (not kmi.is_user_defined) and kmi.is_user_modified:
#     #     #         km.restore_item_to_default(kmi)     ###重置快捷键项 我的天，弄了好久 重置快捷键的选项，激活还没弄
#     #     #         if active         != None: kmi.active             =   True
#     #     #         print(f'重置被修改快捷键 __{kmi.idname}__')

#     #     # 将从字典中get到的内容弄到快捷键上，如果没有则跳过

#     #     #                     if (not kmi.is_user_defined) and kmi.is_user_modified:
#     #     #                         km.restore_item_to_default(kmi)     ###重置快捷键项 我的天，弄了好久 重置快捷键的选项，激活还没弄
#     #     #                         if active         != None: kmi.active

#     #     #             if DEBUG:print(f'重置快捷键__{idname}__')

#     #     #             if (not kmi.is_user_defined) and kmi.is_user_modified:
#     #     #                 km.restore_item_to_default(kmi)     ###重置快捷键项 我的天，弄了好久 重置快捷键的选项，激活还没弄
#     #     #                 if active         != None: kmi.active             =   True
#     #     # print('----------modify_keymaps------------')

#     # keylist.clear()
# ##启动bl时自动运行的内容

# #判断的内容
# ##播放
