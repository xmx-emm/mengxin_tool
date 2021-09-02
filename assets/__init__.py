# from . import icon,addonTemplates


pr = False #print_re_info True or False
reg = (
    # icon,
    # addonTemplates,
)

def register():

    for i in reg:
        i.register()
    if pr:
        print('re_assets')

def unregister():

    for i in reg:
        i.unregister()

    if pr:
        print('un_re_assets')

if __name__ == "__main__":
    register()