from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    raw_body = request.get_data(as_text=True)
    print("===== 原始 Webhook 內容 =====")
    print(raw_body)
    print("=============================")
    return "OK"

app.run(host="0.0.0.0", port=5000)
