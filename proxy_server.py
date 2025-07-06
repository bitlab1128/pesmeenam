from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/price/<symbol>')
def price(symbol):
    try:
        r = requests.get(f"https://api.deepcoin.com/v1/market/ticker?symbol={symbol}", timeout=5)
        return jsonify(r.json())
    except Exception as e:
        return jsonify({"code": -1, "error": str(e)})

import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
