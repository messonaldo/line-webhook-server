from flask import Flask, request

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        body = request.get_data(as_text=True)
        print("📩 原始內容：")
        print(body)
    except Exception as e:
        print("❌ 錯誤：", e)

    return "OK"

app.run(host="0.0.0.0", port=5000)
