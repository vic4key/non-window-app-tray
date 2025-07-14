import os, sys, logging
import PySimpleGUI as sg
from prefs import prefs_get
from tray import Tray
from looper import Looper
from base import CURRENT_DIRECTORY, APP_ICON

# Setup logging

logging_level = logging.DEBUG if prefs_get("debug", False) else logging.ERROR

logging.basicConfig(
    level=logging_level,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[logging.FileHandler("log.log"), logging.StreamHandler()]
)

# Load environment variables

from dotenv import load_dotenv
load_dotenv(os.path.join(CURRENT_DIRECTORY, "prefs/.env"))

if http_proxy := os.environ.get("HTTP_PROXY"):
    os.environ["http_proxy"] = http_proxy
if https_proxy := os.environ.get("HTTPS_PROXY"):
    os.environ["https_proxy"] = https_proxy
os.environ["no_proxy"] = "127.0.0.1,localhost,.local"

# Entry Point

def main():
    # check app running
    try:
        from tendo import singleton
        instance = singleton.SingleInstance()
    except singleton.SingleInstanceException:
        resp = sg.popup_yes_no("The application is already running.\nDo you want to run another instance?", title="Confirmation", icon=APP_ICON)
        if not resp or resp.lower() == "no": sys.exit(0)
    # run app instance
    interval = prefs_get("interval", 1.0)
    looper = Looper(interval=interval)
    app = Tray(looper)
    app.run()

if __name__ == '__main__':
    main()
