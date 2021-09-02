from bpy.utils import register_class, unregister_class


pr = False #print_re_info True or False
reg = (
    
)

def register():

    for i in reg:
        register_class(i)
    if pr:print('re_ui')

def unregister():

    for i in reg:
        unregister_class(i)

    if pr:print('un_re_ui')

if __name__ == "__main__":
    register()