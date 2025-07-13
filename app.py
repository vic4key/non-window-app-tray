import os, logging
from tray import Tray
from looper import Looper
from base import CURRENT_DIRECTORY

# Setup logging

logging.basicConfig(
    level=logging.INFO,
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
    delay = 1.0
    if temp := os.environ.get("MAIN_LOOP_TIME"):
        try: delay = float(temp)
        except Exception: pass
    looper = Looper(interval=delay)
    app = Tray(looper)
    app.run()

if __name__ == '__main__':
    main()
