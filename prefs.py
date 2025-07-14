import os, json, logging
from base import CURRENT_DIRECTORY

__prefs = None

def prefs_update() -> dict:
    global __prefs
    result = {}
    try:
        config_path = os.path.join(CURRENT_DIRECTORY, "prefs/prefs.json")
        if os.path.exists(config_path):
            with open(config_path, "r") as f:
                result = json.load(f)
    except Exception as e:
        result = {}
        logging.exception(repr(e))
    return result

def prefs_get(skeys, default=None):
    global __prefs
    if __prefs is None:
        __prefs = prefs_update()
    assert __prefs, f"Get the preferences failed."
    iter = __prefs
    for idx, key in enumerate(keys := skeys.split(".")):
        if key in iter.keys():
            iter = iter[key]
            if idx == len(keys) - 1:
                return iter
    return default
