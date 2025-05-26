from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    body = request.get_json()
    
    # ✅ 加入這一行來印出 userId
    print("📩 收到 LINE 事件：")
    print(body)  # ✅ 顯示完整 JSON 結構

    return "OK"

app.run(host="0.0.0.0", port=5000)
