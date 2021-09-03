import bpy

class OBJECT_UL_render_check_slow(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index,):
        obj = item
        if self.layout_type in {'DEFAULT', 'COMPACT'}:
            layout.prop(obj,'name',text = '')
        elif self.layout_type == 'GRID':
            layout.alignment = 'CENTER'
            layout.label(text="emm", icon_value=icon)
