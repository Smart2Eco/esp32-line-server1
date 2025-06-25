from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from ESP32 LINE Flask server!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("Received from LINE:", data)
    return jsonify({"status": "received"})
