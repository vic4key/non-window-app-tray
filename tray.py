import threading
from PIL import Image
import tkinter as tk
from tkinter import messagebox
from pystray import Icon, Menu, MenuItem
from base import APP_ICON, APP_DESCRIPTION

def ask_yes_no(title, message):
    root = tk.Tk()
    root.withdraw()  # Hide main window
    result = messagebox.askyesno(title, message)
    root.destroy()
    return result

def safe_notify(title, message, timeout=5, app_icon=None):
    def __safe_notify():
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo(title, message)
        root.destroy()
    threading.Thread(target=__safe_notify).start()

class Tray:
    def __init__(self, worker):
        self.worker = worker
        self.tray = None
        self.should_stop = threading.Event()

    def on_information(self, icon, item):
        safe_notify(title="Information", message=APP_DESCRIPTION, timeout=3)

    def on_exit(self, icon, item):
        self.should_stop.set()
        self.worker.stop()
        icon.stop()

    def run(self):
        image = Image.open(APP_ICON) if APP_ICON else None
        menu = Menu(
            MenuItem('Information', self.on_information),
            MenuItem('Exit', self.on_exit),
        )
        self.worker.start()
        self.tray = Icon("Non-Window App", image, APP_DESCRIPTION, menu)
        self.tray.run()
