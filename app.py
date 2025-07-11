# pyinstaller --onefile --noconsole tray.py

import os
from dotenv import load_dotenv
import logging
from looper import Looper
from tray import Tray

# Load environment variables
load_dotenv()
if http_proxy := os.environ.get("HTTP_PROXY"):
    os.environ["http_proxy"] = http_proxy
if https_proxy := os.environ.get("HTTPS_PROXY"):
    os.environ["https_proxy"] = https_proxy
os.environ["no_proxy"] = "127.0.0.1,localhost,.local"

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()]
)

def main():
    delay = 1.0
    if __delay := os.environ.get("MAIN_LOOP_TIME"):
        try:
            delay = float(__delay)
        except Exception:
            pass
    looper = Looper(interval=delay)
    app = Tray(looper)
    app.run()

if __name__ == '__main__':
    main()
