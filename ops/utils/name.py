from bpy.props import StringProperty, BoolProperty, EnumProperty
import bpy

import re
def generate_name(name,前缀,后缀):
    return 前缀+name+后缀
    
def match_name(name,前缀,后缀): #匹配名称
    pattern = 前缀+r'.+'+后缀    
    return re.findall(pattern=pattern,string=name)

def get_infix(name,前缀,后缀):
    name = str(name)
    name = name.split(前缀)[1]
    return name.split(后缀)[0]