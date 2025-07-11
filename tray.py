import time
import PySimpleGUI as sg
from psgtray import SystemTray

class Tray:
    def __init__(self, worker):
        self.worker = worker
        self.window = None
        self.tray = None

    def run(self):
        layout = [[sg.T('Empty Window', key='-T-')]]
        menu = ['', ['About', 'Exit']]
        self.window = sg.Window('Window Title', layout, finalize=True, enable_close_attempted_event=True, alpha_channel=0)
        self.window.hide()
        self.tray = SystemTray(menu, single_click_events=False, window=self.window, tooltip='Tooltip', icon=sg.DEFAULT_BASE64_ICON, key='-TRAY-')
        self.worker.start()
        while True:
            event, values = self.window.read()
            if event == self.tray.key:
                event = values[event]
            if event in (sg.WIN_CLOSED, 'Exit'):
                self.worker.stop()
                time.sleep(1)
                break
            if event == 'About':
                self.tray.show_message(title="About", message="This is a non-window app tray @ Vic P.")
            else:
                self.tray.show_message(title=event, message="This is a non-window app tray @ Vic P.")
        self.tray.close()
        self.window.close() 