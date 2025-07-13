import os, sys

def norm_path(path: str, included_last_slash: bool = False):
    s = path.replace("\\", os.path.sep).replace("//", os.path.sep).replace("/", os.path.sep)
    if included_last_slash: s += os.path.sep
    return s

def get_current_directory(meipass: bool = False) -> str:
    """
    Get the current directory.
    If `meipass` is True, get the directory of the executable file.
    """
    result = os.getcwd()
    if meipass:
        try:
            result = sys._MEIPASS
        except:
            result = os.path.abspath(".")
    return norm_path(result)
