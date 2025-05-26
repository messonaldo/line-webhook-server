from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    # 這行強制解析 JSON
    data = request.get_json(force=True)

    print("===== Webhook Triggered =====")
    print(data)  # ✅ 印出完整 JSON 結構
    print("=============================")

    return "OK"

app.run(host="0.0.0.0", port=5000)
