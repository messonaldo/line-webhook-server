# main.py
from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Webhook ready!", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    body = request.get_json()
    print("📩 收到 LINE 事件：")
    print(json.dumps(body, indent=2, ensure_ascii=False))  # 印出所有事件內容
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)