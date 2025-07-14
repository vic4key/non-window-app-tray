import os
import PySimpleGUI as sg
from common import get_current_directory, data

CURRENT_DIRECTORY = get_current_directory()
BUNDLE_DIRECTORY  = get_current_directory(meipass=True)

APP_ICON = data("app.ico") or sg.DEFAULT_BASE64_ICON
