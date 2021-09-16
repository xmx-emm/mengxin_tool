import bpy
obj = bpy.context.object

obj.display_type = 'TEXTURED'
obj.show_bounds = False
obj.display_bounds_type = 'CAPSULE'
obj.show_name = True
obj.show_axis = True
obj.show_wire = True
obj.show_all_edges = True
obj.show_texture_space = True
obj.display.show_shadows = True
obj.show_in_front = True
obj.color = (0.0, 1.0, 0.6139969825744629, 1.0)
