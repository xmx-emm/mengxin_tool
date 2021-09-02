# import bpy
# import traceback
# from ...utils.registration import get_emm_name, uprefs
# # from ...utils.registration import uprefs
# DBG=False
# UPREFS = 'USER_PREFERENCES'
# draw_addons_default = None


# def tag_redraw_windows(area=None, region=None):
#     wm = bpy.context.window_manager
#     if not wm:
#         return True

#     for w in wm.windows:
#         for a in w.screen.areas:
#             if area is None or a.type == area or \
#                     area == UPREFS and not a.type:
#                 for r in a.regions:
#                     if region is None or r.type == region:
#                         r.tag_redraw()

#     return True


# def tag_redraw(all=False):
#     if all:
#         tag_redraw_windows()
#     else:
#         tag_redraw_windows(UPREFS, 'WINDOW')


# def draw_addons_maximized(self, context):
#     layout = self.layout

#     if EMMMM_OT_userpref_show.mod != get_emm_name():
#         row = self.layout.row(align=True)
#         row.scale_y = 1.5
#         row.operator(EMMMM_OT_userpref_restore.bl_idname, text="Restore")

#     prefs = uprefs().addons[EMMMM_OT_userpref_show.mod].preferences

#     draw = getattr(prefs, "draw", None)
#     prefs_class = type(prefs)
#     layout = layout.box()
#     prefs_class.layout = layout
#     try:
#         draw(context)
#     except:
#         layout.label(text="Error (see console)")
#     del prefs_class.layout

# class EMMMM_OT_userpref_show(bpy.types.Operator):
#     bl_idname = "emm.userpref_show"
#     bl_label = "User Preferences"
#     bl_options = {'INTERNAL'}

#     mod = None

#     tab: bpy.props.StringProperty(options={'SKIP_SAVE'})
#     addon: bpy.props.StringProperty(options={'SKIP_SAVE'})

#     def execute(self, context):
#         if context.area.type != UPREFS:
#             bpy.ops.screen.userpref_show('INVOKE_DEFAULT')

#         if self.addon:
#             EMMMM_OT_userpref_show.mod = self.addon
#             bpy.types.USERPREF_PT_addons.draw = draw_addons_maximized
#             self.tab = 'ADDONS'

#         else:
#             bpy.types.USERPREF_PT_addons.draw = draw_addons_default

#         if self.tab:
#             uprefs().active_section = self.tab

#         tag_redraw()
#         return {'FINISHED'}


# class EMMMM_OT_userpref_restore(bpy.types.Operator):
#     bl_idname = "emm.userpref_restore"
#     bl_label = "Restore User Preferences Area"

#     def execute(self, context):
#         bpy.types.USERPREF_PT_addons.draw = draw_addons_default
#         return {'FINISHED'}

# def is_userpref_maximized():
#     return bpy.types.USERPREF_PT_addons.draw == draw_addons_maximized

# def get_maximize_prefs(self):
#     return bpy.types.USERPREF_PT_addons.draw == draw_addons_maximized

# def set_maximize_prefs(self, value):
#     if value and not is_userpref_maximized():
#         bpy.ops.emm.userpref_show(addon=get_emm_name())

#     elif not value and is_userpref_maximized():
#         bpy.ops.emm.userpref_restore()


# def register():
#     # bpy.types.UILayout.__getattribute__ = pme_uilayout_getattribute
#     global draw_addons_default
#     draw_addons_default = bpy.types.USERPREF_PT_addons.draw


# def unregister():
#     # bpy.types.UILayout.__getattribute__ = uilayout_getattribute
#     if bpy.types.USERPREF_PT_addons.draw == draw_addons_maximized:
#         bpy.types.USERPREF_PT_addons.draw = draw_addons_default
