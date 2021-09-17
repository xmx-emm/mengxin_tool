import bpy
from bpy.utils import register_class, unregister_class

from . panel import Panel_Class,排除类列表 #EMM_VIEW3D_PT_N_Panel
from . ui import append_TOPBAR_MT_editor_menus, append_TEXT_HT_header
from .toolbar import register_注册工具栏,unregister_注销工具栏
from .tool.render_resolution_switch import render_resolution_switch

def rewrite_ui_更改UI():



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

    register_class(render_resolution_switch)


    ##IF面板是不是一样的，如果不是一样的就改    通过导入Panel_Class
    for name,clas in Panel_Class:
        if clas not in 排除类列表 and clas.bl_idname:
            if getattr(bpy.types, clas.bl_idname, False):
                if hasattr(clas, 'bl_category') and clas.bl_category and clas.bl_category != 'Tool':
                    from .. utils.registration import get_prefs #包含在这里面就可以每次更新
                    unregister_class(clas)
                    clas.bl_category = get_prefs().n_panel_name
                    register_class(clas)


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

    unregister_class(render_resolution_switch)
