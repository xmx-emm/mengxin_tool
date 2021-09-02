import bpy
# from ..utils.update import 

from . ui import append_TOPBAR_MT_editor_menus, append_TEXT_HT_header
def rewrite_ui():
    
    from .toolbar import register as toolbar
    toolbar()

    bpy.types.TOPBAR_MT_editor_menus.append(append_TOPBAR_MT_editor_menus)      #顶部标题栏
    bpy.types.TEXT_HT_footer.prepend(append_TEXT_HT_header)                     #文本编辑器底栏


    from .presets.eevee_passes_presets import register as eevee_passes_presets
    from .presets.cycles_passes_presets import register as cycles_passes_presets
    from .presets.object_display_presets import register as object_display_presets
    cycles_passes_presets()
    object_display_presets()
    eevee_passes_presets()

# VIEW3D_PT_shading
# VIEW3D_PT_overlay
# VIEW3D_PT_gizmo_display
# VIEW3D_PT_object_type_visibility


def restore_ui():
    bpy.types.TOPBAR_MT_editor_menus.remove(append_TOPBAR_MT_editor_menus)
    bpy.types.TEXT_HT_footer.remove(append_TEXT_HT_header)

    from .toolbar import unregister as unregister_toolbar
    unregister_toolbar()






    from .presets.eevee_passes_presets import unregister as eevee_passes_presets
    from .presets.cycles_passes_presets import unregister as cycles_passes_presets
    from .presets.object_display_presets import unregister as object_display_presets

    eevee_passes_presets()
    cycles_passes_presets()
    object_display_presets()
