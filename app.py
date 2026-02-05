from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_TX = "https://sunwinsaygex-production.up.railway.app/api/sun"

@app.route("/", methods=["GET"])
def home():
    return "Zalo webhook is running"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json

    # Gọi API Tài Xỉu
    try:
        r = requests.get(API_TX, timeout=10)
        tx = r.json()
    except:
        tx = {"error": "API TX lỗi"}

    # Trả dữ liệu cho Zalo
    return jsonify({
        "text": f"""🎲 DỰ ĐOÁN TÀI XỈU
Phiên: {tx.get('phien_hien_tai')}
Dự đoán: {tx.get('du_doan')}
Độ tin cậy: {tx.get('do_tin_cay')}%
Chi tiết: {tx.get('chi_tiet')}
"""
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
