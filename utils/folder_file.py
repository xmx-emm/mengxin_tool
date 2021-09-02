import os

def open_folder(path):
    import platform
    import subprocess

    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        os.system('xdg-open "%s" %s &' % (path, "> /dev/null 2> /dev/null"))  # > sends stdout,  2> sends stderr
# import os

# DIRNAME, FILENAME = os.path.split(__file__)
# IDNAME = os.path.splitext(FILENAME)[0]


# print(os.path.split(__file__))
# print(FILENAME)
# print(IDNAME)
