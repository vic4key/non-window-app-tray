import time
import PySimpleGUI as sg
from psgtray import SystemTray
from base import APP_ICON

class Tray:
    def __init__(self, worker):
        self.worker = worker
        self.window = None
        self.tray = None

    def run(self):
        layout = [[sg.T('Empty Window', key='-T-')]]
        menu = ['', ['Information', 'Exit']]
        description = "Non-Window Application with System Tray @ Vic P."
        self.window = sg.Window('Window Title', layout, finalize=True, enable_close_attempted_event=True, alpha_channel=0)
        self.window.hide()
        self.tray = SystemTray(menu, single_click_events=False, window=self.window, tooltip=description, icon=APP_ICON, key='-TRAY-')
        self.worker.start()
        while True:
            event, values = self.window.read()
            if event == self.tray.key:
                event = values[event]
            if event in (sg.WIN_CLOSED, 'Exit'):
                self.worker.stop()
                time.sleep(1)
                break
            if event == 'Information':
                self.tray.show_message(title="Information", message=description)
            else:
                self.tray.show_message(title=event, message=event)
        self.tray.close()
        self.window.close() 