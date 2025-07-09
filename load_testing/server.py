
from flask import Flask, request
import time
import random

app = Flask(__name__)





# Simple home route
@app.route("/")
def home():
    time.sleep(2.77)
    return "Hello, this jj home page!"

# Simulated heavy route (CPU + delay)
@app.route("/heavy")
def heavy():
    time.sleep(0.5)  # simulate delay
    return "Heavy processing done"

# Route to simulate random failure
@app.route("/unstable")
def unstable():
    if random.random() < 0.3:
        return "Simulated server error", 500
    return "Success!", 200

# Login route (POST testing)
@app.route("/login", methods=["POST"])
def login():
    data = request.form
    if data.get("username") == "admin" and data.get("password") == "123":
        return "Login successful"
    else:
        return "Unauthorized", 401

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000)

@app.route("/unstable")
def unstable():
    import random
    if random.random() < 0.5:  # 50% chance of failure
        return "Simulated failure", 500
    return "Success!", 200
