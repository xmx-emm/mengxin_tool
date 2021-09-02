from . import panel, pies ,test


pr = False #print_re_info True or False
reg = (panel,
        pies,
        test
)

def register():

    for i in reg:
        i.register()
    if pr:print('re_ui')

def unregister():

    for i in reg:
        i.unregister()

    if pr:print('un_re_ui')

if __name__ == "__main__":
    register()