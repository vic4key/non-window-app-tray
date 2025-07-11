import threading
import logging
from main import main_init, main_loop, main_exit

class Looper:
    def __init__(self, interval=1.0):
        self.interval = interval
        self._stop_event = threading.Event()
        self.thread = threading.Thread(target=self.run, daemon=True)

    def start(self):
        if not self.thread.is_alive():
            self.thread = threading.Thread(target=self.run, daemon=True)
            self._stop_event.clear()
            self.thread.start()

    def stop(self):
        self._stop_event.set()
        self.thread.join()

    def run(self):
        try:
            main_init()
            while not self._stop_event.is_set():
                try:
                    main_loop()
                except Exception as e:
                    logging.error(f"Error in main_loop: {e}", exc_info=True)
                self._stop_event.wait(self.interval)
        finally:
            try:
                main_exit()
            except Exception as e:
                logging.error(f"Error in main_exit: {e}", exc_info=True) 