import threading
from pystray import Icon, Menu, MenuItem
from PIL import Image
from base import APP_ICON, APP_DESCRIPTION
from plyer import notification
import tkinter as tk
from tkinter import messagebox

def ask_yes_no(title, message):
    root = tk.Tk()
    root.withdraw()  # Ẩn cửa sổ chính
    result = messagebox.askyesno(title, message)
    root.destroy()
    return result

class Tray:
    def __init__(self, worker):
        self.icon = None
        self.worker = worker
        self.should_stop = threading.Event()

    def on_information(self, icon, item):
        notification.notify(title="Information", message=APP_DESCRIPTION, timeout=3)

    def on_exit(self, icon, item):
        self.should_stop.set()
        self.worker.stop()
        icon.stop()

    def run(self):
        # Load icon
        image = Image.open(APP_ICON) if APP_ICON else None
        menu = Menu(
            MenuItem('Information', self.on_information),
            MenuItem('Exit', self.on_exit)
        )
        self.icon = Icon("Non-Window App", image, "Non-Window Application with System Tray @ Vic P.", menu)
        self.worker.start()
        self.icon.run()
