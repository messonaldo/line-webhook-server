from flask import Flask, request
import logging

app = Flask(__name__)

# ✅ 啟用 logging 到 stdout（Render Logs 可看）
logging.basicConfig(level=logging.INFO)

@app.route("/webhook", methods=["POST"])
def webhook():
    raw_body = request.get_data(as_text=True)
    
    logging.info("===== 原始 Webhook 內容 =====")
    logging.info(raw_body)
    logging.info("=============================")
    
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
