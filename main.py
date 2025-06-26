from flask import Flask, request, jsonify

app = Flask(__name__)
latest_command = ""  # เก็บคำสั่งล่าสุดจาก LINE

@app.route('/')
def home():
    return "ESP32 Command Server"

@app.route('/webhook', methods=['POST'])
def webhook():
    global latest_command
    data = request.get_json()
    print("LINE ส่ง:", data)

    try:
        message_text = data['events'][0]['message']['text']
        latest_command = message_text.lower()
    except:
        pass

    return '', 200

@app.route('/command', methods=['GET'])
def get_command():
    return jsonify({'command': latest_command})

@app.route('/ack', methods=['POST'])
def clear_command():
    global latest_command
    latest_command = ""
    return '', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
