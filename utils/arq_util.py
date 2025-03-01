import os

def get_path(relative_path, arquive):
    relative_path = os.path.join(relative_path, arquive)
    path_abs = os.path.abspath(relative_path)
    print(path_abs)
    return path_abs