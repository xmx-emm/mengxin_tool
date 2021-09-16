import bpy
obj = bpy.context.object

obj.display_type = 'TEXTURED'
obj.show_bounds = False
obj.display_bounds_type = 'CAPSULE'
obj.show_name = False
obj.show_axis = False
obj.show_wire = False
obj.show_all_edges = False
obj.show_texture_space = False
obj.display.show_shadows = False
obj.show_in_front = False
obj.color = (0.0, 1.0, 0.6139969825744629, 1.0)
