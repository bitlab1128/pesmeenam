from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/price/<symbol>')
def price(symbol):
    try:
        url = f"https://api.deepcoin.com/v1/market/ticker?symbol={symbol}"
        r = requests.get(url, timeout=5)

        if not r.text.strip():
            return jsonify({"code": -2, "error": "Empty response from Deepcoin"})

        return jsonify(r.json())
    except Exception as e:
        return jsonify({"code": -1, "error": str(e)})

# ✅ 포트 8080으로 실행 (Fly.io 요구사항)
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
