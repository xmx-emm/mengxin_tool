import bpy
from bpy.utils import register_class, unregister_class

from . panel import EMM_VIEW3D_PT_N_Panel,Panel_Class
from . ui import append_TOPBAR_MT_editor_menus, append_TEXT_HT_header
from .toolbar import register_注册工具栏,unregister_注销工具栏
from .. utils.registration import get_prefs


def rewrite_ui_更改UI():
    
    ##IF面板是不是一样的，如果不是一样的就改
    for clas in Panel_Class:
        if getattr(bpy.types, clas.bl_idname, False):
            if hasattr(clas, 'bl_category') and clas.bl_category and clas.bl_category != 'Tool':
                unregister_class(clas)
                clas.bl_category = get_prefs().n_panel_name
                register_class(clas)



    register_注册工具栏()

    ## 添加面板
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


def restore_ui_恢复UI():
    bpy.types.TOPBAR_MT_editor_menus.remove(append_TOPBAR_MT_editor_menus)
    bpy.types.TEXT_HT_footer.remove(append_TEXT_HT_header)

    unregister_注销工具栏()

    #删除面板
    from .presets.eevee_passes_presets import unregister as eevee_passes_presets
    from .presets.cycles_passes_presets import unregister as cycles_passes_presets
    from .presets.object_display_presets import unregister as object_display_presets

    eevee_passes_presets()
    cycles_passes_presets()
    object_display_presets()
