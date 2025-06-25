from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from ESP32 LINE Flask server!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    print("✅ ได้รับข้อมูลจาก LINE:", data)
    return '', 200

if __name__ == '__main__':
    app.run()
