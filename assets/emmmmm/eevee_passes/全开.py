import bpy
vl = bpy.context.view_layer

vl.use_pass_combined = True
vl.use_pass_z = True
vl.use_pass_mist = True
vl.use_pass_normal = True
vl.use_pass_diffuse_direct = True
vl.use_pass_diffuse_color = True
vl.use_pass_glossy_direct = True
vl.use_pass_glossy_color = True
vl.use_pass_cryptomatte_object = True
vl.use_pass_cryptomatte_material = True
vl.use_pass_cryptomatte_asset = True
vl.pass_cryptomatte_depth = 16
vl.use_pass_cryptomatte_accurate = True
vl.use_pass_ambient_occlusion = True
vl.use_pass_shadow = True
vl.use_pass_environment = True
vl.use_pass_emit = True
vl.eevee.use_pass_volume_direct = True
vl.eevee.use_pass_bloom = True
