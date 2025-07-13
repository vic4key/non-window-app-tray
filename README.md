# 🚀 Non-Window Application with System Tray

A python boilerplate for a non-window application with a system tray.
It helps you easily and quickly create applications that run in the background. 🚀

## ✨ Features
- 🖥️ Support system tray menu
- 🔄 Easy to extend background logic in `main.py`
- ⚙️ Flexible configuration via `.env`

## License
- 🪪 Released under the [MIT](LICENSE) license
- ©️ Copyright © Vic P. & Vibe Coding ❤️

## 📦 Installation
1. 🐍 Install Python 3
2. 📥 Install dependencies: `pip install -r requirements.txt`

## ▶️ Usage
1. 🛠️ Edit your background logic in `main.py` (`main_init`, `main_loop`, `main_exit`)
2. 📝 (Optional) Update the `.env` file. Eg. `MAIN_LOOP_TIME=3.0` (in seconds) to change the main loop interval.
3. 🏃‍➡️ Run the app: `python3 app.py`

## 🛠️ Packaging
Create a standalone executable: `pyinstaller --clean --distpath=dist app.spec`

## 📬 Contact
Feel free to contact via [Twitter](https://twitter.com/vic4key) / [Gmail](mailto:vic4key@gmail.com) / [Blog](https://blog.vic.onl/) / [Website](https://vic.onl/)
